from ._memmapping_reducer import TemporaryResourcesManager as TemporaryResourcesManager, get_memmapping_reducers as get_memmapping_reducers
from .externals.loky.reusable_executor import _ReusablePoolExecutor
from _typeshed import Incomplete

def get_memmapping_executor(n_jobs, **kwargs): ...

class MemmappingExecutor(_ReusablePoolExecutor):
    @classmethod
    def get_memmapping_executor(cls, n_jobs, timeout: int = 300, initializer: Incomplete | None = None, initargs=(), env: Incomplete | None = None, temp_folder: Incomplete | None = None, context_id: Incomplete | None = None, **backend_args):
        """Factory for ReusableExecutor with automatic memmapping for large
        numpy arrays.
        """
    def terminate(self, kill_workers: bool = False) -> None: ...

class _TestingMemmappingExecutor(MemmappingExecutor):
    """Wrapper around ReusableExecutor to ease memmapping testing with Pool
    and Executor. This is only for testing purposes.

    """
    def apply_async(self, func, args):
        """Schedule a func to be run"""
    def map(self, f, *args): ...
