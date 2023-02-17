import json
import os
import time
import uuid
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from random import randint
from urllib.parse import parse_qs, urlparse, urlsplit

import pystac
from pydantic.datetime_parse import parse_datetime
from pystac.utils import datetime_to_str
from shapely.geometry import Polygon

from stac_fastapi.sqlalchemy.core import CoreCrudClient
from stac_fastapi.types.core import LandingPageMixin
from stac_fastapi.types.rfc3339 import rfc3339_str_to_datetime


def test_create_and_delete_item(app_client, load_test_data):
    """Test creation and deletion of a single item (transactions extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    resp = app_client.delete(
        f"/collections/{test_item['collection']}/items/{resp.json()['id']}"
    )
    assert resp.status_code == 200


def test_create_item_conflict(app_client, load_test_data):
    """Test creation of an item which already exists (transactions extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 409


def test_create_item_duplicate(app_client, load_test_data):
    """Test creation of an item id which already exists but in a different collection(transactions extension)"""

    # add test_item to test-collection
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # add test_item to test-collection again, resource already exists
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 409

    # create "test-collection-2"
    collection_2 = load_test_data("test_collection.json")
    collection_2["id"] = "test-collection-2"
    resp = app_client.post("/collections", json=collection_2)
    assert resp.status_code == 200

    # add test_item to test-collection-2, posts successfully
    test_item["collection"] = "test-collection-2"
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200


def test_delete_item_duplicate(app_client, load_test_data):
    """Test creation of an item id which already exists but in a different collection(transactions extension)"""

    # add test_item to test-collection
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # create "test-collection-2"
    collection_2 = load_test_data("test_collection.json")
    collection_2["id"] = "test-collection-2"
    resp = app_client.post("/collections", json=collection_2)
    assert resp.status_code == 200

    # add test_item to test-collection-2
    test_item["collection"] = "test-collection-2"
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # delete test_item from test-collection
    test_item["collection"] = "test-collection"
    resp = app_client.delete(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert resp.status_code == 200

    # test-item in test-collection has already been deleted
    resp = app_client.delete(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert resp.status_code == 404

    # test-item in test-collection-2 still exists, was not deleted
    test_item["collection"] = "test-collection-2"
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 409


def test_update_item_duplicate(app_client, load_test_data):
    """Test creation of an item id which already exists but in a different collection(transactions extension)"""

    # add test_item to test-collection
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # create "test-collection-2"
    collection_2 = load_test_data("test_collection.json")
    collection_2["id"] = "test-collection-2"
    resp = app_client.post("/collections", json=collection_2)
    assert resp.status_code == 200

    # add test_item to test-collection-2
    test_item["collection"] = "test-collection-2"
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # update gsd in test_item, test-collection-2
    test_item["properties"]["gsd"] = 16
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        json=test_item,
    )
    assert resp.status_code == 200
    updated_item = resp.json()
    assert updated_item["properties"]["gsd"] == 16

    # update gsd in test_item, test-collection
    test_item["collection"] = "test-collection"
    test_item["properties"]["gsd"] = 17
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        json=test_item,
    )
    assert resp.status_code == 200
    updated_item = resp.json()
    assert updated_item["properties"]["gsd"] == 17

    # test_item in test-collection, updated gsd = 17
    resp = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert resp.status_code == 200
    item = resp.json()
    assert item["properties"]["gsd"] == 17

    # test_item in test-collection-2, updated gsd = 16
    test_item["collection"] = "test-collection-2"
    resp = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert resp.status_code == 200
    item = resp.json()
    assert item["properties"]["gsd"] == 16


def test_delete_missing_item(app_client, load_test_data):
    """Test deletion of an item which does not exist (transactions extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.delete(f"/collections/{test_item['collection']}/items/hijosh")
    assert resp.status_code == 404


def test_create_item_missing_collection(app_client, load_test_data):
    """Test creation of an item without a parent collection (transactions extension)"""
    test_item = load_test_data("test_item.json")
    test_item["collection"] = "stac is cool"
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 424


def test_update_item_already_exists(app_client, load_test_data):
    """Test updating an item which already exists (transactions extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    assert test_item["properties"]["gsd"] != 16
    test_item["properties"]["gsd"] = 16
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        json=test_item,
    )
    updated_item = resp.json()
    assert updated_item["properties"]["gsd"] == 16


def test_update_new_item(app_client, load_test_data):
    """Test updating an item which does not exist (transactions extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        json=test_item,
    )
    assert resp.status_code == 404


def test_update_item_missing_collection(app_client, load_test_data):
    """Test updating an item without a parent collection (transactions extension)"""
    test_item = load_test_data("test_item.json")

    # Create the item
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Try to update collection of the item
    test_item["collection"] = "stac is cool"
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        json=test_item,
    )
    assert resp.status_code == 404


def test_update_item_geometry(app_client, load_test_data):
    test_item = load_test_data("test_item.json")

    # Create the item
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Update the geometry of the item
    test_item["geometry"]["coordinates"] = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        json=test_item,
    )
    assert resp.status_code == 200

    # Fetch the updated item
    resp = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert resp.status_code == 200
    assert resp.json()["geometry"]["coordinates"] == [
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    ]


def test_get_item(app_client, load_test_data):
    """Test read an item by id (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    get_item = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert get_item.status_code == 200


def test_returns_valid_item(app_client, load_test_data):
    """Test validates fetched item with jsonschema"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    get_item = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}"
    )
    assert get_item.status_code == 200
    item_dict = get_item.json()
    # Mock root to allow validation
    mock_root = pystac.Catalog(
        id="test", description="test desc", href="https://example.com"
    )
    item = pystac.Item.from_dict(item_dict, preserve_dict=False, root=mock_root)
    item.validate()


def test_get_item_collection(app_client, load_test_data):
    """Test read an item collection (core)"""
    item_count = randint(1, 4)
    test_item = load_test_data("test_item.json")

    for idx in range(item_count):
        _test_item = deepcopy(test_item)
        _test_item["id"] = test_item["id"] + str(idx)
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=_test_item
        )
        assert resp.status_code == 200

    resp = app_client.get(f"/collections/{test_item['collection']}/items")
    assert resp.status_code == 200

    item_collection = resp.json()
    assert item_collection["context"]["matched"] == len(range(item_count))


def test_pagination(app_client, load_test_data):
    """Test item collection pagination (paging extension)"""
    item_count = 10
    test_item = load_test_data("test_item.json")

    for idx in range(item_count):
        _test_item = deepcopy(test_item)
        _test_item["id"] = test_item["id"] + str(idx)
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=_test_item
        )
        assert resp.status_code == 200

    resp = app_client.get(
        f"/collections/{test_item['collection']}/items", params={"limit": 3}
    )
    assert resp.status_code == 200
    first_page = resp.json()
    assert first_page["context"]["returned"] == 3

    url_components = urlsplit(first_page["links"][0]["href"])
    resp = app_client.get(f"{url_components.path}?{url_components.query}")
    assert resp.status_code == 200
    second_page = resp.json()
    assert second_page["context"]["returned"] == 3


def test_item_timestamps(app_client, load_test_data):
    """Test created and updated timestamps (common metadata)"""
    test_item = load_test_data("test_item.json")
    start_time = datetime.now(timezone.utc)
    time.sleep(2)
    # Confirm `created` timestamp
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    item = resp.json()
    created_dt = parse_datetime(item["properties"]["created"])
    assert resp.status_code == 200
    assert start_time < created_dt < datetime.now(timezone.utc)

    time.sleep(2)
    # Confirm `updated` timestamp
    item["properties"]["proj:epsg"] = 4326
    resp = app_client.put(
        f"/collections/{test_item['collection']}/items/{item['id']}", json=item
    )
    assert resp.status_code == 200
    updated_item = resp.json()

    # Created shouldn't change on update
    assert item["properties"]["created"] == updated_item["properties"]["created"]
    assert parse_datetime(updated_item["properties"]["updated"]) > created_dt


def test_item_search_by_id_post(app_client, load_test_data):
    """Test POST search by item id (core)"""
    ids = ["test1", "test2", "test3"]
    for id in ids:
        test_item = load_test_data("test_item.json")
        test_item["id"] = id
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200

    params = {"collections": [test_item["collection"]], "ids": ids}
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == len(ids)
    assert set([feat["id"] for feat in resp_json["features"]]) == set(ids)


def test_item_search_spatial_query_post(app_client, load_test_data):
    """Test POST search with spatial query (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    params = {
        "collections": [test_item["collection"]],
        "intersects": test_item["geometry"],
    }
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_temporal_query_post(app_client, load_test_data):
    """Test POST search with single-tailed spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    item_date = rfc3339_str_to_datetime(test_item["properties"]["datetime"])
    item_date = item_date + timedelta(seconds=1)

    params = {
        "collections": [test_item["collection"]],
        "intersects": test_item["geometry"],
        "datetime": f"../{datetime_to_str(item_date)}",
    }
    resp = app_client.post("/search", json=params)
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_temporal_window_post(app_client, load_test_data):
    """Test POST search with two-tailed spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    item_date = rfc3339_str_to_datetime(test_item["properties"]["datetime"])
    item_date_before = item_date - timedelta(seconds=1)
    item_date_after = item_date + timedelta(seconds=1)

    params = {
        "collections": [test_item["collection"]],
        "intersects": test_item["geometry"],
        "datetime": f"{datetime_to_str(item_date_before)}/{datetime_to_str(item_date_after)}",
    }
    resp = app_client.post("/search", json=params)
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_temporal_open_window(app_client, load_test_data):
    """Test POST search with open spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    for dt in ["/", "../", "/..", "../.."]:
        resp = app_client.post("/search", json={"datetime": dt})
        assert resp.status_code == 400


def test_item_search_sort_post(app_client, load_test_data):
    """Test POST search with sorting (sort extension)"""
    first_item = load_test_data("test_item.json")
    item_date = rfc3339_str_to_datetime(first_item["properties"]["datetime"])
    resp = app_client.post(
        f"/collections/{first_item['collection']}/items", json=first_item
    )
    assert resp.status_code == 200

    second_item = load_test_data("test_item.json")
    second_item["id"] = "another-item"
    another_item_date = item_date - timedelta(days=1)
    second_item["properties"]["datetime"] = datetime_to_str(another_item_date)
    resp = app_client.post(
        f"/collections/{second_item['collection']}/items", json=second_item
    )
    assert resp.status_code == 200

    params = {
        "collections": [first_item["collection"]],
        "sortby": [{"field": "datetime", "direction": "desc"}],
    }
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == first_item["id"]
    assert resp_json["features"][1]["id"] == second_item["id"]


def test_item_search_by_id_get(app_client, load_test_data):
    """Test GET search by item id (core)"""
    ids = ["test1", "test2", "test3"]
    for id in ids:
        test_item = load_test_data("test_item.json")
        test_item["id"] = id
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200

    params = {"collections": test_item["collection"], "ids": ",".join(ids)}
    resp = app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == len(ids)
    assert set([feat["id"] for feat in resp_json["features"]]) == set(ids)


def test_item_search_bbox_get(app_client, load_test_data):
    """Test GET search with spatial query (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    params = {
        "collections": test_item["collection"],
        "bbox": ",".join([str(coord) for coord in test_item["bbox"]]),
    }
    resp = app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_get_without_collections(app_client, load_test_data):
    """Test GET search without specifying collections"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    params = {
        "bbox": ",".join([str(coord) for coord in test_item["bbox"]]),
    }
    resp = app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_temporal_window_get(app_client, load_test_data):
    """Test GET search with spatio-temporal query (core)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    item_date = rfc3339_str_to_datetime(test_item["properties"]["datetime"])
    item_date_before = item_date - timedelta(seconds=1)
    item_date_after = item_date + timedelta(seconds=1)

    params = {
        "collections": test_item["collection"],
        "bbox": ",".join([str(coord) for coord in test_item["bbox"]]),
        "datetime": f"{datetime_to_str(item_date_before)}/{datetime_to_str(item_date_after)}",
    }
    resp = app_client.get("/search", params=params)
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_sort_get(app_client, load_test_data):
    """Test GET search with sorting (sort extension)"""
    first_item = load_test_data("test_item.json")
    item_date = rfc3339_str_to_datetime(first_item["properties"]["datetime"])
    resp = app_client.post(
        f"/collections/{first_item['collection']}/items", json=first_item
    )
    assert resp.status_code == 200

    second_item = load_test_data("test_item.json")
    second_item["id"] = "another-item"
    another_item_date = item_date - timedelta(days=1)
    second_item["properties"]["datetime"] = datetime_to_str(another_item_date)
    resp = app_client.post(
        f"/collections/{second_item['collection']}/items", json=second_item
    )
    assert resp.status_code == 200
    params = {"collections": [first_item["collection"]], "sortby": "-datetime"}
    resp = app_client.get("/search", params=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == first_item["id"]
    assert resp_json["features"][1]["id"] == second_item["id"]


def test_item_search_post_without_collection(app_client, load_test_data):
    """Test POST search without specifying a collection"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    params = {
        "bbox": test_item["bbox"],
    }
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["features"][0]["id"] == test_item["id"]


def test_item_search_properties_jsonb(app_client, load_test_data):
    """Test POST search with JSONB query (query extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {"query": {"proj:epsg": {"gt": test_item["properties"]["proj:epsg"] + 1}}}
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 0


def test_item_search_properties_field(app_client, load_test_data):
    """Test POST search indexed field with query (query extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # Orientation is an indexed field
    params = {"query": {"orientation": {"eq": "south"}}}
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert len(resp_json["features"]) == 0


def test_item_search_get_query_extension(app_client, load_test_data):
    """Test GET search with JSONB query (query extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    # EPSG is a JSONB key
    params = {
        "collections": [test_item["collection"]],
        "query": json.dumps(
            {"proj:epsg": {"gt": test_item["properties"]["proj:epsg"] + 1}}
        ),
    }
    resp = app_client.get("/search", params=params)
    assert resp.json()["context"]["returned"] == 0

    params["query"] = json.dumps(
        {"proj:epsg": {"eq": test_item["properties"]["proj:epsg"]}}
    )
    resp = app_client.get("/search", params=params)
    resp_json = resp.json()
    assert resp_json["context"]["returned"] == 1
    assert (
        resp_json["features"][0]["properties"]["proj:epsg"]
        == test_item["properties"]["proj:epsg"]
    )


def test_get_missing_item_collection(app_client):
    """Test reading a collection which does not exist"""
    resp = app_client.get("/collections/invalid-collection/items")
    assert resp.status_code == 404


def test_pagination_item_collection(app_client, load_test_data):
    """Test item collection pagination links (paging extension)"""
    test_item = load_test_data("test_item.json")
    ids = []

    # Ingest 5 items
    for idx in range(5):
        uid = str(uuid.uuid4())
        test_item["id"] = uid
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        ids.append(uid)

    # Paginate through all 5 items with a limit of 1 (expecting 5 requests)
    page = app_client.get(
        f"/collections/{test_item['collection']}/items", params={"limit": 1}
    )
    idx = 0
    item_ids = []
    while True:
        idx += 1
        page_data = page.json()
        item_ids.append(page_data["features"][0]["id"])
        next_link = list(filter(lambda link: link["rel"] == "next", page_data["links"]))
        if not next_link:
            break
        query_params = parse_qs(urlparse(next_link[0]["href"]).query)
        page = app_client.get(
            f"/collections/{test_item['collection']}/items",
            params=query_params,
        )

    # Our limit is 1 so we expect len(ids) number of requests before we run out of pages
    assert idx == len(ids)

    # Confirm we have paginated through all items
    assert not set(item_ids) - set(ids)


def test_pagination_post(app_client, load_test_data):
    """Test POST pagination (paging extension)"""
    test_item = load_test_data("test_item.json")
    ids = []

    # Ingest 5 items
    for idx in range(5):
        uid = str(uuid.uuid4())
        test_item["id"] = uid
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        ids.append(uid)

    # Paginate through all 5 items with a limit of 1 (expecting 5 requests)
    request_body = {"ids": ids, "limit": 1}
    page = app_client.post("/search", json=request_body)
    idx = 0
    item_ids = []
    while True:
        idx += 1
        page_data = page.json()
        item_ids.append(page_data["features"][0]["id"])
        next_link = list(filter(lambda link: link["rel"] == "next", page_data["links"]))
        if not next_link:
            break
        # Merge request bodies
        request_body.update(next_link[0]["body"])
        page = app_client.post("/search", json=request_body)

    # Our limit is 1 so we expect len(ids) number of requests before we run out of pages
    assert idx == len(ids)

    # Confirm we have paginated through all items
    assert not set(item_ids) - set(ids)


def test_pagination_token_idempotent(app_client, load_test_data):
    """Test that pagination tokens are idempotent (paging extension)"""
    test_item = load_test_data("test_item.json")
    ids = []

    # Ingest 5 items
    for idx in range(5):
        uid = str(uuid.uuid4())
        test_item["id"] = uid
        resp = app_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        ids.append(uid)

    page = app_client.get("/search", params={"ids": ",".join(ids), "limit": 3})
    page_data = page.json()
    next_link = list(filter(lambda link: link["rel"] == "next", page_data["links"]))

    # Confirm token is idempotent
    resp1 = app_client.get(
        "/search", params=parse_qs(urlparse(next_link[0]["href"]).query)
    )
    resp2 = app_client.get(
        "/search", params=parse_qs(urlparse(next_link[0]["href"]).query)
    )
    resp1_data = resp1.json()
    resp2_data = resp2.json()

    # Two different requests with the same pagination token should return the same items
    assert [item["id"] for item in resp1_data["features"]] == [
        item["id"] for item in resp2_data["features"]
    ]


def test_field_extension_get(app_client, load_test_data):
    """Test GET search with included fields (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    params = {"fields": "+properties.proj:epsg,+properties.gsd"}
    resp = app_client.get("/search", params=params)
    feat_properties = resp.json()["features"][0]["properties"]
    assert not set(feat_properties) - {"proj:epsg", "gsd", "datetime"}


def test_field_extension_post(app_client, load_test_data):
    """Test POST search with included and excluded fields (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    body = {
        "fields": {
            "exclude": ["assets.B1"],
            "include": ["properties.eo:cloud_cover", "properties.orientation"],
        }
    }

    resp = app_client.post("/search", json=body)
    resp_json = resp.json()
    assert "B1" not in resp_json["features"][0]["assets"].keys()
    assert not set(resp_json["features"][0]["properties"]) - {
        "orientation",
        "eo:cloud_cover",
        "datetime",
    }


def test_field_extension_exclude_and_include(app_client, load_test_data):
    """Test POST search including/excluding same field (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    body = {
        "fields": {
            "exclude": ["properties.eo:cloud_cover"],
            "include": ["properties.eo:cloud_cover"],
        }
    }

    resp = app_client.post("/search", json=body)
    resp_json = resp.json()
    assert "eo:cloud_cover" not in resp_json["features"][0]["properties"]


def test_field_extension_exclude_default_includes(app_client, load_test_data):
    """Test POST search excluding a forbidden field (fields extension)"""
    test_item = load_test_data("test_item.json")
    resp = app_client.post(
        f"/collections/{test_item['collection']}/items", json=test_item
    )
    assert resp.status_code == 200

    body = {"fields": {"exclude": ["geometry"]}}

    resp = app_client.post("/search", json=body)
    resp_json = resp.json()
    assert "geometry" not in resp_json["features"][0]


def test_search_intersects_and_bbox(app_client):
    """Test POST search intersects and bbox are mutually exclusive (core)"""
    bbox = [-118, 34, -117, 35]
    geoj = Polygon.from_bounds(*bbox).__geo_interface__
    params = {"bbox": bbox, "intersects": geoj}
    resp = app_client.post("/search", json=params)
    assert resp.status_code == 400


def test_get_missing_item(app_client, load_test_data):
    """Test read item which does not exist (transactions extension)"""
    test_coll = load_test_data("test_collection.json")
    resp = app_client.get(f"/collections/{test_coll['id']}/items/invalid-item")
    assert resp.status_code == 404


def test_search_invalid_query_field(app_client):
    body = {"query": {"gsd": {"lt": 100}, "invalid-field": {"eq": 50}}}
    resp = app_client.post("/search", json=body)
    assert resp.status_code == 400


def test_search_bbox_errors(app_client):
    body = {"query": {"bbox": [0]}}
    resp = app_client.post("/search", json=body)
    assert resp.status_code == 400

    body = {"query": {"bbox": [100.0, 0.0, 0.0, 105.0, 1.0, 1.0]}}
    resp = app_client.post("/search", json=body)
    assert resp.status_code == 400

    params = {"bbox": "100.0,0.0,0.0,105.0"}
    resp = app_client.get("/search", params=params)
    assert resp.status_code == 400


def test_conformance_classes_configurable():
    """Test conformance class configurability"""
    landing = LandingPageMixin()
    landing_page = landing._landing_page(
        base_url="http://test/test",
        conformance_classes=["this is a test"],
        extension_schemas=[],
    )
    assert landing_page["conformsTo"][0] == "this is a test"

    # Update environment to avoid key error on client instantiation
    os.environ["READER_CONN_STRING"] = "testing"
    os.environ["WRITER_CONN_STRING"] = "testing"
    client = CoreCrudClient(base_conformance_classes=["this is a test"])
    assert client.conformance_classes()[0] == "this is a test"


def test_search_datetime_validation_errors(app_client):
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
        resp = app_client.post("/search", json=body)
        assert resp.status_code == 400

        resp = app_client.get("/search?datetime={}".format(dt))
        assert resp.status_code == 400


def test_get_item_forwarded_header(app_client, load_test_data):
    test_item = load_test_data("test_item.json")
    app_client.post(f"/collections/{test_item['collection']}/items", json=test_item)
    get_item = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        headers={"Forwarded": "proto=https;host=testserver:1234"},
    )
    for link in get_item.json()["links"]:
        assert link["href"].startswith("https://testserver:1234/")


def test_get_item_x_forwarded_headers(app_client, load_test_data):
    test_item = load_test_data("test_item.json")
    app_client.post(f"/collections/{test_item['collection']}/items", json=test_item)
    get_item = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        headers={
            "X-Forwarded-Port": "1234",
            "X-Forwarded-Proto": "https",
        },
    )
    for link in get_item.json()["links"]:
        assert link["href"].startswith("https://testserver:1234/")


def test_get_item_duplicate_forwarded_headers(app_client, load_test_data):
    test_item = load_test_data("test_item.json")
    app_client.post(f"/collections/{test_item['collection']}/items", json=test_item)
    get_item = app_client.get(
        f"/collections/{test_item['collection']}/items/{test_item['id']}",
        headers={
            "Forwarded": "proto=https;host=testserver:1234",
            "X-Forwarded-Port": "4321",
            "X-Forwarded-Proto": "http",
        },
    )
    for link in get_item.json()["links"]:
        assert link["href"].startswith("https://testserver:1234/")
