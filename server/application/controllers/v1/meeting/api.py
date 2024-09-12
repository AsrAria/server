# -*- coding: utf-8 -*-

# python imports
import os
import jwt
from datetime import datetime, timedelta

# flask imports
from flask import Blueprint, jsonify, request, g, current_app, send_file

# mongo imports
from mongoengine import DoesNotExist

# project imports
from application.models import User
from application.models import Meeting
from application.forms.upload import UploadForm


api = Blueprint('meeting.api.v1', __name__, url_prefix='/api/v1/meeting')


@api.route('/<id>/file', methods=['POST'])
@User.authenticate
def upload_file(id):
    """
    @apiVersion 1.0.0
    @apiGroup Meeting
    @apiName MeetingUploadFile
    @api {post} /v1/meeting/:id/file Upload meeting file

    @apiParam (URL Parameter) {String} id ID of desired meeting

    @apiUse AccessTokenHeader

    @apiUse UploadForm

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        form = UploadForm()
        if not form.validate():
            return jsonify(), 400

        meeting = Meeting.objects.get(id=id)

        if g.user.role == User.ROLE_PERSON:
            return jsonify(), 403

        if g.user.role == User.ROLE_ORGANIZATION:
            return jsonify(), 403

        if g.user.role == User.ROLE_PSYCHIATRIST and meeting.psychiatrist.id != g.user.id:
            return jsonify(), 403

        type = form.type.data
        if type not in ['attachment']:
            return jsonify(), 400

        # if not current_app.config['DEPLOYMENT']:
            # return jsonify(url=request.url + '/' + type), 201

        file_obj = form.file.data
        file_directory = meeting.get_attachment_path()

        directory_path = os.path.join(current_app.config['FILE_UPLOAD_DIR'], file_directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        file_address = os.path.join(directory_path, meeting.id + '_' + type)
        file_obj.seek(0)
        file_obj.save(file_address)

        return jsonify(url=request.url + '/' + type), 201
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/file/<type>', methods=['GET'])
@User.authenticate
def get_file(id, type):
    """
    @apiVersion 1.0.0
    @apiGroup Meeting
    @apiName MeetingGetFile
    @api {post} /v1/meeting/:id/file/:type Get meeting file

    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired meeting
    @apiParam (URL Parameter) {String} type Type of file

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        meeting = Meeting.objects.get(id=id)

        if type not in ['attachment']:
            return jsonify(), 400

        if g.user.role == User.ROLE_ORGANIZATION and g.user not in meeting.result.shared_with:
            return jsonify(), 403

        if g.user.role == User.ROLE_PERSON and meeting.person.id != g.user.id:
            return jsonify(), 403

        if g.user.role == User.ROLE_PSYCHIATRIST and meeting.psychiatrist.id != g.user.id:
            return jsonify(), 403

        if not current_app.config['DEPLOYMENT']:
            return jsonify(), 200

        file_directory = meeting.get_attachment_path()
        directory_path = os.path.join(current_app.config['FILE_UPLOAD_DIR'], file_directory)
        file_address = os.path.join(directory_path, meeting.id + '_' + type)
        return send_file(file_address)
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/address', methods=['GET'])
@User.authenticate
def get_address(id):
    """
    @apiVersion 1.0.0
    @apiGroup Meeting
    @apiName MeetingGetAddress
    @api {post} /v1/meeting/:id/address Get meeting address

    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired meeting

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        meeting = Meeting.objects.get(id=id)

        if meeting.status in [Meeting.STATUS_REJECTED, Meeting.STATUS_NEW]:
            return jsonify(), 400

        if g.user.role == User.ROLE_ORGANIZATION and g.user not in meeting.result.shared_with:
            return jsonify(), 403

        if g.user.role == User.ROLE_PERSON and meeting.person.id != g.user.id:
            return jsonify(), 403

        if g.user.role == User.ROLE_PSYCHIATRIST and meeting.psychiatrist.id != g.user.id:
            return jsonify(), 403

        KEY = current_app.config['JITSI']['key']
        APPNAME = current_app.config['JITSI']['app_name']
        SERVER = current_app.config['JITSI']['host']
        ROOM = meeting.id

        headers = {
            "typ": "JWT"
        }

        payload = {
            "context": {
                "user": {
                    "name": g.user.get_name(),
                    "id": g.user.id
                }
            },
            "aud": APPNAME,
            "iss": APPNAME,
            "sub": SERVER,
            "room": ROOM,
        }

        payload['exp'] = datetime.now() + timedelta(minutes=180)
        res = jwt.encode(payload, KEY, algorithm="HS256", headers=headers)
        return jsonify(url=f'https://{SERVER}/{ROOM}?jwt={res}'), 200
    except DoesNotExist:
        return jsonify(), 404
