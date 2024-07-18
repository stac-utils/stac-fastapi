from datetime import datetime, timezone

import pytest
from fastapi import HTTPException

from stac_fastapi.types.rfc3339 import (
    now_in_utc,
    now_to_rfc3339_str,
    rfc3339_str_to_datetime,
    str_to_interval,
)

invalid_datetimes = [
    "1985-04-12",  # date only
    "1937-01-01T12:00:27.87+0100",  # invalid TZ format, no sep :
    "37-01-01T12:00:27.87Z",  # invalid year, must be 4 digits
    "1985-12-12T23:20:50.52",  # no TZ
    "21985-12-12T23:20:50.52Z",  # year must be 4 digits
    "1985-13-12T23:20:50.52Z",  # month > 12
    "1985-12-32T23:20:50.52Z",  # day > 31
    "1985-12-01T25:20:50.52Z",  # hour > 24
    "1985-12-01T00:60:50.52Z",  # minute > 59
    "1985-12-01T00:06:61.52Z",  # second > 60
    "1985-04-12T23:20:50.Z",  # fractional sec . but no frac secs
    "1985-04-12T23:20:50,Z",  # fractional sec , but no frac secs
    "1990-12-31T23:59:61Z",  # second > 60 w/o fractional seconds
    "1985-04-12T23:20:50,52Z",  # comma as frac sec sep allowed in ISO8601 but not RFC3339
]

valid_datetimes = [
    "1985-04-12T23:20:50.52Z",
    "1996-12-19T16:39:57-00:00",
    "1996-12-19T16:39:57+00:00",
    "1996-12-19T16:39:57-08:00",
    "1996-12-19T16:39:57+08:00",
    "1937-01-01T12:00:27.87+01:00",
    "1985-04-12T23:20:50.52Z",
    "1937-01-01T12:00:27.8710+01:00",
    "1937-01-01T12:00:27.8+01:00",
    "1937-01-01T12:00:27.8Z",
    "2020-07-23T00:00:00.000+03:00",
    "2020-07-23T00:00:00+03:00",
    "1985-04-12t23:20:50.000z",
    "2020-07-23T00:00:00Z",
    "2020-07-23T00:00:00.0Z",
    "2020-07-23T00:00:00.01Z",
    "2020-07-23T00:00:00.012Z",
    "2020-07-23T00:00:00.0123Z",
    "2020-07-23T00:00:00.01234Z",
    "2020-07-23T00:00:00.012345Z",
    "2020-07-23T00:00:00.0123456Z",
    "2020-07-23T00:00:00.01234567Z",
    "2020-07-23T00:00:00.012345678Z",
]

invalid_intervals = [
    "/"
    "../"
    "/.."
    "../.."
    "/1984-04-12T23:20:50.52Z/1985-04-12T23:20:50.52Z",  # extra start /
    "1984-04-12T23:20:50.52Z/1985-04-12T23:20:50.52Z/",  # extra end /
    "1986-04-12T23:20:50.52Z/1985-04-12T23:20:50.52Z",  # start > end
]

valid_intervals = [
    "../1985-04-12T23:20:50.52Z",
    "1985-04-12T23:20:50.52Z/..",
    "/1985-04-12T23:20:50.52Z",
    "1985-04-12T23:20:50.52Z/",
    "1985-04-12T23:20:50.52Z/1986-04-12T23:20:50.52Z",
    "1985-04-12T23:20:50.52+01:00/1986-04-12T23:20:50.52+01:00",
    "1985-04-12T23:20:50.52-01:00/1986-04-12T23:20:50.52-01:00",
]


@pytest.mark.parametrize("test_input", invalid_datetimes)
def test_parse_invalid_str_to_datetime(test_input):
    with pytest.raises(ValueError):
        rfc3339_str_to_datetime(test_input)


@pytest.mark.parametrize("test_input", valid_datetimes)
def test_parse_valid_str_to_datetime(test_input):
    assert rfc3339_str_to_datetime(test_input)


@pytest.mark.parametrize("test_input", invalid_intervals)
def test_str_to_interval_with_invalid_interval(test_input):
    with pytest.raises(HTTPException) as exc_info:
        str_to_interval(test_input)
    assert (
        exc_info.value.status_code == 400
    ), "str_to_interval should return a 400 status code for invalid interval"


@pytest.mark.parametrize("test_input", invalid_datetimes)
def test_str_to_interval_with_invalid_datetime(test_input):
    with pytest.raises(HTTPException) as exc_info:
        str_to_interval(test_input)
    assert (
        exc_info.value.status_code == 400
    ), "str_to_interval should return a 400 status code for invalid datetime"


@pytest.mark.parametrize("test_input", valid_intervals)
def test_str_to_interval_with_valid_interval(test_input):
    assert isinstance(
        str_to_interval(test_input), tuple
    ), "str_to_interval should return tuple for multi-value input"


@pytest.mark.parametrize("test_input", valid_datetimes)
def test_str_to_interval_with_valid_datetime(test_input):
    assert isinstance(
        str_to_interval(test_input), datetime
    ), "str_to_interval should return single datetime for single-value input"


def test_str_to_interval_with_none():
    """Test that str_to_interval returns None when provided with None."""
    assert (
        str_to_interval(None) is None
    ), "str_to_interval should return None when input is None"


def test_now_functions() -> None:
    now1 = now_in_utc()
    now2 = now_in_utc()

    assert now1 < now2
    assert now1.tzinfo == timezone.utc

    rfc3339_str_to_datetime(now_to_rfc3339_str())
