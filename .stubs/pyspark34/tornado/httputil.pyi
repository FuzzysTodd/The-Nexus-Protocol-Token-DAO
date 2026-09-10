import collections.abc
import copy
import datetime
import http.cookies
import time
import typing
import unittest
from _typeshed import Incomplete
from asyncio import Future
from tornado.escape import native_str as native_str, parse_qs_bytes as parse_qs_bytes, utf8 as utf8
from tornado.log import gen_log as gen_log
from tornado.util import ObjectDict as ObjectDict, unicode_type as unicode_type
from typing import AnyStr, Awaitable, Dict, Iterable, Iterator, List, Mapping, NamedTuple, Tuple

class HTTPHeaders(collections.abc.MutableMapping):
    '''A dictionary that maintains ``Http-Header-Case`` for all keys.

    Supports multiple values per key via a pair of new methods,
    `add()` and `get_list()`.  The regular dictionary interface
    returns a single value per key, with multiple values joined by a
    comma.

    >>> h = HTTPHeaders({"content-type": "text/html"})
    >>> list(h.keys())
    [\'Content-Type\']
    >>> h["Content-Type"]
    \'text/html\'

    >>> h.add("Set-Cookie", "A=B")
    >>> h.add("Set-Cookie", "C=D")
    >>> h["set-cookie"]
    \'A=B,C=D\'
    >>> h.get_list("set-cookie")
    [\'A=B\', \'C=D\']

    >>> for (k,v) in sorted(h.get_all()):
    ...    print(\'%s: %s\' % (k,v))
    ...
    Content-Type: text/html
    Set-Cookie: A=B
    Set-Cookie: C=D
    '''
    @typing.overload
    def __init__(self, __arg: Mapping[str, List[str]]) -> None: ...
    @typing.overload
    def __init__(self, __arg: Mapping[str, str]) -> None: ...
    @typing.overload
    def __init__(self, *args: Tuple[str, str]) -> None: ...
    @typing.overload
    def __init__(self, **kwargs: str) -> None: ...
    def add(self, name: str, value: str) -> None:
        """Adds a new value for the given key."""
    def get_list(self, name: str) -> List[str]:
        """Returns all values for the given header as a list."""
    def get_all(self) -> Iterable[Tuple[str, str]]:
        """Returns an iterable of all (name, value) pairs.

        If a header has multiple values, multiple pairs will be
        returned with the same name.
        """
    def parse_line(self, line: str) -> None:
        '''Updates the dictionary with a single header line.

        >>> h = HTTPHeaders()
        >>> h.parse_line("Content-Type: text/html")
        >>> h.get(\'content-type\')
        \'text/html\'
        '''
    @classmethod
    def parse(cls, headers: str) -> HTTPHeaders:
        '''Returns a dictionary from HTTP header text.

        >>> h = HTTPHeaders.parse("Content-Type: text/html\\r\\nContent-Length: 42\\r\\n")
        >>> sorted(h.items())
        [(\'Content-Length\', \'42\'), (\'Content-Type\', \'text/html\')]

        .. versionchanged:: 5.1

           Raises `HTTPInputError` on malformed headers instead of a
           mix of `KeyError`, and `ValueError`.

        '''
    def __setitem__(self, name: str, value: str) -> None: ...
    def __getitem__(self, name: str) -> str: ...
    def __delitem__(self, name: str) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[typing.Any]: ...
    def copy(self) -> HTTPHeaders: ...
    __copy__ = copy
    __unicode__: Incomplete

