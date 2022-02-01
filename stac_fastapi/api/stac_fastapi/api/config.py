"""Application settings."""
import enum
import re
from logging import getLogger
from os import environ
from typing import Final, Sequence

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


def env_to_sequence(
    env_var: str, default: Sequence[str], sequence_separator: str = "|"
) -> Sequence[str]:
    """Retrieve a sequence of values from an env var string, or default if missing."""
    if env_var in environ:
        if re.search(re.escape(sequence_separator), environ[env_var]):
            return tuple(
                [part for part in environ[env_var].split(sequence_separator) if part]
            )
        else:
            return (environ[env_var],)
    else:
        return default


def env_to_str(env_var: str, default: str) -> str:
    """Retrieve a string from an env var, or default if missing."""
    if env_var in environ:
        return environ[env_var]
    else:
        return default


def env_to_bool(env_var: str, default: bool) -> bool:
    """Retrieve a bool from an env var, or default if missing."""
    if env_var in environ:
        if re.match("^(true|1)$", environ[env_var], re.IGNORECASE):
            return True
        if re.match("^(false|0)$", environ[env_var], re.IGNORECASE):
            return False
        logger.warning(f"{env_var} set but not a valid bool")
    return default


def env_to_int(env_var: str, default: int) -> int:
    """Retrieve an int from an env var, or default if missing."""
    if env_var in environ:
        value = environ[env_var].strip()
        if value.isdigit():
            return int(value)
        else:
            logger.warning(f"{env_var} set but not a valid int")
    return default
