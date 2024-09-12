import random
import string


def random_string(length=10, choices=None):
    if not isinstance(length, int):
        raise Exception('length must be integer.')

    if not choices:
        choices = string.ascii_uppercase + string.ascii_lowercase + string.digits

    return ''.join(random.choice(choices) for _ in range(length))
