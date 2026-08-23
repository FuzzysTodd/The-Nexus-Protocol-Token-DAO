from .abc import AbstractStreamWriter
from .payload import Payload
from _typeshed import Incomplete
from typing import Any, Awaitable, Callable, Dict, Tuple

__all__ = ['streamer']

class _stream_wrapper:
    coro: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, coro: Callable[..., Awaitable[None]], args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> None: ...
    async def __call__(self, writer: AbstractStreamWriter) -> None: ...

class streamer:
    coro: Incomplete
    def __init__(self, coro: Callable[..., Awaitable[None]]) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> _stream_wrapper: ...

class StreamWrapperPayload(Payload):
    async def write(self, writer: AbstractStreamWriter) -> None: ...

class StreamPayload(StreamWrapperPayload):
    def __init__(self, value: Any, *args: Any, **kwargs: Any) -> None: ...
    async def write(self, writer: AbstractStreamWriter) -> None: ...
