# -*- coding: utf-8 -*-

# python imports
import os

# flask imports
from flask import Flask, jsonify, g

# application imports
from application.config import DefaultConfig

# project imports
from application.utils.localize import localize


def configure_extensions(app):
    import application.extensions as ex
    for extension in app.config['INSTALLED_EXTENSIONS']:
        try:
            getattr(ex, extension).init_app(app)
        except (AttributeError, TypeError):
            pass


def configure_controllers(app):
    api_versions = app.config['ENABLE_API_VERSIONS']

    for version, controller_list in api_versions.items():
        for controller in controller_list:
            bp = __import__(
                'application.controllers.%s.%s' % (version, controller),
                fromlist=[version, controller]
            )

            for route in bp.__all__:
                route_obj = getattr(bp, route)
                app.register_blueprint(route_obj)


def configure_error_handlers(app):
    # python imports
    from mongoengine import DoesNotExist, OperationError, ValidationError
    # flask imports
    from flask_jsonschema import ValidationError as JsonValidationError

    """
    @apiDefine OK
    @apiSuccessExample Success Status Code
        HTTP/1.1 200 OK
    """
    """
    @apiDefine Created
    @apiSuccessExample Success Status Code
        HTTP/1.1 201 Created
    """
    """
    @apiDefine Redirect
    @apiSuccessExample Redirect to another url
        HTTP/1.1 301 Redirect
    """
    """
    @apiDefine FailedDependency
    @apiError (Error 424) FailedDependency  The request failed because it depended on another
        request and that request failed (e.g., a PROPPATCH).
    """
    """
    @apiDefine ServiceUnavailable
    @apiError (Error 503) ServiceUnavailable  The server is currently unavailable (because
        it is overloaded or down for maintenance). Generally, this is a temporary state.
    """

    @app.errorhandler(406)
    def not_acceptable(error):
        """
        @apiDefine NotAcceptable
        @apiError (Error 406) NotAcceptable  The requested resource is capable of generating only
            content not acceptable according to the Accept headers sent in the request.
        """
        return (jsonify(message=error.message), 406) if app.config['DEBUG'] else ("", 406)

    @app.errorhandler(409)
    def conflict(error):
        """
        @apiDefine Conflict
        @apiError (Error 409) Conflict  Indicates that the request could not be processed because
            of conflict in the request,
                such as an edit conflict between multiple simultaneous updates.
        """
        return (jsonify(message=error.message), 409) if app.config['DEBUG'] else ("", 409)

    def not_found(error):
        """
        @apiDefine NotFound
        @apiError (Error 404) NotFound  The server has not found anything matching the Request-URI.
        """
        return (jsonify(error=str(error)), 404) if app.config['DEBUG'] else ("", 404)

    app.register_error_handler(DoesNotExist, not_found)
    app.register_error_handler(404, not_found)

    @app.errorhandler(400)
    def bad_request(error):
        """
        @apiDefine BadRequest
        @apiError (Error 400) BadRequest  The request could not be understood by the server
            due to malformed syntax. The client SHOULD NOT repeat the
        request without modifications.
        """
        return (jsonify(error=str(error)), 400) if app.config['DEBUG'] else ("", 400)

    app.register_error_handler(JsonValidationError, bad_request)
    app.register_error_handler(ValidationError, bad_request)
    app.register_error_handler(OperationError, bad_request)

    @app.errorhandler(403)
    def forbidden(error):
        """
        @apiDefine Forbidden
        @apiError (Error 403) Forbidden
            The server understood the request, but is refusing to fulfill it.
        """
        return (jsonify(message=error.message), 403) if app.config['DEBUG'] else ("", 403)

    @app.errorhandler(401)
    def unauthorized(error):
        """
        @apiDefine Unauthorized
        @apiError (Error 401) Unauthorized  The request requires user authentication.
        """
        return (jsonify(message=error.message), 401) if app.config['DEBUG'] else ("", 401)

    @app.errorhandler(500)
    def internal_error(error):
        return "", 500

    @app.errorhandler(OperationError)
    def mongo_operation_error(error):
        if str(error).find("duplicate") != -1:
            return jsonify(message_en=localize('duplicated_field_error')), 409
        return jsonify(message_en=localize('relation_field_error')), 400


def configure_folders(app):
    for key, value in app.config.items():
        if key.endswith('DIR'):
            if not os.path.exists(value):
                os.makedirs(value)
                app.logger.info("{} created at {}".format(key, value))


def configure_app(app, configuration):
    app.config.from_object(DefaultConfig)

    if configuration is not None:
        app.config.from_object(configuration)
    app.config.from_envvar('FLASK_APP_SETTINGS', silent=True)


def configure_middlewares(app):
    @app.before_request
    def before_request_func():
        g.user = None
        g.user_type = 'anonymous'


def create_app(configuration):
    app = Flask(__name__)

    configure_app(app, configuration)
    configure_folders(app)
    configure_extensions(app)
    configure_controllers(app)
    configure_middlewares(app)
    configure_error_handlers(app)

    return app
