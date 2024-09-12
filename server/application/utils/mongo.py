# -*- coding: utf-8 -*-

# python imports
from mongoengine.connection import disconnect, connect

# flask imports
from flask import current_app as app

# project imports
from application.utils.random_generator import random_string


def db_connect(prefix):
    alias = '%s_%s' % (prefix, random_string(length=8))
    connection = connect(alias=alias, **app.config['MONGODB_SETTINGS'])
    return [connection, alias]


def db_disconnect(alias=None):
    if not alias:
        disconnect()
    else:
        disconnect(alias)
