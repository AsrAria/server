# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField


class PersonEdit(Document):
    """
    @apiDefine PersonEditJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} first_name Person first name
    @apiParam (Body Parameter) {String} last_name Person last name
    @apiParam (Body Parameter) {Integer} age Person age
    @apiParam (Body Parameter) {Integer} sex Person sex
    @apiParam (Body Parameter) {String} [birth_date] Person birth date
    @apiParam (Body Parameter) {String} [photo] Person photo
    @apiParam (Body Parameter) {String} [address] Person address
    @apiParam (Body Parameter) {String} [post_code] Person post code
    @apiParam (Body Parameter) {String} [mobile] Person mobile
    @apiParam (Body Parameter) {String} [work_tel] Person work tel
    @apiParam (Body Parameter) {String} [home_tel] Person home tel
    @apiParam (Body Parameter) {Integer} duration_of_hospitalization
        Person duration of hospitalization
    @apiParam (Body Parameter) {String} [illness_severity] Person illness severity
    @apiParam (Body Parameter) {String} [disease_background] Person disease background
    @apiParam (Body Parameter) {String} [family_disease_background]
        Person family disease background
    @apiParam (Body Parameter) {String} [history_of_drug_use] Person history of drug use
    @apiParam (Body Parameter) {String} [family_history_of_drug_use]
        Person family history of drug use
    @apiParam (Body Parameter) {Integer} [birth_order] Person birth order
    @apiParam (Body Parameter) {Integer} [number_of_children_in_family]
        Person number of children in family
    @apiParam (Body Parameter) {String} [more_information] Person more information
    """
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    age = IntField(required=True, minimum=1)
    sex = IntField(required=True, minimum=0, maximum=2)
    birth_date = StringField()
    photo = StringField()
    address = StringField()
    post_code = StringField()
    mobile = StringField()
    work_tel = StringField()
    home_tel = StringField()
    duration_of_hospitalization = IntField(required=True, minimum=0, maximum=4)
    illness_severity = StringField()
    disease_background = StringField()
    family_disease_background = StringField()
    history_of_drug_use = StringField()
    family_history_of_drug_use = StringField()
    birth_order = IntField(minimum=1)
    number_of_children_in_family = IntField(minimum=1)
    more_information = StringField()
