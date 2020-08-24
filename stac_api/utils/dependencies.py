"""FastAPI dependencies."""

from contextvars import ContextVar
from typing import Callable, List

from starlette.requests import Request

READER: ContextVar = ContextVar("reader")
WRITER: ContextVar = ContextVar("writer")


def parse_list_factory(varname) -> Callable[[Request], List[str]]:
    """Parse the value of a specific parameter from comma-delimited string to list of strings"""

    def _parse(request: Request):
        param = request.query_params.get(varname)
        return param.split(",") if param else param

    return _parse
