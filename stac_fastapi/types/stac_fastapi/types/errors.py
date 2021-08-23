"""stac_fastapi.types.errors module."""


class StacApiError(Exception):
    """Generic API error."""

    pass


class ConflictError(StacApiError):
    """Database conflict."""

    pass


class NotFoundError(StacApiError):
    """Resource not found."""

    pass


class ForeignKeyError(StacApiError):
    """Foreign key error (collection does not exist)."""

    pass


class DatabaseError(StacApiError):
    """Generic database errors."""

    pass


class InvalidQueryParameter(StacApiError):
    """Error for unknown or invalid query parameters.

    Used to capture errors that should respond according to
    http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#query_parameters
    """

    pass
