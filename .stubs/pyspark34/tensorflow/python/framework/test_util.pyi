from _typeshed import Incomplete
from collections.abc import Generator
from tensorflow.core.config import flags as flags
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.core.protobuf import rewriter_config_pb2 as rewriter_config_pb2
from tensorflow.python import pywrap_sanitizers as pywrap_sanitizers, tf2 as tf2
from tensorflow.python.client import device_lib as device_lib, pywrap_tf_session as pywrap_tf_session, session as session
from tensorflow.python.compat.compat import forward_compatibility_horizon as forward_compatibility_horizon
from tensorflow.python.eager import backprop as backprop, context as context, def_function as def_function, tape as tape
from tensorflow.python.framework import config as config, dtypes as dtypes, errors as errors, errors_impl as errors_impl, gpu_util as gpu_util, importer as importer, indexed_slices as indexed_slices, ops as ops, random_seed as random_seed, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util, tfrt_utils as tfrt_utils, versions as versions
from tensorflow.python.framework.is_mlir_bridge_test_true import is_mlir_bridge_enabled as is_mlir_bridge_enabled
from tensorflow.python.framework.is_xla_test_true import is_xla_enabled as is_xla_enabled
from tensorflow.python.ops import array_ops as array_ops, control_flow_util as control_flow_util, control_flow_util_v2 as control_flow_util_v2, gen_sync_ops as gen_sync_ops, gradients_impl as gradients_impl, math_ops as math_ops, script_ops as script_ops, summary_ops_v2 as summary_ops_v2, variables as variables
from tensorflow.python.ops.ragged import ragged_ops as ragged_ops, ragged_tensor as ragged_tensor, ragged_tensor_value as ragged_tensor_value
from tensorflow.python.platform import googletest as googletest
from tensorflow.python.training import server_lib as server_lib
from tensorflow.python.util import compat as compat, deprecation as deprecation, nest as nest, tf_decorator as tf_decorator, tf_inspect as tf_inspect, traceback_utils as traceback_utils
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.protobuf import compare as compare
from tensorflow.python.util.tf_export import tf_export as tf_export

def is_xla_enabled(): ...
def is_mlir_bridge_enabled() -> None: ...
def is_asan_enabled():
    """Check if ASAN is enabled."""
def is_msan_enabled():
    """Check if MSAN is enabled."""
def is_tsan_enabled():
    """Check if TSAN is enabled."""
def is_ubsan_enabled():
    """Check if UBSAN is enabled."""
def gpu_device_name():
    '''Returns the name of a GPU device if available or a empty string.

  This method should only be used in tests written with `tf.test.TestCase`.

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_gpu(self):
  ...     if not tf.test.is_built_with_gpu_support():
  ...       self.skipTest("test is only applicable on GPU")
  ...
  ...     with tf.device(tf.test.gpu_device_name()):
  ...       self.assertEqual(tf.math.add(1.0, 2.0), 3.0)

  '''
def assert_ops_in_graph(expected_ops, graph):
    """Assert all expected operations are found.

  Args:
    expected_ops: `dict<string, string>` of op name to op type.
    graph: Graph to check.

  Returns:
    `dict<string, node>` of node name to node.

  Raises:
    ValueError: If the expected ops are not present in the graph.
  """
def assert_equal_graph_def_v2(expected, actual) -> None:
    """Asserts that two `GraphDef`s are (mostly) the same.

  Compares two `GraphDef` protos for equality, ignoring versions and ordering of
  nodes, attrs, and control inputs.  Node names are used to match up nodes
  between the graphs, so the naming of nodes must be consistent. This function
  ignores randomized attribute values that may appear in V2 checkpoints.

  Args:
    expected: The `GraphDef` we expected.
    actual: The `GraphDef` we have.

  Raises:
    AssertionError: If the `GraphDef`s do not match.
    TypeError: If either argument is not a `GraphDef`.
  """
def assert_equal_graph_def_v1(actual, expected, checkpoint_v2: bool = False, hash_table_shared_name: bool = False) -> None:
    """Asserts that two `GraphDef`s are (mostly) the same.

  Compares two `GraphDef` protos for equality, ignoring versions and ordering of
  nodes, attrs, and control inputs.  Node names are used to match up nodes
  between the graphs, so the naming of nodes must be consistent.

  Args:
    actual: The `GraphDef` we have.
    expected: The `GraphDef` we expected.
    checkpoint_v2: boolean determining whether to ignore randomized attribute
      values that appear in V2 checkpoints.
    hash_table_shared_name: boolean determining whether to ignore randomized
      shared_names that appear in HashTableV2 op defs.

  Raises:
    AssertionError: If the `GraphDef`s do not match.
    TypeError: If either argument is not a `GraphDef`.
  """
def assert_equal_graph_def(actual, expected, checkpoint_v2: bool = False, hash_table_shared_name: bool = False) -> None: ...
def assert_meta_graph_protos_equal(tester, a, b) -> None:
    """Compares MetaGraphDefs `a` and `b` in unit test class `tester`."""
def IsGoogleCudaEnabled(): ...
def IsBuiltWithROCm(): ...
def IsBuiltWithXLA(): ...
def IsBuiltWithNvcc(): ...
def GpuSupportsHalfMatMulAndConv(): ...
def IsMklEnabled(): ...
def InstallStackTraceHandler() -> None: ...
def NHWCToNCHW(input_tensor):
    """Converts the input from the NHWC format to NCHW.

  Args:
    input_tensor: a 3-, 4-, or 5-D tensor, or an array representing shape

  Returns:
    converted tensor or shape array
  """
def NHWCToNCHW_VECT_C(input_shape_or_tensor):
    """Transforms the input from the NHWC layout to NCHW_VECT_C layout.

  Note: Does not include quantization or type conversion steps, which should
  be applied afterwards.

  Args:
    input_shape_or_tensor: a 4- or 5-D tensor, or an array representing shape

  Returns:
    tensor or shape array transformed into NCHW_VECT_C

  Raises:
    ValueError: if last dimension of `input_shape_or_tensor` is not evenly
        divisible by 4.
  """
