# -*- coding: utf-8 -*-

# python imports
from uuid import uuid4
from mongoengine import Document, \
    EmbeddedDocument, StringField, DateTimeField

# project imports
from application.utils.time import create_datetime


class BaseDocument(Document):

    # mark: variables

    create_time = DateTimeField(required=True)
    id = StringField(required=True, primary_key=True)

    # mark: meta

    meta = {
        'abstract': True,
        'allow_inheritance': True,
        'indexes': [
            'id',
            '-create_time',
        ],
        'ordering': ['-create_time']
    }

    # mark: override functions

    def save(self, *args, **kwargs):
        self.populate_base_fields()
        super(BaseDocument, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        super(BaseDocument, self).update(*args, **kwargs)

    def populate_base_fields(self):
        if self.id is None:
            self.id = str(uuid4())
        if self.create_time is None:
            self.create_time = create_datetime()


class BaseEmbeddedDocument(EmbeddedDocument):

    # mark: variables

    id = StringField(required=True)

    # mark: meta

    meta = {
        'allow_inheritance': True
    }

    # mark: json functions

    def base_populate(self):
        if self.id is None:
            self.id = str(uuid4())
