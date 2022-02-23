"""stac_fastapi.types.config module."""
from typing import Optional, Set

from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    """Settings for configuring API and serving behavior.

    Any of the attributes defined in this class may be overridden through
    environment variables (https://pydantic-docs.helpmanual.io/usage/settings/).

    Attributes:
        default_includes: The default set of fields returned by the API
            on `/search` requests.
        app_host: The hostname used by the ASGI server.
        app_port: The port used by the ASGI server.
        reload: Determines if the ASGI server is re-loaded on code-changes.
            Very useful for local development.
        enable_response_models: Determines if the application uses `FastAPI response
            models <https://github.com/radiantearth/stac-api-spec>`_ to validate and
            serialize API responses.
        openapi_url: Specifies the endpoint used to serve auto-generated OpenAPI schema.
        docs_url: Specifies the endpoint used to serve auto-generated API documentation
            using Swagger UI and ReDoc.
    """
    # TODO: Remove `default_includes` attribute so we can use `pydantic.BaseSettings` instead
    default_includes: Optional[Set[str]] = None

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    reload: bool = True
    enable_response_models: bool = False

    openapi_url: str = "/api"
    docs_url: str = "/api.html"

    class Config:
        """Model config (https://pydantic-docs.helpmanual.io/usage/model_config/)."""
        extra = "allow"
        env_file = ".env"


class Settings:
    """Holds the global instance of settings.

    Allows backends to access the :class:`~stac_fastapi.api.config.ApiSettings` object
    from within an active request.
    """

    _instance: Optional[ApiSettings] = None

    @classmethod
    def set(cls, base_settings: ApiSettings):
        """Set the global API settings."""
        cls._instance = base_settings

    @classmethod
    def get(cls) -> ApiSettings:
        """Get the settings.

        Returns:
            ApiSettings

        Raises:
            ValueError: Throws an exception if settings have not been set.
        """
        if cls._instance is None:
            raise ValueError("Settings have not yet been set.")
        return cls._instance
