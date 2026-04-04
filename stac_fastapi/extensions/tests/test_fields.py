"""Tests for the Fields extension."""

import pytest
from fastapi import FastAPI

from stac_fastapi.extensions.core.fields import (
    FieldsConformanceClasses,
    FieldsExtension,
)
from stac_fastapi.extensions.core.fields.request import (
    FieldsExtensionGetRequest,
    FieldsExtensionPostRequest,
)


def test_fields_conformance_classes():
    """Test that the enum values match the official STAC API spec URIs."""
    assert (
        FieldsConformanceClasses.SEARCH
        == "https://api.stacspec.org/v1.0.0/item-search#fields"
    )
    assert (
        FieldsConformanceClasses.ITEMS
        == "https://api.stacspec.org/v1.0.0/ogcapi-features#fields"
    )
    assert (
        FieldsConformanceClasses.COLLECTIONS
        == "https://api.stacspec.org/v1.0.0-rc.1/collection-search#fields"
    )


def test_fields_extension_defaults():
    """Test the default instantiation of the FieldsExtension."""
    ext = FieldsExtension()

    assert ext.schema_href is None
    assert ext.conformance_classes == [FieldsConformanceClasses.SEARCH]

    assert ext.GET == FieldsExtensionGetRequest
    assert ext.POST == FieldsExtensionPostRequest


def test_fields_extension_customization():
    """Test instantiating FieldsExtension with custom arguments."""
    custom_conformance = [
        FieldsConformanceClasses.SEARCH,
        FieldsConformanceClasses.ITEMS,
    ]
    custom_schema = "https://example.com/fields-schema.json"

    ext = FieldsExtension(
        conformance_classes=custom_conformance,
        schema_href=custom_schema,
    )

    assert ext.conformance_classes == custom_conformance
    assert ext.schema_href == custom_schema


def test_fields_extension_register():
    """Test the register method with a dummy FastAPI app."""
    ext = FieldsExtension()
    app = FastAPI()

    try:
        ext.register(app)
    except Exception as e:
        pytest.fail(f"FieldsExtension.register() raised an exception: {e}")
