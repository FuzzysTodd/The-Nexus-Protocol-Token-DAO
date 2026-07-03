from _typeshed import Incomplete
from tensorflow.python.profiler import trace as trace
from tensorflow.python.util import tf_inspect as tf_inspect

class MemoryChecker:
    """Memory leak detection class.

  This is a utility class to detect Python and C++ memory leaks. It's intended
  for both testing and debugging. Basic usage:

  >>> # MemoryChecker() context manager tracks memory status inside its scope.
  >>> with MemoryChecker() as memory_checker:
  >>>   tensors = []
  >>>   for _ in range(10):
  >>>     # Simulating `tf.constant(1)` object leak every iteration.
  >>>     tensors.append(tf.constant(1))
  >>>
  >>>     # Take a memory snapshot for later analysis.
  >>>     memory_checker.record_snapshot()
  >>>
  >>> # `report()` generates a html graph file showing allocations over
  >>> # snapshots per every stack trace.
  >>> memory_checker.report()
  >>>
  >>> # This assertion will detect `tf.constant(1)` object leak.
  >>> memory_checker.assert_no_leak_if_all_possibly_except_one()

  `record_snapshot()` must be called once every iteration at the same location.
  This is because the detection algorithm relies on the assumption that if there
  is a leak, it's happening similarly on every snapshot.
  """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def record_snapshot(self) -> None:
        """Take a memory snapshot for later analysis.

    `record_snapshot()` must be called once every iteration at the same
    location. This is because the detection algorithm relies on the assumption
    that if there is a leak, it's happening similarly on every snapshot.

    The recommended number of `record_snapshot()` call depends on the testing
    code complexity and the allcoation pattern.
    """
    def report(self) -> None:
        """Generates a html graph file showing allocations over snapshots.

    It create a temporary directory and put all the output files there.
    If this is running under Google internal testing infra, it will use the
    directory provided the infra instead.
    """
    def assert_no_leak_if_all_possibly_except_one(self) -> None:
        """Raises an exception if a leak is detected.

    This algorithm classifies a series of allocations as a leak if it's the same
    type(Python) or it happens at the same stack trace(C++) at every snapshot,
    but possibly except one snapshot.
    """
    def assert_no_new_python_objects(self, threshold: Incomplete | None = None) -> None:
        """Raises an exception if there are new Python objects created.

    It computes the number of new Python objects per type using the first and
    the last snapshots.

    Args:
      threshold: A dictionary of [Type name string], [count] pair. It won't
        raise an exception if the new Python objects are under this threshold.
    """
