from ._multiprocessing_helpers import mp as mp
from .executor import get_memmapping_executor as get_memmapping_executor
from .externals.loky import cpu_count as cpu_count, process_executor as process_executor
from .externals.loky.process_executor import ShutdownExecutorError as ShutdownExecutorError
from .pool import MemmappingPool as MemmappingPool
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from collections.abc import Generator

class ParallelBackendBase(metaclass=ABCMeta):
    """Helper abc which defines all methods a ParallelBackend must implement"""
    supports_inner_max_num_threads: bool
    supports_retrieve_callback: bool
    default_n_jobs: int
    @property
    def supports_return_generator(self): ...
    @property
    def supports_timeout(self): ...
    nesting_level: Incomplete
    inner_max_num_threads: Incomplete
    def __init__(self, nesting_level: Incomplete | None = None, inner_max_num_threads: Incomplete | None = None, **kwargs) -> None: ...
    MAX_NUM_THREADS_VARS: Incomplete
    TBB_ENABLE_IPC_VAR: str
    @abstractmethod
    def effective_n_jobs(self, n_jobs):
        """Determine the number of jobs that can actually run in parallel

        n_jobs is the number of workers requested by the callers. Passing
        n_jobs=-1 means requesting all available workers for instance matching
        the number of CPU cores on the worker host(s).

        This method should return a guesstimate of the number of workers that
        can actually perform work concurrently. The primary use case is to make
        it possible for the caller to know in how many chunks to slice the
        work.

        In general working on larger data chunks is more efficient (less
        scheduling overhead and better use of CPU cache prefetching heuristics)
        as long as all the workers have enough work to do.
        """
    @abstractmethod
    def apply_async(self, func, callback: Incomplete | None = None):
        """Schedule a func to be run"""
    def retrieve_result_callback(self, out) -> None:
        """Called within the callback function passed in apply_async.

        The argument of this function is the argument given to a callback in
        the considered backend. It is supposed to return the outcome of a task
        if it succeeded or raise the exception if it failed.
        """
    parallel: Incomplete
    def configure(self, n_jobs: int = 1, parallel: Incomplete | None = None, prefer: Incomplete | None = None, require: Incomplete | None = None, **backend_args):
        """Reconfigure the backend and return the number of workers.

        This makes it possible to reuse an existing backend instance for
        successive independent calls to Parallel with different parameters.
        """
    def start_call(self) -> None:
        """Call-back method called at the beginning of a Parallel call"""
    def stop_call(self) -> None:
        """Call-back method called at the end of a Parallel call"""
    def terminate(self) -> None:
        """Shutdown the workers and free the shared memory."""
    def compute_batch_size(self):
        """Determine the optimal batch size"""
    def batch_completed(self, batch_size, duration) -> None:
        """Callback indicate how long it took to run a batch"""
    def get_exceptions(self):
        """List of exception types to be captured."""
    def abort_everything(self, ensure_ready: bool = True) -> None:
        """Abort any running tasks

        This is called when an exception has been raised when executing a task
        and all the remaining tasks will be ignored and can therefore be
        aborted to spare computation resources.

        If ensure_ready is True, the backend should be left in an operating
        state as future tasks might be re-submitted via that same backend
        instance.

        If ensure_ready is False, the implementer of this method can decide
        to leave the backend in a closed / terminated state as no new task
        are expected to be submitted to this backend.

        Setting ensure_ready to False is an optimization that can be leveraged
        when aborting tasks via killing processes from a local process pool
        managed by the backend it-self: if we expect no new tasks, there is no
        point in re-creating new workers.
        """
    def get_nested_backend(self):
        """Backend instance to be used by nested Parallel calls.

        By default a thread-based backend is used for the first level of
        nesting. Beyond, switch to sequential backend to avoid spawning too
        many threads on the host.
        """
    def retrieval_context(self) -> Generator[None, None, None]:
        '''Context manager to manage an execution context.

        Calls to Parallel.retrieve will be made inside this context.

        By default, this does nothing. It may be useful for subclasses to
        handle nested parallelism. In particular, it may be required to avoid
        deadlocks if a backend manages a fixed number of workers, when those
        workers may be asked to do nested Parallel calls. Without
        \'retrieval_context\' this could lead to deadlock, as all the workers
        managed by the backend may be "busy" waiting for the nested parallel
        calls to finish, but the backend has no free workers to execute those
        tasks.
        '''
    @staticmethod
    def in_main_thread(): ...

