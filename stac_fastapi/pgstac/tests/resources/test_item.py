import json
import uuid
from datetime import datetime, timedelta
from typing import Callable
from urllib.parse import parse_qs, urljoin, urlparse

import pystac
import pytest
from httpx import AsyncClient
from shapely.geometry import Polygon
from stac_pydantic import Collection, Item
from stac_pydantic.shared import DATETIME_RFC339
from starlette.requests import Request

from stac_fastapi.pgstac.models.links import CollectionLinks


@pytest.mark.asyncio
async def test_create_collection(app_client, load_test_data: Callable):
    in_json = load_test_data("test_collection.json")
    in_coll = Collection.parse_obj(in_json)
    resp = await app_client.post(
        "/collections",
        json=in_json,
    )
    assert resp.status_code == 200
    post_coll = Collection.parse_obj(resp.json())
    assert in_coll.dict(exclude={"links"}) == post_coll.dict(exclude={"links"})
    resp = await app_client.get(f"/collections/{post_coll.id}")
    assert resp.status_code == 200
    get_coll = Collection.parse_obj(resp.json())
    assert post_coll.dict(exclude={"links"}) == get_coll.dict(exclude={"links"})


@pytest.mark.asyncio
async def test_update_collection(app_client, load_test_data, load_test_collection):
    in_coll = load_test_collection
    in_coll.keywords.append("newkeyword")

    resp = await app_client.put("/collections", json=in_coll.dict())
    assert resp.status_code == 200

    resp = await app_client.get(f"/collections/{in_coll.id}")
    assert resp.status_code == 200

    get_coll = Collection.parse_obj(resp.json())
    assert in_coll.dict(exclude={"links"}) == get_coll.dict(exclude={"links"})
    assert "newkeyword" in get_coll.keywords


@pytest.mark.asyncio
async def test_delete_collection(
    app_client, load_test_data: Callable, load_test_collection
):
    in_coll = load_test_collection

    resp = await app_client.delete(f"/collections/{in_coll.id}")
    assert resp.status_code == 200

    resp = await app_client.get(f"/collections/{in_coll.id}")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_create_item(app_client, load_test_data: Callable, load_test_collection):
    coll = load_test_collection

    in_json = load_test_data("test_item.json")
    in_item = Item.parse_obj(in_json)
    resp = await app_client.post(
        f"/collections/{coll.id}/items",
        json=in_json,
    )
    assert resp.status_code == 200

    post_item = Item.parse_obj(resp.json())
    assert in_item.dict(exclude={"links"}) == post_item.dict(exclude={"links"})

    resp = await app_client.get(f"/collections/{coll.id}/items/{post_item.id}")

    assert resp.status_code == 200
    get_item = Item.parse_obj(resp.json())
    assert in_item.dict(exclude={"links"}) == get_item.dict(exclude={"links"})


@pytest.mark.asyncio
async def test_fetches_valid_item(
    app_client, load_test_data: Callable, load_test_collection
):
    coll = load_test_collection

    in_json = load_test_data("test_item.json")
    in_item = Item.parse_obj(in_json)
    resp = await app_client.post(
        "/collections/{coll.id}/items",
        json=in_json,
    )
    assert resp.status_code == 200

    post_item = Item.parse_obj(resp.json())
    assert in_item.dict(exclude={"links"}) == post_item.dict(exclude={"links"})

    resp = await app_client.get(f"/collections/{coll.id}/items/{post_item.id}")

    assert resp.status_code == 200
    item_dict = resp.json()
    # Mock root to allow validation
    mock_root = pystac.Catalog(
        id="test", description="test desc", href="https://example.com"
    )
    item = pystac.Item.from_dict(item_dict, preserve_dict=False, root=mock_root)
    item.validate()


@pytest.mark.asyncio
async def test_update_item(
    app_client, load_test_data: Callable, load_test_collection, load_test_item
):
    coll = load_test_collection
    item = load_test_item

    item.properties.description = "Update Test"

    resp = await app_client.put(f"/collections/{coll.id}/items", content=item.json())
    assert resp.status_code == 200

    resp = await app_client.get(f"/collections/{coll.id}/items/{item.id}")
    assert resp.status_code == 200

    get_item = Item.parse_obj(resp.json())
    assert item.dict(exclude={"links"}) == get_item.dict(exclude={"links"})
    assert get_item.properties.description == "Update Test"


