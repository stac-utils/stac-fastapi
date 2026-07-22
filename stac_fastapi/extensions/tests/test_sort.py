"""Tests for the Sort extension."""

from typing import Any

import pytest
from fastapi import FastAPI, Request
from starlette.testclient import TestClient

from stac_fastapi.extensions.sort import (
    BaseSortablesClient,
    CollectionSearchSortExtension,
    ItemCollectionSortExtension,
    SearchSortExtension,
    SortConformanceClasses,
    SortExtension,
)
from stac_fastapi.extensions.sort.request import (
    SortExtensionGetRequest,
    SortExtensionPostRequest,
)


class DummySortablesClient(BaseSortablesClient):
    """Dummy client for testing sortables endpoints."""

    def get_sortables(
        self, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get sortables for item search."""
        return {
            "$id": "https://example.com/sortables",
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "title": "Sortables",
            "properties": {},
            "additionalProperties": True,
        }

    def get_collection_sortables(
        self, collection_id: str, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get sortables for a specific collection."""
        return {
            "$id": f"https://example.com/collections/{collection_id}/sortables",
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "title": "Sortables",
            "properties": {},
            "additionalProperties": True,
        }

    def get_collections_sortables(
        self, request: Request | None = None, **kwargs: Any
    ) -> dict[str, Any]:
        """Get sortables for collection search."""
        return {
            "$id": "https://example.com/collections-sortables",
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "title": "Sortables",
            "properties": {},
            "additionalProperties": True,
        }


def test_sort_conformance_classes():
    """Test that the enum values match the official STAC API v1.1.0 spec URIs."""
    assert (
        SortConformanceClasses.ITEM_SEARCH_SORT
        == "https://api.stacspec.org/v1.1.0/item-search#sort"
    )
    assert (
        SortConformanceClasses.ITEM_SEARCH_SORTABLES
        == "https://api.stacspec.org/v1.1.0/item-search#sortables"
    )
    assert (
        SortConformanceClasses.FEATURES_SORT
        == "https://api.stacspec.org/v1.1.0/ogcapi-features#sort"
    )
    assert (
        SortConformanceClasses.FEATURES_SORTABLES
        == "http://www.opengis.net/spec/ogcapi-features-5/1.0/conf/sortables"
    )
    assert (
        SortConformanceClasses.COLLECTION_SEARCH_SORT
        == "https://api.stacspec.org/v1.1.0/collection-search#sort"
    )
    assert (
        SortConformanceClasses.COLLECTION_SEARCH_SORTABLES
        == "https://api.stacspec.org/v1.1.0/collection-search#sortables"
    )

    with pytest.warns(DeprecationWarning):
        assert (
            SortConformanceClasses.COLLECTIONS
            == "https://api.stacspec.org/v1.1.0/collection-search#sort"
        )

    with pytest.warns(DeprecationWarning):
        assert (
            SortConformanceClasses["COLLECTIONS"]
            == "https://api.stacspec.org/v1.1.0/collection-search#sort"
        )

    with pytest.warns(DeprecationWarning):
        assert (
            SortConformanceClasses.ITEMS
            == "https://api.stacspec.org/v1.1.0/ogcapi-features#sort"
        )

    with pytest.warns(DeprecationWarning):
        assert (
            SortConformanceClasses["ITEMS"]
            == "https://api.stacspec.org/v1.1.0/ogcapi-features#sort"
        )

    with pytest.warns(DeprecationWarning):
        assert (
            SortConformanceClasses.SEARCH
            == "https://api.stacspec.org/v1.1.0/item-search#sort"
        )

    with pytest.warns(DeprecationWarning):
        assert (
            SortConformanceClasses["SEARCH"]
            == "https://api.stacspec.org/v1.1.0/item-search#sort"
        )


def test_sort_extension_defaults():
    """Test the default instantiation of the SortExtension."""
    ext = SortExtension()

    assert ext.GET == SortExtensionGetRequest
    assert ext.POST == SortExtensionPostRequest
    assert SortConformanceClasses.ITEM_SEARCH_SORT in ext.conformance_classes
    # Sortables conformance classes are removed when no client is provided
    assert SortConformanceClasses.ITEM_SEARCH_SORTABLES not in ext.conformance_classes
    assert SortConformanceClasses.FEATURES_SORT in ext.conformance_classes
    assert SortConformanceClasses.FEATURES_SORTABLES not in ext.conformance_classes
    assert SortConformanceClasses.COLLECTION_SEARCH_SORT in ext.conformance_classes
    assert (
        SortConformanceClasses.COLLECTION_SEARCH_SORTABLES not in ext.conformance_classes
    )


def test_search_sort_extension():
    """Test SearchSortExtension for item search endpoints."""
    ext = SearchSortExtension()

    # Sortables conformance class is removed when no client is provided
    assert ext.conformance_classes == [SortConformanceClasses.ITEM_SEARCH_SORT]


def test_item_collection_sort_extension():
    """Test ItemCollectionSortExtension for collection item endpoints."""
    ext = ItemCollectionSortExtension()

    # Sortables conformance class is removed when no client is provided
    assert ext.conformance_classes == [SortConformanceClasses.FEATURES_SORT]


def test_collection_search_sort_extension():
    """Test CollectionSearchSortExtension for collection search endpoints."""
    ext = CollectionSearchSortExtension()

    # Sortables conformance class is removed when no client is provided
    assert ext.conformance_classes == [SortConformanceClasses.COLLECTION_SEARCH_SORT]


def test_sort_extension_register():
    """Test the register method with a dummy FastAPI app."""
    ext = SortExtension()
    app = FastAPI()

    try:
        ext.register(app)
    except Exception as e:
        pytest.fail(f"SortExtension.register() raised an exception: {e}")


def test_sort_extension_has_router():
    """Test that SortExtension has a router attribute."""
    ext = SortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None


def test_search_sort_extension_has_router():
    """Test that SearchSortExtension has a router attribute."""
    ext = SearchSortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None


def test_item_collection_sort_extension_has_router():
    """Test that ItemCollectionSortExtension has a router attribute."""
    ext = ItemCollectionSortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None


def test_collection_search_sort_extension_has_router():
    """Test that CollectionSearchSortExtension has a router attribute."""
    ext = CollectionSearchSortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None


def test_sort_extension_v1_1_0_compliance():
    """Test that SortExtension conforms to v1.1.0 spec with granular conformance."""
    ext = SortExtension(client=DummySortablesClient())

    conformance_classes = ext.conformance_classes

    assert len(conformance_classes) == 6

    assert SortConformanceClasses.ITEM_SEARCH_SORT in conformance_classes
    assert SortConformanceClasses.ITEM_SEARCH_SORTABLES in conformance_classes

    assert SortConformanceClasses.FEATURES_SORT in conformance_classes
    assert SortConformanceClasses.FEATURES_SORTABLES in conformance_classes

    assert SortConformanceClasses.COLLECTION_SEARCH_SORT in conformance_classes
    assert SortConformanceClasses.COLLECTION_SEARCH_SORTABLES in conformance_classes


def test_search_sort_extension_v1_1_0_compliance():
    """Test SearchSortExtension conforms to v1.1.0 spec for item search."""
    ext = SearchSortExtension(client=DummySortablesClient())

    conformance_classes = ext.conformance_classes

    assert len(conformance_classes) == 2
    assert SortConformanceClasses.ITEM_SEARCH_SORT in conformance_classes
    assert SortConformanceClasses.ITEM_SEARCH_SORTABLES in conformance_classes

    assert SortConformanceClasses.FEATURES_SORT not in conformance_classes
    assert SortConformanceClasses.COLLECTION_SEARCH_SORT not in conformance_classes


def test_item_collection_sort_extension_v1_1_0_compliance():
    """Test ItemCollectionSortExtension conforms to v1.1.0 spec for OGC API Features."""
    ext = ItemCollectionSortExtension(client=DummySortablesClient())

    conformance_classes = ext.conformance_classes

    assert len(conformance_classes) == 2
    assert SortConformanceClasses.FEATURES_SORT in conformance_classes
    assert SortConformanceClasses.FEATURES_SORTABLES in conformance_classes

    assert SortConformanceClasses.ITEM_SEARCH_SORT not in conformance_classes
    assert SortConformanceClasses.COLLECTION_SEARCH_SORT not in conformance_classes


def test_collection_search_sort_extension_v1_1_0_compliance():
    """Test CollectionSearchSortExtension conforms to v1.1.0 spec for collections."""
    ext = CollectionSearchSortExtension(client=DummySortablesClient())

    conformance_classes = ext.conformance_classes

    assert len(conformance_classes) == 2
    assert SortConformanceClasses.COLLECTION_SEARCH_SORT in conformance_classes
    assert SortConformanceClasses.COLLECTION_SEARCH_SORTABLES in conformance_classes

    assert SortConformanceClasses.ITEM_SEARCH_SORT not in conformance_classes
    assert SortConformanceClasses.FEATURES_SORT not in conformance_classes


def test_sort_extension_request_models():
    """Test that SortExtension has correct GET and POST request models."""
    ext = SortExtension()

    assert ext.GET == SortExtensionGetRequest
    assert ext.POST == SortExtensionPostRequest


def test_search_sort_extension_request_models():
    """Test that SearchSortExtension inherits correct request models."""
    ext = SearchSortExtension()

    assert ext.GET == SortExtensionGetRequest
    assert ext.POST == SortExtensionPostRequest


def test_item_collection_sort_extension_request_models():
    """Test that ItemCollectionSortExtension inherits correct request models."""
    ext = ItemCollectionSortExtension()

    assert ext.GET == SortExtensionGetRequest
    assert ext.POST == SortExtensionPostRequest


def test_collection_search_sort_extension_request_models():
    """Test that CollectionSearchSortExtension inherits correct request models."""
    ext = CollectionSearchSortExtension()

    assert ext.GET == SortExtensionGetRequest
    assert ext.POST == SortExtensionPostRequest


def test_sort_extension_with_client():
    """Test that SortExtension accepts a client parameter."""
    client = DummySortablesClient()
    ext = SortExtension(client=client)
    assert ext.client is client


def test_search_sort_extension_with_client():
    """Test that SearchSortExtension accepts a client parameter."""
    client = DummySortablesClient()
    ext = SearchSortExtension(client=client)
    assert ext.client is client


def test_item_collection_sort_extension_with_client():
    """Test that ItemCollectionSortExtension accepts a client parameter."""
    client = DummySortablesClient()
    ext = ItemCollectionSortExtension(client=client)
    assert ext.client is client


def test_collection_search_sort_extension_with_client():
    """Test that CollectionSearchSortExtension accepts a client parameter."""
    client = DummySortablesClient()
    ext = CollectionSearchSortExtension(client=client)
    assert ext.client is client


def test_sort_extension_graceful_degradation_without_client():
    """Test that SortExtension gracefully handles missing client."""
    app = FastAPI()
    app.state.router_prefix = ""
    ext = SortExtension(client=None)
    ext.register(app)

    assert ext.client is None
    # Verify sortables conformance classes are removed when no client
    assert SortConformanceClasses.ITEM_SEARCH_SORTABLES not in ext.conformance_classes
    assert SortConformanceClasses.FEATURES_SORTABLES not in ext.conformance_classes
    assert (
        SortConformanceClasses.COLLECTION_SEARCH_SORTABLES not in ext.conformance_classes
    )
    # Verify sort conformance classes are still present
    assert SortConformanceClasses.ITEM_SEARCH_SORT in ext.conformance_classes
    assert SortConformanceClasses.FEATURES_SORT in ext.conformance_classes
    assert SortConformanceClasses.COLLECTION_SEARCH_SORT in ext.conformance_classes


def test_sort_extension_router_attribute():
    """Test that SortExtension has a router attribute that can be configured."""
    ext = SortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None
    assert ext.router.prefix == ""


def test_search_sort_extension_router_attribute():
    """Test that SearchSortExtension has a router attribute that can be configured."""
    ext = SearchSortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None
    assert ext.router.prefix == ""


def test_item_collection_sort_extension_router_attribute():
    """Test that ItemCollectionSortExtension has a router attribute."""
    ext = ItemCollectionSortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None
    assert ext.router.prefix == ""


def test_collection_search_sort_extension_router_attribute():
    """Test that CollectionSearchSortExtension has a router attribute."""
    ext = CollectionSearchSortExtension()
    assert hasattr(ext, "router")
    assert ext.router is not None
    assert ext.router.prefix == ""


def test_base_sort_extension_mounts_all_routes():
    """Test that the base extension mounts all three sortables routes."""
    app = FastAPI()
    app.state.router_prefix = ""
    ext = SortExtension(client=DummySortablesClient())
    ext.register(app)

    with TestClient(app) as client:
        assert client.get("/sortables").status_code == 200
        assert client.get("/collections/my-collection/sortables").status_code == 200
        assert client.get("/collections-sortables").status_code == 200


def test_search_sort_extension_routes():
    """Test that SearchSortExtension ONLY mounts /sortables."""
    app = FastAPI()
    app.state.router_prefix = ""
    ext = SearchSortExtension(client=DummySortablesClient())
    ext.register(app)

    with TestClient(app) as client:
        assert client.get("/sortables").status_code == 200
        assert client.get("/collections/my-collection/sortables").status_code == 404
        assert client.get("/collections-sortables").status_code == 404


def test_item_collection_sort_extension_routes():
    """Test that ItemCollectionSortExtension ONLY mounts collection specific routes."""
    app = FastAPI()
    app.state.router_prefix = ""
    ext = ItemCollectionSortExtension(client=DummySortablesClient())
    ext.register(app)

    with TestClient(app) as client:
        assert client.get("/collections/my-collection/sortables").status_code == 200
        assert client.get("/sortables").status_code == 404
        assert client.get("/collections-sortables").status_code == 404


def test_collection_search_sort_extension_routes():
    """Test that CollectionSearchSortExtension ONLY mounts /collections-sortables."""
    app = FastAPI()
    app.state.router_prefix = ""
    ext = CollectionSearchSortExtension(client=DummySortablesClient())
    ext.register(app)

    with TestClient(app) as client:
        assert client.get("/collections-sortables").status_code == 200
        assert client.get("/sortables").status_code == 404
        assert client.get("/collections/my-collection/sortables").status_code == 404


def test_sort_extension_graceful_degradation_routes():
    """Test that without a client, NO routes are mounted and they return 404."""
    app = FastAPI()
    app.state.router_prefix = ""
    ext = SortExtension(client=None)
    ext.register(app)

    with TestClient(app) as client:
        assert client.get("/sortables").status_code == 404
        assert client.get("/collections/my-collection/sortables").status_code == 404
        assert client.get("/collections-sortables").status_code == 404
