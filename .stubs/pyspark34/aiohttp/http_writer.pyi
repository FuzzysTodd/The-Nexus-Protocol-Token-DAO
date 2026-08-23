import asyncio
from .abc import AbstractStreamWriter
from .base_protocol import BaseProtocol
from _typeshed import Incomplete
from multidict import CIMultiDict
from typing import NamedTuple

__all__ = ['StreamWriter', 'HttpVersion', 'HttpVersion10', 'HttpVersion11']

class HttpVersion(NamedTuple):
    major: int
    minor: int

HttpVersion10: Incomplete
HttpVersion11: Incomplete

class StreamWriter(AbstractStreamWriter):
    loop: Incomplete
    length: Incomplete
    chunked: bool
    buffer_size: int
    output_size: int
    def __init__(self, protocol: BaseProtocol, loop: asyncio.AbstractEventLoop, on_chunk_sent: _T_OnChunkSent = None, on_headers_sent: _T_OnHeadersSent = None) -> None: ...
    @property
    def transport(self) -> asyncio.Transport | None: ...
    @property
    def protocol(self) -> BaseProtocol: ...
    def enable_chunking(self) -> None: ...
    def enable_compression(self, encoding: str = 'deflate', strategy: int = ...) -> None: ...
    async def write(self, chunk: bytes, *, drain: bool = True, LIMIT: int = 65536) -> None:
        """Writes chunk of data to a stream.

        write_eof() indicates end of stream.
        writer can't be used after write_eof() method being called.
        write() return drain future.
        """
    async def write_headers(self, status_line: str, headers: CIMultiDict[str]) -> None:
        """Write request/response status and headers."""
    async def write_eof(self, chunk: bytes = b'') -> None: ...
    async def drain(self) -> None:
        """Flush the write buffer.

        The intended use is to write

          await w.write(data)
          await w.drain()
        """
