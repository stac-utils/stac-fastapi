from dataclasses import dataclass
import logging
from typing import List, Tuple, Union

from fastapi import Depends
import geoalchemy2 as ga
import sqlalchemy as sa
from sqlakeyset import get_page, Page
from starlette.requests import Request

from .base_crud import BaseCrudClient
from .collection_crud import CollectionCrudClient, collection_crud_client_factory
from .tokens import PaginationTokenClient, pagination_token_client_factory
from ..errors import DatabaseError
from ..models import database, schemas

logger = logging.getLogger(__name__)

NumType = Union[float, int]


@dataclass
class ItemCrudClient(BaseCrudClient):
    collection_crud: CollectionCrudClient
    pagination_client: PaginationTokenClient

    def stac_search(self, search_request: schemas.STACSearch) -> Tuple[Page, int]:
        token = (
            self.pagination_client.get(search_request.token)
            if search_request.token
            else False
        )
        query = self.reader_session.query(self.table)

        # Filter by collection
        if search_request.collections:
            collection_filter = sa.or_(
                *[
                    self.table.collection_id == col_id
                    for col_id in search_request.collections
                ]
            )
            query = query.filter(collection_filter)

        # Sort
        if search_request.sortby:
            sort_fields = [
                getattr(self.table.get_field(sort.field), sort.direction.value)()
                for sort in search_request.sortby
            ]
            # Add id to end of sort to ensure unique keyset
            sort_fields.append(self.table.id)
            query = query.order_by(*sort_fields)
        else:
            # Default sort is date and id
            query = query.order_by(self.table.datetime.desc(), self.table.id)

        # Ignore other parameters if ID is present
        if search_request.ids:
            id_filter = sa.or_(*[self.table.id == i for i in search_request.ids])
            try:
                items = query.filter(id_filter).order_by(self.table.id)
                page = get_page(items, per_page=search_request.limit, page=token)
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
            except:
                error_message = (
                    "Unhandled database error when searching for items by id"
                )
                logger.error(error_message, exc_info=True)
                raise DatabaseError(message=error_message)
            return page, len(search_request.ids)

        # Spatial query
        poly = search_request.polygon()
        if poly:
            filter_geom = ga.shape.from_shape(poly, srid=4326)
            query = query.filter(
                ga.func.ST_Intersects(self.table.geometry, filter_geom)
            )

        # Temporal query
        if search_request.datetime:
            # Two tailed query (between)
            if ".." not in search_request.datetime:
                query = query.filter(
                    self.table.datetime.between(*search_request.datetime)
                )
            # All items after the start date
            if search_request.datetime[0] != "..":
                query = query.filter(self.table.datetime >= search_request.datetime[0])
            # All items before the end date
            if search_request.datetime[1] != "..":
                query = query.filter(self.table.datetime <= search_request.datetime[1])

        # Query fields
        if search_request.query:
            for (field_name, expr) in search_request.query.items():
                field = self.table.get_field(field_name)
                for (op, value) in expr.items():
                    query = query.filter(op.operator(field, value))

        try:
            count = query.count()
            page = get_page(query, per_page=search_request.limit, page=token)
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
        except:
            error_message = "Unhandled database error during spatial/temporal query"
            logger.error(error_message, exc_info=True)
            raise DatabaseError(message=error_message)
        return page, count


def item_crud_client_factory(
    request: Request,
    collection_crud: CollectionCrudClient = Depends(collection_crud_client_factory),
    pagination_client: PaginationTokenClient = Depends(pagination_token_client_factory),
) -> ItemCrudClient:
    return ItemCrudClient(
        reader_session=request.app.state.DB_READER,
        writer_session=request.app.state.DB_WRITER,
        collection_crud=collection_crud,
        table=database.Item,
        pagination_client=pagination_client,
    )
