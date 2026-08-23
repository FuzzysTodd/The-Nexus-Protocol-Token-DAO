import asyncio
from typing import Any

class EventResultOrError:
    """Event asyncio lock helper class.

    Wraps the Event asyncio lock allowing either to awake the
    locked Tasks without any error or raising an exception.

    thanks to @vorpalsmith for the simple design.
    """
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None: ...
    def set(self, exc: BaseException | None = None) -> None: ...
    async def wait(self) -> Any: ...
    def cancel(self) -> None:
        """Cancel all waiters"""
