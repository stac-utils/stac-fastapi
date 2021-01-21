"""transactions extension client"""

import json
import logging
from typing import Dict, List, Optional, Type, Union

import attr
from sqlalchemy import create_engine

from stac_api import errors
from stac_api.clients.base import BaseTransactionsClient, BulkTransactionsClient
from stac_api.clients.postgres.base import PostgresClient
from stac_api.models import database, schemas

logger = logging.getLogger(__name__)


@attr.s
class TransactionsClient(PostgresClient, BaseTransactionsClient):
    """Transactions extension specific CRUD operations"""

    table: Type[database.Collection] = attr.ib(default=database.Collection)
    item_table: Type[database.Item] = attr.ib(default=database.Item)

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


@attr.s
class PostgresBulkTransactions(BulkTransactionsClient):
    """postgres bulk transactions"""

    connection_str: str = attr.ib()
    debug: bool = attr.ib(default=False)

    def __attrs_post_init__(self):
        """create sqlalchemy engine"""
        self.engine = create_engine(self.connection_str, echo=self.debug)

    @staticmethod
    def _preprocess_item(item) -> Dict:
        """
        preprocess items to match data model
        # TODO: dedup with GetterDict logic (ref #58)
        """
        item["geometry"] = json.dumps(item["geometry"])
        item["collection_id"] = item.pop("collection")
        item["datetime"] = item["properties"].pop("datetime")
        return item

    def bulk_item_insert(
        self, items: List[Dict], chunk_size: Optional[int] = None
    ) -> None:
        """
        bulk item insertion using sqlalchemy core
        https://docs.sqlalchemy.org/en/13/faq/performance.html#i-m-inserting-400-000-rows-with-the-orm-and-it-s-really-slow
        """
        items = [self._preprocess_item(item) for item in items]
        if chunk_size:
            for chunk in self._chunks(items, chunk_size):
                self.engine.execute(database.Item.__table__.insert(), chunk)
            return

        self.engine.execute(database.Item.__table__.insert(), items)
        return
