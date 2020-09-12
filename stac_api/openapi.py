"""openapi"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from stac_api.config import ApiExtensions, ApiSettings


def config_openapi(app: FastAPI, settings: ApiSettings):
    """config openapi"""

    def custom_openapi():
        """config openapi"""
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title="Arturo STAC API", version="0.1", routes=app.routes
        )

        if settings.api_extension_is_enabled(ApiExtensions.fields):
            openapi_schema["paths"]["/search"]["get"]["responses"]["200"]["content"][
                "application/json"
            ]["schema"] = {"$ref": "#/components/schemas/ItemCollection"}
            openapi_schema["paths"]["/search"]["post"]["responses"]["200"]["content"][
                "application/json"
            ]["schema"] = {"$ref": "#/components/schemas/ItemCollection"}

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi
