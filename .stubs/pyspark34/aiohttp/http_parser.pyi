import abc
import asyncio
from ._http_parser import HttpRequestParser as HttpRequestParser, HttpResponseParser as HttpResponseParser, RawRequestMessage as RawRequestMessage, RawResponseMessage as RawResponseMessage
from .base_protocol import BaseProtocol
from .helpers import BaseTimerContext
from .http_writer import HttpVersion
from .streams import StreamReader
from .typedefs import RawHeaders
from _typeshed import Incomplete
from enum import IntEnum
from multidict import CIMultiDictProxy, istr
from typing import Any, ClassVar, Generic, List, NamedTuple, Tuple, Type
from yarl import URL

__all__ = ['HeadersParser', 'HttpParser', 'HttpRequestParser', 'HttpResponseParser', 'RawRequestMessage', 'RawResponseMessage']

class RawRequestMessage(NamedTuple):
    method: str
    path: str
    version: HttpVersion
    headers: CIMultiDictProxy[str]
    raw_headers: RawHeaders
    should_close: bool
    compression: str | None
    upgrade: bool
    chunked: bool
    url: URL

class RawResponseMessage(NamedTuple):
    version: Incomplete
    code: Incomplete
    reason: Incomplete
    headers: Incomplete
    raw_headers: Incomplete
    should_close: Incomplete
    compression: Incomplete
    upgrade: Incomplete
    chunked: Incomplete

class ParseState(IntEnum):
    PARSE_NONE: int
    PARSE_LENGTH: int
    PARSE_CHUNKED: int
    PARSE_UNTIL_EOF: int

class ChunkState(IntEnum):
    PARSE_CHUNKED_SIZE: int
    PARSE_CHUNKED_CHUNK: int
    PARSE_CHUNKED_CHUNK_EOF: int
    PARSE_MAYBE_TRAILERS: int
    PARSE_TRAILERS: int

class HeadersParser:
    max_line_size: Incomplete
    max_headers: Incomplete
    max_field_size: Incomplete
    def __init__(self, max_line_size: int = 8190, max_headers: int = 32768, max_field_size: int = 8190) -> None: ...
    def parse_headers(self, lines: List[bytes]) -> Tuple['CIMultiDictProxy[str]', RawHeaders]: ...

class HttpParser(abc.ABC, Generic[_MsgT], metaclass=abc.ABCMeta):
    lax: ClassVar[bool]
    protocol: Incomplete
    loop: Incomplete
    max_line_size: Incomplete
    max_headers: Incomplete
    max_field_size: Incomplete
    timer: Incomplete
    code: Incomplete
    method: Incomplete
    readall: Incomplete
    payload_exception: Incomplete
    response_with_body: Incomplete
    read_until_eof: Incomplete
    def __init__(self, protocol: BaseProtocol | None = None, loop: asyncio.AbstractEventLoop | None = None, limit: int = ..., max_line_size: int = 8190, max_headers: int = 32768, max_field_size: int = 8190, timer: BaseTimerContext | None = None, code: int | None = None, method: str | None = None, readall: bool = False, payload_exception: Type[BaseException] | None = None, response_with_body: bool = True, read_until_eof: bool = False, auto_decompress: bool = True) -> None: ...
    @abc.abstractmethod
    def parse_message(self, lines: List[bytes]) -> _MsgT: ...
    def feed_eof(self) -> _MsgT | None: ...
    def feed_data(self, data: bytes, SEP: _SEP = b'\r\n', EMPTY: bytes = b'', CONTENT_LENGTH: istr = ..., METH_CONNECT: str = ..., SEC_WEBSOCKET_KEY1: istr = ...) -> Tuple[List[Tuple[_MsgT, StreamReader]], bool, bytes]: ...
    def parse_headers(self, lines: List[bytes]) -> Tuple['CIMultiDictProxy[str]', RawHeaders, bool | None, str | None, bool, bool]:
        """Parses RFC 5322 headers from a stream.

        Line continuations are supported. Returns list of header name
        and value pairs. Header name is in upper case.
        """
    def set_upgraded(self, val: bool) -> None:
        """Set connection upgraded (to websocket) mode.

        :param bool val: new state.
        """

class HttpRequestParser(HttpParser[RawRequestMessage]):
    """Read request status line.

    Exception .http_exceptions.BadStatusLine
    could be raised in case of any errors in status line.
    Returns RawRequestMessage.
    """
    def parse_message(self, lines: List[bytes]) -> RawRequestMessage: ...

class HttpResponseParser(HttpParser[RawResponseMessage]):
    """Read response status line and headers.

    BadStatusLine could be raised in case of any errors in status line.
    Returns RawResponseMessage.
    """
    lax: Incomplete
    def feed_data(self, data: bytes, SEP: _SEP | None = None, *args: Any, **kwargs: Any) -> Tuple[List[Tuple[RawResponseMessage, StreamReader]], bool, bytes]: ...
    def parse_message(self, lines: List[bytes]) -> RawResponseMessage: ...

class HttpPayloadParser:
    done: bool
    payload: Incomplete
    def __init__(self, payload: StreamReader, length: int | None = None, chunked: bool = False, compression: str | None = None, code: int | None = None, method: str | None = None, readall: bool = False, response_with_body: bool = True, auto_decompress: bool = True, lax: bool = False) -> None: ...
    def feed_eof(self) -> None: ...
    def feed_data(self, chunk: bytes, SEP: _SEP = b'\r\n', CHUNK_EXT: bytes = b';') -> Tuple[bool, bytes]: ...

class DeflateBuffer:
    """DeflateStream decompress stream and feed data into specified stream."""
    decompressor: Any
    out: Incomplete
    size: int
    encoding: Incomplete
    def __init__(self, out: StreamReader, encoding: str | None) -> None: ...
    def set_exception(self, exc: BaseException) -> None: ...
    def feed_data(self, chunk: bytes, size: int) -> None: ...
    def feed_eof(self) -> None: ...
    def begin_http_chunk_receiving(self) -> None: ...
    def end_http_chunk_receiving(self) -> None: ...
HttpRequestParserPy = HttpRequestParser
HttpResponseParserPy = HttpResponseParser
RawRequestMessagePy = RawRequestMessage
RawResponseMessagePy = RawResponseMessage
HttpRequestParserC = HttpRequestParser
HttpResponseParserC = HttpResponseParser
RawRequestMessageC = RawRequestMessage
RawResponseMessageC = RawResponseMessage
