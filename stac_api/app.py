"""FastAPI application."""
from stac_api.clients.postgres.collection import CollectionCrudClient
from stac_api.clients.postgres.item import ItemCrudClient
from stac_api.clients.postgres.tokens import PaginationTokenClient
from stac_api.config import ApiSettings
from stac_api.create_app import create_app

settings = ApiSettings()
pagination_client = PaginationTokenClient()
collection_client = CollectionCrudClient(pagination_client=pagination_client)
item_client = ItemCrudClient(
    collection_crud=collection_client, pagination_client=pagination_client
)
app = create_app(
    settings=settings,
    collection_client=collection_client,
    item_client=item_client,
    transactions=True,
)
