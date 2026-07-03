import aiohttp
from _typeshed import Incomplete
from google.auth import transport

class _CombinedResponse(transport.Response):
    """
    In order to more closely resemble the `requests` interface, where a raw
    and deflated content could be accessed at once, this class lazily reads the
    stream in `transport.Response` so both return forms can be used.

    The gzip and deflate transfer-encodings are automatically decoded for you
    because the default parameter for autodecompress into the ClientSession is set
    to False, and therefore we add this class to act as a wrapper for a user to be
    able to access both the raw and decoded response bodies - mirroring the sync
    implementation.
    """
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...
    async def raw_content(self): ...
    async def content(self): ...

class _Response(transport.Response):
    """
    Requests transport response adapter.

    Args:
        response (requests.Response): The raw Requests response.
    """
    def __init__(self, response) -> None: ...
    @property
    def status(self): ...
    @property
    def headers(self): ...
    @property
    def data(self): ...

class Request(transport.Request):
    """Requests request adapter.

    This class is used internally for making requests using asyncio transports
    in a consistent way. If you use :class:`AuthorizedSession` you do not need
    to construct or use this class directly.

    This class can be useful if you want to manually refresh a
    :class:`~google.auth.credentials.Credentials` instance::

        import google.auth.transport.aiohttp_requests

        request = google.auth.transport.aiohttp_requests.Request()

        credentials.refresh(request)

    Args:
        session (aiohttp.ClientSession): An instance :class:`aiohttp.ClientSession` used
            to make HTTP requests. If not specified, a session will be created.

    .. automethod:: __call__
    """
    session: Incomplete
    def __init__(self, session: Incomplete | None = None) -> None: ...
    async def __call__(self, url, method: str = 'GET', body: Incomplete | None = None, headers: Incomplete | None = None, timeout=..., **kwargs):
        """
        Make an HTTP request using aiohttp.

        Args:
            url (str): The URL to be requested.
            method (Optional[str]):
                The HTTP method to use for the request. Defaults to 'GET'.
            body (Optional[bytes]):
                The payload or body in HTTP request.
            headers (Optional[Mapping[str, str]]):
                Request headers.
            timeout (Optional[int]): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                requests default timeout will be used.
            kwargs: Additional arguments passed through to the underlying
                requests :meth:`requests.Session.request` method.

        Returns:
            google.auth.transport.Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """

class AuthorizedSession(aiohttp.ClientSession):
    """This is an async implementation of the Authorized Session class. We utilize an
    aiohttp transport instance, and the interface mirrors the google.auth.transport.requests
    Authorized Session class, except for the change in the transport used in the async use case.

    A Requests Session class with credentials.

    This class is used to perform requests to API endpoints that require
    authorization::

        from google.auth.transport import aiohttp_requests

        async with aiohttp_requests.AuthorizedSession(credentials) as authed_session:
            response = await authed_session.request(
                'GET', 'https://www.googleapis.com/storage/v1/b')

    The underlying :meth:`request` implementation handles adding the
    credentials' headers to the request and refreshing credentials as needed.

    Args:
        credentials (google.auth._credentials_async.Credentials):
            The credentials to add to the request.
        refresh_status_codes (Sequence[int]): Which HTTP status codes indicate
            that credentials should be refreshed and the request should be
            retried.
        max_refresh_attempts (int): The maximum number of times to attempt to
            refresh the credentials and retry the request.
        refresh_timeout (Optional[int]): The timeout value in seconds for
            credential refresh HTTP requests.
        auth_request (google.auth.transport.aiohttp_requests.Request):
            (Optional) An instance of
            :class:`~google.auth.transport.aiohttp_requests.Request` used when
            refreshing credentials. If not passed,
            an instance of :class:`~google.auth.transport.aiohttp_requests.Request`
            is created.
        kwargs: Additional arguments passed through to the underlying
            ClientSession :meth:`aiohttp.ClientSession` object.
    """
    credentials: Incomplete
    def __init__(self, credentials, refresh_status_codes=..., max_refresh_attempts=..., refresh_timeout: Incomplete | None = None, auth_request: Incomplete | None = None, auto_decompress: bool = False, **kwargs) -> None: ...
    async def request(self, method, url, data: Incomplete | None = None, headers: Incomplete | None = None, max_allowed_time: Incomplete | None = None, timeout=..., auto_decompress: bool = False, **kwargs):
        """Implementation of Authorized Session aiohttp request.

        Args:
            method (str):
                The http request method used (e.g. GET, PUT, DELETE)
            url (str):
                The url at which the http request is sent.
            data (Optional[dict]): Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the Request.
            headers (Optional[dict]): Dictionary of HTTP Headers to send with the
                Request.
            timeout (Optional[Union[float, aiohttp.ClientTimeout]]):
                The amount of time in seconds to wait for the server response
                with each individual request. Can also be passed as an
                ``aiohttp.ClientTimeout`` object.
            max_allowed_time (Optional[float]):
                If the method runs longer than this, a ``Timeout`` exception is
                automatically raised. Unlike the ``timeout`` parameter, this
                value applies to the total method execution time, even if
                multiple requests are made under the hood.

                Mind that it is not guaranteed that the timeout error is raised
                at ``max_allowed_time``. It might take longer, for example, if
                an underlying request takes a lot of time, but the request
                itself does not timeout, e.g. if a large file is being
                transmitted. The timout error will be raised after such
                request completes.
        """
