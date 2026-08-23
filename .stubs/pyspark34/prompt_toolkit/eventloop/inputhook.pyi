from _typeshed import FileDescriptorLike, Incomplete
from asyncio import AbstractEventLoop
from selectors import BaseSelector, SelectorKey
from typing import Any, Callable, Mapping

__all__ = ['new_eventloop_with_inputhook', 'set_eventloop_with_inputhook', 'InputHookSelector', 'InputHookContext']

def new_eventloop_with_inputhook(inputhook: Callable[[InputHookContext], None]) -> AbstractEventLoop:
    """
    Create a new event loop with the given inputhook.
    """
def set_eventloop_with_inputhook(inputhook: Callable[[InputHookContext], None]) -> AbstractEventLoop:
    """
    Create a new event loop with the given inputhook, and activate it.
    """

class InputHookSelector(BaseSelector):
    """
    Usage:

        selector = selectors.SelectSelector()
        loop = asyncio.SelectorEventLoop(InputHookSelector(selector, inputhook))
        asyncio.set_event_loop(loop)
    """
    selector: Incomplete
    inputhook: Incomplete
    def __init__(self, selector: BaseSelector, inputhook: Callable[[InputHookContext], None]) -> None: ...
    def register(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def unregister(self, fileobj: FileDescriptorLike) -> SelectorKey: ...
    def modify(self, fileobj: FileDescriptorLike, events: _EventMask, data: Any = None) -> SelectorKey: ...
    def select(self, timeout: float | None = None) -> list[tuple[SelectorKey, _EventMask]]: ...
    def close(self) -> None:
        """
        Clean up resources.
        """
    def get_map(self) -> Mapping[FileDescriptorLike, SelectorKey]: ...

class InputHookContext:
    """
    Given as a parameter to the inputhook.
    """
    input_is_ready: Incomplete
    def __init__(self, fileno: int, input_is_ready: Callable[[], bool]) -> None: ...
    def fileno(self) -> int: ...
