import json
from urllib.parse import quote_plus

import attr
import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_request_model
from stac_fastapi.extensions.core import (
    AggregationExtension,
    CollectionSearchExtension,
    CollectionSearchFilterExtension,
    CollectionSearchPostExtension,
    FieldsExtension,
    FreeTextAdvancedExtension,
    FreeTextExtension,
    QueryExtension,
    SortExtension,
)
from stac_fastapi.extensions.core.collection_search import (
    CollectionSearchConformanceClasses,
)
from stac_fastapi.extensions.core.collection_search.client import (
    BaseCollectionSearchClient,
)
from stac_fastapi.extensions.core.collection_search.request import (
    BaseCollectionSearchGetRequest,
    BaseCollectionSearchPostRequest,
)
from stac_fastapi.extensions.core.fields import FieldsConformanceClasses
from stac_fastapi.extensions.core.fields.request import (
    FieldsExtensionGetRequest,
    FieldsExtensionPostRequest,
)
from stac_fastapi.extensions.core.filter import FilterConformanceClasses
from stac_fastapi.extensions.core.filter.request import (
    FilterExtensionGetRequest,
    FilterExtensionPostRequest,
)
from stac_fastapi.extensions.core.free_text import FreeTextConformanceClasses
from stac_fastapi.extensions.core.free_text.request import (
    FreeTextExtensionGetRequest,
    FreeTextExtensionPostRequest,
)
from stac_fastapi.extensions.core.query import QueryConformanceClasses
from stac_fastapi.extensions.core.query.request import (
    QueryExtensionGetRequest,
    QueryExtensionPostRequest,
)
from stac_fastapi.extensions.core.sort import SortConformanceClasses
from stac_fastapi.extensions.core.sort.request import (
    SortExtensionGetRequest,
    SortExtensionPostRequest,
)
from stac_fastapi.types import stac
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient


