"""base api extension"""
import abc
from dataclasses import dataclass

from fastapi import FastAPI


@dataclass  # type:ignore
class ApiExtension(abc.ABC):
    """orchestration for API extensions"""

    @abc.abstractmethod
    def register(self, api: FastAPI) -> None:
        """register extension with the application"""
        ...
