from _typeshed import Incomplete
from tensorflow.python.client import session as session
from tensorflow.python.data.ops import dataset_ops as dataset_ops
from tensorflow.python.data.util import nest as nest
from tensorflow.python.eager import context as context
from tensorflow.python.platform import test as test

class DatasetBenchmarkBase(test.Benchmark):
    """Base class for dataset benchmarks."""
    def run_op_benchmark(self, op, iters: int = 1, warmup: bool = True, session_config: Incomplete | None = None):
        """Benchmarks the op.

    Runs the op `iters` times. In each iteration, the benchmark measures
    the time it takes to go execute the op.

    Args:
      op: The tf op to benchmark.
      iters: Number of times to repeat the timing.
      warmup: If true, warms up the session caches by running an untimed run.
      session_config: A ConfigProto protocol buffer with configuration options
        for the session. Applicable only for benchmarking in graph mode.

    Returns:
      A float, representing the per-execution wall time of the op in seconds.
      This is the median time (with respect to `iters`) it takes for the op
      to be executed `iters` num of times.
    """
    def run_benchmark(self, dataset, num_elements, iters: int = 1, warmup: bool = True, apply_default_optimizations: bool = False, session_config: Incomplete | None = None):
        """Benchmarks the dataset.

    Runs the dataset `iters` times. In each iteration, the benchmark measures
    the time it takes to go through `num_elements` elements of the dataset.

    Args:
      dataset: Dataset to benchmark.
      num_elements: Number of dataset elements to iterate through each benchmark
        iteration.
      iters: Number of times to repeat the timing.
      warmup: If true, warms up the session caches by running an untimed run.
      apply_default_optimizations: Determines whether default optimizations
        should be applied.
      session_config: A ConfigProto protocol buffer with configuration options
        for the session. Applicable only for benchmarking in graph mode.

    Returns:
      A float, representing the per-element wall time of the dataset in seconds.
      This is the median time (with respect to `iters`) it takes for the dataset
      to go through `num_elements` elements, divided by `num_elements.`
    """
    def run_and_report_benchmark(self, dataset, num_elements, name, iters: int = 5, extras: Incomplete | None = None, warmup: bool = True, apply_default_optimizations: bool = False, session_config: Incomplete | None = None):
        """Benchmarks the dataset and reports the stats.

    Runs the dataset `iters` times. In each iteration, the benchmark measures
    the time it takes to go through `num_elements` elements of the dataset.
    This is followed by logging/printing the benchmark stats.

    Args:
      dataset: Dataset to benchmark.
      num_elements: Number of dataset elements to iterate through each benchmark
        iteration.
      name: Name of the benchmark.
      iters: Number of times to repeat the timing.
      extras: A dict which maps string keys to additional benchmark info.
      warmup: If true, warms up the session caches by running an untimed run.
      apply_default_optimizations: Determines whether default optimizations
        should be applied.
      session_config: A ConfigProto protocol buffer with configuration options
        for the session. Applicable only for benchmarking in graph mode.

    Returns:
      A float, representing the per-element wall time of the dataset in seconds.
      This is the median time (with respect to `iters`) it takes for the dataset
      to go through `num_elements` elements, divided by `num_elements.`
    """
