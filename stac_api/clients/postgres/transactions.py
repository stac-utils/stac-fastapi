"""transactions extension client"""

import logging
from dataclasses import dataclass
from typing import Type, Union

import sqlalchemy as sa
from fastapi import Depends
from sqlalchemy.orm import Session

from ... import errors
from ...models import database, schemas
from ...utils.dependencies import database_reader_factory, database_writer_factory
from ..base import BaseTransactionsClient
from .base import PostgresClient

logger = logging.getLogger(__name__)


@dataclass
class TransactionsClient(PostgresClient, BaseTransactionsClient):
    """Transactions extension specific CRUD operations"""

    reader_session: sa.orm.Session
    writer_session: sa.orm.Session
    table: Type[database.Collection]
    item_table: Type[database.Item]

    @property
    def collection_table(self):
        """alias for `self.table` # TODO: Figure out a better way to do this"""
        return self.table

    def _create(
        self,
        model: Union[schemas.Collection, schemas.Item],
        table: Union[Type[database.Collection], Type[database.Item]],
    ) -> Union[database.Collection, database.Item]:
        """Create a single record"""
        try:
            self.lookup_id(model.id, table=table)
            error_message = f"Row {model.id} already exists"
            logger.error(error_message, exc_info=True)
            raise errors.ConflictError(error_message)
        except errors.NotFoundError:
            row_data = table.from_schema(model)
            self.writer_session.add(row_data)
            self.commit()
            return row_data

    def _update(
        self,
        model: Union[schemas.Collection, schemas.Item],
        table: Union[Type[database.Collection], Type[database.Item]],
    ) -> Union[database.Collection, database.Item]:
        """Create a single record if it does not exist or update an existing record"""
        try:
            query = self.lookup_id(model.id, table=table)
            update_data = table.get_database_model(model)
            # SQLAlchemy orm updates don't seem to like geoalchemy types
            update_data.pop("geometry", None)
            query.update(update_data)
            self.commit()
            return table.from_schema(model)
        except errors.NotFoundError:
            row_data = table.from_schema(model)
            self.writer_session.add(row_data)
            self.commit()
            return row_data

    def _delete(
        self, item_id: str, table: Union[Type[database.Collection], Type[database.Item]]
    ) -> Union[database.Collection, database.Item]:
        """Delete a single record"""
        query = self.lookup_id(item_id, table=table)
        row_data = query.first()
        query.delete()
        self.commit()
        return row_data

    def create_item(self, model: schemas.Item) -> database.Item:
        """Create an item"""
        return self._create(model, table=self.item_table)

    def update_item(self, model: schemas.Item) -> database.Item:
        """Update an item"""
        return self._update(model, table=self.item_table)

    def delete_item(self, id: str) -> database.Item:
        """Delete an item"""
        return self._delete(id, table=self.item_table)

    def create_collection(self, model: schemas.Collection) -> database.Collection:
        """Create a collection"""
        return self._create(model, table=self.collection_table)

    def update_collection(self, model: schemas.Collection) -> database.Collection:
        """Update a collection"""
        return self._update(model, table=self.collection_table)

    def delete_collection(self, id: str) -> database.Collection:
        """Delete a collection"""
        return self._delete(id, table=self.collection_table)


def transactions_client_factory(
    reader_session: Session = Depends(database_reader_factory),
    writer_session: Session = Depends(database_writer_factory),
) -> TransactionsClient:
    """FastAPI dependency"""
    return TransactionsClient(
        reader_session=reader_session,
        writer_session=writer_session,
        table=database.Collection,
        item_table=database.Item,
    )
