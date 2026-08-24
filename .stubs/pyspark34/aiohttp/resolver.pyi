import asyncio
from .abc import AbstractResolver
from typing import Any, Dict, List

__all__ = ['ThreadedResolver', 'AsyncResolver', 'DefaultResolver']

class ThreadedResolver(AbstractResolver):
    """Threaded resolver.

    Uses an Executor for synchronous getaddrinfo() calls.
    concurrent.futures.ThreadPoolExecutor is used by default.
    """
    def __init__(self, loop: asyncio.AbstractEventLoop | None = None) -> None: ...
    async def resolve(self, hostname: str, port: int = 0, family: int = ...) -> List[Dict[str, Any]]: ...
    async def close(self) -> None: ...

class AsyncResolver(AbstractResolver):
    """Use the `aiodns` package to make asynchronous DNS lookups"""
    def __init__(self, loop: asyncio.AbstractEventLoop | None = None, *args: Any, **kwargs: Any) -> None: ...
    async def resolve(self, host: str, port: int = 0, family: int = ...) -> List[Dict[str, Any]]: ...
    async def close(self) -> None: ...

DefaultResolver: _DefaultType
