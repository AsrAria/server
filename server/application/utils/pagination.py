# -*- coding: utf-8 -*-

# python imports
from functools import wraps
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

# mongo imports
from mongoengine.queryset import QuerySet

# flask imports
from flask import jsonify, request, current_app
from flask_mongoengine.pagination import Pagination


def paginate(key, max_per_page):
    """
    @apiDefine Paginate

    @apiParam (URL Parameter) {Integer} [page=1] Current page
    @apiParam (URL Parameter) {Integer} [per_page=25]
        Object per page (per_page = -1 return all)

    @apiSuccess (Success - 2xx) {Object} meta Pagination meta data.
    @apiSuccess (Success - 2xx) {Boolean} meta.has_next Pagination has next page
    @apiSuccess (Success - 2xx) {Url} [meta.next] Url for next page of results
    @apiSuccess (Success - 2xx) {Boolean} meta.has_prev Pagination has previous page
    @apiSuccess (Success - 2xx) {Url} [meta.prev] Url for previous page of results
    @apiSuccess (Success - 2xx) {Integer} meta.page Number of the current page
    @apiSuccess (Success - 2xx) {Integer} meta.pages All pages count
    @apiSuccess (Success - 2xx) {Integer} meta.per_page Item per each page
    @apiSuccess (Success - 2xx) {Integer} meta.total Count of all items
    """

    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            query = f(*args, **kwargs)
            page = request.args.get('page', 1, type=int)

            per_page = min(request.args.get(
                'per_page',
                current_app.config['PAGE_SIZE'],
                type=int
            ), max_per_page)

            if not isinstance(query, QuerySet):
                return query

            obj_count = query.count()
            if per_page == -1:
                per_page = max(obj_count, 1)

            pagination_obj, meta = _paginate(query, page, per_page)

            return jsonify({
                str(key): [item.to_json() for item in pagination_obj],
                'meta': meta
            })

        return wrapped

    return decorator


def _paginate(query, page, per_page):

    pagination_obj = Pagination(query, page, per_page)
    meta = {'page': pagination_obj.page, 'per_page': pagination_obj.per_page,
            'total': pagination_obj.total, 'pages': pagination_obj.pages}
    if meta['pages'] == 0:
        meta['pages'] = 1

    url_parsed = list(urlparse(request.url))
    args = parse_qs(url_parsed[4])

    meta['has_prev'] = pagination_obj.has_prev
    if pagination_obj.has_prev:
        args['page'] = page - 1
        url_parsed[4] = urlencode(encode_obj(args), doseq=True)
        meta['prev'] = urlunparse(url_parsed)

    meta['has_next'] = pagination_obj.has_next
    if pagination_obj.has_next:
        args['page'] = page + 1
        url_parsed[4] = urlencode(encode_obj(args), doseq=True)
        meta['next'] = urlunparse(url_parsed)

    return pagination_obj.items, meta


def encode_obj(in_obj):

    def encode_list(in_list):
        out_list = []
        for el in in_list:
            out_list.append(encode_obj(el))
        return out_list

    def encode_dict(in_dict):
        out_dict = {}
        for k, v in in_dict.items():
            out_dict[k] = encode_obj(v)
        return out_dict

    if isinstance(in_obj, str):
        return in_obj.encode('utf-8')
    elif isinstance(in_obj, list):
        return encode_list(in_obj)
    elif isinstance(in_obj, tuple):
        return tuple(encode_list(in_obj))
    elif isinstance(in_obj, dict):
        return encode_dict(in_obj)

    return in_obj
