import datetime
import ssl
from _typeshed import Incomplete
from io import BytesIO
from tornado import gen as gen, httputil as httputil
from tornado.concurrent import Future as Future, future_set_exception_unless_cancelled as future_set_exception_unless_cancelled, future_set_result_unless_cancelled as future_set_result_unless_cancelled
from tornado.escape import native_str as native_str, utf8 as utf8
from tornado.ioloop import IOLoop as IOLoop
from tornado.util import Configurable as Configurable
from typing import Any, Callable, Dict, Type

class HTTPClient:
    '''A blocking HTTP client.

    This interface is provided to make it easier to share code between
    synchronous and asynchronous applications. Applications that are
    running an `.IOLoop` must use `AsyncHTTPClient` instead.

    Typical usage looks like this::

        http_client = httpclient.HTTPClient()
        try:
            response = http_client.fetch("http://www.google.com/")
            print(response.body)
        except httpclient.HTTPError as e:
            # HTTPError is raised for non-200 responses; the response
            # can be found in e.response.
            print("Error: " + str(e))
        except Exception as e:
            # Other errors are possible, such as IOError.
            print("Error: " + str(e))
        http_client.close()

    .. versionchanged:: 5.0

       Due to limitations in `asyncio`, it is no longer possible to
       use the synchronous ``HTTPClient`` while an `.IOLoop` is running.
       Use `AsyncHTTPClient` instead.

    '''
    def __init__(self, async_client_class: Type[AsyncHTTPClient] | None = None, **kwargs: Any) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None:
        """Closes the HTTPClient, freeing any resources used."""
    def fetch(self, request: HTTPRequest | str, **kwargs: Any) -> HTTPResponse:
        """Executes a request, returning an `HTTPResponse`.

        The request may be either a string URL or an `HTTPRequest` object.
        If it is a string, we construct an `HTTPRequest` using any additional
        kwargs: ``HTTPRequest(request, **kwargs)``

        If an error occurs during the fetch, we raise an `HTTPError` unless
        the ``raise_error`` keyword argument is set to False.
        """

