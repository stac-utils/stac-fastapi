from datetime import datetime
from typing import List, Optional, Union

import pytest
from stac_pydantic.api.utils import link_factory
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient, BaseSearchPostRequest, NumType

collection_links = link_factory.CollectionLinks("/", "test").create_links()
item_links = link_factory.ItemLinks("/", "test", "test").create_links()


collections = [
    stac_types.Collection(
        id=f"test_collection_{n}",
        title="Test Collection",
        description="A test collection",
        keywords=["test"],
        license="proprietary",
        extent={
            "spatial": {"bbox": [[-180, -90, 180, 90]]},
            "temporal": {"interval": [["2000-01-01T00:00:00Z", None]]},
        },
        links=collection_links.dict(exclude_none=True),
    )
    for n in range(0, 10)
]

items = [
    stac_types.Item(
        id=f"test_item_{n}",
        type="Feature",
        geometry={"type": "Point", "coordinates": [0, 0]},
        bbox=[-180, -90, 180, 90],
        properties={"datetime": "2000-01-01T00:00:00Z"},
        links=item_links.dict(exclude_none=True),
        assets={},
    )
    for n in range(0, 1000)
]


class CoreClient(BaseCoreClient):
    def post_search(
        self, search_request: BaseSearchPostRequest, **kwargs
    ) -> stac_types.ItemCollection:
        raise NotImplementedError

    def get_search(
        self,
        collections: Optional[List[str]] = None,
        ids: Optional[List[str]] = None,
        bbox: Optional[List[NumType]] = None,
        intersects: Optional[str] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: Optional[int] = 10,
        **kwargs,
    ) -> stac_types.ItemCollection:
        raise NotImplementedError

    def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac_types.Item:
        raise NotImplementedError

    def all_collections(self, **kwargs) -> stac_types.Collections:
        return stac_types.Collections(
            collections=collections,
            links=[
                {"href": "test", "rel": "root"},
                {"href": "test", "rel": "self"},
                {"href": "test", "rel": "parent"},
            ],
        )

    def get_collection(self, collection_id: str, **kwargs) -> stac_types.Collection:
        return collections[0]

    def item_collection(
        self,
        collection_id: str,
        bbox: Optional[List[Union[float, int]]] = None,
        datetime: Optional[Union[str, datetime]] = None,
        limit: int = 10,
        token: str = None,
        **kwargs,
    ) -> stac_types.ItemCollection:
        return stac_types.ItemCollection(
            type="FeatureCollection",
            features=items[0:limit],
            links=[
                {"href": "test", "rel": "root"},
                {"href": "test", "rel": "self"},
                {"href": "test", "rel": "parent"},
            ],
        )


@pytest.fixture(autouse=True)
def client_validation() -> TestClient:
    settings = ApiSettings(enable_response_models=True)
    app = StacApi(settings=settings, client=CoreClient())
    with TestClient(app.app) as client:
        yield client


@pytest.fixture(autouse=True)
def client_no_validation() -> TestClient:
    settings = ApiSettings(enable_response_models=False)
    app = StacApi(settings=settings, client=CoreClient())
    with TestClient(app.app) as client:
        yield client


@pytest.mark.parametrize("limit", [1, 10, 50, 100, 200, 250, 1000])
@pytest.mark.parametrize("validate", [True, False])
def test_benchmark_items(
    benchmark, client_validation, client_no_validation, validate, limit
):
    """Benchmark items endpoint."""
    params = {"limit": limit}

    def f(p):
        if validate:
            return client_validation.get("/collections/fake_collection/items", params=p)
        else:
            return client_no_validation.get(
                "/collections/fake_collection/items", params=p
            )

    benchmark.group = "Items With Model validation" if validate else "Items"
    benchmark.name = (
        f"Items With Model validation ({limit})"
        if validate
        else f"Items Limit: ({limit})"
    )
    benchmark.fullname = (
        f"Items With Model validation ({limit})"
        if validate
        else f"Items Limit: ({limit})"
    )

    response = benchmark(f, params)
    assert response.status_code == 200


@pytest.mark.parametrize("validate", [True, False])
def test_benchmark_collection(
    benchmark, client_validation, client_no_validation, validate
):
    """Benchmark items endpoint."""

    def f():
        if validate:
            return client_validation.get("/collections/fake_collection")
        else:
            return client_no_validation.get("/collections/fake_collection")

    benchmark.group = "Collection With Model validation" if validate else "Collection"
    benchmark.name = "Collection With Model validation" if validate else "Collection"
    benchmark.fullname = "Collection With Model validation" if validate else "Collection"

    response = benchmark(f)
    assert response.status_code == 200


@pytest.mark.parametrize("validate", [True, False])
def test_benchmark_collections(
    benchmark, client_validation, client_no_validation, validate
):
    """Benchmark items endpoint."""

    def f():
        if validate:
            return client_validation.get("/collections")
        else:
            return client_no_validation.get("/collections")

    benchmark.group = "Collections With Model validation" if validate else "Collections"
    benchmark.name = "Collections With Model validation" if validate else "Collections"
    benchmark.fullname = (
        "Collections With Model validation" if validate else "Collections"
    )

    response = benchmark(f)
    assert response.status_code == 200
