"""rfc3339."""

from datetime import datetime, timezone
from typing import Optional, Tuple

import ciso8601
import pystac


def parse_rfc3339(value: str) -> datetime:
    """Doc."""
    return ciso8601.parse_rfc3339(value)


def now_in_utc() -> datetime:
    """Doc."""
    return datetime.now(timezone.utc)


def now_as_rfc3339_str() -> str:
    """Doc."""
    return pystac.utils.datetime_to_str(now_in_utc())


def parse_interval(
    value: str,
) -> Optional[Tuple[Optional[datetime], Optional[datetime]]]:
    """Extract a tuple of datetimes from an interval string."""
    if not value:
        return None

    values = value.split("/")
    if len(values) != 2:
        return None

    start = None
    end = None
    if not values[0] in ["..", ""]:
        start = parse_rfc3339(values[0])
    if not values[1] in ["..", ""]:
        end = parse_rfc3339(values[1])

    if start is None and end is None:
        return None
    else:
        return start, end
