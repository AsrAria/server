# -*- coding: utf-8 -*-

# jsonschema imports
from jsl import Document, StringField, IntField, \
    ArrayField, DocumentField

# project imports
from application.utils.pattern import Pattern


class Permission(Document):
    name = StringField(required=True)
    access_level = IntField(required=True)
    sub_permissions = ArrayField(DocumentField("Permission"))


class AdminCreate(Document):
    """
    @apiDefine AdminCreateJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} name Admin name
    @apiParam (Body Parameter) {String} email Admin email
    @apiParam (Body Parameter) {String} username Admin username
    @apiParam (Body Parameter) {String} password Admin password (pattern='^[A-Za-z0-9]{5,}$')
    @apiParam (Body Parameter) {Permission[]} permissions Admin permissions
    @apiParam (Body Parameter) {String} [permissions.name] Permission name
    @apiParam (Body Parameter) {Integer} [permissions.access_level]
        Permission access level (none=0, read=1, write=2)
    @apiParam (Body Parameter) {Permission[]} [permissions.sub_permissions]
        Sub permission of permissions
    """
    name = StringField(required=True)
    email = StringField(pattern=Pattern.PATTERN_EMAIL)
    username = StringField(required=True)
    password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)
    permissions = ArrayField(DocumentField(Permission), required=True)


class AdminUpdate(Document):
    """
    @apiDefine AdminUpdateJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} name Admin name
    @apiParam (Body Parameter) {String} email Admin email
    @apiParam (Body Parameter) {String} password Admin password (pattern='^[A-Za-z0-9]{5,}$')
    @apiParam (Body Parameter) {Permission[]} permissions Admin permissions
    @apiParam (Body Parameter) {String} [permissions.name] Permission name
    @apiParam (Body Parameter) {Integer} [permissions.access_level]
        Permission access level (none=0, read=1, write=2)
    @apiParam (Body Parameter) {Permission[]} [permissions.sub_permissions]
        Sub permission of permissions
    """
    name = StringField()
    email = StringField(pattern=Pattern.PATTERN_EMAIL)
    password = StringField(pattern=Pattern.PATTERN_PASSWORD)
    permissions = ArrayField(DocumentField(Permission), required=True)


class AdminAuthenticate(Document):
    """
    @apiDefine AdminAuthenticateJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} username Admin username
    @apiParam (Body Parameter) {String} password Admin password (pattern='^[A-Za-z0-9]{5,}$')
    """
    username = StringField(required=True)
    password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)


class AdminActivate(Document):
    """
    @apiDefine AdminActivateJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} code Activation code for the admin
    @apiParam (Body Parameter) {String} username User name of the admin
    """
    code = StringField(required=True, pattern=Pattern.PATTERN_ACTIVATION_CODE)
    username = StringField(required=True)


class AdminUpdateProfile(Document):
    """
    @apiDefine AdminUpdateProfileJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} name Admin name
    @apiParam (Body Parameter) {String} email Admin email
    """
    name = StringField()
    email = StringField(pattern=Pattern.PATTERN_EMAIL)


class AdminChangePassword(Document):
    """
    @apiDefine AdminChangePasswordJson

    @apiHeader {String} Content-Type JSON (application/json)

    @apiParam (Body Parameter) {String} old_password
        Old password of this admin. (pattern='^[A-Za-z0-9]{5,}$')
    @apiParam (Body Parameter) {String} new_password
        New password of this admin. (pattern='^[A-Za-z0-9]{5,}$')
    """
    old_password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)
    new_password = StringField(required=True, pattern=Pattern.PATTERN_PASSWORD)
