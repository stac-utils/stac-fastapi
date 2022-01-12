import json
import os
from typing import Callable, Dict

import pytest
from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_request_model
from stac_fastapi.extensions.core import (
    ContextExtension,
    FieldsExtension,
    SortExtension,
    TokenPaginationExtension,
    TransactionExtension,
)
from stac_fastapi.mongo.config import MongoSettings
from stac_fastapi.mongo.core import CoreCrudClient
from stac_fastapi.mongo.extensions import QueryExtension
from stac_fastapi.mongo.transactions import BulkTransactionsClient, TransactionsClient
from stac_fastapi.types.config import Settings
from stac_fastapi.types.search import BaseSearchGetRequest, BaseSearchPostRequest

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


class TestSettings(MongoSettings):
    class Config:
        env_file = ".env.test"


settings = TestSettings()
Settings.set(settings)


@pytest.fixture(autouse=True)
def cleanup(mongo_core: CoreCrudClient, mongo_transactions: TransactionsClient):
    yield
    collections = mongo_core.all_collections(request=MockStarletteRequest)
    for coll in collections["collections"]:
        if coll["id"].split("-")[0] == "test":
            # Delete the items
            items = mongo_core.item_collection(
                coll["id"], limit=100, request=MockStarletteRequest
            )
            for feat in items["features"]:
                mongo_transactions.delete_item(
                    feat["id"], feat["collection"], request=MockStarletteRequest
                )

            # Delete the collection
            mongo_transactions.delete_collection(
                coll["id"], request=MockStarletteRequest
            )


@pytest.fixture
def load_test_data() -> Callable[[str], Dict]:
    def load_file(filename: str) -> Dict:
        with open(os.path.join(DATA_DIR, filename)) as file:
            return json.load(file)

    return load_file


class MockStarletteRequest:
    base_url = "http://test-server"


# @pytest.fixture
# def db_session() -> Session:
#     return Session(
#         reader_conn_string=settings.reader_connection_string,
#         writer_conn_string=settings.writer_connection_string,
#     )


@pytest.fixture
def mongo_core():
    return CoreCrudClient(session=None)


@pytest.fixture
def mongo_transactions():
    return TransactionsClient(session=None)


@pytest.fixture
def mongo_bulk_transactions():
    return BulkTransactionsClient(session=None)


@pytest.fixture
def api_client():
    settings = MongoSettings()
    extensions = [
        TransactionExtension(
            client=TransactionsClient(session=None), settings=settings
        ),
        ContextExtension(),
        SortExtension(),
        FieldsExtension(),
        QueryExtension(),
        TokenPaginationExtension(),
    ]

    get_request_model = create_request_model(
        "SearchGetRequest",
        base_model=BaseSearchGetRequest,
        extensions=extensions,
        request_type="GET",
    )

    post_request_model = create_request_model(
        "SearchPostRequest",
        base_model=BaseSearchPostRequest,
        extensions=extensions,
        request_type="POST",
    )

    return StacApi(
        settings=settings,
        client=CoreCrudClient(
            session=None,
            extensions=extensions,
            post_request_model=post_request_model,
        ),
        extensions=extensions,
        search_get_request_model=get_request_model,
        search_post_request_model=post_request_model,
    )


@pytest.fixture
def app_client(api_client, load_test_data):
    coll = load_test_data("test_collection.json")
    client = TransactionsClient(
        session=None,
    )
    client.create_collection(coll, request=MockStarletteRequest)

    with TestClient(api_client.app) as test_app:
        yield test_app
