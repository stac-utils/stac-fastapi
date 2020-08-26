"""transactions extension client"""

import logging
from dataclasses import dataclass
from typing import Type, Union

from stac_api import errors
from stac_api.clients.base import BaseTransactionsClient
from stac_api.clients.postgres.base import PostgresClient
from stac_api.models import database, schemas

logger = logging.getLogger(__name__)


@dataclass
class TransactionsClient(PostgresClient, BaseTransactionsClient):
    """Transactions extension specific CRUD operations"""

    table: Type[database.Collection] = database.Collection
    item_table: Type[database.Item] = database.Item

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

    def create_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Create an item"""
        obj = self._create(model, table=self.item_table)
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Item.from_orm(obj)

    def update_item(self, model: schemas.Item, **kwargs) -> schemas.Item:
        """Update an item"""
        obj = self._update(model, table=self.item_table)
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Item.from_orm(obj)

    def delete_item(self, id: str, **kwargs) -> schemas.Item:
        """Delete an item"""
        obj = self._delete(id, table=self.item_table)
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Item.from_orm(obj)

    def create_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Create a collection"""
        obj = self._create(model, table=self.collection_table)
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Collection.from_orm(obj)

    def update_collection(
        self, model: schemas.Collection, **kwargs
    ) -> schemas.Collection:
        """Update a collection"""
        obj = self._update(model, table=self.collection_table)
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Collection.from_orm(obj)

    def delete_collection(self, id: str, **kwargs) -> schemas.Collection:
        """Delete a collection"""
        obj = self._delete(id, table=self.collection_table)
        obj.base_url = str(kwargs["request"].base_url)
        return schemas.Collection.from_orm(obj)
