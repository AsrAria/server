# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField, ArrayField


class DocumentShare(Document):
    """
    @apiDefine DocumentShareJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String[]} shared_with The document is shared with these users
    """
    shared_with = ArrayField(StringField(), required=True)


class DocumentSubmitTest(Document):
    """
    @apiDefine DocumentSubmitTestJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {Integer[]} choices Choices made for questions
    """
    choices = ArrayField(IntField(minimum=1, maximum=2),
                         required=True, min_items=175, max_items=175)
