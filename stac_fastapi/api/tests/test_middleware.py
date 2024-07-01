from unittest import mock

import pytest
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.applications import Starlette
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.middleware import ProxyHeaderMiddleware
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient


@pytest.fixture
def proxy_header_middleware() -> ProxyHeaderMiddleware:
    app = Starlette()
    return ProxyHeaderMiddleware(app)


@pytest.fixture
def test_client() -> TestClient:
    app = StacApi(settings=ApiSettings(), client=mock.create_autospec(BaseCoreClient))
    with TestClient(app.app) as client:
        yield client


@pytest.mark.parametrize(
    "headers,key,expected",
    [
        ([(b"host", b"testserver")], "host", "testserver"),
        ([(b"host", b"testserver")], "user-agent", None),
        (
            [(b"host", b"testserver"), (b"accept-encoding", b"gzip, deflate, br")],
            "accept-encoding",
            "gzip, deflate, br",
        ),
    ],
)
def test_get_header_value_by_name(
    proxy_header_middleware: ProxyHeaderMiddleware, headers, key, expected
):
    scope = {"headers": headers}
    actual = proxy_header_middleware._get_header_value_by_name(scope, key)
    assert actual == expected


@pytest.mark.parametrize(
    "headers,key,value",
    [
        ([(b"host", b"testserver")], "host", "another-server"),
        ([(b"host", b"testserver")], "user-agent", "agent"),
        (
            [(b"host", b"testserver"), (b"accept-encoding", b"gzip, deflate, br")],
            "accept-encoding",
            "deflate",
        ),
    ],
)
def test_replace_header_value_by_name(
    proxy_header_middleware: ProxyHeaderMiddleware, headers, key, value
):
    scope = {"headers": headers}
    updated_headers = proxy_header_middleware._replace_header_value_by_name(
        scope, key, value
    )

    header_value = proxy_header_middleware._get_header_value_by_name(
        {"headers": updated_headers}, key
    )
    assert header_value == value


@pytest.mark.parametrize(
    "scope,expected",
    [
        (
            {"scheme": "https", "server": ["testserver", 80], "headers": []},
            ("https", "testserver", 80),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"host", b"testserver:81")],
            },
            ("http", "testserver", 81),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"host", b"testserver")],
            },
            ("http", "testserver", None),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"forwarded", b"proto=https;host=test:1234")],
            },
            ("https", "test", 1234),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"forwarded", b"proto=https;host=test:not-an-integer")],
            },
            ("https", "test", 80),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"x-forwarded-host", b"test")],
            },
            ("http", "test", 80),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"x-forwarded-proto", b"https")],
            },
            ("https", "testserver", 80),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"x-forwarded-port", b"1111")],
            },
            ("http", "testserver", 1111),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [(b"x-forwarded-port", b"not-an-integer")],
            },
            ("http", "testserver", 80),
        ),
        (
            {
                "scheme": "http",
                "server": ["testserver", 80],
                "headers": [
                    (b"forwarded", b"proto=https;host=test:1234"),
                    (b"x-forwarded-host", b"another-test"),
                    (b"x-forwarded-port", b"1111"),
                    (b"x-forwarded-proto", b"https"),
                ],
            },
            ("https", "test", 1234),
        ),
    ],
)
def test_get_forwarded_url_parts(
    proxy_header_middleware: ProxyHeaderMiddleware, scope, expected
):
    actual = proxy_header_middleware._get_forwarded_url_parts(scope)
    assert actual == expected


def test_cors_middleware(test_client):
    resp = test_client.get("/_mgmt/ping", headers={"Origin": "http://netloc"})
    assert resp.status_code == 200
    assert resp.headers["access-control-allow-origin"] == "*"


def test_middleware_stack():
    stac_api = StacApi(
        settings=ApiSettings(), client=mock.create_autospec(BaseCoreClient)
    )

    def exception_handler(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"customerrordetail": "yoo", "body": "yo"},
        )

    class CustomException(Exception):
        "Custom Exception"

        pass

    stac_api.app.add_exception_handler(CustomException, exception_handler)

    @stac_api.app.get("/error")
    def error_endpoint():
        raise CustomException("got you!")

    with TestClient(stac_api.app) as client:
        resp = client.get("/error")
        assert resp.status_code == 400
        assert resp.json()["customerrordetail"] == "yoo"
