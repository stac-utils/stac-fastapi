"""database session management."""
import logging
import os
from contextlib import contextmanager
from typing import Iterator

import attr
import psycopg2
import sqlalchemy as sa
from fastapi_utils.session import FastAPISessionMaker as _FastAPISessionMaker
from sqlalchemy.orm import Session as SqlSession

from stac_fastapi.sqlalchemy.config import SqlalchemySettings
from stac_fastapi.types import errors

logger = logging.getLogger(__name__)


class FastAPISessionMaker(_FastAPISessionMaker):
    """FastAPISessionMaker."""

    @contextmanager
    def context_session(self) -> Iterator[SqlSession]:
        """Override base method to include exception handling."""
        try:
            yield from self.get_db()
        except sa.exc.StatementError as e:
            if isinstance(e.orig, psycopg2.errors.UniqueViolation):
                raise errors.ConflictError("resource already exists") from e
            elif isinstance(e.orig, psycopg2.errors.ForeignKeyViolation):
                raise errors.ForeignKeyError("collection does not exist") from e
            logger.error(e, exc_info=True)
            raise errors.DatabaseError("unhandled database error")


@attr.s
class Session:
    """Database session management."""

    reader_conn_string: str = attr.ib()
    writer_conn_string: str = attr.ib()

    @classmethod
    def create_from_env(cls):
        """Create from environment."""
        return cls(
            reader_conn_string=os.environ["READER_CONN_STRING"],
            writer_conn_string=os.environ["WRITER_CONN_STRING"],
        )

    @classmethod
    def create_from_settings(cls, settings: SqlalchemySettings) -> "Session":
        """Create a Session object from settings."""
        return cls(
            reader_conn_string=settings.reader_connection_string,
            writer_conn_string=settings.writer_connection_string,
        )

    def __attrs_post_init__(self):
        """Post init handler."""
        self.reader: FastAPISessionMaker = FastAPISessionMaker(self.reader_conn_string)
        self.writer: FastAPISessionMaker = FastAPISessionMaker(self.writer_conn_string)
