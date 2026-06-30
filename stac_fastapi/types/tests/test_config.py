"""test config classes."""

import logging

import pytest
from pydantic import ValidationError

from stac_fastapi.types.config import ApiSettings


def test_incompatible_options():
    """test incompatible output model options."""
    settings = ApiSettings(
        enable_response_models=True,
        enable_direct_response=False,
    )
    assert settings.enable_response_models
    assert not settings.enable_direct_response

    settings = ApiSettings(
        enable_response_models=False,
        enable_direct_response=True,
    )
    assert not settings.enable_response_models
    assert settings.enable_direct_response

    with pytest.raises(ValidationError):
        ApiSettings(
            enable_response_models=True,
            enable_direct_response=True,
        )


def test_default_values_warning(caplog):
    """test that a warning is logged when using default values."""
    with caplog.at_level(logging.WARNING):
        ApiSettings()

    assert "Using default values for" in caplog.text
    assert "stac_fastapi_title" in caplog.text
    assert "stac_fastapi_description" in caplog.text
    assert "stac_fastapi_landing_id" in caplog.text
    assert "stac_fastapi_version" in caplog.text


def test_custom_values_no_warning(caplog):
    """test that no warning is logged when using custom values."""
    with caplog.at_level(logging.WARNING):
        ApiSettings(
            stac_fastapi_title="My API",
            stac_fastapi_description="My API Description",
            stac_fastapi_landing_id="my-api",
            stac_fastapi_version="1.0.0",
        )

    assert "Using default values for" not in caplog.text


def test_partial_custom_values_warning(caplog):
    """test that a warning is logged only for remaining default values."""
    with caplog.at_level(logging.WARNING):
        ApiSettings(
            stac_fastapi_title="My API",
            stac_fastapi_description="My API Description",
        )

    assert "Using default values for" in caplog.text
    assert "stac_fastapi_landing_id" in caplog.text
    assert "stac_fastapi_version" in caplog.text
    assert "stac_fastapi_title" not in caplog.text
    assert "stac_fastapi_description" not in caplog.text
