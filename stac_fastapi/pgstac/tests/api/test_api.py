from datetime import datetime, timedelta
from typing import Any, Dict, List
from urllib.parse import quote_plus

import orjson
import pytest
from pystac import Collection, Extent, Item, SpatialExtent, TemporalExtent

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
    "PUT /collections/{collection_id}/items/{item_id}",
]

GLOBAL_BBOX = [-180.0, -90.0, 180.0, 90.0]
GLOBAL_GEOMETRY = {
    "type": "Polygon",
    "coordinates": (
        (
            (180.0, -90.0),
            (180.0, 90.0),
            (-180.0, 90.0),
            (-180.0, -90.0),
            (180.0, -90.0),
        ),
    ),
}
DEFAULT_EXTENT = Extent(
    SpatialExtent(GLOBAL_BBOX),
    TemporalExtent([[datetime.now(), None]]),
)


async def test_post_search_content_type(app_client):
    params = {"limit": 1}
    resp = await app_client.post("search", json=params)
    assert resp.headers["content-type"] == "application/geo+json"


async def test_get_search_content_type(app_client):
    resp = await app_client.get("search")
    assert resp.headers["content-type"] == "application/geo+json"


async def test_get_queryables_content_type(app_client, load_test_collection):
    resp = await app_client.get("queryables")
    assert resp.headers["content-type"] == "application/schema+json"

    coll = load_test_collection
    resp = await app_client.get(f"collections/{coll.id}/queryables")
    assert resp.headers["content-type"] == "application/schema+json"


async def test_get_features_content_type(app_client, load_test_collection):
    coll = load_test_collection
    resp = await app_client.get(f"collections/{coll.id}/items")
    assert resp.headers["content-type"] == "application/geo+json"


async def test_get_features_self_link(app_client, load_test_collection):
    # https://github.com/stac-utils/stac-fastapi/issues/483
    resp = await app_client.get(f"collections/{load_test_collection.id}/items")
    assert resp.status_code == 200
    resp_json = resp.json()
    self_link = next(
        (link for link in resp_json["links"] if link["rel"] == "self"), None
    )
    assert self_link is not None
    assert self_link["href"].endswith("/items")


async def test_get_feature_content_type(
    app_client, load_test_collection, load_test_item
):
    resp = await app_client.get(
        f"collections/{load_test_collection.id}/items/{load_test_item.id}"
    )
    assert resp.headers["content-type"] == "application/geo+json"


async def test_api_headers(app_client):
    resp = await app_client.get("/api")
    assert (
        resp.headers["content-type"] == "application/vnd.oai.openapi+json;version=3.0"
    )
    assert resp.status_code == 200


async def test_core_router(api_client, app):
    core_routes = set()
    for core_route in STAC_CORE_ROUTES:
        method, path = core_route.split(" ")
        core_routes.add("{} {}".format(method, app.state.router_prefix + path))

    api_routes = set(
        [f"{list(route.methods)[0]} {route.path}" for route in api_client.app.routes]
    )
    assert not core_routes - api_routes


async def test_landing_page_stac_extensions(app_client):
    resp = await app_client.get("/")
    assert resp.status_code == 200
    resp_json = resp.json()
    assert not resp_json["stac_extensions"]


async def test_transactions_router(api_client, app):
    transaction_routes = set()
    for transaction_route in STAC_TRANSACTION_ROUTES:
        method, path = transaction_route.split(" ")
        transaction_routes.add("{} {}".format(method, app.state.router_prefix + path))

    api_routes = set(
        [f"{list(route.methods)[0]} {route.path}" for route in api_client.app.routes]
    )
    assert not transaction_routes - api_routes


