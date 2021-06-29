from datetime import datetime, timedelta

import pytest

STAC_CORE_ROUTES = [
    "GET /",
    "GET /collections",
    "GET /collections/{collectionId}",
    "GET /collections/{collectionId}/items",
    "GET /collections/{collectionId}/items/{itemId}",
    "GET /conformance",
    "GET /search",
    "POST /search",
]

STAC_TRANSACTION_ROUTES = [
    "DELETE /collections/{collectionId}",
    "DELETE /collections/{collectionId}/items/{itemId}",
    "POST /collections",
    "POST /collections/{collectionId}/items",
    "PUT /collections",
    "PUT /collections/{collectionId}/items",
]


@pytest.mark.asyncio
async def test_core_router(api_client):
    core_routes = set(STAC_CORE_ROUTES)
    api_routes = set(
        [f"{list(route.methods)[0]} {route.path}" for route in api_client.app.routes]
    )
    assert not core_routes - api_routes


@pytest.mark.asyncio
async def test_transactions_router(api_client):
    transaction_routes = set(STAC_TRANSACTION_ROUTES)
    api_routes = set(
        [f"{list(route.methods)[0]} {route.path}" for route in api_client.app.routes]
    )
    assert not transaction_routes - api_routes


@pytest.mark.asyncio
async def test_app_transaction_extension(
    app_client, load_test_data, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_app_query_extension(load_test_data, app_client, load_test_collection):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"query": {"proj:epsg": {"eq": item["properties"]["proj:epsg"]}}}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


@pytest.mark.asyncio
async def test_app_sort_extension(load_test_data, app_client, load_test_collection):
    coll = load_test_collection
    first_item = load_test_data("test_item.json")
    item_date = datetime.strptime(
        first_item["properties"]["datetime"], "%Y-%m-%dT%H:%M:%SZ"
    )
    resp = await app_client.post(f"/collections/{coll.id}/items", json=first_item)
    assert resp.status_code == 200

    second_item = load_test_data("test_item.json")
    second_item["id"] = "another-item"
    another_item_date = item_date - timedelta(days=1)
    second_item["properties"]["datetime"] = another_item_date.strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    resp = await app_client.post(f"/collections/{coll.id}/items", json=second_item)
    assert resp.status_code == 200

    params = {
        "collections": [coll.id],
        "sortby": [{"field": "datetime", "direction": "desc"}],
    }
    print(params)
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == first_item["id"]
    assert resp_json["features"][1]["id"] == second_item["id"]

    params = {
        "collections": [coll.id],
        "sortby": [{"field": "datetime", "direction": "asc"}],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][1]["id"] == first_item["id"]
    assert resp_json["features"][0]["id"] == second_item["id"]
