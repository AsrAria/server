# -*- coding: utf-8 -*-

# flask imports
from flask import Blueprint, jsonify, request, g
from flask_jsonschema import validate

# mongo imports
from mongoengine import DoesNotExist

# project imports
from application.models import User
from application.models import Admin
from application.models import Organization
from application.models import Permission
from application.models import Person
from application.models import Package
from application.models import Document
from application.extensions import email
from application.utils.localize import localize
from application.utils.pagination import paginate
from application.utils.authenticate import authenticate


api = Blueprint('organization.api.v1', __name__, url_prefix='/api/v1/organization')


@api.route('', methods=['GET'])
@Admin.authenticate('organization', 'organization', Permission.ACCESS_READ)
@paginate(key='list', max_per_page=50)
def get_list():
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationList
    @api {get} /v1/organization Get organization list

    @apiUse Paginate

    @apiUse SecretKeyHeader

    @apiParam (Query Parameter) {String} [email] Filter by email
    @apiParam (Query Parameter) {String} [is_confirmed] Filter by is_confirmed field (true, false)

    @apiSuccess (Success Response) {Organization[]} list
        List of <a href="#api-Organization-GetOrganization">organization object</a>

    @apiUse OK
    @apiUse Unauthorized
    """
    try:
        query = Organization.objects().order_by('-create_time')

        if request.args.get('email'):
            query = query.filter(email__contains=request.args['email'].lower())

        if request.args.get('is_confirmed'):
            query = query.filter(is_confirmed=(request.args['is_confirmed'] == 'true'))

        return query
    except Exception:
        return jsonify(), 400


@api.route('/<id>', methods=['GET'])
@authenticate('organization', 'organization', Permission.ACCESS_READ, True)
def get_organization(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganization
    @api {get} /v1/organization/:id Get a organization

    @apiParam (URL Parameter) {String} id ID of desired organization

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse OrganizationToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        organization.update_balance()
        return jsonify(organization.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>', methods=['PUT'])
@validate('organization_edit')
@authenticate('organization', 'organization', Permission.ACCESS_WRITE, True)
def update(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName UpdateOrganization
    @api {put} /v1/organization/:id Update a organization

    @apiParam (URL Parameter) {String} id ID of desired organization

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse OrganizationEditJson
    @apiUse OrganizationToJson

    @apiUse OK
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    """
    try:
        json = request.json

        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        organization.update(json)

        if g.user_type == 'user':
            organization.is_profile_updated = True
            organization.save()

        return jsonify(organization.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
    except Exception:
        return jsonify(), 400


@api.route('/<id>/confirm', methods=['POST'])
@Admin.authenticate('organization', 'organization', Permission.ACCESS_WRITE)
def confirm(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName ConfirmOrganization
    @api {post} /v1/organization/:id/confirm Confirm organization

    @apiParam (URL Parameter) {String} id ID of desired organization

    @apiUse SecretKeyHeader

    @apiUse OrganizationToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        organization = Organization.objects.get(id=id)
        organization.is_confirmed = True
        organization.save()
        email.send(
            organization.email,
            organization.get_name(),
            localize('your_activation_status_title'),
            localize('your_activation_confirmed_message')
        )
        return jsonify(organization.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/reject', methods=['POST'])
@Admin.authenticate('organization', 'organization', Permission.ACCESS_WRITE)
def reject(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName RejectOrganization
    @api {post} /v1/organization/:id/reject Reject organization

    @apiParam (URL Parameter) {String} id ID of desired organization

    @apiUse SecretKeyHeader

    @apiUse OrganizationToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse NotFound
    """
    try:
        organization = Organization.objects.get(id=id)
        organization.is_confirmed = False
        organization.save()
        email.send(
            organization.email,
            organization.get_name(),
            localize('your_activation_status_title'),
            localize('your_activation_rejected_message')
        )
        return jsonify(organization.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/package', methods=['GET'])
@authenticate('organization', 'organization', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_organization_package_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationPackageList
    @api {get} /v1/organization/:id/package Get organization package list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (Query Parameter) {String} [person] Filter by person email

    @apiSuccess (Success Response) {Package[]} list
        List of <a href="#api-Organization-GetOrganizationPackage">package object</a>

    @apiParam (URL Parameter) {String} id ID of desired organization

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        query = Package.objects(organization=organization).order_by('-create_time')

        if request.args.get('person'):
            query = query.filter(
                person__in=Person.objects(email__contains=request.args.get('person')))

        return query
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/package/<package_id>', methods=['GET'])
@authenticate('organization', 'organization', Permission.ACCESS_READ, True)
def get_organization_package(id, package_id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationPackage
    @api {get} /v1/organization/:id/package/:package_id Get a organization package

    @apiParam (URL Parameter) {String} id ID of desired organization
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

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        package = Package.objects.get(id=package_id)
        if package.organization.id != organization.id:
            return jsonify(), 403

        return jsonify(package.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/package', methods=['POST'])
@validate('package')
@authenticate('organization', 'organization', Permission.ACCESS_WRITE, True)
def create(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName CreateOrganizationPackage
    @api {post} /v1/organization/:id/package Create a organization package

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiUse PackageJson
    @apiUse PackageToJson

    @apiUse Created
    @apiUse BadRequest
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        package = Package()
        package.populate(organization, request.json)

        check_conflict_result = package.check_conflict()
        if check_conflict_result:
            return jsonify(message_en=check_conflict_result), 400

        package.save()
        package.update_balance()
        return jsonify(package.to_json()), 201
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/package/<package_id>', methods=['DELETE'])
@authenticate('organization', 'organization', Permission.ACCESS_WRITE, True)
def delete_organization_package(id, package_id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName DeleteOrganizationPackage
    @api {delete} /v1/organization/:id/package/:package_id Delete a organization package

    @apiParam (URL Parameter) {String} id ID of desired organization
    @apiParam (URL Parameter) {String} package_id ID of desired package

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

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        package = Package.objects.get(id=package_id)
        if package.organization.id != organization.id:
            return jsonify(), 403
        person = package.person
        package.delete()

        person.update_balance()
        organization.update_balance()
        return jsonify(), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/person', methods=['GET'])
@authenticate('organization', 'organization', Permission.ACCESS_READ, True)
@paginate(key='list', max_per_page=50)
def get_organization_person_list(id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationPersonList
    @api {get} /v1/organization/:id/person Get organization person list

    @apiUse Paginate

    @apiUse SecretKeyHeader
    @apiUse AccessTokenHeader

    @apiParam (Query Parameter) {String} [person] Filter by person email

    @apiSuccess (Success Response) {Person[]} list
        List of <a href="#api-Person-GetPerson">person object</a>

    @apiParam (URL Parameter) {String} id ID of desired organization

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        persons = []
        for package in Package.objects(organization=organization):
            if request.args.get('person') and \
               request.args.get('person') not in package.person.email:
                continue
            if package.person.id not in persons:
                persons.append(package.person.id)

        return Person.objects(id__in=persons).order_by('-create_time')
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/person/<person_id>', methods=['GET'])
@authenticate('organization', 'organization', Permission.ACCESS_READ, True)
def get_organization_person(id, person_id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationPerson
    @api {get} /v1/organization/:id/person/:person_id Get a organization person

    @apiParam (URL Parameter) {String} id ID of desired organization
    @apiParam (URL Parameter) {String} person_id ID of desired person

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

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        person = Person.objects.get(id=person_id)
        if Package.objects(person=person).count() == 0:
            return jsonify(), 403

        return jsonify(person.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/person/<person_id>/document', methods=['GET'])
@User.authenticate
@paginate(key='list', max_per_page=50)
def get_organization_person_document_list(id, person_id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationPersonDocumentLit
    @api {get} /v1/organization/:id/person/:person_id/document Get person document list

    @apiUse Paginate

    @apiUse AccessTokenHeader

    @apiSuccess (Success Response) {Document[]} list
        List of <a href="#api-Organization-GetOrganizationPersonDocument">document object</a>

    @apiParam (URL Parameter) {String} id ID of desired organization
    @apiParam (URL Parameter) {String} person_id ID of desired person

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        person = Person.objects.get(id=person_id)
        return Document.objects(person=person, shared_with=organization).order_by('-create_time')
    except DoesNotExist:
        return jsonify(), 404


@api.route('/<id>/person/<person_id>/document/<document_id>', methods=['GET'])
@User.authenticate
def get_organization_person_document(id, person_id, document_id):
    """
    @apiVersion 1.0.0
    @apiGroup Organization
    @apiName GetOrganizationPersonDocument
    @api {get} /v1/organization/:id/person/:person_id/document/:document_id
        Get a organization person document

    @apiParam (URL Parameter) {String} id ID of desired organization
    @apiParam (URL Parameter) {String} person_id ID of desired person
    @apiParam (URL Parameter) {String} document_id ID of desired document

    @apiUse AccessTokenHeader

    @apiUse DocumentToJson

    @apiUse OK
    @apiUse Unauthorized
    @apiUse Forbidden
    @apiUse NotFound
    """
    try:
        if g.user_type == 'user' and g.user.id != id:
            return jsonify(), 403

        organization = Organization.objects.get(id=id)
        if organization.role != User.ROLE_ORGANIZATION:
            return jsonify(), 403

        person = Person.objects.get(id=person_id)
        document = Document.objects.get(id=document_id, person=person, shared_with=organization)
        return jsonify(document.to_json()), 200
    except DoesNotExist:
        return jsonify(), 404
