# -*- coding: utf-8 -*-


def check_redis():
    """
    @apiDefine RedisError
    @apiError (Error 521) Redis health check failed
    """
    from application.extensions import redis

    try:
        redis.echo("Testing from flask app")
        return True, 200
    except Exception as err:
        return err, 521


def check_mongo():
    """
    @apiDefine MongoDBError
    @apiError (Error 522) MongoDB health check failed
    """
    from mongoengine import Document, StringField, register_connection
    from flask import current_app as app

    try:
        register_connection('test', **app.config['MONGODB_SETTINGS'])

        class TestDocument(Document):
            test_field = StringField()
            meta = {'db_alias': 'test'}

        TestDocument(test_field='test').save()
        TestDocument.drop_collection()
        return True, 200
    except Exception as err:
        return err, 522


check_funcs = {
    'redis': check_redis,
    'mongo': check_mongo,
}