@pytest.mark.asyncio
async def test_delete_item(
    app_client, load_test_data: Callable, load_test_collection, load_test_item
):
    coll = load_test_collection
    item = load_test_item

    resp = await app_client.delete(f"/collections/{coll.id}/items/{item.id}")
    print(resp.content)
    assert resp.status_code == 200

    resp = await app_client.get(f"/collections/{coll.id}/items/{item.id}")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_collection_items(app_client, load_test_collection, load_test_item):
    coll = load_test_collection
    item = load_test_item

    for _ in range(4):
        item.id = str(uuid.uuid4())
        resp = await app_client.post(
            f"/collections/{coll.id}/items",
            content=item.json(),
        )
        assert resp.status_code == 200

    resp = await app_client.get(
        f"/collections/{coll.id}/items",
    )
    assert resp.status_code == 200
    fc = resp.json()
    assert "features" in fc
    assert len(fc["features"]) == 5


@pytest.mark.asyncio
async def test_create_item_conflict(
    app_client, load_test_data: Callable, load_test_collection
):
    pass

    in_json = load_test_data("test_item.json")
    Item.parse_obj(in_json)
    resp = await app_client.post(
        "/collections/{coll.id}/items",
        json=in_json,
    )
    assert resp.status_code == 200

    resp = await app_client.post(
        "/collections/{coll.id}/items",
        json=in_json,
    )
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_delete_missing_item(
    app_client, load_test_data: Callable, load_test_collection, load_test_item
):
    coll = load_test_collection
    item = load_test_item

    resp = await app_client.delete(f"/collections/{coll.id}/items/{item.id}")
    print(resp.content)
    assert resp.status_code == 200

    resp = await app_client.delete(f"/collections/{coll.id}/items/{item.id}")
    print(resp.content)
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_create_item_missing_collection(
    app_client, load_test_data: Callable, load_test_collection
):
    coll = load_test_collection
    item = load_test_data("test_item.json")
    item["collection"] = None

    resp = await app_client.post(f"/collections/{coll.id}/items", json=item)
    assert resp.status_code == 424


@pytest.mark.asyncio
async def test_update_new_item(
    app_client, load_test_data: Callable, load_test_collection, load_test_item
):
    coll = load_test_collection
    item = load_test_item
    item.id = "test-updatenewitem"

    resp = await app_client.put(f"/collections/{coll.id}/items", content=item.json())
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_update_item_missing_collection(
    app_client, load_test_data: Callable, load_test_collection, load_test_item
):
    coll = load_test_collection
    item = load_test_item
    item.collection = None

    resp = await app_client.put(f"/collections/{coll.id}/items", content=item.json())
    assert resp.status_code == 424


@pytest.mark.asyncio
async def test_pagination(app_client, load_test_data, load_test_collection):
    """Test item collection pagination (paging extension)"""
    coll = load_test_collection
    item_count = 21
    test_item = load_test_data("test_item.json")

    for idx in range(1, item_count):
        item = Item.parse_obj(test_item)
        item.id = item.id + str(idx)
        item.properties.datetime = f"2020-01-{idx:02d}T00:00:00"
        resp = await app_client.post(f"/collections/{coll.id}/items", json=item.dict())
        assert resp.status_code == 200

    resp = await app_client.get(f"/collections/{coll.id}/items", params={"limit": 3})
    assert resp.status_code == 200
    first_page = resp.json()
    for feature in first_page["features"]:
        print(feature["id"], feature["properties"]["datetime"])
    print(f"first page links {first_page['links']}")
    assert len(first_page["features"]) == 3

    nextlink = [
        link["href"] for link in first_page["links"] if link["rel"] == "next"
    ].pop()

    assert nextlink is not None

    assert [f["id"] for f in first_page["features"]] == [
        "test-item20",
        "test-item19",
        "test-item18",
    ]

    print(f"Next {nextlink}")

    resp = await app_client.get(nextlink)
    assert resp.status_code == 200
    second_page = resp.json()
    for feature in second_page["features"]:
        print(feature["id"], feature["properties"]["datetime"])
    print(f"second page links {second_page['links']}")
    assert len(first_page["features"]) == 3

    nextlink = [
        link["href"] for link in second_page["links"] if link["rel"] == "next"
    ].pop()

    assert nextlink is not None

    prevlink = [
        link["href"] for link in second_page["links"] if link["rel"] == "previous"
    ].pop()

    assert prevlink is not None
    print(nextlink, prevlink)

    assert [f["id"] for f in second_page["features"]] == [
        "test-item17",
        "test-item16",
        "test-item15",
    ]

    resp = await app_client.get(prevlink)
    assert resp.status_code == 200
    back_page = resp.json()
    for feature in back_page["features"]:
        print(feature["id"], feature["properties"]["datetime"])
    print(back_page["links"])
    assert len(back_page["features"]) == 3
    assert [f["id"] for f in back_page["features"]] == [
        "test-item20",
        "test-item19",
        "test-item18",
    ]


