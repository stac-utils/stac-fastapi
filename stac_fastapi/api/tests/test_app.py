from typing import List, Optional, Union

import attr
import pytest
from fastapi import Path, Query
from fastapi.testclient import TestClient
from pydantic import ValidationError
from stac_pydantic import api
from typing_extensions import Annotated

from stac_fastapi.api import app
from stac_fastapi.api.models import (
    APIRequest,
    JSONResponse,
    create_get_request_model,
    create_post_request_model,
)
from stac_fastapi.extensions.core import (
    FieldsExtension,
    FilterExtension,
    SearchFilterExtension,
)
from stac_fastapi.types import stac
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient, NumType
from stac_fastapi.types.search import BaseSearchPostRequest


def test_client_response_type(TestCoreClient):
    """Test all GET endpoints. Verify that responses are valid STAC items."""

    test_app = app.StacApi(
        settings=ApiSettings(),
        client=TestCoreClient(),
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
                "collections": ["test"],
            },
        )
        post_search = client.post(
            "/search",
            json={
                "collections": ["test"],
            },
        )

    assert landing.status_code == 200, landing.text
    api.LandingPage(**landing.json())

    assert collection.status_code == 200, collection.text
    api.Collection(**collection.json())

    assert collections.status_code == 200, collections.text
    api.collections.Collections(**collections.json())

    assert item.status_code == 200, item.text
    api.Item(**item.json())

    assert item_collection.status_code == 200, item_collection.text
    api.ItemCollection(**item_collection.json())

    assert get_search.status_code == 200, get_search.text
    api.ItemCollection(**get_search.json())

    assert post_search.status_code == 200, post_search.text
    api.ItemCollection(**post_search.json())


@pytest.mark.parametrize("validate", [True, False])
def test_client_invalid_response_type(validate, TestCoreClient, item_dict):
    """Check if the build in response validation switch works."""

    class InValidResponseClient(TestCoreClient):
        def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
            item_dict.pop("bbox")
            item_dict.pop("geometry")
            return stac.Item(**item_dict)

    test_app = app.StacApi(
        settings=ApiSettings(enable_response_models=validate),
        client=InValidResponseClient(),
    )

    with TestClient(test_app.app) as client:
        item = client.get("/collections/test/items/test")

    # Even if API validation passes, we should receive an invalid item
    if item.status_code == 200:
        with pytest.raises(ValidationError):
            api.Item(**item.json())

    # If internal validation is on, we should expect an internal error
    if validate:
        assert item.status_code == 500, item.text
    else:
        assert item.status_code == 200, item.text


def test_client_openapi(TestCoreClient):
    """Test if response models are all documented with OpenAPI."""

    test_app = app.StacApi(
        settings=ApiSettings(),
        client=TestCoreClient(),
    )
    test_app.app.openapi()
    components = ["LandingPage", "Collection", "Collections", "Item", "ItemCollection"]
    for component in components:
        assert component in test_app.app.openapi_schema["components"]["schemas"]


@pytest.mark.parametrize("validate", [True, False])
def test_filter_extension(validate, TestCoreClient, item_dict):
    """Test if Filter Parameters are passed correctly."""

    class FilterClient(TestCoreClient):
        def post_search(
            self, search_request: BaseSearchPostRequest, **kwargs
        ) -> stac.ItemCollection:
            search_request.collections = ["test"]
            search_request.filter_expr = {}
            search_request.filter_crs = "EPSG:4326"
            search_request.filter_lang = "cql2-text"

            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

        def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[NumType]] = None,
            intersects: Optional[str] = None,
            datetime: Optional[str] = None,
            limit: Optional[int] = 10,
            filter_expr: Optional[str] = None,
            filter_crs: Optional[str] = None,
            filter_lang: Optional[str] = None,
            **kwargs,
        ) -> stac.ItemCollection:
            assert filter_expr == "TEST"
            assert filter_crs == "EPSG:4326"
            assert filter_lang == "cql2-text"

            return stac.ItemCollection(
                type="FeatureCollection", features=[stac.Item(**item_dict)]
            )

    test_app = app.StacApi(
        settings=ApiSettings(enable_response_models=validate),
        client=FilterClient(),
        search_get_request_model=create_get_request_model([FilterExtension()]),
        search_post_request_model=create_post_request_model([FilterExtension()]),
        extensions=[FilterExtension()],
    )

    with TestClient(test_app.app) as client:
        landing = client.get("/")
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
                "filter-lang": "cql2-json",
            },
        )

    assert landing.status_code == 200, landing.text
    assert "Queryables" in [link.get("title") for link in landing.json()["links"]]
    assert get_search.status_code == 200, get_search.text
    assert post_search.status_code == 200, post_search.text

    test_app = app.StacApi(
        settings=ApiSettings(enable_response_models=validate),
        client=FilterClient(),
        search_get_request_model=create_get_request_model([SearchFilterExtension()]),
        search_post_request_model=create_post_request_model([SearchFilterExtension()]),
        extensions=[SearchFilterExtension()],
    )

    with TestClient(test_app.app) as client:
        landing = client.get("/")
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
                "filter-lang": "cql2-json",
            },
        )

    assert landing.status_code == 200, landing.text
    assert "Queryables" in [link.get("title") for link in landing.json()["links"]]
    assert get_search.status_code == 200, get_search.text
    assert post_search.status_code == 200, post_search.text


