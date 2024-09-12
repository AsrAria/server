# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField

# project imports
from application.utils.pattern import Pattern


class Package(Document):
    """
    @apiDefine PackageJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} person Person email of the package
    @apiParam (Body Parameter) {String} start_date Start date of the package (ISO format yyyy-mm-dd)
    @apiParam (Body Parameter) {String} end_date End date of the package (ISO format yyyy-mm-dd)
    @apiParam (Body Parameter) {String} budget Budget of the package
    """
    person = StringField(required=True, pattern=Pattern.PATTERN_EMAIL)
    start_date = StringField(required=True)
    end_date = StringField(required=True)
    budget = IntField(required=True)
