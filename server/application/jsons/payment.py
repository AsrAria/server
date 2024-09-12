# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, IntField


class Payment(Document):
    """
    @apiDefine PaymentJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} amount Amoun of the payment
    """
    amount = IntField(required=True, minimum=0)
