"""Collection crud client."""

import logging
from dataclasses import dataclass
from typing import List, Tuple

from fastapi import Depends
from sqlalchemy.orm import Session

from sqlakeyset import Page, get_page
from stac_api import errors
from stac_api.clients.base import BaseCollectionClient
from stac_api.clients.postgres.base import PostgresClient
from stac_api.clients.postgres.tokens import (
    PaginationTokenClient,
    pagination_token_client_factory,
)
from stac_api.models import database
from stac_api.utils.dependencies import database_reader_factory, database_writer_factory

logger = logging.getLogger(__name__)


@dataclass
class CollectionCrudClient(PostgresClient, BaseCollectionClient):
    """Collection specific CRUD operations"""

    pagination_client: PaginationTokenClient

    def all_collections(self) -> List[database.Collection]:
        """Read all collections from the database"""
        try:
            items = self.reader_session.query(self.table).all()
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting item collection"
            )
        return items

    def item_collection(
        self, collection_id: str, limit: int = 10, token: str = None
    ) -> Tuple[Page, int]:
        """Read an item collection from the database"""
        try:
            collection_children = (
                self.lookup_id(collection_id)
                .first()
                .children.order_by(database.Item.datetime.desc(), database.Item.id)
            )
            count = collection_children.count()
            token = self.pagination_client.get(token) if token else token
            page = get_page(collection_children, per_page=limit, page=(token or False))
            # Create dynamic attributes for each page
            page.next = (
                self.pagination_client.insert(keyset=page.paging.bookmark_next)
                if page.paging.has_next
                else None
            )
            page.previous = (
                self.pagination_client.insert(keyset=page.paging.bookmark_previous)
                if page.paging.has_previous
                else None
            )
        except errors.NotFoundError:
            raise
        except Exception as e:
            logger.error(e, exc_info=True)
            raise errors.DatabaseError(
                "Unhandled database error when getting collection children"
            )
        return page, count


def collection_crud_client_factory(
    reader_session: Session = Depends(database_reader_factory),
    writer_session: Session = Depends(database_writer_factory),
    pagination_client: PaginationTokenClient = Depends(pagination_token_client_factory),
) -> CollectionCrudClient:
    """FastAPI dependency"""
    return CollectionCrudClient(
        reader_session=reader_session,
        writer_session=writer_session,
        table=database.Collection,
        pagination_client=pagination_client,
    )
