import uuid
from typing import Callable

import pytest
from stac_pydantic import Collection, Item
from tests.conftest import MockStarletteRequest

from stac_fastapi.extensions.third_party.bulk_transactions import Items
from stac_fastapi.sqlalchemy.core import CoreCrudClient
from stac_fastapi.sqlalchemy.transactions import (
    BulkTransactionsClient,
    TransactionsClient,
)
from stac_fastapi.types.errors import ConflictError, NotFoundError


def test_create_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = Collection.parse_obj(load_test_data("test_collection.json"))
    resp = postgres_transactions.create_collection(data, request=MockStarletteRequest)
    assert data.dict(exclude={"links"}) == resp.dict(exclude={"links"})
    coll = postgres_core.get_collection(data.id, request=MockStarletteRequest)
    assert coll.id == data.id


def test_create_collection_already_exists(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(data, request=MockStarletteRequest)

    with pytest.raises(ConflictError):
        postgres_transactions.create_collection(data, request=MockStarletteRequest)


def test_update_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(data, request=MockStarletteRequest)

    data.keywords.append("new keyword")
    postgres_transactions.update_collection(data, request=MockStarletteRequest)

    coll = postgres_core.get_collection(data.id, request=MockStarletteRequest)
    assert "new keyword" in coll.keywords


def test_delete_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(data, request=MockStarletteRequest)

    deleted = postgres_transactions.delete_collection(
        data.id, request=MockStarletteRequest
    )

    with pytest.raises(NotFoundError):
        postgres_core.get_collection(deleted.id, request=MockStarletteRequest)


def test_get_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(data, request=MockStarletteRequest)
    coll = postgres_core.get_collection(data.id, request=MockStarletteRequest)
    assert data.dict(exclude={"links"}) == coll.dict(exclude={"links"})
    assert coll.id == data.id


def test_get_collection_items(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = Item.parse_obj(load_test_data("test_item.json"))

    for _ in range(5):
        item.id = str(uuid.uuid4())
        postgres_transactions.create_item(item, request=MockStarletteRequest)

    fc = postgres_core.item_collection(coll.id, request=MockStarletteRequest)
    assert len(fc.features) == 5

    for item in fc.features:
        assert item.collection == coll.id


def test_create_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)
    item = Item.parse_obj(load_test_data("test_item.json"))
    postgres_transactions.create_item(item, request=MockStarletteRequest)
    resp = postgres_core.get_item(item.id, request=MockStarletteRequest)
    assert item.dict(
        exclude={"links": ..., "properties": {"created", "updated"}}
    ) == resp.dict(exclude={"links": ..., "properties": {"created", "updated"}})


def test_create_item_already_exists(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = Item.parse_obj(load_test_data("test_item.json"))
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    with pytest.raises(ConflictError):
        postgres_transactions.create_item(item, request=MockStarletteRequest)


def test_update_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = Item.parse_obj(load_test_data("test_item.json"))
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    item.properties.foo = "bar"
    postgres_transactions.update_item(item, request=MockStarletteRequest)

    updated_item = postgres_core.get_item(item.id, request=MockStarletteRequest)
    assert updated_item.properties.foo == "bar"


def test_delete_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = Item.parse_obj(load_test_data("test_item.json"))
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    postgres_transactions.delete_item(item.id, request=MockStarletteRequest)

    with pytest.raises(NotFoundError):
        postgres_core.get_item(item.id, request=MockStarletteRequest)


def test_bulk_item_insert(
    postgres_transactions: TransactionsClient,
    postgres_bulk_transactions: BulkTransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = Item.parse_obj(load_test_data("test_item.json"))

    items = []
    for _ in range(10):
        _item = item.dict()
        _item["id"] = str(uuid.uuid4())
        items.append(_item)

    postgres_bulk_transactions.bulk_item_insert(Items(items=items))

    for item in items:
        postgres_transactions.delete_item(item["id"], request=MockStarletteRequest)


def test_bulk_item_insert_chunked(
    postgres_transactions: TransactionsClient,
    postgres_bulk_transactions: BulkTransactionsClient,
    load_test_data: Callable,
):
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = Item.parse_obj(load_test_data("test_item.json"))

    items = []
    for _ in range(10):
        _item = item.dict()
        _item["id"] = str(uuid.uuid4())
        items.append(_item)

    postgres_bulk_transactions.bulk_item_insert(Items(items=items), chunk_size=2)

    for item in items:
        postgres_transactions.delete_item(item["id"], request=MockStarletteRequest)
