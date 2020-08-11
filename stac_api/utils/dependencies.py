from dataclasses import dataclass
from typing import Callable, List

from sqlalchemy.orm import Session
from starlette.requests import Request


@dataclass
class DatabaseConnectionError(Exception):
    message: str


def discover_base_url(request: Request):
    """Discover base url of a request"""
    return f"{request.url.scheme}://{request.url.netloc}"


def parse_list_factory(varname) -> Callable[[Request], List[str]]:
    """Parse the value of a specific parameter from comma-delimited string to list of strings"""

    def _parse(request: Request):
        param = request.query_params.get(varname)
        return param.split(",") if param else param

    return _parse


def database_reader_factory(request: Request) -> Session:
    """Instantiate the database reader session"""
    try:
        db = request.app.state.DB_READER()
        yield db
    finally:
        db.close()


def database_writer_factory(request: Request) -> Session:
    """Instantiate the database writer session"""
    try:
        db = request.app.state.DB_WRITER()
        yield db
    finally:
        db.close()
