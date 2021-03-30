"""Application settings."""
import enum


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
