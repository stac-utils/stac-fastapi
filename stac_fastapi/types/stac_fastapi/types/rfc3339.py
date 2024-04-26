"""rfc3339."""

import re
from datetime import datetime, timezone
from typing import Optional, Tuple, Union

import iso8601
from fastapi import HTTPException
from pystac.utils import datetime_to_str

RFC33339_PATTERN = (
    r"^(\d\d\d\d)\-(\d\d)\-(\d\d)(T|t)(\d\d):(\d\d):(\d\d)([.]\d+)?"
    r"(Z|([-+])(\d\d):(\d\d))$"
)

DateTimeType = Union[
    datetime,
    Tuple[datetime, datetime],
    Tuple[datetime, None],
    Tuple[None, datetime],
]


def rfc3339_str_to_datetime(s: str) -> datetime:
    """Convert a string conforming to RFC 3339 to a :class:`datetime.datetime`.

    Uses :meth:`iso8601.parse_date` under the hood.

    Args:
        s (str) : The string to convert to :class:`datetime.datetime`.

    Returns:
        str: The datetime represented by the ISO8601 (RFC 3339) formatted string.

    Raises:
        ValueError: If the string is not a valid RFC 3339 string.
    """
    # Uppercase the string
    s = s.upper()

    # Match against RFC3339 regex.
    result = re.match(RFC33339_PATTERN, s)
    if not result:
        raise ValueError("Invalid RFC3339 datetime.")

    # Parse with pyiso8601
    return iso8601.parse_date(s)


def parse_single_date(date_str: str) -> datetime:
    """
    Parse a single RFC3339 date string into a datetime object.

    Args:
        date_str (str): A string representing the date in RFC3339 format.

    Returns:
        datetime: A datetime object parsed from the date_str.

    Raises:
        ValueError: If the date_str is empty or contains the placeholder '..'.
    """
    if ".." in date_str or not date_str:
        raise ValueError("Invalid date format.")
    return rfc3339_str_to_datetime(date_str)


def str_to_interval(interval: Optional[str]) -> Optional[DateTimeType]:
    """
    Extract a tuple of datetime objects from an interval string defined by the OGC API.
    The interval can either be a single datetime or a range with start and end datetime.

    Args:
        interval (Optional[str]): The interval string to convert to datetime objects,
        or None if no datetime is specified.

    Returns:
        Optional[DateTimeType]: A tuple of datetime.datetime objects or
        None if input is None.

    Raises:
        HTTPException: If the string is not valid for various reasons such as being empty,
        having more than one slash, or if date formats are invalid.
    """
    if interval is None:
        return None

    if not interval:
        raise HTTPException(status_code=400, detail="Empty interval string is invalid.")

    values = interval.split("/")
    if len(values) > 2:
        raise HTTPException(
            status_code=400,
            detail="Interval string contains more than one forward slash.",
        )

    try:
        start = parse_single_date(values[0]) if values[0] not in ["..", ""] else None
        end = (
            parse_single_date(values[1])
            if len(values) > 1 and values[1] not in ["..", ""]
            else None
        )
    except (ValueError, iso8601.ParseError) as e:
        raise HTTPException(status_code=400, detail=str(e))

    if start is None and end is None:
        raise HTTPException(
            status_code=400, detail="Double open-ended intervals are not allowed."
        )
    if start is not None and end is not None and start > end:
        raise HTTPException(
            status_code=400, detail="Start datetime cannot be before end datetime."
        )

    return start, end


def now_in_utc() -> datetime:
    """Return a datetime value of now with the UTC timezone applied."""
    return datetime.now(timezone.utc)


def now_to_rfc3339_str() -> str:
    """Return an RFC 3339 string representing now."""
    return datetime_to_str(now_in_utc())
