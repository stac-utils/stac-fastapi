# from random import randint
#
# import pytest
# from sqlalchemy.orm import Session
#
# from psycopg2._psycopg import sqlstate_errors
# from stac_api.clients.postgres.base import PostgresClient
# from stac_api.clients.postgres.collection import CollectionCrudClient
# from stac_api.clients.postgres.transactions import TransactionsClient
# from stac_api.errors import ConflictError, DatabaseError, ForeignKeyError, NotFoundError
# from stac_api.models import database
# from stac_api.models.schemas import Collection, Item
#
# from ..conftest import create_mock
#
# def random_pg_exception():
#     """Generate a random psycopg2 exception"""
#     pg_errors = list(sqlstate_errors)
#     return sqlstate_errors[pg_errors[randint(0, len(pg_errors) - 1)]]
#
#
# def test_create_and_delete_item(transaction_client, load_test_data):
#     """Test creation and deletion of a single item"""
#     test_item = Item(**load_test_data("test_item.json"))
#     row_data = transaction_client.create_item(test_item)
#     assert test_item.id == row_data.id
#
#     deleted_item = transaction_client.delete_item(test_item.id)
#     assert deleted_item.id == test_item.id
#
#
# def test_create_item_already_exists(transaction_client, load_test_data):
#     """Test creation of an item which already exists"""
#     test_item = Item(**load_test_data("test_item.json"))
#     row_data = transaction_client.create_item(test_item)
#     assert test_item.id == row_data.id
#
#     with pytest.raises(ConflictError):
#         test_item_duplicate = Item(**load_test_data("test_item.json"))
#         transaction_client.create_item(test_item_duplicate)
#
#
# def test_delete_missing_item(transaction_client):
#     """Test deletion of an item which does not exist"""
#     with pytest.raises(NotFoundError):
#         transaction_client.delete_item("this id doesn't exist")
#
#
# def test_create_item_missing_collection(transaction_client, load_test_data):
#     """Test creation of an item without a parent collection"""
#     test_item = Item(**load_test_data("test_item.json"))
#     test_item.collection = "this collection doesn't exist"
#     with pytest.raises(ForeignKeyError):
#         transaction_client.create_item(test_item)
#
#
# def test_update_item_already_exists(transaction_client, load_test_data):
#     """Test updating an item"""
#     test_item = Item(**load_test_data("test_item.json"))
#     transaction_client.create_item(test_item)
#
#     test_item = Item(**load_test_data("test_item.json"))
#     test_item.properties.new_prop = "test"
#     updated_row = transaction_client.update_item(test_item)
#
#     assert updated_row.properties["new_prop"] == "test"
#
#
# def test_update_new_item(transaction_client, load_test_data):
#     """Test updating an item which doesn't exist (same as creation)"""
#     test_item = Item(**load_test_data("test_item.json"))
#     row_data = transaction_client.update_item(test_item)
#     assert test_item.id == row_data.id
#
#
# def test_create_and_delete_collection(transaction_client, load_test_data):
#     """Test creation and deletion of a collection"""
#     test_collection = Collection(**load_test_data("test_collection.json"))
#     test_collection.id = "test-coll"
#     row_data = transaction_client.create_collection(test_collection)
#     assert test_collection.id == row_data.id
#
#     deleted_collection = transaction_client.delete_collection(test_collection.id)
#     assert deleted_collection.id == test_collection.id
#
#
# def test_create_collection_conflict(transaction_client, load_test_data):
#     """Test creation of a collection which already exists"""
#     test_collection = Collection(**load_test_data("test_collection.json"))
#     test_collection.id = "123-test"
#     row_data = transaction_client.create_collection(test_collection)
#     assert test_collection.id == row_data.id
#
#     with pytest.raises(ConflictError):
#         test_collection = Collection(**load_test_data("test_collection.json"))
#         transaction_client.create_collection(test_collection)
#
#     transaction_client.delete_collection("123-test")
#
#
# def test_delete_missing_collection(transaction_client):
#     """Test deletion of a collection which does not exist"""
#     with pytest.raises(NotFoundError):
#         transaction_client.delete_collection("this id also doesn't exist")
#
#
# def test_update_collection_already_exists(transaction_client, load_test_data):
#     """Test updating a collection which already exists"""
#     test_collection = Collection(**load_test_data("test_collection.json"))
#     test_collection.id = "testing-collection"
#     transaction_client.create_collection(test_collection)
#
#     test_collection = Collection(**load_test_data("test_collection.json"))
#     test_collection.id = "testing-collection"
#     test_collection.keywords.append("new keyword")
#     updated_row = transaction_client.update_collection(test_collection)
#
#     assert "new keyword" in updated_row.keywords
#
#     transaction_client.delete_collection(test_collection.id)
#
#
# def test_update_new_collection(transaction_client, load_test_data):
#     """Test update a collection which does not exist (same as creation)"""
#     test_collection = Collection(**load_test_data("test_collection.json"))
#     row_data = transaction_client.update_collection(test_collection)
#     assert test_collection.id == row_data.id


# def test_read_database_error():
#     """Test custom exception is raised on psycopg2 errors"""
#     mock_session = create_mock(
#         client=Session, mocked_method="query", error=random_pg_exception()
#     )
#     crud_client = PostgresClient(
#         reader_session=mock_session, writer_session=mock_session, table=database.Item
#     )
#
#     with pytest.raises(DatabaseError):
#         crud_client.read("test-item")
#
#
# def test_update_database_error(load_test_data):
#     """Test custom exception is raised on psycopg2 errors"""
#     test_item = Item(**load_test_data("test_item.json"))
#     mock_session = create_mock(
#         client=Session, mocked_method="commit", error=random_pg_exception()
#     )
#     crud_client = TransactionsClient(
#         reader_session=mock_session,
#         writer_session=mock_session,
#         table=database.Collection,
#         item_table=database.Item,
#     )
#
#     with pytest.raises(DatabaseError):
#         crud_client.update_item(test_item)
#
#
# def test_create_database_error(load_test_data):
#     """Test custom exception is raised on psycopg2 errors"""
#     test_item = Item(**load_test_data("test_item.json"))
#     mock_session = create_mock(
#         client=Session, mocked_method="query", error=random_pg_exception()
#     )
#     crud_client = TransactionsClient(
#         reader_session=mock_session,
#         writer_session=mock_session,
#         table=database.Collection,
#         item_table=database.Item,
#     )
#
#     with pytest.raises(DatabaseError):
#         crud_client.create_item(test_item)
#
#
# def test_get_all_collections_database_error(pagination_client):
#     """Test custom exception is raised on psycopg2 errors"""
#     mock_session = create_mock(
#         client=Session, mocked_method="query", error=random_pg_exception()
#     )
#     crud_client = CollectionCrudClient(
#         reader_session=mock_session,
#         writer_session=mock_session,
#         table=database.Collection,
#         pagination_client=pagination_client,
#     )
#     with pytest.raises(DatabaseError):
#         crud_client.all_collections()
#
#
# def test_get_item_collection_database_error(load_test_data, pagination_client):
#     """Test custom exception is raised on psycopg2 errors"""
#     test_coll = Collection(**load_test_data("test_collection.json"))
#     mock_session = create_mock(
#         client=Session, mocked_method="query", error=random_pg_exception()
#     )
#     crud_client = CollectionCrudClient(
#         reader_session=mock_session,
#         writer_session=mock_session,
#         table=database.Collection,
#         pagination_client=pagination_client,
#     )
#     with pytest.raises(DatabaseError):
#         crud_client.item_collection(test_coll.id, limit=10)
