"""base api extension."""
import abc

import attr
from fastapi import FastAPI

from typing import List


@attr.s
class ApiExtension(abc.ABC):
    """Abstract base class for defining API extensions."""

    conformance_classes: List[str] = attr.ib()

    @abc.abstractmethod
    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
