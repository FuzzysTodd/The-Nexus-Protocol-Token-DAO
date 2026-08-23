from .. import ClosedResourceError as ClosedResourceError, DelimiterNotFound as DelimiterNotFound, EndOfStream as EndOfStream, IncompleteRead as IncompleteRead
from ..abc import AnyByteReceiveStream as AnyByteReceiveStream, ByteReceiveStream as ByteReceiveStream
from dataclasses import dataclass
from typing import Any, Callable, Mapping

@dataclass(eq=False)
class BufferedByteReceiveStream(ByteReceiveStream):
    """
    Wraps any bytes-based receive stream and uses a buffer to provide sophisticated receiving
    capabilities in the form of a byte stream.
    """
    receive_stream: AnyByteReceiveStream
    async def aclose(self) -> None: ...
    @property
    def buffer(self) -> bytes:
        """The bytes currently in the buffer."""
    @property
    def extra_attributes(self) -> Mapping[Any, Callable[[], Any]]: ...
    async def receive(self, max_bytes: int = 65536) -> bytes: ...
    async def receive_exactly(self, nbytes: int) -> bytes:
        """
        Read exactly the given amount of bytes from the stream.

        :param nbytes: the number of bytes to read
        :return: the bytes read
        :raises ~anyio.IncompleteRead: if the stream was closed before the requested
            amount of bytes could be read from the stream

        """
    async def receive_until(self, delimiter: bytes, max_bytes: int) -> bytes:
        """
        Read from the stream until the delimiter is found or max_bytes have been read.

        :param delimiter: the marker to look for in the stream
        :param max_bytes: maximum number of bytes that will be read before raising
            :exc:`~anyio.DelimiterNotFound`
        :return: the bytes read (not including the delimiter)
        :raises ~anyio.IncompleteRead: if the stream was closed before the delimiter
            was found
        :raises ~anyio.DelimiterNotFound: if the delimiter is not found within the
            bytes read up to the maximum allowed

        """
    def __init__(self, receive_stream) -> None: ...
