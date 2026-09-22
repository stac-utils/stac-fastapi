from collections.abc import Iterator

import pytest
from stac_pydantic import Collection
from stac_pydantic.item import Item
from stac_pydantic.item_collection import ItemCollection
from starlette.responses import Response
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions import TransactionExtension
from stac_fastapi.extensions.transaction import BaseTransactionsClient
from stac_fastapi.extensions.transaction.request import (
    PartialCollection,
    PartialItem,
    PatchOperation,
)
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient


class DummyCoreClient(BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        raise NotImplementedError

    def get_collection(self, *args, **kwargs):
        raise NotImplementedError

    def get_item(self, *args, **kwargs):
        raise NotImplementedError

    def get_search(self, *args, **kwargs):
        raise NotImplementedError

    def post_search(self, *args, **kwargs):
        raise NotImplementedError

    def item_collection(self, *args, **kwargs):
        raise NotImplementedError


class DummyTransactionsClient(BaseTransactionsClient):
    """Dummy client returning parts of the request, rather than proper STAC items."""

    def create_item(self, item: Item | ItemCollection, *args, **kwargs):
        return {"created": True, "type": item.type}

    def update_item(self, collection_id: str, item_id: str, item: Item, **kwargs):
        return {
            "path_collection_id": collection_id,
            "path_item_id": item_id,
            "type": item.type,
        }

    def patch_item(
        self,
        collection_id: str,
        item_id: str,
        patch: PartialItem | list[PatchOperation],
        **kwargs,
    ):
        if isinstance(patch, PartialItem):
            patch = patch.operations()

        return {
            "path_collection_id": collection_id,
            "path_item_id": item_id,
            "patch": patch,
        }

    def delete_item(self, item_id: str, collection_id: str, **kwargs):
        return {
            "path_collection_id": collection_id,
            "path_item_id": item_id,
        }

    def create_collection(self, collection: Collection, **kwargs):
        return {"type": collection.type}

    def update_collection(self, collection_id: str, collection: Collection, **kwargs):
        return {"path_collection_id": collection_id, "type": collection.type}

    def patch_collection(
        self,
        collection_id: str,
        patch: PartialCollection | list[PatchOperation],
        **kwargs,
    ):
        if isinstance(patch, PartialCollection):
            patch = patch.operations()

        return {
            "path_collection_id": collection_id,
            "patch": patch,
        }

    def delete_collection(self, collection_id: str, **kwargs):
        return {"path_collection_id": collection_id}


class ResponseTransactionsClient(DummyTransactionsClient):
    """Client returning raw `Response` objects."""

    def create_item(self, item: Item | ItemCollection, *args, **kwargs):
        return Response(status_code=201)

    def create_collection(self, collection: Collection, **kwargs):
        return Response(status_code=201, headers={"Location": "/custom-location"})


def test_create_item(client: TestClient, item: Item) -> None:
    response = client.post("/collections/a-collection/items", json=item)
    assert response.status_code == 201, response.text
    assert response.json()["type"] == "Feature"
    assert response.headers["location"].endswith(
        "/collections/a-collection/items/test_item"
    )


def test_create_item_collection(
    client: TestClient, item_collection: ItemCollection
) -> None:
    response = client.post("/collections/a-collection/items", json=item_collection)
    assert response.is_success, response.text
    assert response.json()["type"] == "FeatureCollection"
    assert "location" not in response.headers


def test_create_item_response_location(response_client: TestClient, item: Item) -> None:
    """A `Location` header is added when the client returns a `Response`."""
    response = response_client.post("/collections/a-collection/items", json=item)
    assert response.status_code == 201, response.text
    assert response.headers["location"].endswith(
        "/collections/a-collection/items/test_item"
    )


def test_create_item_collection_with_response_models(
    core_client: DummyCoreClient, item: Item, item_collection: ItemCollection
) -> None:
    class EchoTransactionsClient(DummyTransactionsClient):
        def create_item(self, item: Item | ItemCollection, *args, **kwargs):
            return item.model_dump(mode="json")

    settings = ApiSettings(enable_response_models=True)
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            TransactionExtension(client=EchoTransactionsClient(), settings=settings),
        ],
    )
    with TestClient(api.app) as client:
        response = client.post("/collections/a-collection/items", json=item_collection)
        assert response.status_code == 201, response.text
        assert response.json()["type"] == "FeatureCollection"

        response = client.post("/collections/a-collection/items", json=item)
        assert response.status_code == 201, response.text
        assert response.json()["type"] == "Feature"


def test_update_item(client: TestClient, item: Item) -> None:
    response = client.put("/collections/a-collection/items/an-item", json=item)
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["path_item_id"] == "an-item"
    assert response.json()["type"] == "Feature"


