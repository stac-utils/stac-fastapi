from datetime import datetime
from typing import List, Optional, Union

import pytest
from stac_pydantic import Collection, Item
from stac_pydantic.api.utils import link_factory

from stac_fastapi.types import core, stac
from stac_fastapi.types.core import NumType
from stac_fastapi.types.search import BaseSearchPostRequest

collection_links = link_factory.CollectionLinks("/", "test").create_links()
item_links = link_factory.ItemLinks("/", "test", "test").create_links()


@pytest.fixture
def _collection():
    return Collection(
        id="test_collection",
        title="Test Collection",
        description="A test collection",
        keywords=["test"],
        license="proprietary",
        extent={
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [["2000-01-01T00:00:00Z", None]]},
        },
        links=collection_links,
    )


@pytest.fixture
def collection(_collection: Collection):
    return _collection.model_dump_json()


@pytest.fixture
def collection_dict(_collection: Collection):
    return _collection.model_dump(mode="json")


@pytest.fixture
def _item():
    return Item(
        id="test_item",
        type="Feature",
        geometry={"type": "Point", "coordinates": [0, 0]},
        bbox=[-180, -90, 180, 90],
        properties={"datetime": "2000-01-01T00:00:00Z"},
        links=item_links,
        assets={},
    )


@pytest.fixture
def item(_item: Item):
    return _item.model_dump_json()


@pytest.fixture
def item_dict(_item: Item):
    return _item.model_dump(mode="json")


@pytest.fixture
def TestCoreClient(collection_dict, item_dict):
    class CoreClient(core.BaseCoreClient):
        def post_search(
            self, search_request: BaseSearchPostRequest, **kwargs
        ) -> stac.ItemCollection:
            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

        def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[NumType]] = None,
            intersects: Optional[str] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: Optional[int] = 10,
            **kwargs,
        ) -> stac.ItemCollection:
            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

        def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
            return stac.Item(**item_dict)

        def all_collections(self, **kwargs) -> stac.Collections:
            return stac.Collections(
                collections=[stac.Collection(**collection_dict)],
                links=[
                    {"href": "test", "rel": "root"},
                    {"href": "test", "rel": "self"},
                    {"href": "test", "rel": "parent"},
                ],
            )

        def get_collection(self, collection_id: str, **kwargs) -> stac.Collection:
            return stac.Collection(**collection_dict)

        def item_collection(
            self,
            collection_id: str,
            bbox: Optional[List[Union[float, int]]] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: int = 10,
            token: str = None,
            **kwargs,
        ) -> stac.ItemCollection:
            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

    return CoreClient


@pytest.fixture
def AsyncTestCoreClient(collection_dict, item_dict):
    class AsyncCoreClient(core.AsyncBaseCoreClient):
        async def post_search(
            self, search_request: BaseSearchPostRequest, **kwargs
        ) -> stac.ItemCollection:
            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

        async def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[NumType]] = None,
            intersects: Optional[str] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: Optional[int] = 10,
            **kwargs,
        ) -> stac.ItemCollection:
            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

        async def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
            return stac.Item(**item_dict)

        async def all_collections(self, **kwargs) -> stac.Collections:
            return stac.Collections(
                collections=[stac.Collection(**collection_dict)],
                links=[
                    {"href": "test", "rel": "root"},
                    {"href": "test", "rel": "self"},
                    {"href": "test", "rel": "parent"},
                ],
            )

        async def get_collection(self, collection_id: str, **kwargs) -> stac.Collection:
            return stac.Collection(**collection_dict)

        async def item_collection(
            self,
            collection_id: str,
            bbox: Optional[List[Union[float, int]]] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: int = 10,
            token: str = None,
            **kwargs,
        ) -> stac.ItemCollection:
            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

    return AsyncCoreClient
