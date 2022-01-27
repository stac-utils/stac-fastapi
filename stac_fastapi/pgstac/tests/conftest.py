import asyncio
import json
import os
from typing import Callable, Dict, Optional

import asyncpg
import pytest
from fastapi.responses import ORJSONResponse
from httpx import AsyncClient
from pypgstac import pypgstac
from stac_pydantic import Collection, Item

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.middleware import MiddlewareConfig
from stac_fastapi.api.models import create_get_request_model, create_post_request_model
from stac_fastapi.extensions.core import (
    FieldsExtension,
    FilterExtension,
    SortExtension,
    TokenPaginationExtension,
    TransactionExtension,
)
from stac_fastapi.pgstac.config import Settings
from stac_fastapi.pgstac.core import CoreCrudClient
from stac_fastapi.pgstac.db import close_db_connection, connect_to_db
from stac_fastapi.pgstac.extensions import QueryExtension
from stac_fastapi.pgstac.transactions import TransactionsClient
from stac_fastapi.pgstac.types.search import PgstacSearch

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

settings = Settings(testing=True)


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
    version = await pypgstac.run_migration(dsn=settings.testing_connection_string)
    print(f"PGStac Migrated to {version}")

    yield settings.testing_connection_string

    print("Getting rid of test database")
    os.environ["postgres_dbname"] = os.environ["orig_postgres_dbname"]
    conn = await asyncpg.connect(dsn=settings.writer_connection_string)
    await conn.execute("DROP DATABASE pgstactestdb;")
    await conn.close()


@pytest.fixture(autouse=True)
async def pgstac(pg):
    print(f"{os.environ['postgres_dbname']}")
    yield
    print("Truncating Data")
    conn = await asyncpg.connect(dsn=settings.testing_connection_string)
    await conn.execute(
        """
        TRUNCATE pgstac.items CASCADE;
        TRUNCATE pgstac.collections CASCADE;
        TRUNCATE pgstac.searches CASCADE;
        TRUNCATE pgstac.search_wheres CASCADE;
        """
    )
    await conn.close()


def _api_client_provider(middleware_configs: Optional[MiddlewareConfig] = []):
    print("creating client with settings")

    extensions = [
        TransactionExtension(client=TransactionsClient(), settings=settings),
        QueryExtension(),
        FilterExtension(),
        SortExtension(),
        FieldsExtension(),
        TokenPaginationExtension(),
    ]
    post_request_model = create_post_request_model(extensions, base_model=PgstacSearch)

    api = StacApi(
        settings=settings,
        extensions=extensions,
        client=CoreCrudClient(post_request_model=post_request_model),
        search_get_request_model=create_get_request_model(extensions),
        search_post_request_model=post_request_model,
        response_class=ORJSONResponse,
        middlewares=middleware_configs,
    )

    return api


@pytest.fixture(scope="session")
def api_client(pg):
    return _api_client_provider()


@pytest.mark.asyncio
@pytest.fixture(scope="session")
async def app_client(pg, request):
    # support custom behaviours driven by fixture caller
    middleware_configs = []
    if hasattr(request, "param"):
        setup_func = request.param.get("setup_func")
        if setup_func is not None:
            setup_func()
        middleware_configs = request.param.get("middleware_configs", [])
    app = _api_client_provider(middleware_configs=middleware_configs).app
    async with AsyncClient(app=app, base_url="http://test") as c:
        await connect_to_db(app)
        yield c
        await close_db_connection(app)


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
    data = load_test_data("test_item.json")
    resp = await app_client.post(
        "/collections/{coll.id}/items",
        json=data,
    )
    assert resp.status_code == 200
    return Item.parse_obj(resp.json())
