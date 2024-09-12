# -*- coding: utf-8 -*-

# flask imports
from flask import g

# python imports
from mongoengine import StringField, IntField, DateField

# project imports
from application.models import User
from application.models import Permission
from application.utils.time import date_to_string, string_to_datetime


class Person(User):

    # mark: variables

    first_name = StringField(default="")
    last_name = StringField(default="")

    age = IntField()
    sex = IntField()

    birth_date = DateField()
    photo = StringField(default="")

    address = StringField(default="")
    post_code = StringField(default="")

    mobile = StringField(default="")
    work_tel = StringField(default="")
    home_tel = StringField(default="")

    duration_of_hospitalization = IntField()

    illness_severity = StringField(default="")
    disease_background = StringField(default="")
    family_disease_background = StringField(default="")
    history_of_drug_use = StringField(default="")
    family_history_of_drug_use = StringField(default="")

    birth_order = IntField()
    number_of_children_in_family = IntField()

    more_information = StringField(default="")

    balance = IntField(required=True, default=0)
    notification_count = IntField(required=True, default=0)

    # mark: meta

    meta = {
    }

    # mark: json functions

    def to_json(self, details=False):
        """
        @apiDefine PersonToJson

        @apiSuccess (Success Response) {String} id Person id
        @apiSuccess (Success Response) {String} email Person email
        @apiSuccess (Success Response) {String} name Person name
        @apiSuccess (Success Response) {String} [first_name] Person first name
        @apiSuccess (Success Response) {String} [last_name] Person last name
        @apiSuccess (Success Response) {Integer} [age] Person age
        @apiSuccess (Success Response) {Integer} [sex] Person sex
        @apiSuccess (Success Response) {String} [birth_date] Person birth date
        @apiSuccess (Success Response) {String} [photo] Person photo
        @apiSuccess (Success Response) {String} [address] Person address
        @apiSuccess (Success Response) {String} [post_code] Person post code
        @apiSuccess (Success Response) {String} [mobile] Person mobile
        @apiSuccess (Success Response) {String} [work_tel] Person work tel
        @apiSuccess (Success Response) {String} [home_tel] Person home tel
        @apiSuccess (Success Response) {Integer} [duration_of_hospitalization]
            Person duration of hospitalization
        @apiSuccess (Success Response) {String} [illness_severity] Person illness severity
        @apiSuccess (Success Response) {String} [disease_background] Person disease background
        @apiSuccess (Success Response) {String} [family_disease_background]
            Person family disease background
        @apiSuccess (Success Response) {String} [history_of_drug_use] Person history of drug use
        @apiSuccess (Success Response) {String} [family_history_of_drug_use]
            Person family history of drug use
        @apiSuccess (Success Response) {Integer} [birth_order] Person birth order
        @apiSuccess (Success Response) {Integer} [number_of_children_in_family]
            Person number of children in family
        @apiSuccess (Success Response) {String} [more_information] Person more information
        @apiSuccess (Success Response) {Integer} [balance] Person balance
        @apiSuccess (Success Response) {Integer} [notification_count] Person notification count
        @apiSuccess (Success Response) {Boolean} [is_active] Is the person active?
        @apiSuccess (Success Response) {Boolean} [is_enable] Is the person enable?
        @apiSuccess (Success Response) {Boolean} [is_profile_updated]
            Has the user profile been updated?
        """
        dic = User.to_json(self, details)
        dic['name'] = self.get_name()
        dic['first_name'] = self.first_name
        dic['last_name'] = self.last_name
        if details or (g.user_type == 'user' and g.user.id == self.id) or (g.user_type == 'admin'
           and g.user.get_access_level('person', None) >= Permission.ACCESS_WRITE):
            dic['age'] = self.age
            dic['sex'] = self.sex
            dic['birth_date'] = date_to_string(self.birth_date) if self.birth_date else None
            dic['photo'] = self.photo
            dic['address'] = self.address
            dic['post_code'] = self.post_code
            dic['mobile'] = self.mobile
            dic['work_tel'] = self.work_tel
            dic['home_tel'] = self.home_tel
            dic['duration_of_hospitalization'] = self.duration_of_hospitalization
            dic['illness_severity'] = self.illness_severity
            dic['disease_background'] = self.disease_background
            dic['family_disease_background'] = self.family_disease_background
            dic['history_of_drug_use'] = self.history_of_drug_use
            dic['family_history_of_drug_use'] = self.family_history_of_drug_use
            dic['birth_order'] = self.birth_order
            dic['number_of_children_in_family'] = self.number_of_children_in_family
            dic['more_information'] = self.more_information
            dic['balance'] = self.balance
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
        self.address = json.get('address')
        self.post_code = json.get('post_code')
        self.mobile = json.get('mobile')
        self.work_tel = json.get('work_tel')
        self.home_tel = json.get('home_tel')
        self.duration_of_hospitalization = json.get('duration_of_hospitalization')
        self.illness_severity = json.get('illness_severity')
        self.disease_background = json.get('disease_background')
        self.family_disease_background = json.get('family_disease_background')
        self.history_of_drug_use = json.get('history_of_drug_use')
        self.family_history_of_drug_use = json.get('family_history_of_drug_use')
        self.birth_order = json.get('birth_order')
        self.number_of_children_in_family = json.get('number_of_children_in_family')
        self.more_information = json.get('more_information')

    def update_balance(self):
        from application.models import Package, Meeting, Payment
        self.balance = Meeting.objects(person=self, status=Meeting.STATUS_COMPLETED).sum('price') \
            - Package.objects(person=self).sum('balance') \
            - Payment.objects(user=self, status=Payment.STATUS_SUCCESS).sum('amount')
        self.save()

    def update_notification_count(self):
        from application.models import Meeting
        self.notification_count = Meeting.objects(
            person=self, person_have_notification=True).count()
        self.save()

    # mark: helper functions

    def get_name(self):
        return self.first_name + " " + self.last_name
