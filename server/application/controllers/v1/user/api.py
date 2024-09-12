# -*- coding: utf-8 -*-

# python imports
import os
import imagesize

# flask imports
from flask import Blueprint, jsonify, request, g, current_app, send_file, render_template
from flask_jsonschema import validate

# mongo imports
from mongoengine import DoesNotExist

# project imports
from application.models import User
from application.models import Token
from application.models import Admin
from application.models import Payment
from application.models import Permission
from application.forms.upload import UploadForm
from application.extensions import magic
from application.extensions import limiter
from application.utils.localize import localize
from application.utils.pagination import paginate
from application.utils.authenticate import authenticate
from application.utils.request import get_remote_address
from application.utils.hashing import hash_password


api = Blueprint('user.api.v1', __name__, url_prefix='/api/v1/user')


@api.route('/register', methods=['POST'])
@validate('register')
@limiter.limit('5/minute', get_remote_address)
def register():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName RegisterUser
    @api {post} /v1/user/register Register a new user

    @apiUse RegisterJson

    @apiSuccess (Success Response) {String} activate_ttl Activate token ttl
    @apiSuccess (Success Response) {String} email Email of the user

    @apiUse Created
    @apiUse BadRequest
    @apiUse Conflict
    """
    json = request.json

    user = User.create(json)
    if not user:
        return jsonify(), 409

    user.send_activation_code()
    return jsonify(
        email=user.email,
        activate_ttl=current_app.config['ACTIVATION_CODE_TIMEOUT']
    ), 201


@api.route('/activate', methods=['POST'])
@validate('activate')
def activate():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName ActivateUser
    @api {post} /v1/user/activate Activate a new user and get access token

    @apiUse ActivateJson

    @apiSuccess (Success Response) {String} access_token
    @apiSuccess (Success Response) {String} refresh_token
    @apiSuccess (Success Response) {User} user
        User details (<a href="#api-User-GetUser">User object</a>)

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        json = request.json
        user = User.objects.get(email=json['email'].lower())

        if user.consume_activation_code(json['code']):
            if not user.is_active:
                user.is_active = True
                user.save()

            token = Token.create(user)
            return jsonify(
                user=user.to_json(True),
                access_token=token.access_token,
                refresh_token=token.refresh_token
            ), 200
    except DoesNotExist:
        pass
    return jsonify(), 401


@api.route('/activate/code', methods=['POST'])
@validate('send_activate_code')
@limiter.limit('5/minute', get_remote_address)
def send_activate_code():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName SendActivateCodeJson
    @api {post} /v1/user/activate/code Send new activation code to user

    @apiUse SendActivateCodeJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        json = request.json
        user = User.objects.get(email=json['email'].lower())

        if user.password != hash_password(json['password']):
            return jsonify(), 401

        user.send_activation_code()
        return jsonify(
            email=user.email,
            activate_ttl=current_app.config['ACTIVATION_CODE_TIMEOUT']
        ), 200
    except DoesNotExist:
        return jsonify(), 401
    return jsonify(), 401


@api.route('/token/refresh', methods=['POST'])
@validate('refresh_token')
def refresh():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName RefreshToken
    @api {post} /v1/user/token/refresh Refresh access token

    @apiUse RefreshTokenJson

    @apiSuccess (Success Response) {String} access_token Access token of user
    @apiSuccess (Success Response) {String} refresh_token Refresh token for user

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        json = request.json
        token = Token.objects.get(refresh_token=json['refresh_token'])
        if (not token) or (json['access_token'] != token.access_token):
            return jsonify(), 401

        user = token.user
        token = Token.create(user)
        return jsonify(
            access_token=token.access_token,
            refresh_token=token.refresh_token
        ), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/token/revoke', methods=['DELETE'])
def revoke():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName RevokeToken
    @api {delete} /v1/user/token/revoke Revoke access token

    @apiUse AccessTokenHeader

    @apiUse OK
    @apiUse Unauthorized
    """
    try:
        Token.objects.get(access_token=request.headers.get('Access-Token'))
        Token.revoke(request.headers.get('Access-Token'))
        return jsonify(), 200
    except Exception:
        return jsonify(), 401


