"""Postgresql base client"""
import abc
import logging
from dataclasses import dataclass
from typing import Optional, Type

import sqlalchemy as sa
from sqlalchemy.orm import Query

import psycopg2
from stac_api import errors
from stac_api.models import database
from stac_api.utils.dependencies import READER, WRITER

logger = logging.getLogger(__name__)


@dataclass
class PostgresClient(abc.ABC):
    """Database CRUD operations on the defined table"""

    table: Type[database.BaseModel]

    @property
    def reader_session(self):
        """Get reader session from context var"""
        return READER.get()

    @property
    def writer_session(self):
        """Get writer session from context var"""
        return WRITER.get()

    @staticmethod
    def row_exists(query: Query) -> bool:
        """Check if a record exists from the sqlalchemy query object"""
        return True if query.scalar() else False

    def commit(self) -> None:
        """Commit both reader and writer sessions to keep them in sync, rolling back on psycopg2 errors"""
        try:
            self.writer_session.commit()
            self.reader_session.commit()
        except sa.exc.IntegrityError as e:
            self.writer_session.rollback()
            self.reader_session.rollback()
            logger.error(e.orig.pgerror, exc_info=True)
            # Explicitly catch foreign key errors to be reraised by the API as validation errors
            if isinstance(e.orig, psycopg2.errors.ForeignKeyViolation):
                raise errors.ForeignKeyError(e.orig.pgerror)
            raise errors.DatabaseError(e.orig.pgerror) from e
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError("Unhandled database exception during commit")

    def lookup_id(
        self, item_id: str, table: Optional[Type[database.BaseModel]] = None
    ) -> Query:
        """Create a query to access a single record from the table"""
        table = table or self.table
        try:
            query = self.reader_session.query(table).filter(table.id == item_id)
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError("Unhandled database during ID lookup")
        if not self.row_exists(query):
            error_message = f"Row {item_id} does not exist"
            logger.warning(error_message)
            raise errors.NotFoundError(error_message)
        return query
