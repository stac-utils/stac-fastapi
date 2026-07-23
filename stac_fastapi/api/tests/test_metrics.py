import pytest
from fastapi import APIRouter
from fastapi.testclient import TestClient

from stac_fastapi.api import app
from stac_fastapi.api.metrics import (
    OPERATIONS,
    register_operations,
    resolve_operation,
)
from stac_fastapi.types.config import ApiSettings


@pytest.mark.parametrize(
    ("method", "route", "router_prefix", "expected"),
    [
        ("GET", "/search", "", "search"),
        ("GET", "/collections/{collection_id}/items/{item_id}", "", "get_item"),
        ("POST", "/collections/{collection_id}/bulk_items", "", "bulk"),
        ("GET", "/aggregations", "", "aggregations"),
        ("GET", "/_mgmt/health", "", "unknown"),
        ("GET", "/catalogs/root", "", "catalog"),
        ("GET", "/api/search", "/api", "search"),
        ("GET", "none", "", "unknown"),
    ],
)
def test_resolve_operation(method, route, router_prefix, expected):
    assert resolve_operation(method, route, router_prefix) == expected


def test_register_operations():
    key = ("GET", "/custom/viewer")
    previous = OPERATIONS.pop(key, None)
    try:
        register_operations({key: "viewer"})
        assert resolve_operation("GET", "/custom/viewer") == "viewer"
    finally:
        if previous is None:
            OPERATIONS.pop(key, None)
        else:
            OPERATIONS[key] = previous


def test_metrics_operation_labels(TestCoreClient):
    test_app = app.StacApi(
        settings=ApiSettings(),
        client=TestCoreClient(),
        add_metrics=True,
    )

    with TestClient(test_app.app) as client:
        assert client.get("/search", params={"limit": 1}).status_code == 200
        assert client.get("/collections/c/items/item-a").status_code == 200
        assert client.get("/collections/c/items/item-b").status_code == 200
        body = client.get("/_mgmt/metrics").text

    assert 'operation="search"' in body
    assert 'operation="get_item"' in body
    assert "item-a" not in body
    assert "item-b" not in body


def test_metrics_router_prefix(TestCoreClient):
    test_app = app.StacApi(
        settings=ApiSettings(),
        client=TestCoreClient(),
        router=APIRouter(prefix="/api"),
        add_metrics=True,
    )

    with TestClient(test_app.app) as client:
        assert client.get("/_mgmt/metrics").status_code == 404
        resp = client.get("/api/_mgmt/metrics")
        assert resp.status_code == 200
        assert "http_requests_total" in resp.text


def test_metrics_disabled_by_default(TestCoreClient):
    test_app = app.StacApi(
        settings=ApiSettings(),
        client=TestCoreClient(),
    )

    with TestClient(test_app.app) as client:
        assert client.get("/_mgmt/metrics").status_code == 404


def test_instrument_app_requires_metrics_extra(monkeypatch):
    from fastapi import FastAPI

    import stac_fastapi.api.metrics as metrics

    monkeypatch.setattr(metrics, "Instrumentator", None)

    with pytest.raises(ImportError, match=r"stac-fastapi-api\[metrics\]"):
        metrics.instrument_app(FastAPI(), endpoint="/_mgmt/metrics")
