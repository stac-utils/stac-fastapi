"""database session management"""
import logging
import os
from contextlib import contextmanager
from typing import Iterator

import attr
import sqlalchemy as sa
from sqlalchemy.orm import Session as SqlSession

import psycopg2
from fastapi_utils.session import FastAPISessionMaker as _FastAPISessionMaker
from stac_api import errors

logger = logging.getLogger(__name__)


class FastAPISessionMaker(_FastAPISessionMaker):
    """FastAPISessionMaker"""

    def __init__(self, database_uri: str):
        """init"""
        super().__init__(database_uri)

    @contextmanager
    def context_session(self) -> Iterator[SqlSession]:
        """override base method to include exception handling"""
        try:
            yield from self.get_db()
        except sa.exc.IntegrityError as e:
            if isinstance(e.orig, psycopg2.errors.UniqueViolation):
                raise errors.ConflictError("resource already exists") from e
            elif isinstance(e.orig, psycopg2.errors.ForeignKeyViolation):
                raise errors.ForeignKeyError("collection does not exist") from e
            logger.error(e, exc_info=True)
            raise errors.DatabaseError("unhandled database error")


@attr.s
class Session:
    reader_conn_string: str = attr.ib()
    writer_conn_string: str = attr.ib()

    @classmethod
    def create_from_env(cls):
        return cls(
            reader_conn_string=os.environ["READER_CONN_STRING"],
            writer_conn_string=os.environ["WRITER_CONN_STRING"],
        )

    def __attrs_post_init__(self):
        self.reader: FastAPISessionMaker = FastAPISessionMaker(self.reader_conn_string)
        self.writer: FastAPISessionMaker = FastAPISessionMaker(self.writer_conn_string)