class SequentialBackend(ParallelBackendBase):
    """A ParallelBackend which will execute all batches sequentially.

    Does not use/create any threading objects, and hence has minimal
    overhead. Used when n_jobs == 1.
    """
    uses_threads: bool
    supports_timeout: bool
    supports_retrieve_callback: bool
    supports_sharedmem: bool
    def effective_n_jobs(self, n_jobs):
        """Determine the number of jobs which are going to run in parallel"""
    def apply_async(self, func, callback: Incomplete | None = None) -> None:
        """Schedule a func to be run"""
    def retrieve_result_callback(self, out) -> None: ...
    def get_nested_backend(self): ...

class PoolManagerMixin:
    """A helper class for managing pool of workers."""
    def effective_n_jobs(self, n_jobs):
        """Determine the number of jobs which are going to run in parallel"""
    def terminate(self) -> None:
        """Shutdown the process or thread pool"""
    def apply_async(self, func, callback: Incomplete | None = None):
        """Schedule a func to be run"""
    def retrieve_result_callback(self, out):
        """Mimic concurrent.futures results, raising an error if needed."""
    def abort_everything(self, ensure_ready: bool = True) -> None:
        """Shutdown the pool and restart a new one with the same parameters"""

class AutoBatchingMixin:
    """A helper class for automagically batching jobs."""
    MIN_IDEAL_BATCH_DURATION: float
    MAX_IDEAL_BATCH_DURATION: int
    def __init__(self, **kwargs) -> None: ...
    def compute_batch_size(self):
        """Determine the optimal batch size"""
    def batch_completed(self, batch_size, duration) -> None:
        """Callback indicate how long it took to run a batch"""
    def reset_batch_stats(self) -> None:
        """Reset batch statistics to default values.

        This avoids interferences with future jobs.
        """

class ThreadingBackend(PoolManagerMixin, ParallelBackendBase):
    '''A ParallelBackend which will use a thread pool to execute batches in.

    This is a low-overhead backend but it suffers from the Python Global
    Interpreter Lock if the called function relies a lot on Python objects.
    Mostly useful when the execution bottleneck is a compiled extension that
    explicitly releases the GIL (for instance a Cython loop wrapped in a "with
    nogil" block or an expensive call to a library such as NumPy).

    The actual thread pool is lazily initialized: the actual thread pool
    construction is delayed to the first call to apply_async.

    ThreadingBackend is used as the default backend for nested calls.
    '''
    supports_retrieve_callback: bool
    uses_threads: bool
    supports_sharedmem: bool
    parallel: Incomplete
    def configure(self, n_jobs: int = 1, parallel: Incomplete | None = None, **backend_args):
        """Build a process or thread pool and return the number of workers"""

class MultiprocessingBackend(PoolManagerMixin, AutoBatchingMixin, ParallelBackendBase):
    """A ParallelBackend which will use a multiprocessing.Pool.

    Will introduce some communication and memory overhead when exchanging
    input and output data with the with the worker Python processes.
    However, does not suffer from the Python Global Interpreter Lock.
    """
    supports_retrieve_callback: bool
    supports_return_generator: bool
    def effective_n_jobs(self, n_jobs):
        """Determine the number of jobs which are going to run in parallel.

        This also checks if we are attempting to create a nested parallel
        loop.
        """
    parallel: Incomplete
    def configure(self, n_jobs: int = 1, parallel: Incomplete | None = None, prefer: Incomplete | None = None, require: Incomplete | None = None, **memmappingpool_args):
        """Build a process or thread pool and return the number of workers"""
    def terminate(self) -> None:
        """Shutdown the process or thread pool"""

class LokyBackend(AutoBatchingMixin, ParallelBackendBase):
    """Managing pool of workers with loky instead of multiprocessing."""
    supports_retrieve_callback: bool
    supports_inner_max_num_threads: bool
    parallel: Incomplete
    def configure(self, n_jobs: int = 1, parallel: Incomplete | None = None, prefer: Incomplete | None = None, require: Incomplete | None = None, idle_worker_timeout: int = 300, **memmappingexecutor_args):
        """Build a process executor and return the number of workers"""
    def effective_n_jobs(self, n_jobs):
        """Determine the number of jobs which are going to run in parallel"""
    def apply_async(self, func, callback: Incomplete | None = None):
        """Schedule a func to be run"""
    def retrieve_result_callback(self, out): ...
    def terminate(self) -> None: ...
    def abort_everything(self, ensure_ready: bool = True) -> None:
        """Shutdown the workers and restart a new one with the same parameters
        """

class FallbackToBackend(Exception):
    """Raised when configuration should fallback to another backend"""
    backend: Incomplete
    def __init__(self, backend) -> None: ...

def inside_dask_worker():
    """Check whether the current function is executed inside a Dask worker.
    """
