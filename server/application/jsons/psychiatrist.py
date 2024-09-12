# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField, \
    BooleanField, ArrayField, DocumentField


class Plan(Document):
    price = IntField(required=True, minimum=0)


class PsychiatristEdit(Document):
    """
    @apiDefine PsychiatristEditJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} first_name Psychiatrist first name
    @apiParam (Body Parameter) {String} last_name Psychiatrist last name
    @apiParam (Body Parameter) {Integer} age Psychiatrist age
    @apiParam (Body Parameter) {Integer} sex Psychiatrist sex
    @apiParam (Body Parameter) {String} birth_date Psychiatrist birth date
    @apiParam (Body Parameter) {String} [photo] Psychiatrist photo
    @apiParam (Body Parameter) {String} [attachment] Psychiatrist attachment
    @apiParam (Body Parameter) {String} address Psychiatrist address
    @apiParam (Body Parameter) {String} post_code Psychiatrist post code
    @apiParam (Body Parameter) {String} mobile Psychiatrist mobile
    @apiParam (Body Parameter) {String} [work_tel] Psychiatrist work tel
    @apiParam (Body Parameter) {String} home_tel Psychiatrist home tel
    @apiParam (Body Parameter) {Integer} primary_credential
        Psychiatrist primary credential
    @apiParam (Body Parameter) {Integer} primary_specialty
        Psychiatrist primary specialty
    @apiParam (Body Parameter) {String} last_three_years_experiences
        Psychiatrist last three years experiences
    @apiParam (Body Parameter) {String} name_of_posts_of_the_last_3_years
        Psychiatrist name of posts of the last 3 years
    @apiParam (Body Parameter) {Boolean} applied_before Psychiatrist applied before
    @apiParam (Body Parameter) {String} [more_information] Psychiatrist more information
    @apiParam (Body Parameter) {String} [more_data] Psychiatrist more data
    @apiParam (Body Parameter) {Plan[]} plans Psychiatrist plans
    @apiParam (Body Parameter) {Integer} [plans.price] Plan price
    """
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    age = IntField(required=True, minimum=1)
    sex = IntField(required=True, minimum=0, maximum=2)
    birth_date = StringField(required=True)
    photo = StringField()
    attachment = StringField()
    address = StringField(required=True)
    post_code = StringField(required=True)
    mobile = StringField(required=True)
    work_tel = StringField()
    home_tel = StringField(required=True)
    primary_credential = IntField(required=True, minimum=0, maximum=7)
    primary_specialty = IntField(required=True, minimum=0, maximum=4)
    last_three_years_experiences = StringField(required=True)
    name_of_posts_of_the_last_3_years = StringField(required=True)
    applied_before = BooleanField(required=True)
    more_information = StringField()
    more_data = StringField()
    plans = ArrayField(DocumentField(Plan), required=True, min_items=3, max_items=3)
