from typing import Iterator

import pytest
from fastapi import Depends, FastAPI
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import AggregationExtension
from stac_fastapi.extensions.core.aggregation.client import BaseAggregationClient
from stac_fastapi.extensions.core.aggregation.request import (
    AggregationExtensionGetRequest,
)
from stac_fastapi.extensions.core.aggregation.types import (
    Aggregation,
    AggregationCollection,
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


def test_get_aggregations(client: TestClient) -> None:
    response = client.get("/aggregations")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == [
        {"name": "total_count", "data_type": "integer"}
    ]
    assert AggregationCollection(
        type="AggregationCollection",
        aggregations=[Aggregation(**response.json()["aggregations"][0])],
    )


def test_get_aggregate(client: TestClient) -> None:
    response = client.get("/aggregate")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == []
    assert AggregationCollection(
        type="AggregationCollection", aggregations=response.json()["aggregations"]
    )


def test_post_aggregations(client: TestClient) -> None:
    response = client.post("/aggregations")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == [
        {"name": "total_count", "data_type": "integer"}
    ]
    assert AggregationCollection(
        type="AggregationCollection",
        aggregations=[Aggregation(**response.json()["aggregations"][0])],
    )


def test_post_aggregate(client: TestClient) -> None:
    response = client.post("/aggregate", content="{}")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == []
    assert AggregationCollection(
        type="AggregationCollection", aggregations=response.json()["aggregations"]
    )


@pytest.fixture
def client(
    core_client: DummyCoreClient, aggregations_client: BaseAggregationClient
) -> Iterator[TestClient]:
    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=core_client,
        extensions=[
            AggregationExtension(client=aggregations_client),
        ],
    )
    with TestClient(api.app) as client:
        yield client


@pytest.fixture
def core_client() -> DummyCoreClient:
    return DummyCoreClient()


@pytest.fixture
def aggregations_client() -> BaseAggregationClient:
    return BaseAggregationClient()


def test_agg_get_query():
    """test AggregationExtensionGetRequest model."""
    app = FastAPI()

    @app.get("/test")
    def test(query=Depends(AggregationExtensionGetRequest)):
        return query

    with TestClient(app) as client:
        response = client.get("/test")
        assert response.is_success
        params = response.json()
        assert not params["collections"]
        assert not params["aggregations"]

        response = client.get(
            "/test",
            params={
                "collections": "collection1,collection2",
                "aggregations": "prop1,prop2",
            },
        )
        assert response.is_success
        params = response.json()
        assert params["collections"] == ["collection1", "collection2"]
        assert params["aggregations"] == ["prop1", "prop2"]
