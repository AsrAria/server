# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField

# project imports
from application.utils.pattern import Pattern


class Register(Document):
    """
    @apiDefine RegisterJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} role User role (person=0, psychiatrist=1, organization=2)
    @apiParam (Body Parameter) {String} email Email of the user
    @apiParam (Body Parameter) {String} password Password of the user (pattern='^[A-Za-z0-9]{8,}$')
    """
    role = IntField(required=True, minimum=0, maximum=2)
    email = StringField(required=True, pattern=Pattern.PATTERN_EMAIL)
    password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)


class Activate(Document):
    """
    @apiDefine ActivateJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} code Activation code for the user
    @apiParam (Body Parameter) {String} email Email of the user
    """
    code = StringField(required=True, pattern=Pattern.PATTERN_ACTIVATION_CODE)
    email = StringField(required=True, pattern=Pattern.PATTERN_EMAIL)


class SendActivateCode(Document):
    """
    @apiDefine SendActivateCodeJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} email Email of the user
    @apiParam (Body Parameter) {String} password Password of the user (pattern='^[A-Za-z0-9]{8,}$')
    """
    email = StringField(required=True, pattern=Pattern.PATTERN_EMAIL)
    password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)


class RefreshToken(Document):
    """
    @apiDefine RefreshTokenJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} access_token Access token of the user
    @apiParam (Body Parameter) {String} refresh_token Refresh token of the user
    """
    access_token = StringField(required=True, pattern=Pattern.PATTERN_TOKEN)
    refresh_token = StringField(required=True, pattern=Pattern.PATTERN_TOKEN)


class UserEdit(Document):
    """
    @apiDefine UserEditJson

    @apiHeader {String} Content-Type JSON (application/json)
    """


class UserChangePassword(Document):
    """
    @apiDefine UserChangePasswordJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} old_password
        Old password of this user. (pattern='^[A-Za-z0-9]{8,}$')
    @apiParam (Body Parameter) {String} new_password
        New password of this user. (pattern='^[A-Za-z0-9]{8,}$')
    """
    old_password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)
    new_password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)


class UserRecoverPassword(Document):
    """
    @apiDefine UserRecoverPasswordJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} email User email
    """
    email = StringField(required=True, pattern=Pattern.PATTERN_EMAIL)


class UserSetPassword(Document):
    """
    @apiDefine UserSetPasswordJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} token Recover token
    @apiParam (Body Parameter) {String} new_password
        New password of this user. (pattern='^[A-Za-z0-9]{8,}$')
    """
    token = StringField(required=True)
    new_password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)
