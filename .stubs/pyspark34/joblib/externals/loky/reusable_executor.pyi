from .process_executor import ProcessPoolExecutor
from _typeshed import Incomplete

__all__ = ['get_reusable_executor']

def get_reusable_executor(max_workers: Incomplete | None = None, context: Incomplete | None = None, timeout: int = 10, kill_workers: bool = False, reuse: str = 'auto', job_reducers: Incomplete | None = None, result_reducers: Incomplete | None = None, initializer: Incomplete | None = None, initargs=(), env: Incomplete | None = None):
    """Return the current ReusableExectutor instance.

    Start a new instance if it has not been started already or if the previous
    instance was left in a broken state.

    If the previous instance does not have the requested number of workers, the
    executor is dynamically resized to adjust the number of workers prior to
    returning.

    Reusing a singleton instance spares the overhead of starting new worker
    processes and importing common python packages each time.

    ``max_workers`` controls the maximum number of tasks that can be running in
    parallel in worker processes. By default this is set to the number of
    CPUs on the host.

    Setting ``timeout`` (in seconds) makes idle workers automatically shutdown
    so as to release system resources. New workers are respawn upon submission
    of new tasks so that ``max_workers`` are available to accept the newly
    submitted tasks. Setting ``timeout`` to around 100 times the time required
    to spawn new processes and import packages in them (on the order of 100ms)
    ensures that the overhead of spawning workers is negligible.

    Setting ``kill_workers=True`` makes it possible to forcibly interrupt
    previously spawned jobs to get a new instance of the reusable executor
    with new constructor argument values.

    The ``job_reducers`` and ``result_reducers`` are used to customize the
    pickling of tasks and results send to the executor.

    When provided, the ``initializer`` is run first in newly spawned
    processes with argument ``initargs``.

    The environment variable in the child process are a copy of the values in
    the main process. One can provide a dict ``{ENV: VAL}`` where ``ENV`` and
    ``VAL`` are string literals to overwrite the environment variable ``ENV``
    in the child processes to value ``VAL``. The environment variables are set
    in the children before any module is loaded. This only works with the
    ``loky`` context.
    """

class _ReusablePoolExecutor(ProcessPoolExecutor):
    executor_id: Incomplete
    def __init__(self, submit_resize_lock, max_workers: Incomplete | None = None, context: Incomplete | None = None, timeout: Incomplete | None = None, executor_id: int = 0, job_reducers: Incomplete | None = None, result_reducers: Incomplete | None = None, initializer: Incomplete | None = None, initargs=(), env: Incomplete | None = None) -> None: ...
    @classmethod
    def get_reusable_executor(cls, max_workers: Incomplete | None = None, context: Incomplete | None = None, timeout: int = 10, kill_workers: bool = False, reuse: str = 'auto', job_reducers: Incomplete | None = None, result_reducers: Incomplete | None = None, initializer: Incomplete | None = None, initargs=(), env: Incomplete | None = None): ...
    def submit(self, fn, *args, **kwargs): ...
