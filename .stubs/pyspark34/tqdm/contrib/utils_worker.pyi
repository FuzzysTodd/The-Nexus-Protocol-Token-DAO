from _typeshed import Incomplete

__all__ = ['MonoWorker']

class MonoWorker:
    """
    Supports one running task and one waiting task.
    The waiting task is the most recent submitted (others are discarded).
    """
    pool: Incomplete
    futures: Incomplete
    def __init__(self) -> None: ...
    def submit(self, func, *args, **kwargs):
        """`func(*args, **kwargs)` may replace currently waiting task."""
