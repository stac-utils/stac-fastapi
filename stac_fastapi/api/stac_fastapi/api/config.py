"""Application settings."""
import enum


class AddOns(enum.Enum):
    """Enumeration of available third party add ons."""

    tiles = "tiles"
    bulk_transaction = "bulk-transaction"