@pytest.mark.parametrize("validate", [True, False])
def test_fields_extension(validate, TestCoreClient, item_dict):
    """Test if fields Parameters are passed correctly."""

    class BadCoreClient(BaseCoreClient):
        def post_search(
            self, search_request: BaseSearchPostRequest, **kwargs
        ) -> stac.ItemCollection:
            resp = {"not": "a proper stac item"}

            # if `fields` extension is enabled, then we return a JSONResponse
            # to avoid Item validation
            if getattr(search_request, "fields", None):
                return JSONResponse(content=resp)

            return resp

        def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[NumType]] = None,
            intersects: Optional[str] = None,
            datetime: Optional[str] = None,
            limit: Optional[int] = 10,
            **kwargs,
        ) -> stac.ItemCollection:
            resp = {"not": "a proper stac item"}

            # if `fields` extension is enabled, then we return a JSONResponse
            # to avoid Item validation
            if "fields" in kwargs:
                return JSONResponse(content=resp)

            return resp

        def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
            raise NotImplementedError

        def all_collections(self, **kwargs) -> stac.Collections:
            raise NotImplementedError

        def get_collection(self, collection_id: str, **kwargs) -> stac.Collection:
            raise NotImplementedError

        def item_collection(
            self,
            collection_id: str,
            bbox: Optional[List[Union[float, int]]] = None,
            datetime: Optional[str] = None,
            limit: int = 10,
            token: str = None,
            **kwargs,
        ) -> stac.ItemCollection:
            raise NotImplementedError

    # With FieldsExtension
    test_app = app.StacApi(
        settings=ApiSettings(enable_response_models=validate),
        client=BadCoreClient(),
        search_get_request_model=create_get_request_model([FieldsExtension()]),
        search_post_request_model=create_post_request_model([FieldsExtension()]),
        extensions=[FieldsExtension()],
    )

    with TestClient(test_app.app) as client:
        get_search = client.get(
            "/search",
            params={"fields": "properties.datetime"},
        )
        post_search = client.post(
            "/search",
            json={
                "collections": ["test"],
                "fields": {
                    "include": ["properties.datetime"],
                    "exclude": [],
                },
            },
        )

    # With or without validation, /search endpoints will always return 200
    # because we have the `FieldsExtension` enabled, so the endpoint
    # will avoid the model validation (by returning JSONResponse)
    assert get_search.status_code == 200, get_search.text
    assert post_search.status_code == 200, post_search.text

    # Without FieldsExtension
    test_app = app.StacApi(
        settings=ApiSettings(enable_response_models=validate),
        client=BadCoreClient(),
        search_get_request_model=create_get_request_model([]),
        search_post_request_model=create_post_request_model([]),
        extensions=[],
    )

    with TestClient(test_app.app) as client:
        get_search = client.get(
            "/search",
            params={"fields": "properties.datetime"},
        )
        post_search = client.post(
            "/search",
            json={
                "collections": ["test"],
                "fields": {
                    "include": ["properties.datetime"],
                    "exclude": [],
                },
            },
        )

    if validate:
        # NOTE: the `fields` options will be ignored by fastAPI because it's
        # not part of the request model, so the client should not by-pass the validation
        assert get_search.status_code == 500, (
            get_search.json()["code"] == "ResponseValidationError"
        )
        assert post_search.status_code == 500, (
            post_search.json()["code"] == "ResponseValidationError"
        )
    else:
        assert get_search.status_code == 200, get_search.text
        assert post_search.status_code == 200, post_search.text


