from ._core._eventloop import current_time as current_time, get_asynclib as get_asynclib, get_cancelled_exc_class as get_cancelled_exc_class
from ._core._exceptions import BrokenWorkerProcess as BrokenWorkerProcess
from ._core._subprocesses import open_process as open_process
from ._core._synchronization import CapacityLimiter as CapacityLimiter
from ._core._tasks import CancelScope as CancelScope, fail_after as fail_after
from .abc import ByteReceiveStream as ByteReceiveStream, ByteSendStream as ByteSendStream, Process as Process
from .lowlevel import RunVar as RunVar, checkpoint_if_cancelled as checkpoint_if_cancelled
from .streams.buffered import BufferedByteReceiveStream as BufferedByteReceiveStream
from typing import Callable, TypeVar

WORKER_MAX_IDLE_TIME: int
T_Retval = TypeVar('T_Retval')

async def run_sync(func: Callable[..., T_Retval], *args: object, cancellable: bool = False, limiter: CapacityLimiter | None = None) -> T_Retval:
    """
    Call the given function with the given arguments in a worker process.

    If the ``cancellable`` option is enabled and the task waiting for its completion is cancelled,
    the worker process running it will be abruptly terminated using SIGKILL (or
    ``terminateProcess()`` on Windows).

    :param func: a callable
    :param args: positional arguments for the callable
    :param cancellable: ``True`` to allow cancellation of the operation while it's running
    :param limiter: capacity limiter to use to limit the total amount of processes running
        (if omitted, the default limiter is used)
    :return: an awaitable that yields the return value of the function.

    """
def current_default_process_limiter() -> CapacityLimiter:
    """
    Return the capacity limiter that is used by default to limit the number of worker processes.

    :return: a capacity limiter object

    """
def process_worker() -> None: ...
