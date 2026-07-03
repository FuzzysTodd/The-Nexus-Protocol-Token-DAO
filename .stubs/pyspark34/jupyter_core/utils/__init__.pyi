from typing import Any, Awaitable, Callable, TypeVar

def ensure_dir_exists(path: str, mode: int = 511) -> None:
    """Ensure that a directory exists

    If it doesn't exist, try to create it, protecting against a race condition
    if another process is doing the same.
    The default permissions are determined by the current umask.
    """
def deprecation(message: str, internal: str | list[str] = 'jupyter_core/') -> None:
    """Generate a deprecation warning targeting the first frame that is not 'internal'

    internal is a string or list of strings, which if they appear in filenames in the
    frames, the frames will be considered internal. Changing this can be useful if, for example,
    we know that our internal code is calling out to another library.
    """
T = TypeVar('T')

class _TaskRunner:
    """A task runner that runs an asyncio event loop on a background thread."""
    def __init__(self) -> None: ...
    def run(self, coro: Any) -> Any:
        """Synchronously run a coroutine on a background thread."""

def run_sync(coro: Callable[..., Awaitable[T]]) -> Callable[..., T]:
    """Wraps coroutine in a function that blocks until it has executed.

    Parameters
    ----------
    coro : coroutine-function
        The coroutine-function to be executed.

    Returns
    -------
    result :
        Whatever the coroutine-function returns.
    """
async def ensure_async(obj: Awaitable[T] | T) -> T:
    """Convert a non-awaitable object to a coroutine if needed,
    and await it if it was not already awaited.

    This function is meant to be called on the result of calling a function,
    when that function could either be asynchronous or not.
    """
