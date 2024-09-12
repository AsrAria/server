# -*- coding: utf-8 -*-

# python imports
from uuid import uuid4
from datetime import timedelta

# flask imports
from flask import Blueprint, jsonify, request, g
from flask_jsonschema import validate

# mongo imports
from mongoengine import DoesNotExist

# project imports
from application.models import User
from application.models import Admin
from application.models import Person
from application.models import Package
from application.models import TimeBox
from application.models import Meeting
from application.models import Document
from application.models import Permission
from application.models import Psychiatrist
from application.models import Organization
from application.extensions import email
from application.utils.localize import localize
from application.utils.pagination import paginate
from application.utils.authenticate import authenticate
from application.utils.time import string_to_datetime, \
    datetime_to_string, date_to_string, create_datetime


api = Blueprint('person.api.v1', __name__, url_prefix='/api/v1/person')


@api.route('', methods=['GET'])
@Admin.authenticate('person', 'person', Permission.ACCESS_READ)
@paginate(key='list', max_per_page=50)
def get_list():
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonList
    @api {get} /v1/person Get person list

    @apiUse Paginate

    @apiUse SecretKeyHeader

    @apiParam (Query Parameter) {String} [email] Filter by email

    @apiSuccess (Success Response) {Person[]} list
        List of <a href="#api-Person-GetPerson">person object</a>

    @apiUse OK
    @apiUse Unauthorized
    """
    try:
        query = Person.objects().order_by('-create_time')

        if request.args.get('email'):
            query = query.filter(email__contains=request.args['email'].lower())

        return query
    except Exception:
        return jsonify(), 400


@api.route('/<id>', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
def get_person(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPerson
    @api {get} /v1/person/:id Get a person

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse PersonToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        person.update_balance()
        return jsonify(person.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>', methods=['PUT'])
@validate('person_edit')
@authenticate('person', 'person', Permission.ACCESS_WRITE, True)
def update(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName UpdatePerson
    @api {put} /v1/person/:id Update a person

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse PersonEditJson
    @apiUse PersonToJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse Conflict
    """
    try:
        json = request.json

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        person.update(json)

        if g.user_type == 'user':
            person.is_profile_updated = True
            person.save()

        return jsonify(person.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/package', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_person_package_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonPackageList
    @api {get} /v1/person/:id/package Get person package list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiSuccess (Success Response) {Package[]} list
        List of <a href="#api-Person-GetPersonPackage">package object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        query = Package.objects(person=person).order_by('-create_time')

        return query
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/package/<package_id>', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
def get_person_package(id, package_id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonPackage
    @api {get} /v1/person/:id/package/:package_id Get a person package

    @apiParam (URL Parameter) {String} id ID of desired person
    @apiParam (URL Parameter) {String} package_id ID of desired package

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse PackageToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        package = Package.objects.get(id=package_id)
        if package.person.id != person.id:
            return jsonify(), 403

        return jsonify(package.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/organization', methods=['GET'])
@User.authenticate
def get_person_organization_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonOrganizationList
    @api {get} /v1/person/:id/organization Get person organization list

    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiSuccess (Success Response) {Organization[]} list
        List of <a href="#api-Organization-GetOrganization">organization object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        query = Package.objects(person=person).aggregate({
            '$group': {'_id': '$organization'}
        })

        return jsonify(list=[Organization.objects.get(id=organization['_id']).to_json()
                             for organization in query]), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/submit_test', methods=['POST'])
@validate('document_submit_test')
@User.authenticate
def person_submit_test(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName SubmitPersonTest
    @api {get} /v1/person/:id/submit_test Submit person test

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiUse AccessTokenHeader

    @apiUse DocumentSubmitTestJson
    @apiUse DocumentToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        document = Document()
        document.populate_test_result(request.json)
        document.save()

        json = document.to_json()
        if 'items' not in json['data']['result']:
            document.delete()
            return jsonify(message_en=localize('your_response_are_invalid')), 400
        return jsonify(json), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/document', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_person_document_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonDocumentList
    @api {get} /v1/person/:id/document Get person document list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiSuccess (Success Response) {Document[]} list
        List of <a href="#api-Document-GetPersonDocument">document object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        person = Person.objects.get(id=id)

        if g.user_type == 'user' and g.user.role == User.ROLE_PERSON:
            if g.user.id != id:
                return jsonify(), 403

        if g.user_type == 'user' and g.user.role == User.ROLE_PSYCHIATRIST:
            meeting_query = Meeting.objects(
                person=person,
                psychiatrist=g.user,
                status__nin=[Meeting.STATUS_REJECTED]
            )
            if meeting_query.count() == 0:
                return jsonify(), 403

        if g.user_type == 'user' and g.user.role == User.ROLE_ORGANIZATION:
            return jsonify(), 403

        return Document.objects(person=person).order_by('-create_time')
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/document/<document_id>', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
def get_person_document(id, document_id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonDocument
    @api {get} /v1/person/:id/document/:document_id Get a person document

    @apiParam (URL Parameter) {String} id ID of desired person
    @apiParam (URL Parameter) {String} document_id ID of desired document

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse DocumentToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        person = Person.objects.get(id=id)

        if g.user_type == 'user' and g.user.role == User.ROLE_PERSON:
            if g.user.id != id:
                return jsonify(), 403

        if g.user_type == 'user' and g.user.role == User.ROLE_PSYCHIATRIST:
            meeting_query = Meeting.objects(
                person=person,
                psychiatrist=g.user,
                status__nin=[Meeting.STATUS_REJECTED]
            )
            if meeting_query.count() == 0:
                return jsonify(), 403

        if g.user_type == 'user' and g.user.role == User.ROLE_ORGANIZATION:
            return jsonify(), 403

        document = Document.objects.get(id=document_id)
        return jsonify(document.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/document/<document_id>', methods=['PUT'])
@validate('document_share')
@User.authenticate
def update_person_document(id, document_id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName UpdatePersonDocument
    @api {get} /v1/person/:id/document/:document_id Update a person document

    @apiParam (URL Parameter) {String} id ID of desired person
    @apiParam (URL Parameter) {String} document_id ID of desired document

    @apiUse AccessTokenHeader

    @apiUse DocumentShareJson
    @apiUse DocumentToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        document = Document.objects.get(id=document_id)
        if document.person.id != person.id:
            return jsonify(), 403

        document.populate(request.json)
        document.save()
        return jsonify(document.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/psychiatrist_suggestion', methods=['GET'])
@User.authenticate
def get_psychiatrist_suggestion_for_person(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPsychiatristSuggestionForPerson
    @api {get} /v1/person/:id/psychiatrist_suggestion Get psychiatrist suggestion for the person

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiUse AccessTokenHeader

    @apiSuccess (Success Response) {Psychiatrist[]} list
        List of <a href="#api-Psychiatrist-GetPsychiatrist">psychiatrist object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        list = []
        for psychiatrist in Psychiatrist.objects(is_confirmed=True).order_by('-score'):
            capacity = TimeBox.objects(
                psychiatrist=psychiatrist,
                start_time__gt=create_datetime(),
                end_time__lt=create_datetime() + timedelta(days=30)
            ).sum('length')
            reserved = Meeting.objects(
                psychiatrist=psychiatrist,
                start_time__gt=create_datetime(),
                end_time__lt=create_datetime() + timedelta(days=30),
                status__in=[Meeting.STATUS_ACCEPTED, Meeting.STATUS_COMPLETED]
            ).sum('length')
            if capacity > reserved:
                list.append(psychiatrist.to_json())
            if len(list) == 10:
                break
        return jsonify(list=list), 200
    except DoesNotExist:
        return jsonify(), 404
    except ValueError:
        return jsonify(), 400


@api.route('/<id>/meeting', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_person_meeting_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonMeetingList
    @api {get} /v1/person/:id/meeting Get person meeting list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiParam (Query Parameter) {String} [date] Filter by date (ISO format yyyy-mm-dd)

    @apiSuccess (Success Response) {Meeting[]} list
        List of <a href="#api-Person-GetPersonMeeting">meeting object</a>

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        query = Meeting.objects(person=person).order_by('-create_time')

        if request.args.get('date'):
            date = string_to_datetime(request.args.get('date'))
            query = query.filter(start_time__gte=date, start_time__lt=date + timedelta(days=1))

        return query
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting/<meeting_id>', methods=['GET'])
@authenticate('person', 'person', Permission.ACCESS_READ, True)
def get_person_meeting(id, meeting_id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetPersonMeeting
    @api {get} /v1/person/:id/meeting/:meeting_id Get a person meeting

    @apiParam (URL Parameter) {String} id ID of desired person
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

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        meeting = Meeting.objects.get(id=meeting_id)
        if meeting.person.id != person.id:
            return jsonify(), 403

        response = meeting.to_json()
        meeting.set_person_have_notification(False)
        return jsonify(response), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting', methods=['POST'])
@validate('create_person_meeting')
@User.authenticate
def create_person_meeting(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName CreatePersonMeeting
    @api {post} /v1/person/:id/meeting Create a person meeting

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse CreatePersonMeetingJson
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

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        person.update_balance()
        if person.balance > 5:
            return jsonify(message_en=localize('needs_payment_error')), 400

        meeting = Meeting()
        meeting.populate(person, None, request.json)
        meeting.person_accepted = True

        check_conflict_result = meeting.check_conflict()
        if check_conflict_result:
            return jsonify(message_en=check_conflict_result), 400

        meeting.set_psychiatrist_have_notification(True)
        return jsonify(meeting.to_json()), 201
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting/<meeting_id>', methods=['PUT'])
@validate('update_person_meeting')
@User.authenticate
def update_person_meeting(id, meeting_id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName UpdatePersonMeeting
    @api {put} /v1/person/:id/meeting/:meeting_id Update a person meeting

    @apiParam (URL Parameter) {String} id ID of desired person
    @apiParam (URL Parameter) {String} meeting_id ID of desired meeting

    @apiUse AccessTokenHeader

    @apiUse UpdatePersonMeetingJson
    @apiUse MeetingToJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        json = request.json

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        person = Person.objects.get(id=id)
        if person.role != User.ROLE_PERSON:
            return jsonify(), 403

        meeting = Meeting.objects.get(id=meeting_id)
        if meeting.person.id != person.id:
            return jsonify(), 403

        previous_status = meeting.status

        if previous_status == Meeting.STATUS_NEW or previous_status == Meeting.STATUS_ACCEPTED:
            if ('accepted' not in json) or ('score' in json) or ('comment' in json):
                return jsonify(), 400
            meeting.update_status(json['accepted'], None)
            if meeting.status == Meeting.STATUS_ACCEPTED:
                check_conflict_result = meeting.check_conflict()
                if check_conflict_result:
                    return jsonify(message_en=check_conflict_result), 400
            meeting.set_psychiatrist_have_notification(True)

        if previous_status == Meeting.STATUS_REJECTED:
            return jsonify(), 400

        if previous_status == Meeting.STATUS_COMPLETED:
            if ('accepted' in json) or ('score' not in json) or ('comment' not in json):
                return jsonify(), 400
            meeting.populate(None, None, json)
            meeting.set_psychiatrist_have_notification(True)
            meeting.psychiatrist.update_score()

        if previous_status != meeting.status:
            email.send(
                meeting.psychiatrist.email,
                meeting.psychiatrist.get_name(),
                localize('meeting_status'),
                localize(
                    'accepted_meeting_message'
                    if meeting.status == Meeting.STATUS_ACCEPTED else
                    'completed_meeting_message'
                    if meeting.status == Meeting.STATUS_COMPLETED else
                    'rejected_meeting_message'
                ) % meeting.person.get_name()
            )

        return jsonify(meeting.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/meeting_suggestion', methods=['GET'])
@User.authenticate
def get_meeting_suggestion_for_person(id):
    """
    @apiVersion 1.0.0
    @apiGroup Person
    @apiName GetMeetingSuggestionForPerson
    @api {get} /v1/person/:id/meeting_suggestion Get meeting suggestion for the person

    @apiParam (URL Parameter) {String} id ID of desired person

    @apiParam (Query Parameter) {String} psychiatrist ID of psychiatrist
    @apiParam (Query Parameter) {String} start_date Start date
    @apiParam (Query Parameter) {String} end_date End date
    @apiParam (Query Parameter) {String} length Length (0=30min, 1=60min, 2=90min)

    @apiUse AccessTokenHeader

    @apiSuccess (Success Response) {Object[]} list List of time box array
    @apiSuccess (Success Response) {String} list.date Desired date
    @apiSuccess (Success Response) {TimeBox[]} list.time_boxes Time boxes
    @apiSuccess (Success Response) {String} list.time_boxes.start_time Start of time box
    @apiSuccess (Success Response) {Integer} list.time_boxes.length
        Length of time box (0=30min, 1=60min, 2=90min)

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user.role != User.ROLE_PERSON and g.user.role != User.ROLE_PSYCHIATRIST:
            return jsonify(), 403

        person = Person.objects.get(id=id)

        if not request.args.get('psychiatrist') or not request.args.get('length') or \
           not request.args.get('start_date') or not request.args.get('end_date'):
            return jsonify(), 400

        length = int(request.args.get('length'))
        psychiatrist = Psychiatrist.objects().get(id=request.args.get('psychiatrist'))
        start_date = string_to_datetime(request.args.get('start_date'))
        end_date = string_to_datetime(request.args.get('end_date'))

        list = []
        current_date = start_date
        while (current_date < end_date):
            next_date = current_date + timedelta(days=1)
            query = TimeBox.objects(
                psychiatrist=psychiatrist,
                start_time__gte=current_date,
                start_time__lt=next_date,
                end_time__gt=create_datetime,
            ).order_by('+start_time')

            suggestions = []
            for time_box in query:
                current_time = time_box.start_time
                while current_time < time_box.end_time:
                    next_time = current_time + timedelta(minutes=30)
                    suggestion = {
                        'id': str(uuid4()),
                        'start_time': datetime_to_string(current_time),
                        'length': length
                    }
                    meeting = Meeting()
                    meeting.populate(person, psychiatrist, suggestion)
                    if not meeting.check_conflict():
                        suggestions.append(suggestion)
                    current_time = next_time
            list.append({
                'date': date_to_string(current_date),
                'time_boxes': suggestions
            })
            current_date = next_date

        return jsonify(list=list), 200
    except DoesNotExist:
        return jsonify(), 404
    except ValueError:
        return jsonify(), 400
