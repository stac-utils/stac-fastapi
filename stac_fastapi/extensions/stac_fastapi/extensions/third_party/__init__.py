"""third_party backwards compatibility namespace."""

import warnings

from ..bulk_transactions import BulkTransactionExtension

# Issue a warning so users know to migrate, but the code won't break
warnings.warn(
    """The 'stac_fastapi.extensions.third_party' namespace is deprecated
     and will be removed in a future release.
    Please import extensions directly from 'stac_fastapi.extensions' instead.""",
    DeprecationWarning,
    stacklevel=2,
)


__all__ = ("BulkTransactionExtension",)
