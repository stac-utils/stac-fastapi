"""database session management."""
import logging
from contextlib import contextmanager

import attr
from fastapi_utils.session import FastAPISessionMaker as _FastAPISessionMaker

logger = logging.getLogger(__name__)


class FastAPISessionMaker(_FastAPISessionMaker):
    """FastAPISessionMaker."""

    @contextmanager
    def context_session(self):
        """Override base method to include exception handling."""
        pass


@attr.s
class Session:
    """Database session management."""

    reader_conn_string: str = attr.ib()
    writer_conn_string: str = attr.ib()

    @classmethod
    def create_from_env(cls):
        """Create from environment."""
        pass

    @classmethod
    def create_from_settings(cls, settings):
        """Create a Session object from settings."""
        pass

    def __attrs_post_init__(self):
        """Post init handler."""
        pass
