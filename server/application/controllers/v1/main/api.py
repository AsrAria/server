# -*- coding: utf-8 -*-

# flask imports
from flask import Blueprint, jsonify, current_app

# project imports
from application.models import User
from application.models import Admin
from application.utils.health_check import check_funcs


api = Blueprint('main.api.v1', __name__, url_prefix='/api/v1')


@api.route('/health_check', methods=['GET'])
def health_check():
    """
    @apiVersion 1.0.0
    @apiGroup Main
    @apiName HealthCheck
    @api {get} /v1/health_check Check health

    @apiUse OK
    @apiUse RedisError
    @apiUse MongoDBError
    """
    ext_list = current_app.config['HEALTH_CHECK_COMPONENTS']
    for ext in ext_list:
        if ext in check_funcs:
            result, status = check_funcs[ext]()
            if result is not True:
                return jsonify(), status
    return jsonify(), 200


@api.route('/check_token', methods=['GET'])
def check_token():
    """
    @apiVersion 1.0.0
    @apiGroup Main
    @apiName CheckToken
    @api {get} /v1/check_token Check token exists or not

    @apiUse AccessTokenHeader
    @apiUse SecretKeyHeader

    @apiUse OK
    @apiUse NotFound
    """
    if User.check_authentication() == 200:
        return jsonify({}), 200
    if Admin.check_authentication() == 200:
        return jsonify({}), 200
    return jsonify({}), 404
