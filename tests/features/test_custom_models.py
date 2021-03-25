# from typing import Type
#
# import sqlalchemy as sa
# from starlette.testclient import TestClient
#
# # TODO: move these
# from stac_api.models.database import Item
# from stac_api.models.schemas import Collection
#
# from stac_fastapi.api.app import StacApi
# from stac_fastapi.extensions.core import TransactionExtension
# from stac_fastapi.postgres.core import CoreCrudClient, Session
# from stac_fastapi.postgres.transactions import TransactionsClient
# from stac_fastapi.postgres.config import PostgresSettings
#
#
# from ..conftest import MockStarletteRequest
#
#
# class CustomItem(Item):
#     foo = sa.Column(sa.VARCHAR(10))
#
#
# def create_app(item_model: Type[Item], db_session: Session) -> StacApi:
#     """Create application with a custom sqlalchemy item"""
#     api = StacApi(
#         settings=PostgresSettings(indexed_fields={"datetime", "foo"}),
#         extensions=[
#             TransactionExtension(
#                 client=TransactionsClient(item_table=item_model, session=db_session)
#             )
#         ],
#         client=CoreCrudClient(item_table=item_model, session=db_session),
#     )
#     return api
#
#
# def test_custom_item(load_test_data, postgres_transactions, db_session):
#     api = create_app(CustomItem, db_session)
#     transactions = TransactionsClient(item_table=CustomItem, session=db_session)
#
#     with TestClient(api.app) as test_client:
#         # Ingest a collection
#         coll = Collection.parse_obj(load_test_data("test_collection.json"))
#         transactions.create_collection(coll, request=MockStarletteRequest)
#
#         # Modify the table to match our custom item
#         # This would typically be done with alembic
#         db_session.writer.cached_engine.execute(
#             "ALTER TABLE data.items ADD COLUMN foo VARCHAR(10)"
#         )
#
#         # Post an item
#         test_item = load_test_data("test_item.json")
#         test_item["properties"]["foo"] = "hello"
#         resp = test_client.post(
#             f"/collections/{test_item['collection']}/items", json=test_item
#         )
#         assert resp.status_code == 200
#         assert resp.json()["properties"]["foo"] == "hello"
#
#         # Search for the item
#         body = {"query": {"foo": {"eq": "hello"}}}
#         resp = test_client.post("/search", json=body)
#         assert resp.status_code == 200
#         resp_json = resp.json()
#         assert len(resp_json["features"]) == 1
#         assert resp_json["features"][0]["properties"]["foo"] == "hello"
#
#         # Cleanup
#         transactions.delete_item(test_item["id"], request=MockStarletteRequest)
#         transactions.delete_collection(coll.id, request=MockStarletteRequest)
#         db_session.writer.cached_engine.execute(
#             "ALTER TABLE data.items DROP COLUMN foo"
#         )
