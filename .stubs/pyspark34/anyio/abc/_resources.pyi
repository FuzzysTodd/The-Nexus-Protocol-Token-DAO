from abc import ABCMeta, abstractmethod
from types import TracebackType
from typing import TypeVar

T = TypeVar('T')

class AsyncResource(metaclass=ABCMeta):
    """
    Abstract base class for all closeable asynchronous resources.

    Works as an asynchronous context manager which returns the instance itself on enter, and calls
    :meth:`aclose` on exit.
    """
    async def __aenter__(self) -> T: ...
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...
    @abstractmethod
    async def aclose(self) -> None:
        """Close the resource."""
