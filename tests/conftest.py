import json
import os
from contextlib import contextmanager
from typing import Callable, Dict, Generator, List, Type
from unittest.mock import MagicMock, Mock

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.config import environ
from starlette.testclient import TestClient

from stac_api.app import app
from stac_api.clients.base_crud import BaseCrudClient
from stac_api.clients.collection_crud import CollectionCrudClient
from stac_api.clients.item_crud import ItemCrudClient
from stac_api.clients.tokens import PaginationTokenClient
from stac_api.errors import NotFoundError
from stac_api.models import database, schemas
from stac_api.settings import settings

# This line would raise an error if we use it after 'settings' has been imported.
environ["TESTING"] = "true"
environ["DEBUG"] = "true"


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def create_mock(
    client: Type[BaseCrudClient], mocked_method: str, error: Exception
) -> MagicMock:
    """Create a mock client which raises an exception"""
    mock_client = MagicMock(client)
    setattr(mock_client, mocked_method, Mock(side_effect=error))
    return mock_client


@contextmanager
def create_test_client_with_error(
    client: Type[BaseCrudClient],
    mocked_method: str,
    dependency: Callable,
    error: Exception,
) -> Generator[TestClient, None, None]:
    """Inject a mock client into the test app"""
    app.dependency_overrides[dependency] = lambda: create_mock(
        client, mocked_method, error
    )
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides = {}


@pytest.fixture
def app_client(load_test_data):
    """
    Make a client fixture available to test cases.
    """
    test_collection = load_test_data("test_collection.json")
    with TestClient(app) as test_client:
        # Create collection
        test_client.post("/collections", json=test_collection)
        yield test_client

    # Cleanup test data
    collections = test_client.get("/collections").json()
    for coll in collections:
        collection_id = coll["id"]
        if "test" in collection_id:
            # Get collection items
            item_collection = test_client.get(
                f"/collections/{collection_id}/items", params={"limit": 500}
            ).json()
            for item in item_collection["features"]:
                test_client.delete(f"/collections/{collection_id}/items/{item['id']}")
            test_client.delete(f"/collections/{collection_id}")


@pytest.fixture
def load_test_data() -> Callable[[str], Dict]:
    def load_file(filename: str) -> Dict:
        with open(os.path.join(DATA_DIR, filename)) as file:
            return json.load(file)

    return load_file


def load_all_test_data(filter: str) -> List[Dict]:
    return [
        json.load(open(os.path.join(DATA_DIR, f)))
        for f in os.listdir(DATA_DIR)
        if filter in f
    ]


@pytest.fixture
def reader_connection() -> Generator[Session, None, None]:
    """Create a reader connection"""
    engine = create_engine(settings.reader_connection_string)
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    yield db_session
    db_session.close()
    engine.dispose()


@pytest.fixture
def writer_connection() -> Generator[Session, None, None]:
    """Create a writer connection"""
    engine = create_engine(settings.writer_connection_string)
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    yield db_session
    db_session.close()
    engine.dispose()


@pytest.fixture
def pagination_client(
    reader_connection: Session, writer_connection: Session
) -> PaginationTokenClient:
    """Create a pagination client"""
    return PaginationTokenClient(
        reader_session=reader_connection,
        writer_session=writer_connection,
        table=database.PaginationToken,
    )


@pytest.fixture
def collection_crud_client(
    reader_connection: Session,
    writer_connection: Session,
    pagination_client: PaginationTokenClient,
) -> Generator[CollectionCrudClient, None, None]:
    """Create a collection client.  Clean up data after each test. """
    client = CollectionCrudClient(
        reader_session=reader_connection,
        writer_session=writer_connection,
        table=database.Collection,
        pagination_client=pagination_client,
    )
    yield client

    # Cleanup collections
    for test_data in load_all_test_data("collection"):
        try:
            client.delete(test_data["id"])
        except NotFoundError:
            pass


@pytest.fixture
def item_crud_client(
    reader_connection: Session,
    writer_connection: Session,
    collection_crud_client: CollectionCrudClient,
    load_test_data,
) -> Generator[ItemCrudClient, None, None]:
    """Create an item client.  Create a collection used for testing and clean up data after each test."""
    # Create a test collection (foreignkey)
    test_collection = schemas.Collection(**load_test_data("test_collection.json"))
    collection_crud_client.create(test_collection)

    client = ItemCrudClient(
        reader_session=reader_connection,
        writer_session=writer_connection,
        table=database.Item,
        collection_crud=collection_crud_client,
        pagination_client=pagination_client,
    )
    yield client

    # Cleanup test items
    for test_data in load_all_test_data("item"):
        try:
            client.delete(test_data["id"])
        except NotFoundError:
            pass

    # Cleanup collection
    try:
        collection_crud_client.delete(test_collection.id)
    except NotFoundError:
        pass
