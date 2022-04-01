"""rfc3339."""

from datetime import datetime, timezone
from typing import Optional, Tuple

import dateutil
from pystac.utils import datetime_to_str


def rfc3339_str_to_datetime(s: str) -> datetime:
    """Convert a string conforming to RFC 3339 to a :class:`datetime.datetime`.

    Uses :meth:`dateutil.parser.isoparse` under the hood.

    Args:
        s (str) : The string to convert to :class:`datetime.datetime`.

    Returns:
        str: The datetime represented by the ISO8601 (RFC 3339) formatted string.

    Raises:
        ValueError: If the string is not a valid RFC 3339 string.
    """
    return dateutil.parser.isoparse(s)


def str_to_interval(
    interval: str,
) -> Optional[Tuple[Optional[datetime], Optional[datetime]]]:
    """Extract a tuple of datetimes from an interval string.

    Interval strings are defined by
    OGC API - Features Part 1 for the datetime query parameter value. These follow the
    form '1985-04-12T23:20:50.52Z/1986-04-12T23:20:50.52Z', and allow either the start
    or end (but not both) to be open-ended with '..' or ''.

    Args:
        interval (str) : The interval string to convert to a :class:`datetime.datetime`
        tuple.

    Raises:
        ValueError: If the string is not a valid interval string.
    """
    if not interval:
        raise ValueError("Empty interval string is invalid.")

    values = interval.split("/")
    if len(values) != 2:
        raise ValueError(
            f"Interval string '{interval}' contains more than one forward slash."
        )

    start = None
    end = None
    if not values[0] in ["..", ""]:
        start = rfc3339_str_to_datetime(values[0])
    if not values[1] in ["..", ""]:
        end = rfc3339_str_to_datetime(values[1])

    if start is None and end is None:
        raise ValueError("Double open-ended intervals are not allowed.")
    if start is not None and end is not None and start > end:
        raise ValueError("Start datetime cannot be before end datetime.")
    else:
        return start, end


def now_in_utc() -> datetime:
    """Return a datetime value of now with the UTC timezone applied."""
    return datetime.now(timezone.utc)


def now_to_rfc3339_str() -> str:
    """Return an RFC 3339 string representing now."""
    return datetime_to_str(now_in_utc())
