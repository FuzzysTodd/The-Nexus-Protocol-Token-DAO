import logging
import types
from _typeshed import Incomplete
from tornado import gen as gen, httputil as httputil, iostream as iostream
from tornado.concurrent import Future as Future, future_add_done_callback as future_add_done_callback, future_set_result_unless_cancelled as future_set_result_unless_cancelled
from tornado.escape import native_str as native_str, utf8 as utf8
from tornado.log import app_log as app_log, gen_log as gen_log
from tornado.util import GzipDecompressor as GzipDecompressor
from typing import Awaitable, Callable, Type

class _QuietException(Exception):
    def __init__(self) -> None: ...

class _ExceptionLoggingContext:
    """Used with the ``with`` statement when calling delegate methods to
    log any exceptions with the given logger.  Any exceptions caught are
    converted to _QuietException
    """
    logger: Incomplete
    def __init__(self, logger: logging.Logger) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, typ: Type[BaseException] | None, value: BaseException | None, tb: types.TracebackType) -> None: ...

class HTTP1ConnectionParameters:
    """Parameters for `.HTTP1Connection` and `.HTTP1ServerConnection`."""
    no_keep_alive: Incomplete
    chunk_size: Incomplete
    max_header_size: Incomplete
    header_timeout: Incomplete
    max_body_size: Incomplete
    body_timeout: Incomplete
    decompress: Incomplete
    def __init__(self, no_keep_alive: bool = False, chunk_size: int | None = None, max_header_size: int | None = None, header_timeout: float | None = None, max_body_size: int | None = None, body_timeout: float | None = None, decompress: bool = False) -> None:
        """
        :arg bool no_keep_alive: If true, always close the connection after
            one request.
        :arg int chunk_size: how much data to read into memory at once
        :arg int max_header_size:  maximum amount of data for HTTP headers
        :arg float header_timeout: how long to wait for all headers (seconds)
        :arg int max_body_size: maximum amount of data for body
        :arg float body_timeout: how long to wait while reading body (seconds)
        :arg bool decompress: if true, decode incoming
            ``Content-Encoding: gzip``
        """

class HTTP1Connection(httputil.HTTPConnection):
    """Implements the HTTP/1.x protocol.

    This class can be on its own for clients, or via `HTTP1ServerConnection`
    for servers.
    """
    is_client: Incomplete
    stream: Incomplete
    params: Incomplete
    context: Incomplete
    no_keep_alive: Incomplete
    def __init__(self, stream: iostream.IOStream, is_client: bool, params: HTTP1ConnectionParameters | None = None, context: object | None = None) -> None:
        """
        :arg stream: an `.IOStream`
        :arg bool is_client: client or server
        :arg params: a `.HTTP1ConnectionParameters` instance or ``None``
        :arg context: an opaque application-defined object that can be accessed
            as ``connection.context``.
        """
    def read_response(self, delegate: httputil.HTTPMessageDelegate) -> Awaitable[bool]:
        """Read a single HTTP response.

        Typical client-mode usage is to write a request using `write_headers`,
        `write`, and `finish`, and then call ``read_response``.

        :arg delegate: a `.HTTPMessageDelegate`

        Returns a `.Future` that resolves to a bool after the full response has
        been read. The result is true if the stream is still open.
        """
    def set_close_callback(self, callback: Callable[[], None] | None) -> None:
        """Sets a callback that will be run when the connection is closed.

        Note that this callback is slightly different from
        `.HTTPMessageDelegate.on_connection_close`: The
        `.HTTPMessageDelegate` method is called when the connection is
        closed while receiving a message. This callback is used when
        there is not an active delegate (for example, on the server
        side this callback is used if the client closes the connection
        after sending its request but before receiving all the
        response.
        """
    def close(self) -> None: ...
    def detach(self) -> iostream.IOStream:
        """Take control of the underlying stream.

        Returns the underlying `.IOStream` object and stops all further
        HTTP processing.  May only be called during
        `.HTTPMessageDelegate.headers_received`.  Intended for implementing
        protocols like websockets that tunnel over an HTTP handshake.
        """
    def set_body_timeout(self, timeout: float) -> None:
        """Sets the body timeout for a single request.

        Overrides the value from `.HTTP1ConnectionParameters`.
        """
    def set_max_body_size(self, max_body_size: int) -> None:
        """Sets the body size limit for a single request.

        Overrides the value from `.HTTP1ConnectionParameters`.
        """
    def write_headers(self, start_line: httputil.RequestStartLine | httputil.ResponseStartLine, headers: httputil.HTTPHeaders, chunk: bytes | None = None) -> Future[None]:
        """Implements `.HTTPConnection.write_headers`."""
    def write(self, chunk: bytes) -> Future[None]:
        """Implements `.HTTPConnection.write`.

        For backwards compatibility it is allowed but deprecated to
        skip `write_headers` and instead call `write()` with a
        pre-encoded header block.
        """
    def finish(self) -> None:
        """Implements `.HTTPConnection.finish`."""

class _GzipMessageDelegate(httputil.HTTPMessageDelegate):
    """Wraps an `HTTPMessageDelegate` to decode ``Content-Encoding: gzip``."""
    def __init__(self, delegate: httputil.HTTPMessageDelegate, chunk_size: int) -> None: ...
    def headers_received(self, start_line: httputil.RequestStartLine | httputil.ResponseStartLine, headers: httputil.HTTPHeaders) -> Awaitable[None] | None: ...
    async def data_received(self, chunk: bytes) -> None: ...
    def finish(self) -> None: ...
    def on_connection_close(self) -> None: ...

class HTTP1ServerConnection:
    """An HTTP/1.x server."""
    stream: Incomplete
    params: Incomplete
    context: Incomplete
    def __init__(self, stream: iostream.IOStream, params: HTTP1ConnectionParameters | None = None, context: object | None = None) -> None:
        """
        :arg stream: an `.IOStream`
        :arg params: a `.HTTP1ConnectionParameters` or None
        :arg context: an opaque application-defined object that is accessible
            as ``connection.context``
        """
    async def close(self) -> None:
        """Closes the connection.

        Returns a `.Future` that resolves after the serving loop has exited.
        """
    def start_serving(self, delegate: httputil.HTTPServerConnectionDelegate) -> None:
        """Starts serving requests on this connection.

        :arg delegate: a `.HTTPServerConnectionDelegate`
        """

DIGITS: Incomplete
HEXDIGITS: Incomplete

def parse_int(s: str) -> int:
    """Parse a non-negative integer from a string."""
def parse_hex_int(s: str) -> int:
    """Parse a non-negative hexadecimal integer from a string."""
