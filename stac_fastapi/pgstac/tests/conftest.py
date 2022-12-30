import asyncio
import json
import os
import time
from typing import Callable, Dict
from urllib.parse import urljoin

import asyncpg
import pytest
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from httpx import AsyncClient
from pypgstac.db import PgstacDB
from pypgstac.migrate import Migrate
from stac_pydantic import Collection, Item

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import create_get_request_model, create_post_request_model
from stac_fastapi.extensions.core import (
    ContextExtension,
    FieldsExtension,
    FilterExtension,
    SortExtension,
    TokenPaginationExtension,
    TransactionExtension,
)
from stac_fastapi.extensions.third_party import BulkTransactionExtension
from stac_fastapi.pgstac.config import Settings
from stac_fastapi.pgstac.core import CoreCrudClient
from stac_fastapi.pgstac.db import close_db_connection, connect_to_db
from stac_fastapi.pgstac.extensions import QueryExtension
from stac_fastapi.pgstac.extensions.filter import FiltersClient
from stac_fastapi.pgstac.transactions import BulkTransactionsClient, TransactionsClient
from stac_fastapi.pgstac.types.search import PgstacSearch

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

settings = Settings(testing=True)
pgstac_api_hydrate_settings = Settings(testing=True, use_api_hydrate=True)


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
async def pg():
    print(f"Connecting to write database {settings.writer_connection_string}")
    os.environ["orig_postgres_dbname"] = settings.postgres_dbname
    conn = await asyncpg.connect(dsn=settings.writer_connection_string)
    try:
        await conn.execute("CREATE DATABASE pgstactestdb;")
        await conn.execute(
            """
            ALTER DATABASE pgstactestdb SET search_path to pgstac, public;
            ALTER DATABASE pgstactestdb SET log_statement to 'all';
            """
        )
    except asyncpg.exceptions.DuplicateDatabaseError:
        await conn.execute("DROP DATABASE pgstactestdb;")
        await conn.execute("CREATE DATABASE pgstactestdb;")
        await conn.execute(
            "ALTER DATABASE pgstactestdb SET search_path to pgstac, public;"
        )
    await conn.close()
    print("migrating...")
    os.environ["postgres_dbname"] = "pgstactestdb"
    conn = await asyncpg.connect(dsn=settings.testing_connection_string)
    val = await conn.fetchval("SELECT true")
    print(val)
    await conn.close()
    db = PgstacDB(dsn=settings.testing_connection_string)
    migrator = Migrate(db)
    version = migrator.run_migration()
    db.close()
    print(f"PGStac Migrated to {version}")

    yield settings.testing_connection_string

    print("Getting rid of test database")
    os.environ["postgres_dbname"] = os.environ["orig_postgres_dbname"]
    conn = await asyncpg.connect(dsn=settings.writer_connection_string)
    try:
        await conn.execute("DROP DATABASE pgstactestdb;")
        await conn.close()
    except Exception:
        try:
            await conn.execute("DROP DATABASE pgstactestdb WITH (force);")
            await conn.close()
        except Exception:
            pass


@pytest.fixture(autouse=True)
async def pgstac(pg):
    print(f"{os.environ['postgres_dbname']}")
    yield
    print("Truncating Data")
    conn = await asyncpg.connect(dsn=settings.testing_connection_string)
    await conn.execute(
        """
        DROP SCHEMA IF EXISTS pgstac CASCADE;
        """
    )
    await conn.close()
    with PgstacDB(dsn=settings.testing_connection_string) as db:
        migrator = Migrate(db)
        version = migrator.run_migration()
    print(f"PGStac Migrated to {version}")


# Run all the tests that use the api_client in both db hydrate and api hydrate mode
@pytest.fixture(
    params=[
        (settings, ""),
        (settings, "/router_prefix"),
        (pgstac_api_hydrate_settings, ""),
        (pgstac_api_hydrate_settings, "/router_prefix"),
    ],
    scope="session",
)
def api_client(request, pg):
    api_settings, prefix = request.param

    api_settings.openapi_url = prefix + api_settings.openapi_url
    api_settings.docs_url = prefix + api_settings.docs_url

    print(
        "creating client with settings, hydrate: {}, router prefix: '{}'".format(
            api_settings.use_api_hydrate, prefix
        )
    )

    extensions = [
        TransactionExtension(client=TransactionsClient(), settings=settings),
        QueryExtension(),
        SortExtension(),
        FieldsExtension(),
        TokenPaginationExtension(),
        ContextExtension(),
        FilterExtension(client=FiltersClient()),
        BulkTransactionExtension(client=BulkTransactionsClient()),
    ]

    post_request_model = create_post_request_model(extensions, base_model=PgstacSearch)
    api = StacApi(
        settings=api_settings,
        extensions=extensions,
        client=CoreCrudClient(post_request_model=post_request_model),
        search_get_request_model=create_get_request_model(extensions),
        search_post_request_model=post_request_model,
        response_class=ORJSONResponse,
        router=APIRouter(prefix=prefix),
    )

    return api


@pytest.fixture(scope="function")
async def app(api_client):
    print("Creating app Fixture")
    time.time()
    app = api_client.app
    await connect_to_db(app)

    yield app

    await close_db_connection(app)

    print("Closed Pools.")


@pytest.fixture(scope="function")
async def app_client(app):
    print("creating app_client")

    base_url = "http://test"
    if app.state.router_prefix != "":
        base_url = urljoin(base_url, app.state.router_prefix)

    async with AsyncClient(app=app, base_url=base_url) as c:
        yield c


@pytest.fixture
def load_test_data() -> Callable[[str], Dict]:
    def load_file(filename: str) -> Dict:
        with open(os.path.join(DATA_DIR, filename)) as file:
            return json.load(file)

    return load_file


@pytest.fixture
async def load_test_collection(app_client, load_test_data):
    data = load_test_data("test_collection.json")
    resp = await app_client.post(
        "/collections",
        json=data,
    )
    assert resp.status_code == 200
    return Collection.parse_obj(resp.json())


@pytest.fixture
async def load_test_item(app_client, load_test_data, load_test_collection):
    coll = load_test_collection
    data = load_test_data("test_item.json")
    resp = await app_client.post(
        f"/collections/{coll.id}/items",
        json=data,
    )
    assert resp.status_code == 200
    return Item.parse_obj(resp.json())


@pytest.fixture
async def load_test2_collection(app_client, load_test_data):
    data = load_test_data("test2_collection.json")
    resp = await app_client.post(
        "/collections",
        json=data,
    )
    assert resp.status_code == 200
    return Collection.parse_obj(resp.json())


@pytest.fixture
async def load_test2_item(app_client, load_test_data, load_test2_collection):
    coll = load_test2_collection
    data = load_test_data("test2_item.json")
    resp = await app_client.post(
        f"/collections/{coll.id}/items",
        json=data,
    )
    assert resp.status_code == 200
    return Item.parse_obj(resp.json())
