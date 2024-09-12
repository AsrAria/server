# -*- coding: utf-8 -*-

# python imports
from random import randint
from flask import g, request
from mongoengine import StringField, IntField, ReferenceField, DateTimeField, DENY

# project imports
from application.models import User
from application.models import BaseDocument
from application.extensions import paypal
from application.utils.time import datetime_to_string, create_datetime


class Payment(BaseDocument):

    # mark: constants

    STATUS_IN_PROGRESS = 0
    STATUS_SUCCESS = 1
    STATUS_UNSUCCESS = 2

    # mark: meta

    amount = IntField(required=True, default=0)

    gateway = StringField(required=True)

    status = IntField(required=True, default=STATUS_IN_PROGRESS)
    tracking_id = StringField(unique=True)

    payment_id = StringField()
    payment_time = DateTimeField()

    user = ReferenceField(User, required=True, reverse_delete_rule=DENY)

    # mark: meta

    meta = {
        'collection': 'payments'
    }

    # mark: json functions

    def to_json(self):
        """
        @apiDefine PaymentToJson

        @apiSuccess (Success Response) {String} id Id of the payment
        @apiSuccess (Success Response) {Integer} amount Amount of the payment
        @apiSuccess (Success Response) {String} gateway Gateway of the payment
        @apiSuccess (Success Response) {Integer} status
            Status of the payment (0=in progress, 1=success, 2=cancel)
        @apiSuccess (Success Response) {String} tracking_id Tracking id of the payment
        @apiSuccess (Success Response) {String} [payment_id] Payment id of the payment
        @apiSuccess (Success Response) {String} [payment_time]
            Time of the payment completed (ISO format yyyy-mm-ddThh:mm:ss)
        @apiSuccess (Success Response) {User} user User of the payment
        @apiSuccess (Success Response) {String} user.id Id of the user
        @apiSuccess (Success Response) {String} user.email Email of the user
        """
        dic = {
            'id': self.id,
            'amount': self.amount,
            'gateway': self.gateway,
            'status': self.status,
            'tracking_id': self.tracking_id,
        }
        if self.payment_id:
            dic['payment_id'] = self.payment_id
        if self.payment_time:
            dic['payment_time'] = datetime_to_string(self.payment_time)
        if 'user_type' in g and g.user_type == 'admin':
            dic['user'] = {
                'id': self.user.id,
                'email': self.user.email
            }
        return dic

    def populate(self, user, amount):
        self.user = user
        self.amount = amount
        self.gateway = "paypal"
        self.tracking_id = str(randint(0, 99999999)).zfill(8)

    # mark: zarinpal payment functions

    def start_payment(self):
        self.save()
        result = paypal.create_payment(
            "Increase account balance",
            "Increase account balance",
            self.amount,
            self.tracking_id,
            request.url + '/verify/' + self.id,
            request.url + '/cancel/' + self.id
        )
        if not result:
            return None
        self.payment_id = result['payment_id']
        self.save()
        return result['url']

    def verify_payment(self, payment_id, payer_id):
        if paypal.execute_payment(payment_id, payer_id):
            self.status = Payment.STATUS_SUCCESS
            self.payment_time = create_datetime()
            self.save()
            self.user.update_balance()
            return True
        self.status = Payment.STATUS_UNSUCCESS
        self.save()
        return False
