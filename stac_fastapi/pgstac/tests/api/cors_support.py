from os import environ
from typing import Final

cors_origin_1: Final = "http://permit.one"
cors_origin_2: Final = "http://permit.two"
cors_origin_3: Final = "http://permit.three"
cors_origin_deny: Final = "http://deny.me"


def cors_permit_1():
    environ["CORS_ALLOW_ORIGINS"] = cors_origin_1


def cors_permit_2():
    environ["CORS_ALLOW_ORIGINS"] = cors_origin_2


def cors_permit_3():
    environ["CORS_ALLOW_ORIGINS"] = cors_origin_3


def cors_permit_12():
    environ["CORS_ALLOW_ORIGINS"] = f"{cors_origin_1}|{cors_origin_2}"


def cors_permit_123_regex():
    environ["CORS_ALLOW_ORIGIN_REGEX"] = "http\\://permit\\..+"


def cors_deny():
    environ["CORS_ALLOW_ORIGINS"] = cors_origin_deny


def cors_disable_get():
    environ["CORS_ALLOW_METHODS"] = "HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH"


def cors_clear_config():
    environ.pop("CORS_ALLOW_ORIGINS", None)
    environ.pop("CORS_ALLOW_METHODS", None)
    environ.pop("CORS_ALLOW_HEADERS", None)
    environ.pop("CORS_ALLOW_CREDENTIALS", None)
    environ.pop("CORS_ALLOW_ORIGIN_REGEX", None)
    environ.pop("CORS_EXPOSE_HEADERS", None)
    environ.pop("CORS_MAX_AGE", None)
