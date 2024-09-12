# -*- coding: utf-8 -*-

# flask imports
from flask import g

# python imports
from mongoengine import IntField, DictField, ReferenceField, ListField, PULL

# project imports
from application.models import User
from application.models import Person
from application.models import BaseDocument
from application.utils.time import datetime_to_string, date_to_string
from application.utils.questionnaire import calculate_result


class Document(BaseDocument):

    # mark: constants

    TYPE_TEST = 0
    TYPE_MEETING = 1

    # mark: variables

    type = IntField(required=True, default=TYPE_TEST)

    person = ReferenceField(Person, required=True)
    creator = ReferenceField(User)

    data = DictField(required=True)

    shared_with = ListField(ReferenceField(User, reverse_delete_rule=PULL))

    # mark: meta

    meta = {
        'collection': 'documents',
        'indexes': [
            'person'
        ],
    }

    # mark: json functions

    def to_json(self):
        """
        @apiDefine DocumentToJson

        @apiSuccess (Success Response) {String} id Document id
        @apiSuccess (Success Response) {String} type Document type (test=0, meeting=1)
        @apiSuccess (Success Response) {Object} data Document data
        @apiSuccess (Success Response) {User} [creator] Document creator
        @apiSuccess (Success Response) {String} creator.id User id
        @apiSuccess (Success Response) {String} creator.name User name
        @apiSuccess (Success Response) {User} [shared_with]
            The document is shared with these users (owner only)
        @apiSuccess (Success Response) {String} shared_with.id User id
        @apiSuccess (Success Response) {String} shared_with.name User name
        @apiSuccess (Success Response) {String} [create_time]
            Document create time (ISO format yyyy-mm-ddThh:mm:ss)
        """
        dic = {
            'id': self.id,
            'type': self.type,
            'data': self.data,
            'create_time': datetime_to_string(self.create_time)
        }
        if self.type == Document.TYPE_TEST:
            dic['data'] = {
                'result': calculate_result(self.person, [0] + self.data['choices']),
                'history': [
                    Document.create_history_item(
                        calculate_result(self.person, [0] + item.data['choices']), item.create_time)
                    for item in Document.objects(person=self.person, type=Document.TYPE_TEST)
                    .order_by('-create_time').limit(5)
                ]
            }
        if self.creator:
            dic['creator'] = {
                'id': self.creator.id,
                'name': self.creator.get_name()
            }
        if g.user_type == 'user' and g.user.id == self.person.id:
            dic['shared_with'] = [
                {'id': user.id, 'name': user.get_name()} for user in self.shared_with]
        return dic

    def populate(self, json):
        self.shared_with = []
        for user in json['shared_with']:
            self.shared_with.append(User.objects.get(id=user))

    def populate_test_result(self, json):
        self.type = Document.TYPE_TEST
        self.person = g.user
        self.creator = g.user
        self.data = json

    def populate_meeting_result(self, meeting, json):
        self.type = Document.TYPE_MEETING
        self.person = meeting.person
        self.creator = meeting.psychiatrist
        self.data = {
            'result': json['result'],
            'attachment': json['attachment']
        }

    # mark: history body

    @classmethod
    def create_history_item(cls, result, create_time):
        dic = {}
        if 'items' in result:
            for item in result['items']:
                dic[item['name']] = item['final_br']

        dic['date'] = date_to_string(create_time)
        return dic
