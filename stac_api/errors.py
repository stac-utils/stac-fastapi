from dataclasses import dataclass


@dataclass
class ConflictError(Exception):
    message: str


@dataclass
class NotFoundError(Exception):
    message: str


@dataclass
class ForeignKeyError(Exception):
    message: str


@dataclass
class DatabaseError(Exception):
    message: str
