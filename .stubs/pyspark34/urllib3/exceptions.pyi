from .packages.six.moves.http_client import IncompleteRead as httplib_IncompleteRead
from _typeshed import Incomplete

class HTTPError(Exception):
    """Base exception used by this module."""
class HTTPWarning(Warning):
    """Base warning used by this module."""

class PoolError(HTTPError):
    """Base exception for errors caused within a pool."""
    pool: Incomplete
    def __init__(self, pool, message) -> None: ...
    def __reduce__(self): ...

class RequestError(PoolError):
    """Base exception for PoolErrors that have associated URLs."""
    url: Incomplete
    def __init__(self, pool, url, message) -> None: ...
    def __reduce__(self): ...

class SSLError(HTTPError):
    """Raised when SSL certificate fails in an HTTPS connection."""

class ProxyError(HTTPError):
    """Raised when the connection to a proxy fails."""
    original_error: Incomplete
    def __init__(self, message, error, *args) -> None: ...

class DecodeError(HTTPError):
    """Raised when automatic decoding based on Content-Type fails."""
class ProtocolError(HTTPError):
    """Raised when something unexpected happens mid-request/response."""
ConnectionError = ProtocolError

class MaxRetryError(RequestError):
    """Raised when the maximum number of retries is exceeded.

    :param pool: The connection pool
    :type pool: :class:`~urllib3.connectionpool.HTTPConnectionPool`
    :param string url: The requested Url
    :param exceptions.Exception reason: The underlying error

    """
    reason: Incomplete
    def __init__(self, pool, url, reason: Incomplete | None = None) -> None: ...

class HostChangedError(RequestError):
    """Raised when an existing pool gets a request for a foreign host."""
    retries: Incomplete
    def __init__(self, pool, url, retries: int = 3) -> None: ...

class TimeoutStateError(HTTPError):
    """Raised when passing an invalid state to a timeout"""
class TimeoutError(HTTPError):
    """Raised when a socket timeout error occurs.

    Catching this error will catch both :exc:`ReadTimeoutErrors
    <ReadTimeoutError>` and :exc:`ConnectTimeoutErrors <ConnectTimeoutError>`.
    """
class ReadTimeoutError(TimeoutError, RequestError):
    """Raised when a socket timeout occurs while receiving data from a server"""
class ConnectTimeoutError(TimeoutError):
    """Raised when a socket timeout occurs while connecting to a server"""
class NewConnectionError(ConnectTimeoutError, PoolError):
    """Raised when we fail to establish a new connection. Usually ECONNREFUSED."""
class EmptyPoolError(PoolError):
    """Raised when a pool runs out of connections and no more are allowed."""
class ClosedPoolError(PoolError):
    """Raised when a request enters a pool after the pool has been closed."""
class LocationValueError(ValueError, HTTPError):
    """Raised when there is something wrong with a given URL input."""

class LocationParseError(LocationValueError):
    """Raised when get_host or similar fails to parse the URL input."""
    location: Incomplete
    def __init__(self, location) -> None: ...

class URLSchemeUnknown(LocationValueError):
    """Raised when a URL input has an unsupported scheme."""
    scheme: Incomplete
    def __init__(self, scheme) -> None: ...

class ResponseError(HTTPError):
    """Used as a container for an error reason supplied in a MaxRetryError."""
    GENERIC_ERROR: str
    SPECIFIC_ERROR: str

class SecurityWarning(HTTPWarning):
    """Warned when performing security reducing actions"""
class SubjectAltNameWarning(SecurityWarning):
    """Warned when connecting to a host with a certificate missing a SAN."""
class InsecureRequestWarning(SecurityWarning):
    """Warned when making an unverified HTTPS request."""
class SystemTimeWarning(SecurityWarning):
    """Warned when system time is suspected to be wrong"""
class InsecurePlatformWarning(SecurityWarning):
    """Warned when certain TLS/SSL configuration is not available on a platform."""
class SNIMissingWarning(HTTPWarning):
    """Warned when making a HTTPS request without SNI available."""
class DependencyWarning(HTTPWarning):
    """
    Warned when an attempt is made to import a module with missing optional
    dependencies.
    """
class ResponseNotChunked(ProtocolError, ValueError):
    """Response needs to be chunked in order to read it as chunks."""
class BodyNotHttplibCompatible(HTTPError):
    """
    Body should be :class:`http.client.HTTPResponse` like
    (have an fp attribute which returns raw chunks) for read_chunked().
    """

class IncompleteRead(HTTPError, httplib_IncompleteRead):
    """
    Response length doesn't match expected Content-Length

    Subclass of :class:`http.client.IncompleteRead` to allow int value
    for ``partial`` to avoid creating large objects on streamed reads.
    """
    def __init__(self, partial, expected) -> None: ...

class InvalidChunkLength(HTTPError, httplib_IncompleteRead):
    """Invalid chunk length in a chunked response."""
    response: Incomplete
    length: Incomplete
    def __init__(self, response, length) -> None: ...

class InvalidHeader(HTTPError):
    """The header provided was somehow invalid."""

class ProxySchemeUnknown(AssertionError, URLSchemeUnknown):
    """ProxyManager does not support the supplied scheme"""
    def __init__(self, scheme) -> None: ...

class ProxySchemeUnsupported(ValueError):
    """Fetching HTTPS resources through HTTPS proxies is unsupported"""

class HeaderParsingError(HTTPError):
    """Raised by assert_header_parsing, but we convert it to a log.warning statement."""
    def __init__(self, defects, unparsed_data) -> None: ...

class UnrewindableBodyError(HTTPError):
    """urllib3 encountered an error when trying to rewind a body"""
