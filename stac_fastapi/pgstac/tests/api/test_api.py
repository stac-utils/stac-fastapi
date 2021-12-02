from datetime import datetime, timedelta

import pytest

STAC_CORE_ROUTES = [
    "GET /",
    "GET /collections",
    "GET /collections/{collection_id}",
    "GET /collections/{collection_id}/items",
    "GET /collections/{collection_id}/items/{item_id}",
    "GET /conformance",
    "GET /search",
    "POST /search",
]

STAC_TRANSACTION_ROUTES = [
    "DELETE /collections/{collection_id}",
    "DELETE /collections/{collection_id}/items/{item_id}",
    "POST /collections",
    "POST /collections/{collection_id}/items",
    "PUT /collections",
    "PUT /collections/{collection_id}/items",
]


@pytest.mark.asyncio
async def test_post_search_content_type(app_client):
    params = {"limit": 1}
    resp = await app_client.post("search", json=params)
    assert resp.headers["content-type"] == "application/geo+json"


@pytest.mark.asyncio
async def test_get_search_content_type(app_client):
    resp = await app_client.get("search")
    assert resp.headers["content-type"] == "application/geo+json"


@pytest.mark.asyncio
async def test_api_headers(app_client):
    resp = await app_client.get("/api")
    assert (
        resp.headers["content-type"] == "application/vnd.oai.openapi+json;version=3.0"
    )
    assert resp.status_code == 200


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
async def test_app_query_extension_limit_1(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"limit": 1}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


@pytest.mark.asyncio
async def test_app_query_extension_limit_eq0(app_client):
    params = {"limit": 0}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 400


@pytest.mark.asyncio
async def test_app_query_extension_limit_lt0(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"limit": -1}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 400


@pytest.mark.asyncio
async def test_app_query_extension_limit_gt10000(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"limit": 10001}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 400


@pytest.mark.asyncio
async def test_app_query_extension_gt(load_test_data, app_client, load_test_collection):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"query": {"proj:epsg": {"gt": item["properties"]["proj:epsg"]}}}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 0


@pytest.mark.asyncio
async def test_app_query_extension_gte(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"query": {"proj:epsg": {"gte": item["properties"]["proj:epsg"]}}}
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


@pytest.mark.asyncio
async def test_search_invalid_date(load_test_data, app_client, load_test_collection):
    coll = load_test_collection
    first_item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=first_item)
    assert resp.status_code == 200

    params = {
        "datetime": "2020-XX-01/2020-10-30",
        "collections": [coll.id],
    }

    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 400


@pytest.mark.asyncio
async def test_bbox_3d(load_test_data, app_client, load_test_collection):
    coll = load_test_collection
    first_item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=first_item)
    assert resp.status_code == 200

    australia_bbox = [106.343365, -47.199523, 0.1, 168.218365, -19.437288, 0.1]
    params = {
        "bbox": australia_bbox,
        "collections": [coll.id],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200

    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


@pytest.mark.asyncio
async def test_app_search_response(load_test_data, app_client, load_test_collection):
    coll = load_test_collection
    params = {
        "collections": [coll.id],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()

    assert resp_json.get("type") == "FeatureCollection"
    # stac_version and stac_extensions were removed in v1.0.0-beta.3
    assert resp_json.get("stac_version") is None
    assert resp_json.get("stac_extensions") is None


@pytest.mark.asyncio
async def test_search_point_intersects(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    point = [150.04, -33.14]
    intersects = {"type": "Point", "coordinates": point}

    params = {
        "intersects": intersects,
        "collections": [item["collection"]],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


@pytest.mark.asyncio
async def test_search_line_string_intersects(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    line = [[150.04, -33.14], [150.22, -33.89]]
    intersects = {"type": "LineString", "coordinates": line}

    params = {
        "intersects": intersects,
        "collections": [item["collection"]],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
