import json

import pytest
from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import ValidationError

from stac_fastapi.api.models import create_get_request_model, create_post_request_model
from stac_fastapi.extensions.core import FieldsExtension, FilterExtension, SortExtension
from stac_fastapi.types.search import BaseSearchGetRequest, BaseSearchPostRequest


def test_create_get_request_model():
    request_model = create_get_request_model(
        extensions=[FilterExtension(), FieldsExtension()],
        base_model=BaseSearchGetRequest,
    )

    model = request_model(
        collections="test1,test2",
        ids="test1,test2",
        bbox="0,0,1,1",
        intersects=json.dumps(
            {
                "type": "Polygon",
                "coordinates": [[[0, 0], [0, 1], [1, 1], [1, 0], [0, 0]]],
            }
        ),
        datetime="2020-01-01T00:00:00Z",
        limit=10,
        filter="test==test",
        filter_crs="epsg:4326",
        filter_lang="cql2-text",
    )

    assert model.collections == ["test1", "test2"]
    assert model.filter_crs == "epsg:4326"

    with pytest.raises(HTTPException):
        request_model(datetime="yo")

    app = FastAPI()

    @app.get("/test")
    def route(model=Depends(request_model)):
        return model

    with TestClient(app) as client:
        resp = client.get(
            "/test",
            params={
                "collections": "test1,test2",
                "filter-crs": "epsg:4326",
                "filter-lang": "cql2-text",
            },
        )
        assert resp.status_code == 200
        response_dict = resp.json()
        assert response_dict["collections"] == ["test1", "test2"]
        assert response_dict["filter_crs"] == "epsg:4326"
        assert response_dict["filter_lang"] == "cql2-text"


@pytest.mark.parametrize(
    "filter,passes",
    [(None, True), ({"test": "test"}, True), ([], False)],
)
def test_create_post_request_model(filter, passes):
    request_model = create_post_request_model(
        extensions=[FilterExtension(), FieldsExtension()],
        base_model=BaseSearchPostRequest,
    )

    if not passes:
        with pytest.raises(ValidationError):
            model = request_model(filter=filter)
    else:
        model = request_model(
            collections=["test1", "test2"],
            ids=["test1", "test2"],
            bbox=[0, 0, 1, 1],
            datetime="2020-01-01T00:00:00Z",
            limit=10,
            filter=filter,
            **{"filter-crs": "epsg:4326", "filter-lang": "cql2-json"},
        )

        assert model.collections == ["test1", "test2"]
        assert model.filter_crs == "epsg:4326"
        assert model.filter == filter


@pytest.mark.parametrize(
    "sortby,passes",
    [
        (None, True),
        (
            [
                {"field": "test", "direction": "asc"},
                {"field": "test2", "direction": "desc"},
            ],
            True,
        ),
        ({"field": "test", "direction": "desc"}, False),
        ("test", False),
    ],
)
def test_create_post_request_model_nested_fields(sortby, passes):
    request_model = create_post_request_model(
        extensions=[SortExtension()],
        base_model=BaseSearchPostRequest,
    )

    if not passes:
        with pytest.raises(ValidationError):
            model = request_model(sortby=sortby)
    else:
        model = request_model(
            collections=["test1", "test2"],
            ids=["test1", "test2"],
            bbox=[0, 0, 1, 1],
            datetime="2020-01-01T00:00:00Z",
            limit=10,
            sortby=sortby,
        )

        assert model.collections == ["test1", "test2"]
        if model.sortby is None:
            assert sortby is None
        else:
            assert model.model_dump(mode="json")["sortby"] == sortby