async def test_app_transaction_extension(
    app_client, load_test_data, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200


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

    params["query"] = quote_plus(orjson.dumps(params["query"]))
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


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


async def test_app_query_extension_limit_eq0(app_client):
    params = {"limit": 0}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 400


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


async def test_app_query_extension_limit_gt10000(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    params = {"limit": 10001}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200


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


async def test_search_point_intersects(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 200

    new_coordinates = list()
    for coordinate in item["geometry"]["coordinates"][0]:
        new_coordinates.append([coordinate[0] * -1, coordinate[1] * -1])
    item["id"] = "test-item-other-hemispheres"
    item["geometry"]["coordinates"] = [new_coordinates]
    item["bbox"] = list(value * -1 for value in item["bbox"])
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

    params["intersects"] = orjson.dumps(params["intersects"]).decode("utf-8")
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


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


@pytest.mark.asyncio
async def test_landing_forwarded_header(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    await app_client.post(f"/collections/{coll.id}/items", json=item)
    response = (
        await app_client.get(
            "/",
            headers={
                "Forwarded": "proto=https;host=test:1234",
                "X-Forwarded-Proto": "http",
                "X-Forwarded-Port": "4321",
            },
        )
    ).json()
    for link in response["links"]:
        assert link["href"].startswith("https://test:1234/")


@pytest.mark.asyncio
async def test_search_forwarded_header(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    await app_client.post(f"/collections/{coll.id}/items", json=item)
    resp = await app_client.post(
        "/search",
        json={
            "collections": [item["collection"]],
        },
        headers={"Forwarded": "proto=https;host=test:1234"},
    )
    features = resp.json()["features"]
    assert len(features) > 0
    for feature in features:
        for link in feature["links"]:
            assert link["href"].startswith("https://test:1234/")


@pytest.mark.asyncio
async def test_search_x_forwarded_headers(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    await app_client.post(f"/collections/{coll.id}/items", json=item)
    resp = await app_client.post(
        "/search",
        json={
            "collections": [item["collection"]],
        },
        headers={
            "X-Forwarded-Proto": "https",
            "X-Forwarded-Port": "1234",
        },
    )
    features = resp.json()["features"]
    assert len(features) > 0
    for feature in features:
        for link in feature["links"]:
            assert link["href"].startswith("https://test:1234/")


@pytest.mark.asyncio
async def test_search_duplicate_forward_headers(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    await app_client.post(f"/collections/{coll.id}/items", json=item)
    resp = await app_client.post(
        "/search",
        json={
            "collections": [item["collection"]],
        },
        headers={
            "Forwarded": "proto=https;host=test:1234",
            "X-Forwarded-Proto": "http",
            "X-Forwarded-Port": "4321",
        },
    )
    features = resp.json()["features"]
    assert len(features) > 0
    for feature in features:
        for link in feature["links"]:
            assert link["href"].startswith("https://test:1234/")


@pytest.mark.asyncio
async def test_base_queryables(load_test_data, app_client, load_test_collection):
    resp = await app_client.get("/queryables")
    assert resp.headers["Content-Type"] == "application/schema+json"
    q = resp.json()
    assert q["$id"].endswith("/queryables")
    assert q["type"] == "object"
    assert "properties" in q
    assert "id" in q["properties"]
    assert "eo:cloud_cover" in q["properties"]


@pytest.mark.asyncio
async def test_collection_queryables(load_test_data, app_client, load_test_collection):
    resp = await app_client.get("/collections/test-collection/queryables")
    assert resp.headers["Content-Type"] == "application/schema+json"
    q = resp.json()
    assert q["$id"].endswith("/collections/test-collection/queryables")
    assert q["type"] == "object"
    assert "properties" in q
    assert "id" in q["properties"]
    assert "eo:cloud_cover" in q["properties"]


@pytest.mark.asyncio
async def test_item_collection_filter_bbox(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    first_item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=first_item)
    assert resp.status_code == 200

    bbox = "100,-50,170,-20"
    resp = await app_client.get(f"/collections/{coll.id}/items", params={"bbox": bbox})
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1

    bbox = "1,2,3,4"
    resp = await app_client.get(f"/collections/{coll.id}/items", params={"bbox": bbox})
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 0


@pytest.mark.asyncio
async def test_item_collection_filter_datetime(
    load_test_data, app_client, load_test_collection
):
    coll = load_test_collection
    first_item = load_test_data("test_item.json")
    resp = await app_client.post(f"/collections/{coll.id}/items", json=first_item)
    assert resp.status_code == 200

    datetime_range = "2020-01-01T00:00:00.00Z/.."
    resp = await app_client.get(
        f"/collections/{coll.id}/items", params={"datetime": datetime_range}
    )
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1

    datetime_range = "2018-01-01T00:00:00.00Z/2019-01-01T00:00:00.00Z"
    resp = await app_client.get(
        f"/collections/{coll.id}/items", params={"datetime": datetime_range}
    )
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 0


@pytest.mark.asyncio
async def test_bad_collection_queryables(
    load_test_data, app_client, load_test_collection
):
    resp = await app_client.get("/collections/bad-collection/queryables")
    assert resp.status_code == 404


async def test_deleting_items_with_identical_ids(app_client):
    collection_a = Collection("collection-a", "The first collection", DEFAULT_EXTENT)
    collection_b = Collection("collection-b", "The second collection", DEFAULT_EXTENT)
    item = Item("the-item", GLOBAL_GEOMETRY, GLOBAL_BBOX, datetime.now(), {})

    for collection in (collection_a, collection_b):
        response = await app_client.post(
            "/collections", json=collection.to_dict(include_self_link=False)
        )
        assert response.status_code == 200
        item_as_dict = item.to_dict(include_self_link=False)
        item_as_dict["collection"] = collection.id
        response = await app_client.post(
            f"/collections/{collection.id}/items", json=item_as_dict
        )
        assert response.status_code == 200
        response = await app_client.get(f"/collections/{collection.id}/items")
        assert response.status_code == 200, response.json()
        assert len(response.json()["features"]) == 1

    for collection in (collection_a, collection_b):
        response = await app_client.delete(
            f"/collections/{collection.id}/items/{item.id}"
        )
        assert response.status_code == 200, response.json()
        response = await app_client.get(f"/collections/{collection.id}/items")
        assert response.status_code == 200, response.json()
        assert not response.json()["features"]


@pytest.mark.parametrize("direction", ("asc", "desc"))
async def test_sorting_and_paging(app_client, load_test_collection, direction: str):
    collection_id = load_test_collection.id
    for i in range(10):
        item = Item(
            id=f"item-{i}",
            geometry={"type": "Point", "coordinates": [-105.1019, 40.1672]},
            bbox=[-105.1019, 40.1672, -105.1019, 40.1672],
            datetime=datetime.now(),
            properties={
                "eo:cloud_cover": 42 + i if i % 3 != 0 else None,
            },
        )
        item.collection_id = collection_id
        response = await app_client.post(
            f"/collections/{collection_id}/items",
            json=item.to_dict(include_self_link=False, transform_hrefs=False),
        )
        assert response.status_code == 200

    async def search(query: Dict[str, Any]) -> List[Item]:
        items: List[Item] = list()
        while True:
            response = await app_client.post("/search", json=query)
            json = response.json()
            assert response.status_code == 200, json
            items.extend((Item.from_dict(d) for d in json["features"]))
            next_link = next(
                (link for link in json["links"] if link["rel"] == "next"), None
            )
            if next_link is None:
                return items
            else:
                query = next_link["body"]

    query = {
        "collections": [collection_id],
        "sortby": [{"field": "properties.eo:cloud_cover", "direction": direction}],
        "limit": 5,
    }
    items = await search(query)
    assert len(items) == 10, items
