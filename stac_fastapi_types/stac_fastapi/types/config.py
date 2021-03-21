"""stac_fastapi.types.config module."""
from typing import Optional, Set

from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    """ApiSettings.

    Defines api configuration, potentially through environment variables.
    See https://pydantic-docs.helpmanual.io/usage/settings/.
    Attributes:
        environment: name of the environment (ex. dev/prod).
        debug: toggles debug mode.
        forbidden_fields: set of fields defined by STAC but not included in the database.
        indexed_fields:
            set of fields which are usually in `item.properties` but are indexed as distinct columns in
            the database.
    """

    environment: str
    debug: bool = False
    default_includes: Optional[Set[str]] = None

    # Fields which are defined by STAC but not included in the database model
    forbidden_fields: Set[str] = {"type"}

    # Fields which are item properties but indexed as distinct fields in the database model
    indexed_fields: Set[str] = {"datetime"}

    class Config:
        """model config (https://pydantic-docs.helpmanual.io/usage/model_config/)."""

        extra = "allow"
        env_file = ".env"
