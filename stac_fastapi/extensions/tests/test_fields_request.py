from stac_fastapi.extensions.core.fields.request import (
    FieldsExtensionGetRequest,
    FieldsExtensionPostRequest,
    PostFieldsExtension,
)


def test_post_fields_extension_defaults():
    """Test the default instantiation."""
    ext = PostFieldsExtension()
    assert ext.include == set()
    assert ext.exclude == set()


def test_get_field_dict_empty():
    """Test field dict generation with empty/None inputs."""
    assert PostFieldsExtension._get_field_dict(None) == {}
    assert PostFieldsExtension._get_field_dict(set()) == {}


def test_get_field_dict_simple_fields():
    """Test field dict generation with top-level fields."""
    fields = {"id", "type", "geometry"}
    result = PostFieldsExtension._get_field_dict(fields)

    assert result == {"id": ..., "type": ..., "geometry": ...}


def test_get_field_dict_nested_fields():
    """Test field dict generation with dot-notation nested fields."""
    fields = {"properties.datetime", "properties.cloud_cover", "assets.visual"}
    result = PostFieldsExtension._get_field_dict(fields)

    assert result == {"properties": {"datetime", "cloud_cover"}, "assets": {"visual"}}


def test_get_field_dict_mixed_fields():
    """Test field dict generation with a mix of top-level and nested fields."""
    fields = {"id", "properties", "properties.datetime"}

    result = PostFieldsExtension._get_field_dict(fields)

    assert "id" in result
    assert result["id"] is ...
    assert "properties" in result


def test_fields_extension_get_request():
    """Test that the GET request properly uses the converter
    for comma-separated strings."""
    req = FieldsExtensionGetRequest(fields="id,type,properties.datetime")
    assert req.fields == ["id", "type", "properties.datetime"]

    req_none = FieldsExtensionGetRequest(fields=None)
    assert req_none.fields is None


def test_fields_extension_post_request():
    """Test POST request model defaults."""
    req = FieldsExtensionPostRequest()
    assert isinstance(req.fields, PostFieldsExtension)
    assert req.fields.include == set()
    assert req.fields.exclude == set()
