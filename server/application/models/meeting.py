# -*- coding: utf-8 -*-

# python imports
from datetime import timedelta
from mongoengine import DateTimeField, IntField, StringField, ReferenceField, BooleanField

# flask imports
from flask import abort

# project imports
from application.models import Person
from application.models import TimeBox
from application.models import Document
from application.models import Psychiatrist
from application.models import BaseDocument
from application.utils.localize import localize
from application.utils.time import datetime_to_string, string_to_datetime


class Meeting(BaseDocument):

    # mark: constants

    STATUS_NEW = 0
    STATUS_ACCEPTED = 1
    STATUS_REJECTED = 2
    STATUS_COMPLETED = 3

    # mark: variables

    person_accepted = BooleanField(required=True, default=False)
    psychiatrist_accepted = BooleanField(required=True, default=False)

    status = IntField(required=True, default=STATUS_NEW)

    psychiatrist = ReferenceField(Psychiatrist, required=True)
    person = ReferenceField(Person, required=True)

    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    length = IntField(required=True)

    result = ReferenceField(Document)

    score = IntField(default=0)
    comment = StringField(default="")

    price = IntField(required=True)

    person_have_notification = BooleanField(required=True, default=False)
    psychiatrist_have_notification = BooleanField(required=True, default=False)

    # mark: meta

    meta = {
        'collection': 'meetings',
        'indexes': [
            'psychiatrist',
            'person',
            'start_time'
        ],
    }

    # mark: json functions

    def to_json(self):
        """
        @apiDefine MeetingToJson

        @apiSuccess (Success Response) {String} id Meeting id
        @apiSuccess (Success Response) {Integer} person_accepted
            Person accepted this meeting?
        @apiSuccess (Success Response) {Integer} psychiatrist_accepted
            Psychiatrist accepted this meeting?
        @apiSuccess (Success Response) {Integer} status
            Meeting status (waiting=0, accepted=1, completed=2)
        @apiSuccess (Success Response) {Person} person Meeting
            person (<a href="#api-Person-GetPerson">person object</a>)
        @apiSuccess (Success Response) {Psychiatrist} psychiatrist Meeting
            psychiatrist (<a href="#api-Psychiatrist-GetPsychiatrist">psychiatrist object</a>)
        @apiSuccess (Success Response) {String} result Meeting result
        @apiSuccess (Success Response) {String} attachment Meeting attachment
        @apiSuccess (Success Response) {Integer} score Meeting score
        @apiSuccess (Success Response) {String} comment Meeting comment
        @apiSuccess (Success Response) {Integer} price Meeting price
        @apiSuccess (Success Response) {String} start_time Meeting start time
        @apiSuccess (Success Response) {String} end_time Meeting end time
        @apiSuccess (Success Response) {Boolean} person_have_notification
            Person have a notification?
        @apiSuccess (Success Response) {Boolean} psychiatrist_have_notification
            Psychiatrist have a notification?
        @apiSuccess (Success Response) {Document} health_test Person latest health test
        """
        dic = {
            'id': self.id,
            'status': self.status,
            'person_accepted': self.person_accepted,
            'psychiatrist_accepted': self.psychiatrist_accepted,
            'person': self.person.to_json(),
            'psychiatrist': self.psychiatrist.to_json(),
            'result': "",
            'attachment': "",
            'score': self.score,
            'comment': self.comment,
            'price': self.price,
            'start_time': datetime_to_string(self.start_time),
            'end_time': datetime_to_string(self.end_time),
            'person_have_notification': self.person_have_notification,
            'psychiatrist_have_notification': self.psychiatrist_have_notification
        }
        if self.result:
            dic['result'] = self.result.data['result']
            dic['attachment'] = self.result.data['attachment']
        try:
            dic['health_test'] = Document.\
                objects(person=self.person, type=Document.TYPE_TEST).\
                order_by('-create_time')[0].to_json()
        except Exception:
            pass
        return dic

    def populate(self, person, psychiatrist, json):
        if person:
            self.person = person
        if 'person' in json:
            self.person = Person.objects.get(id=json['person'])
        if psychiatrist:
            self.psychiatrist = psychiatrist
        if 'psychiatrist' in json:
            self.psychiatrist = Psychiatrist.objects.get(id=json['psychiatrist'])
        if 'start_time' in json:
            self.start_time = string_to_datetime(json.get('start_time'))
        if 'length' in json:
            self.end_time = self.start_time + timedelta(minutes=30*(json['length'] + 1))
            self.length = (self.end_time - self.start_time).seconds
        if 'result' in json and 'attachment' in json:
            if not self.result:
                self.result = Document()
            self.result.populate_meeting_result(self, json)
            self.result.save()
        if 'score' in json:
            self.score = json['score']
        if 'comment' in json:
            self.comment = json['comment']
        if 'length' in json and self.price is None and self.psychiatrist:
            self.price = 0
            if len(self.psychiatrist.plans) > json['length']:
                self.price = self.psychiatrist.plans[json['length']].price

    def update_status(self, person_accepted, psychiatrist_accepted):
        if self.status == Meeting.STATUS_COMPLETED \
           or self.status == Meeting.STATUS_REJECTED:
            abort(400)

        if person_accepted is not None:
            self.person_accepted = person_accepted
        if psychiatrist_accepted is not None:
            self.psychiatrist_accepted = psychiatrist_accepted

        if self.status == Meeting.STATUS_NEW:
            if self.person_accepted and self.psychiatrist_accepted:
                self.status = Meeting.STATUS_ACCEPTED
                return

        if self.status == Meeting.STATUS_ACCEPTED:
            if not self.person_accepted or not self.psychiatrist_accepted:
                self.status = Meeting.STATUS_REJECTED
                return

    # mark: helper functions

    def get_attachment_path(self):
        return 'meeting/attachment/%s/%s/%s' % (self.id[0], self.id[1], self.id[2])

    def check_conflict(self):
        if Meeting.objects(
            id__ne=self.id,
            person=self.person,
            status__ne=Meeting.STATUS_REJECTED,
            start_time__lte=self.start_time,
            end_time__gt=self.start_time
        ).count() > 0:
            return localize('meeting_conflict_error')

        if Meeting.objects(
            id__ne=self.id,
            person=self.person,
            status__ne=Meeting.STATUS_REJECTED,
            start_time__lt=self.end_time,
            end_time__gte=self.end_time
        ).count() > 0:
            return localize('meeting_conflict_error')

        if Meeting.objects(
            id__ne=self.id,
            person=self.person,
            status__ne=Meeting.STATUS_REJECTED,
            start_time__gte=self.start_time,
            end_time__lte=self.end_time
        ).count() > 0:
            return localize('meeting_conflict_error')

        if Meeting.objects(
            id__ne=self.id,
            psychiatrist=self.psychiatrist,
            status__ne=Meeting.STATUS_REJECTED,
            start_time__lte=self.start_time,
            end_time__gt=self.start_time
        ).count() > 0:
            return localize('meeting_conflict_error')

        if Meeting.objects(
            id__ne=self.id,
            psychiatrist=self.psychiatrist,
            status__ne=Meeting.STATUS_REJECTED,
            start_time__lt=self.end_time,
            end_time__gte=self.end_time
        ).count() > 0:
            return localize('meeting_conflict_error')

        if Meeting.objects(
            id__ne=self.id,
            psychiatrist=self.psychiatrist,
            status__ne=Meeting.STATUS_REJECTED,
            start_time__gte=self.start_time,
            end_time__lte=self.end_time
        ).count() > 0:
            return localize('meeting_conflict_error')

        if TimeBox.objects(
            psychiatrist=self.psychiatrist,
            start_time__lte=self.start_time,
            end_time__gte=self.end_time
        ).count() == 0:
            return localize('meeting_time_box_not_found_error')

        return None

    def set_person_have_notification(self, status):
        self.person_have_notification = status
        self.save()
        self.person.update_notification_count()

    def set_psychiatrist_have_notification(self, status):
        self.psychiatrist_have_notification = status
        self.save()
        self.psychiatrist.update_notification_count()
