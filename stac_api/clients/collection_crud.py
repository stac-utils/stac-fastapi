from dataclasses import dataclass
import logging
from typing import List, Tuple

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlakeyset import get_page, Page

from .base_crud import BaseCrudClient
from .tokens import PaginationTokenClient, pagination_token_client_factory
from .. import errors
from ..models import database
from ..utils.dependencies import database_reader_factory, database_writer_factory

logger = logging.getLogger(__name__)


@dataclass
class CollectionCrudClient(BaseCrudClient):
    pagination_client: PaginationTokenClient

    def get_all_collections(self) -> List[database.Collection]:
        """Read all collections from the database"""
        try:
            items = self.reader_session.query(self.table).all()
        except:
            error_message = "Unhandled database error when getting item collection"
            logger.error(error_message, exc_info=True)
            raise errors.DatabaseError(message=error_message)
        return items

    def get_item_collection(
        self, collection_id: str, limit: int, token: str = None
    ) -> Tuple[Page, int]:
        """Read an item collection from the database"""
        try:
            query = (
                self.lookup_id(collection_id)
                .first()
                .children.order_by(database.Item.datetime.desc(), database.Item.id)
            )
            count_query = query.statement.with_only_columns([func.count()]).order_by(None)
            count = query.session.execute(count_query).scalar()
            token = self.pagination_client.get(token) if token else token
            page = get_page(query, per_page=limit, page=(token or False))
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
        except:
            error_message = "Unhandled database error when getting collection children"
            logger.error(error_message, exc_info=True)
            raise errors.DatabaseError(message=error_message)
        return page, count


def collection_crud_client_factory(
    reader_session: Session = Depends(database_reader_factory),
    writer_session: Session = Depends(database_writer_factory),
    pagination_client: PaginationTokenClient = Depends(pagination_token_client_factory),
) -> CollectionCrudClient:
    return CollectionCrudClient(
        reader_session=reader_session,
        writer_session=writer_session,
        table=database.Collection,
        pagination_client=pagination_client,
    )
