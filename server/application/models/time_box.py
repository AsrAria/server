# -*- coding: utf-8 -*-

# python imports
from mongoengine import DateTimeField, ReferenceField, IntField

# project imports
from application.models import Psychiatrist
from application.models import BaseDocument
from application.utils.localize import localize
from application.utils.time import datetime_to_string, string_to_datetime


class TimeBox(BaseDocument):

    # mark: variables

    psychiatrist = ReferenceField(Psychiatrist, required=True)

    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    length = IntField(required=True)

    # mark: meta

    meta = {
        'collection': 'time_boxes',
        'indexes': [
            'psychiatrist',
            'start_time'
        ],
    }

    # mark: json functions

    def to_json(self):
        """
        @apiDefine TimeBoxToJson

        @apiSuccess (Success Response) {String} id TimeBox id
        @apiSuccess (Success Response) {Psychiatrist} psychiatrist Time box
            psychiatrist (<a href="#api-Psychiatrist-GetPsychiatrist">psychiatrist object</a>)
        @apiSuccess (Success Response) {String} start_time TimeBox start time
        @apiSuccess (Success Response) {String} end_time TimeBox end time
        """
        return {
            'id': self.id,
            'psychiatrist': self.psychiatrist.to_json(),
            'start_time': datetime_to_string(self.start_time),
            'end_time': datetime_to_string(self.end_time)
        }

    def populate(self, psychiatrist, json):
        self.psychiatrist = psychiatrist
        self.start_time = string_to_datetime(json.get('start_time'))
        self.end_time = string_to_datetime(json.get('end_time'))
        self.length = (self.end_time - self.start_time).seconds

    # mark: helper functions

    def check_conflict(self):
        if self.end_time < self.start_time:
            return localize('time_box_order_error')

        if TimeBox.objects(
            psychiatrist=self.psychiatrist,
            start_time__lte=self.start_time,
            end_time__gt=self.start_time
        ).count() > 0:
            return localize('time_box_conflict_error')

        if TimeBox.objects(
            psychiatrist=self.psychiatrist,
            start_time__lt=self.end_time,
            end_time__gte=self.end_time
        ).count() > 0:
            return localize('time_box_conflict_error')

        if TimeBox.objects(
            psychiatrist=self.psychiatrist,
            start_time__gte=self.start_time,
            end_time__lte=self.end_time
        ).count() > 0:
            return localize('time_box_conflict_error')

        return None
