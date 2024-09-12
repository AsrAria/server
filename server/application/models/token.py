# -*- coding: utf-8 -*-

# flask imports
from application.extensions import redis
from mongoengine import Document, StringField, ReferenceField

# project imports
from application.models import User
from application.utils.hashing import generate_token


class Token(Document):

    # mark: variables

    user = ReferenceField(User, required=True)

    access_token = StringField(request=True)
    refresh_token = StringField(request=True)

    # mark: meta

    meta = {
        'collection': 'tokens',
        'indexes': [
            'access_token',
            'refresh_token'
        ]
    }

    # mark: controll functions

    @classmethod
    def create(cls, user):
        access_token = user.generate_access_token()
        refresh_token = generate_token()
        token = Token(
            user=user,
            access_token=access_token,
            refresh_token=refresh_token
        )
        token.save()
        return token

    @classmethod
    def revoke(cls, access_token):
        # Warning! deleting data from mongodb does
        # not reclaim space you should do it manually
        cls.objects(access_token=access_token).delete()
        redis.delete('uat:%s' % access_token)

    @classmethod
    def revoke_all(cls, user_obj):
        # Warning! deleting data from mongodb does
        # not reclaim space you should do it manually
        tokens_obj = cls.objects(user=user_obj)
        for token_obj in tokens_obj:
            redis.delete('uat:%s' % token_obj.access_token)
        tokens_obj.delete()
