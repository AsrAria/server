# -*- coding: utf-8 -*-

# flask imports
from flask import Blueprint, jsonify, request, g, current_app
from flask_jsonschema import validate

# mongo imports
from mongoengine import DoesNotExist, Q

# project imports
from application.models import Admin
from application.models import Permission
from application.extensions import limiter
from application.utils.hashing import hash_password
from application.utils.localize import localize
from application.utils.pagination import paginate
from application.utils.request import get_remote_address

api = Blueprint('admin.api.v1', __name__, url_prefix='/api/v1/admin')


@api.route('/authenticate', methods=['POST'])
@validate('admin_authenticate')
@limiter.limit('5/minute', get_remote_address)
def authenticate():
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName AdminAuthenticate
    @api {post} /v1/admin/authenticate
        Authenticate a admin user and send activation code

    @apiUse AdminAuthenticateJson

    @apiSuccess (Success Response) {String} username Username of the user
    @apiSuccess (Success Response) {String} activate_ttl Activate token ttl

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        admin = Admin.objects.get(username=request.json['username'])
        if admin.password == hash_password(request.json['password']):
            admin.send_activation_code()
            return jsonify(
                username=admin.username,
                activate_ttl=current_app.config['ACTIVATION_CODE_TIMEOUT']
            ), 200
        return jsonify(), 401
    except DoesNotExist:
        return jsonify(), 401


@api.route('/activate', methods=['POST'])
@validate('admin_activate')
def activate():
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName AdminActivate
    @api {post} /v1/admin/activate Activate a admin user

    @apiUse AdminActivateJson

    @apiSuccess (Success Response) {String} ttl TTL of secret key
    @apiSuccess (Success Response) {String} secret_key Secret key of admin
    @apiSuccess (Success Response) {Admin} admin
        Admin details (<a href="#api-Admin-GetAdmin">admin object</a>)

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        json = request.json
        admin = Admin.objects.get(username=request.json['username'])

        if admin.consume_activation_code(json['code']):
            admin.secret_key = admin.generate_secret_key()
            admin.save()

            return jsonify(
                admin=admin.to_json(),
                secret_key=admin.secret_key,
                ttl=current_app.config['ADMIN_SECRET_KEY_TIMEOUT'],
            ), 200
        return jsonify(), 401
    except DoesNotExist:
        return jsonify(), 404


@api.route('', methods=['GET'])
@Admin.authenticate('admin', None, Permission.ACCESS_READ)
@paginate(key='list', max_per_page=50)
def get_list():
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName GetAdminList
    @api {get} /v1/admin Get admin list

    @apiUse Paginate

    @apiUse SecretKeyHeader

    @apiParam (Query Parameter) {String} [query]
        Filter by query (search in email and username)

    @apiSuccess (Success Response) {Admin[]} list
        List of <a href="#api-Admin-GetAdmin">admin object</a>

    @apiUse OK
    @apiUse Unauthorized
    """
    query = Admin.objects.filter().order_by('+username')

    if request.args.get('query'):
        query = query.filter(
            Q(email__icontains=request.args['query'].lower()) |
            Q(username__icontains=request.args['query'])
        )

    return query


@api.route('/<username>', methods=['GET'])
@Admin.authenticate('admin', None, Permission.ACCESS_READ)
def get(username):
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName GetAdmin
    @api {get} /v1/admin/:username Get a admin user

    @apiUse SecretKeyHeader

    @apiParam (URL Parameter) {String} username Admin username

    @apiUse AdminToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        admin = Admin.objects.get(username=username)
        return jsonify(admin.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('', methods=['POST'])
@validate('admin_create')
@Admin.authenticate('admin', None, Permission.ACCESS_WRITE)
def create():
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName CreateAdmin
    @api {post} /v1/admin Create a admin user

    @apiUse SecretKeyHeader

    @apiUse AdminCreateJson
    @apiUse AdminToJson

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        admin = Admin()
        admin.populate(request.json)
        admin.save()
        return jsonify(admin.to_json()), 201
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<username>', methods=['PUT'])
@validate('admin_update')
@Admin.authenticate('admin', None, Permission.ACCESS_WRITE)
def update(username):
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName UpdateAdmin
    @api {put} /v1/admin/:username Update a admin user

    @apiUse SecretKeyHeader

    @apiParam (URL Parameter) {String} username Admin username

    @apiUse AdminUpdateJson
    @apiUse AdminToJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        admin = Admin.objects.get(username=username)
        admin.populate(request.json)

        if username == g.user.username and \
           admin.get_access_level("admin", None) < Permission.ACCESS_WRITE:
            return jsonify(message_en=localize('remove_admin_access_error')), 403
        admin.save()

        if 'password' in request.json:
            admin.password = hash_password(request.json['password'])
            admin.save()

        return jsonify(admin.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<username>', methods=['DELETE'])
@Admin.authenticate('admin', None, Permission.ACCESS_WRITE)
def delete(username):
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName DeleteAdmin
    @api {delete} /v1/admin/:username Delete a admin user

    @apiParam (URL Parameter) {String} username Admin username

    @apiUse SecretKeyHeader

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        admin = Admin.objects.get(username=username)
        if admin.username == g.user.username:
            return jsonify(message_en=localize('remove_admin_error')), 403
        if admin.username == 'admin':
            return jsonify(message_en=localize('remove_main_admin_error')), 403
        admin.delete()
        return jsonify(), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/profile', methods=['PUT'])
@validate('admin_update_profile')
@Admin.authenticate()
def update_profile():
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName AdminUpdateProfile
    @api {put} /v1/admin/profile Update admin profile

    @apiUse SecretKeyHeader

    @apiUse AdminUpdateProfileJson
    @apiUse AdminToJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        admin = g.user
        admin.populate(request.json)
        admin.save()
        return jsonify(admin.to_json()), 200
    except Exception:
        return jsonify(), 400


@api.route('/password', methods=['PUT'])
@validate('admin_change_password')
@Admin.authenticate()
def change_password():
    """
    @apiVersion 1.0.0
    @apiGroup Admin
    @apiName AdminChangePassword
    @api {put} /v1/admin/password Change admin password

    @apiUse SecretKeyHeader

    @apiUse AdminChangePasswordJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        admin = g.user
        if admin.password == hash_password(request.json['old_password']):
            admin.password = hash_password(request.json['new_password'])
            admin.save()
            return jsonify(), 200
        return jsonify(), 401
    except Exception:
        return jsonify(), 400
