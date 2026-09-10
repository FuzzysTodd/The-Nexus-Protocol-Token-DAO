from _typeshed import Incomplete
from tensorflow.python.eager import test as test
from tensorflow.python.platform import flags as flags

class MicroBenchmarksBase(test.Benchmark):
    """Run and report benchmark results.

  The first run is without any profilng.
  Second run is with xprof and python trace. Third run is with xprof without
  python trace. Note: xprof runs are with fewer iterations.
  """
    def run_with_xprof(self, enable_python_trace, run_benchmark, func, num_iters_xprof, execution_mode, suid): ...
    def run_report(self, run_benchmark, func, num_iters, execution_mode: Incomplete | None = None) -> None:
        """Run and report benchmark results."""
