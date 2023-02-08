import pytest
from pydantic import ValidationError

from stac_fastapi.types.search import BaseSearchPostRequest


@pytest.mark.parametrize("value", [0, -1])
def test_limit_ge(value):
    with pytest.raises(ValidationError):
        BaseSearchPostRequest(limit=value)


@pytest.mark.parametrize("value", [1, 10_000])
def test_limit(value):
    search = BaseSearchPostRequest(limit=value)
    assert search.limit == value


@pytest.mark.parametrize("value", [10_001, 100_000, 1_000_000])
def test_limit_le(value):
    search = BaseSearchPostRequest(limit=value)
    assert search.limit == 10_000
