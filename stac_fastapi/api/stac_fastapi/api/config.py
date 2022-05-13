"""Application settings."""
import enum
from logging import getLogger
from typing import Final, Sequence

from pydantic import BaseSettings, Field

logger: Final = getLogger(__file__)


# TODO: Move to stac-pydantic
# Does that make sense now? The shift to json schema rather than a well-known enumeration makes that less obvious.
class ApiExtensions(enum.Enum):
    """Enumeration of available stac api extensions.

    Ref: https://github.com/radiantearth/stac-api-spec/tree/master/extensions
    """

    context = "context"
    fields = "fields"
    filter = "filter"
    query = "query"
    sort = "sort"
    transaction = "transaction"


class AddOns(enum.Enum):
    """Enumeration of available third party add ons."""

    bulk_transaction = "bulk-transaction"


class FastApiAppSettings(BaseSettings):
    """API settings."""

    allow_origins: Sequence[str] = Field(("*",), env="cors_allow_origins")
    allow_methods: Sequence[str] = Field(("*",), env="cors_allow_methods")
    allow_headers: Sequence[str] = Field(("*",), env="cors_allow_headers")
    allow_credentials: bool = Field(False, env="cors_allow_credentials")
    allow_origin_regex: str = Field(None, env="cors_allow_origin_regex")
    expose_headers: Sequence[str] = Field(("*",), env="cors_expose_headers")
    max_age: int = Field(600, env="cors_max_age")


fastapi_app_settings: Final = FastApiAppSettings()
