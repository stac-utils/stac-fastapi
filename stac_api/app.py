"""FastAPI application."""
from stac_api.api import create_app
from stac_api.config import ApiSettings

settings = ApiSettings(
    stac_api_extensions=["context", "fields", "query", "sort", "transaction"],
    add_ons=["tiles"],
)
app = create_app(settings=settings)
