import importlib
from datetime import datetime
from typing import List, Optional, Union

import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_get_request_model, create_post_request_model
from stac_fastapi.extensions.core.filter.filter import FilterExtension
from stac_fastapi.types import core, response_model, search
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import NumType
from stac_fastapi.types.search import BaseSearchPostRequest


@pytest.mark.parametrize(
    "validate, response_type",
    [
        ("True", BaseModel),
        ("False", dict),
    ],
)
def test_client_response_type(validate, response_type, TestCoreClient, monkeypatch):
    """Test for correct response type when VALIDATE_RESPONSE is set."""
    monkeypatch.setenv("VALIDATE_RESPONSE", validate)

    importlib.reload(response_model)
    importlib.reload(core)

    test_app = StacApi(
        settings=ApiSettings(),
        client=TestCoreClient(),
    )

    class MockRequest:
        base_url = "http://test"
        app = test_app.app

    assert isinstance(TestCoreClient().landing_page(request=MockRequest()), response_type)
    assert isinstance(TestCoreClient().get_collection("test"), response_type)
    assert isinstance(TestCoreClient().all_collections(), response_type)
    assert isinstance(TestCoreClient().get_item("test", "test"), response_type)
    assert isinstance(TestCoreClient().item_collection("test"), response_type)
    assert isinstance(
        TestCoreClient().post_search(search.BaseSearchPostRequest()), response_type
    )
    assert isinstance(
        TestCoreClient().get_search(),
        response_type,
    )


def test_filter_extension(TestCoreClient, item_dict):
    """Test if Filter Parameters are passed correctly."""

    class FilterClient(TestCoreClient):
        def post_search(
            self, search_request: BaseSearchPostRequest, **kwargs
        ) -> response_model.ItemCollection:
            search_request.collections = ["test"]
            search_request.filter = {}
            search_request.filter_crs = "EPSG:4326"
            search_request.filter_lang = "cql2-text"

            return response_model.ItemCollection(
                type="FeatureCollection", features=[response_model.Item(**item_dict)]
            )

        def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[NumType]] = None,
            intersects: Optional[str] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: Optional[int] = 10,
            filter: Optional[str] = None,
            filter_crs: Optional[str] = None,
            filter_lang: Optional[str] = None,
            **kwargs,
        ) -> response_model.ItemCollection:
            # Check if all filter parameters are passed correctly

            assert filter == "TEST"

            # FIXME: https://github.com/stac-utils/stac-fastapi/issues/638
            # hyphen alias for filter_crs and filter_lang are currently not working
            # Query parameters `filter-crs` and `filter-lang`
            # should be recognized by the API
            # They are present in the `request.query_params` but not in the `kwargs`

            # assert filter_crs == "EPSG:4326"
            # assert filter_lang == "cql2-text"

            return response_model.ItemCollection(
                type="FeatureCollection", features=[response_model.Item(**item_dict)]
            )

    post_request_model = create_post_request_model([FilterExtension()])

    test_app = StacApi(
        settings=ApiSettings(),
        client=FilterClient(post_request_model=post_request_model),
        search_get_request_model=create_get_request_model([FilterExtension()]),
        search_post_request_model=post_request_model,
    )

    with TestClient(test_app.app) as client:
        landing = client.get("/")
        collection = client.get("/collections/test")
        collections = client.get("/collections")
        item = client.get("/collections/test/items/test")
        item_collection = client.get(
            "/collections/test/items",
            params={"limit": 10},
        )
        get_search = client.get(
            "/search",
            params={
                "filter": "TEST",
                "filter-crs": "EPSG:4326",
                "filter-lang": "cql2-text",
            },
        )
        post_search = client.post(
            "/search",
            json={
                "collections": ["test"],
                "filter": {},
                "filter-crs": "EPSG:4326",
                "filter-lang": "cql2-text",
            },
        )

    assert landing.status_code == 200, landing.text
    assert collection.status_code == 200, collection.text
    assert collections.status_code == 200, collections.text
    assert item.status_code == 200, item.text
    assert item_collection.status_code == 200, item_collection.text
    assert get_search.status_code == 200, get_search.text
    assert post_search.status_code == 200, post_search.text
