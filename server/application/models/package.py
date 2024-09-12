# -*- coding: utf-8 -*-

# python imports
from mongoengine import IntField, DateField, ReferenceField

# project imports
from application.models import User
from application.models import Person
from application.models import Organization
from application.models import BaseDocument
from application.utils.localize import localize
from application.utils.time import date_to_string, string_to_datetime


class Package(BaseDocument):

    # mark: variables

    person = ReferenceField(Person, required=True)
    organization = ReferenceField(Organization, required=True)

    start_date = DateField(required=True)
    end_date = DateField(required=True)

    budget = IntField(required=True)
    balance = IntField(required=True, default=0)

    # mark: meta

    meta = {
        'collection': 'packages',
        'indexes': [
            'person',
            'organization'
        ],
    }

    # mark: json functions

    def to_json(self):
        """
        @apiDefine PackageToJson

        @apiSuccess (Success Response) {String} id Package id
        @apiSuccess (Success Response) {Person} person
            Package person (<a href="#api-Person-GetPerson">person object</a>)
        @apiSuccess (Success Response) {Person} organization Package
            organization (<a href="#api-Organization-GetOrganization">organization object</a>)
        @apiSuccess (Success Response) {String} start_date Package start date
        @apiSuccess (Success Response) {String} end_date Package end date
        @apiSuccess (Success Response) {Integer} budget Package budget
        @apiSuccess (Success Response) {Integer} balance Package balance
        """
        return {
            'id': self.id,
            'person': self.person.to_json(),
            'organization': self.organization.to_json(),
            'start_date': date_to_string(self.start_date),
            'end_date': date_to_string(self.end_date),
            'budget': self.budget,
            'balance': self.balance,
        }

    def populate(self, organization, json):
        self.organization = organization
        try:
            self.person = Person.objects.get(email=json.get('person').lower())
        except Exception:
            self.person = User.create({
                'role': User.ROLE_PERSON,
                'email': json.get('person').lower()
            })
        self.start_date = string_to_datetime(json.get('start_date'))
        self.end_date = string_to_datetime(json.get('end_date'))
        self.budget = json.get('budget')

    def update_balance(self):
        from application.models import Meeting
        balance = Meeting.objects(person=self.person, status=Meeting.STATUS_COMPLETED).sum('price')
        self.balance = min(self.budget, balance)
        self.save()
        self.person.update_balance()
        self.organization.update_balance()

    # mark: helper functions

    def check_conflict(self):
        if self.end_date < self.start_date:
            return localize('package_order_error')

        if Package.objects(
            person=self.person,
            start_date__lte=self.start_date,
            end_date__gte=self.start_date
        ).count() > 0:
            return localize('package_conflict_error')

        if Package.objects(
            person=self.person,
            start_date__lte=self.end_date,
            end_date__gte=self.end_date
        ).count() > 0:
            return localize('package_conflict_error')

        if Package.objects(
            person=self.person,
            start_date__gte=self.start_date,
            end_date__lte=self.end_date
        ).count() > 0:
            return localize('package_conflict_error')

        return None