def test_patch_operation_item(client: TestClient) -> None:
    response = client.patch(
        "/collections/a-collection/items/an-item",
        json=[{"op": "add", "path": "/properties/foo", "value": "bar"}],
    )
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["path_item_id"] == "an-item"
    assert response.json()["patch"] == [
        {"op": "add", "path": "/properties/foo", "value": "bar"}
    ]


def test_patch_merge_item(client: TestClient) -> None:
    response = client.patch(
        "/collections/a-collection/items/an-item",
        json={"properties": {"hello": "world", "foo": None}},
    )
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["path_item_id"] == "an-item"
    assert response.json()["patch"] == [
        {"op": "add", "path": "/properties/hello", "value": "world"},
        {"op": "remove", "path": "/properties/foo"},
    ]


def test_delete_item(client: TestClient) -> None:
    response = client.delete("/collections/a-collection/items/an-item")
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["path_item_id"] == "an-item"


def test_create_collection(client: TestClient, collection: Collection) -> None:
    response = client.post("/collections", json=collection)
    assert response.status_code == 201, response.text
    assert response.json()["type"] == "Collection"
    assert response.headers["location"].endswith("/collections/test_collection")


def test_create_collection_response_location(
    response_client: TestClient, collection: Collection
) -> None:
    """A `Location` header set by the client is preserved."""
    response = response_client.post("/collections", json=collection)
    assert response.status_code == 201, response.text
    assert response.headers["location"] == "/custom-location"


def test_update_collection(client: TestClient, collection: Collection) -> None:
    response = client.put("/collections/a-collection", json=collection)
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["type"] == "Collection"


def test_patch_operation_collection(client: TestClient) -> None:
    response = client.patch(
        "/collections/a-collection",
        json=[{"op": "add", "path": "/properties/foo", "value": "bar"}],
    )
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["patch"] == [
        {"op": "add", "path": "/properties/foo", "value": "bar"}
    ]


def test_patch_merge_collection(client: TestClient) -> None:
    response = client.patch(
        "/collections/a-collection",
        json={"summaries": {"hello": "world", "foo": None}},
    )
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"
    assert response.json()["patch"] == [
        {"op": "add", "path": "/summaries/hello", "value": "world"},
        {"op": "remove", "path": "/summaries/foo"},
    ]


def test_patch_merge_collection_links(client: TestClient) -> None:
    links = [{"rel": "self", "href": "https://example.com/collections/a-collection"}]
    response = client.patch("/collections/a-collection", json={"links": links})
    assert response.is_success, response.text
    assert response.json()["patch"] == [{"op": "add", "path": "/links", "value": links}]


def test_delete_collection(client: TestClient, collection: Collection) -> None:
    response = client.delete("/collections/a-collection")
    assert response.is_success, response.text
    assert response.json()["path_collection_id"] == "a-collection"


@pytest.fixture
def client(
    core_client: DummyCoreClient, transactions_client: DummyTransactionsClient
) -> Iterator[TestClient]:
    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            TransactionExtension(client=transactions_client, settings=settings),
        ],
    )
    with TestClient(api.app) as client:
        yield client


@pytest.fixture
def core_client() -> DummyCoreClient:
    return DummyCoreClient()


@pytest.fixture
def transactions_client() -> DummyTransactionsClient:
    return DummyTransactionsClient()


@pytest.fixture
def response_client(core_client: DummyCoreClient) -> Iterator[TestClient]:
    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            TransactionExtension(client=ResponseTransactionsClient(), settings=settings),
        ],
    )
    with TestClient(api.app) as client:
        yield client


@pytest.fixture
def item_collection(item: Item) -> ItemCollection:
    return {
        "type": "FeatureCollection",
        "features": [item],
        "links": [],
        "context": None,
    }


@pytest.fixture
def item() -> Item:
    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "stac_extensions": [],
        "id": "test_item",
        "geometry": {"type": "Point", "coordinates": [-105, 40]},
        "bbox": [-105, 40, -105, 40],
        "properties": {"datetime": "2020-06-13T13:00:00Z"},
        "links": [],
        "assets": {},
        "collection": "test_collection",
    }


@pytest.fixture
def collection() -> Collection:
    return {
        "type": "Collection",
        "stac_version": "1.0.0",
        "stac_extensions": [],
        "id": "test_collection",
        "description": "A test collection",
        "extent": {
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [["2000-01-01T00:00:00Z", "2024-01-01T00:00:00Z"]]},
        },
        "links": [],
        "assets": {},
        "license": "proprietary",
    }
