# -*- coding: utf-8 -*-

# flask imports
from flask import g

# flask imports
from mongoengine import BooleanField, StringField, FloatField, \
    IntField, DateField, EmbeddedDocument, EmbeddedDocumentListField

# project imports
from application.models import User
from application.models import Permission
from application.utils.time import date_to_string, string_to_datetime


class Plan(EmbeddedDocument):

    # mark: variables

    price = IntField(default=0)

    # mark: json functions

    def to_json(self):
        return {
            'price': self.price
        }

    def populate(self, json):
        self.price = json['price']


class Psychiatrist(User):

    # mark: variables

    is_confirmed = BooleanField(required=True, default=False)

    first_name = StringField(default="")
    last_name = StringField(default="")

    age = IntField()
    sex = IntField()

    birth_date = DateField()
    photo = StringField(default="")
    attachment = StringField(default="")

    address = StringField(default="")
    post_code = StringField(default="")

    mobile = StringField(default="")
    work_tel = StringField(default="")
    home_tel = StringField(default="")

    primary_credential = IntField()
    primary_specialty = IntField()

    last_three_years_experiences = StringField(default="")
    name_of_posts_of_the_last_3_years = StringField(default="")

    applied_before = BooleanField(default=False)

    more_information = StringField(default="")
    more_data = StringField(default="")

    plans = EmbeddedDocumentListField(Plan, default=[])

    score = FloatField(default=3)

    notification_count = IntField(required=True, default=0)

    # mark: meta

    meta = {
    }

    # mark: json functions

    def to_json(self, details=False):
        """
        @apiDefine PsychiatristToJson

        @apiSuccess (Success Response) {String} id Psychiatrist id
        @apiSuccess (Success Response) {String} email Psychiatrist email
        @apiSuccess (Success Response) {String} name Psychiatrist name
        @apiSuccess (Success Response) {String} [first_name] Psychiatrist first name
        @apiSuccess (Success Response) {String} [last_name] Psychiatrist last name
        @apiSuccess (Success Response) {Integer} [score] Psychiatrist score
        @apiSuccess (Success Response) {Integer} [age] Psychiatrist age
        @apiSuccess (Success Response) {Integer} [sex] Psychiatrist sex
        @apiSuccess (Success Response) {String} [birth_date] Psychiatrist birth date
        @apiSuccess (Success Response) {String} [photo] Psychiatrist photo
        @apiSuccess (Success Response) {String} [attachment] Psychiatrist attachment
        @apiSuccess (Success Response) {String} [address] Psychiatrist address
        @apiSuccess (Success Response) {String} [post_code] Psychiatrist post code
        @apiSuccess (Success Response) {String} [mobile] Psychiatrist mobile
        @apiSuccess (Success Response) {String} [work_tel] Psychiatrist work tel
        @apiSuccess (Success Response) {String} [home_tel] Psychiatrist home tel
        @apiSuccess (Success Response) {Integer} [primary_credential]
            Psychiatrist primary credential
        @apiSuccess (Success Response) {Integer} [primary_specialty]
            Psychiatrist primary specialty
        @apiSuccess (Success Response) {String} [last_three_years_experiences]
            Psychiatrist last three years experiences
        @apiSuccess (Success Response) {String} [name_of_posts_of_the_last_3_years]
            Psychiatrist name of posts of the last 3 years
        @apiSuccess (Success Response) {Boolean} [applied_before] Psychiatrist applied before
        @apiSuccess (Success Response) {String} [more_information] Psychiatrist more information
        @apiSuccess (Success Response) {String} [more_data] Psychiatrist more data
        @apiSuccess (Success Response) {Plan} [plans] Psychiatrist plans
        @apiSuccess (Success Response) {Integer} [plans.price] Plan price
        @apiSuccess (Success Response) {Integer} [notification_count] Person notification count
        @apiSuccess (Success Response) {Boolean} [is_active] Is the psychiatrist active?
        @apiSuccess (Success Response) {Boolean} [is_enable] Is the psychiatrist enable?
        @apiSuccess (Success Response) {Boolean} [is_confirmed] Approved psychiatrist?
        @apiSuccess (Success Response) {Boolean} [is_profile_updated]
            Has the user profile been updated?
        """
        dic = User.to_json(self, details)
        dic['name'] = self.get_name()
        dic['first_name'] = self.first_name
        dic['last_name'] = self.last_name
        dic['photo'] = self.photo
        dic['attachment'] = self.attachment
        dic['score'] = self.score
        if details or (g.user_type == 'user' and g.user.id == self.id) or (g.user_type == 'admin'
           and g.user.get_access_level('psychiatrist', None) >= Permission.ACCESS_WRITE):
            dic['is_confirmed'] = self.is_confirmed
            dic['age'] = self.age
            dic['sex'] = self.sex
            dic['birth_date'] = date_to_string(self.birth_date) if self.birth_date else None
            dic['address'] = self.address
            dic['post_code'] = self.post_code
            dic['mobile'] = self.mobile
            dic['work_tel'] = self.work_tel
            dic['home_tel'] = self.home_tel
            dic['primary_credential'] = self.primary_credential
            dic['primary_specialty'] = self.primary_specialty
            dic['last_three_years_experiences'] = self.last_three_years_experiences
            dic['name_of_posts_of_the_last_3_years'] = self.name_of_posts_of_the_last_3_years
            dic['applied_before'] = self.applied_before
            dic['more_information'] = self.more_information
            dic['more_data'] = self.more_data
            dic['plans'] = [plan.to_json() for plan in self.plans]
            dic['notification_count'] = self.notification_count
        return dic

    def populate(self, json):
        User.populate(self, json)
        self.first_name = json.get('first_name')
        self.last_name = json.get('last_name')
        self.age = json.get('age')
        self.sex = json.get('sex')
        self.birth_date = string_to_datetime(json.get('birth_date'))\
            if 'birth_date' in json else None
        self.photo = json.get('photo')
        self.attachment = json.get('attachment')
        self.address = json.get('address')
        self.post_code = json.get('post_code')
        self.mobile = json.get('mobile')
        self.work_tel = json.get('work_tel')
        self.home_tel = json.get('home_tel')
        self.primary_credential = json.get('primary_credential')
        self.primary_specialty = json.get('primary_specialty')
        self.last_three_years_experiences = json.get('last_three_years_experiences')
        self.name_of_posts_of_the_last_3_years = json.get('name_of_posts_of_the_last_3_years')
        self.applied_before = json.get('applied_before')
        self.more_information = json.get('more_information')
        self.more_data = json.get('more_data')
        if json.get('plans'):
            self.plans = []
            for item in json.get('plans'):
                plan = Plan()
                plan.populate(item)
                self.plans.append(plan)

    def update_notification_count(self):
        from application.models import Meeting
        self.notification_count = Meeting.objects(
            psychiatrist=self, psychiatrist_have_notification=True).count()
        self.save()

    # mark: helper functions

    def get_name(self):
        return self.first_name + " " + self.last_name

    def update_score(self):
        from application.models import Meeting
        query = Meeting.objects(psychiatrist=self, status=Meeting.STATUS_COMPLETED, score__ne=0)
        self.score = 3 if query.count() == 0 else query.average('score')
        self.save()
