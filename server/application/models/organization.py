# -*- coding: utf-8 -*-

# flask imports
from flask import g

# flask imports
from mongoengine import BooleanField, StringField, IntField

# project imports
from application.models import User
from application.models import Permission


class Organization(User):

    # mark: variables

    is_confirmed = BooleanField(required=True, default=False)

    name = StringField(default="")

    field_of_activity = StringField(default="")

    number_of_staff = IntField()

    applied_before = BooleanField(default=False)

    manager_name = StringField(default="")
    operator_name = StringField(default="")

    address = StringField(default="")
    post_code = StringField(default="")

    work_tel = StringField(default="")
    work_fax = StringField(default="")

    purpose_for_taking_the_test = StringField(default="")

    more_information = StringField(default="")
    more_data = StringField(default="")

    balance = IntField(required=True, default=0)

    # mark: meta

    meta = {
    }

    # mark: json functions

    def to_json(self, details=False):
        """
        @apiDefine OrganizationToJson

        @apiSuccess (Success Response) {String} id Organization id
        @apiSuccess (Success Response) {String} email Organization email
        @apiSuccess (Success Response) {String} name Organization name
        @apiSuccess (Success Response) {String} [field_of_activity] Organization field of activity
        @apiSuccess (Success Response) {Integer} [number_of_staff] Organization number of staff
        @apiSuccess (Success Response) {Boolean} [applied_before] Organization applied before
        @apiSuccess (Success Response) {String} [manager_name] Organization manager name
        @apiSuccess (Success Response) {String} [operator_name] Organization operator name
        @apiSuccess (Success Response) {String} [address] Organization address
        @apiSuccess (Success Response) {String} [post_code] Organization post code
        @apiSuccess (Success Response) {String} [work_tel] Organization work tel
        @apiSuccess (Success Response) {String} [work_fax] Organization home fax
        @apiSuccess (Success Response) {String} [purpose_for_taking_the_test]
            Organization purpose for taking the test
        @apiSuccess (Success Response) {String} [more_information] Organization more information
        @apiSuccess (Success Response) {String} [more_data] Organization more data
        @apiSuccess (Success Response) {Integer} [balance] Organization balance
        @apiSuccess (Success Response) {Boolean} [is_active] Is the organization active?
        @apiSuccess (Success Response) {Boolean} [is_enable] Is the organization enable?
        @apiSuccess (Success Response) {Boolean} [is_confirmed] Approved organization?
        @apiSuccess (Success Response) {Boolean} [is_profile_updated]
            Has the user profile been updated?
        """
        dic = User.to_json(self, details)
        dic['name'] = self.name
        if details or (g.user_type == 'user' and g.user.id == self.id) or (g.user_type == 'admin'
           and g.user.get_access_level('organization', None) >= Permission.ACCESS_WRITE):
            dic['is_confirmed'] = self.is_confirmed
            dic['field_of_activity'] = self.field_of_activity
            dic['number_of_staff'] = self.number_of_staff
            dic['applied_before'] = self.applied_before
            dic['manager_name'] = self.manager_name
            dic['operator_name'] = self.operator_name
            dic['address'] = self.address
            dic['post_code'] = self.post_code
            dic['work_tel'] = self.work_tel
            dic['work_fax'] = self.work_fax
            dic['purpose_for_taking_the_test'] = self.purpose_for_taking_the_test
            dic['more_information'] = self.more_information
            dic['more_data'] = self.more_data
            dic['balance'] = self.balance
        return dic

    def populate(self, json):
        User.populate(self, json)
        self.name = json.get('name')
        self.field_of_activity = json.get('field_of_activity')
        self.number_of_staff = json.get('number_of_staff')
        self.applied_before = json.get('applied_before')
        self.manager_name = json.get('manager_name')
        self.operator_name = json.get('operator_name')
        self.address = json.get('address')
        self.post_code = json.get('post_code')
        self.work_tel = json.get('work_tel')
        self.work_fax = json.get('work_fax')
        self.purpose_for_taking_the_test = json.get('purpose_for_taking_the_test')
        self.more_information = json.get('more_information')
        self.more_data = json.get('more_data')

    def update_balance(self):
        from application.models import Package
        self.balance = Package.objects(organization=self).sum('balance')
        self.save()

    # mark: helper functions

    def get_name(self):
        return self.name
