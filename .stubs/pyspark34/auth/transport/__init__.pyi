import abc
from _typeshed import Incomplete

DEFAULT_RETRYABLE_STATUS_CODES: Incomplete
DEFAULT_REFRESH_STATUS_CODES: Incomplete
DEFAULT_MAX_REFRESH_ATTEMPTS: int

class Response(metaclass=abc.ABCMeta):
    """HTTP Response data."""
    @property
    @abc.abstractmethod
    def status(self):
        """int: The HTTP status code."""
    @property
    @abc.abstractmethod
    def headers(self):
        """Mapping[str, str]: The HTTP response headers."""
    @property
    @abc.abstractmethod
    def data(self):
        """bytes: The response body."""

class Request(metaclass=abc.ABCMeta):
    """Interface for a callable that makes HTTP requests.

    Specific transport implementations should provide an implementation of
    this that adapts their specific request / response API.

    .. automethod:: __call__
    """
    @abc.abstractmethod
    def __call__(self, url, method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None, timeout: Incomplete | None = None, **kwargs):
        """Make an HTTP request.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload / body in HTTP request.
            headers (Mapping[str, str]): Request headers.
            timeout (Optional[int]): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                transport-specific default timeout will be used.
            kwargs: Additionally arguments passed on to the transport's
                request method.

        Returns:
            Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """
