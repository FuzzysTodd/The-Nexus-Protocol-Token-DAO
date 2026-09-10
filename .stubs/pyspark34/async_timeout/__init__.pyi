import asyncio
import enum
from types import TracebackType
from typing import Type

__all__ = ['timeout', 'timeout_at', 'Timeout']

def timeout(delay: float | None) -> Timeout:
    """timeout context manager.

    Useful in cases when you want to apply timeout logic around block
    of code or in cases when asyncio.wait_for is not suitable. For example:

    >>> async with timeout(0.001):
    ...     async with aiohttp.get('https://github.com') as r:
    ...         await r.text()


    delay - value in seconds or None to disable timeout logic
    """
def timeout_at(deadline: float | None) -> Timeout:
    """Schedule the timeout at absolute time.

    deadline argument points on the time in the same clock system
    as loop.time().

    Please note: it is not POSIX time but a time with
    undefined starting base, e.g. the time of the system power on.

    >>> async with timeout_at(loop.time() + 10):
    ...     async with aiohttp.get('https://github.com') as r:
    ...         await r.text()


    """

class _State(enum.Enum):
    INIT: str
    ENTER: str
    TIMEOUT: str
    EXIT: str

class Timeout:
    def __init__(self, deadline: float | None, loop: asyncio.AbstractEventLoop) -> None: ...
    def __enter__(self) -> Timeout: ...
    def __exit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...
    async def __aenter__(self) -> Timeout: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...
    @property
    def expired(self) -> bool:
        """Is timeout expired during execution?"""
    @property
    def deadline(self) -> float | None: ...
    def reject(self) -> None:
        """Reject scheduled timeout if any."""
    def shift(self, delay: float) -> None:
        """Advance timeout on delay seconds.

        The delay can be negative.

        Raise RuntimeError if shift is called when deadline is not scheduled
        """
    def update(self, deadline: float) -> None:
        """Set deadline to absolute value.

        deadline argument points on the time in the same clock system
        as loop.time().

        If new deadline is in the past the timeout is raised immediately.

        Please note: it is not POSIX time but a time with
        undefined starting base, e.g. the time of the system power on.
        """