def NCHW_VECT_CToNHWC(input_shape_or_tensor):
    """Transforms the input from the NCHW_VECT_C layout to NHWC layout.

  Note: Does not include de-quantization or type conversion steps, which should
  be applied beforehand.

  Args:
    input_shape_or_tensor: a 5- or 6-D tensor, or an array representing shape

  Returns:
    tensor or shape array transformed into NHWC

  Raises:
    ValueError: if last dimension of `input_shape_or_tensor` is not 4.
  """
def NCHWToNHWC(input_tensor):
    """Converts the input from the NCHW format to NHWC.

  Args:
    input_tensor: a 4- or 5-D tensor, or an array representing shape

  Returns:
    converted tensor or shape array
  """
def skip_if(condition):
    '''Skips the decorated function if condition is or evaluates to True.

  Args:
    condition: Either an expression that can be used in "if not condition"
      statement, or a callable whose result should be a boolean.

  Returns:
    The wrapped function
  '''
def skip_if_error(test_obj, error_type, messages: Incomplete | None = None) -> Generator[None, None, None]:
    """Context manager to skip cases not considered failures by the tests.

  Note that this does not work if used in setUpClass/tearDownClass.
  Usage in setUp/tearDown works fine just like regular test methods.

  Args:
    test_obj: A test object provided as `self` in the test methods; this object
      is usually an instance of `unittest.TestCase`'s subclass and should have
      `skipTest` method.
    error_type: The error type to skip. Note that if `messages` are given, both
      `error_type` and `messages` need to match for the test to be skipped.
    messages: Optional, a string or list of strings. If `None`, the test will be
      skipped if `error_type` matches what is raised; otherwise, the test is
      skipped if any of the `messages` is contained in the message of the error
      raised, and `error_type` matches the error raised.

  Yields:
    Nothing.
  """
def enable_c_shapes(fn):
    """No-op. TODO(b/74620627): Remove this."""
def with_c_shapes(cls):
    """No-op. TODO(b/74620627): Remove this."""
def enable_control_flow_v2(fn):
    """Decorator for enabling CondV2 and WhileV2 on a test.

  Note this enables using CondV2 and WhileV2 after running the test class's
  setup/teardown methods.

  In addition to this, callers must import the while_v2 module in order to set
  the _while_v2 module in control_flow_ops.

  Args:
    fn: the function to be wrapped

  Returns:
    The wrapped function
  """
def with_control_flow_v2(cls):
    '''Adds methods that call original methods with WhileV2 and CondV2 enabled.

  Note this enables CondV2 and WhileV2 in new methods after running the test
  class\'s setup method.

  In addition to this, callers must import the while_v2 module in order to set
  the _while_v2 module in control_flow_ops.

  If a test function has _disable_control_flow_v2 attr set to True (using the
  @disable_control_flow_v2 decorator), the v2 function is not generated for it.

  Example:

  @test_util.with_control_flow_v2
  class ControlFlowTest(test.TestCase):

    def testEnabledForV2(self):
      ...

    @test_util.disable_control_flow_v2("b/xyzabc")
    def testDisabledForV2(self):
      ...

  Generated class:
  class ControlFlowTest(test.TestCase):

    def testEnabledForV2(self):
      ...

    def testEnabledForV2WithControlFlowV2(self):
      // Enable V2 flags.
      testEnabledForV2(self)
      // Restore V2 flags.

    def testDisabledForV2(self):
      ...

  Args:
    cls: class to decorate

  Returns:
    cls with new test methods added
  '''
def disable_control_flow_v2(unused_msg):
    """Decorator for a function in a with_control_flow_v2 enabled test class.

  Blocks the function from being run with v2 control flow ops.

  Args:
    unused_msg: Reason for disabling.

  Returns:
    The wrapped function with _disable_control_flow_v2 attr set to True.
  """
def enable_output_all_intermediates(fn):
    """Force-enable outputing all intermediates from functional control flow ops.

  Args:
    fn: the function to be wrapped

  Returns:
    The wrapped function
  """
def assert_no_new_pyobjects_executing_eagerly(func: Incomplete | None = None, warmup_iters: int = 2):
    """Decorator for asserting that no new Python objects persist after a test.

  Runs the test multiple times executing eagerly, first as a warmup and then to
  let objects accumulate. The warmup helps ignore caches which do not grow as
  the test is run repeatedly.

  Useful for checking that there are no missing Py_DECREFs in the C exercised by
  a bit of Python.

  Args:
    func: The function to test.
    warmup_iters: The numer of warmup iterations, excluded from measuring.

  Returns:
    The wrapped function performing the test.
  """
def assert_no_new_tensors(f):
    """Decorator for asserting that no new Tensors persist after a test.

  Mainly useful for checking that code using the Python C API has correctly
  manipulated reference counts.

  Clears the caches that it knows about, runs the garbage collector, then checks
  that there are no Tensor or Tensor-like objects still around. This includes
  Tensors to which something still has a reference (e.g. from missing
  Py_DECREFs) and uncollectable cycles (i.e. Python reference cycles where one
  of the objects has __del__ defined).

  Args:
    f: The test case to run.

  Returns:
    The decorated test case.
  """
def assert_no_garbage_created(f):
    """Test method decorator to assert that no garbage has been created.

  Note that this decorator sets DEBUG_SAVEALL, which in some Python interpreters
  cannot be un-set (i.e. will disable garbage collection for any other unit
  tests in the same file/shard).

  Args:
    f: The function to decorate.

  Returns:
    The decorated function.
  """
def generate_combinations_with_testcase_name(**kwargs):
    """Generate combinations based on its keyword arguments using combine().

  This function calls combine() and appends a testcase name to the list of
  dictionaries returned. The 'testcase_name' key is a required for named
  parameterized tests.

  Args:
    **kwargs: keyword arguments of form `option=[possibilities, ...]` or
      `option=the_only_possibility`.

  Returns:
    a list of dictionaries for each combination. Keys in the dictionaries are
    the keyword argument names.  Each key has one value - one of the
    corresponding keyword argument values.
  """
def run_all_in_graph_and_eager_modes(cls):
    """Execute all test methods in the given class with and without eager."""
