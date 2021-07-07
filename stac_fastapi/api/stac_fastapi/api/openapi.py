"""openapi."""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from stac_fastapi.types.config import ApiSettings


def config_openapi(app: FastAPI, settings: ApiSettings):
    """Config openapi."""

    def custom_openapi():
        """Config openapi."""
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title="Arturo STAC API", version="0.1", routes=app.routes
        )

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
