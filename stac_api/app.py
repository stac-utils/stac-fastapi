"""FastAPI application."""
from stac_api.config import ApiSettings
from stac_api.create_app import create_app

settings = ApiSettings()
app = create_app(settings, transactions=True)