def enable_nested_function_shape_inference(fn):
    """Decorator for enabling nested_function_shape_inference on a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will set nested_function_shape_inference,
  reset the context, execute the test, then reset the context to the state
  it was in prior to this test.

  Example:

  class MyTest(test.TestCase):

    @enable_nested_function_shape_inference
    def testFoo(self):
      ...

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """
def enable_quantized_dtypes_training(fn):
    """Decorator for enabling quantized_dtypes_training on a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will set quantized_dtypes_training,
  reset the context, execute the test, then reset the context to the state
  it was in prior to this test.

  Example:

  class MyTest(test.TestCase):

    @enable_quantized_dtypes_training
    def testFoo(self):
      ...

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """
def enable_eager_op_as_function(fn):
    """Returns the same fn. This will be removed once all usages are removed.

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """
def with_eager_op_as_function(cls: Incomplete | None = None, only_as_function: bool = False):
    """Returns the same class. This will be removed once all usages are removed.

  Args:
    cls: class to decorate.
    only_as_function: unused argument.

  Returns:
    cls
  """
def enable_graph_building_optimization(fn):
    """Decorator for enabling graph_building_optimization on a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will enable graph_building_optimization,
  execute the test, then reset the feature flag to its default value.

  Example:

  class MyTest(test.TestCase):

    @enable_graph_building_optimization
    def testFoo(self):
      ...

  Args:
    fn: the function to be wrapped.

  Returns:
    The wrapped function.
  """
def add_graph_building_optimization_tests(cls: Incomplete | None = None):
    """Adds methods with graph_building_optimization enabled to the test suite.

  Example:

  @test_util.add_graph_building_optimization_tests
  class FooTest(test.TestCase):

    def testBar(self):
      ...

  Generated class:
  class FooTest(test.TestCase):

    def testBar(self):
      ...

    def testBarWithGraphBuildingOptimization(self):
      // Enable graph_building_optimization
      testBar(self)
      // Disable graph_building_optimization

  Args:
    cls: class to decorate.

  Returns:
    cls with new test methods added.
  """
def disable_eager_op_as_function(unused_msg):
    """Decorator for a function in a with_eager_op_as_function enabled test class.

  Blocks the function from being run with eager_op_as_function enabled.

  Args:
    unused_msg: Reason for disabling.

  Returns:
    The wrapped function with _disable_eager_op_as_function attr set to True.
  """
def set_xla_env_flag(func: Incomplete | None = None, flag: str = ''):
    """Decorator for setting XLA_FLAGS prior to running a test.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will allow users to set any xla flags
  exposed via the XLA_FLAGS environment variable, execute the test, then reset
  the XLA_FLAGS to the state it was in prior to this test.

  Example:

  class MyTest(test.TestCase):

    @set_xla_env_flag(flag='--xla_gpu_enable_fast_min_max=false')
    def testFoo(self):
      ...

  Args:
    func: The function to be wrapped.
    flag: The xla flag to be set in the XLA_FLAGS env variable.

  Returns:
    The wrapped function.
  """
def build_as_function_and_v1_graph(func: Incomplete | None = None):
    """Run a test case in v1 graph mode and inside tf.function in eager mode.

  WARNING: This decorator can only be used in test cases that statically checks
  generated graph. Attempting to evaluate graph or function results via.
  session.run() or self.evaluate() will fail.

  WARNING: This decorator can only be used for test cases that inherit from
  absl.testing.parameterized.TestCase.

  Args:
    func: Test case function to be decorated.

  Returns:
    Decorated test case function.
  """
def run_in_async_and_sync_mode(f):
    """Execute the test in async mode and sync mode."""
def run_in_graph_and_eager_modes(func: Incomplete | None = None, config: Incomplete | None = None, use_gpu: bool = True, assert_no_eager_garbage: bool = False):
    '''Execute the decorated test with and without enabling eager execution.

  This function returns a decorator intended to be applied to test methods in
  a `tf.test.TestCase` class. Doing so will cause the contents of the test
  method to be executed twice - once normally, and once with eager execution
  enabled. This allows unittests to confirm the equivalence between eager
  and graph execution (see `tf.compat.v1.enable_eager_execution`).

  For example, consider the following unittest:

  ```python
  class MyTests(tf.test.TestCase):

    @run_in_graph_and_eager_modes
    def test_foo(self):
      x = tf.constant([1, 2])
      y = tf.constant([3, 4])
      z = tf.add(x, y)
      self.assertAllEqual([4, 6], self.evaluate(z))

  if __name__ == "__main__":
    tf.test.main()
  ```

  This test validates that `tf.add()` has the same behavior when computed with
  eager execution enabled as it does when constructing a TensorFlow graph and
  executing the `z` tensor in a session.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.


  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.
    config: An optional config_pb2.ConfigProto to use to configure the session
      when executing graphs.
    use_gpu: If True, attempt to run as many operations as possible on GPU.
    assert_no_eager_garbage: If True, sets DEBUG_SAVEALL on the garbage
      collector and asserts that no extra garbage has been created when running
      the test with eager execution enabled. This will fail if there are
      reference cycles (e.g. a = []; a.append(a)). Off by default because some
      tests may create garbage for legitimate reasons (e.g. they define a class
      which inherits from `object`), and because DEBUG_SAVEALL is sticky in some
      Python interpreters (meaning that tests which rely on objects being
      collected elsewhere in the unit test file will not work). Additionally,
      checks that nothing still has a reference to Tensors that the test
      allocated.

  Returns:
    Returns a decorator that will run the decorated test method twice:
    once by constructing and executing a graph in a session and once with
    eager execution enabled.
  '''
def py_func_if_in_function(f): ...
def also_run_as_tf_function(f):
    """Runs the decorated test twice--once as is, once inside a tf.function.

  This allows you to run a test both in eager execution and inside a
  tf.function, exercising the two execution modes supported in tf 2.0. The test
  assertions are automatically done inside tf.py_funcs, and tf.function ensures
  that they run in the proper order and with the proper side effects.

  Currently variable creation is not supported in tests annotated with this
  decorator since it's tricky to ensure the variable doesn't get repeatedly
  created when retracing the tf.function.

  Args:
    f: the test method to be decorated

  Returns:
    The decorated test method, which will run both in eager and inside a
    tf.function.
  """
def deprecated_graph_mode_only(func: Incomplete | None = None):
    """Execute the decorated test in graph mode.

  This function returns a decorator intended to be applied to tests that are not
  compatible with eager mode. When this decorator is applied, the test body will
  be run in an environment where API calls construct graphs instead of executing
  eagerly.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will run the decorated test method in graph mode.
  """
run_deprecated_v1 = deprecated_graph_mode_only

