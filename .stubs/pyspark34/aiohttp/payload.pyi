import abc
import enum
from .abc import AbstractStreamWriter
from .streams import StreamReader
from .typedefs import JSONEncoder, _CIMultiDict
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from itertools import chain
from typing import Any, ByteString, Dict, IO, Iterable, TextIO, Tuple, Type

__all__ = ['PAYLOAD_REGISTRY', 'get_payload', 'payload_type', 'Payload', 'BytesPayload', 'StringPayload', 'IOBasePayload', 'BytesIOPayload', 'BufferedReaderPayload', 'TextIOPayload', 'StringIOPayload', 'JsonPayload', 'AsyncIterablePayload']

class LookupError(Exception): ...

class Order(str, enum.Enum):
    normal: str
    try_first: str
    try_last: str

def get_payload(data: Any, *args: Any, **kwargs: Any) -> Payload: ...

class payload_type:
    type: Incomplete
    order: Incomplete
    def __init__(self, type: Any, *, order: Order = ...) -> None: ...
    def __call__(self, factory: Type['Payload']) -> Type['Payload']: ...

class PayloadRegistry:
    """Payload registry.

    note: we need zope.interface for more efficient adapter search
    """
    def __init__(self) -> None: ...
    def get(self, data: Any, *args: Any, _CHAIN: Type[chain[_PayloadRegistryItem]] = ..., **kwargs: Any) -> Payload: ...
    def register(self, factory: PayloadType, type: Any, *, order: Order = ...) -> None: ...

class Payload(ABC, metaclass=abc.ABCMeta):
    def __init__(self, value: Any, headers: _CIMultiDict | Dict[str, str] | Iterable[Tuple[str, str]] | None = None, content_type: str | None = ..., filename: str | None = None, encoding: str | None = None, **kwargs: Any) -> None: ...
    @property
    def size(self) -> int | None:
        """Size of the payload."""
    @property
    def filename(self) -> str | None:
        """Filename of the payload."""
    @property
    def headers(self) -> _CIMultiDict:
        """Custom item headers"""
    @property
    def encoding(self) -> str | None:
        """Payload encoding"""
    @property
    def content_type(self) -> str:
        """Content type"""
    def set_content_disposition(self, disptype: str, quote_fields: bool = True, _charset: str = 'utf-8', **params: Any) -> None:
        """Sets ``Content-Disposition`` header."""
    @abstractmethod
    async def write(self, writer: AbstractStreamWriter) -> None:
        """Write payload.

        writer is an AbstractStreamWriter instance:
        """

class BytesPayload(Payload):
    def __init__(self, value: ByteString, *args: Any, **kwargs: Any) -> None: ...
    async def write(self, writer: AbstractStreamWriter) -> None: ...

class StringPayload(BytesPayload):
    def __init__(self, value: str, *args: Any, encoding: str | None = None, content_type: str | None = None, **kwargs: Any) -> None: ...

class StringIOPayload(StringPayload):
    def __init__(self, value: IO[str], *args: Any, **kwargs: Any) -> None: ...

class IOBasePayload(Payload):
    def __init__(self, value: IO[Any], disposition: str = 'attachment', *args: Any, **kwargs: Any) -> None: ...
    async def write(self, writer: AbstractStreamWriter) -> None: ...

class TextIOPayload(IOBasePayload):
    def __init__(self, value: TextIO, *args: Any, encoding: str | None = None, content_type: str | None = None, **kwargs: Any) -> None: ...
    @property
    def size(self) -> int | None: ...
    async def write(self, writer: AbstractStreamWriter) -> None: ...

class BytesIOPayload(IOBasePayload):
    @property
    def size(self) -> int: ...

class BufferedReaderPayload(IOBasePayload):
    @property
    def size(self) -> int | None: ...

class JsonPayload(BytesPayload):
    def __init__(self, value: Any, encoding: str = 'utf-8', content_type: str = 'application/json', dumps: JSONEncoder = ..., *args: Any, **kwargs: Any) -> None: ...

class AsyncIterablePayload(Payload):
    def __init__(self, value: _AsyncIterable, *args: Any, **kwargs: Any) -> None: ...
    async def write(self, writer: AbstractStreamWriter) -> None: ...

class StreamReaderPayload(AsyncIterablePayload):
    def __init__(self, value: StreamReader, *args: Any, **kwargs: Any) -> None: ...

PAYLOAD_REGISTRY: Incomplete
