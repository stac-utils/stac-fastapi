"""openapi."""

from fastapi import FastAPI
from fastapi.routing import request_response
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route


def update_openapi(app: FastAPI) -> FastAPI:
    """Update OpenAPI response content-type.

    This function modifies the openapi route to comply with the STAC API spec's required
    content-type response header.
    """
    # Find the route for the openapi_url in the app
    # TODO: Type info is Route, while it shoukd maybe be APIRoute? Check FastAPI source.
    openapi_route: Route = next(
        route
        for route in app.router.routes
        if route.path == app.openapi_url  # type: ignore
    )
    # Store the old endpoint function so we can call it from the patched function
    old_endpoint = openapi_route.endpoint

    # Create a patched endpoint function that modifies the content type of the response
    async def patched_openapi_endpoint(req: Request) -> Response:
        # Get the response from the old endpoint function
        response = await old_endpoint(req)
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
