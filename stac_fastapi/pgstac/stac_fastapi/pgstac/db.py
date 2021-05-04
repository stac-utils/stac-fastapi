"""Database connection handling."""
import logging

import orjson
from buildpg import asyncpg
from fastapi import FastAPI

from stac_fastapi.pgstac.config import Settings

settings = Settings()


logger = logging.getLogger(__name__)


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
    """Connect."""
    logger.info(f"Connecting  read pool to {settings.reader_connection_string}")
    app.state.readpool = await asyncpg.create_pool(
        settings.reader_connection_string,
        min_size=settings.db_min_conn_size,
        max_size=settings.db_max_conn_size,
        max_queries=settings.db_max_queries,
        max_inactive_connection_lifetime=settings.db_max_inactive_conn_lifetime,
        init=con_init,
        server_settings={
            "search_path": "pgstac,public",
            "application_name": "pgstac-reader",
        },
    )
    logger.info("Connection to read pool established")
    logger.info(f"Connecting write pool to {settings.writer_connection_string}")

    app.state.writepool = await asyncpg.create_pool(
        settings.writer_connection_string,
        min_size=settings.db_min_conn_size,
        max_size=settings.db_max_conn_size,
        max_queries=settings.db_max_queries,
        max_inactive_connection_lifetime=settings.db_max_inactive_conn_lifetime,
        init=con_init,
        server_settings={
            "search_path": "pgstac,public",
            "application_name": "pgstac-writer",
        },
    )
    logger.info("Connection to write pool established")


async def close_db_connection(app: FastAPI) -> None:
    """Close connection."""
    logger.info("Closing connections to database")
    await app.state.readpool.close()
    await app.state.writepool.close()
    logger.info("Connections closed")


class DB:
    """DB class that can be used with context manager."""

    pool = None

    def __init__(
        self,
        pool=None,
        kwargs=None,
        write: bool = False,
    ):
        """Init."""
        if self.pool is None:
            if write is False:
                self.pool = kwargs["request"].app.state.readpool
            else:
                self.pool = kwargs["request"].app.state.writepool

    async def __aenter__(self):
        """Aenter."""
        self.connection = self.pool.acquire()
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Aexit."""
        await self.pool.release()
