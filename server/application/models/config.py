# -*- coding: utf-8 -*-

# python imports
from mongoengine import Document, DictField, StringField, DoesNotExist


class Config(Document):

    # mark: variables

    key = StringField(primary_key=True, required=True)
    value = DictField(default={}, required=True)

    # mark: meta

    meta = {
        'collection': 'configs'
    }

    # mark: getter setter

    def get(self, key, default=None):
        return self.value.get(key, None)

    def set(self, key, value):
        self.value[key] = value
        self.save()

    @classmethod
    def get_config(cls, key):
        try:
            return Config.objects.get(key=key)
        except DoesNotExist:
            config = Config()
            config.key = key
            return config

    @classmethod
    def set_config(cls, key, value):
        try:
            config = Config.objects.get(key=key)
            config.value = value
            config.save()
            return config
        except DoesNotExist:
            config = Config()
            config.key = key
            config.value = value
            config.save()
            return config

    # mark: json functions

    def to_json(self):
        return {self.key: self.value}
