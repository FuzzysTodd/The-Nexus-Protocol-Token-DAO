import dataclasses
from . import datastructures as datastructures, exceptions as exceptions
from _typeshed import Incomplete
from typing import Callable, Generator

MAX_HEADERS: int
MAX_LINE: int
MAX_BODY: Incomplete

def d(value: bytes) -> str:
    """
    Decode a bytestring for interpolating into an error message.

    """

@dataclasses.dataclass
class Request:
    """
    WebSocket handshake request.

    Attributes:
        path: Request path, including optional query.
        headers: Request headers.
    """
    path: str
    headers: datastructures.Headers
    @property
    def exception(self) -> Exception | None: ...
    @classmethod
    def parse(cls, read_line: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, Request]:
        """
        Parse a WebSocket handshake request.

        This is a generator-based coroutine.

        The request path isn't URL-decoded or validated in any way.

        The request path and headers are expected to contain only ASCII
        characters. Other characters are represented with surrogate escapes.

        :meth:`parse` doesn't attempt to read the request body because
        WebSocket handshake requests don't have one. If the request contains a
        body, it may be read from the data stream after :meth:`parse` returns.

        Args:
            read_line: generator-based coroutine that reads a LF-terminated
                line or raises an exception if there isn't enough data

        Raises:
            EOFError: if the connection is closed without a full HTTP request.
            SecurityError: if the request exceeds a security limit.
            ValueError: if the request isn't well formatted.

        """
    def serialize(self) -> bytes:
        """
        Serialize a WebSocket handshake request.

        """
    def __init__(self, path, headers, _exception) -> None: ...

@dataclasses.dataclass
class Response:
    """
    WebSocket handshake response.

    Attributes:
        status_code: Response code.
        reason_phrase: Response reason.
        headers: Response headers.
        body: Response body, if any.

    """
    status_code: int
    reason_phrase: str
    headers: datastructures.Headers
    body: bytes | None = ...
    @property
    def exception(self) -> Exception | None: ...
    @classmethod
    def parse(cls, read_line: Callable[[int], Generator[None, None, bytes]], read_exact: Callable[[int], Generator[None, None, bytes]], read_to_eof: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, Response]:
        """
        Parse a WebSocket handshake response.

        This is a generator-based coroutine.

        The reason phrase and headers are expected to contain only ASCII
        characters. Other characters are represented with surrogate escapes.

        Args:
            read_line: generator-based coroutine that reads a LF-terminated
                line or raises an exception if there isn't enough data.
            read_exact: generator-based coroutine that reads the requested
                bytes or raises an exception if there isn't enough data.
            read_to_eof: generator-based coroutine that reads until the end
                of the stream.

        Raises:
            EOFError: if the connection is closed without a full HTTP response.
            SecurityError: if the response exceeds a security limit.
            LookupError: if the response isn't well formatted.
            ValueError: if the response isn't well formatted.

        """
    def serialize(self) -> bytes:
        """
        Serialize a WebSocket handshake response.

        """
    def __init__(self, status_code, reason_phrase, headers, body, _exception) -> None: ...

def parse_headers(read_line: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, datastructures.Headers]:
    """
    Parse HTTP headers.

    Non-ASCII characters are represented with surrogate escapes.

    Args:
        read_line: generator-based coroutine that reads a LF-terminated line
            or raises an exception if there isn't enough data.

    Raises:
        EOFError: if the connection is closed without complete headers.
        SecurityError: if the request exceeds a security limit.
        ValueError: if the request isn't well formatted.

    """
def parse_line(read_line: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, bytes]:
    """
    Parse a single line.

    CRLF is stripped from the return value.

    Args:
        read_line: generator-based coroutine that reads a LF-terminated line
            or raises an exception if there isn't enough data.

    Raises:
        EOFError: if the connection is closed without a CRLF.
        SecurityError: if the response exceeds a security limit.

    """
