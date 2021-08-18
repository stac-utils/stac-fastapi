import uuid
from typing import Callable

import pytest
from stac_pydantic import Collection, Item

# from tests.conftest import MockStarletteRequest


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
async def test_update_collection(app_client, load_test_collection):
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
async def test_delete_collection(app_client, load_test_collection):
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
async def test_update_item(app_client, load_test_collection, load_test_item):
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
async def test_delete_item(app_client, load_test_collection, load_test_item):
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


# TODO since right now puts implement upsert
# test_create_collection_already_exists
# test create_item_already_exists


# def test_get_collection_items(
#     postgres_core: CoreCrudClient,
#     postgres_transactions: TransactionsClient,
#     load_test_data: Callable,
# ):
#     coll = Collection.parse_obj(load_test_data("test_collection.json"))
#     postgres_transactions.create_collection(coll, request=MockStarletteRequest)

#     item = Item.parse_obj(load_test_data("test_item.json"))

#     for _ in range(5):
#         item.id = str(uuid.uuid4())
#         postgres_transactions.create_item(item, request=MockStarletteRequest)

#     fc = postgres_core.item_collection(coll.id, request=MockStarletteRequest)
#     assert len(fc.features) == 5

#     for item in fc.features:
#         assert item.collection == coll.id
