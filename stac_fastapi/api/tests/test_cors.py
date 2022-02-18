from http import HTTPStatus

from starlette.testclient import TestClient
from tests.cors_support import (
    cors_clear_config,
    cors_deny,
    cors_origin_1,
    cors_origin_deny,
    cors_permit_1,
    cors_permit_12,
    cors_permit_123_regex,
)
from tests.util import build_api

from stac_fastapi.extensions.core import TokenPaginationExtension


def teardown_function():
    cors_clear_config()


def _get_api():
    return build_api([TokenPaginationExtension()])


def test_with_default_cors_origin():
    api = _get_api()
    with TestClient(api.app) as client:
        resp = client.get("/conformance", headers={"Origin": cors_origin_1})
        assert resp.status_code == HTTPStatus.OK
        assert resp.headers["access-control-allow-origin"] == "*"


def test_with_match_cors_single():
    cors_permit_1()
    api = _get_api()
    with TestClient(api.app) as client:
        resp = client.get("/conformance", headers={"Origin": cors_origin_1})
        assert resp.status_code == HTTPStatus.OK
        assert resp.headers["access-control-allow-origin"] == cors_origin_1


def test_with_match_cors_double():
    cors_permit_12()
    api = _get_api()
    with TestClient(api.app) as client:
        resp = client.get("/conformance", headers={"Origin": cors_origin_1})
        assert resp.status_code == HTTPStatus.OK
        assert resp.headers["access-control-allow-origin"] == cors_origin_1


def test_with_match_cors_all_regex_match():
    cors_permit_123_regex()
    api = _get_api()
    with TestClient(api.app) as client:
        resp = client.get("/conformance", headers={"Origin": cors_origin_1})
        assert resp.status_code == HTTPStatus.OK
        assert resp.headers["access-control-allow-origin"] == cors_origin_1


def test_with_match_cors_all_regex_mismatch():
    cors_permit_123_regex()
    api = _get_api()
    with TestClient(api.app) as client:
        resp = client.get("/conformance", headers={"Origin": cors_origin_deny})
        assert resp.status_code == HTTPStatus.OK
        assert "access-control-allow-origin" not in resp.headers


def test_with_mismatch_cors_origin():
    cors_deny()
    api = _get_api()
    with TestClient(api.app) as client:
        resp = client.get("/conformance", headers={"Origin": cors_origin_1})
        assert resp.status_code == HTTPStatus.OK
        assert "access-control-allow-origin" not in resp.headers
