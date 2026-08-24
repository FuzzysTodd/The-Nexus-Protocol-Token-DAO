from ..abc import AnyByteReceiveStream as AnyByteReceiveStream, AnyByteSendStream as AnyByteSendStream, AnyByteStream as AnyByteStream, ObjectReceiveStream as ObjectReceiveStream, ObjectSendStream as ObjectSendStream, ObjectStream as ObjectStream
from dataclasses import InitVar, dataclass
from typing import Any, Callable, Mapping

@dataclass(eq=False)
class TextReceiveStream(ObjectReceiveStream[str]):
    """
    Stream wrapper that decodes bytes to strings using the given encoding.

    Decoding is done using :class:`~codecs.IncrementalDecoder` which returns any completely
    received unicode characters as soon as they come in.

    :param transport_stream: any bytes-based receive stream
    :param encoding: character encoding to use for decoding bytes to strings (defaults to
        ``utf-8``)
    :param errors: handling scheme for decoding errors (defaults to ``strict``; see the
        `codecs module documentation`_ for a comprehensive list of options)

    .. _codecs module documentation: https://docs.python.org/3/library/codecs.html#codec-objects
    """
    transport_stream: AnyByteReceiveStream
    encoding: InitVar[str] = ...
    errors: InitVar[str] = ...
    def __post_init__(self, encoding: str, errors: str) -> None: ...
    async def receive(self) -> str: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    def __init__(self, transport_stream, encoding, errors) -> None: ...

@dataclass(eq=False)
class TextSendStream(ObjectSendStream[str]):
    """
    Sends strings to the wrapped stream as bytes using the given encoding.

    :param AnyByteSendStream transport_stream: any bytes-based send stream
    :param str encoding: character encoding to use for encoding strings to bytes (defaults to
        ``utf-8``)
    :param str errors: handling scheme for encoding errors (defaults to ``strict``; see the
        `codecs module documentation`_ for a comprehensive list of options)

    .. _codecs module documentation: https://docs.python.org/3/library/codecs.html#codec-objects
    """
    transport_stream: AnyByteSendStream
    encoding: InitVar[str] = ...
    errors: str = ...
    def __post_init__(self, encoding: str) -> None: ...
    async def send(self, item: str) -> None: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    def __init__(self, transport_stream, encoding, errors) -> None: ...

@dataclass(eq=False)
class TextStream(ObjectStream[str]):
    """
    A bidirectional stream that decodes bytes to strings on receive and encodes strings to bytes on
    send.

    Extra attributes will be provided from both streams, with the receive stream providing the
    values in case of a conflict.

    :param AnyByteStream transport_stream: any bytes-based stream
    :param str encoding: character encoding to use for encoding/decoding strings to/from bytes
        (defaults to ``utf-8``)
    :param str errors: handling scheme for encoding errors (defaults to ``strict``; see the
        `codecs module documentation`_ for a comprehensive list of options)

    .. _codecs module documentation: https://docs.python.org/3/library/codecs.html#codec-objects
    """
    transport_stream: AnyByteStream
    encoding: InitVar[str] = ...
    errors: InitVar[str] = ...
    def __post_init__(self, encoding: str, errors: str) -> None: ...
    async def receive(self) -> str: ...
    async def send(self, item: str) -> None: ...
    async def send_eof(self) -> None: ...
    async def aclose(self) -> None: ...
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    def __init__(self, transport_stream, encoding, errors) -> None: ...
