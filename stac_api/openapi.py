"""openapi"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def config_openapi(app: FastAPI):
    """config openapi"""

    def custom_openapi():
        """config openapi"""
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Sherlock STAC API", version="0.1", routes=app.routes
        )
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
