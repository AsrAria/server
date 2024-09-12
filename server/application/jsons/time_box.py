# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField


class TimeBox(Document):
    """
    @apiDefine TimeBoxJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} start_time
        Start time of the time box (ISO format yyyy-mm-ddThh:mm:ss)
    @apiParam (Body Parameter) {String} end_time
        End time of the time box (ISO format yyyy-mm-ddThh:mm:ss)
    """
    start_time = StringField(required=True)
    end_time = StringField(required=True)