def test_request_model(AsyncTestCoreClient):
    """Test if request models are passed correctly."""

    @attr.s
    class CollectionsRequest(APIRequest):
        user: Annotated[str, Query(...)] = attr.ib()

    @attr.s
    class CollectionRequest(APIRequest):
        collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()
        user: Annotated[str, Query(...)] = attr.ib()

    @attr.s
    class ItemsRequest(APIRequest):
        collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()
        user: Annotated[str, Query(...)] = attr.ib()

    @attr.s
    class ItemRequest(APIRequest):
        collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()
        item_id: Annotated[str, Path(description="Item ID")] = attr.ib()
        user: Annotated[str, Query(...)] = attr.ib()

    test_app = app.StacApi(
        settings=ApiSettings(),
        client=AsyncTestCoreClient(),
        collections_get_request_model=CollectionsRequest,
        collection_get_request_model=CollectionRequest,
        items_get_request_model=ItemsRequest,
        item_get_request_model=ItemRequest,
        extensions=[],
    )

    with TestClient(test_app.app) as client:
        resp = client.get("/collections")
        assert resp.status_code == 400

        resp = client.get("/collections", params={"user": "Luke"})
        assert resp.status_code == 200

        resp = client.get("/collections/test_collection")
        assert resp.status_code == 400

        resp = client.get("/collections/test_collection", params={"user": "Leia"})
        assert resp.status_code == 200

        resp = client.get("/collections/test_collection/items")
        assert resp.status_code == 400

        resp = client.get(
            "/collections/test_collection/items", params={"user": "Obi-Wan"}
        )
        assert resp.status_code == 200

        resp = client.get("/collections/test_collection/items/test_item")
        assert resp.status_code == 400

        resp = client.get(
            "/collections/test_collection/items/test_item", params={"user": "Chewbacca"}
        )
        assert resp.status_code == 200


def test_client_datetime_input_params():
    """Test all endpoints. Verify input models."""

    class FakeClient(BaseCoreClient):
        def post_search(self, search_request: BaseSearchPostRequest, **kwargs):
            assert isinstance(search_request.datetime, str)
            return search_request.datetime

        def get_search(
            self,
            collections: Optional[List[str]] = None,
            ids: Optional[List[str]] = None,
            bbox: Optional[List[NumType]] = None,
            intersects: Optional[str] = None,
            datetime: Optional[str] = None,
            limit: Optional[int] = 10,
            **kwargs,
        ):
            assert isinstance(datetime, str)
            return datetime

        def get_item(self, item_id: str, collection_id: str, **kwargs) -> stac.Item:
            raise NotImplementedError

        def all_collections(self, **kwargs) -> stac.Collections:
            raise NotImplementedError

        def get_collection(self, collection_id: str, **kwargs) -> stac.Collection:
            raise NotImplementedError

        def item_collection(
            self,
            collection_id: str,
            bbox: Optional[List[Union[float, int]]] = None,
            datetime: Optional[str] = None,
            limit: int = 10,
            token: str = None,
            **kwargs,
        ) -> stac.ItemCollection:
            raise NotImplementedError

    test_app = app.StacApi(
        settings=ApiSettings(enable_response_models=False),
        client=FakeClient(),
    )

    with TestClient(test_app.app) as client:
        get_search = client.get(
            "/search",
            params={
                "collections": ["test"],
                "datetime": "2020-01-01T00:00:00.00001Z",
            },
        )
        get_search_zero = client.get(
            "/search",
            params={
                "collections": ["test"],
                "datetime": "2020-01-01T00:00:00.0000Z",
            },
        )
        post_search = client.post(
            "/search",
            json={
                "collections": ["test"],
                "datetime": "2020-01-01T00:00:00.00001Z",
            },
        )
        post_search_zero = client.post(
            "/search",
            json={
                "collections": ["test"],
                "datetime": "2020-01-01T00:00:00.0000Z",
            },
        )

    assert get_search.status_code == 200, get_search.text
    assert get_search.json() == "2020-01-01T00:00:00.00001Z"
    assert get_search_zero.status_code == 200, get_search_zero.text
    assert get_search_zero.json() == "2020-01-01T00:00:00.0000Z"

    assert post_search.status_code == 200, post_search.text
    assert post_search.json() == "2020-01-01T00:00:00.00001Z"
    assert post_search_zero.status_code == 200, post_search_zero.text
    assert post_search_zero.json() == "2020-01-01T00:00:00.0000Z"
