"""bulk transactions extension."""
import attr
from fastapi import APIRouter, FastAPI

from stac_api.models import schemas
from stac_fastapi.api.models import _create_request_model
from stac_fastapi.api.routes import create_endpoint_from_model
from stac_fastapi.backend.client import BaseBulkTransactionsClient
from stac_fastapi.extensions.core.extension import ApiExtension


@attr.s
class BulkTransactionExtension(ApiExtension):
    """Bulk Transaction Extension.

    Bulk Transaction extension adds the `POST /collections/{collectionId}/bulk_items` endpoint to the application
    for efficient bulk insertion of items.
    """

    client: BaseBulkTransactionsClient = attr.ib()

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        items_request_model = _create_request_model(schemas.Items)

        router = APIRouter()
        router.add_api_route(
            name="Bulk Create Item",
            path="/collections/{collectionId}/bulk_items",
            response_model=str,
            response_model_exclude_unset=True,
            response_model_exclude_none=True,
            methods=["POST"],
            endpoint=create_endpoint_from_model(
                self.client.bulk_item_insert, items_request_model
            ),
        )
        app.include_router(router, tags=["Bulk Transaction Extension"])
