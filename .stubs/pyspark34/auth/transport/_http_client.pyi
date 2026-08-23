from _typeshed import Incomplete
from google.auth import transport

class Response(transport.Response):
    """http.client transport response adapter.

    Args:
        response (http.client.HTTPResponse): The raw http client response.
    """
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    """http.client transport request adapter."""
    def __call__(self, url, method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None, timeout: Incomplete | None = None, **kwargs):
        """Make an HTTP request using http.client.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload / body in HTTP request.
            headers (Mapping): Request headers.
            timeout (Optional(int)): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                socket global default timeout will be used.
            kwargs: Additional arguments passed throught to the underlying
                :meth:`~http.client.HTTPConnection.request` method.

        Returns:
            Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """
