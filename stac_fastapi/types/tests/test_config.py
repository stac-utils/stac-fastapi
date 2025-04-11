"""test config classes."""

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
