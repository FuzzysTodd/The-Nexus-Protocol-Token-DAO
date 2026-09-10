from _typeshed import Incomplete

class PublicError(RuntimeError):
    '''An error whose text does not contain sensitive information.

    Fields:
      http_code: Integer between 400 and 599 inclusive (e.g., 404).
      headers: List of additional key-value pairs to include in the
        response body, like `[("Allow", "GET")]` for HTTP 405 or
        `[("WWW-Authenticate", "Digest")]` for HTTP 401. May be empty.
    '''
    http_code: int
    headers: Incomplete
    def __init__(self, details) -> None: ...

class InvalidArgumentError(PublicError):
    """Client specified an invalid argument.

    The text of this error is assumed not to contain sensitive data,
    and so may appear in (e.g.) the response body of a failed HTTP
    request.

    Corresponds to HTTP 400 Bad Request or Google error code `INVALID_ARGUMENT`.
    """
    http_code: int
    def __init__(self, details: Incomplete | None = None) -> None: ...

class NotFoundError(PublicError):
    """Some requested entity (e.g., file or directory) was not found.

    The text of this error is assumed not to contain sensitive data,
    and so may appear in (e.g.) the response body of a failed HTTP
    request.

    Corresponds to HTTP 404 Not Found or Google error code `NOT_FOUND`.
    """
    http_code: int
    def __init__(self, details: Incomplete | None = None) -> None: ...

class UnauthenticatedError(PublicError):
    """Request does not have valid authentication credentials for the operation.

    The text of this error is assumed not to contain sensitive data,
    and so may appear in (e.g.) the response body of a failed HTTP
    request.

    Corresponds to HTTP 401 Unauthorized (despite the name) or Google
    error code `UNAUTHENTICATED`. HTTP 401 responses are required to
    contain a `WWW-Authenticate` challenge, so `UnauthenticatedError`
    values are, too.
    """
    http_code: int
    def __init__(self, details: Incomplete | None = None, *, challenge) -> None:
        """Initialize an `UnauthenticatedError`.

        Args;
          details: Optional public, user-facing error message, as a
            string or any value that can be converted to string, or
            `None` to omit details.
          challenge: String value of the `WWW-Authenticate` HTTP header
            as described in RFC 7235.
        """

class PermissionDeniedError(PublicError):
    """The caller does not have permission to execute the specified operation.

    The text of this error is assumed not to contain sensitive data,
    and so may appear in (e.g.) the response body of a failed HTTP
    request.

    Corresponds to HTTP 403 Forbidden or Google error code `PERMISSION_DENIED`.
    """
    http_code: int
    def __init__(self, details: Incomplete | None = None) -> None: ...