def run_all_in_deprecated_graph_mode_only(cls):
    """Execute all tests in a class in graph mode."""
def run_v1_only(reason, func: Incomplete | None = None):
    """Execute the decorated test only if running in v1 mode.

  This function is intended to be applied to tests that exercise v1 only
  functionality. If the test is run in v2 mode it will simply be skipped.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.

  Args:
    reason: string giving a reason for limiting the test to v1 only.
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """
def run_v2_only(func: Incomplete | None = None):
    """Execute the decorated test only if running in v2 mode.

  This function is intended to be applied to tests that exercise v2 only
  functionality. If the test is run in v1 mode it will simply be skipped.

  `deprecated_graph_mode_only`, `run_v1_only`, `run_v2_only`, and
  `run_in_graph_and_eager_modes` are available decorators for different
  v1/v2/eager/graph combinations.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """
def run_gpu_only(func: Incomplete | None = None):
    """Execute the decorated test only if a GPU is available.

  This function is intended to be applied to tests that require the presence
  of a GPU. If a GPU is absent, it will simply be skipped.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """
def run_cuda_only(func: Incomplete | None = None):
    """Execute the decorated test only if a GPU is available.

  This function is intended to be applied to tests that require the presence
  of a CUDA GPU. If a CUDA GPU is absent, it will simply be skipped.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """
def run_gpu_or_tpu(func: Incomplete | None = None):
    """Execute the decorated test only if a physical GPU or TPU is available.

  This function is intended to be applied to tests that require the presence
  of a physical GPU or TPU. It complies with the following rules:
  - If a GPU is available, the test will run on the GPU.
  - If a GPU is absent and a TPU is available, the test will run on the TPU.
  - If both GPU and TPU are absent, the test will be skipped.

  Args:
    func: function to be annotated. If `func` is None, this method returns a
      decorator the can be applied to a function. If `func` is not None this
      returns the decorator applied to `func`.

  Returns:
    Returns a decorator that will conditionally skip the decorated test method.
  """
def with_forward_compatibility_horizons(*horizons):
    """Executes the decorated test with the specified forward-compat horizons.

  Args:
    *horizons: A list of (year, month, day) tuples.  If the list includes
      `None`, then the test will also be run with no forward-compatibility
      horizon set.

  Returns:
    A decorator that will execute the test with the specified horizons.
  """
def is_gpu_available(cuda_only: bool = False, min_cuda_compute_capability: Incomplete | None = None):
    '''Returns whether TensorFlow can access a GPU.

  Warning: if a non-GPU version of the package is installed, the function would
  also return False. Use `tf.test.is_built_with_cuda` to validate if TensorFlow
  was build with CUDA support.

  For example,
  >>> gpu_available = tf.test.is_gpu_available()
  >>> is_cuda_gpu_available = tf.test.is_gpu_available(cuda_only=True)
  >>> is_cuda_gpu_min_3 = tf.test.is_gpu_available(True, (3,0))

  Args:
    cuda_only: limit the search to CUDA GPUs.
    min_cuda_compute_capability: a (major,minor) pair that indicates the minimum
      CUDA compute capability required, or None if no requirement.

  Note that the keyword arg name "cuda_only" is misleading (since routine will
  return true when a GPU device is available irrespective of whether TF was
  built with CUDA support or ROCm support. However no changes here because

  ++ Changing the name "cuda_only" to something more generic would break
     backward compatibility

  ++ Adding an equivalent "rocm_only" would require the implementation check
     the build type. This in turn would require doing the same for CUDA and thus
     potentially break backward compatibility

  ++ Adding a new "cuda_or_rocm_only" would not break backward compatibility,
     but would require most (if not all) callers to update the call to use
     "cuda_or_rocm_only" instead of "cuda_only"

  Returns:
    True if a GPU device of the requested kind is available.
  '''
def device(use_gpu) -> Generator[None, None, None]:
    """Uses gpu when requested and available."""
def use_gpu() -> Generator[None, None, None]:
    """Uses gpu when requested and available."""
def force_gpu() -> Generator[None, None, None]:
    """Force the gpu to be used."""
def force_cpu() -> Generator[None, None, None]:
    """Force the cpu to be used."""
def deterministic_ops() -> Generator[None, None, None]:
    """Enables deterministic ops."""

class CapturedWrites:
    """A utility class to load the captured writes made to a stream."""
    capture_location: Incomplete
    def __init__(self, capture_location) -> None: ...
    def contents(self):
        """Get the captured writes as a single string."""

class FakeEagerSession:
    """Fake session so tests that conditionally use placeholders can use eager.

  There are a number of tests that conditionally use placeholders for shape
  inference. The pattern is demonstrated here:

  ```python
  with self.cached_session() as sess:
    if static_shape:
      y = math_ops.matmul(x, ...)
      feed_dict = {}
    else:
      x_ph = array_ops.placeholder(...)
      y = math_ops.matmul(x_ph, ...)
      feed_dict = {x_ph: x}
    val = sess.run(y, feed_dict=feed_dict)
  ```

  Since the feed_dict is empty when not using placeholders we should be able to
  call self.evaluate(), however this requires rewriting the test case.
  This class should be considered a stop-gap solution to get tests running with
  eager with minimal changes to the actual test.
  """
    def __init__(self, test_case) -> None: ...
    def run(self, fetches, *args, **kwargs):
        """Evaluate `fetches`.

    Fail if additional args are specified.

    Args:
      fetches: A Tensor or a nested list/tuple of Tensors.
      *args: Positional arguments
      **kwargs: Keyword arguments

    Raises:
      RuntimeError: If args or kwargs are specified.

    Returns:
      Tensors as numpy values.
    """

class ErrorLoggingSession(session.Session):
    """Wrapper around a Session that logs errors in run()."""
    def run(self, *args, **kwargs): ...

def disable_cudnn_autotune(func):
    """Disable autotuning during the call to this function.

  Some tests want to base assertions on a graph being isomorphic with a copy.
  To ensure this, this decorator disables autotuning.

  Args:
    func: Function to run with CuDNN autotuning turned off.

  Returns:
    Decorated function.
  """
def enable_tf_xla_constant_folding(description): ...
def disable_xla(description):
    """Execute the test method only if xla is not enabled."""
def disable_mlir_bridge(description):
    """Execute the test method only if MLIR bridge is not enabled."""
