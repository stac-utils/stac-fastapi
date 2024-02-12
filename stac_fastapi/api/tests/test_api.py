import json

import pytest
from fastapi import Depends, HTTPException, security, status
from stac_pydantic import Collection, Item
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

                path = route["path"].format(
                    collectionId="test_collection", itemId="test_item"
                )
                response = client.request(
                    method=route["method"].lower(),
                    url=path,
                    auth=("bob", "dobbs"),
                    content=route.get("payload"),
                    headers={"content-type": "application/json"},
                )
                assert (
                    response.status_code == 200
                ), "Authenticated requests should be accepted"
                assert response.json() == "dummy response"

    def test_openapi_content_type(self):
        api = self._build_api()
        with TestClient(api.app) as client:
            response = client.get(api.settings.openapi_url)
            assert (
                response.headers["content-type"]
                == "application/vnd.oai.openapi+json;version=3.0"
            )

    def test_build_api_with_route_dependencies(
        self, collection: Collection, item: Item
    ):
        routes = [
            {"path": "/collections", "method": "POST", "payload": collection},
            {"path": "/collections", "method": "PUT", "payload": collection},
            {"path": "/collections/{collectionId}", "method": "DELETE"},
            {
                "path": "/collections/{collectionId}/items",
                "method": "POST",
                "payload": item,
            },
            {
                "path": "/collections/{collectionId}/items/{itemId}",
                "method": "PUT",
                "payload": item,
            },
            {
                "path": "/collections/{collectionId}/items/{itemId}",
                "method": "DELETE",
            },
        ]
        dependencies = [Depends(must_be_bob)]
        api = self._build_api(route_dependencies=[(routes, dependencies)])
        self._assert_dependency_applied(api, routes)

    def test_add_route_dependencies_after_building_api(
        self, collection: Collection, item: Item
    ):
        routes = [
            {"path": "/collections", "method": "POST", "payload": collection},
            {"path": "/collections", "method": "PUT", "payload": collection},
            {"path": "/collections/{collectionId}", "method": "DELETE"},
            {
                "path": "/collections/{collectionId}/items",
                "method": "POST",
                "payload": item,
            },
            {
                "path": "/collections/{collectionId}/items/{itemId}",
                "method": "PUT",
                "payload": item,
            },
            {
                "path": "/collections/{collectionId}/items/{itemId}",
                "method": "DELETE",
            },
        ]
        api = self._build_api()
        api.add_route_dependencies(scopes=routes, dependencies=[Depends(must_be_bob)])
        self._assert_dependency_applied(api, routes)


class DummyCoreClient(core.BaseCoreClient):
    def all_collections(self, *args, **kwargs): ...

    def get_collection(self, *args, **kwargs): ...

    def get_item(self, *args, **kwargs): ...

    def get_search(self, *args, **kwargs): ...

    def post_search(self, *args, **kwargs): ...

    def item_collection(self, *args, **kwargs): ...


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


@pytest.fixture
def collection():
    return json.dumps(
        {
            "id": "test_collection",
            "title": "Test collection",
            "description": "This is a test collection",
            "license": "open",
            "keywords": [],
            "extent": {
                "spatial": {"bbox": [[-105, 40, -105, 40]]},
                "temporal": {"interval": [["2023-02-12T12:00:00Z", None]]},
            },
            "links": [],
        }
    )


@pytest.fixture
def item():
    return json.dumps(
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "stac_extensions": [],
            "id": "test_item",
            "geometry": {"type": "Point", "coordinates": [-105, 40]},
            "bbox": [-105, 40, -105, 40],
            "properties": {"datetime": "2023-02-12T12:00:00Z"},
            "links": [],
            "assets": {},
            "collection": "test_collection",
        }
    )
