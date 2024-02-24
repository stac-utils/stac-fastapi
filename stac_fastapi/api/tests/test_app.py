import importlib
import os
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
from stac_fastapi.types.search import BaseSearchPostRequest


@pytest.fixture
def cleanup():
    old_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(old_environ)


@pytest.mark.parametrize(
    "validate, response_type",
    [
        ("True", BaseModel),
        ("False", dict),
    ],
)
def test_app(validate, response_type, collection_dict, item_dict, cleanup):
    os.environ["VALIDATE_RESPONSE"] = str(validate)
    importlib.reload(response_model)
    importlib.reload(core)

    class MyCoreClient(core.BaseCoreClient):
        def post_search(
            self, search_request: BaseSearchPostRequest, **kwargs
        ) -> response_model.ItemCollection:
            return response_model.ItemCollection(
                type="FeatureCollection", features=[response_model.Item(**item_dict)]
            )

        def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[Union[float, int]]] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: Optional[int] = 10,
            query: Optional[str] = None,
            token: Optional[str] = None,
            fields: Optional[List[str]] = None,
            sortby: Optional[str] = None,
            intersects: Optional[str] = None,
            **kwargs,
        ) -> response_model.ItemCollection:
            # FIXME: hyphen alias for filter_crs and filter_lang are currently not working
            # assert kwargs.get("filter_crs") == "EPSG:4326"
            # assert kwargs.get("filter_lang") == "cql-test"

            return response_model.ItemCollection(
                type="FeatureCollection", features=[response_model.Item(**item_dict)]
            )

        def get_item(
            self, item_id: str, collection_id: str, **kwargs
        ) -> response_model.Item:
            return response_model.Item(**item_dict)

        def all_collections(self, **kwargs) -> response_model.Collections:
            return response_model.Collections(
                collections=[response_model.Collection(**collection_dict)],
                links=[
                    {"href": "test", "rel": "root"},
                    {"href": "test", "rel": "self"},
                    {"href": "test", "rel": "parent"},
                ],
            )

        def get_collection(
            self, collection_id: str, **kwargs
        ) -> response_model.Collection:
            return response_model.Collection(**collection_dict)

        def item_collection(
            self,
            collection_id: str,
            bbox: Optional[List[Union[float, int]]] = None,
            datetime: Optional[Union[str, datetime]] = None,
            limit: int = 10,
            token: str = None,
            **kwargs,
        ) -> response_model.ItemCollection:
            return response_model.ItemCollection(
                type="FeatureCollection", features=[response_model.Item(**item_dict)]
            )

    post_request_model = create_post_request_model([FilterExtension()])

    test_app = StacApi(
        settings=ApiSettings(),
        client=MyCoreClient(post_request_model=post_request_model),
        search_get_request_model=create_get_request_model([FilterExtension()]),
        search_post_request_model=post_request_model,
    )

    class MockRequest:
        base_url = "http://test"
        app = test_app.app

    assert isinstance(MyCoreClient().landing_page(request=MockRequest()), response_type)
    assert isinstance(MyCoreClient().get_collection("test"), response_type)
    assert isinstance(MyCoreClient().all_collections(), response_type)
    assert isinstance(MyCoreClient().get_item("test", "test"), response_type)
    assert isinstance(MyCoreClient().item_collection("test"), response_type)
    assert isinstance(
        MyCoreClient().post_search(search.BaseSearchPostRequest()), response_type
    )
    assert isinstance(
        MyCoreClient().get_search(
            **{"filter_crs": "EPSG:4326", "filter_lang": "cql-test"}
        ),
        response_type,
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
            "/search", params={"filter-crs": "EPSG:4326", "filter-lang": "cql-test"}
        )
        post_search = client.post("/search", json={"collections": ["test"]})

    assert landing.status_code == 200, landing.text
    assert collection.status_code == 200, collection.text
    assert collections.status_code == 200, collections.text
    assert item.status_code == 200, item.text
    assert item_collection.status_code == 200, item_collection.text
    assert get_search.status_code == 200, get_search.text
    assert post_search.status_code == 200, post_search.text
