from typing import Iterator

import pytest
from stac_pydantic.api.collections import Collections
from stac_pydantic.shared import BBox
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import CollectionSearchExtension
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCollectionSearchClient, BaseCoreClient
from stac_fastapi.types.rfc3339 import DateTimeType
from stac_fastapi.types.search import (
    BaseCollectionSearchPostRequest,
)
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
    """Defines a pattern for implementing the STAC collection search extension."""

    def post_all_collections(
        self, search_request: BaseCollectionSearchPostRequest, **kwargs
    ) -> Collections:
        assert search_request.bbox == BBox([-180, -90, 180, 90])
        assert search_request.datetime == DateTimeType("2024-01-01T00:00:00Z")
        assert search_request.limit == 10

        return Collections(
            collections=[Collections()],
            links=[
                {"href": "test", "rel": "root"},
                {"href": "test", "rel": "self"},
                {"href": "test", "rel": "parent"},
            ],
        )


def test_post_collection_search(client: TestClient) -> None:
    post_collections = client.post(
        "/collections",
        json={},
        #     "bbox": [-180,-90,180,90],
        #     "datetime": "2024-01-01T00:00:00Z",
        #     "limit": 10,
        # },
    )
    assert post_collections.status_code == 200, post_collections.text
    Collections(**post_collections.json())


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
