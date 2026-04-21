"""Tests for the Sort extension."""

import pytest
from fastapi import FastAPI

# Adjust the import path based on your project structure
from stac_fastapi.extensions.core.sort import (
    SortConformanceClasses,
    SortExtension,
)
from stac_fastapi.extensions.core.sort.request import (
    SortExtensionGetRequest,
    SortExtensionPostRequest,
)


def test_sort_conformance_classes():
    """Test that the enum values match the official STAC API spec URIs."""
    assert (
        SortConformanceClasses.SEARCH
        == "https://api.stacspec.org/v1.0.0/item-search#sort"
    )
    assert (
        SortConformanceClasses.ITEMS
        == "https://api.stacspec.org/v1.0.0/ogcapi-features#sort"
    )
    assert (
        SortConformanceClasses.COLLECTIONS
        == "https://api.stacspec.org/v1.0.0-rc.1/collection-search#sort"
    )


def test_sort_extension_defaults():
    """Test the default instantiation of the SortExtension."""
    ext = SortExtension()

    assert ext.schema_href is None
    assert ext.conformance_classes == [SortConformanceClasses.SEARCH]

    # Ensure the GET/POST request models are properly assigned
    assert ext.GET == SortExtensionGetRequest
    assert ext.POST == SortExtensionPostRequest


def test_sort_extension_customization():
    """Test instantiating SortExtension with custom arguments."""
    custom_conformance = [
        SortConformanceClasses.SEARCH,
        SortConformanceClasses.ITEMS,
        SortConformanceClasses.COLLECTIONS,
    ]
    custom_schema = "https://example.com/sort-schema.json"

    ext = SortExtension(
        conformance_classes=custom_conformance,
        schema_href=custom_schema,
    )

    assert ext.conformance_classes == custom_conformance
    assert ext.schema_href == custom_schema


def test_sort_extension_register():
    """Test the register method with a dummy FastAPI app."""
    ext = SortExtension()
    app = FastAPI()

    try:
        ext.register(app)
    except Exception as e:
        pytest.fail(f"SortExtension.register() raised an exception: {e}")
