# -*- coding: utf-8 -*-

# python imports
from random import randint
from functools import wraps
from mongoengine import StringField, IntField, DoesNotExist, \
    ValidationError, EmbeddedDocument, EmbeddedDocumentListField

# flask imports
from flask import request, jsonify, g, current_app

# project imports
from application.models import BaseDocument
from application.extensions import redis, email
from application.utils.localize import localize
from application.utils.hashing import hash_password, generate_token


class Permission(EmbeddedDocument):

    # mark: constants

    ACCESS_NONE = 0
    ACCESS_READ = 1
    ACCESS_WRITE = 2

    # mark: variables

    name = StringField(required=True)
    access_level = IntField(required=True, default=ACCESS_NONE)

    sub_permissions = EmbeddedDocumentListField("Permission")

    # mark: json functions

    def to_json(self):
        return {
            'name': self.name,
            'access_level': self.access_level,
            'sub_permissions': [permission.to_json() for permission in self.sub_permissions]
        }

    def populate(self, json):
        self.name = json['name']
        self.access_level = json['access_level']
        if 'sub_permissions' in json:
            self.sub_permissions = Permission.\
                create_permission_list(json['sub_permissions'], self.access_level)

    # mark: class functions

    @classmethod
    def create_permission_list(cls, list, parent_access_level=ACCESS_NONE):
        permissions = []
        for json in list:
            permission = Permission()
            permission.populate(json)
            permission.access_level = max(permission.access_level, parent_access_level)
            permissions.append(permission)
        return permissions


class Admin(BaseDocument):

    # mark: variables

    username = StringField(required=True, unique=True)

    name = StringField(required=True, default="")
    email = StringField(required=True, default="")

    password = StringField(required=True, default="-")
    secret_key = StringField(required=True, default="_")

    permissions = EmbeddedDocumentListField(Permission)

    # mark: meta

    meta = {
        'collection': 'admins',
        'indexes': [
            'username'
        ]
    }

    # mark: json functions

    def to_json(self):
        """
        @apiDefine AdminToJson

        @apiSuccess (Success Response) {String} id Id of admin
        @apiSuccess (Success Response) {String} name Name of admin
        @apiSuccess (Success Response) {String} email Email of admin
        @apiSuccess (Success Response) {String} username Username of admin
        @apiSuccess (Success Response) {Permission[]} permissions Permissions of admin
        @apiSuccess (Success Response) {String} [permissions.name] Name of permission
        @apiSuccess (Success Response) {String} [permissions.access_level]
            Access level of permission (None=0, Read=1, Write=2)
        @apiSuccess (Success Response) {Permission[]} [permissions.sub_permissions]
            Sub permissions of permission
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'username': self.username,
            'permissions': [permission.to_json() for permission in self.permissions]
        }

    def populate(self, json):
        if 'name' in json:
            self.name = json['name']
        if 'email' in json:
            self.email = json['email'].lower()
        if 'username' in json:
            self.username = json['username']
        if 'password' in json:
            self.password = hash_password(json['password'])
        if 'permissions' in json:
            self.permissions = Permission.create_permission_list(json['permissions'])

    # mark: manage users

    @classmethod
    def create_first_user(cls, reset=False):
        json = current_app.config['DEFAULT_ADMIN']
        try:
            admin = Admin.objects.get(username=json['username'])
            if not reset:
                return
        except (DoesNotExist):
            admin = Admin()
        admin.populate(json)
        admin.secret_key = '_'
        admin.save()

    # mark: activation

    def consume_activation_code(self, code):
        key = 'aac:%s' % self.username
        if redis.exists(key) and redis.get(key).decode() == code:
            redis.delete(key)
            return True
        return False

    def send_activation_code(self):
        key = 'aac:%s' % self.username
        if redis.exists(key):
            redis.delete(key)

        code = str(randint(0, 9999)).zfill(4)
        if current_app.config['DEFAULT_ACTIVATE_CODE_ON']:
            code = current_app.config['DEFAULT_ACTIVATE_CODE']

        redis.setex(key, current_app.config['ACTIVATION_CODE_TIMEOUT'], code)
        email.send(
            self.email,
            self.name,
            localize('your_activation_code_title'),
            localize('your_activation_code_message') % code,
        )
        return code

    # mark: authentication flow

    def generate_secret_key(self):
        key = generate_token()
        self.add_secret_key_to_redis(key)
        return key

    def add_secret_key_to_redis(self, key):
        redis.setex('ask:%s' % key, current_app.config['ADMIN_SECRET_KEY_TIMEOUT'], self.username)

    def get_access_level(self, permission_name, sub_permission_name):
        for permission in self.permissions:
            if permission.name == permission_name:
                access_level = permission.access_level
                for sub_permission in permission.sub_permissions:
                    if sub_permission.name == sub_permission_name \
                            and sub_permission.access_level > access_level:
                        access_level = sub_permission.access_level
                return access_level
        return Permission.ACCESS_NONE

    @classmethod
    def authenticate(cls, permission=None, sub_permission=None, level=Permission.ACCESS_NONE):
        """
        If admin authenticated correctly then g.user value will be filled with admin mongodb obj
        other wise it will abort request with 401 unauthorised http response code

        @apiDefine SecretKeyHeader
        @apiHeader {String} Secret-Key Admin Request - Secret key for admin to use special APIs
        """
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                authentication_result = Admin.check_authentication(
                    permission_name=permission,
                    sub_permission_name=sub_permission,
                    need_access_level=level
                )
                if authentication_result == 200:
                    return f(*args, **kwargs)
                return authentication_result
            return wrapper
        return decorator

    @classmethod
    def check_authentication(cls, permission_name=None, sub_permission_name=None,
                             need_access_level=Permission.ACCESS_NONE):
        try:
            secret_key = request.headers.get('Secret-Key')
            assert secret_key

            admin = Admin.get_admin_by_secret_key(secret_key)
            assert admin

            access_level = admin.get_access_level(permission_name, sub_permission_name)
            if access_level < need_access_level:
                return jsonify(message_en=localize('insufficient_access_level_error')), 401

            g.user = admin
            g.user_type = 'admin'
            return 200
        except (DoesNotExist, ValidationError, AssertionError):
            return jsonify(message_en=localize('invalid_token_error')), 401

    @classmethod
    def get_admin_by_secret_key(cls, secret_key):
        try:
            username = redis.get('ask:%s' % secret_key)
            assert username
            return cls.objects.get(username=username.decode())
        except (DoesNotExist, ValidationError, AssertionError):
            return None