@api.route('/token/revoke_all', methods=['DELETE'])
@User.authenticate
def revoke_all():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName RevokeAllTokens
    @api {delete} /v1/user/token/revoke_all Revoke all access tokens

    @apiUse AccessTokenHeader

    @apiUse OK
    @apiUse Unauthorized
    """
    Token.revoke_all(g.user)
    return jsonify(), 200


@api.route('', methods=['GET'])
@Admin.authenticate('user', 'user', Permission.ACCESS_READ)
@paginate(key='list', max_per_page=50)
def get_list():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName GetUserList
    @api {get} /v1/user Get user list

    @apiUse Paginate

    @apiUse SecretKeyHeader

    @apiParam (Query Parameter) {String} [role] Filter by role
    @apiParam (Query Parameter) {String} [query] Filter by email (user)
    @apiParam (Query Parameter) {String} [email] Filter by email (admin)
    @apiParam (Query Parameter) {String} [is_active] Filter by is_active field (true, false)
    @apiParam (Query Parameter) {String} [is_enable] Filter by is_enable field (true, false)

    @apiSuccess (Success Response) {User[]} list
        List of <a href="#api-User-GetUser">user object</a>

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        query = User.objects().order_by('-create_time')

        if request.args.get('role'):
            query = query.filter(role=int(request.args['role']))

        if g.user_type != 'admin':
            if request.args.get('query'):
                query = query.filter(email=request.args['query'].lower())
            else:
                query = query.filter(email="-")
        elif request.args.get('email'):
            query = query.filter(email__contains=request.args['email'].lower())

        if g.user_type != 'admin':
            query = query.filter(is_active=True)
        elif request.args.get('is_active'):
            query = query.filter(is_active=(request.args['is_active'] == 'true'))

        if g.user_type != 'admin':
            query = query.filter(is_enable=True)
        elif request.args.get('is_enable'):
            query = query.filter(is_enable=(request.args['is_enable'] == 'true'))

        return query
    except Exception:
        return jsonify(), 400


@api.route('/<id>', methods=['GET'])
@authenticate('user', 'user', Permission.ACCESS_READ, True)
def get_user(id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName GetUser
    @api {get} /v1/user/:id Get a user

    @apiParam (URL Parameter) {String} id ID of desired user

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse UserToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        user = User.objects.get(id=id)
        return jsonify(user.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/password', methods=['PUT'])
@validate('user_change_password')
@User.authenticate
def change_password():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserChangePassword
    @api {put} /v1/user/password Change user password

    @apiUse AccessTokenHeader

    @apiUse UserChangePasswordJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        user = g.user
        if user.password == hash_password(request.json['old_password']):
            user.password = hash_password(request.json['new_password'])
            user.save()
            return jsonify(), 200
        return jsonify(), 401
    except Exception:
        return jsonify(), 400


@api.route('/password/recover', methods=['POST'])
@validate('user_recover_password')
def recover_password():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserRecoverPassword
    @api {put} /v1/user/password/recover Request recover password

    @apiUse UserRecoverPasswordJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        json = request.json
        user = User.objects.get(email=json['email'].lower())
        token = user.send_recover_password_token()
        return (jsonify(), 200) if current_app.config['DEPLOYMENT'] else (jsonify(token=token), 200)
    except DoesNotExist:
        return jsonify(), 404


@api.route('/password/set', methods=['POST'])
@validate('user_set_password')
def set_password():
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserSetPassword
    @api {put} /v1/user/password/set Set password by recover token

    @apiUse UserSetPasswordJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    user = User.consume_recover_password_token(request.json['token'])
    if user:
        user.password = hash_password(request.json['new_password'])
        user.save()
        return jsonify(), 200
    return jsonify(), 401


@api.route('/<id>/enable', methods=['POST'])
@Admin.authenticate('user', 'user', Permission.ACCESS_WRITE)
def enable(id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName EnableUser
    @api {post} /v1/user/:id/enable Enable user

    @apiParam (URL Parameter) {String} id ID of desired user

    @apiUse SecretKeyHeader

    @apiUse UserToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        user = User.objects.get(id=id)
        user.is_enable = True
        user.save()
        return jsonify(user.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/disable', methods=['POST'])
@Admin.authenticate('user', 'user', Permission.ACCESS_WRITE)
def disable(id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName DisableUser
    @api {post} /v1/user/:id/disable Disable user

    @apiParam (URL Parameter) {String} id ID of desired user

    @apiUse SecretKeyHeader

    @apiUse UserToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        user = User.objects.get(id=id)
        user.is_enable = False
        user.save()
        return jsonify(user.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/image', methods=['POST'])
@authenticate('user', 'user', Permission.ACCESS_WRITE, True)
def upload_image(id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserUploadImage
    @api {post} /v1/user/:id/image Upload user image

    @apiParam (URL Parameter) {String} id ID of desired user

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse UploadForm

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        form = UploadForm()
        if not form.validate():
            return jsonify(), 400

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403
        user = User.objects.get(id=id)

        type = form.type.data
        if type not in ['photo']:
            return jsonify(), 400

        # if not current_app.config['DEPLOYMENT']:
            # return jsonify(url=request.url + '/' + type), 201

        file_obj = form.file.data
        file_directory = user.get_image_path()
        magic.get_extension(file_obj.read(1024), type='image')

        directory_path = os.path.join(current_app.config['FILE_UPLOAD_DIR'], file_directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_address = os.path.join(directory_path, user.id + '_' + type)
        file_obj.seek(0)
        file_obj.save(file_address)

        width, height = imagesize.get(file_address)
        if width > 1000 or height > 1000:
            os.remove(file_address)
            return jsonify(message_en=localize('image_size_error')), 400

        return jsonify(url=request.url + '/' + type), 201
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/image/<type>', methods=['GET'])
def get_image(id, type):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserGetImage
    @api {post} /v1/user/:id/image/:type Get user image

    @apiParam (URL Parameter) {String} id ID of desired user
    @apiParam (URL Parameter) {String} type Type of image

    @apiUse OK
    @apiUse BadRequest
    @apiUse NotFound
    """
    try:
        user = User.objects.get(id=id)
        file_directory = user.get_image_path()
        directory_path = os.path.join(current_app.config['FILE_UPLOAD_DIR'], file_directory)
        file_address = os.path.join(directory_path, user.id + '_' + type)
        return send_file(file_address)
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/file', methods=['POST'])
@authenticate('user', 'user', Permission.ACCESS_WRITE, True)
def upload_file(id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserUploadFile
    @api {post} /v1/user/:id/file Upload user file

    @apiParam (URL Parameter) {String} id ID of desired user

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse UploadForm

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        form = UploadForm()
        if not form.validate():
            return jsonify(), 400

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403
        user = User.objects.get(id=id)

        type = form.type.data
        if type not in ['attachment']:
            return jsonify(), 400

        # if not current_app.config['DEPLOYMENT']:
            # return jsonify(url=request.url + '/' + type), 201

        file_obj = form.file.data
        file_directory = user.get_attachment_path()

        directory_path = os.path.join(current_app.config['FILE_UPLOAD_DIR'], file_directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_address = os.path.join(directory_path, user.id + '_' + type)
        file_obj.seek(0)
        file_obj.save(file_address)

        return jsonify(url=request.url + '/' + type), 201
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/file/<type>', methods=['GET'])
@authenticate('user', 'user', Permission.ACCESS_READ, True)
def get_file(id, type):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserGetFile
    @api {post} /v1/user/:id/file/:type Get user file

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired user
    @apiParam (URL Parameter) {String} type Type of file

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403
        user = User.objects.get(id=id)

        if type not in ['attachment']:
            return jsonify(), 400

        file_directory = user.get_attachment_path()
        directory_path = os.path.join(current_app.config['FILE_UPLOAD_DIR'], file_directory)
        file_address = os.path.join(directory_path, user.id + '_' + type)
        return send_file(file_address)
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/pay', methods=['POST'])
@validate('payment')
@User.authenticate
def create_payment_url(id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserCreatePayment
    @api {post} /v1/user/:id/pay Create a payment url

    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired user

    @apiUse PaymentJson

    @apiSuccess (Success Response) {String} id Id of payment
    @apiSuccess (Success Response) {String} url URL of payment

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotAcceptable
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403
        user = User.objects.get(id=id)

        payment = Payment()
        payment.populate(user, request.json['amount'])
        url = payment.start_payment()
        if not url and current_app.config['DEPLOYMENT']:
            payment.delete()
            return jsonify(), 406
        return jsonify(url=url, id=payment.id), 201
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/pay/verify/<payment_id>', methods=['GET'])
def verify_payment(id, payment_id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserVerifyPayment
    @api {get} /v1/user/:id/pay/varify/:payment_id Verify a payment

    @apiParam (URL Parameter) {String} id ID of desired user
    @apiParam (URL Parameter) {String} payment_id Payment id

    @apiParam (Query Parameter) {String} [paymentId] Paypal payment id
    @apiParam (Query Parameter) {String} [PayerID] Paypal payer id

    @apiUse OK
    @apiUse BadRequest
    @apiUse NotFound
    """
    try:
        if 'paymentId' not in request.args or 'PayerID' not in request.args:
            return jsonify(), 400

        payment = Payment.objects.get(id=payment_id, payment_id=request.args['paymentId'])
        if payment.status == Payment.STATUS_IN_PROGRESS:
            payment.verify_payment(request.args['paymentId'], request.args['PayerID'])
        return render_template('payment.html', payment=payment, message=""), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/pay/cancel/<payment_id>', methods=['GET'])
def cancel_payment(id, payment_id):
    """
    @apiVersion 1.0.0
    @apiGroup User
    @apiName UserCancelPayment
    @api {get} /v1/user/:id/pay/cancel/:payment_id Cancel a payment

    @apiParam (URL Parameter) {String} id ID of desired user
    @apiParam (URL Parameter) {String} payment_id Payment id

    @apiUse OK
    @apiUse NotFound
    """
    try:
        payment = Payment.objects.get(id=payment_id)
        if payment.status == Payment.STATUS_IN_PROGRESS:
            payment.status = Payment.STATUS_UNSUCCESS
        payment.save()
        return render_template('payment.html', payment=payment, message=""), 200
    except DoesNotExist:
        return jsonify(), 404
