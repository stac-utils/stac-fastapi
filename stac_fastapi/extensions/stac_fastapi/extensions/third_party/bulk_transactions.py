"""bulk transactions extension."""
import abc
from typing import Any, Dict, List, Optional

import attr
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

from stac_fastapi.api.models import _create_request_model
from stac_fastapi.api.routes import create_sync_endpoint
from stac_fastapi.types.extension import ApiExtension


class Items(BaseModel):
    """A list of STAC items."""

    items: Dict[str, Any]

    def __iter__(self):
        """Return an iterable of STAC items."""
        return iter(self.items)


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


@attr.s
class BulkTransactionExtension(ApiExtension):
    """Bulk Transaction Extension.

    Bulk Transaction extension adds the `POST /collections/{collectionId}/bulk_items` endpoint to the application
    for efficient bulk insertion of items.
    """

    client: BaseBulkTransactionsClient = attr.ib()
    conformance_classes: List[str] = attr.ib(default=list())
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        items_request_model = _create_request_model(Items)

        router = APIRouter()
        router.add_api_route(
            name="Bulk Create Item",
            path="/collections/{collectionId}/bulk_items",
            response_model=str,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_sync_endpoint(
                self.client.bulk_item_insert, items_request_model
            ),
        )
        app.include_router(router, tags=["Bulk Transaction Extension"])
