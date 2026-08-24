from ._core._eventloop import get_asynclib as get_asynclib, get_cancelled_exc_class as get_cancelled_exc_class, threadlocals as threadlocals
from ._core._synchronization import Event as Event
from ._core._tasks import CancelScope as CancelScope, create_task_group as create_task_group
from .abc._tasks import TaskStatus as TaskStatus
from concurrent.futures import Future
from contextlib import AbstractContextManager
from types import TracebackType
from typing import Any, AsyncContextManager, Awaitable, Callable, ContextManager, Generator, Generic, TypeVar, overload

T_Retval = TypeVar('T_Retval')
T_co = TypeVar('T_co')

def run(func: Callable[..., Awaitable[T_Retval]], *args: object) -> T_Retval:
    """
    Call a coroutine function from a worker thread.

    :param func: a coroutine function
    :param args: positional arguments for the callable
    :return: the return value of the coroutine function

    """
def run_async_from_thread(func: Callable[..., Awaitable[T_Retval]], *args: object) -> T_Retval: ...
def run_sync(func: Callable[..., T_Retval], *args: object) -> T_Retval:
    """
    Call a function in the event loop thread from a worker thread.

    :param func: a callable
    :param args: positional arguments for the callable
    :return: the return value of the callable

    """
def run_sync_from_thread(func: Callable[..., T_Retval], *args: object) -> T_Retval: ...

class _BlockingAsyncContextManager(AbstractContextManager, Generic[T_co]):
    def __init__(self, async_cm: AsyncContextManager[T_co], portal: BlockingPortal) -> None: ...
    async def run_async_cm(self) -> bool | None: ...
    def __enter__(self) -> T_co: ...
    def __exit__(self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None) -> bool | None: ...

class _BlockingPortalTaskStatus(TaskStatus):
    def __init__(self, future: Future) -> None: ...
    def started(self, value: object = None) -> None: ...

class BlockingPortal:
    """An object that lets external threads run code in an asynchronous event loop."""
    def __new__(cls) -> BlockingPortal: ...
    def __init__(self) -> None: ...
    async def __aenter__(self) -> BlockingPortal: ...
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> bool | None: ...
    async def sleep_until_stopped(self) -> None:
        """Sleep until :meth:`stop` is called."""
    async def stop(self, cancel_remaining: bool = False) -> None:
        """
        Signal the portal to shut down.

        This marks the portal as no longer accepting new calls and exits from
        :meth:`sleep_until_stopped`.

        :param cancel_remaining: ``True`` to cancel all the remaining tasks, ``False`` to let them
            finish before returning

        """
    @overload
    def call(self, func: Callable[..., Awaitable[T_Retval]], *args: object) -> T_Retval: ...
    @overload
    def call(self, func: Callable[..., T_Retval], *args: object) -> T_Retval: ...
    @overload
    def spawn_task(self, func: Callable[..., Awaitable[T_Retval]], *args: object, name: object = None) -> Future[T_Retval]: ...
    @overload
    def spawn_task(self, func: Callable[..., T_Retval], *args: object, name: object = None) -> Future[T_Retval]: ...
    @overload
    def start_task_soon(self, func: Callable[..., Awaitable[T_Retval]], *args: object, name: object = None) -> Future[T_Retval]: ...
    @overload
    def start_task_soon(self, func: Callable[..., T_Retval], *args: object, name: object = None) -> Future[T_Retval]: ...
    def start_task(self, func: Callable[..., Awaitable[Any]], *args: object, name: object = None) -> tuple[Future[Any], Any]:
        """
        Start a task in the portal's task group and wait until it signals for readiness.

        This method works the same way as :meth:`.abc.TaskGroup.start`.

        :param func: the target function
        :param args: positional arguments passed to ``func``
        :param name: name of the task (will be coerced to a string if not ``None``)
        :return: a tuple of (future, task_status_value) where the ``task_status_value``
            is the value passed to ``task_status.started()`` from within the target
            function
        :rtype: tuple[concurrent.futures.Future[Any], Any]

        .. versionadded:: 3.0

        """
    def wrap_async_context_manager(self, cm: AsyncContextManager[T_co]) -> ContextManager[T_co]:
        """
        Wrap an async context manager as a synchronous context manager via this portal.

        Spawns a task that will call both ``__aenter__()`` and ``__aexit__()``, stopping in the
        middle until the synchronous context manager exits.

        :param cm: an asynchronous context manager
        :return: a synchronous context manager

        .. versionadded:: 2.1

        """

def create_blocking_portal() -> BlockingPortal:
    """
    Create a portal for running functions in the event loop thread from external threads.

    Use this function in asynchronous code when you need to allow external threads access to the
    event loop where your asynchronous code is currently running.

    .. deprecated:: 3.0
        Use :class:`.BlockingPortal` directly.

    """
def start_blocking_portal(backend: str = 'asyncio', backend_options: dict[str, Any] | None = None) -> Generator[BlockingPortal, Any, None]:
    """
    Start a new event loop in a new thread and run a blocking portal in its main task.

    The parameters are the same as for :func:`~anyio.run`.

    :param backend: name of the backend
    :param backend_options: backend options
    :return: a context manager that yields a blocking portal

    .. versionchanged:: 3.0
        Usage as a context manager is now required.

    """
