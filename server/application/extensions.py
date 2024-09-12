# -*- coding: utf-8 -*-

# flask imports
from flask_redis import FlaskRedis
from flask_limiter import Limiter
from flask_jsonschema import JsonSchema
from flask_mongoengine import MongoEngine
from flask_limiter.util import get_remote_address

# project imports
from application.utils.magic import Magic
from application.modules.email import EmailClient
from application.modules.paypal import PayPalClient


# external modules
db = MongoEngine()
json = JsonSchema()
redis = FlaskRedis(strict=True)
limiter = Limiter(key_func=get_remote_address)

# internal modules
magic = Magic()
email = EmailClient()
paypal = PayPalClient()
