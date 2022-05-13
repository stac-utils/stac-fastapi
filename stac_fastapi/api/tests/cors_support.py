from copy import deepcopy
from json import dumps
from typing import Final

from stac_fastapi.api.config import fastapi_app_settings

settings_fallback = deepcopy(fastapi_app_settings)
cors_origin_1: Final = "http://permit.one"
cors_origin_2: Final = "http://permit.two"
cors_origin_3: Final = "http://permit.three"
cors_origin_deny: Final = "http://deny.me"


def cors_permit_1():
    fastapi_app_settings.allow_origins = dumps((cors_origin_1,))


def cors_permit_2():
    fastapi_app_settings.allow_origins = dumps((cors_origin_2,))


def cors_permit_3():
    fastapi_app_settings.allow_origins = dumps((cors_origin_3,))


def cors_permit_12():
    fastapi_app_settings.allow_origins = dumps((cors_origin_1, cors_origin_2))


def cors_permit_123_regex():
    fastapi_app_settings.allow_origin_regex = "http\\://permit\\..+"


def cors_deny():
    fastapi_app_settings.allow_origins = dumps((cors_origin_deny,))


def cors_disable_get():
    fastapi_app_settings.allow_methods = dumps(
        (
            "HEAD",
            "POST",
            "PUT",
            "DELETE",
            "CONNECT",
            "OPTIONS",
            "TRACE",
            "PATCH",
        )
    )


def cors_clear_config():
    fastapi_app_settings.allow_origins = settings_fallback.allow_origins
    fastapi_app_settings.allow_methods = settings_fallback.allow_methods
    fastapi_app_settings.allow_headers = settings_fallback.allow_headers
    fastapi_app_settings.allow_credentials = settings_fallback.allow_credentials
    fastapi_app_settings.allow_origin_regex = settings_fallback.allow_origin_regex
    fastapi_app_settings.expose_headers = settings_fallback.expose_headers
    fastapi_app_settings.max_age = settings_fallback.max_age
