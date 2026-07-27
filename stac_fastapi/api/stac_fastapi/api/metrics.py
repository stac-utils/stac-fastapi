"""Prometheus metrics with low-cardinality STAC operation labels."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from fastapi import FastAPI

try:
    from prometheus_client import REGISTRY, Counter, Histogram
    from prometheus_fastapi_instrumentator import Instrumentator
    from prometheus_fastapi_instrumentator.metrics import Info

    REQUESTS: Any = Counter(
        "http_requests_total",
        "Total HTTP requests by STAC operation.",
        labelnames=("operation", "method", "status"),
        registry=REGISTRY,
    )
    LATENCY: Any = Histogram(
        "http_request_duration_seconds",
        "HTTP request latency by STAC operation.",
        labelnames=("operation", "method"),
        buckets=(0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10, float("inf")),
        registry=REGISTRY,
    )
except ImportError:  # pragma: no cover
    REGISTRY = None  # type: ignore
    Counter = None  # type: ignore
    Histogram = None  # type: ignore
    Instrumentator = None  # type: ignore
    Info = None  # type: ignore
    REQUESTS = None
    LATENCY = None

OPERATIONS: dict[tuple[str, str], str] = {
    ("GET", "/"): "landing",
    ("GET", "/conformance"): "conformance",
    ("GET", "/collections"): "list_collections",
    ("GET", "/collections/{collection_id}"): "get_collection",
    ("GET", "/collections/{collection_id}/items"): "list_items",
    ("GET", "/collections/{collection_id}/items/{item_id}"): "get_item",
    ("GET", "/search"): "search",
    ("POST", "/search"): "search",
    ("POST", "/collections"): "create_collection",
    ("PUT", "/collections/{collection_id}"): "edit_collection",
    ("PATCH", "/collections/{collection_id}"): "edit_collection",
    ("DELETE", "/collections/{collection_id}"): "delete_collection",
    ("POST", "/collections/{collection_id}/items"): "create_item",
    ("PUT", "/collections/{collection_id}/items/{item_id}"): "edit_item",
    ("PATCH", "/collections/{collection_id}/items/{item_id}"): "edit_item",
    ("DELETE", "/collections/{collection_id}/items/{item_id}"): "delete_item",
    ("POST", "/collections/{collection_id}/bulk_items"): "bulk",
    ("GET", "/queryables"): "queryables",
    ("GET", "/collections/{collection_id}/queryables"): "queryables",
    ("GET", "/aggregations"): "aggregations",
    ("POST", "/aggregations"): "aggregations",
    ("GET", "/collections/{collection_id}/aggregations"): "aggregations",
    ("POST", "/collections/{collection_id}/aggregations"): "aggregations",
    ("GET", "/aggregate"): "aggregate",
    ("POST", "/aggregate"): "aggregate",
    ("GET", "/collections/{collection_id}/aggregate"): "aggregate",
    ("POST", "/collections/{collection_id}/aggregate"): "aggregate",
}


def register_operations(mapping: dict[tuple[str, str], str]) -> None:
    """Register or override operation labels for route templates."""
    OPERATIONS.update(mapping)


def resolve_operation(method: str, route: str | None, router_prefix: str = "") -> str:
    """Map a request method and route template to a STAC operation label."""
    if not route or route == "none":
        return "unknown"

    path = route
    prefix = (router_prefix or "").rstrip("/")
    if prefix and path.startswith(prefix):
        path = path[len(prefix) :] or "/"

    operation = OPERATIONS.get((method.upper(), path))
    if operation:
        return operation

    if path.startswith("/catalogs"):
        return "catalog"
    if "bulk" in path:
        return "bulk"

    return "unknown"


def record_stac_metrics(info: Info) -> None:
    """Record request count and latency using STAC operation labels."""
    route = info.request.scope.get("route")
    route_path = getattr(route, "path", None)
    router_prefix = getattr(info.request.app.state, "router_prefix", "") or ""
    operation = resolve_operation(info.method, route_path, router_prefix)

    REQUESTS.labels(operation, info.method, info.modified_status).inc()
    LATENCY.labels(operation, info.method).observe(info.modified_duration)


def instrument_app(app: FastAPI, endpoint: str) -> None:
    """Instrument a FastAPI app and expose Prometheus metrics.

    Must be called during app construction (e.g. from ``StacApi``), before any
    requests. Adding middleware after the app has started is not supported.

    Raises:
        ImportError: If ``stac-fastapi-api[metrics]`` is not installed.
    """
    if Instrumentator is None:
        raise ImportError(
            "Prometheus metrics require the optional dependency "
            "`stac-fastapi-api[metrics]`. Install with: "
            "pip install 'stac-fastapi-api[metrics]'"
        )

    (
        Instrumentator(
            should_group_status_codes=True,
            should_ignore_untemplated=True,
            excluded_handlers=[".*/_mgmt/.*"],
        )
        .add(record_stac_metrics)
        .instrument(app)
        .expose(app, endpoint=endpoint, include_in_schema=False)
    )
