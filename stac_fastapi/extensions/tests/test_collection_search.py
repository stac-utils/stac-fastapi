import json
from urllib.parse import quote_plus

from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_request_model
from stac_fastapi.extensions.core import CollectionSearchExtension
from stac_fastapi.extensions.core.collection_search.collection_search import (
    ConformanceClasses,
)
from stac_fastapi.extensions.core.collection_search.request import (
    CollectionSearchExtensionGetRequest,
    FreeTextGetRequest,
)
from stac_fastapi.extensions.core.fields.request import FieldsExtensionGetRequest
from stac_fastapi.extensions.core.filter.request import FilterExtensionGetRequest
from stac_fastapi.extensions.core.query.request import QueryExtensionGetRequest
from stac_fastapi.extensions.core.sort.request import SortExtensionGetRequest
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


def test_collection_search_extension_default():
    """Test /collections endpoint with collection-search ext."""
    api = StacApi(
        settings=ApiSettings(),
        client=DummyCoreClient(),
        extensions=[CollectionSearchExtension()],
        collections_get_request_model=CollectionSearchExtensionGetRequest,
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
        assert [
            "2020-06-13T13:00:00+00:00",
            "2020-06-13T14:00:00+00:00",
        ] == response_dict["datetime"]
        assert 100 == response_dict["limit"]


def test_collection_search_extension_models():
    """Test /collections endpoint with collection-search ext with additional models."""
    collections_get_request_model = create_request_model(
        model_name="SearchGetRequest",
        base_model=CollectionSearchExtensionGetRequest,
        mixins=[
            FreeTextGetRequest,
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
                conformance_classes=[
                    ConformanceClasses.COLLECTIONSEARCH,
                    ConformanceClasses.BASIS,
                    ConformanceClasses.FREETEXT,
                    ConformanceClasses.FILTER,
                    ConformanceClasses.QUERY,
                    ConformanceClasses.SORT,
                    ConformanceClasses.FIELDS,
                ]
            )
        ],
        collections_get_request_model=collections_get_request_model,
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
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#free-text"
            in response_dict["conformsTo"]
        )
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#filter"
            in response_dict["conformsTo"]
        )
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#query"
            in response_dict["conformsTo"]
        )
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#sort"
            in response_dict["conformsTo"]
        )
        assert (
            "https://api.stacspec.org/v1.0.0-rc.1/collection-search#fields"
            in response_dict["conformsTo"]
        )

        response = client.get("/collections")
        assert response.is_success, response.json()
        response_dict = response.json()
        assert "bbox" in response_dict
        assert "datetime" in response_dict
        assert "limit" in response_dict
        assert "q" in response_dict
        assert "filter" in response_dict
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
        assert [
            "2020-06-13T13:00:00+00:00",
            "2020-06-13T14:00:00+00:00",
        ] == response_dict["datetime"]
        assert 100 == response_dict["limit"]
        assert "EO,Earth Observation" == response_dict["q"]
        assert "id='item_id' AND collection='collection_id'" == response_dict["filter"]
        assert "filter_crs" in response_dict
        assert "cql2-text" in response_dict["filter_lang"]
        assert "query" in response_dict
        assert ["-gsd", "-datetime"] == response_dict["sortby"]
        assert ["properties.datetime"] == response_dict["fields"]
