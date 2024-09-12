# -*- coding: utf-8 -*-


class Pattern:

    # mark: constants

    PATTERN_TOKEN = r"^[0-9a-f]{160}$"
    PATTERN_ACTIVATION_CODE = r"^[0-9]{4}$"
    PATTERN_PASSWORD = r"^[A-Za-z0-9]{8,}$"

    PATTERN_EMAIL = r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
