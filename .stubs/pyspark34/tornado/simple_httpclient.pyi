from _typeshed import Incomplete
from tornado import gen as gen, httputil as httputil, version as version
from tornado.http1connection import HTTP1Connection as HTTP1Connection, HTTP1ConnectionParameters as HTTP1ConnectionParameters
from tornado.httpclient import AsyncHTTPClient as AsyncHTTPClient, HTTPError as HTTPError, HTTPRequest as HTTPRequest, HTTPResponse as HTTPResponse, main as main
from tornado.ioloop import IOLoop as IOLoop
from tornado.iostream import IOStream as IOStream, StreamClosedError as StreamClosedError
from tornado.log import gen_log as gen_log
from tornado.netutil import OverrideResolver as OverrideResolver, Resolver as Resolver, is_valid_ip as is_valid_ip
from tornado.tcpclient import TCPClient as TCPClient
from typing import Any, Callable, Dict

class HTTPTimeoutError(HTTPError):
    """Error raised by SimpleAsyncHTTPClient on timeout.

    For historical reasons, this is a subclass of `.HTTPClientError`
    which simulates a response code of 599.

    .. versionadded:: 5.1
    """
    def __init__(self, message: str) -> None: ...

class HTTPStreamClosedError(HTTPError):
    """Error raised by SimpleAsyncHTTPClient when the underlying stream is closed.

    When a more specific exception is available (such as `ConnectionResetError`),
    it may be raised instead of this one.

    For historical reasons, this is a subclass of `.HTTPClientError`
    which simulates a response code of 599.

    .. versionadded:: 5.1
    """
    def __init__(self, message: str) -> None: ...

class SimpleAsyncHTTPClient(AsyncHTTPClient):
    """Non-blocking HTTP client with no external dependencies.

    This class implements an HTTP 1.1 client on top of Tornado's IOStreams.
    Some features found in the curl-based AsyncHTTPClient are not yet
    supported.  In particular, proxies are not supported, connections
    are not reused, and callers cannot select the network interface to be
    used.

    This implementation supports the following arguments, which can be passed
    to ``configure()`` to control the global singleton, or to the constructor
    when ``force_instance=True``.

    ``max_clients`` is the number of concurrent requests that can be
    in progress; when this limit is reached additional requests will be
    queued. Note that time spent waiting in this queue still counts
    against the ``request_timeout``.

    ``defaults`` is a dict of parameters that will be used as defaults on all
    `.HTTPRequest` objects submitted to this client.

    ``hostname_mapping`` is a dictionary mapping hostnames to IP addresses.
    It can be used to make local DNS changes when modifying system-wide
    settings like ``/etc/hosts`` is not possible or desirable (e.g. in
    unittests). ``resolver`` is similar, but using the `.Resolver` interface
    instead of a simple mapping.

    ``max_buffer_size`` (default 100MB) is the number of bytes
    that can be read into memory at once. ``max_body_size``
    (defaults to ``max_buffer_size``) is the largest response body
    that the client will accept.  Without a
    ``streaming_callback``, the smaller of these two limits
    applies; with a ``streaming_callback`` only ``max_body_size``
    does.

    .. versionchanged:: 4.2
        Added the ``max_body_size`` argument.
    """
    max_clients: Incomplete
    queue: Incomplete
    active: Incomplete
    waiting: Incomplete
    max_buffer_size: Incomplete
    max_header_size: Incomplete
    max_body_size: Incomplete
    resolver: Incomplete
    own_resolver: bool
    tcp_client: Incomplete
    def initialize(self, max_clients: int = 10, hostname_mapping: Dict[str, str] | None = None, max_buffer_size: int = 104857600, resolver: Resolver | None = None, defaults: Dict[str, Any] | None = None, max_header_size: int | None = None, max_body_size: int | None = None) -> None: ...
    def close(self) -> None: ...
    def fetch_impl(self, request: HTTPRequest, callback: Callable[[HTTPResponse], None]) -> None: ...

class _HTTPConnection(httputil.HTTPMessageDelegate):
    io_loop: Incomplete
    start_time: Incomplete
    start_wall_time: Incomplete
    client: Incomplete
    request: Incomplete
    release_callback: Incomplete
    final_callback: Incomplete
    max_buffer_size: Incomplete
    tcp_client: Incomplete
    max_header_size: Incomplete
    max_body_size: Incomplete
    code: Incomplete
    headers: Incomplete
    chunks: Incomplete
    def __init__(self, client: SimpleAsyncHTTPClient | None, request: HTTPRequest, release_callback: Callable[[], None], final_callback: Callable[[HTTPResponse], None], max_buffer_size: int, tcp_client: TCPClient, max_header_size: int, max_body_size: int) -> None: ...
    parsed: Incomplete
    parsed_hostname: Incomplete
    stream: Incomplete
    connection: Incomplete
    async def run(self) -> None: ...
    def on_connection_close(self) -> None: ...
    reason: Incomplete
    async def headers_received(self, first_line: httputil.ResponseStartLine | httputil.RequestStartLine, headers: httputil.HTTPHeaders) -> None: ...
    def finish(self) -> None: ...
    def data_received(self, chunk: bytes) -> None: ...
