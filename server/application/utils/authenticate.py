# python imports
from functools import wraps

# flask imports
from flask import jsonify

# project imports
from application.models import User
from application.models import Admin
from application.models import Permission


def authenticate(permission=None, sub_permission=None, level=Permission.ACCESS_NONE, user=False):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            admin_authentication_result = Admin.check_authentication(
                permission_name=permission,
                sub_permission_name=sub_permission,
                need_access_level=level
            )
            if admin_authentication_result == 200:
                return f(*args, **kwargs)

            if user:
                user_authentication_result = User.check_authentication()
                if user_authentication_result == 200:
                    return f(*args, **kwargs)
                if user_authentication_result[1] == 403:
                    return user_authentication_result

            return jsonify(), 401
        return wrapper
    return decorator
