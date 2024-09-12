# -*- coding: utf-8 -*-

# python imports
import os


class DefaultConfig(object):

    # api configs

    API_VERSION = 1
    SITE_NAME = 'Psykon'

    # deployment configs

    DEBUG = True
    TESTING = True
    DEPLOYMENT = False

    # mongo db configs

    MONGODB_SETTINGS = {
        'db': 'psykon',
        'host': '0.0.0.0',
        'port': 27017
    }
    if 'MONGODB_DB_NAME' in os.environ:
        MONGODB_SETTINGS['db'] = os.environ['MONGODB_DB_NAME']
    if 'MONGODB_HOST' in os.environ:
        MONGODB_SETTINGS['host'] = os.environ['MONGODB_HOST']
    if 'MONGODB_PORT' in os.environ:
        MONGODB_SETTINGS['port'] = os.environ['MONGODB_PORT']
    if 'MONGODB_USERNAME' in os.environ and os.environ['MONGODB_USERNAME'] != "":
        MONGODB_SETTINGS['username'] = os.environ['MONGODB_USERNAME']
    if 'MONGODB_PASSWORD' in os.environ and os.environ['MONGODB_PASSWORD'] != "":
        MONGODB_SETTINGS['password'] = os.environ['MONGODB_PASSWORD']
    if 'MONGODB_AUTHENTICATION_SOURCE' in os.environ \
       and os.environ['MONGODB_AUTHENTICATION_SOURCE'] != "":
        MONGODB_SETTINGS['authentication_source'] = os.environ['MONGODB_AUTHENTICATION_SOURCE']

    CURRENT_VERSION = 1

    # redis db configs

    REDIS_URL = "redis://0.0.0.0:6379/0"
    if 'REDIS_URL' in os.environ:
        REDIS_URL = os.environ['REDIS_URL']

    # code configs

    ENABLE_API_VERSIONS = {
        'v1': [
            'main',
            'admin',
            'user',
            'person',
            'psychiatrist',
            'organization',
            'meeting',
            'payment'
        ]
    }

    INSTALLED_EXTENSIONS = (
        'db',
        'json',
        'redis',
        'magic',
        'limiter',
        'email',
        'paypal',
    )

    HEALTH_CHECK_COMPONENTS = [
        'mongo',
        'redis'
    ]

    # directory configs

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    JSONSCHEMA_DIR = os.path.join(BASE_DIR, 'jsonschema')

    TEMP_DIR = os.path.join(BASE_DIR, 'tmp')
    VOLUME_DIR = os.path.abspath(os.environ.get('VOLUME_DIR', TEMP_DIR))
    FILE_UPLOAD_DIR = os.environ.get('FILE_UPLOAD_DIR', os.path.join(VOLUME_DIR, 'upload'))

    # pagination configs

    PAGE_SIZE = 10

    # email configs

    EMAIL_ON = False

    EMAIL_SETTINGS = {
        'sender_name': 'Psykon',
        'sender_address': 'hello@psykon.ca',
        'address': 'https://api.sendgrid.com/v3/mail/send',
        'api_key': 'Bearer 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',
        'limit': 2000,
        'timeout': 30,
    }

    # authentication config

    DEFAULT_ACTIVATE_CODE_ON = True
    DEFAULT_ACTIVATE_CODE = '6732'

    ACTIVATION_CODE_TIMEOUT = 5 * 60
    FORGET_PASSWORD_TOKEN_TIMEOUT = 15 * 60 * 60

    ADMIN_SECRET_KEY_TIMEOUT = 7 * 24 * 60 * 60
    ACCESS_TOKEN_TIMEOUT = 20 * 365 * 24 * 60 * 60

    # flask form config

    WTF_CSRF_ENABLED = False
    MAGIC_ALLOWED_EXTENSIONS = {
        'image': ['jpg', 'jpeg', 'png']
    }

    # initial application data

    DEFAULT_ADMIN = {
        'username': 'admin',
        'password': 'admin123',
        'email': 'ppsykon@gmail.com',
        'permissions': [
            {
                'name': 'admin',
                'access_level': 2,
                'sub_permissions': []
            }
        ]
    }

    # limiter configs

    RATELIMIT_ENABLED = False
    RATELIMIT_STORAGE_URL = REDIS_URL

    # website config

    RECOVER_PASSWORD_URL = "https://panel-dev.psykon.ca/setPassword"

    # jitsi config

    JITSI = {
        'key': 'PKN14xDCzuiyU6WzcC201xaisNYGCMeriQaks',
        'app_name': 'psykon',
        'host': 'meeting.psykon.ca'
    }

    # paypal config

    PAY_PAL_CONFIG = {
        'urls': {
            'oauth': 'https://api.sandbox.paypal.com/v1/oauth2/token',
            'payment': 'https://api.sandbox.paypal.com/v1/payments/payment',
            'execute': 'https://api.sandbox.paypal.com/v1/payments/payment/%s/execute'
        },
        'secret':
        'ENtiNIfFohYUbB9V7KsvKPwmFsR7cbvBAQn0ZAtnzucg62uxZA0JqwMlXNqKSTMBjBLGrSJ_mP-28sqJ',
        'client_id':
        'AT61p1eOLNHUZ5y3VlakWbUGP8KRfQmHwTuubzerWj33llL4C44qwy55Os2BYhFDDlm24w5fE3TEVwJW',
    }


class DevelopmentConfig(DefaultConfig):

    # application configs

    DEBUG = False
    TESTING = False
    DEPLOYMENT = True

    # authentication configs

    DEFAULT_ACTIVATE_CODE_ON = True

    # email configs

    EMAIL_ON = True

    # code config

    HEALTH_CHECK_COMPONENTS = [
        'mongo',
        'redis',
    ]

    # limiter configs

    RATELIMIT_ENABLED = True

    # website config

    RECOVER_PASSWORD_URL = "https://panel-dev.psykon.ca/setPassword"


class MasterConfig(DefaultConfig):

    # application configs

    DEBUG = False
    TESTING = False
    DEPLOYMENT = True

    # authentication configs

    DEFAULT_ACTIVATE_CODE_ON = False

    # email configs

    EMAIL_ON = True

    # code config

    HEALTH_CHECK_COMPONENTS = [
        'mongo',
        'redis',
    ]

    # limiter configs

    RATELIMIT_ENABLED = True

    # website config

    RECOVER_PASSWORD_URL = "https://panel.psykon.ca/setPassword"

    # paypal config

    PAY_PAL_CONFIG = {
        'urls': {
            'oauth': 'https://api.paypal.com/v1/oauth2/token',
            'payment': 'https://api.paypal.com/v1/payments/payment',
            'execute': 'https://api.paypal.com/v1/payments/payment/%s/execute'
        },
        'secret': '',
        'client_id': '',
    }
