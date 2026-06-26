from _typeshed import Incomplete
from tensorflow.python.profiler import trace as trace

class _PythonMemoryChecker:
    """Python memory leak detection class."""
    def __init__(self) -> None: ...
    def record_snapshot(self) -> None: ...
    def report(self) -> None: ...
    def assert_no_leak_if_all_possibly_except_one(self) -> None:
        """Raises an exception if a leak is detected.

    This algorithm classifies a series of allocations as a leak if it's the same
    type at every snapshot, but possibly except one snapshot.
    """
    def assert_no_new_objects(self, threshold: Incomplete | None = None) -> None:
        """Assert no new Python objects."""
