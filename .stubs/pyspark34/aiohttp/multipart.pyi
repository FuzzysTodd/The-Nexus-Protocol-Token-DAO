from .client_reqrep import ClientResponse
from .payload import Payload
from .streams import StreamReader
from _typeshed import Incomplete
from multidict import CIMultiDictProxy, MultiMapping
from types import TracebackType
from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Sequence, Tuple, Type

__all__ = ['MultipartReader', 'MultipartWriter', 'BodyPartReader', 'BadContentDispositionHeader', 'BadContentDispositionParam', 'parse_content_disposition', 'content_disposition_filename']

class BadContentDispositionHeader(RuntimeWarning): ...
class BadContentDispositionParam(RuntimeWarning): ...

def parse_content_disposition(header: str | None) -> Tuple[str | None, Dict[str, str]]: ...
def content_disposition_filename(params: Mapping[str, str], name: str = 'filename') -> str | None: ...

class MultipartResponseWrapper:
    """Wrapper around the MultipartReader.

    It takes care about
    underlying connection and close it when it needs in.
    """
    resp: Incomplete
    stream: Incomplete
    def __init__(self, resp: ClientResponse, stream: MultipartReader) -> None: ...
    def __aiter__(self) -> MultipartResponseWrapper: ...
    async def __anext__(self) -> MultipartReader | BodyPartReader: ...
    def at_eof(self) -> bool:
        """Returns True when all response data had been read."""
    async def next(self) -> MultipartReader | BodyPartReader | None:
        """Emits next multipart reader object."""
    async def release(self) -> None:
        """Release the connection gracefully.

        All remaining content is read to the void.
        """

class BodyPartReader:
    """Multipart reader for single body part."""
    chunk_size: int
    headers: Incomplete
    def __init__(self, boundary: bytes, headers: CIMultiDictProxy[str], content: StreamReader) -> None: ...
    def __aiter__(self) -> AsyncIterator['BodyPartReader']: ...
    async def __anext__(self) -> bytes: ...
    async def next(self) -> bytes | None: ...
    async def read(self, *, decode: bool = False) -> bytes:
        """Reads body part data.

        decode: Decodes data following by encoding
                method from Content-Encoding header. If it missed
                data remains untouched
        """
    async def read_chunk(self, size: int = ...) -> bytes:
        """Reads body part content chunk of the specified size.

        size: chunk size
        """
    async def readline(self) -> bytes:
        """Reads body part by line by line."""
    async def release(self) -> None:
        """Like read(), but reads all the data to the void."""
    async def text(self, *, encoding: str | None = None) -> str:
        """Like read(), but assumes that body part contains text data."""
    async def json(self, *, encoding: str | None = None) -> Dict[str, Any] | None:
        """Like read(), but assumes that body parts contains JSON data."""
    async def form(self, *, encoding: str | None = None) -> List[Tuple[str, str]]:
        """Like read(), but assumes that body parts contain form urlencoded data."""
    def at_eof(self) -> bool:
        """Returns True if the boundary was reached or False otherwise."""
    def decode(self, data: bytes) -> bytes:
        """Decodes data.

        Decoding is done according the specified Content-Encoding
        or Content-Transfer-Encoding headers value.
        """
    def get_charset(self, default: str) -> str:
        """Returns charset parameter from Content-Type header or default."""
    def name(self) -> str | None:
        """Returns name specified in Content-Disposition header.

        If the header is missing or malformed, returns None.
        """
    def filename(self) -> str | None:
        """Returns filename specified in Content-Disposition header.

        Returns None if the header is missing or malformed.
        """

class BodyPartReaderPayload(Payload):
    def __init__(self, value: BodyPartReader, *args: Any, **kwargs: Any) -> None: ...
    async def write(self, writer: Any) -> None: ...

class MultipartReader:
    """Multipart body reader."""
    response_wrapper_cls = MultipartResponseWrapper
    multipart_reader_cls: Incomplete
    part_reader_cls = BodyPartReader
    headers: Incomplete
    def __init__(self, headers: Mapping[str, str], content: StreamReader) -> None: ...
    def __aiter__(self) -> AsyncIterator['BodyPartReader']: ...
    async def __anext__(self) -> MultipartReader | BodyPartReader | None: ...
    @classmethod
    def from_response(cls, response: ClientResponse) -> MultipartResponseWrapper:
        """Constructs reader instance from HTTP response.

        :param response: :class:`~aiohttp.client.ClientResponse` instance
        """
    def at_eof(self) -> bool:
        """Returns True if the final boundary was reached, false otherwise."""
    async def next(self) -> MultipartReader | BodyPartReader | None:
        """Emits the next multipart body part."""
    async def release(self) -> None:
        """Reads all the body parts to the void till the final boundary."""
    async def fetch_next_part(self) -> MultipartReader | BodyPartReader:
        """Returns the next body part reader."""

class MultipartWriter(Payload):
    """Multipart body writer."""
    def __init__(self, subtype: str = 'mixed', boundary: str | None = None) -> None: ...
    def __enter__(self) -> MultipartWriter: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    def __iter__(self) -> Iterator[_Part]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    @property
    def boundary(self) -> str: ...
    def append(self, obj: Any, headers: MultiMapping[str] | None = None) -> Payload: ...
    def append_payload(self, payload: Payload) -> Payload:
        """Adds a new body part to multipart writer."""
    def append_json(self, obj: Any, headers: MultiMapping[str] | None = None) -> Payload:
        """Helper to append JSON part."""
    def append_form(self, obj: Sequence[Tuple[str, str]] | Mapping[str, str], headers: MultiMapping[str] | None = None) -> Payload:
        """Helper to append form urlencoded part."""
    @property
    def size(self) -> int | None:
        """Size of the payload."""
    async def write(self, writer: Any, close_boundary: bool = True) -> None:
        """Write body."""

class MultipartPayloadWriter:
    def __init__(self, writer: Any) -> None: ...
    def enable_encoding(self, encoding: str) -> None: ...
    def enable_compression(self, encoding: str = 'deflate', strategy: int = ...) -> None: ...
    async def write_eof(self) -> None: ...
    async def write(self, chunk: bytes) -> None: ...
