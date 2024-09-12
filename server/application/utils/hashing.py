# python imports
import hashlib
from uuid import uuid4


# mark: functions

def hash_password(s):
    for i in range(1, 100):
        s = hash_function(s)
    return s


def generate_token():
    out = ""
    for i in range(1, 5):
        out += generate_small_token()
    return out


def generate_small_token():
    return hash_function(str(uuid4().hex))


# mark: helper functions

def hash_function(s):
    m = hashlib.sha1()
    m.update(s.encode('utf-8'))
    return m.hexdigest()
