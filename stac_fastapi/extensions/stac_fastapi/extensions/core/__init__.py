"""core backwards compatibility namespace."""

import warnings

from ..aggregation import AggregationExtension
from ..collection_search import CollectionSearchExtension, CollectionSearchPostExtension
from ..fields import FieldsExtension
from ..filter import (
    CollectionSearchFilterExtension,
    FilterExtension,
    ItemCollectionFilterExtension,
    SearchFilterExtension,
)
from ..free_text import FreeTextAdvancedExtension, FreeTextExtension
from ..pagination import (
    OffsetPaginationExtension,
    PaginationExtension,
    TokenPaginationExtension,
)
from ..query import QueryExtension
from ..sort import SortExtension
from ..transaction import TransactionExtension

# Issue a warning so users know to migrate, but the code won't break
warnings.warn(
    """The 'stac_fastapi.extensions.core' namespace is deprecated
      and will be removed in a future release.
    Please import extensions directly from 'stac_fastapi.extensions' instead.""",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = (
    "AggregationExtension",
    "FieldsExtension",
    "FilterExtension",
    "FreeTextExtension",
    "FreeTextAdvancedExtension",
    "OffsetPaginationExtension",
    "PaginationExtension",
    "QueryExtension",
    "SortExtension",
    "TokenPaginationExtension",
    "TransactionExtension",
    "CollectionSearchExtension",
    "CollectionSearchPostExtension",
    "SearchFilterExtension",
    "ItemCollectionFilterExtension",
    "CollectionSearchFilterExtension",
)
