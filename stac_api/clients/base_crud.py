"""Base crud client."""
import logging
from dataclasses import dataclass
from typing import Union

import sqlalchemy as sa
from sqlalchemy.orm import Query

import psycopg2

from .. import errors
from ..models import database, schemas

logger = logging.getLogger(__name__)


@dataclass
class BaseCrudClient:
    """Database CRUD operations on the defined table"""

    reader_session: sa.orm.Session
    writer_session: sa.orm.Session
    table: database.BaseModel

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

    def lookup_id(self, item_id: str) -> Query:
        """Create a query to access a single record from the table"""
        try:
            query = self.reader_session.query(self.table).filter(
                self.table.id == item_id
            )
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError("Unhandled database during ID lookup")
        if not self.row_exists(query):
            error_message = f"Row {item_id} does not exist"
            logger.warning(error_message)
            raise errors.NotFoundError(error_message)
        return query

    def create(
        self, item: Union[schemas.Collection, schemas.Item]
    ) -> Union[database.Collection, database.Item]:
        """Create a single record for the table"""
        try:
            self.lookup_id(item.id)
            error_message = f"Row {item.id} already exists"
            logger.error(error_message, exc_info=True)
            raise errors.ConflictError(error_message)
        except errors.NotFoundError:
            row_data = self.table.from_schema(item)
            self.writer_session.add(row_data)
            self.commit()
            return row_data

    def read(self, item_id: str) -> Union[database.Collection, database.Item]:
        """Read a single record from the table"""
        row_data = self.lookup_id(item_id).first()
        return row_data

    def update(
        self, item: Union[schemas.Collection, schemas.Item]
    ) -> Union[database.Collection, database.Item]:
        """Create a single record if it does not exist or update an existing record"""
        try:
            query = self.lookup_id(item.id)
            update_data = self.table.get_database_model(item)
            # SQLAlchemy orm updates don't seem to like geoalchemy types
            update_data.pop("geometry", None)
            query.update(update_data)
            self.commit()
            return self.table.from_schema(item)
        except errors.NotFoundError:
            row_data = self.table.from_schema(item)
            self.writer_session.add(row_data)
            self.commit()
            return row_data

    def delete(self, item_id: str) -> Union[database.Collection, database.Item]:
        """Delete a single record from the table"""
        query = self.lookup_id(item_id)
        row_data = query.first()
        query.delete()
        self.commit()
        return row_data
