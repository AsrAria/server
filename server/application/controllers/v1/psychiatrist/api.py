# -*- coding: utf-8 -*-

# python imports
from datetime import timedelta

# flask imports
from flask import Blueprint, jsonify, request, g
from flask_jsonschema import validate

# mongo imports
from mongoengine import DoesNotExist

# project imports
from application.models import User
from application.models import Admin
from application.models import Meeting
from application.models import TimeBox
from application.models import Psychiatrist
from application.models import Permission
from application.extensions import email
from application.utils.localize import localize
from application.utils.pagination import paginate
from application.utils.authenticate import authenticate
from application.utils.time import string_to_datetime


api = Blueprint('psychiatrist.api.v1', __name__, url_prefix='/api/v1/psychiatrist')


@api.route('', methods=['GET'])
@Admin.authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_READ)
@paginate(key='list', max_per_page=50)
def get_list():
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName GetPsychiatristList
    @api {get} /v1/psychiatrist Get psychiatrist list

    @apiUse Paginate

    @apiUse SecretKeyHeader

    @apiParam (Query Parameter) {String} [email] Filter by email
    @apiParam (Query Parameter) {String} [is_confirmed] Filter by is_confirmed field (true, false)

    @apiSuccess (Success Response) {Psychiatrist[]} list
        List of <a href="#api-Psychiatrist-GetPsychiatrist">psychiatrist object</a>

    @apiUse OK
    @apiUse Unauthorized
    """
    try:
        query = Psychiatrist.objects().order_by('-create_time')

        if request.args.get('email'):
            query = query.filter(email__contains=request.args['email'].lower())

        if request.args.get('is_confirmed'):
            query = query.filter(is_confirmed=(request.args['is_confirmed'] == 'true'))

        return query
    except Exception:
        return jsonify(), 400


@api.route('/<id>', methods=['GET'])
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_READ, True)
def get_psychiatrist(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName GetPsychiatrist
    @api {get} /v1/psychiatrist/:id Get a psychiatrist

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse PsychiatristToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        return jsonify(psychiatrist.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>', methods=['PUT'])
@validate('psychiatrist_edit')
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_WRITE, True)
def update(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName UpdatePsychiatrist
    @api {put} /v1/psychiatrist/:id Update a psychiatrist

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse PsychiatristEditJson
    @apiUse PsychiatristToJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    """
    try:
        json = request.json

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        psychiatrist.update(json)

        if g.user_type == 'user':
            psychiatrist.is_profile_updated = True
            psychiatrist.save()

        return jsonify(psychiatrist.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/confirm', methods=['POST'])
@Admin.authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_WRITE)
def confirm(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName ConfirmPsychiatrist
    @api {post} /v1/psychiatrist/:id/confirm Confirm psychiatrist

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiUse SecretKeyHeader

    @apiUse PsychiatristToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        psychiatrist = Psychiatrist.objects.get(id=id)
        psychiatrist.is_confirmed = True
        psychiatrist.save()
        email.send(
            psychiatrist.email,
            psychiatrist.get_name(),
            localize('your_activation_status_title'),
            localize('your_activation_confirmed_message')
        )
        return jsonify(psychiatrist.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/reject', methods=['POST'])
@Admin.authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_WRITE)
def reject(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName RejectPsychiatrist
    @api {post} /v1/psychiatrist/:id/reject Reject psychiatrist

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiUse SecretKeyHeader

    @apiUse PsychiatristToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        psychiatrist = Psychiatrist.objects.get(id=id)
        psychiatrist.is_confirmed = False
        psychiatrist.save()
        email.send(
            psychiatrist.email,
            psychiatrist.get_name(),
            localize('your_activation_status_title'),
            localize('your_activation_rejected_message')
        )
        return jsonify(psychiatrist.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/time_box', methods=['GET'])
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_psychiatrist_time_box_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName GetPsychiatristTimeBoxList
    @api {get} /v1/psychiatrist/:id/time_box Get psychiatrist time box list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiParam (Query Parameter) {String} [date] Filter by date (ISO format yyyy-mm-dd)

    @apiSuccess (Success Response) {TimeBox[]} list
        List of <a href="#api-Psychiatrist-GetPsychiatristTimeBox">time box object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        query = TimeBox.objects(psychiatrist=psychiatrist).order_by('-create_time')

        if request.args.get('date'):
            date = string_to_datetime(request.args.get('date'))
            query = query.filter(start_time__gte=date, start_time__lt=date + timedelta(days=1))

        return query
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/time_box/<time_box_id>', methods=['GET'])
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_READ, True)
def get_psychiatrist_time_box(id, time_box_id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName GetPsychiatristTimeBox
    @api {get} /v1/psychiatrist/:id/time_box/:time_box_id Get a psychiatrist time box

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist
    @apiParam (URL Parameter) {String} time_box_id ID of desired time box

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse TimeBoxToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        time_box = TimeBox.objects.get(id=time_box_id)
        if time_box.psychiatrist.id != psychiatrist.id:
            return jsonify(), 403

        return jsonify(time_box.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/time_box', methods=['POST'])
@validate('time_box')
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_WRITE, True)
def create_psychiatrist_time_box(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName CreatePsychiatristTimeBox
    @api {post} /v1/psychiatrist/:id/time_box Create a psychiatrist time box

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse TimeBoxJson
    @apiUse TimeBoxToJson

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        time_box = TimeBox()
        time_box.populate(psychiatrist, request.json)

        check_conflict_result = time_box.check_conflict()
        if check_conflict_result:
            return jsonify(message_en=check_conflict_result), 400

        time_box.save()
        return jsonify(time_box.to_json()), 201
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/time_box/<time_box_id>', methods=['DELETE'])
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_WRITE, True)
def delete_psychiatrist_time_box(id, time_box_id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName DeletePsychiatristTimeBox
    @api {delete} /v1/psychiatrist/:id/time_box/:time_box_id Delete a psychiatrist time_box

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist
    @apiParam (URL Parameter) {String} time_box_id ID of desired time box

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        time_box = TimeBox.objects.get(id=time_box_id)
        if time_box.psychiatrist.id != psychiatrist.id:
            return jsonify(), 403

        time_box.delete()
        return jsonify(), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting', methods=['GET'])
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_psychiatrist_meeting_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName GetPsychiatristMeetingList
    @api {get} /v1/psychiatrist/:id/meeting Get psychiatrist meeting list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiParam (Query Parameter) {String} [date] Filter by date (ISO format yyyy-mm-dd)

    @apiSuccess (Success Response) {Meeting[]} list
        List of <a href="#api-Psychiatrist-GetPsychiatristMeeting">meeting object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        query = Meeting.objects(psychiatrist=psychiatrist).order_by('-create_time')

        if request.args.get('date'):
            date = string_to_datetime(request.args.get('date'))
            query = query.filter(start_time__gte=date, start_time__lt=date + timedelta(days=1))

        return query
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting/<meeting_id>', methods=['GET'])
@authenticate('psychiatrist', 'psychiatrist', Permission.ACCESS_READ, True)
def get_psychiatrist_meeting(id, meeting_id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName GetPsychiatristMeeting
    @api {get} /v1/psychiatrist/:id/meeting/:meeting_id Get a psychiatrist meeting

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist
    @apiParam (URL Parameter) {String} meeting_id ID of desired meeting

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse MeetingToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        meeting = Meeting.objects.get(id=meeting_id)
        if meeting.psychiatrist.id != psychiatrist.id:
            return jsonify(), 403

        response = meeting.to_json()
        meeting.set_psychiatrist_have_notification(False)
        return jsonify(response), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting', methods=['POST'])
@validate('create_psychiatrist_meeting')
@User.authenticate
def create_psychiatrist_meeting(id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName CreatePsychiatristMeeting
    @api {post} /v1/psychiatrist/:id/meeting Create a psychiatrist meeting

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse CreatePsychiatristMeetingJson
    @apiUse MeetingToJson

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        meeting = Meeting()
        meeting.populate(None, psychiatrist, request.json)
        meeting.psychiatrist_accepted = True

        check_conflict_result = meeting.check_conflict()
        if check_conflict_result:
            return jsonify(message_en=check_conflict_result), 400

        meeting.set_person_have_notification(True)
        return jsonify(meeting.to_json()), 201
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting/<meeting_id>', methods=['PUT'])
@validate('update_psychiatrist_meeting')
@User.authenticate
def update_psychiatrist_meeting(id, meeting_id):
    """
    @apiVersion 1.0.0
    @apiGroup Psychiatrist
    @apiName UpdatePsychiatristMeeting
    @api {put} /v1/psychiatrist/:id/meeting/:meeting_id Update a psychiatrist meeting

    @apiParam (URL Parameter) {String} id ID of desired psychiatrist
    @apiParam (URL Parameter) {String} meeting_id ID of desired meeting

    @apiUse AccessTokenHeader

    @apiUse UpdatePsychiatristMeetingJson
    @apiUse MeetingToJson

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        json = request.json

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        psychiatrist = Psychiatrist.objects.get(id=id)
        if psychiatrist.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        meeting = Meeting.objects.get(id=meeting_id)
        if meeting.psychiatrist.id != psychiatrist.id:
            return jsonify(), 403

        previous_status = meeting.status

        if previous_status == Meeting.STATUS_NEW:
            if ('accepted' not in json) or ('result' in json) or ('attachment' in json):
                return jsonify(), 400
            meeting.update_status(None, json['accepted'])
            if meeting.status == Meeting.STATUS_ACCEPTED:
                check_conflict_result = meeting.check_conflict()
                if check_conflict_result:
                    return jsonify(message_en=check_conflict_result), 400
            meeting.set_person_have_notification(True)

        if previous_status == Meeting.STATUS_ACCEPTED:
            if ('accepted' in json) and (('result' in json) or ('attachment' in json)):
                return jsonify(), 400
            if ('accepted' not in json) and (('result' not in json) or ('attachment' not in json)):
                return jsonify(), 400

            if 'accepted' in json:
                meeting.update_status(None, json['accepted'])
                if meeting.status == Meeting.STATUS_ACCEPTED:
                    check_conflict_result = meeting.check_conflict()
                    if check_conflict_result:
                        return jsonify(message_en=check_conflict_result), 400
                meeting.set_person_have_notification(True)

            if 'accepted' not in json:
                meeting.populate(None, None, json)
                meeting.status = Meeting.STATUS_COMPLETED
                meeting.set_person_have_notification(True)
                from application.models import Package
                for package in Package.objects(person=meeting.person):
                    package.update_balance()

        if previous_status == Meeting.STATUS_REJECTED:
            return jsonify(), 400

        if previous_status == Meeting.STATUS_COMPLETED:
            if ('accepted' in json) or ('result' not in json) or ('attachment' not in json):
                return jsonify(), 400
            meeting.populate(None, None, json)
            meeting.set_person_have_notification(True)

        if previous_status != meeting.status:
            email.send(
                meeting.person.email,
                meeting.person.get_name(),
                localize('meeting_status'),
                localize(
                    'accepted_meeting_message'
                    if meeting.status == Meeting.STATUS_ACCEPTED else
                    'completed_meeting_message'
                    if meeting.status == Meeting.STATUS_COMPLETED else
                    'rejected_meeting_message'
                ) % meeting.psychiatrist.get_name()
            )

        return jsonify(meeting.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
