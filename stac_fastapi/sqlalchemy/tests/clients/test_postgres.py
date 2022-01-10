import uuid
from copy import deepcopy
from typing import Callable

import pytest
from stac_pydantic import Collection, Item
from tests.conftest import MockStarletteRequest

from stac_fastapi.api.app import StacApi
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
    data = load_test_data("test_collection.json")
    resp = postgres_transactions.create_collection(data, request=MockStarletteRequest)
    assert Collection(**data).dict(exclude={"links"}) == Collection(**resp).dict(
        exclude={"links"}
    )
    coll = postgres_core.get_collection(data["id"], request=MockStarletteRequest)
    assert coll["id"] == data["id"]


def test_create_collection_already_exists(
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    postgres_transactions.create_collection(data, request=MockStarletteRequest)

    with pytest.raises(ConflictError):
        postgres_transactions.create_collection(data, request=MockStarletteRequest)


def test_update_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    postgres_transactions.create_collection(data, request=MockStarletteRequest)

    data["keywords"].append("new keyword")
    postgres_transactions.update_collection(data, request=MockStarletteRequest)

    coll = postgres_core.get_collection(data["id"], request=MockStarletteRequest)
    assert "new keyword" in coll["keywords"]


def test_delete_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    postgres_transactions.create_collection(data, request=MockStarletteRequest)

    deleted = postgres_transactions.delete_collection(
        data["id"], request=MockStarletteRequest
    )

    with pytest.raises(NotFoundError):
        postgres_core.get_collection(deleted["id"], request=MockStarletteRequest)


def test_get_collection(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    postgres_transactions.create_collection(data, request=MockStarletteRequest)
    coll = postgres_core.get_collection(data["id"], request=MockStarletteRequest)
    assert Collection(**data).dict(exclude={"links"}) == Collection(**coll).dict(
        exclude={"links"}
    )
    assert coll["id"] == data["id"]


def test_get_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    collection_data = load_test_data("test_collection.json")
    postgres_transactions.create_collection(
        collection_data, request=MockStarletteRequest
    )
    data = load_test_data("test_item.json")
    postgres_transactions.create_item(data, request=MockStarletteRequest)
    coll = postgres_core.get_item(
        item_id=data["id"],
        collection_id=data["collection"],
        request=MockStarletteRequest,
    )
    assert coll["id"] == data["id"]
    assert coll["collection"] == data["collection"]


def test_get_collection_items(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")

    for _ in range(5):
        item["id"] = str(uuid.uuid4())
        postgres_transactions.create_item(item, request=MockStarletteRequest)

    fc = postgres_core.item_collection(coll["id"], request=MockStarletteRequest)
    assert len(fc["features"]) == 5

    for item in fc["features"]:
        assert item["collection"] == coll["id"]


def test_create_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)
    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)
    resp = postgres_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert Item(**item).dict(
        exclude={"links": ..., "properties": {"created", "updated"}}
    ) == Item(**resp).dict(exclude={"links": ..., "properties": {"created", "updated"}})


def test_create_item_already_exists(
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    with pytest.raises(ConflictError):
        postgres_transactions.create_item(item, request=MockStarletteRequest)


def test_create_duplicate_item_different_collections(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    # create test-collection
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    # create test-collection-2
    coll["id"] = "test-collection-2"
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    # add item to test-collection
    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    # get item from test-collection
    resp = postgres_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert Item(**item).dict(
        exclude={"links": ..., "properties": {"created", "updated"}}
    ) == Item(**resp).dict(exclude={"links": ..., "properties": {"created", "updated"}})

    # add item to test-collection-2
    item["collection"] = "test-collection-2"
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    # get item with same id from test-collection-2
    resp = postgres_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert Item(**item).dict(
        exclude={"links": ..., "properties": {"created", "updated"}}
    ) == Item(**resp).dict(exclude={"links": ..., "properties": {"created", "updated"}})


def test_update_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    item["properties"]["foo"] = "bar"
    postgres_transactions.update_item(item, request=MockStarletteRequest)

    updated_item = postgres_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert updated_item["properties"]["foo"] == "bar"


def test_update_geometry(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    item["geometry"]["coordinates"] = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
    postgres_transactions.update_item(item, request=MockStarletteRequest)

    updated_item = postgres_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert updated_item["geometry"]["coordinates"] == item["geometry"]["coordinates"]


def test_delete_item(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    postgres_transactions.create_item(item, request=MockStarletteRequest)

    postgres_transactions.delete_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )

    with pytest.raises(NotFoundError):
        postgres_core.get_item(
            item["id"], item["collection"], request=MockStarletteRequest
        )


def test_bulk_item_insert(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    postgres_bulk_transactions: BulkTransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")

    items = []
    for _ in range(10):
        _item = deepcopy(item)
        _item["id"] = str(uuid.uuid4())
        items.append(_item)

    fc = postgres_core.item_collection(coll["id"], request=MockStarletteRequest)
    assert len(fc["features"]) == 0

    postgres_bulk_transactions.bulk_item_insert(items=items)

    fc = postgres_core.item_collection(coll["id"], request=MockStarletteRequest)
    assert len(fc["features"]) == 10

    for item in items:
        postgres_transactions.delete_item(
            item["id"], item["collection"], request=MockStarletteRequest
        )


def test_bulk_item_insert_chunked(
    postgres_transactions: TransactionsClient,
    postgres_bulk_transactions: BulkTransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")

    items = []
    for _ in range(10):
        _item = deepcopy(item)
        _item["id"] = str(uuid.uuid4())
        items.append(_item)

    postgres_bulk_transactions.bulk_item_insert(items=items, chunk_size=2)

    for item in items:
        postgres_transactions.delete_item(
            item["id"], item["collection"], request=MockStarletteRequest
        )


def test_landing_page_no_collection_title(
    postgres_core: CoreCrudClient,
    postgres_transactions: TransactionsClient,
    load_test_data: Callable,
    api_client: StacApi,
):
    class MockStarletteRequestWithApp(MockStarletteRequest):
        app = api_client.app

    coll = load_test_data("test_collection.json")
    del coll["title"]
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    landing_page = postgres_core.landing_page(request=MockStarletteRequestWithApp)
    for link in landing_page["links"]:
        if link["href"].split("/")[-1] == coll["id"]:
            assert link["title"]
