import asyncio
import json
import os
import time
from typing import Callable, Dict

import docker
import pypgstac
import pytest
from dockerctx import get_open_port, new_container, pg_ready
from httpx import AsyncClient
from stac_pydantic import Collection, Item

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TransactionExtension,
)
from stac_fastapi.pgstac.config import Settings
from stac_fastapi.pgstac.core import CoreCrudClient
from stac_fastapi.pgstac.db import close_db_connection, connect_to_db
from stac_fastapi.pgstac.transactions import TransactionsClient
from stac_fastapi.pgstac.types.search import PgstacSearch

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

os.environ["postgres_user"] = "testuser"
os.environ["postgres_pass"] = "testpw"
os.environ["postgres_host_reader"] = "localhost"
os.environ["postgres_host_writer"] = "localhost"
os.environ["postgres_dbname"] = "testdb"


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session")
def pgport():
    port = get_open_port()
    os.environ["postgres_port"] = str(port)
    return port


@pytest.fixture(scope="session")
def dockerimage():
    print("pulling docker image for pgstac")
    client = docker.from_env()
    image = client.images.get(f"bitner/pgstac:{pypgstac.__version__}")
    return image


def pgready(pgport):
    st = time.time()
    print("Testing if PG is ready...")
    ready = pg_ready(
        "localhost",
        pgport,
        dbuser="testuser",
        dbpass="testpw",
        dbname="testdb",
    )
    if ready:
        print(f"PG is ready ({time.time() - st})")
    return ready


@pytest.fixture(autouse=True)
def pg(pgport, dockerimage):
    st = time.time()
    print(f"creating db instance on port {pgport}")
    with new_container(
        dockerimage,
        ports={"5432/tcp": pgport},
        environment=[
            "POSTGRES_USER=testuser",
            "POSTGRES_PASSWORD=testpw",
            "POSTGRES_DB=testdb",
        ],
        ready_test=lambda: pgready(pgport),
        docker_api_version="1.41",
    ) as container:
        print(
            f"{container.name} {container.status} in {time.time() -st} seconds"
        )
        yield container


@pytest.fixture(autouse=True, scope="session")
def settings(pgport):
    settings = Settings()
    print(settings)
    print(settings.reader_connection_string)
    return settings


@pytest.fixture()
def api_client(settings, pg):
    print("creating client with settings")
    print(settings)
    api = StacApi(
        settings=settings,
        extensions=[
            TransactionExtension(client=TransactionsClient),
            QueryExtension(),
            SortExtension(),
            FieldsExtension(),
        ],
        client=CoreCrudClient(),
        search_request_model=PgstacSearch,
    )

    return api


@pytest.mark.asyncio
@pytest.fixture()
async def app(api_client):
    st = time.time()
    app = api_client.app
    await connect_to_db(app)

    yield app

    await close_db_connection(app)


@pytest.mark.asyncio
@pytest.fixture()
async def app_client(app):
    async with AsyncClient(app=app, base_url="http://test") as c:
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
        "/collections/{coll.id}/items",
        json=data,
    )
    assert resp.status_code == 200
    return Item.parse_obj(resp.json())
