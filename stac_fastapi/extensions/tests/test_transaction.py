import json
from typing import Iterator, Union

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import TransactionExtension
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient, BaseTransactionsClient
from stac_fastapi.types.stac import Item, ItemCollection


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
    """Defines a pattern for implementing the STAC transaction extension."""

    def create_item(self, item: Union[Item, ItemCollection], *args, **kwargs):
        return {"created": True, "type": item["type"]}

    def update_item(self, *args, **kwargs):
        raise NotImplementedError

    def delete_item(self, *args, **kwargs):
        raise NotImplementedError

    def create_collection(self, *args, **kwargs):
        raise NotImplementedError

    def update_collection(self, *args, **kwargs):
        raise NotImplementedError

    def delete_collection(self, *args, **kwargs):
        raise NotImplementedError


def test_create_item(client: TestClient, item: Item) -> None:
    response = client.post("/collections/a-collection/items", content=json.dumps(item))
    assert response.is_success, response.text
    assert response.json()["type"] == "Feature"


def test_create_item_collection(
    client: TestClient, item_collection: ItemCollection
) -> None:
    response = client.post(
        "/collections/a-collection/items", content=json.dumps(item_collection)
    )
    assert response.is_success, response.text
    assert response.json()["type"] == "FeatureCollection"


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
        "properties": {},
        "links": [],
        "assets": {},
        "collection": "test_collection",
    }
