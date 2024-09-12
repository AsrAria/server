# -*- coding: utf-8 -*-

# python imports
from wtforms import FileField, StringField
from wtforms.validators import DataRequired

# flask imports
from flask_wtf import FlaskForm


class UploadForm(FlaskForm):
    """
    @apiDefine UploadForm

    @apiParam (Form Parameter) {String} type File type
    @apiParam (Form Parameter) {File} file File content, Max file size is 10MB
    """
    file = FileField(validators=[DataRequired()])
    type = StringField(validators=[DataRequired()])
