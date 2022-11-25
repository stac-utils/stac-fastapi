from json import dumps

from fastapi import Depends, HTTPException, security, status
from pytest import MonkeyPatch
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import TokenPaginationExtension, TransactionExtension
from stac_fastapi.types import config, core


class TestRouteDependencies:
    @staticmethod
    def _build_api(**overrides):
        settings = config.ApiSettings()
        return StacApi(
            **{
                "settings": settings,
                "client": DummyCoreClient(),
                "extensions": [
                    TransactionExtension(
                        client=DummyTransactionsClient(), settings=settings
                    ),
                    TokenPaginationExtension(),
                ],
                **overrides,
            }
        )

    @staticmethod
    def _assert_dependency_applied(api, routes):
        with TestClient(api.app) as client:
            for route in routes:
                response = getattr(client, route["method"].lower())(route["path"])
                assert (
                    response.status_code == 401
                ), "Unauthenticated requests should be rejected"
                assert response.json() == {"detail": "Not authenticated"}

                make_request = getattr(client, route["method"].lower())
                path = route["path"].format(
                    collectionId="test_collection", itemId="test_item"
                )
                response = make_request(
                    path,
                    auth=("bob", "dobbs"),
                    data='{"dummy": "payload"}',
                    headers={"content-type": "application/json"},
                )
                assert (
                    response.status_code == 200
                ), "Authenticated requests should be accepted"
                assert response.json() == "dummy response"

    def test_build_api_with_route_dependencies(self):
        routes = [
            {"path": "/collections", "method": "POST"},
            {"path": "/collections", "method": "PUT"},
            {"path": "/collections/{collectionId}", "method": "DELETE"},
            {"path": "/collections/{collectionId}/items", "method": "POST"},
            {"path": "/collections/{collectionId}/items/{itemId}", "method": "PUT"},
            {"path": "/collections/{collectionId}/items/{itemId}", "method": "DELETE"},
        ]
        dependencies = [Depends(must_be_bob)]
        api = self._build_api(route_dependencies=[(routes, dependencies)])
        self._assert_dependency_applied(api, routes)

    def test_add_route_dependencies_after_building_api(self):
        routes = [
            {"path": "/collections", "method": "POST"},
            {"path": "/collections", "method": "PUT"},
            {"path": "/collections/{collectionId}", "method": "DELETE"},
            {"path": "/collections/{collectionId}/items", "method": "POST"},
            {"path": "/collections/{collectionId}/items/{itemId}", "method": "PUT"},
            {"path": "/collections/{collectionId}/items/{itemId}", "method": "DELETE"},
        ]
        api = self._build_api()
        api.add_route_dependencies(scopes=routes, dependencies=[Depends(must_be_bob)])
        self._assert_dependency_applied(api, routes)


class DummyCoreClient(core.BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        ...

    def get_collection(self, *args, **kwargs):
        ...

    def get_item(self, *args, **kwargs):
        ...

    def get_search(self, *args, **kwargs):
        ...

    def post_search(self, *args, **kwargs):
        ...

    def item_collection(self, *args, **kwargs):
        ...


class DummyTransactionsClient(core.BaseTransactionsClient):
    """Defines a pattern for implementing the STAC transaction extension."""

    def create_item(self, *args, **kwargs):
        return "dummy response"

    def update_item(self, *args, **kwargs):
        return "dummy response"

    def delete_item(self, *args, **kwargs):
        return "dummy response"

    def create_collection(self, *args, **kwargs):
        return "dummy response"

    def update_collection(self, *args, **kwargs):
        return "dummy response"

    def delete_collection(self, *args, **kwargs):
        return "dummy response"


def must_be_bob(
    credentials: security.HTTPBasicCredentials = Depends(security.HTTPBasic()),
):
    if credentials.username == "bob":
        return True

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You're not Bob",
        headers={"WWW-Authenticate": "Basic"},
    )


def test_openapi(monkeypatch: MonkeyPatch):
    api_description = "API Description for Testing"
    api_title = "API Title For Testing"
    api_version = "0.1-testing"
    api_servers = [
        {"url": "http://api1", "description": "API 1"},
        {"url": "http://api2"},
    ]

    with monkeypatch.context() as m:
        m.setenv("API_DESCRIPTION", api_description)
        m.setenv("API_TITLE", api_title)
        m.setenv("API_VERSION", api_version)
        m.setenv("API_SERVERS", dumps(api_servers))
        settings = config.ApiSettings()

    api = StacApi(
        **{
            "settings": settings,
            "client": DummyCoreClient(),
            "extensions": [
                TransactionExtension(
                    client=DummyTransactionsClient(), settings=settings
                ),
                TokenPaginationExtension(),
            ],
        }
    )

    with TestClient(api.app) as client:
        response = client.get(api.app.openapi_url)

    assert response.status_code == 200
    assert (
        response.headers["Content-Type"]
        == "application/vnd.oai.openapi+json;version=3.0"
    )

    data = response.json()
    info = data["info"]
    assert info["description"] == api_description
    assert info["title"] == api_title
    assert info["version"] == api_version
    assert data["servers"] == api_servers
