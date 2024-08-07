"""Application settings."""

import enum


# TODO: Move to stac-pydantic
# Does that make sense now? The shift to json schema rather than a well-known
# enumeration makes that less obvious.
class ApiExtensions(enum.Enum):
    """Enumeration of available stac api extensions.

    Ref: https://github.com/stac-api-extensions
    """

    fields = "fields"
    filter = "filter"
    query = "query"
    sort = "sort"
    transaction = "transaction"
    aggregation = "aggregation"
    collection_search = "collection-search"
    free_text = "free-text"


class AddOns(enum.Enum):
    """Enumeration of available third party add ons."""

    bulk_transaction = "bulk-transaction"
