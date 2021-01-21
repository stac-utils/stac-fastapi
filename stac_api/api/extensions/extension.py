"""base api extension"""
import abc

import attr
from fastapi import FastAPI


@attr.s
class ApiExtension(abc.ABC):
    """orchestration for API extensions"""

    @abc.abstractmethod
    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        ...
