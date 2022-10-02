"""bulk transactions extension."""
import abc
from typing import Any, Callable, Dict, List, Optional, Type, Union

import attr
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

from stac_fastapi.api.models import create_request_model
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest


class Items(BaseModel):
    """A group of STAC Item objects, in the form of a dictionary from Item.id -> Item."""

    items: Dict[str, Any]

    def __iter__(self):
        """Return an iterable of STAC Item objects."""
        return iter(self.items.values())


@attr.s  # type: ignore
class BaseBulkTransactionsClient(abc.ABC):
    """BulkTransactionsClient."""

    @staticmethod
    def _chunks(lst, n):
        """Yield successive n-sized chunks from list.

        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
        """
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    @abc.abstractmethod
    def bulk_item_insert(
        self, items: Items, chunk_size: Optional[int] = None, **kwargs
    ) -> str:
        """Bulk creation of items.

        Args:
            items: list of items.
            chunk_size: number of items processed at a time.

        Returns:
            Message indicating the status of the insert.

        """
        raise NotImplementedError


@attr.s  # type: ignore
class AsyncBaseBulkTransactionsClient(abc.ABC):
    """BulkTransactionsClient."""

    @abc.abstractmethod
    async def bulk_item_insert(self, items: Items, **kwargs) -> str:
        """Bulk creation of items.

        Args:
            items: list of items.

        Returns:
            Message indicating the status of the insert.

        """
        raise NotImplementedError


@attr.s
class BulkTransactionExtension(ApiExtension):
    """Bulk Transaction Extension.

    Bulk Transaction extension adds the `POST /collections/{collection_id}/bulk_items` endpoint to the application
    for efficient bulk insertion of items. The input to this is an object with an attribute  "items", that has a value
    that is an object with a group of attributes that are the ids of each Item, and the value is the Item entity.

        {
        "items": {
            "id1": { "type": "Feature", ... },
            "id2": { "type": "Feature", ... },
            "id3": { "type": "Feature", ... }
        }

    """

    client: Union[
        AsyncBaseBulkTransactionsClient, BaseBulkTransactionsClient
    ] = attr.ib()
    conformance_classes: List[str] = attr.ib(default=list())
    schema_href: Optional[str] = attr.ib(default=None)

    def _create_endpoint(
        self,
        func: Callable,
        request_type: Union[Type[APIRequest], Type[BaseModel], Dict],
    ) -> Callable:
        """Create a FastAPI endpoint."""
        return create_async_endpoint(func, request_type)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        items_request_model = create_request_model("Items", base_model=Items)

        router = APIRouter(prefix=app.state.router_prefix)
        router.add_api_route(
            name="Bulk Create Item",
            path="/collections/{collection_id}/bulk_items",
            response_model=str,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=self._create_endpoint(
                self.client.bulk_item_insert, items_request_model
            ),
        )
        app.include_router(router, tags=["Bulk Transaction Extension"])
