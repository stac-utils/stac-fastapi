"""Database connection handling."""

import json
from contextlib import contextmanager
from typing import Dict, Generator, Union

import attr
import orjson
from asyncpg import exceptions, pool
from buildpg import V, asyncpg, render
from fastapi import FastAPI

from stac_fastapi.types.errors import (
    ConflictError,
    DatabaseError,
    ForeignKeyError,
    NotFoundError,
)


async def con_init(conn):
    """Use orjson for json returns."""
    await conn.set_type_codec(
        "json",
        encoder=orjson.dumps,
        decoder=orjson.loads,
        schema="pg_catalog",
    )
    await conn.set_type_codec(
        "jsonb",
        encoder=orjson.dumps,
        decoder=orjson.loads,
        schema="pg_catalog",
    )


async def connect_to_db(app: FastAPI) -> None:
    """Connect to Database."""
    settings = app.state.settings
    if app.state.settings.testing:
        readpool = writepool = settings.testing_connection_string
    else:
        readpool = settings.reader_connection_string
        writepool = settings.writer_connection_string
    db = DB()
    app.state.readpool = await db.create_pool(readpool, settings)
    app.state.writepool = await db.create_pool(writepool, settings)


async def close_db_connection(app: FastAPI) -> None:
    """Close connection."""
    await app.state.readpool.close()
    await app.state.writepool.close()


async def dbfunc(pool: pool, func: str, arg: Union[str, Dict]):
    """Wrap PLPGSQL Functions.

    Keyword arguments:
    pool -- the asyncpg pool to use to connect to the database
    func -- the name of the PostgreSQL function to call
    arg -- the argument to the PostgreSQL function as either a string
    or a dict that will be converted into jsonb
    """
    with translate_pgstac_errors():
        if isinstance(arg, str):
            async with pool.acquire() as conn:
                q, p = render(
                    """
                    SELECT * FROM :func(:item::text);
                    """,
                    func=V(func),
                    item=arg,
                )
                return await conn.fetchval(q, *p)
        else:
            async with pool.acquire() as conn:
                q, p = render(
                    """
                    SELECT * FROM :func(:item::text::jsonb);
                    """,
                    func=V(func),
                    item=json.dumps(arg),
                )
                return await conn.fetchval(q, *p)


@contextmanager
def translate_pgstac_errors() -> Generator[None, None, None]:
    """Context manager that translates pgstac errors into FastAPI errors."""
    try:
        yield
    except exceptions.UniqueViolationError as e:
        raise ConflictError from e
    except exceptions.NoDataFoundError as e:
        raise NotFoundError from e
    except exceptions.NotNullViolationError as e:
        raise DatabaseError from e
    except exceptions.ForeignKeyViolationError as e:
        raise ForeignKeyError from e


@attr.s
class DB:
    """DB class that can be used with context manager."""

    connection_string = attr.ib(default=None)
    _pool = attr.ib(default=None)
    _connection = attr.ib(default=None)

    async def create_pool(self, connection_string: str, settings):
        """Create a connection pool."""
        pool = await asyncpg.create_pool(
            connection_string,
            min_size=settings.db_min_conn_size,
            max_size=settings.db_max_conn_size,
            max_queries=settings.db_max_queries,
            max_inactive_connection_lifetime=settings.db_max_inactive_conn_lifetime,
            init=con_init,
            server_settings={
                "search_path": "pgstac,public",
                "application_name": "pgstac",
            },
        )
        return pool
