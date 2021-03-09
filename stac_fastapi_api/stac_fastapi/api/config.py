"""Application settings."""
import enum
from typing import Optional, Set

from pydantic import BaseSettings


# TODO: Move to stac-pydantic
class ApiExtensions(enum.Enum):
    """Enumeration of available stac api extensions.

    Ref: https://github.com/radiantearth/stac-api-spec/tree/master/extensions
    """

    context = "context"
    fields = "fields"
    query = "query"
    sort = "sort"
    transaction = "transaction"


class AddOns(enum.Enum):
    """Enumeration of available third party add ons."""

    tiles = "tiles"
    bulk_transaction = "bulk-transaction"


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
    default_includes: Set[str] = None

    # Fields which are defined by STAC but not included in the database model
    forbidden_fields: Set[str] = {"type"}

    # Fields which are item properties but indexed as distinct fields in the database model
    indexed_fields: Set[str] = {"datetime"}

    class Config:
        """model config (https://pydantic-docs.helpmanual.io/usage/model_config/)."""

        extra = "allow"
        env_file = ".env"


settings: Optional[ApiSettings] = None


def inject_settings(base_settings: ApiSettings):
    """Inject settings to global scope.

    Attributes:
        base_settings: api settings.

    """
    global settings
    settings = base_settings