class AsyncHTTPClient(Configurable):
    '''An non-blocking HTTP client.

    Example usage::

        async def f():
            http_client = AsyncHTTPClient()
            try:
                response = await http_client.fetch("http://www.google.com")
            except Exception as e:
                print("Error: %s" % e)
            else:
                print(response.body)

    The constructor for this class is magic in several respects: It
    actually creates an instance of an implementation-specific
    subclass, and instances are reused as a kind of pseudo-singleton
    (one per `.IOLoop`). The keyword argument ``force_instance=True``
    can be used to suppress this singleton behavior. Unless
    ``force_instance=True`` is used, no arguments should be passed to
    the `AsyncHTTPClient` constructor. The implementation subclass as
    well as arguments to its constructor can be set with the static
    method `configure()`

    All `AsyncHTTPClient` implementations support a ``defaults``
    keyword argument, which can be used to set default values for
    `HTTPRequest` attributes.  For example::

        AsyncHTTPClient.configure(
            None, defaults=dict(user_agent="MyUserAgent"))
        # or with force_instance:
        client = AsyncHTTPClient(force_instance=True,
            defaults=dict(user_agent="MyUserAgent"))

    .. versionchanged:: 5.0
       The ``io_loop`` argument (deprecated since version 4.1) has been removed.

    '''
    @classmethod
    def configurable_base(cls) -> Type[Configurable]: ...
    @classmethod
    def configurable_default(cls) -> Type[Configurable]: ...
    def __new__(cls, force_instance: bool = False, **kwargs: Any) -> AsyncHTTPClient: ...
    io_loop: Incomplete
    defaults: Incomplete
    def initialize(self, defaults: Dict[str, Any] | None = None) -> None: ...
    def close(self) -> None:
        """Destroys this HTTP client, freeing any file descriptors used.

        This method is **not needed in normal use** due to the way
        that `AsyncHTTPClient` objects are transparently reused.
        ``close()`` is generally only necessary when either the
        `.IOLoop` is also being closed, or the ``force_instance=True``
        argument was used when creating the `AsyncHTTPClient`.

        No other methods may be called on the `AsyncHTTPClient` after
        ``close()``.

        """
    def fetch(self, request: str | HTTPRequest, raise_error: bool = True, **kwargs: Any) -> Future[HTTPResponse]:
        """Executes a request, asynchronously returning an `HTTPResponse`.

        The request may be either a string URL or an `HTTPRequest` object.
        If it is a string, we construct an `HTTPRequest` using any additional
        kwargs: ``HTTPRequest(request, **kwargs)``

        This method returns a `.Future` whose result is an
        `HTTPResponse`. By default, the ``Future`` will raise an
        `HTTPError` if the request returned a non-200 response code
        (other errors may also be raised if the server could not be
        contacted). Instead, if ``raise_error`` is set to False, the
        response will always be returned regardless of the response
        code.

        If a ``callback`` is given, it will be invoked with the `HTTPResponse`.
        In the callback interface, `HTTPError` is not automatically raised.
        Instead, you must check the response's ``error`` attribute or
        call its `~HTTPResponse.rethrow` method.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned
           `.Future` instead.

           The ``raise_error=False`` argument only affects the
           `HTTPError` raised when a non-200 response code is used,
           instead of suppressing all errors.
        """
    def fetch_impl(self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None: ...
    @classmethod
    def configure(cls, impl: None | str | Type[Configurable], **kwargs: Any) -> None:
        '''Configures the `AsyncHTTPClient` subclass to use.

        ``AsyncHTTPClient()`` actually creates an instance of a subclass.
        This method may be called with either a class object or the
        fully-qualified name of such a class (or ``None`` to use the default,
        ``SimpleAsyncHTTPClient``)

        If additional keyword arguments are given, they will be passed
        to the constructor of each subclass instance created.  The
        keyword argument ``max_clients`` determines the maximum number
        of simultaneous `~AsyncHTTPClient.fetch()` operations that can
        execute in parallel on each `.IOLoop`.  Additional arguments
        may be supported depending on the implementation class in use.

        Example::

           AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
        '''

class HTTPRequest:
    """HTTP client request object."""
    proxy_host: Incomplete
    proxy_port: Incomplete
    proxy_username: Incomplete
    proxy_password: Incomplete
    proxy_auth_mode: Incomplete
    url: Incomplete
    method: Incomplete
    body_producer: Incomplete
    auth_username: Incomplete
    auth_password: Incomplete
    auth_mode: Incomplete
    connect_timeout: Incomplete
    request_timeout: Incomplete
    follow_redirects: Incomplete
    max_redirects: Incomplete
    user_agent: Incomplete
    decompress_response: Incomplete
    network_interface: Incomplete
    streaming_callback: Incomplete
    header_callback: Incomplete
    prepare_curl_callback: Incomplete
    allow_nonstandard_methods: Incomplete
    validate_cert: Incomplete
    ca_certs: Incomplete
    allow_ipv6: Incomplete
    client_key: Incomplete
    client_cert: Incomplete
    ssl_options: Incomplete
    expect_100_continue: Incomplete
    start_time: Incomplete
    def __init__(self, url: str, method: str = 'GET', headers: Dict[str, str] | httputil.HTTPHeaders | None = None, body: bytes | str | None = None, auth_username: str | None = None, auth_password: str | None = None, auth_mode: str | None = None, connect_timeout: float | None = None, request_timeout: float | None = None, if_modified_since: float | datetime.datetime | None = None, follow_redirects: bool | None = None, max_redirects: int | None = None, user_agent: str | None = None, use_gzip: bool | None = None, network_interface: str | None = None, streaming_callback: Callable[[bytes], None] | None = None, header_callback: Callable[[str], None] | None = None, prepare_curl_callback: Callable[[Any], None] | None = None, proxy_host: str | None = None, proxy_port: int | None = None, proxy_username: str | None = None, proxy_password: str | None = None, proxy_auth_mode: str | None = None, allow_nonstandard_methods: bool | None = None, validate_cert: bool | None = None, ca_certs: str | None = None, allow_ipv6: bool | None = None, client_key: str | None = None, client_cert: str | None = None, body_producer: Callable[[Callable[[bytes], None]], 'Future[None]'] | None = None, expect_100_continue: bool = False, decompress_response: bool | None = None, ssl_options: Dict[str, Any] | ssl.SSLContext | None = None) -> None:
        '''All parameters except ``url`` are optional.

        :arg str url: URL to fetch
        :arg str method: HTTP method, e.g. "GET" or "POST"
        :arg headers: Additional HTTP headers to pass on the request
        :type headers: `~tornado.httputil.HTTPHeaders` or `dict`
        :arg body: HTTP request body as a string (byte or unicode; if unicode
           the utf-8 encoding will be used)
        :type body: `str` or `bytes`
        :arg collections.abc.Callable body_producer: Callable used for
           lazy/asynchronous request bodies.
           It is called with one argument, a ``write`` function, and should
           return a `.Future`.  It should call the write function with new
           data as it becomes available.  The write function returns a
           `.Future` which can be used for flow control.
           Only one of ``body`` and ``body_producer`` may
           be specified.  ``body_producer`` is not supported on
           ``curl_httpclient``.  When using ``body_producer`` it is recommended
           to pass a ``Content-Length`` in the headers as otherwise chunked
           encoding will be used, and many servers do not support chunked
           encoding on requests.  New in Tornado 4.0
        :arg str auth_username: Username for HTTP authentication
        :arg str auth_password: Password for HTTP authentication
        :arg str auth_mode: Authentication mode; default is "basic".
           Allowed values are implementation-defined; ``curl_httpclient``
           supports "basic" and "digest"; ``simple_httpclient`` only supports
           "basic"
        :arg float connect_timeout: Timeout for initial connection in seconds,
           default 20 seconds (0 means no timeout)
        :arg float request_timeout: Timeout for entire request in seconds,
           default 20 seconds (0 means no timeout)
        :arg if_modified_since: Timestamp for ``If-Modified-Since`` header
        :type if_modified_since: `datetime` or `float`
        :arg bool follow_redirects: Should redirects be followed automatically
           or return the 3xx response? Default True.
        :arg int max_redirects: Limit for ``follow_redirects``, default 5.
        :arg str user_agent: String to send as ``User-Agent`` header
        :arg bool decompress_response: Request a compressed response from
           the server and decompress it after downloading.  Default is True.
           New in Tornado 4.0.
        :arg bool use_gzip: Deprecated alias for ``decompress_response``
           since Tornado 4.0.
        :arg str network_interface: Network interface or source IP to use for request.
           See ``curl_httpclient`` note below.
        :arg collections.abc.Callable streaming_callback: If set, ``streaming_callback`` will
           be run with each chunk of data as it is received, and
           ``HTTPResponse.body`` and ``HTTPResponse.buffer`` will be empty in
           the final response.
        :arg collections.abc.Callable header_callback: If set, ``header_callback`` will
           be run with each header line as it is received (including the
           first line, e.g. ``HTTP/1.0 200 OK\\r\\n``, and a final line
           containing only ``\\r\\n``.  All lines include the trailing newline
           characters).  ``HTTPResponse.headers`` will be empty in the final
           response.  This is most useful in conjunction with
           ``streaming_callback``, because it\'s the only way to get access to
           header data while the request is in progress.
        :arg collections.abc.Callable prepare_curl_callback: If set, will be called with
           a ``pycurl.Curl`` object to allow the application to make additional
           ``setopt`` calls.
        :arg str proxy_host: HTTP proxy hostname.  To use proxies,
           ``proxy_host`` and ``proxy_port`` must be set; ``proxy_username``,
           ``proxy_pass`` and ``proxy_auth_mode`` are optional.  Proxies are
           currently only supported with ``curl_httpclient``.
        :arg int proxy_port: HTTP proxy port
        :arg str proxy_username: HTTP proxy username
        :arg str proxy_password: HTTP proxy password
        :arg str proxy_auth_mode: HTTP proxy Authentication mode;
           default is "basic". supports "basic" and "digest"
        :arg bool allow_nonstandard_methods: Allow unknown values for ``method``
           argument? Default is False.
        :arg bool validate_cert: For HTTPS requests, validate the server\'s
           certificate? Default is True.
        :arg str ca_certs: filename of CA certificates in PEM format,
           or None to use defaults.  See note below when used with
           ``curl_httpclient``.
        :arg str client_key: Filename for client SSL key, if any.  See
           note below when used with ``curl_httpclient``.
        :arg str client_cert: Filename for client SSL certificate, if any.
           See note below when used with ``curl_httpclient``.
        :arg ssl.SSLContext ssl_options: `ssl.SSLContext` object for use in
           ``simple_httpclient`` (unsupported by ``curl_httpclient``).
           Overrides ``validate_cert``, ``ca_certs``, ``client_key``,
           and ``client_cert``.
        :arg bool allow_ipv6: Use IPv6 when available?  Default is True.
        :arg bool expect_100_continue: If true, send the
           ``Expect: 100-continue`` header and wait for a continue response
           before sending the request body.  Only supported with
           ``simple_httpclient``.

        .. note::

            When using ``curl_httpclient`` certain options may be
            inherited by subsequent fetches because ``pycurl`` does
            not allow them to be cleanly reset.  This applies to the
            ``ca_certs``, ``client_key``, ``client_cert``, and
            ``network_interface`` arguments.  If you use these
            options, you should pass them on every request (you don\'t
            have to always use the same values, but it\'s not possible
            to mix requests that specify these options with ones that
            use the defaults).

        .. versionadded:: 3.1
           The ``auth_mode`` argument.

        .. versionadded:: 4.0
           The ``body_producer`` and ``expect_100_continue`` arguments.

        .. versionadded:: 4.2
           The ``ssl_options`` argument.

        .. versionadded:: 4.5
           The ``proxy_auth_mode`` argument.
        '''
    @property
    def headers(self) -> httputil.HTTPHeaders: ...
    @headers.setter
    def headers(self, value: Dict[str, str] | httputil.HTTPHeaders) -> None: ...
    @property
    def body(self) -> bytes: ...
    @body.setter
    def body(self, value: bytes | str) -> None: ...

class HTTPResponse:
    """HTTP Response object.

    Attributes:

    * ``request``: HTTPRequest object

    * ``code``: numeric HTTP status code, e.g. 200 or 404

    * ``reason``: human-readable reason phrase describing the status code

    * ``headers``: `tornado.httputil.HTTPHeaders` object

    * ``effective_url``: final location of the resource after following any
      redirects

    * ``buffer``: ``cStringIO`` object for response body

    * ``body``: response body as bytes (created on demand from ``self.buffer``)

    * ``error``: Exception object, if any

    * ``request_time``: seconds from request start to finish. Includes all
      network operations from DNS resolution to receiving the last byte of
      data. Does not include time spent in the queue (due to the
      ``max_clients`` option). If redirects were followed, only includes
      the final request.

    * ``start_time``: Time at which the HTTP operation started, based on
      `time.time` (not the monotonic clock used by `.IOLoop.time`). May
      be ``None`` if the request timed out while in the queue.

    * ``time_info``: dictionary of diagnostic timing information from the
      request. Available data are subject to change, but currently uses timings
      available from http://curl.haxx.se/libcurl/c/curl_easy_getinfo.html,
      plus ``queue``, which is the delay (if any) introduced by waiting for
      a slot under `AsyncHTTPClient`'s ``max_clients`` setting.

    .. versionadded:: 5.1

       Added the ``start_time`` attribute.

    .. versionchanged:: 5.1

       The ``request_time`` attribute previously included time spent in the queue
       for ``simple_httpclient``, but not in ``curl_httpclient``. Now queueing time
       is excluded in both implementations. ``request_time`` is now more accurate for
       ``curl_httpclient`` because it uses a monotonic clock when available.
    """
    error: BaseException | None
    request: HTTPRequest
    code: Incomplete
    reason: Incomplete
    headers: Incomplete
    buffer: Incomplete
    effective_url: Incomplete
    start_time: Incomplete
    request_time: Incomplete
    time_info: Incomplete
    def __init__(self, request: HTTPRequest, code: int, headers: httputil.HTTPHeaders | None = None, buffer: BytesIO | None = None, effective_url: str | None = None, error: BaseException | None = None, request_time: float | None = None, time_info: Dict[str, float] | None = None, reason: str | None = None, start_time: float | None = None) -> None: ...
    @property
    def body(self) -> bytes: ...
    def rethrow(self) -> None:
        """If there was an error on the request, raise an `HTTPError`."""

class HTTPClientError(Exception):
    """Exception thrown for an unsuccessful HTTP request.

    Attributes:

    * ``code`` - HTTP error integer error code, e.g. 404.  Error code 599 is
      used when no HTTP response was received, e.g. for a timeout.

    * ``response`` - `HTTPResponse` object, if any.

    Note that if ``follow_redirects`` is False, redirects become HTTPErrors,
    and you can look at ``error.response.headers['Location']`` to see the
    destination of the redirect.

    .. versionchanged:: 5.1

       Renamed from ``HTTPError`` to ``HTTPClientError`` to avoid collisions with
       `tornado.web.HTTPError`. The name ``tornado.httpclient.HTTPError`` remains
       as an alias.
    """
    code: Incomplete
    message: Incomplete
    response: Incomplete
    def __init__(self, code: int, message: str | None = None, response: HTTPResponse | None = None) -> None: ...
HTTPError = HTTPClientError

class _RequestProxy:
    """Combines an object with a dictionary of defaults.

    Used internally by AsyncHTTPClient implementations.
    """
    request: Incomplete
    defaults: Incomplete
    def __init__(self, request: HTTPRequest, defaults: Dict[str, Any] | None) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

def main() -> None: ...
