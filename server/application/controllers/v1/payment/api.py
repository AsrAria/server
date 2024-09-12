# -*- coding: utf-8 -*-

# flask imports
from flask import Blueprint, jsonify, request, g

# mongo imports
from mongoengine import DoesNotExist

# project imports
from application.models import User
from application.models import Payment
from application.models import Permission
from application.utils.pagination import paginate
from application.utils.authenticate import authenticate


api = Blueprint('payment.api.v1', __name__, url_prefix='/api/v1/payment')


@api.route('', methods=['GET'])
@authenticate('user', 'user', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_list():
    """
    @apiVersion 1.0.0
    @apiGroup Payment
    @apiName GetPaymentList
    @api {get} /v1/payment Get payment list

    @apiUse Paginate

    @apiUse SecretKeyHeader

    @apiParam (Query Parameter) {String} [email] Filter by user email
    @apiParam (Query Parameter) {String} [status]
        Filter by status (0=in progress, 1=success, 2=unsuccess)

    @apiSuccess (Success Response) {Payment[]} list
        List of <a href="#api-Payment-GetPayment">payment object</a>

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    """
    try:
        query = Payment.objects().order_by('-create_time')

        if request.args.get('status'):
            query = query.filter(status=int(request.args['status']))

        if g.user_type == 'user':
            query = query.filter(user=g.user)
        elif request.args.get('email'):
            try:
                user = User.objects.get(email=request.args['email'].lower())
            except Exception:
                user = None
            query = query.filter(user=user)

        return query
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>', methods=['GET'])
@authenticate('user', 'user', Permission.ACCESS_READ, True)
def get_payment(id):
    """
    @apiVersion 1.0.0
    @apiGroup Payment
    @apiName GetPayment
    @api {get} /v1/payment/:id Get a payment

    @apiParam (URL Parameter) {String} id ID of desired payment

    @apiUse SecretKeyHeader

    @apiUse PaymentToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        payment = Payment.objects.get(id=id)

        if g.user_type == 'user' and g.user.id != payment.user.id:
            return jsonify(), 403

        return jsonify(payment.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
