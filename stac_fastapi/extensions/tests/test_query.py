import json
from typing import Iterator
from urllib.parse import quote_plus, unquote_plus

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_get_request_model, create_post_request_model
from stac_fastapi.extensions.core import QueryExtension
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
        return kwargs.pop("query", None)

    def post_search(self, *args, **kwargs):
        return args[0].query

    def item_collection(self, *args, **kwargs):
        raise NotImplementedError


@pytest.fixture
def client() -> Iterator[TestClient]:
    settings = ApiSettings()
    extensions = [QueryExtension()]

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=extensions,
        search_get_request_model=create_get_request_model(extensions),
        search_post_request_model=create_post_request_model(extensions),
    )
    with TestClient(api.app) as client:
        yield client


def test_search_query_get(client: TestClient):
    """Test search GET endpoints with query ext."""
    response = client.get(
        "/search",
        params={"collections": ["test"]},
    )
    assert response.is_success
    assert not response.text

    response = client.get(
        "/search",
        params={
            "collections": ["test"],
            "query": quote_plus(
                json.dumps({"eo:cloud_cover": {"gte": 95}}),
            ),
        },
    )
    assert response.is_success, response.json()
    query = json.loads(unquote_plus(response.json()))
    assert query["eo:cloud_cover"] == {"gte": 95}


def test_search_query_post(client: TestClient):
    """Test search POST endpoints with query ext."""
    response = client.post(
        "/search",
        json={
            "collections": ["test"],
        },
    )

    assert response.is_success
    assert not response.text

    response = client.post(
        "/search",
        json={
            "collections": ["test"],
            "query": {"eo:cloud_cover": {"gte": 95}},
        },
    )

    assert response.is_success, response.json()
    assert response.json()["eo:cloud_cover"] == {"gte": 95}
