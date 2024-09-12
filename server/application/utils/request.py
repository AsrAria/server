# -*- coding: utf-8 -*-

# flask imports
from flask import request


def get_remote_address():
    try:
        return request.remote_addr
    except Exception:
        return "0.0.0.0"
