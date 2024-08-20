import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient
from pydantic import ValidationError

from stac_fastapi.types.search import BaseSearchGetRequest, BaseSearchPostRequest


@pytest.mark.parametrize("value", [0, -1])
def test_limit_ge(value):
    with pytest.raises(ValidationError):
        BaseSearchPostRequest(limit=value)


@pytest.mark.parametrize("value", [1, 10_000])
def test_limit(value):
    search = BaseSearchPostRequest(limit=value)
    assert search.limit == value


@pytest.mark.parametrize("value", [10_001, 100_000, 1_000_000])
def test_limit_le(value):
    search = BaseSearchPostRequest(limit=value)
    assert search.limit == 10_000


def test_limit_get_request():
    """test GET model."""

    app = FastAPI()

    @app.get("/test")
    def route(model=Depends(BaseSearchGetRequest)):
        return model

    with TestClient(app) as client:
        resp = client.get(
            "/test",
            params={
                "limit": 10,
            },
        )
        assert resp.status_code == 200
        response_dict = resp.json()
        assert response_dict["limit"] == 10

        resp = client.get(
            "/test",
            params={
                "limit": 100_000,
            },
        )
        assert resp.status_code == 200
        response_dict = resp.json()
        assert response_dict["limit"] == 10_000
