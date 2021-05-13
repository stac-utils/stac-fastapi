"""Database connection handling."""
import logging

import orjson
from asyncpg import exceptions
from buildpg import asyncpg, render
from fastapi import FastAPI

from stac_fastapi.types.errors import (
    ConflictError,
    DatabaseError,
    ForeignKeyError,
    NotFoundError,
)

# from stac_fastapi.pgstac.config import Settings
# settings = Settings()
# if app.state.testing:
#     settings.reader_connection_string = settings.writer_connection_string = settings.testing_connection_string

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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
    logger.info(f"Creating Connection Pools {readpool} {writepool}")
    db = DB()
    app.state.readpool = await db.create_pool(readpool, settings)
    app.state.writepool = await db.create_pool(writepool, settings)


async def close_db_connection(app: FastAPI) -> None:
    """Close connection."""
    logger.info("Closing connections to database")
    await app.state.readpool.close()
    await app.state.writepool.close()
    logger.info("Connections closed")


async def dbfunc(pool, func, arg):
    """Wrap PLPGSQL Functions."""
    try:
        if isinstance(arg, str):
            async with pool.acquire() as conn:
                q, p = render(
                    f"""
                        SELECT * FROM {func}(:item::text);
                        """,
                    item=arg,
                )
                return await conn.fetchval(q, *p)
        else:
            async with pool.acquire() as conn:
                q, p = render(
                    f"""
                        SELECT * FROM {func}(:item::text::jsonb);
                        """,
                    item=arg.json(),
                )
                return await conn.fetchval(q, *p)
    except exceptions.UniqueViolationError:
        raise ConflictError
    except exceptions.NoDataFoundError:
        raise NotFoundError
    except exceptions.NotNullViolationError:
        raise DatabaseError
    except exceptions.ForeignKeyViolationError:
        raise ForeignKeyError


class DB:
    """DB class that can be used with context manager."""

    pool = None
    write = False

    def __init__(self, connection_string: str = None):
        """Init."""
        self.connection_string = connection_string

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
        logger.info("Connection to pool established")
        return pool

    # async def get_pool(self, write: bool = False):
    #     """Get a connection pool."""
    #     if write or self.write:
    #         self.pool = await self.create_pool(
    #             settings.writer_connection_string
    #         )
    #     else:
    #         self.pool = await self.create_pool(
    #             settings.reader_connection_string
    #         )
    #     return self.pool

    async def __aenter__(self):
        """Aenter."""
        self.pool = await self.create_pool(self.connection_string)
        self.connection = await self.pool.acquire()
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Aexit."""
        await self.pool.close()
