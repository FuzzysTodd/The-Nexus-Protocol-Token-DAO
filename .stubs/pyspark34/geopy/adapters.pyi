import abc
from _typeshed import Incomplete
from geopy.exc import GeocoderParseError as GeocoderParseError, GeocoderServiceError as GeocoderServiceError, GeocoderTimedOut as GeocoderTimedOut, GeocoderUnavailable as GeocoderUnavailable, GeopyError as GeopyError
from geopy.util import logger as logger
from requests.adapters import HTTPAdapter as RequestsHTTPAdapter

requests_available: bool
RequestsHTTPAdapter = object
aiohttp_available: bool

class AdapterHTTPError(IOError):
    """An exception which must be raised by adapters when an HTTP response
    with a non-successful status code has been received.

    Base Geocoder class translates this exception to an instance of
    :class:`geopy.exc.GeocoderServiceError`.

    """
    status_code: Incomplete
    headers: Incomplete
    text: Incomplete
    def __init__(self, message, *, status_code, headers, text) -> None:
        """

        :param str message: Standard exception message.
        :param int status_code: HTTP status code.
        :param dict headers: HTTP response readers. A mapping object
            with lowercased or case-insensitive keys.

            .. versionadded:: 2.2
        :param str text: HTTP body text.
        """

def get_retry_after(headers):
    """Return Retry-After header value in seconds.

    .. versionadded:: 2.2
    """

class BaseAdapter(abc.ABC, metaclass=abc.ABCMeta):
    """Base class for an Adapter.

    There are two types of adapters:

    - :class:`.BaseSyncAdapter` -- synchronous adapter,
    - :class:`.BaseAsyncAdapter` -- asynchronous (asyncio) adapter.

    Concrete adapter implementations must extend one of the two
    base adapters above.

    See :attr:`geopy.geocoders.options.default_adapter_factory`
    for details on how to specify an adapter to be used by geocoders.

    """
    is_available: bool
    def __init__(self, *, proxies, ssl_context) -> None:
        '''Initialize adapter.

        :param dict proxies: An urllib-style proxies dict, e.g.
            ``{"http": "192.0.2.0:8080", "https": "192.0.2.0:8080"}``,
            ``{"https": "http://user:passw0rd@192.0.2.0:8080""}``.
            See :attr:`geopy.geocoders.options.default_proxies` (note
            that Adapters always receive a dict: the string proxy
            is transformed to dict in the base
            :class:`geopy.geocoders.base.Geocoder` class.).

        :type ssl_context: :class:`ssl.SSLContext`
        :param ssl_context:
            See :attr:`geopy.geocoders.options.default_ssl_context`.

        '''
    @abc.abstractmethod
    def get_json(self, url, *, timeout, headers):
        """Same as ``get_text`` except that the response is expected
        to be a valid JSON. The value returned is the parsed JSON.

        :class:`geopy.exc.GeocoderParseError` must be raised if
        the response cannot be parsed.

        :param str url: The target URL.

        :param float timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict headers: A dict with custom HTTP request headers.
        """
    @abc.abstractmethod
    def get_text(self, url, *, timeout, headers):
        """Make a GET request and return the response as string.

        This method should not raise any exceptions other than these:

        - :class:`geopy.adapters.AdapterHTTPError` should be raised if the response
          was successfully retrieved but the status code was non-successful.
        - :class:`geopy.exc.GeocoderTimedOut` should be raised when the request
          times out.
        - :class:`geopy.exc.GeocoderUnavailable` should be raised when the target
          host is unreachable.
        - :class:`geopy.exc.GeocoderServiceError` is the least specific error
          in the exceptions hierarchy and should be raised in any other cases.

        :param str url: The target URL.

        :param float timeout:
            See :attr:`geopy.geocoders.options.default_timeout`.

        :param dict headers: A dict with custom HTTP request headers.
        """

class BaseSyncAdapter(BaseAdapter, metaclass=abc.ABCMeta):
    """Base class for synchronous adapters.
    """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class BaseAsyncAdapter(BaseAdapter, metaclass=abc.ABCMeta):
    """Base class for asynchronous adapters.

    See also: :ref:`Async Mode <async_mode>`.
    """
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...

class URLLibAdapter(BaseSyncAdapter):
    """The fallback adapter which uses urllib from the Python standard
    library, see :func:`urllib.request.urlopen`.

    urllib doesn't support keep-alives, request retries,
    doesn't persist Cookies and is HTTP/1.1 only.

    urllib was the only available option
    for making requests in geopy 1.x, so this adapter behaves the same
    as geopy 1.x in terms of HTTP requests.
    """
    urlopen: Incomplete
    def __init__(self, *, proxies, ssl_context) -> None: ...
    def get_json(self, url, *, timeout, headers): ...
    def get_text(self, url, *, timeout, headers): ...

class RequestsAdapter(BaseSyncAdapter):
    """The adapter which uses `requests`_ library.

    .. _requests: https://requests.readthedocs.io

    `requests` supports keep-alives, retries, persists Cookies,
    allows response compression and uses HTTP/1.1 [currently].

    ``requests`` package must be installed in order to use this adapter.
    """
    is_available = requests_available
    session: Incomplete
    def __init__(self, *, proxies, ssl_context, pool_connections: int = 10, pool_maxsize: int = 10, max_retries: int = 2, pool_block: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __del__(self) -> None: ...
    def get_text(self, url, *, timeout, headers): ...
    def get_json(self, url, *, timeout, headers): ...

class AioHTTPAdapter(BaseAsyncAdapter):
    """The adapter which uses `aiohttp`_ library.

    .. _aiohttp: https://docs.aiohttp.org/

    `aiohttp` supports keep-alives, persists Cookies, allows response
    compression and uses HTTP/1.1 [currently].

    ``aiohttp`` package must be installed in order to use this adapter.
    """
    is_available = aiohttp_available
    proxies: Incomplete
    ssl_context: Incomplete
    def __init__(self, *, proxies, ssl_context) -> None: ...
    @property
    def session(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def get_text(self, url, *, timeout, headers): ...
    async def get_json(self, url, *, timeout, headers): ...

class RequestsHTTPWithSSLContextAdapter(RequestsHTTPAdapter):
    def __init__(self, *, ssl_context: Incomplete | None = None, **kwargs) -> None: ...
    def init_poolmanager(self, *args, **kwargs): ...
    def proxy_manager_for(self, proxy, **proxy_kwargs): ...
    def cert_verify(self, conn, url, verify, cert) -> None: ...
