"""rfc3339."""

from datetime import datetime, timezone

import ciso8601


def parse_rfc3339(value: str) -> datetime:
    """Doc."""
    return ciso8601.parse_rfc3339(value)


def rfc3339_str(value: datetime, use_z: bool = True) -> str:
    """Doc."""
    if not value.tzinfo:
        value = value.replace(tzinfo=timezone.utc)

    str_value = value.isoformat()
    str_value = str_value.replace("+00:00", "Z") if use_z else str_value
    return str_value


def now_in_utc() -> datetime:
    """Doc."""
    return datetime.now(timezone.utc)


def now_as_rfc3339_str() -> str:
    """Doc."""
    return rfc3339_str(now_in_utc())
