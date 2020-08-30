import json
import os
from typing import Callable, Dict, Generator
from unittest.mock import PropertyMock, patch

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from starlette.testclient import TestClient

from stac_api.api import create_app
from stac_api.clients.postgres.core import CoreCrudClient
from stac_api.clients.postgres.transactions import TransactionsClient
from stac_api.config import ApiSettings, inject_settings
from stac_api.models.schemas import Collection

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


class TestSettings(ApiSettings):
    class Config:
        env_file = ".env.test"


settings = TestSettings(
    stac_api_extensions=["context", "fields", "query", "sort", "transaction"],
)
inject_settings(settings)


@pytest.fixture(autouse=True)
def cleanup(postgres_core: CoreCrudClient, postgres_transactions: TransactionsClient):
    yield
    collections = postgres_core.all_collections(request=MockStarletteRequest)
    for coll in collections:
        if coll.id.split("-")[0] == "test":
            # Delete the items
            items = postgres_core.item_collection(
                coll.id, limit=100, request=MockStarletteRequest
            )
            for feat in items.features:
                postgres_transactions.delete_item(feat.id, request=MockStarletteRequest)

            # Delete the collection
            postgres_transactions.delete_collection(
                coll.id, request=MockStarletteRequest
            )


@pytest.fixture
def load_test_data() -> Callable[[str], Dict]:
    def load_file(filename: str) -> Dict:
        with open(os.path.join(DATA_DIR, filename)) as file:
            return json.load(file)

    return load_file


class MockStarletteRequest:
    base_url = "http://test-server"


@pytest.fixture
def reader_connection() -> Generator[Session, None, None]:
    """Create a reader connection"""
    engine = create_engine(settings.reader_connection_string, echo=True)
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    yield db_session
    db_session.close()
    engine.dispose()


@pytest.fixture
def writer_connection() -> Generator[Session, None, None]:
    """Create a writer connection"""
    engine = create_engine(settings.writer_connection_string, echo=True)
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    yield db_session
    db_session.close()
    engine.dispose()


@pytest.fixture
def postgres_core(reader_connection, writer_connection):
    with patch(
        "stac_api.clients.postgres.base.PostgresClient.writer_session",
        new_callable=PropertyMock,
    ) as mock_writer:
        mock_writer.return_value = writer_connection
        with patch(
            "stac_api.clients.postgres.base.PostgresClient.reader_session",
            new_callable=PropertyMock,
        ) as mock_reader:
            mock_reader.return_value = reader_connection
            client = CoreCrudClient()
            yield client


@pytest.fixture
def postgres_transactions(reader_connection, writer_connection):
    with patch(
        "stac_api.clients.postgres.base.PostgresClient.writer_session",
        new_callable=PropertyMock,
    ) as mock_writer:
        mock_writer.return_value = writer_connection
        with patch(
            "stac_api.clients.postgres.base.PostgresClient.reader_session",
            new_callable=PropertyMock,
        ) as mock_reader:
            mock_reader.return_value = reader_connection
            client = TransactionsClient()
            yield client


@pytest.fixture
def app_client(load_test_data, postgres_transactions):
    app = create_app(settings)
    coll = Collection.parse_obj(load_test_data("test_collection.json"))
    postgres_transactions.create_collection(coll, request=MockStarletteRequest)

    with TestClient(app) as test_app:
        yield test_app
