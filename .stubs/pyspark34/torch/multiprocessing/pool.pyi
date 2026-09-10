import multiprocessing.pool
from .queue import SimpleQueue as SimpleQueue

def clean_worker(*args, **kwargs) -> None: ...

class Pool(multiprocessing.pool.Pool):
    """Pool implementation which uses our version of SimpleQueue.
    This lets us pass tensors in shared memory across processes instead of
    serializing the underlying data."""
