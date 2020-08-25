"""FastAPI dependencies."""

from contextvars import ContextVar

# TODO: Find a new home
READER: ContextVar = ContextVar("reader")
WRITER: ContextVar = ContextVar("writer")