class HTTPServerRequest:
    '''A single HTTP request.

    All attributes are type `str` unless otherwise noted.

    .. attribute:: method

       HTTP request method, e.g. "GET" or "POST"

    .. attribute:: uri

       The requested uri.

    .. attribute:: path

       The path portion of `uri`

    .. attribute:: query

       The query portion of `uri`

    .. attribute:: version

       HTTP version specified in request, e.g. "HTTP/1.1"

    .. attribute:: headers

       `.HTTPHeaders` dictionary-like object for request headers.  Acts like
       a case-insensitive dictionary with additional methods for repeated
       headers.

    .. attribute:: body

       Request body, if present, as a byte string.

    .. attribute:: remote_ip

       Client\'s IP address as a string.  If ``HTTPServer.xheaders`` is set,
       will pass along the real IP address provided by a load balancer
       in the ``X-Real-Ip`` or ``X-Forwarded-For`` header.

    .. versionchanged:: 3.1
       The list format of ``X-Forwarded-For`` is now supported.

    .. attribute:: protocol

       The protocol used, either "http" or "https".  If ``HTTPServer.xheaders``
       is set, will pass along the protocol used by a load balancer if
       reported via an ``X-Scheme`` header.

    .. attribute:: host

       The requested hostname, usually taken from the ``Host`` header.

    .. attribute:: arguments

       GET/POST arguments are available in the arguments property, which
       maps arguments names to lists of values (to support multiple values
       for individual names). Names are of type `str`, while arguments
       are byte strings.  Note that this is different from
       `.RequestHandler.get_argument`, which returns argument values as
       unicode strings.

    .. attribute:: query_arguments

       Same format as ``arguments``, but contains only arguments extracted
       from the query string.

       .. versionadded:: 3.2

    .. attribute:: body_arguments

       Same format as ``arguments``, but contains only arguments extracted
       from the request body.

       .. versionadded:: 3.2

    .. attribute:: files

       File uploads are available in the files property, which maps file
       names to lists of `.HTTPFile`.

    .. attribute:: connection

       An HTTP request is attached to a single HTTP connection, which can
       be accessed through the "connection" attribute. Since connections
       are typically kept open in HTTP/1.1, multiple requests can be handled
       sequentially on a single connection.

    .. versionchanged:: 4.0
       Moved from ``tornado.httpserver.HTTPRequest``.
    '''
    path: str
    query: str
    method: Incomplete
    uri: Incomplete
    version: Incomplete
    headers: Incomplete
    body: Incomplete
    remote_ip: Incomplete
    protocol: Incomplete
    host: Incomplete
    host_name: Incomplete
    files: Incomplete
    connection: Incomplete
    server_connection: Incomplete
    arguments: Incomplete
    query_arguments: Incomplete
    body_arguments: Incomplete
    def __init__(self, method: str | None = None, uri: str | None = None, version: str = 'HTTP/1.0', headers: HTTPHeaders | None = None, body: bytes | None = None, host: str | None = None, files: Dict[str, List['HTTPFile']] | None = None, connection: HTTPConnection | None = None, start_line: RequestStartLine | None = None, server_connection: object | None = None) -> None: ...
    @property
    def cookies(self) -> Dict[str, http.cookies.Morsel]:
        """A dictionary of ``http.cookies.Morsel`` objects."""
    def full_url(self) -> str:
        """Reconstructs the full URL for this request."""
    def request_time(self) -> float:
        """Returns the amount of time it took for this request to execute."""
    def get_ssl_certificate(self, binary_form: bool = False) -> None | Dict | bytes:
        '''Returns the client\'s SSL certificate, if any.

        To use client certificates, the HTTPServer\'s
        `ssl.SSLContext.verify_mode` field must be set, e.g.::

            ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_ctx.load_cert_chain("foo.crt", "foo.key")
            ssl_ctx.load_verify_locations("cacerts.pem")
            ssl_ctx.verify_mode = ssl.CERT_REQUIRED
            server = HTTPServer(app, ssl_options=ssl_ctx)

        By default, the return value is a dictionary (or None, if no
        client certificate is present).  If ``binary_form`` is true, a
        DER-encoded form of the certificate is returned instead.  See
        SSLSocket.getpeercert() in the standard library for more
        details.
        http://docs.python.org/library/ssl.html#sslsocket-objects
        '''

class HTTPInputError(Exception):
    """Exception class for malformed HTTP requests or responses
    from remote sources.

    .. versionadded:: 4.0
    """
class HTTPOutputError(Exception):
    """Exception class for errors in HTTP output.

    .. versionadded:: 4.0
    """

class HTTPServerConnectionDelegate:
    """Implement this interface to handle requests from `.HTTPServer`.

    .. versionadded:: 4.0
    """
    def start_request(self, server_conn: object, request_conn: HTTPConnection) -> HTTPMessageDelegate:
        """This method is called by the server when a new request has started.

        :arg server_conn: is an opaque object representing the long-lived
            (e.g. tcp-level) connection.
        :arg request_conn: is a `.HTTPConnection` object for a single
            request/response exchange.

        This method should return a `.HTTPMessageDelegate`.
        """
    def on_close(self, server_conn: object) -> None:
        """This method is called when a connection has been closed.

        :arg server_conn: is a server connection that has previously been
            passed to ``start_request``.
        """

class HTTPMessageDelegate:
    """Implement this interface to handle an HTTP request or response.

    .. versionadded:: 4.0
    """
    def headers_received(self, start_line: RequestStartLine | ResponseStartLine, headers: HTTPHeaders) -> Awaitable[None] | None:
        """Called when the HTTP headers have been received and parsed.

        :arg start_line: a `.RequestStartLine` or `.ResponseStartLine`
            depending on whether this is a client or server message.
        :arg headers: a `.HTTPHeaders` instance.

        Some `.HTTPConnection` methods can only be called during
        ``headers_received``.

        May return a `.Future`; if it does the body will not be read
        until it is done.
        """
    def data_received(self, chunk: bytes) -> Awaitable[None] | None:
        """Called when a chunk of data has been received.

        May return a `.Future` for flow control.
        """
    def finish(self) -> None:
        """Called after the last chunk of data has been received."""
    def on_connection_close(self) -> None:
        """Called if the connection is closed without finishing the request.

        If ``headers_received`` is called, either ``finish`` or
        ``on_connection_close`` will be called, but not both.
        """

