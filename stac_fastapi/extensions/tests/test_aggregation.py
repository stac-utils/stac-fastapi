from typing import Iterator

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import AggregationExtension
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseAggregationClient, BaseCoreClient


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


def test_get_aggregate(client: TestClient) -> None:
    response = client.get("/aggregate")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == []


def test_post_aggregations(client: TestClient) -> None:
    response = client.post("/aggregations")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == [
        {"name": "total_count", "data_type": "integer"}
    ]


def test_post_aggregate(client: TestClient) -> None:
    response = client.post("/aggregate")
    assert response.is_success, response.text
    assert response.json()["aggregations"] == []


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
