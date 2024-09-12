# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField, BooleanField


class CreatePsychiatristMeeting(Document):
    """
    @apiDefine CreatePsychiatristMeetingJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} person ID of desired person
    @apiParam (Body Parameter) {String} start_time
        Start time of the meeting (ISO format yyyy-mm-ddThh:mm:ss)
    @apiParam (Body Parameter) {Integer} length Length of meeting (0=30min, 1=60min, 2=90min)
    """
    person = StringField(required=True)
    start_time = StringField(required=True)
    length = IntField(required=True, minimum=0, maximum=2)


class UpdatePsychiatristMeeting(Document):
    """
    @apiDefine UpdatePsychiatristMeetingJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} [accepted] Is the meeting accepted?
    @apiParam (Body Parameter) {String} [result] Result of meeting
    @apiParam (Body Parameter) {String} [attachment] Attachment of meeting
    """
    accepted = BooleanField()
    result = StringField()
    attachment = StringField()


class CreatePersonMeeting(Document):
    """
    @apiDefine CreatePersonMeetingJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} psychiatrist ID of desired psychiatrist
    @apiParam (Body Parameter) {String} start_time
        Start time of the meeting (ISO format yyyy-mm-ddThh:mm:ss)
    @apiParam (Body Parameter) {Integer} length Length of meeting (0=30min, 1=60min, 2=90min)
    """
    psychiatrist = StringField(required=True)
    start_time = StringField(required=True)
    length = IntField(required=True, minimum=0, maximum=2)


class UpdatePersonMeeting(Document):
    """
    @apiDefine UpdatePersonMeetingJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} [accepted] Is the meeting accepted?
    @apiParam (Body Parameter) {Integer} [score] Score of meeting (1-5)
    @apiParam (Body Parameter) {String} [comment] Comment of meeting
    """
    accepted = BooleanField()
    score = IntField(minimum=1, maximum=5)
    comment = StringField()
