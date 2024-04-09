import os
from unittest import mock

from starlette.requests import Request

from stac_fastapi.types.requests import get_base_url


def test_get_base_url_with_env():
    env = {'REQUEST_BASE_URL': 'http://example.com/path/'}
    with mock.patch.dict(os.environ, env):
        assert get_base_url(Request({"type": "http", "app": None})) == "http://example.com/path/"
