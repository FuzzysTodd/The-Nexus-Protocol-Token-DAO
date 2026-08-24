import threading
from ._base import Future as Future
from .backend import get_context as get_context
from .backend.context import cpu_count as cpu_count
from .backend.queues import Queue as Queue, SimpleQueue as SimpleQueue
from .backend.reduction import get_loky_pickler_name as get_loky_pickler_name, set_loky_pickler as set_loky_pickler
from .backend.utils import get_exitcodes_terminated_worker as get_exitcodes_terminated_worker, kill_process_tree as kill_process_tree
from _typeshed import Incomplete
from concurrent.futures import Executor
from concurrent.futures.process import BrokenProcessPool as _BPPException

MAX_DEPTH: Incomplete

class _ThreadWakeup:
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def wakeup(self) -> None: ...
    def clear(self) -> None: ...

class _ExecutorFlags:
    """necessary references to maintain executor states without preventing gc

    It permits to keep the information needed by executor_manager_thread
    and crash_detection_thread to maintain the pool without preventing the
    garbage collection of unreferenced executors.
    """
    shutdown: bool
    broken: Incomplete
    kill_workers: bool
    shutdown_lock: Incomplete
    def __init__(self, shutdown_lock) -> None: ...
    def flag_as_shutting_down(self, kill_workers: Incomplete | None = None) -> None: ...
    def flag_as_broken(self, broken) -> None: ...

process_pool_executor_at_exit: Incomplete
EXTRA_QUEUED_CALLS: int

class _RemoteTraceback(Exception):
    """Embed stringification of remote traceback in local traceback"""
    tb: Incomplete
    def __init__(self, tb: Incomplete | None = None) -> None: ...

class _ExceptionWithTraceback:
    exc: Incomplete
    tb: Incomplete
    def __init__(self, exc) -> None: ...
    def __reduce__(self): ...

class _WorkItem:
    future: Incomplete
    fn: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, future, fn, args, kwargs) -> None: ...

class _ResultItem:
    work_id: Incomplete
    exception: Incomplete
    result: Incomplete
    def __init__(self, work_id, exception: Incomplete | None = None, result: Incomplete | None = None) -> None: ...

class _CallItem:
    work_id: Incomplete
    fn: Incomplete
    args: Incomplete
    kwargs: Incomplete
    loky_pickler: Incomplete
    def __init__(self, work_id, fn, args, kwargs) -> None: ...
    def __call__(self): ...

class _SafeQueue(Queue):
    """Safe Queue set exception to the future object linked to a job"""
    thread_wakeup: Incomplete
    pending_work_items: Incomplete
    running_work_items: Incomplete
    def __init__(self, max_size: int = 0, ctx: Incomplete | None = None, pending_work_items: Incomplete | None = None, running_work_items: Incomplete | None = None, thread_wakeup: Incomplete | None = None, reducers: Incomplete | None = None) -> None: ...

class _ExecutorManagerThread(threading.Thread):
    """Manages the communication between this process and the worker processes.

    The manager is run in a local thread.

    Args:
        executor: A reference to the ProcessPoolExecutor that owns
            this thread. A weakref will be own by the manager as well as
            references to internal objects used to introspect the state of
            the executor.
    """
    thread_wakeup: Incomplete
    shutdown_lock: Incomplete
    executor_reference: Incomplete
    executor_flags: Incomplete
    processes: Incomplete
    call_queue: Incomplete
    result_queue: Incomplete
    work_ids_queue: Incomplete
    pending_work_items: Incomplete
    running_work_items: Incomplete
    processes_management_lock: Incomplete
    daemon: bool
    def __init__(self, executor) -> None: ...
    def run(self) -> None: ...
    def add_call_item_to_queue(self) -> None: ...
    def wait_result_broken_or_wakeup(self): ...
    def process_result_item(self, result_item) -> None: ...
    def is_shutting_down(self): ...
    def terminate_broken(self, bpe) -> None: ...
    def flag_executor_shutting_down(self) -> None: ...
    def kill_workers(self, reason: str = '') -> None: ...
    def shutdown_workers(self) -> None: ...
    def join_executor_internals(self) -> None: ...
    def get_n_children_alive(self): ...

class LokyRecursionError(RuntimeError):
    """A process tries to spawn too many levels of nested processes."""
class BrokenProcessPool(_BPPException):
    """
    Raised when the executor is broken while a future was in the running state.
    The cause can an error raised when unpickling the task in the worker
    process or when unpickling the result value in the parent process. It can
    also be caused by a worker process being terminated unexpectedly.
    """
class TerminatedWorkerError(BrokenProcessPool):
    """
    Raised when a process in a ProcessPoolExecutor terminated abruptly
    while a future was in the running state.
    """
BrokenExecutor = BrokenProcessPool

class ShutdownExecutorError(RuntimeError):
    """
    Raised when a ProcessPoolExecutor is shutdown while a future was in the
    running or pending state.
    """

class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers: Incomplete | None = None, job_reducers: Incomplete | None = None, result_reducers: Incomplete | None = None, timeout: Incomplete | None = None, context: Incomplete | None = None, initializer: Incomplete | None = None, initargs=(), env: Incomplete | None = None) -> None:
        """Initializes a new ProcessPoolExecutor instance.

        Args:
            max_workers: int, optional (default: cpu_count())
                The maximum number of processes that can be used to execute the
                given calls. If None or not given then as many worker processes
                will be created as the number of CPUs the current process
                can use.
            job_reducers, result_reducers: dict(type: reducer_func)
                Custom reducer for pickling the jobs and the results from the
                Executor. If only `job_reducers` is provided, `result_reducer`
                will use the same reducers
            timeout: int, optional (default: None)
                Idle workers exit after timeout seconds. If a new job is
                submitted after the timeout, the executor will start enough
                new Python processes to make sure the pool of workers is full.
            context: A multiprocessing context to launch the workers. This
                object should provide SimpleQueue, Queue and Process.
            initializer: An callable used to initialize worker processes.
            initargs: A tuple of arguments to pass to the initializer.
            env: A dict of environment variable to overwrite in the child
                process. The environment variables are set before any module is
                loaded. Note that this only works with the loky context.
        """
    def submit(self, fn, *args, **kwargs): ...
    def map(self, fn, *iterables, **kwargs):
        """Returns an iterator equivalent to map(fn, iter).

        Args:
            fn: A callable that will take as many arguments as there are
                passed iterables.
            timeout: The maximum number of seconds to wait. If None, then there
                is no limit on the wait time.
            chunksize: If greater than one, the iterables will be chopped into
                chunks of size chunksize and submitted to the process pool.
                If set to one, the items in the list will be sent one at a
                time.

        Returns:
            An iterator equivalent to: map(func, *iterables) but the calls may
            be evaluated out-of-order.

        Raises:
            TimeoutError: If the entire result iterator could not be generated
                before the given timeout.
            Exception: If fn(*args) raises for any values.
        """
    def shutdown(self, wait: bool = True, kill_workers: bool = False) -> None: ...
