"""common error checks."""

import attr
from pymongo import MongoClient

from stac_fastapi.mongo.session import Session
from stac_fastapi.types import stac as stac_types
from stac_fastapi.types.errors import ConflictError, ForeignKeyError, NotFoundError


@attr.s
class ErrorChecks:
    """error checks class."""

    session: Session = attr.ib(default=Session)
    client: MongoClient = attr.ib(default=None)

    def _check_collection_foreign_key(self, model: stac_types.Collection):
        if not self.client.stac.stac_collection.count_documents(
            {"id": model["collection"]}, limit=1, session=self.session
        ):
            raise ForeignKeyError(f"Collection {model['collection']} does not exist")

    def _check_collection_conflict(self, model: stac_types.Collection):
        if self.client.stac.stac_collection.count_documents(
            {"id": model["id"]}, limit=1, session=self.session
        ):
            raise ConflictError(f"Collection {model['id']} already exists")

    def _check_collection_not_found(self, collection_id: str):
        if (
            self.client.stac.stac_collection.count_documents(
                {"id": collection_id}, session=self.session
            )
            == 0
        ):
            raise NotFoundError(f"Collection {collection_id} not found")

    def _check_item_conflict(self, model: stac_types.Item):
        if self.client.stac.stac_item.count_documents(
            {"id": model["id"], "collection": model["collection"]},
            limit=1,
            session=self.session,
        ):
            raise ConflictError(
                f"Item {model['id']} in collection {model['collection']} already exists"
            )

    def _check_item_not_found(self, item_id: str, collection_id: str):
        if (
            self.client.stac.stac_item.count_documents(
                {"id": item_id, "collection": collection_id},
                session=self.session,
            )
            == 0
        ):
            raise NotFoundError(
                f"Item {item_id} in collection {collection_id} not found"
            )
