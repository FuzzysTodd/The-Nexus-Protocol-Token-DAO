from _typeshed import Incomplete
from tensorflow.core.protobuf import config_pb2 as config_pb2, rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.core.util import test_log_pb2 as test_log_pb2
from tensorflow.python.client import timeline as timeline
from tensorflow.python.framework import ops as ops
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.util import tf_inspect as tf_inspect
from tensorflow.python.util.tf_export import tf_export as tf_export

GLOBAL_BENCHMARK_REGISTRY: Incomplete
TEST_REPORTER_TEST_ENV: str
OVERRIDE_GLOBAL_THREADPOOL: str

class _BenchmarkRegistrar(type):
    """The Benchmark class registrar.  Used by abstract Benchmark class."""
    def __new__(mcs, clsname, base, attrs): ...

class ParameterizedBenchmark(_BenchmarkRegistrar):
    '''Metaclass to generate parameterized benchmarks.

  Use this class as a metaclass and override the `_benchmark_parameters` to
  generate multiple benchmark test cases. For example:

  class FooBenchmark(metaclass=tf.test.ParameterizedBenchmark,
                     tf.test.Benchmark):
    # The `_benchmark_parameters` is expected to be a list with test cases.
    # Each of the test case is a tuple, with the first time to be test case
    # name, followed by any number of the parameters needed for the test case.
    _benchmark_parameters = [
      (\'case_1\', Foo, 1, \'one\'),
      (\'case_2\', Bar, 2, \'two\'),
    ]

    def benchmark_test(self, target_class, int_param, string_param):
      # benchmark test body

  The example above will generate two benchmark test cases:
  "benchmark_test__case_1" and "benchmark_test__case_2".
  '''
    def __new__(mcs, clsname, base, attrs): ...

class Benchmark(metaclass=_BenchmarkRegistrar):
    '''Abstract class that provides helper functions for running benchmarks.

  Any class subclassing this one is immediately registered in the global
  benchmark registry.

  Only methods whose names start with the word "benchmark" will be run during
  benchmarking.
  '''
    @classmethod
    def is_abstract(cls): ...
    def report_benchmark(self, iters: Incomplete | None = None, cpu_time: Incomplete | None = None, wall_time: Incomplete | None = None, throughput: Incomplete | None = None, extras: Incomplete | None = None, name: Incomplete | None = None, metrics: Incomplete | None = None) -> None:
        """Report a benchmark.

    Args:
      iters: (optional) How many iterations were run
      cpu_time: (optional) Median or mean cpu time in seconds.
      wall_time: (optional) Median or mean wall time in seconds.
      throughput: (optional) Throughput (in MB/s)
      extras: (optional) Dict mapping string keys to additional benchmark info.
        Values may be either floats or values that are convertible to strings.
      name: (optional) Override the BenchmarkEntry name with `name`.
        Otherwise it is inferred from the top-level method name.
      metrics: (optional) A list of dict, where each dict has the keys below
        name (required), string, metric name
        value (required), double, metric value
        min_value (optional), double, minimum acceptable metric value
        max_value (optional), double, maximum acceptable metric value
    """

def benchmark_config():
    """Returns a tf.compat.v1.ConfigProto for disabling the dependency optimizer.

    Returns:
      A TensorFlow ConfigProto object.
  """

class TensorFlowBenchmark(Benchmark):
    """Abstract class that provides helpers for TensorFlow benchmarks."""
    def __init__(self) -> None: ...
    @classmethod
    def is_abstract(cls): ...
    def run_op_benchmark(self, sess, op_or_tensor, feed_dict: Incomplete | None = None, burn_iters: int = 2, min_iters: int = 10, store_trace: bool = False, store_memory_usage: bool = True, name: Incomplete | None = None, extras: Incomplete | None = None, mbs: int = 0):
        '''Run an op or tensor in the given session.  Report the results.

    Args:
      sess: `Session` object to use for timing.
      op_or_tensor: `Operation` or `Tensor` to benchmark.
      feed_dict: A `dict` of values to feed for each op iteration (see the
        `feed_dict` parameter of `Session.run`).
      burn_iters: Number of burn-in iterations to run.
      min_iters: Minimum number of iterations to use for timing.
      store_trace: Boolean, whether to run an extra untimed iteration and
        store the trace of iteration in returned extras.
        The trace will be stored as a string in Google Chrome trace format
        in the extras field "full_trace_chrome_format". Note that trace
        will not be stored in test_log_pb2.TestResults proto.
      store_memory_usage: Boolean, whether to run an extra untimed iteration,
        calculate memory usage, and store that in extras fields.
      name: (optional) Override the BenchmarkEntry name with `name`.
        Otherwise it is inferred from the top-level method name.
      extras: (optional) Dict mapping string keys to additional benchmark info.
        Values may be either floats or values that are convertible to strings.
      mbs: (optional) The number of megabytes moved by this op, used to
        calculate the ops throughput.

    Returns:
      A `dict` containing the key-value pairs that were passed to
      `report_benchmark`. If `store_trace` option is used, then
      `full_chrome_trace_format` will be included in return dictionary even
      though it is not passed to `report_benchmark` with `extras`.
    '''
    def evaluate(self, tensors):
        """Evaluates tensors and returns numpy values.

    Args:
      tensors: A Tensor or a nested list/tuple of Tensors.

    Returns:
      tensors numpy values.
    """

def benchmarks_main(true_main, argv: Incomplete | None = None):
    """Run benchmarks as declared in argv.

  Args:
    true_main: True main function to run if benchmarks are not requested.
    argv: the command line arguments (if None, uses sys.argv).
  """
