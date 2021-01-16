from typing import Type

import sqlalchemy as sa
from starlette.testclient import TestClient

from stac_api.api.app import StacApi
from stac_api.api.extensions import TransactionExtension
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.config import ApiSettings
from stac_api.models.database import Item
from stac_api.models.schemas import Collection

from ..conftest import MockStarletteRequest


class CustomItem(Item):
    foo = sa.Column(sa.VARCHAR(10))


def create_app(item_model: Type[Item]) -> StacApi:
    """Create application with a custom sqlalchemy item"""
    api = StacApi(
        settings=ApiSettings(indexed_fields={"datetime", "foo"}),
        extensions=[
            TransactionExtension(client=TransactionsClient(item_table=item_model))
        ],
        client=CoreCrudClient(
            table=item_model, pagination_client=PaginationTokenClient()
        ),
    )
    return api


def test_custom_item(load_test_data, postgres_transactions):
    api = create_app(CustomItem)
    transactions = TransactionsClient(item_table=CustomItem)

    with TestClient(api.app) as test_client:
        test_app = test_client.app

        # Ingest a collection
        coll = Collection.parse_obj(load_test_data("test_collection.json"))
        transactions.create_collection(coll, request=MockStarletteRequest)

        # Modify the table to match our custom item
        # This would typically be done with alembic
        test_app.state.ENGINE_WRITER.execute(
            "ALTER TABLE data.items ADD COLUMN foo VARCHAR(10)"
        )

        # Post an item
        test_item = load_test_data("test_item.json")
        test_item["properties"]["foo"] = "hello"
        resp = test_client.post(
            f"/collections/{test_item['collection']}/items", json=test_item
        )
        assert resp.status_code == 200
        assert resp.json()["properties"]["foo"] == "hello"

        # Search for the item
        body = {"query": {"foo": {"eq": "hello"}}}
        resp = test_client.post("/search", json=body)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert len(resp_json["features"]) == 1
        assert resp_json["features"][0]["properties"]["foo"] == "hello"

        # Cleanup
        transactions.delete_item(test_item["id"], request=MockStarletteRequest)
        transactions.delete_collection(coll.id, request=MockStarletteRequest)
        test_app.state.ENGINE_WRITER.execute("ALTER TABLE data.items DROP COLUMN foo")
