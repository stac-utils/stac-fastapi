import importlib
import os

import pytest
from pydantic import BaseModel

from stac_fastapi.types import response_model


@pytest.fixture
def cleanup():
    old_environ = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(old_environ)


@pytest.mark.parametrize(
    "validate, response_type",
    [
        ("True", BaseModel),
        ("False", dict),
    ],
)
def test_response_model(validate, response_type, cleanup):

    os.environ["VALIDATE_RESPONSE"] = str(validate)
    importlib.reload(response_model)

    landing_page = response_model.LandingPage(
        id="test",
        description="test",
        links=[
            {"href": "test", "rel": "root"},
            {"href": "test", "rel": "self"},
            {"href": "test", "rel": "service-desc"},
        ],
    )

    assert isinstance(landing_page, response_type)
