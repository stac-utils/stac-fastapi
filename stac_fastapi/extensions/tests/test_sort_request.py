import pytest
from pydantic import ValidationError
from stac_pydantic.api.extensions.sort import SortExtension as PostSortModel

from stac_fastapi.extensions.core.sort.request import (
    SortExtensionGetRequest,
    SortExtensionPostRequest,
)

## GET Request Tests


def test_sort_extension_get_request_parsing():
    """Test that the GET request properly converts comma-separated strings to a list."""
    # Single field
    req = SortExtensionGetRequest(sortby="-gsd")
    assert req.sortby == ["-gsd"]

    # Multiple fields
    req = SortExtensionGetRequest(sortby="-gsd,+datetime,id")
    assert req.sortby == ["-gsd", "+datetime", "id"]


def test_sort_extension_get_request_empty():
    """Test GET request with null or empty values."""
    req_none = SortExtensionGetRequest(sortby=None)
    assert req_none.sortby is None


## POST Request Tests


def test_sort_extension_post_request_defaults():
    """Test POST request model default values."""
    req = SortExtensionPostRequest()
    assert req.sortby is None


def test_sort_extension_post_request_valid_data():
    """Test POST request with valid structured sort objects."""
    data = {
        "sortby": [
            {"field": "properties.created", "direction": "asc"},
            {"field": "id", "direction": "desc"},
        ]
    }
    req = SortExtensionPostRequest(**data)

    assert len(req.sortby) == 2
    assert isinstance(req.sortby[0], PostSortModel)
    assert req.sortby[0].field == "properties.created"
    assert req.sortby[0].direction == "asc"


def test_sort_extension_post_request_invalid_direction():
    """
    Test that pydantic validation catches invalid directions.
    The PostSortModel restricts direction to 'asc' or 'desc'.
    """
    invalid_data = {"sortby": [{"field": "properties.created", "direction": "sideways"}]}
    with pytest.raises(ValidationError):
        SortExtensionPostRequest(**invalid_data)
