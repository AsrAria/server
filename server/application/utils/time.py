# python imports
from datetime import datetime


DATE_FORMAT = r"%Y-%m-%d"
DATETIME_FORMAT_1 = r"%Y-%m-%dT%H:%M:%S"
DATETIME_FORMAT_2 = r"%Y-%m-%d %H:%M:%S"
DATETIME_FORMAT_3 = r"%Y-%m-%dT%H:%M:%S.%f%z"


class DateTimeException(Exception):
    pass


def create_datetime(time=None):
    if time is None:
        time = datetime.utcnow()
    return time


def string_to_datetime(time):
    for dt_format in [DATE_FORMAT, DATETIME_FORMAT_1, DATETIME_FORMAT_2, DATETIME_FORMAT_3]:
        try:
            result = datetime.strptime(time, dt_format)
            if result.year < 1950:
                raise DateTimeException('year must be greater than 1950.')
            if result.year > 9000:
                raise DateTimeException('year must be less than 9000.')
            return result
        except Exception:
            pass
    raise DateTimeException()


def date_to_string(datetime, fmt=DATE_FORMAT):
    return str(create_formetted_datetime(datetime, fmt))


def datetime_to_string(datetime, fmt=DATETIME_FORMAT_1):
    return str(create_formetted_datetime(datetime, fmt))


def create_formetted_datetime(utc_time, fmt=DATETIME_FORMAT_1):
    return utc_time.strftime(fmt)