@pytest.mark.asyncio
async def test_item_search_by_id_post(app_client, load_test_data, load_test_collection):
    """Test POST search by item id (core)"""
    ids = ["test1", "test2", "test3"]
    for id in ids:
        test_item = load_test_data("test_item.json")
        test_item["id"] = id
        resp = await app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200

    params = {"collections": [test_item["collection"]], "ids": ids}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == len(ids)
    assert set([feat["id"] for feat in resp_json["features"]]) == set(ids)


@pytest.mark.asyncio
async def test_item_search_by_id_no_results_post(
    app_client, load_test_data, load_test_collection
):
    """Test POST search by item id (core) when there are no results"""
    test_item = load_test_data("test_item.json")

    search_ids = ["nonexistent_id"]

    params = {"collections": [test_item["collection"]], "ids": search_ids}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 0


@pytest.mark.asyncio
async def test_item_search_spatial_query_post(
    app_client, load_test_data, load_test_collection
):
    """Test POST search with spatial query (core)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    params = {
        "collections": [test_item["collection"]],
        "intersects": test_item["geometry"],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_temporal_query_post(
    app_client, load_test_data, load_test_collection
):
    """Test POST search with single-tailed spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    item_date = datetime.strptime(test_item["properties"]["datetime"], DATETIME_RFC339)
    print(item_date)
    item_date = item_date + timedelta(seconds=1)

    params = {
        "collections": [test_item["collection"]],
        "intersects": test_item["geometry"],
        "datetime": item_date.strftime(DATETIME_RFC339),
    }

    resp = await app_client.post("/search", json=params)
    print(resp.content)
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_temporal_window_post(
    app_client, load_test_data, load_test_collection
):
    """Test POST search with two-tailed spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    item_date = datetime.strptime(test_item["properties"]["datetime"], DATETIME_RFC339)
    item_date_before = item_date - timedelta(seconds=1)
    item_date_after = item_date + timedelta(seconds=1)

    params = {
        "collections": [test_item["collection"]],
        "datetime": f"{item_date_before.strftime(DATETIME_RFC339)}/{item_date_after.strftime(DATETIME_RFC339)}",
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_temporal_open_window(
    app_client, load_test_data, load_test_collection
):
    """Test POST search with open spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    params = {
        "collections": [test_item["collection"]],
        "datetime": "../..",
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()
    assert len(resp_json["features"]) == 2


@pytest.mark.asyncio
async def test_item_search_sort_post(app_client, load_test_data, load_test_collection):
    """Test POST search with sorting (sort extension)"""
    first_item = load_test_data("test_item.json")
    item_date = datetime.strptime(first_item["properties"]["datetime"], DATETIME_RFC339)
    resp = await app_client.post(
        f"/collections/{first_item['collection']}/items", json=first_item
    )
    assert resp.status_code == 200

    second_item = load_test_data("test_item.json")
    second_item["id"] = "another-item"
    another_item_date = item_date - timedelta(days=1)
    second_item["properties"]["datetime"] = another_item_date.strftime(DATETIME_RFC339)
    resp = await app_client.post(
        f"/collections/{second_item['collection']}/items", json=second_item
    )
    assert resp.status_code == 200

    params = {
        "collections": [first_item["collection"]],
        "sortby": [{"field": "datetime", "direction": "desc"}],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == first_item["id"]
    assert resp_json["features"][1]["id"] == second_item["id"]


@pytest.mark.asyncio
async def test_item_search_by_id_get(app_client, load_test_data, load_test_collection):
    """Test GET search by item id (core)"""
    ids = ["test1", "test2", "test3"]
    for id in ids:
        test_item = load_test_data("test_item.json")
        test_item["id"] = id
        resp = await app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200

    params = {"collections": test_item["collection"], "ids": ",".join(ids)}
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == len(ids)
    assert set([feat["id"] for feat in resp_json["features"]]) == set(ids)


@pytest.mark.asyncio
async def test_item_search_bbox_get(app_client, load_test_data, load_test_collection):
    """Test GET search with spatial query (core)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    params = {
        "collections": test_item["collection"],
        "bbox": ",".join([str(coord) for coord in test_item["bbox"]]),
    }
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_get_without_collections(
    app_client, load_test_data, load_test_collection
):
    """Test GET search without specifying collections"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    params = {
        "bbox": ",".join([str(coord) for coord in test_item["bbox"]]),
    }
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_temporal_window_get(
    app_client, load_test_data, load_test_collection
):
    """Test GET search with spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Add second item with a different datetime.
    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    item_date = datetime.strptime(test_item["properties"]["datetime"], DATETIME_RFC339)
    item_date_before = item_date - timedelta(seconds=1)
    item_date_after = item_date + timedelta(seconds=1)

    params = {
        "collections": test_item["collection"],
        "datetime": f"{item_date_before.strftime(DATETIME_RFC339)}/{item_date_after.strftime(DATETIME_RFC339)}",
    }
    resp = await app_client.get("/search", params=params)
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_sort_get(app_client, load_test_data, load_test_collection):
    """Test GET search with sorting (sort extension)"""
    first_item = load_test_data("test_item.json")
    item_date = datetime.strptime(first_item["properties"]["datetime"], DATETIME_RFC339)
    resp = await app_client.post(
        f"/collections/{first_item['collection']}/items", json=first_item
    )
    assert resp.status_code == 200

    second_item = load_test_data("test_item.json")
    second_item["id"] = "another-item"
    another_item_date = item_date - timedelta(days=1)
    second_item["properties"]["datetime"] = another_item_date.strftime(DATETIME_RFC339)
    resp = await app_client.post(
        f"/collections/{second_item['collection']}/items", json=second_item
    )
    assert resp.status_code == 200
    params = {"collections": [first_item["collection"]], "sortby": "-datetime"}
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == first_item["id"]
    assert resp_json["features"][1]["id"] == second_item["id"]


@pytest.mark.asyncio
async def test_item_search_post_without_collection(
    app_client, load_test_data, load_test_collection
):
    """Test POST search without specifying a collection"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    params = {
        "bbox": test_item["bbox"],
    }
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


