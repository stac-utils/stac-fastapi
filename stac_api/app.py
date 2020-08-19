"""FastAPI application."""
from stac_api.clients.postgres.collection import (
    CollectionCrudClient,
    PaginationTokenClient,
)
from stac_api.config import ApiSettings
from stac_api.create_app import create_app

settings = ApiSettings()
collection_client = CollectionCrudClient(pagination_client=PaginationTokenClient())
app = create_app(
    settings=settings, collection_client=collection_client, transactions=True
)