class DummyCoreClient(BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        _ = kwargs.pop("request", None)
        return kwargs

    def get_collection(self, *args, **kwargs):
        raise NotImplementedError

    def get_item(self, *args, **kwargs):
        raise NotImplementedError

    def get_search(self, *args, **kwargs):
        raise NotImplementedError

    def post_search(self, *args, **kwargs):
        return args[0].model_dump()

    def item_collection(self, *args, **kwargs):
        raise NotImplementedError


@attr.s
class DummyPostClient(BaseCollectionSearchClient):
    def post_all_collections(
        self, search_request: BaseCollectionSearchPostRequest, **kwargs
    ) -> stac.ItemCollection:
        """fake method."""
        return search_request.model_dump()


def test_collection_search_extension_default():
    """Test GET - /collections endpoint with collection-search ext."""
    api = StacApi(
        settings=ApiSettings(),
        client=DummyCoreClient(),
        extensions=[CollectionSearchExtension()],
        collections_get_request_model=BaseCollectionSearchGetRequest,
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search"
            in response_dict["conformsTo"]
        )
        assert (
            "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"
            in response_dict["conformsTo"]
        )

        response = client.get("/collections")
        assert response.is_success, response.json()
        response_dict = response.json()
        assert "bbox" in response_dict
        assert "datetime" in response_dict
        assert "limit" in response_dict

        response = client.get(
            "/collections",
            params={
                "datetime": "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z",
                "bbox": "-175.05,-85.05,175.05,85.05",
                "limit": 100,
            },
        )
        assert response.is_success, response.json()
        response_dict = response.json()
        assert [-175.05, -85.05, 175.05, 85.05] == response_dict["bbox"]
        assert "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z" == response_dict["datetime"]
        assert 100 == response_dict["limit"]


def test_collection_search_extension_models():
    """Test GET - /collections endpoint with collection-search ext
    with additional models.
    """
    collections_get_request_model = create_request_model(
        model_name="SearchGetRequest",
        base_model=BaseCollectionSearchGetRequest,
        mixins=[
            FreeTextExtensionGetRequest,
            FilterExtensionGetRequest,
            QueryExtensionGetRequest,
            SortExtensionGetRequest,
            FieldsExtensionGetRequest,
        ],
        request_type="GET",
    )

    api = StacApi(
        settings=ApiSettings(),
        client=DummyCoreClient(),
        extensions=[
            CollectionSearchExtension(
                GET=collections_get_request_model,
                conformance_classes=[
                    CollectionSearchConformanceClasses.COLLECTIONSEARCH,
                    CollectionSearchConformanceClasses.BASIS,
                    FieldsConformanceClasses.COLLECTIONS,
                    FilterConformanceClasses.COLLECTIONS,
                    FreeTextConformanceClasses.COLLECTIONS,
                    QueryConformanceClasses.COLLECTIONS,
                    SortConformanceClasses.COLLECTIONS,
                ],
            )
        ],
        collections_get_request_model=collections_get_request_model,
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        conforms = response_dict["conformsTo"]
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search" in conforms
        assert (
            "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"
            in conforms
        )
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text" in conforms
        )
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#filter" in conforms
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#query" in conforms
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#sort" in conforms
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#fields" in conforms

        response = client.get("/collections")
        assert response.is_success, response.json()
        response_dict = response.json()
        assert "bbox" in response_dict
        assert "datetime" in response_dict
        assert "limit" in response_dict
        assert "q" in response_dict
        assert "filter_expr" in response_dict
        assert "query" in response_dict
        assert "sortby" in response_dict
        assert "fields" in response_dict

        response = client.get(
            "/collections",
            params={
                "datetime": "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z",
                "bbox": "-175.05,-85.05,175.05,85.05",
                "limit": 100,
                "q": "EO,Earth Observation",
                "filter": "id='item_id' AND collection='collection_id'",
                "query": quote_plus(
                    json.dumps({"eo:cloud_cover": {"gte": 95}}),
                ),
                "sortby": "-gsd,-datetime",
                "fields": "properties.datetime",
            },
        )
        assert response.is_success, response.json()
        response_dict = response.json()
        assert [-175.05, -85.05, 175.05, 85.05] == response_dict["bbox"]
        assert "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z" == response_dict["datetime"]
        assert 100 == response_dict["limit"]
        assert ["EO", "Earth Observation"] == response_dict["q"]
        assert (
            "id='item_id' AND collection='collection_id'" == response_dict["filter_expr"]
        )
        assert "filter_crs" in response_dict
        assert "cql2-text" in response_dict["filter_lang"]
        assert "query" in response_dict
        assert ["-gsd", "-datetime"] == response_dict["sortby"]
        assert ["properties.datetime"] == response_dict["fields"]


def test_collection_search_extension_post_default():
    """Test POST - /collections endpoint with collection-search ext."""
    settings = ApiSettings()
    collection_search_ext = CollectionSearchPostExtension(
        client=DummyPostClient(),
        settings=settings,
    )

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=[collection_search_ext],
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search"
            in response_dict["conformsTo"]
        )
        assert (
            "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"
            in response_dict["conformsTo"]
        )

        response = client.post("/collections", json={})
        assert response.is_success, response.json()
        response_dict = response.json()
        assert "bbox" in response_dict
        assert "datetime" in response_dict
        assert "limit" in response_dict
        assert response_dict["limit"] == 10

        response = client.post(
            "/collections",
            json={
                "datetime": "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z",
                "bbox": [-175.05, -85.05, 175.05, 85.05],
                "limit": 100_000,
            },
        )
        assert response.is_success, response.json()
        response_dict = response.json()
        assert [-175.05, -85.05, 175.05, 85.05] == response_dict["bbox"]
        assert "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z" == response_dict["datetime"]
        assert 10_000 == response_dict["limit"]


