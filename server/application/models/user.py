# -*- coding: utf-8 -*-

# python imports
from random import randint
from functools import wraps

# flask imports
from flask import request, jsonify, g, current_app
from mongoengine import StringField, DoesNotExist, IntField, BooleanField, ValidationError

# project imports
from application.models import BaseDocument
from application.extensions import redis, email
from application.utils.hashing import hash_password, generate_token, generate_small_token
from application.utils.localize import localize


class User(BaseDocument):

    # mark: constants

    ROLE_PERSON = 0
    ROLE_PSYCHIATRIST = 1
    ROLE_ORGANIZATION = 2

    # mark: variables

    role = IntField(required=True, default=ROLE_PERSON)

    email = StringField(unique=True, required=True)
    password = StringField(required=True, default="-")

    is_active = BooleanField(required=True, default=False)

    is_enable = BooleanField(required=True, default=True)
    is_profile_updated = BooleanField(required=True, default=False)

    # mark: meta

    meta = {
        'collection': 'users',
        'allow_inheritance': True,
        'indexes': [
            'role',
            'email'
        ],
    }

    # mark: json functions

    def to_json(self, details=False):
        """
        @apiDefine UserToJson

        @apiSuccess (Success Response) {String} id User id
        @apiSuccess (Success Response) {String} role User role
        @apiSuccess (Success Response) {String} email User email
        @apiSuccess (Success Response) {Boolean} [is_active] Is the user active?
        @apiSuccess (Success Response) {Boolean} [is_enable] Is the user enable?
        @apiSuccess (Success Response) {Boolean} [is_profile_updated]
            Has the user profile been updated?
        """
        dic = {
            'id': self.id,
            'role': self.role,
            'email': self.email
        }
        if g.user_type == 'admin' or (g.user_type == 'user' and g.user.id == self.id) or details:
            dic['is_profile_updated'] = self.is_profile_updated
        if g.user_type == 'admin':
            dic['is_active'] = self.is_active
            dic['is_enable'] = self.is_enable
        return dic

    def populate(self, json):
        if 'role' in json:
            self.role = json['role']
        if 'email' in json:
            self.email = json['email'].lower()
        if 'password' in json:
            self.password = hash_password(json['password'])

    # mark: helper functions

    def get_image_path(self):
        return 'user/image/%s/%s/%s' % (self.id[0], self.id[1], self.id[2])

    def get_attachment_path(self):
        return 'user/attachment/%s/%s/%s' % (self.id[0], self.id[1], self.id[2])

    # mark: create or update

    @classmethod
    def create(cls, json):
        try:
            User.objects.get(email=json['email'].lower())
            return None
        except DoesNotExist:
            if json['role'] == User.ROLE_PERSON:
                from application.models import Person
                user = Person()
            if json['role'] == User.ROLE_PSYCHIATRIST:
                from application.models import Psychiatrist
                user = Psychiatrist()
            if json['role'] == User.ROLE_ORGANIZATION:
                from application.models import Organization
                user = Organization()

            user.update(json)
            return user

    def update(self, json):
        self.populate(json)
        self.save()

    # mark: activation

    def consume_activation_code(self, code):
        key = 'uac:%s' % self.id
        if redis.exists(key) and redis.get(key).decode() == code:
            redis.delete(key)
            return True
        return False

    def send_activation_code(self):
        key = 'uac:%s' % self.id
        if redis.exists(key):
            redis.delete(key)

        code = str(randint(0, 9999)).zfill(4)
        if current_app.config['DEFAULT_ACTIVATE_CODE_ON']:
            code = current_app.config['DEFAULT_ACTIVATE_CODE']

        redis.setex(key, current_app.config['ACTIVATION_CODE_TIMEOUT'], code)
        email.send(
            self.email,
            "",
            localize('your_activation_code_title'),
            localize('your_activation_code_message') % code,
        )
        return code

    # mark: manage password

    def send_recover_password_token(self):
        token = generate_small_token()
        redis.setex(
            'urpt:%s' % token,
            current_app.config['FORGET_PASSWORD_TOKEN_TIMEOUT'],
            self.id
        )
        address = current_app.config['RECOVER_PASSWORD_URL'] + "?token=" + token
        email.send(
            self.email,
            "",
            localize('recover_passsword_title'),
            localize('recover_passsword_message') % address,
        )
        return token

    @classmethod
    def consume_recover_password_token(cls, token):
        key = 'urpt:%s' % token
        if redis.exists(key):
            id = redis.get(key)
            redis.delete(key)
            return User.objects.get(id=id.decode())
        return None

    # mark: authenticaton

    def generate_access_token(self):
        token = generate_token()
        self.add_access_token_to_redis(token)
        return token

    def add_access_token_to_redis(self, token):
        redis.setex('uat:%s' % token, current_app.config['ACCESS_TOKEN_TIMEOUT'], self.id)

    @classmethod
    def authenticate(cls, f):
        """
        If user authenticated correctly then g.user value will be filled with user mongodb obj
        other wise it will abort request with 401 unauthorised http response code

        @apiDefine AccessTokenHeader
        @apiHeader {String} Access-Token User Request -
            Access token given after activation and refreshing
        """
        @wraps(f)
        def wrapper(*args, **kwargs):
            authentication_result = User.check_authentication()
            if authentication_result == 200:
                return f(*args, **kwargs)
            return authentication_result
        return wrapper

    @classmethod
    def check_authentication(cls):
        try:
            access_token = request.headers.get('Access-Token')
            assert access_token

            user = User.get_user_by_access_token(access_token)
            assert user

            if not user.is_enable:
                return jsonify(
                    type='user_disable',
                    message_en=localize('your_account_is_disabled_error')
                ), 403

            g.user = user
            g.user_type = 'user'
            return 200
        except (DoesNotExist, ValidationError, AssertionError):
            return jsonify(message_en=localize('not_have_access_error')), 401

    @classmethod
    def get_user_by_access_token(cls, access_token):
        try:
            id = redis.get('uat:%s' % access_token)
            assert id
            return cls.objects.get(id=id.decode())
        except (DoesNotExist, ValidationError, AssertionError):
            return None