def disable_asan(description):
    """Execute the test method only if ASAN is not enabled."""
def disable_msan(description):
    """Execute the test method only if MSAN is not enabled."""
def disable_tsan(description):
    """Execute the test method only if TSAN is not enabled."""
def disable_ubsan(description):
    """Execute the test method only if UBSAN is not enabled."""
def disable_tfrt(unused_description): ...
def for_all_test_methods(decorator, *args, **kwargs):
    """Generate class-level decorator from given method-level decorator.

  It is expected for the given decorator to take some arguments and return
  a method that is then called on the test method to produce a decorated
  method.

  Args:
    decorator: The decorator to apply.
    *args: Positional arguments
    **kwargs: Keyword arguments
  Returns: Function that will decorate a given classes test methods with the
    decorator.
  """
def no_xla_auto_jit(description):
    """This test is not intended to be run with XLA auto jit enabled."""
def xla_allow_fallback(description): ...
def run_without_tensor_float_32(description):
    """Execute test with TensorFloat-32 disabled.

  While almost every real-world deep learning model runs fine with
  TensorFloat-32, many tests use assertAllClose or similar methods.
  TensorFloat-32 matmuls typically will cause such methods to fail with the
  default tolerances.

  Args:
    description: A description used for documentation purposes, describing why
      the test requires TensorFloat-32 to be disabled.

  Returns:
    Decorator which runs a test with TensorFloat-32 disabled.
  """
def run_all_without_tensor_float_32(description):
    """Execute all tests in a class with TensorFloat-32 disabled."""
def matmul_without_tf32(a, b, *args, **kwargs):
    """Run matmul but cast float32 inputs to float64 if TensorFloat-32 is enabled.

  This effectively runs matmul without TensorFloat-32. It should only be used in
  tests when verifying some other op or functions works correctly, e.g. to test
  `tf.linalg.sqrtm` by matrix multiplying the output of the op by itself. In
  such cases, the matmul itself is not being tested so it's OK to run it with
  higher precision.

  If a matmul itself is being tested, or some other op which uses matmul, use
  `run_without_tensor_float_32` instead.

  This also casts complex64 inputs to complex128, since TensorFloat-32 can also
  be used with complex64

  Args:
    a: First input to tf.linalg.matmul
    b: Second input to tf.linalg.matmul
    args: Other positional arguments to tf.linalg.matmul
    **kwargs: Other keyword arguments to tf.linalg.matmul

  Returns:
    A tensor with the same type as `a`.
  """

class EagerSessionWarner:
    def __getattr__(self, attr) -> None: ...