def test_collection_search_extension_post_models():
    """Test POST - /collections endpoint with collection-search ext
    with additional models.
    """
    post_request_model = create_request_model(
        model_name="SearchPostRequest",
        base_model=BaseCollectionSearchPostRequest,
        mixins=[
            FreeTextExtensionPostRequest,
            FilterExtensionPostRequest,
            QueryExtensionPostRequest,
            SortExtensionPostRequest,
            FieldsExtensionPostRequest,
        ],
        request_type="POST",
    )

    get_request_model = create_request_model(
        model_name="SearchGetRequest",
        base_model=BaseCollectionSearchGetRequest,
        mixins=[
            FreeTextExtensionGetRequest,
            FilterExtensionGetRequest,
            QueryExtensionGetRequest,
            SortExtensionGetRequest,
            FieldsExtensionGetRequest,
        ],
        request_type="GET",
    )

    settings = ApiSettings()
    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=[
            CollectionSearchPostExtension(
                client=DummyPostClient(),
                settings=settings,
                GET=get_request_model,
                POST=post_request_model,
                conformance_classes=[
                    CollectionSearchConformanceClasses.COLLECTIONSEARCH,
                    CollectionSearchConformanceClasses.BASIS,
                    FieldsConformanceClasses.COLLECTIONS,
                    FilterConformanceClasses.COLLECTIONS,
                    FreeTextConformanceClasses.COLLECTIONS,
                    QueryConformanceClasses.COLLECTIONS,
                    SortConformanceClasses.COLLECTIONS,
                ],
            )
        ],
        collections_get_request_model=get_request_model,
    )

    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        conforms = response_dict["conformsTo"]
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search" in conforms
        assert (
            "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"
            in conforms
        )
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text" in conforms
        )
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#filter" in conforms
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#query" in conforms
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#sort" in conforms
        assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#fields" in conforms

        response = client.post("/collections", json={})
        assert response.is_success, response.json()
        response_dict = response.json()
        assert "bbox" in response_dict
        assert "datetime" in response_dict
        assert "limit" in response_dict
        assert "q" in response_dict
        assert "filter_expr" in response_dict
        assert "query" in response_dict
        assert "sortby" in response_dict
        assert "fields" in response_dict

        response = client.post(
            "/collections",
            json={
                "datetime": "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z",
                "bbox": [-175.05, -85.05, 175.05, 85.05],
                "limit": 100_000,
                "q": ["EO", "Earth Observation"],
                "filter": {
                    "op": "and",
                    "args": [
                        {"op": "=", "args": [{"property": "id"}, "item_id"]},
                        {
                            "op": "=",
                            "args": [{"property": "collection"}, "collection_id"],
                        },
                    ],
                },
                "query": {"eo:cloud_cover": {"gte": 95}},
                "sortby": [
                    {
                        "field": "properties.gsd",
                        "direction": "desc",
                    },
                    {
                        "field": "properties.datetime",
                        "direction": "asc",
                    },
                ],
            },
        )
        assert response.is_success, response.json()
        response_dict = response.json()
        assert [-175.05, -85.05, 175.05, 85.05] == response_dict["bbox"]
        assert "2020-06-13T13:00:00Z/2020-06-13T14:00:00Z" == response_dict["datetime"]
        assert 10_000 == response_dict["limit"]
        assert ["EO", "Earth Observation"] == response_dict["q"]
        assert response_dict["filter_expr"]
        assert "filter_crs" in response_dict
        assert "cql2-json" in response_dict["filter_lang"]
        assert response_dict["query"]
        assert response_dict["sortby"]
        assert response_dict["fields"]


