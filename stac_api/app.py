"""FastAPI application."""
from stac_api.config import ApiSettings
from stac_api.create_app import create_app

settings = ApiSettings(
    stac_api_extensions=["context", "fields", "query", "sort", "transaction"]
)
app = create_app(settings=settings)