class TensorFlowTestCase(googletest.TestCase):
    """Base class for tests that need to test TensorFlow."""
    def __init__(self, methodName: str = 'runTest') -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def get_temp_dir(self):
        """Returns a unique temporary directory for the test to use.

    If you call this method multiple times during in a test, it will return the
    same folder. However, across different runs the directories will be
    different. This will ensure that across different runs tests will not be
    able to pollute each others environment.
    If you need multiple unique directories within a single test, you should
    use tempfile.mkdtemp as follows:
      tempfile.mkdtemp(dir=self.get_temp_dir()):

    Returns:
      string, the path to the unique temporary directory created for this test.
    """
    def captureWritesToStream(self, stream) -> Generator[Incomplete, None, None]:
        '''A context manager that captures the writes to a given stream.

    This context manager captures all writes to a given stream inside of a
    `CapturedWrites` object. When this context manager is created, it yields
    the `CapturedWrites` object. The captured contents can be accessed  by
    calling `.contents()` on the `CapturedWrites`.

    For this function to work, the stream must have a file descriptor that
    can be modified using `os.dup` and `os.dup2`, and the stream must support
    a `.flush()` method. The default python sys.stdout and sys.stderr are
    examples of this. Note that this does not work in Colab or Jupyter
    notebooks, because those use alternate stdout streams.

    Example:
    ```python
    class MyOperatorTest(test_util.TensorFlowTestCase):
      def testMyOperator(self):
        input = [1.0, 2.0, 3.0, 4.0, 5.0]
        with self.captureWritesToStream(sys.stdout) as captured:
          result = MyOperator(input).eval()
        self.assertStartsWith(captured.contents(), "This was printed.")
    ```

    Args:
      stream: The stream whose writes should be captured. This stream must have
        a file descriptor, support writing via using that file descriptor, and
        must have a `.flush()` method.

    Yields:
      A `CapturedWrites` object that contains all writes to the specified stream
      made during this context.
    '''
    def assertProtoEquals(self, expected_message_maybe_ascii, message, msg: Incomplete | None = None) -> None:
        """Asserts that message is same as parsed expected_message_ascii.

    Creates another prototype of message, reads the ascii message into it and
    then compares them using self._AssertProtoEqual().

    Args:
      expected_message_maybe_ascii: proto message in original or ascii form.
      message: the message to validate.
      msg: Optional message to report on failure.
    """
    def assertProtoEqualsVersion(self, expected, actual, producer=..., min_consumer=..., msg: Incomplete | None = None) -> None: ...
    def assertStartsWith(self, actual, expected_start, msg: Incomplete | None = None) -> None:
        """Assert that actual.startswith(expected_start) is True.

    Args:
      actual: str
      expected_start: str
      msg: Optional message to report on failure.
    """
    def evaluate(self, tensors):
        """Evaluates tensors and returns numpy values.

    Args:
      tensors: A Tensor or a nested list/tuple of Tensors.

    Returns:
      tensors numpy values.
    """
    def session(self, graph: Incomplete | None = None, config: Incomplete | None = None, use_gpu: bool = True, force_gpu: bool = False) -> Generator[Incomplete, None, None]:
        '''A context manager for a TensorFlow Session for use in executing tests.

    Note that this will set this session and the graph as global defaults.

    Use the `use_gpu` and `force_gpu` options to control where ops are run. If
    `force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if
    `use_gpu` is True, TensorFlow tries to run as many ops on the GPU as
    possible. If both `force_gpu and `use_gpu` are False, all ops are pinned to
    the CPU.

    Example:

    ``` python
    class MyOperatorTest(test_util.TensorFlowTestCase):
      def testMyOperator(self):
        with self.session():
          valid_input = [1.0, 2.0, 3.0, 4.0, 5.0]
          result = MyOperator(valid_input).eval()
          self.assertEqual(result, [1.0, 2.0, 3.0, 5.0, 8.0]
          invalid_input = [-1.0, 2.0, 7.0]
          with self.assertRaisesOpError("negative input not supported"):
            MyOperator(invalid_input).eval()
    ```

    Args:
      graph: Optional graph to use during the returned session.
      config: An optional config_pb2.ConfigProto to use to configure the
        session.
      use_gpu: If True, attempt to run as many ops as possible on GPU.
      force_gpu: If True, pin all ops to `/device:GPU:0`.

    Yields:
      A Session object that should be used as a context manager to surround
      the graph building and execution code in a test case.
    '''
    def cached_session(self, graph: Incomplete | None = None, config: Incomplete | None = None, use_gpu: bool = True, force_gpu: bool = False) -> Generator[Incomplete, None, None]:
        '''Returns a TensorFlow Session for use in executing tests.

    This method behaves differently than self.session(): for performance reasons
    `cached_session` will by default reuse the same session within the same
    test. The session returned by this function will only be closed at the end
    of the test (in the TearDown function).

    Use the `use_gpu` and `force_gpu` options to control where ops are run. If
    `force_gpu` is True, all ops are pinned to `/device:GPU:0`. Otherwise, if
    `use_gpu` is True, TensorFlow tries to run as many ops on the GPU as
    possible. If both `force_gpu and `use_gpu` are False, all ops are pinned to
    the CPU.

    Example:
    ```python
    class MyOperatorTest(test_util.TensorFlowTestCase):
      def testMyOperator(self):
        with self.cached_session() as sess:
          valid_input = [1.0, 2.0, 3.0, 4.0, 5.0]
          result = MyOperator(valid_input).eval()
          self.assertEqual(result, [1.0, 2.0, 3.0, 5.0, 8.0]
          invalid_input = [-1.0, 2.0, 7.0]
          with self.assertRaisesOpError("negative input not supported"):
            MyOperator(invalid_input).eval()
    ```

    Args:
      graph: Optional graph to use during the returned session.
      config: An optional config_pb2.ConfigProto to use to configure the
        session.
      use_gpu: If True, attempt to run as many ops as possible on GPU.
      force_gpu: If True, pin all ops to `/device:GPU:0`.

    Yields:
      A Session object that should be used as a context manager to surround
      the graph building and execution code in a test case.
    '''
    def test_session(self, graph: Incomplete | None = None, config: Incomplete | None = None, use_gpu: bool = True, force_gpu: bool = False) -> Generator[Incomplete, None, None]:
        """Use cached_session instead."""
    class _CheckedThread:
        """A wrapper class for Thread that asserts successful completion.

    This class should be created using the TensorFlowTestCase.checkedThread()
    method.
    """
        def __init__(self, testcase, target, args: Incomplete | None = None, kwargs: Incomplete | None = None) -> None:
            """Constructs a new instance of _CheckedThread.

      Args:
        testcase: The TensorFlowTestCase for which this thread is being created.
        target: A callable object representing the code to be executed in the
          thread.
        args: A tuple of positional arguments that will be passed to target.
        kwargs: A dictionary of keyword arguments that will be passed to target.
      """
        def start(self) -> None:
            """Starts the thread's activity.

      This must be called at most once per _CheckedThread object. It arranges
      for the object's target to be invoked in a separate thread of control.
      """
        def join(self) -> None:
            """Blocks until the thread terminates.

      Raises:
        self._testcase.failureException: If the thread terminates with due to
          an exception.
      """
        def is_alive(self):
            """Returns whether the thread is alive.

      This method returns True just before the run() method starts
      until just after the run() method terminates.

      Returns:
        True if the thread is alive, otherwise False.
      """
        def check_termination(self) -> None:
            '''Returns whether the checked thread was properly used and did terminate.

      Every checked thread should be "join"ed after starting, and before the
      test tears down. If it is not joined, it is possible the thread will hang
      and cause flaky failures in tests.

      Raises:
        self._testcase.failureException: If check_termination was called before
        thread was joined.

        RuntimeError: If the thread is not terminated. This means thread was not
        joined with the main thread.
      '''
    def checkedThread(self, target, args: Incomplete | None = None, kwargs: Incomplete | None = None):
        """Returns a Thread wrapper that asserts 'target' completes successfully.

    This method should be used to create all threads in test cases, as
    otherwise there is a risk that a thread will silently fail, and/or
    assertions made in the thread will not be respected.

    Args:
      target: A callable object to be executed in the thread.
      args: The argument tuple for the target invocation. Defaults to ().
      kwargs: A dictionary of keyword arguments for the target invocation.
        Defaults to {}.

    Returns:
      A wrapper for threading.Thread that supports start() and join() methods.
    """
    def assertNear(self, f1, f2, err, msg: Incomplete | None = None) -> None:
        """Asserts that two floats are near each other.

    Checks that |f1 - f2| < err and asserts a test failure
    if not.

    Args:
      f1: A float value.
      f2: A float value.
      err: A float value.
      msg: An optional string message to append to the failure message.
    """
    def assertArrayNear(self, farray1, farray2, err, msg: Incomplete | None = None) -> None:
        """Asserts that two float arrays are near each other.

    Checks that for all elements of farray1 and farray2
    |f1 - f2| < err.  Asserts a test failure if not.

    Args:
      farray1: a list of float values.
      farray2: a list of float values.
      err: a float value.
      msg: Optional message to report on failure.
    """
    def assertNDArrayNear(self, ndarray1, ndarray2, err, msg: Incomplete | None = None) -> None:
        """Asserts that two numpy arrays have near values.

    Args:
      ndarray1: a numpy ndarray.
      ndarray2: a numpy ndarray.
      err: a float. The maximum absolute difference allowed.
      msg: Optional message to report on failure.
    """
    def evaluate_if_both_tensors(self, a, b): ...
    def assertAllClose(self, a, b, rtol: float = 1e-06, atol: float = 1e-06, msg: Incomplete | None = None) -> None:
        """Asserts that two structures of numpy arrays or Tensors, have near values.

    `a` and `b` can be arbitrarily nested structures. A layer of a nested
    structure can be a `dict`, `namedtuple`, `tuple` or `list`.

    Note: the implementation follows
    [`numpy.allclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
    (and numpy.testing.assert_allclose). It checks whether two arrays are
    element-wise equal within a tolerance. The relative difference
    (`rtol * abs(b)`) and the absolute difference `atol` are added together
    to compare against the absolute difference between `a` and `b`.

    Args:
      a: The expected numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor), or any arbitrarily nested of
        structure of these.
      b: The actual numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor), or any arbitrarily nested of
        structure of these.
      rtol: relative tolerance.
      atol: absolute tolerance.
      msg: Optional message to report on failure.

    Raises:
      ValueError: if only one of `a[p]` and `b[p]` is a dict or
          `a[p]` and `b[p]` have different length, where `[p]` denotes a path
          to the nested structure, e.g. given `a = [(1, 1), {'d': (6, 7)}]` and
          `[p] = [1]['d']`, then `a[p] = (6, 7)`.
    """
    def assertAllCloseAccordingToType(self, a, b, rtol: float = 1e-06, atol: float = 1e-06, float_rtol: float = 1e-06, float_atol: float = 1e-06, half_rtol: float = 0.001, half_atol: float = 0.001, bfloat16_rtol: float = 0.01, bfloat16_atol: float = 0.01, msg: Incomplete | None = None) -> None:
        """Like assertAllClose, but also suitable for comparing fp16 arrays.

    In particular, the tolerance is reduced to 1e-3 if at least
    one of the arguments is of type float16.

    Args:
      a: the expected numpy ndarray or anything can be converted to one.
      b: the actual numpy ndarray or anything can be converted to one.
      rtol: relative tolerance.
      atol: absolute tolerance.
      float_rtol: relative tolerance for float32.
      float_atol: absolute tolerance for float32.
      half_rtol: relative tolerance for float16.
      half_atol: absolute tolerance for float16.
      bfloat16_rtol: relative tolerance for bfloat16.
      bfloat16_atol: absolute tolerance for bfloat16.
      msg: Optional message to report on failure.
    """
    def assertNotAllClose(self, a, b, rtol: float = 1e-06, atol: float = 1e-06, msg: Incomplete | None = None) -> None:
        """Assert that two numpy arrays, or Tensors, do not have near values.

    Args:
      a: The expected numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor), or any arbitrarily nested of
        structure of these.
      b: The actual numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor), or any arbitrarily nested of
        structure of these.
      rtol: relative tolerance.
      atol: absolute tolerance.
      msg: Optional message to report on failure.

    Raises:
      AssertionError: If `a` and `b` are unexpectedly close at all elements.
    """
    def assertAllEqual(self, a, b, msg: Incomplete | None = None):
        """Asserts that two numpy arrays or Tensors have the same values.

    Args:
      a: the expected numpy ndarray or anything can be converted to one.
      b: the actual numpy ndarray or anything can be converted to one.
      msg: Optional message to report on failure.
    """
    def assertNotAllEqual(self, a, b, msg: Incomplete | None = None) -> None:
        """Asserts that two numpy arrays or Tensors do not have the same values.

    Args:
      a: the expected numpy ndarray or anything can be converted to one.
      b: the actual numpy ndarray or anything can be converted to one.
      msg: Optional message to report on failure.
    """
    def assertAllGreater(self, a, comparison_target) -> None:
        """Assert element values are all greater than a target value.

    Args:
      a: The numpy `ndarray`, or anything that can be converted into a numpy
        `ndarray` (including Tensor).
      comparison_target: The target value of comparison.
    """
    def assertAllLess(self, a, comparison_target) -> None:
        """Assert element values are all less than a target value.

    Args:
      a: The numpy `ndarray`, or anything that can be converted into a numpy
        `ndarray` (including Tensor).
      comparison_target: The target value of comparison.
    """
    def assertAllGreaterEqual(self, a, comparison_target) -> None:
        """Assert element values are all greater than or equal to a target value.

    Args:
      a: The numpy `ndarray`, or anything that can be converted into a numpy
        `ndarray` (including Tensor).
      comparison_target: The target value of comparison.
    """
    def assertAllLessEqual(self, a, comparison_target) -> None:
        """Assert element values are all less than or equal to a target value.

    Args:
      a: The numpy `ndarray`, or anything that can be converted into a numpy
        `ndarray` (including Tensor).
      comparison_target: The target value of comparison.
    """
    def assertAllInRange(self, target, lower_bound, upper_bound, open_lower_bound: bool = False, open_upper_bound: bool = False) -> None:
        """Assert that elements in a Tensor are all in a given range.

    Args:
      target: The numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor).
      lower_bound: lower bound of the range
      upper_bound: upper bound of the range
      open_lower_bound: (`bool`) whether the lower bound is open (i.e., > rather
        than the default >=)
      open_upper_bound: (`bool`) whether the upper bound is open (i.e., < rather
        than the default <=)

    Raises:
      AssertionError:
        if the value tensor does not have an ordered numeric type (float* or
          int*), or
        if there are nan values, or
        if any of the elements do not fall in the specified range.
    """
    def assertAllInSet(self, target, expected_set) -> None:
        """Assert that elements of a Tensor are all in a given closed set.

    Args:
      target: The numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor).
      expected_set: (`list`, `tuple` or `set`) The closed set that the elements
        of the value of `target` are expected to fall into.

    Raises:
      AssertionError:
        if any of the elements do not fall into `expected_set`.
    """
    def assertDTypeEqual(self, target, expected_dtype) -> None:
        """Assert ndarray data type is equal to expected.

    Args:
      target: The numpy `ndarray`, or anything that can be converted into a
        numpy `ndarray` (including Tensor).
      expected_dtype: Expected data type.
    """
    def assertRaisesWithPredicateMatch(self, exception_type, expected_err_re_or_predicate) -> Generator[None, None, Incomplete]:
        """Returns a context manager to enclose code expected to raise an exception.

    If the exception is an OpError, the op stack is also included in the message
    predicate search.

    Args:
      exception_type: The expected type of exception that should be raised.
      expected_err_re_or_predicate: If this is callable, it should be a function
        of one argument that inspects the passed-in exception and returns True
        (success) or False (please fail the test). Otherwise, the error message
        is expected to match this regular expression partially.

    Returns:
      A context manager to surround code that is expected to raise an
      exception.
    """
    def assertRaisesOpError(self, expected_err_re_or_predicate): ...
    def assertRaisesIncompatibleShapesError(self, exception_type=...): ...
    def assertShapeEqual(self, input_a, input_b, msg: Incomplete | None = None) -> None:
        """Asserts that two Numpy or TensorFlow objects have the same shape.

    For Tensors, this compares statically known shapes at compile time, not
    dynamic shapes at runtime.

    Args:
      input_a: A Numpy ndarray, Numpy scalar, or a Tensor.
      input_b: A Numpy ndarray, Numpy scalar, or a Tensor.
      msg: Optional message to report on failure.

    Raises:
      TypeError: If the arguments have the wrong type.
    """
    def assertDeviceEqual(self, device1, device2, msg: Incomplete | None = None) -> None:
        """Asserts that the two given devices are the same.

    Args:
      device1: A string device name or TensorFlow `DeviceSpec` object.
      device2: A string device name or TensorFlow `DeviceSpec` object.
      msg: Optional message to report on failure.
    """
    def assertDictEqual(self, a, b, msg: Incomplete | None = None) -> None:
        """Assert that two given dictionary of tensors are the same.

    Args:
      a: Expected dictionary with numpy ndarray or anything else that can be
        converted to one as values.
      b: Actual dictionary with numpy ndarray or anything else that can be
        converted to one as values.
      msg: Optional message to report on failure.
    """
    assertRaisesRegexp: Incomplete
    assertItemsEqual: Incomplete

