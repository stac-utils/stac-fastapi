import uuid
from copy import deepcopy
from typing import Callable

import pytest
from stac_pydantic import Item
from tests.conftest import MockStarletteRequest

from stac_fastapi.api.app import StacApi
from stac_fastapi.mongo.core import CoreCrudClient
from stac_fastapi.mongo.transactions import BulkTransactionsClient, TransactionsClient
from stac_fastapi.types.errors import ConflictError, NotFoundError


def test_create_collection(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    mongo_transactions.create_collection(data, request=MockStarletteRequest)
    coll = mongo_core.get_collection(data["id"], request=MockStarletteRequest)
    assert coll["id"] == data["id"]


def test_create_collection_already_exists(
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    mongo_transactions.create_collection(data, request=MockStarletteRequest)

    # change id to avoid mongo duplicate key error
    data["_id"] = str(uuid.uuid4())

    with pytest.raises(ConflictError):
        mongo_transactions.create_collection(data, request=MockStarletteRequest)


def test_update_collection(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")

    mongo_transactions.create_collection(data, request=MockStarletteRequest)
    data["keywords"].append("new keyword")
    mongo_transactions.update_collection(data, request=MockStarletteRequest)

    coll = mongo_core.get_collection(data["id"], request=MockStarletteRequest)
    assert "new keyword" in coll["keywords"]


def test_delete_collection(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    mongo_transactions.create_collection(data, request=MockStarletteRequest)

    mongo_transactions.delete_collection(data["id"], request=MockStarletteRequest)

    with pytest.raises(NotFoundError):
        mongo_core.get_collection(data["id"], request=MockStarletteRequest)


def test_get_collection(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    data = load_test_data("test_collection.json")
    mongo_transactions.create_collection(data, request=MockStarletteRequest)
    coll = mongo_core.get_collection(data["id"], request=MockStarletteRequest)
    assert coll["id"] == data["id"]


def test_get_item(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    collection_data = load_test_data("test_collection.json")
    item_data = load_test_data("test_item.json")
    mongo_transactions.create_collection(collection_data, request=MockStarletteRequest)
    mongo_transactions.create_item(item_data, request=MockStarletteRequest)
    coll = mongo_core.get_item(
        item_id=item_data["id"],
        collection_id=item_data["collection"],
        request=MockStarletteRequest,
    )
    assert coll["id"] == item_data["id"]
    assert coll["collection"] == item_data["collection"]


def test_get_collection_items(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")

    for _ in range(5):
        item["_id"] = str(uuid.uuid4())
        item["id"] = str(uuid.uuid4())
        mongo_transactions.create_item(item, request=MockStarletteRequest)

    fc = mongo_core.item_collection(coll["id"], request=MockStarletteRequest)
    assert len(fc["features"]) == 5

    for item in fc["features"]:
        assert item["collection"] == coll["id"]


def test_create_item(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)
    item = load_test_data("test_item.json")
    mongo_transactions.create_item(item, request=MockStarletteRequest)
    resp = mongo_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert Item(**item).dict(
        exclude={"links": ..., "properties": {"created", "updated"}}
    ) == Item(**resp).dict(exclude={"links": ..., "properties": {"created", "updated"}})


def test_create_item_already_exists(
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    mongo_transactions.create_item(item, request=MockStarletteRequest)

    with pytest.raises(ConflictError):
        mongo_transactions.create_item(item, request=MockStarletteRequest)


def test_update_item(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    mongo_transactions.create_item(item, request=MockStarletteRequest)

    item["properties"]["foo"] = "bar"
    mongo_transactions.update_item(item, request=MockStarletteRequest)

    updated_item = mongo_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert updated_item["properties"]["foo"] == "bar"


def test_update_geometry(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    mongo_transactions.create_item(item, request=MockStarletteRequest)

    new_coordinates = [
        [
            [142.15052873427666, -33.82243006904891],
            [140.1000346138806, -34.257132625788756],
            [139.5776607193635, -32.514709769700254],
            [141.6262528041627, -32.08081674221862],
            [142.15052873427666, -33.82243006904891],
        ]
    ]

    item["geometry"]["coordinates"] = new_coordinates
    mongo_transactions.update_item(item, request=MockStarletteRequest)

    updated_item = mongo_core.get_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )
    assert updated_item["geometry"]["coordinates"] == new_coordinates


def test_delete_item(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")
    mongo_transactions.create_item(item, request=MockStarletteRequest)

    mongo_transactions.delete_item(
        item["id"], item["collection"], request=MockStarletteRequest
    )

    with pytest.raises(NotFoundError):
        mongo_core.get_item(
            item["id"], item["collection"], request=MockStarletteRequest
        )


def test_bulk_item_insert(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    mongo_bulk_transactions: BulkTransactionsClient,
    load_test_data: Callable,
):
    coll = load_test_data("test_collection.json")
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    item = load_test_data("test_item.json")

    items = []
    for _ in range(10):
        _item = deepcopy(item)
        _item["id"] = str(uuid.uuid4())
        items.append(_item)

    fc = mongo_core.item_collection(coll["id"], request=MockStarletteRequest)
    assert len(fc["features"]) == 0

    mongo_bulk_transactions.bulk_item_insert(items=items)

    fc = mongo_core.item_collection(coll["id"], request=MockStarletteRequest)
    assert len(fc["features"]) == 10

    for item in items:
        mongo_transactions.delete_item(
            item["id"], item["collection"], request=MockStarletteRequest
        )


@pytest.mark.skip(reason="Not working")
def test_landing_page_no_collection_title(
    mongo_core: CoreCrudClient,
    mongo_transactions: TransactionsClient,
    load_test_data: Callable,
    api_client: StacApi,
):
    class MockStarletteRequestWithApp(MockStarletteRequest):
        app = api_client.app

    coll = load_test_data("test_collection.json")
    del coll["title"]
    mongo_transactions.create_collection(coll, request=MockStarletteRequest)

    landing_page = mongo_core.landing_page(request=MockStarletteRequestWithApp)
    for link in landing_page["links"]:
        if link["href"].split("/")[-1] == coll["id"]:
            assert link["title"]
