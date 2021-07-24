from typing import Callable

import pystac
import pytest
from stac_pydantic import Collection


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
async def test_create_collection_conflict(app_client, load_test_data: Callable):
    in_json = load_test_data("test_collection.json")
    Collection.parse_obj(in_json)
    resp = await app_client.post(
        "/collections",
        json=in_json,
    )
    assert resp.status_code == 200
    Collection.parse_obj(resp.json())
    resp = await app_client.post(
        "/collections",
        json=in_json,
    )
    assert resp.status_code == 409


@pytest.mark.asyncio
async def test_delete_missing_collection(
    app_client,
):
    resp = await app_client.delete("/collections")
    assert resp.status_code == 405


@pytest.mark.asyncio
async def test_update_new_collection(app_client, load_test_collection):
    in_coll = load_test_collection
    in_coll.id = "test-updatenew"

    resp = await app_client.put("/collections", json=in_coll.dict())
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_nocollections(
    app_client,
):
    resp = await app_client.get("/collections")
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_returns_valid_collection(app_client, load_test_data):
    """Test updating a collection which already exists"""
    in_json = load_test_data("test_collection.json")
    resp = await app_client.post(
        "/collections",
        json=in_json,
    )
    assert resp.status_code == 200

    resp = await app_client.get(f"/collections/{in_json['id']}")
    assert resp.status_code == 200
    resp_json = resp.json()

    # Mock root to allow validation
    mock_root = pystac.Catalog(
        id="test", description="test desc", href="https://example.com"
    )
    collection = pystac.Collection.from_dict(
        resp_json, root=mock_root, preserve_dict=False
    )
    collection.validate()
