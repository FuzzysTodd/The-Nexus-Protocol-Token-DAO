from _typeshed import Incomplete
from joblib.parallel import AutoBatchingMixin, ParallelBackendBase

def register() -> None:
    """
    Register joblib spark backend.
    """

class SparkDistributedBackend(ParallelBackendBase, AutoBatchingMixin):
    """A ParallelBackend which will execute all batches on spark.

    This backend will launch one spark job for task batch. Multiple spark job will run parallelly.
    The maximum parallelism won't exceed `sparkContext._jsc.sc().maxNumConcurrentTasks()`

    Each task batch will be run inside one spark task on worker node, and will be executed
    by `SequentialBackend`
    """
    def __init__(self, **backend_args) -> None: ...
    def effective_n_jobs(self, n_jobs): ...
    def abort_everything(self, ensure_ready: bool = True) -> None: ...
    def terminate(self) -> None: ...
    parallel: Incomplete
    def configure(self, n_jobs: int = 1, parallel: Incomplete | None = None, prefer: Incomplete | None = None, require: Incomplete | None = None, **backend_args): ...
    def start_call(self) -> None: ...
    def apply_async(self, func, callback: Incomplete | None = None): ...
    def get_nested_backend(self):
        """Backend instance to be used by nested Parallel calls.
           For nested backend, always use `SequentialBackend`
        """