ASSIGNED_PORTS: Incomplete
lock: Incomplete

def pick_unused_port():
    """Returns an unused and unassigned local port."""
def create_local_cluster(num_workers, num_ps, protocol: str = 'grpc', worker_config: Incomplete | None = None, ps_config: Incomplete | None = None):
    '''Create and start local servers and return the associated `Server` objects.

  "PS" stands for "parameter server": a task responsible for storing and
  updating the model\'s parameters. Other tasks send updates to these parameters
  as they work on optimizing the parameters. This particular division of labor
  between tasks is not required, but is common for distributed training.

  Read more at https://www.tensorflow.org/guide/extend/architecture

  ![components](https://www.tensorflow.org/images/diag1.svg "components")


  Figure illustrates the interaction of these components.
  "/job:worker/task:0" and "/job:ps/task:0" are both tasks with worker services.


  Example:
  ```python
  workers, _ = tf.test.create_local_cluster(num_workers=2, num_ps=2)

  worker_sessions = [tf.compat.v1.Session(w.target) for w in workers]

  with tf.device("/job:ps/task:0"):
    ...
  with tf.device("/job:ps/task:1"):
    ...
  with tf.device("/job:worker/task:0"):
    ...
  with tf.device("/job:worker/task:1"):
    ...

  worker_sessions[0].run(...)
  ```

  Args:
    num_workers: Number of worker servers to start.
    num_ps: Number of PS servers to start.
    protocol: Communication protocol. Allowed values are documented in the
      documentation of `tf.distribute.Server`.
    worker_config: (optional) `tf.ConfigProto` to initialize workers. Can be
      used to instantiate multiple devices etc.
    ps_config: (optional) `tf.ConfigProto` to initialize PS servers.

  Returns:
    A tuple `(worker_servers, ps_servers)`.  `worker_servers` is a list
    of `num_workers` objects of type `tf.distribute.Server` (all running
    locally);
    and `ps_servers` is a list of `num_ps` objects of similar type.

  Raises:
    ImportError: if portpicker module was not found at load time
  '''
