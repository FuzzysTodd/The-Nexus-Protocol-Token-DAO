import weakref
from .connection import BaseSSLError as BaseSSLError, BrokenPipeError as BrokenPipeError, DummyConnection as DummyConnection, HTTPConnection as HTTPConnection, HTTPException as HTTPException, HTTPSConnection as HTTPSConnection, VerifiedHTTPSConnection as VerifiedHTTPSConnection, port_by_scheme as port_by_scheme
from .exceptions import ClosedPoolError as ClosedPoolError, EmptyPoolError as EmptyPoolError, HeaderParsingError as HeaderParsingError, HostChangedError as HostChangedError, InsecureRequestWarning as InsecureRequestWarning, LocationValueError as LocationValueError, MaxRetryError as MaxRetryError, NewConnectionError as NewConnectionError, ProtocolError as ProtocolError, ProxyError as ProxyError, ReadTimeoutError as ReadTimeoutError, SSLError as SSLError, TimeoutError as TimeoutError
from .packages.backports.weakref_finalize import weakref_finalize as weakref_finalize
from .request import RequestMethods as RequestMethods
from .response import HTTPResponse as HTTPResponse
from .util.connection import is_connection_dropped as is_connection_dropped
from .util.proxy import connection_requires_http_tunnel as connection_requires_http_tunnel
from .util.queue import LifoQueue as LifoQueue
from .util.request import set_file_position as set_file_position
from .util.response import assert_header_parsing as assert_header_parsing
from .util.retry import Retry as Retry
from .util.ssl_match_hostname import CertificateError as CertificateError
from .util.timeout import Timeout as Timeout
from .util.url import Url as Url, get_host as get_host, parse_url as parse_url
from _typeshed import Incomplete

weakref_finalize = weakref.finalize
xrange: Incomplete
log: Incomplete

class ConnectionPool:
    """
    Base class for all connection pools, such as
    :class:`.HTTPConnectionPool` and :class:`.HTTPSConnectionPool`.

    .. note::
       ConnectionPool.urlopen() does not normalize or percent-encode target URIs
       which is useful if your target server doesn't support percent-encoded
       target URIs.
    """
    scheme: Incomplete
    QueueCls = LifoQueue
    host: Incomplete
    port: Incomplete
    def __init__(self, host, port: Incomplete | None = None) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def close(self) -> None:
        """
        Close all pooled connections and disable the pool.
        """

