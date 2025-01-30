from typing import Iterator

import pytest
from fastapi import APIRouter
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_get_request_model, create_post_request_model
from stac_fastapi.extensions.core import FilterExtension
from stac_fastapi.extensions.core.filter import (
    CollectionSearchFilterExtension,
    ItemCollectionFilterExtension,
    SearchFilterExtension,
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
        _ = kwargs.pop("request", None)
        return kwargs

    def post_search(self, *args, **kwargs):
        return args[0].model_dump()

    def item_collection(self, *args, **kwargs):
        raise NotImplementedError


@pytest.fixture(autouse=True)
def client() -> Iterator[TestClient]:
    settings = ApiSettings()
    extensions = [FilterExtension()]
    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=extensions,
        search_get_request_model=create_get_request_model(extensions),
        search_post_request_model=create_post_request_model(extensions),
    )
    with TestClient(api.app) as client:
        yield client


@pytest.fixture(autouse=True)
def client_multit_ext() -> Iterator[TestClient]:
    settings = ApiSettings()
    extensions = [
        SearchFilterExtension(),
        ItemCollectionFilterExtension(),
        # Technically `CollectionSearchFilterExtension`
        # shouldn't be registered to the application but to the collection-search class
        CollectionSearchFilterExtension(),
    ]

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=extensions,
        search_get_request_model=create_get_request_model([SearchFilterExtension()]),
        search_post_request_model=create_post_request_model([SearchFilterExtension()]),
    )
    with TestClient(api.app) as client:
        yield client


@pytest.mark.parametrize("client_name", ["client", "client_multit_ext"])
def test_filter_endpoints_conformances(client_name, request):
    """Make sure conformances classes are set."""
    client = request.getfixturevalue(client_name)

    response = client.get("/conformance")
    assert response.is_success, response.json()
    response_dict = response.json()
    conf = response_dict["conformsTo"]
    assert (
        "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter" in conf
    )
    assert "https://api.stacspec.org/v1.0.0-rc.2/item-search#filter" in conf
    assert client.get("/queryables").is_success
    assert client.get("/collections/collection_id/queryables").is_success


def test_filter_conformances_collection_search(client_multit_ext):
    """Make sure conformances classes are set."""
    response = client_multit_ext.get("/conformance")
    assert response.is_success, response.json()
    response_dict = response.json()
    conf = response_dict["conformsTo"]
    assert (
        "http://www.opengis.net/spec/ogcapi-features-3/1.0/conf/features-filter" in conf
    )
    assert "https://api.stacspec.org/v1.0.0-rc.2/item-search#filter" in conf
    assert "https://api.stacspec.org/v1.0.0-rc.1/collection-search#filter" in conf


@pytest.mark.parametrize("client_name", ["client", "client_multit_ext"])
def test_search_filter_post_filter_lang_default(client_name, request):
    """Test search POST endpoint with filter ext."""
    client = request.getfixturevalue(client_name)

    response = client.post(
        "/search",
        json={
            "collections": ["test"],
            "filter": {"op": "=", "args": [{"property": "test_property"}, "test-value"]},
        },
    )
    assert response.is_success, response.json()
    response_dict = response.json()
    assert response_dict["filter_expr"]
    assert response_dict["filter_lang"] == "cql2-json"


@pytest.mark.parametrize("client_name", ["client", "client_multit_ext"])
def test_search_filter_post_filter_lang_non_default(client_name, request):
    """Test search POST endpoint with filter ext."""
    client = request.getfixturevalue(client_name)

    filter_lang_value = "cql-json"
    response = client.post(
        "/search",
        json={
            "collections": ["test"],
            "filter": {"eq": [{"property": "test_property"}, "test-value"]},
            "filter-lang": filter_lang_value,
        },
    )
    assert response.is_success, response.json()
    response_dict = response.json()
    assert response_dict["filter_expr"]
    assert response_dict["filter_lang"] == filter_lang_value


@pytest.mark.parametrize("client_name", ["client", "client_multit_ext"])
def test_search_filter_get(client_name, request):
    """Test search GET endpoint with filter ext."""
    client = request.getfixturevalue(client_name)

    response = client.get(
        "/search",
        params={
            "filter": "id='item_id' AND collection='collection_id'",
        },
    )
    assert response.is_success, response.json()
    response_dict = response.json()
    assert not response_dict["collections"]
    assert response_dict["filter_expr"] == "id='item_id' AND collection='collection_id'"
    assert not response_dict["filter_crs"]
    assert response_dict["filter_lang"] == "cql2-text"

    response = client.get(
        "/search",
        params={
            "filter": {"op": "=", "args": [{"property": "id"}, "test-item"]},
            "filter-lang": "cql2-json",
        },
    )
    assert response.is_success, response.json()
    response_dict = response.json()
    assert not response_dict["collections"]
    assert (
        response_dict["filter_expr"]
        == "{'op': '=', 'args': [{'property': 'id'}, 'test-item']}"
    )
    assert not response_dict["filter_crs"]
    assert response_dict["filter_lang"] == "cql2-json"

    response = client.get(
        "/search",
        params={
            "collections": "collection1,collection2",
        },
    )
    assert response.is_success, response.json()
    response_dict = response.json()
    assert response_dict["collections"] == ["collection1", "collection2"]


@pytest.mark.parametrize("prefix", ["", "/a_prefix"])
def test_multi_ext_prefix(prefix):
    settings = ApiSettings()
    extensions = [
        SearchFilterExtension(),
        ItemCollectionFilterExtension(),
        # Technically `CollectionSearchFilterExtension`
        # shouldn't be registered to the application but to the collection-search class
        CollectionSearchFilterExtension(),
    ]

    api = StacApi(
        settings=settings,
        router=APIRouter(prefix=prefix),
        client=DummyCoreClient(),
        extensions=extensions,
        search_get_request_model=create_get_request_model([SearchFilterExtension()]),
        search_post_request_model=create_post_request_model([SearchFilterExtension()]),
    )
    with TestClient(api.app, base_url="http://stac.io") as client:
        queryables = client.get(f"{prefix}/queryables")
        assert queryables.status_code == 200, queryables.json()
        assert queryables.headers["content-type"] == "application/schema+json"