@pytest.mark.parametrize(
    "extensions",
    [
        # with FreeTextExtension
        [
            FieldsExtension(conformance_classes=[FieldsConformanceClasses.COLLECTIONS]),
            CollectionSearchFilterExtension(),
            FreeTextExtension(
                conformance_classes=[FreeTextConformanceClasses.COLLECTIONS]
            ),
            QueryExtension(conformance_classes=[QueryConformanceClasses.COLLECTIONS]),
            SortExtension(conformance_classes=[SortConformanceClasses.COLLECTIONS]),
        ],
        # with FreeTextAdvancedExtension
        [
            FieldsExtension(conformance_classes=[FieldsConformanceClasses.COLLECTIONS]),
            CollectionSearchFilterExtension(),
            FreeTextAdvancedExtension(
                conformance_classes=[FreeTextConformanceClasses.COLLECTIONS]
            ),
            QueryExtension(conformance_classes=[QueryConformanceClasses.COLLECTIONS]),
            SortExtension(conformance_classes=[SortConformanceClasses.COLLECTIONS]),
        ],
    ],
)
def test_from_extensions_methods(extensions):
    """
    Make sure `from_extensions` create the correct
    models and adds desired conformances classes.
    """
    ext = CollectionSearchExtension.from_extensions(
        extensions,
    )
    collection_search = ext.GET()
    assert collection_search.__class__.__name__ == "CollectionsGetRequest"
    assert hasattr(collection_search, "bbox")
    assert hasattr(collection_search, "datetime")
    assert hasattr(collection_search, "limit")
    assert hasattr(collection_search, "fields")
    assert hasattr(collection_search, "q")
    assert hasattr(collection_search, "sortby")
    assert hasattr(collection_search, "filter_expr")
    for conf in [
        CollectionSearchConformanceClasses.COLLECTIONSEARCH,
        CollectionSearchConformanceClasses.BASIS,
        FieldsConformanceClasses.COLLECTIONS,
        FilterConformanceClasses.COLLECTIONS,
        FilterConformanceClasses.FILTER,
        FilterConformanceClasses.BASIC_CQL2,
        FilterConformanceClasses.CQL2_JSON,
        FilterConformanceClasses.CQL2_TEXT,
        FreeTextConformanceClasses.COLLECTIONS,
        QueryConformanceClasses.COLLECTIONS,
        SortConformanceClasses.COLLECTIONS,
    ]:
        assert conf in ext.conformance_classes

    ext = CollectionSearchPostExtension.from_extensions(
        extensions,
        client=DummyPostClient(),
        settings=ApiSettings(),
    )
    collection_search = ext.POST()
    assert collection_search.__class__.__name__ == "CollectionsPostRequest"
    assert hasattr(collection_search, "bbox")
    assert hasattr(collection_search, "datetime")
    assert hasattr(collection_search, "limit")
    assert hasattr(collection_search, "fields")
    assert hasattr(collection_search, "q")
    assert hasattr(collection_search, "sortby")
    assert hasattr(collection_search, "filter_expr")
    for conf in [
        CollectionSearchConformanceClasses.COLLECTIONSEARCH,
        CollectionSearchConformanceClasses.BASIS,
        FieldsConformanceClasses.COLLECTIONS,
        FilterConformanceClasses.COLLECTIONS,
        FilterConformanceClasses.FILTER,
        FilterConformanceClasses.BASIC_CQL2,
        FilterConformanceClasses.CQL2_JSON,
        FilterConformanceClasses.CQL2_TEXT,
        FreeTextConformanceClasses.COLLECTIONS,
        QueryConformanceClasses.COLLECTIONS,
        SortConformanceClasses.COLLECTIONS,
    ]:
        assert conf in ext.conformance_classes


def test_from_extensions_methods_invalid():
    """Should also work with unknown extensions."""
    extensions = [
        AggregationExtension(),
    ]
    ext = CollectionSearchExtension.from_extensions(
        extensions,
    )

    collection_search = ext.GET()
    assert collection_search.__class__.__name__ == "CollectionsGetRequest"
    assert hasattr(collection_search, "bbox")
    assert hasattr(collection_search, "datetime")
    assert hasattr(collection_search, "limit")
    assert hasattr(collection_search, "aggregations")
    for conf in [
        CollectionSearchConformanceClasses.COLLECTIONSEARCH,
        CollectionSearchConformanceClasses.BASIS,
    ]:
        assert conf in ext.conformance_classes

    ext = CollectionSearchPostExtension.from_extensions(
        extensions,
        client=DummyPostClient(),
        settings=ApiSettings(),
    )
    collection_search = ext.POST()
    assert collection_search.__class__.__name__ == "CollectionsPostRequest"
    assert hasattr(collection_search, "bbox")
    assert hasattr(collection_search, "datetime")
    assert hasattr(collection_search, "limit")
    assert hasattr(collection_search, "aggregations")
    for conf in [
        CollectionSearchConformanceClasses.COLLECTIONSEARCH,
        CollectionSearchConformanceClasses.BASIS,
    ]:
        assert conf in ext.conformance_classes