class HTTPConnection:
    """Applications use this interface to write their responses.

    .. versionadded:: 4.0
    """
    def write_headers(self, start_line: RequestStartLine | ResponseStartLine, headers: HTTPHeaders, chunk: bytes | None = None) -> Future[None]:
        """Write an HTTP header block.

        :arg start_line: a `.RequestStartLine` or `.ResponseStartLine`.
        :arg headers: a `.HTTPHeaders` instance.
        :arg chunk: the first (optional) chunk of data.  This is an optimization
            so that small responses can be written in the same call as their
            headers.

        The ``version`` field of ``start_line`` is ignored.

        Returns a future for flow control.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed.
        """
    def write(self, chunk: bytes) -> Future[None]:
        """Writes a chunk of body data.

        Returns a future for flow control.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed.
        """
    def finish(self) -> None:
        """Indicates that the last body data has been written."""

def url_concat(url: str, args: None | Dict[str, str] | List[Tuple[str, str]] | Tuple[Tuple[str, str], ...]) -> str:
    '''Concatenate url and arguments regardless of whether
    url has existing query parameters.

    ``args`` may be either a dictionary or a list of key-value pairs
    (the latter allows for multiple values with the same key.

    >>> url_concat("http://example.com/foo", dict(c="d"))
    \'http://example.com/foo?c=d\'
    >>> url_concat("http://example.com/foo?a=b", dict(c="d"))
    \'http://example.com/foo?a=b&c=d\'
    >>> url_concat("http://example.com/foo?a=b", [("c", "d"), ("c", "d2")])
    \'http://example.com/foo?a=b&c=d&c=d2\'
    '''

class HTTPFile(ObjectDict):
    """Represents a file uploaded via a form.

    For backwards compatibility, its instance attributes are also
    accessible as dictionary keys.

    * ``filename``
    * ``body``
    * ``content_type``
    """
    filename: str
    body: bytes
    content_type: str

def parse_body_arguments(content_type: str, body: bytes, arguments: Dict[str, List[bytes]], files: Dict[str, List[HTTPFile]], headers: HTTPHeaders | None = None) -> None:
    """Parses a form request body.

    Supports ``application/x-www-form-urlencoded`` and
    ``multipart/form-data``.  The ``content_type`` parameter should be
    a string and ``body`` should be a byte string.  The ``arguments``
    and ``files`` parameters are dictionaries that will be updated
    with the parsed contents.
    """
def parse_multipart_form_data(boundary: bytes, data: bytes, arguments: Dict[str, List[bytes]], files: Dict[str, List[HTTPFile]]) -> None:
    """Parses a ``multipart/form-data`` body.

    The ``boundary`` and ``data`` parameters are both byte strings.
    The dictionaries given in the arguments and files parameters
    will be updated with the contents of the body.

    .. versionchanged:: 5.1

       Now recognizes non-ASCII filenames in RFC 2231/5987
       (``filename*=``) format.
    """
def format_timestamp(ts: int | float | tuple | time.struct_time | datetime.datetime) -> str:
    """Formats a timestamp in the format used by HTTP.

    The argument may be a numeric timestamp as returned by `time.time`,
    a time tuple as returned by `time.gmtime`, or a `datetime.datetime`
    object.

    >>> format_timestamp(1359312200)
    'Sun, 27 Jan 2013 18:43:20 GMT'
    """

class RequestStartLine(NamedTuple):
    method: Incomplete
    path: Incomplete
    version: Incomplete

def parse_request_start_line(line: str) -> RequestStartLine:
    '''Returns a (method, path, version) tuple for an HTTP 1.x request line.

    The response is a `collections.namedtuple`.

    >>> parse_request_start_line("GET /foo HTTP/1.1")
    RequestStartLine(method=\'GET\', path=\'/foo\', version=\'HTTP/1.1\')
    '''

class ResponseStartLine(NamedTuple):
    version: Incomplete
    code: Incomplete
    reason: Incomplete

def parse_response_start_line(line: str) -> ResponseStartLine:
    '''Returns a (version, code, reason) tuple for an HTTP 1.x response line.

    The response is a `collections.namedtuple`.

    >>> parse_response_start_line("HTTP/1.1 200 OK")
    ResponseStartLine(version=\'HTTP/1.1\', code=200, reason=\'OK\')
    '''
def encode_username_password(username: str | bytes, password: str | bytes) -> bytes:
    """Encodes a username/password pair in the format used by HTTP auth.

    The return value is a byte string in the form ``username:password``.

    .. versionadded:: 5.1
    """
def doctests() -> unittest.TestSuite: ...
def split_host_and_port(netloc: str) -> Tuple[str, int | None]:
    """Returns ``(host, port)`` tuple from ``netloc``.

    Returned ``port`` will be ``None`` if not present.

    .. versionadded:: 4.1
    """
def qs_to_qsl(qs: Dict[str, List[AnyStr]]) -> Iterable[Tuple[str, AnyStr]]:
    """Generator converting a result of ``parse_qs`` back to name-value pairs.

    .. versionadded:: 5.0
    """
def parse_cookie(cookie: str) -> Dict[str, str]:
    """Parse a ``Cookie`` HTTP header into a dict of name/value pairs.

    This function attempts to mimic browser cookie parsing behavior;
    it specifically does not follow any of the cookie-related RFCs
    (because browsers don't either).

    The algorithm used is identical to that used by Django version 1.9.10.

    .. versionadded:: 4.4.2
    """
