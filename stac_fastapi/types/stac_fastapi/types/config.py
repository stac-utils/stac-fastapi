"""stac_fastapi.types.config module."""

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    """ApiSettings.

    Defines api configuration, potentially through environment variables.
    See https://pydantic-docs.helpmanual.io/usage/settings/.
    Attributes:
        environment: name of the environment (ex. dev/prod).
        debug: toggles debug mode.
        forbidden_fields: set of fields defined by STAC but not included in the database.
        indexed_fields:
            set of fields which are usually in `item.properties` but are indexed
            as distinct columns in the database.
    """

    stac_fastapi_title: str = "stac-fastapi"
    stac_fastapi_description: str = "stac-fastapi"
    stac_fastapi_version: str = "0.1"
    stac_fastapi_landing_id: str = "stac-fastapi"

    app_host: str = "0.0.0.0"
    app_port: int = 8000
    reload: bool = True
    enable_response_models: bool = False

    openapi_url: str = "/api"
    docs_url: str = "/api.html"

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


class Settings:
    """Holds the global instance of settings."""

    _instance: Optional[ApiSettings] = None

    @classmethod
    def set(cls, base_settings: ApiSettings):
        """Set the global settings."""
        cls._instance = base_settings

    @classmethod
    def get(cls) -> ApiSettings:
        """Get the settings.

        If they have not yet been set, throws an exception.
        """
        if cls._instance is None:
            raise ValueError("Settings have not yet been set.")
        return cls._instance
