import asyncio
from types import TracebackType
from typing import Any, Awaitable, Callable

__all__ = ['run_in_executor_with_context', 'call_soon_threadsafe', 'get_traceback_from_context']

def run_in_executor_with_context(func: Callable[..., _T], *args: Any, loop: asyncio.AbstractEventLoop | None = None) -> Awaitable[_T]:
    """
    Run a function in an executor, but make sure it uses the same contextvars.
    This is required so that the function will see the right application.

    See also: https://bugs.python.org/issue34014
    """
def call_soon_threadsafe(func: Callable[[], None], max_postpone_time: float | None = None, loop: asyncio.AbstractEventLoop | None = None) -> None:
    """
    Wrapper around asyncio's `call_soon_threadsafe`.

    This takes a `max_postpone_time` which can be used to tune the urgency of
    the method.

    Asyncio runs tasks in first-in-first-out. However, this is not what we
    want for the render function of the prompt_toolkit UI. Rendering is
    expensive, but since the UI is invalidated very often, in some situations
    we render the UI too often, so much that the rendering CPU usage slows down
    the rest of the processing of the application.  (Pymux is an example where
    we have to balance the CPU time spend on rendering the UI, and parsing
    process output.)
    However, we want to set a deadline value, for when the rendering should
    happen. (The UI should stay responsive).
    """
def get_traceback_from_context(context: dict[str, Any]) -> TracebackType | None:
    """
    Get the traceback object from the context.
    """
