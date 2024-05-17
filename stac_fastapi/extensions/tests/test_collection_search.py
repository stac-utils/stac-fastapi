from typing import Iterator

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import CollectionSearchExtension
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCollectionSearchClient, BaseCoreClient
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


class DummyCollectionSearchClient(BaseCollectionSearchClient):
    """Defines a pattern for implementing the STAC transaction extension."""

    def get_collection_search(self, *args, **kwargs):
        return NotImplementedError

    def post_collection_search(self, *args, **kwargs):
        return NotImplementedError


@pytest.fixture
def client(
    core_client: DummyCoreClient, collection_search_client: DummyCollectionSearchClient
) -> Iterator[TestClient]:
    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            CollectionSearchExtension(client=collection_search_client, settings=settings),
        ],
    )
    with TestClient(api.app) as client:
        yield client


@pytest.fixture
def core_client() -> DummyCoreClient:
    return DummyCoreClient()


@pytest.fixture
def collection_search_client() -> DummyCollectionSearchClient:
    return DummyCollectionSearchClient()


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
