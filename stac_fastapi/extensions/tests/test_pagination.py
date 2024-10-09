from typing import Iterator

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import (
    EmptyRequest,
    create_post_request_model,
    create_request_model,
)
from stac_fastapi.extensions.core import (
    OffsetPaginationExtension,
    PaginationExtension,
    TokenPaginationExtension,
)
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient
from stac_fastapi.types.search import BaseSearchGetRequest


class DummyCoreClient(BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return args, kwargs

    def get_collection(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return args, kwargs

    def get_item(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return args, kwargs

    def get_search(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return args, kwargs

    def post_search(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return args[0].model_dump(), kwargs

    def item_collection(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return args, kwargs


collections_get_request_model = create_request_model(
    model_name="CollectionsGetRequest",
    base_model=EmptyRequest,
    mixins=[
        OffsetPaginationExtension().GET,
    ],
    request_type="GET",
)

items_get_request_model = create_request_model(
    model_name="ItemsGetRequest",
    base_model=EmptyRequest,
    mixins=[
        PaginationExtension().GET,
    ],
    request_type="GET",
)

search_get_request_model = create_request_model(
    model_name="SearchGetRequest",
    base_model=BaseSearchGetRequest,
    mixins=[
        TokenPaginationExtension().GET,
    ],
    request_type="GET",
)


@pytest.fixture
def client() -> Iterator[TestClient]:
    settings = ApiSettings()

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=[],
        collections_get_request_model=collections_get_request_model,
        items_get_request_model=items_get_request_model,
        search_get_request_model=search_get_request_model,
        search_post_request_model=create_post_request_model([]),
    )
    with TestClient(api.app) as client:
        yield client


def test_pagination_extension(client: TestClient):
    """Test endpoints with pagination extensions."""
    # OffsetPaginationExtension
    response = client.get("/collections")
    assert response.is_success, response.json()
    arg, kwargs = response.json()
    assert "offset" in kwargs
    assert kwargs["offset"] is None

    response = client.get("/collections", params={"offset": 1})
    assert response.is_success, response.json()
    arg, kwargs = response.json()
    assert "offset" in kwargs
    assert kwargs["offset"] == 1

    # PaginationExtension
    response = client.get("/collections/a_collection/items")
    assert response.is_success, response.json()
    arg, kwargs = response.json()
    assert "page" in kwargs
    assert kwargs["page"] is None

    response = client.get("/collections/a_collection/items", params={"page": "1"})
    assert response.is_success, response.json()
    arg, kwargs = response.json()
    assert "page" in kwargs
    assert kwargs["page"] == "1"

    # TokenPaginationExtension
    response = client.get("/search")
    assert response.is_success, response.json()
    arg, kwargs = response.json()
    assert "token" in kwargs
    assert kwargs["token"] is None

    response = client.get("/search", params={"token": "atoken"})
    assert response.is_success, response.json()
    arg, kwargs = response.json()
    assert "token" in kwargs
    assert kwargs["token"] == "atoken"