@pytest.mark.asyncio
async def test_item_search_properties_jsonb(
    app_client, load_test_data, load_test_collection
):
    """Test POST search with JSONB query (query extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {"query": {"proj:epsg": {"gt": test_item["properties"]["proj:epsg"] - 1}}}
    print(params)
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


@pytest.mark.asyncio
async def test_item_search_properties_field(
    app_client, load_test_data, load_test_collection
):
    """Test POST search indexed field with query (query extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    params = {"query": {"eo:cloud_cover": {"eq": 0}}}
    print(params)
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 1


@pytest.mark.asyncio
async def test_item_search_get_query_extension(
    app_client, load_test_data, load_test_collection
):
    """Test GET search with JSONB query (query extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {
        "collections": [test_item["collection"]],
        "query": json.dumps(
            {"proj:epsg": {"gt": test_item["properties"]["proj:epsg"] + 1}}
        ),
    }
    resp = await app_client.get("/search", params=params)
    # No items found should still return a 200 but with an empty list of features
    assert resp.status_code == 200
    assert len(resp.json()["features"]) == 0

    params["query"] = json.dumps(
        {"proj:epsg": {"eq": test_item["properties"]["proj:epsg"]}}
    )
    resp = await app_client.get("/search", params=params)
    resp_json = resp.json()
    assert len(resp.json()["features"]) == 1
    assert (
        resp_json["features"][0]["properties"]["proj:epsg"]
        == test_item["properties"]["proj:epsg"]
    )


@pytest.mark.asyncio
async def test_item_search_get_filter_extension_cql(
    app_client, load_test_data, load_test_collection
):
    """Test GET search with JSONB query (cql json filter extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    second_test_item = load_test_data("test_item2.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=second_test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {
        "collections": [test_item["collection"]],
        "filter": {
            "gt": [
                {"property": "proj:epsg"},
                test_item["properties"]["proj:epsg"] + 1,
            ]
        },
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()

    assert resp.status_code == 200
    assert len(resp_json.get("features")) == 0

    params = {
        "collections": [test_item["collection"]],
        "filter": {
            "eq": [
                {"property": "proj:epsg"},
                test_item["properties"]["proj:epsg"],
            ]
        },
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()
    assert len(resp.json()["features"]) == 1
    assert (
        resp_json["features"][0]["properties"]["proj:epsg"]
        == test_item["properties"]["proj:epsg"]
    )


@pytest.mark.asyncio
async def test_get_missing_item_collection(app_client):
    """Test reading a collection which does not exist"""
    resp = await app_client.get("/collections/invalid-collection/items")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_item_from_missing_item_collection(app_client):
    """Test reading an item from a collection which does not exist"""
    resp = await app_client.get("/collections/invalid-collection/items/some-item")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_pagination_item_collection(
    app_client, load_test_data, load_test_collection
):
    """Test item collection pagination links (paging extension)"""
    test_item = load_test_data("test_item.json")
    ids = []

    # Ingest 5 items
    for idx in range(5):
        uid = str(uuid.uuid4())
        test_item["id"] = uid
        resp = await app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        ids.append(uid)

    print(ids)

    # Paginate through all 5 items with a limit of 1 (expecting 5 requests)
    page = await app_client.get(
        f"/collections/{test_item['collection']}/items", params={"limit": 1}
    )
    idx = 0
    item_ids = []
    while True:
        idx += 1
        page_data = page.json()
        item_ids.append(page_data["features"][0]["id"])
        print(idx, item_ids)
        nextlink = [
            link["href"] for link in page_data["links"] if link["rel"] == "next"
        ]
        if len(nextlink) < 1:
            break
        page = await app_client.get(nextlink.pop())
        if idx >= 10:
            assert False

    # Our limit is 1 so we expect len(ids) number of requests before we run out of pages
    assert idx == len(ids)

    # Confirm we have paginated through all items
    assert not set(item_ids) - set(ids)


@pytest.mark.asyncio
async def test_pagination_post(app_client, load_test_data, load_test_collection):
    """Test POST pagination (paging extension)"""
    test_item = load_test_data("test_item.json")
    ids = []

    # Ingest 5 items
    for idx in range(5):
        uid = str(uuid.uuid4())
        test_item["id"] = uid
        resp = await app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        ids.append(uid)

    # Paginate through all 5 items with a limit of 1 (expecting 5 requests)
    request_body = {"ids": ids, "limit": 1}
    page = await app_client.post("/search", json=request_body)
    idx = 0
    item_ids = []
    while True:
        idx += 1
        page_data = page.json()
        item_ids.append(page_data["features"][0]["id"])
        next_link = list(filter(lambda l: l["rel"] == "next", page_data["links"]))
        if not next_link:
            break
        # Merge request bodies
        request_body.update(next_link[0]["body"])
        page = await app_client.post("/search", json=request_body)

        if idx > 10:
            assert False

    # Our limit is 1 so we expect len(ids) number of requests before we run out of pages
    assert idx == len(ids)

    # Confirm we have paginated through all items
    assert not set(item_ids) - set(ids)


@pytest.mark.asyncio
async def test_pagination_token_idempotent(
    app_client, load_test_data, load_test_collection
):
    """Test that pagination tokens are idempotent (paging extension)"""
    test_item = load_test_data("test_item.json")
    ids = []

    # Ingest 5 items
    for idx in range(5):
        uid = str(uuid.uuid4())
        test_item["id"] = uid
        resp = await app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        ids.append(uid)

    page = await app_client.get("/search", params={"ids": ",".join(ids), "limit": 3})
    page_data = page.json()
    next_link = list(filter(lambda l: l["rel"] == "next", page_data["links"]))

    # Confirm token is idempotent
    resp1 = await app_client.get(
        "/search", params=parse_qs(urlparse(next_link[0]["href"]).query)
    )
    resp2 = await app_client.get(
        "/search", params=parse_qs(urlparse(next_link[0]["href"]).query)
    )
    resp1_data = resp1.json()
    resp2_data = resp2.json()

    # Two different requests with the same pagination token should return the same items
    assert [item["id"] for item in resp1_data["features"]] == [
        item["id"] for item in resp2_data["features"]
    ]


@pytest.mark.asyncio
async def test_field_extension_get(app_client, load_test_data, load_test_collection):
    """Test GET search with included fields (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    params = {"fields": "+properties.proj:epsg,+properties.gsd,+collection"}
    resp = await app_client.get("/search", params=params)
    feat_properties = resp.json()["features"][0]["properties"]
    assert not set(feat_properties) - {"proj:epsg", "gsd", "datetime"}


@pytest.mark.asyncio
async def test_field_extension_post(app_client, load_test_data, load_test_collection):
    """Test POST search with included and excluded fields (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    body = {
        "fields": {
            "exclude": ["assets.B1"],
            "include": [
                "properties.eo:cloud_cover",
                "properties.orientation",
                "assets",
                "collection",
            ],
        }
    }

    resp = await app_client.post("/search", json=body)
    resp_json = resp.json()
    print(resp_json)
    assert "B1" not in resp_json["features"][0]["assets"].keys()
    assert not set(resp_json["features"][0]["properties"]) - {
        "orientation",
        "eo:cloud_cover",
        "datetime",
    }


@pytest.mark.asyncio
async def test_field_extension_exclude_and_include(
    app_client, load_test_data, load_test_collection
):
    """Test POST search including/excluding same field (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    body = {
        "fields": {
            "exclude": ["properties.eo:cloud_cover"],
            "include": ["properties.eo:cloud_cover", "collection"],
        }
    }

    resp = await app_client.post("/search", json=body)
    resp_json = resp.json()
    assert "properties" not in resp_json["features"][0]


@pytest.mark.asyncio
async def test_field_extension_exclude_default_includes(
    app_client, load_test_data, load_test_collection
):
    """Test POST search excluding a forbidden field (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    body = {"fields": {"exclude": ["geometry"]}}

    resp = await app_client.post("/search", json=body)
    resp_json = resp.json()
    assert "geometry" not in resp_json["features"][0]


@pytest.mark.asyncio
async def test_search_intersects_and_bbox(app_client):
    """Test POST search intersects and bbox are mutually exclusive (core)"""
    bbox = [-118, 34, -117, 35]
    geoj = Polygon.from_bounds(*bbox).__geo_interface__
    params = {"bbox": bbox, "intersects": geoj}
    resp = await app_client.post("/search", json=params)
    assert resp.status_code == 400


@pytest.mark.asyncio
async def test_get_missing_item(app_client, load_test_data):
    """Test read item which does not exist (transactions extension)"""
    test_coll = load_test_data("test_collection.json")
    resp = await app_client.get(f"/collections/{test_coll['id']}/items/invalid-item")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_relative_link_construction():
    req = Request(
        scope={
            "type": "http",
            "scheme": "http",
            "method": "PUT",
            "root_path": "http://test/stac",
            "path": "/",
            "raw_path": b"/tab/abc",
            "query_string": b"",
            "headers": {},
        }
    )
    links = CollectionLinks(collection_id="naip", request=req)
    assert links.link_items()["href"] == "http://test/stac/collections/naip/items"


@pytest.mark.asyncio
async def test_search_bbox_errors(app_client):
    body = {"query": {"bbox": [0]}}
    resp = await app_client.post("/search", json=body)
    assert resp.status_code == 400

    body = {"query": {"bbox": [100.0, 0.0, 0.0, 105.0, 1.0, 1.0]}}
    resp = await app_client.post("/search", json=body)
    assert resp.status_code == 400

    params = {"bbox": "100.0,0.0,0.0,105.0"}
    resp = await app_client.get("/search", params=params)
    assert resp.status_code == 400


@pytest.mark.asyncio
async def test_preserves_extra_link(
    app_client: AsyncClient, load_test_data, load_test_collection
):
    coll = load_test_collection
    test_item = load_test_data("test_item.json")
    expected_href = urljoin(str(app_client.base_url), "preview.html")

    resp = await app_client.post(f"/collections/{coll.id}/items", json=test_item)
    assert resp.status_code == 200

    response_item = await app_client.get(
        f"/collections/{coll.id}/items/{test_item['id']}",
        params={"limit": 1},
    )
    assert response_item.status_code == 200
    item = response_item.json()

    extra_link = [link for link in item["links"] if link["rel"] == "preview"]
    assert extra_link
    assert extra_link[0]["href"] == expected_href


@pytest.mark.asyncio
async def test_item_search_get_filter_extension_cql_explicitlang(
    app_client, load_test_data, load_test_collection
):
    """Test GET search with JSONB query (cql json filter extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {
        "collections": [test_item["collection"]],
        "filter-lang": "cql-json",
        "filter": {
            "gt": [
                {"property": "proj:epsg"},
                test_item["properties"]["proj:epsg"] + 1,
            ]
        },
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()

    assert resp.status_code == 200
    assert len(resp_json.get("features")) == 0

    params = {
        "collections": [test_item["collection"]],
        "filter-lang": "cql-json",
        "filter": {
            "eq": [
                {"property": "proj:epsg"},
                test_item["properties"]["proj:epsg"],
            ]
        },
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()
    assert len(resp.json()["features"]) == 1
    assert (
        resp_json["features"][0]["properties"]["proj:epsg"]
        == test_item["properties"]["proj:epsg"]
    )


@pytest.mark.asyncio
async def test_item_search_get_filter_extension_cql2(
    app_client, load_test_data, load_test_collection
):
    """Test GET search with JSONB query (cql json filter extension)"""
    test_item = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {
        "filter-lang": "cql2-json",
        "filter": {
            "op": "and",
            "args": [
                {
                    "op": "eq",
                    "args": [
                        {"property": "proj:epsg"},
                        test_item["properties"]["proj:epsg"] + 1,
                    ],
                },
                {
                    "op": "in",
                    "args": [
                        {"property": "collection"},
                        [test_item["collection"]],
                    ],
                },
            ],
        },
    }
    print(json.dumps(params))
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()
    print(resp_json)

    assert resp.status_code == 200
    assert len(resp_json.get("features")) == 0

    params = {
        "filter-lang": "cql2-json",
        "filter": {
            "op": "and",
            "args": [
                {
                    "op": "eq",
                    "args": [
                        {"property": "proj:epsg"},
                        test_item["properties"]["proj:epsg"],
                    ],
                },
                {
                    "op": "in",
                    "args": [
                        {"property": "collection"},
                        [test_item["collection"]],
                    ],
                },
            ],
        },
    }
    resp = await app_client.post("/search", json=params)
    resp_json = resp.json()
    print(resp_json)
    assert len(resp.json()["features"]) == 1
    assert (
        resp_json["features"][0]["properties"]["proj:epsg"]
        == test_item["properties"]["proj:epsg"]
    )


@pytest.mark.asyncio
async def test_search_datetime_validation_errors(app_client):
    bad_datetimes = [
        "37-01-01T12:00:27.87Z",
        "1985-13-12T23:20:50.52Z",
        "1985-12-32T23:20:50.52Z",
        "1985-12-01T25:20:50.52Z",
        "1985-12-01T00:60:50.52Z",
        "1985-12-01T00:06:61.52Z",
        "1990-12-31T23:59:61Z",
        "1986-04-12T23:20:50.52Z/1985-04-12T23:20:50.52Z",
    ]
    for dt in bad_datetimes:
        body = {"query": {"datetime": dt}}
        resp = await app_client.post("/search", json=body)
        assert resp.status_code == 400

        resp = await app_client.get("/search?datetime={}".format(dt))
        assert resp.status_code == 400