class HTTPConnectionPool(ConnectionPool, RequestMethods):
    '''
    Thread-safe connection pool for one host.

    :param host:
        Host used for this HTTP Connection (e.g. "localhost"), passed into
        :class:`http.client.HTTPConnection`.

    :param port:
        Port used for this HTTP Connection (None is equivalent to 80), passed
        into :class:`http.client.HTTPConnection`.

    :param strict:
        Causes BadStatusLine to be raised if the status line can\'t be parsed
        as a valid HTTP/1.0 or 1.1 status line, passed into
        :class:`http.client.HTTPConnection`.

        .. note::
           Only works in Python 2. This parameter is ignored in Python 3.

    :param timeout:
        Socket timeout in seconds for each individual connection. This can
        be a float or integer, which sets the timeout for the HTTP request,
        or an instance of :class:`urllib3.util.Timeout` which gives you more
        fine-grained control over request timeouts. After the constructor has
        been parsed, this is always a `urllib3.util.Timeout` object.

    :param maxsize:
        Number of connections to save that can be reused. More than 1 is useful
        in multithreaded situations. If ``block`` is set to False, more
        connections will be created but they will not be saved once they\'ve
        been used.

    :param block:
        If set to True, no more than ``maxsize`` connections will be used at
        a time. When no free connections are available, the call will block
        until a connection has been released. This is a useful side effect for
        particular multithreaded situations where one does not want to use more
        than maxsize connections per host to prevent flooding.

    :param headers:
        Headers to include with all requests, unless other headers are given
        explicitly.

    :param retries:
        Retry configuration to use by default with requests in this pool.

    :param _proxy:
        Parsed proxy URL, should not be used directly, instead, see
        :class:`urllib3.ProxyManager`

    :param _proxy_headers:
        A dictionary with proxy headers, should not be used directly,
        instead, see :class:`urllib3.ProxyManager`

    :param \\**conn_kw:
        Additional parameters are used to create fresh :class:`urllib3.connection.HTTPConnection`,
        :class:`urllib3.connection.HTTPSConnection` instances.
    '''
    scheme: str
    ConnectionCls = HTTPConnection
    ResponseCls = HTTPResponse
    strict: Incomplete
    timeout: Incomplete
    retries: Incomplete
    pool: Incomplete
    block: Incomplete
    proxy: Incomplete
    proxy_headers: Incomplete
    proxy_config: Incomplete
    num_connections: int
    num_requests: int
    conn_kw: Incomplete
    def __init__(self, host, port: Incomplete | None = None, strict: bool = False, timeout=..., maxsize: int = 1, block: bool = False, headers: Incomplete | None = None, retries: Incomplete | None = None, _proxy: Incomplete | None = None, _proxy_headers: Incomplete | None = None, _proxy_config: Incomplete | None = None, **conn_kw) -> None: ...
    def close(self) -> None:
        """
        Close all pooled connections and disable the pool.
        """
    def is_same_host(self, url):
        """
        Check if the given ``url`` is a member of the same host as this
        connection pool.
        """
    def urlopen(self, method, url, body: Incomplete | None = None, headers: Incomplete | None = None, retries: Incomplete | None = None, redirect: bool = True, assert_same_host: bool = True, timeout=..., pool_timeout: Incomplete | None = None, release_conn: Incomplete | None = None, chunked: bool = False, body_pos: Incomplete | None = None, **response_kw):
        """
        Get a connection from the pool and perform an HTTP request. This is the
        lowest level call for making a request, so you'll need to specify all
        the raw details.

        .. note::

           More commonly, it's appropriate to use a convenience method provided
           by :class:`.RequestMethods`, such as :meth:`request`.

        .. note::

           `release_conn` will only behave as expected if
           `preload_content=False` because we want to make
           `preload_content=False` the default behaviour someday soon without
           breaking backwards compatibility.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param url:
            The URL to perform the request on.

        :param body:
            Data to send in the request body, either :class:`str`, :class:`bytes`,
            an iterable of :class:`str`/:class:`bytes`, or a file-like object.

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Configure the number of retries to allow before raising a
            :class:`~urllib3.exceptions.MaxRetryError` exception.

            Pass ``None`` to retry until you receive a response. Pass a
            :class:`~urllib3.util.retry.Retry` object for fine-grained control
            over different types of retries.
            Pass an integer number to retry connection errors that many times,
            but no other types of errors. Pass zero to never retry.

            If ``False``, then retries are disabled and any exception is raised
            immediately. Also, instead of raising a MaxRetryError on redirects,
            the redirect response will be returned.

        :type retries: :class:`~urllib3.util.retry.Retry`, False, or an int.

        :param redirect:
            If True, automatically handle redirects (status codes 301, 302,
            303, 307, 308). Each redirect counts as a retry. Disabling retries
            will disable redirect, too.

        :param assert_same_host:
            If ``True``, will make sure that the host of the pool requests is
            consistent else will raise HostChangedError. When ``False``, you can
            use the pool on an HTTP proxy and request foreign hosts.

        :param timeout:
            If specified, overrides the default timeout for this one
            request. It may be a float (in seconds) or an instance of
            :class:`urllib3.util.Timeout`.

        :param pool_timeout:
            If set and the pool is set to block=True, then this method will
            block for ``pool_timeout`` seconds and raise EmptyPoolError if no
            connection is available within the time period.

        :param release_conn:
            If False, then the urlopen call will not release the connection
            back into the pool once a response is received (but will release if
            you read the entire contents of the response such as when
            `preload_content=True`). This is useful if you're not preloading
            the response's content immediately. You will need to call
            ``r.release_conn()`` on the response ``r`` to return the connection
            back into the pool. If None, it takes the value of
            ``response_kw.get('preload_content', True)``.

        :param chunked:
            If True, urllib3 will send the body using chunked transfer
            encoding. Otherwise, urllib3 will send the body using the standard
            content-length form. Defaults to False.

        :param int body_pos:
            Position to seek to in file-like body in the event of a retry or
            redirect. Typically this won't need to be set because urllib3 will
            auto-populate the value when needed.

        :param \\**response_kw:
            Additional parameters are passed to
            :meth:`urllib3.response.HTTPResponse.from_httplib`
        """

class HTTPSConnectionPool(HTTPConnectionPool):
    """
    Same as :class:`.HTTPConnectionPool`, but HTTPS.

    :class:`.HTTPSConnection` uses one of ``assert_fingerprint``,
    ``assert_hostname`` and ``host`` in this order to verify connections.
    If ``assert_hostname`` is False, no verification is done.

    The ``key_file``, ``cert_file``, ``cert_reqs``, ``ca_certs``,
    ``ca_cert_dir``, ``ssl_version``, ``key_password`` are only used if :mod:`ssl`
    is available and are fed into :meth:`urllib3.util.ssl_wrap_socket` to upgrade
    the connection socket into an SSL socket.
    """
    scheme: str
    ConnectionCls = HTTPSConnection
    key_file: Incomplete
    cert_file: Incomplete
    cert_reqs: Incomplete
    key_password: Incomplete
    ca_certs: Incomplete
    ca_cert_dir: Incomplete
    ssl_version: Incomplete
    assert_hostname: Incomplete
    assert_fingerprint: Incomplete
    def __init__(self, host, port: Incomplete | None = None, strict: bool = False, timeout=..., maxsize: int = 1, block: bool = False, headers: Incomplete | None = None, retries: Incomplete | None = None, _proxy: Incomplete | None = None, _proxy_headers: Incomplete | None = None, key_file: Incomplete | None = None, cert_file: Incomplete | None = None, cert_reqs: Incomplete | None = None, key_password: Incomplete | None = None, ca_certs: Incomplete | None = None, ssl_version: Incomplete | None = None, assert_hostname: Incomplete | None = None, assert_fingerprint: Incomplete | None = None, ca_cert_dir: Incomplete | None = None, **conn_kw) -> None: ...

def connection_from_url(url, **kw):
    """
    Given a url, return an :class:`.ConnectionPool` instance of its host.

    This is a shortcut for not having to parse out the scheme, host, and port
    of the url before creating an :class:`.ConnectionPool` instance.

    :param url:
        Absolute URL string that must include the scheme. Port is optional.

    :param \\**kw:
        Passes additional parameters to the constructor of the appropriate
        :class:`.ConnectionPool`. Useful for specifying things like
        timeout, maxsize, headers, etc.

    Example::

        >>> conn = connection_from_url('http://google.com/')
        >>> r = conn.request('GET', '/')
    """
