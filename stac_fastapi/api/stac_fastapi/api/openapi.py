"""openapi."""

import warnings

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route, request_response

from stac_fastapi.api.config import ApiExtensions
from stac_fastapi.types.config import ApiSettings


class VndOaiResponse(JSONResponse):
    """JSON with custom, vendor content-type."""

    media_type = "application/vnd.oai.openapi+json;version=3.0"

    def __init__(self, *args, **kwargs):
        """Init function with deprecation warning."""
        warnings.warn(
            "VndOaiResponse is deprecated and will be removed in v3.0",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)


def update_openapi(app: FastAPI) -> FastAPI:
    """Update OpenAPI response content-type.

    This function modifies the openapi route to comply with the STAC API spec's required
    content-type response header.
    """
    # Find the route for the openapi_url in the app
    openapi_route: Route = next(
        route for route in app.router.routes if route.path == app.openapi_url
    )
    # Store the old endpoint function so we can call it from the patched function
    old_endpoint = openapi_route.endpoint

    # Create a patched endpoint function that modifies the content type of the response
    async def patched_openapi_endpoint(req: Request) -> Response:
        # Get the response from the old endpoint function
        response: JSONResponse = await old_endpoint(req)
        # Update the content type header in place
        response.headers["content-type"] = "application/vnd.oai.openapi+json;version=3.0"
        # Return the updated response
        return response

    # When a Route is accessed the `handle` function calls `self.app`. Which is
    # the endpoint function wrapped with `request_response`. So we need to wrap
    # our patched function and replace the existing app with it.
    openapi_route.app = request_response(patched_openapi_endpoint)

    # return the patched app
    return app


def config_openapi(app: FastAPI, settings: ApiSettings):
    """Config openapi."""
    warnings.warn(
        "config_openapi is deprecated and will be removed in v3.0",
        DeprecationWarning,
    )

    def custom_openapi():
        """Config openapi."""
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
