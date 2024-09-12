# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField, BooleanField


class OrganizationEdit(Document):
    """
    @apiDefine OrganizationEditJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} name Name of the organization
    @apiParam (Body Parameter) {String} field_of_activity Organization field of activity
    @apiParam (Body Parameter) {Integer} number_of_staff Organization number of staff
    @apiParam (Body Parameter) {Boolean} applied_before Organization applied before
    @apiParam (Body Parameter) {String} manager_name Organization manager name
    @apiParam (Body Parameter) {String} operator_name Organization operator name
    @apiParam (Body Parameter) {String} address Organization address
    @apiParam (Body Parameter) {String} post_code Organization post code
    @apiParam (Body Parameter) {String} work_tel Organization work tel
    @apiParam (Body Parameter) {String} [work_fax] Organization home fax
    @apiParam (Body Parameter) {String} purpose_for_taking_the_test
        Organization purpose for taking the test
    @apiParam (Body Parameter) {String} [more_information] Organization more information
    @apiParam (Body Parameter) {String} [more_data] Organization more data
    """
    name = StringField(required=True)
    field_of_activity = StringField(required=True)
    number_of_staff = IntField(required=True, minimum=0)
    applied_before = BooleanField(required=True)
    manager_name = StringField(required=True)
    operator_name = StringField(required=True)
    address = StringField(required=True)
    post_code = StringField(required=True)
    work_tel = StringField(required=True)
    work_fax = StringField()
    purpose_for_taking_the_test = StringField(required=True)
    more_information = StringField()
    more_data = StringField()
