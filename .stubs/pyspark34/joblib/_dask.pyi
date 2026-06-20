from .parallel import AutoBatchingMixin as AutoBatchingMixin, ParallelBackendBase as ParallelBackendBase, parallel_config as parallel_config
from _typeshed import Incomplete
from collections.abc import Generator

def is_weakrefable(obj): ...

class _WeakKeyDictionary:
    """A variant of weakref.WeakKeyDictionary for unhashable objects.

    This datastructure is used to store futures for broadcasted data objects
    such as large numpy arrays or pandas dataframes that are not hashable and
    therefore cannot be used as keys of traditional python dicts.

    Furthermore using a dict with id(array) as key is not safe because the
    Python is likely to reuse id of recently collected arrays.
    """
    def __init__(self) -> None: ...
    def __getitem__(self, obj): ...
    def __setitem__(self, obj, value) -> None: ...
    def __len__(self) -> int: ...
    def clear(self) -> None: ...

class Batch:
    """dask-compatible wrapper that executes a batch of tasks"""
    def __init__(self, tasks) -> None: ...
    def __call__(self, tasks: Incomplete | None = None): ...

class DaskDistributedBackend(AutoBatchingMixin, ParallelBackendBase):
    MIN_IDEAL_BATCH_DURATION: float
    MAX_IDEAL_BATCH_DURATION: float
    supports_timeout: bool
    default_n_jobs: int
    client: Incomplete
    data_futures: Incomplete
    wait_for_workers_timeout: Incomplete
    submit_kwargs: Incomplete
    waiting_futures: Incomplete
    def __init__(self, scheduler_host: Incomplete | None = None, scatter: Incomplete | None = None, client: Incomplete | None = None, loop: Incomplete | None = None, wait_for_workers_timeout: int = 10, **submit_kwargs) -> None: ...
    def __reduce__(self): ...
    def get_nested_backend(self): ...
    parallel: Incomplete
    def configure(self, n_jobs: int = 1, parallel: Incomplete | None = None, **backend_args): ...
    call_data_futures: Incomplete
    def start_call(self) -> None: ...
    def stop_call(self) -> None: ...
    def effective_n_jobs(self, n_jobs): ...
    def apply_async(self, func, callback: Incomplete | None = None): ...
    def abort_everything(self, ensure_ready: bool = True) -> None:
        """ Tell the client to cancel any task submitted via this instance

        joblib.Parallel will never access those results
        """
    def retrieval_context(self) -> Generator[None, None, None]:
        """Override ParallelBackendBase.retrieval_context to avoid deadlocks.

        This removes thread from the worker's thread pool (using 'secede').
        Seceding avoids deadlock in nested parallelism settings.
        """