def get_node_def_from_graph(node_name, graph_def):
    """Returns the `NodeDef` instance for given node name in the graph def.

  This method explores only the NodeDefs in `graph_def.node`.

  Args:
    node_name: Name of the NodeDef to search for.
    graph_def: An instance of `GraphDef` proto.

  Returns:
    the `NodeDef` instance whose name field matches the given node_name or None.
  """
def set_producer_version(graph, producer_version) -> None:
    """Sets graph.graph_def_versions.producer to `producer_version`."""

class AbstractGradientTape:
    """Abstract GradientTape context manager that has multiple implementations.

  This is useful to test both tf.GradientTape() and tf.gradients() without
  duplicating tests.
  """
    def __init__(self, use_tape, persistent: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def run_functions_eagerly(run_eagerly) -> Generator[None, None, None]:
    """Runs functions eagerly if `run_eagerly` is true.

  WARNING: Setting `run_eagerly` to True in tests running in V1 graph mode
  *WILL NOT* make the tf.function to run eagerly because eager is disabled by
  default in V1. Instead, tf.function will run as a traced graph function.

  Ensures that the state (for running functions eagerly) is back to the initial
  `def_function.RUN_FUNCTIONS_EAGERLY` state.

  Args:
    run_eagerly: Boolean determining whether to run the function eagerly or not.

  Raises:
    ValueError if `run_eagerly` is not a boolean.

  Yields:
    Nothing.
  """

class TestDelta:
    """A utility class to track increments to test counters."""
    name: Incomplete
    label: Incomplete
    def __init__(self, name, label) -> None: ...
    last_value: Incomplete
    def Reset(self) -> None: ...
    def Get(self): ...

def sync_devices() -> None:
    """Synchronizes all devices.

  By default, GPUs run asynchronously. This means that when you run an op on the
  GPU, like `tf.linalg.matmul`, the op may still be running on the GPU when the
  function returns. Non-GPU devices can also be made to run asynchronously by
  calling `tf.config.experimental.set_synchronous_execution(False)`. Calling
  `sync_devices()` blocks until pending ops have finished executing. This is
  primarily useful for measuring performance during a benchmark.

  For example, here is how you can measure how long `tf.linalg.matmul` runs:

  >>> import time
  >>> x = tf.random.normal((4096, 4096))
  >>> tf.linalg.matmul(x, x)  # Warmup.
  >>> tf.test.experimental.sync_devices()  # Block until warmup has completed.
  >>>
  >>> start = time.time()
  >>> y = tf.linalg.matmul(x, x)
  >>> tf.test.experimental.sync_devices()  # Block until matmul has completed.
  >>> end = time.time()
  >>> print(f'Time taken: {end - start}')

  If the call to `sync_devices()` was omitted, the time printed could be too
  small. This is because the op could still be running asynchronously when
  the line `end = time.time()` is executed.

  Raises:
    RuntimeError: If run outside Eager mode. This must be called in Eager mode,
      outside any `tf.function`s.
  """
