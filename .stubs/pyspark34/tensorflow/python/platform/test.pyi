from _typeshed import Incomplete
from tensorflow.python.framework.test_util import assert_equal_graph_def as assert_equal_graph_def, create_local_cluster as create_local_cluster, gpu_device_name as gpu_device_name, is_gpu_available as is_gpu_available
from tensorflow.python.ops.gradient_checker import compute_gradient as compute_gradient, compute_gradient_error as compute_gradient_error
from tensorflow.python.platform import googletest as _googletest
from tensorflow.python.util.tf_export import tf_export as tf_export

Benchmark: Incomplete
StubOutForTesting = _googletest.StubOutForTesting

def main(argv: Incomplete | None = None):
    """Runs all unit tests."""
def get_temp_dir():
    """Returns a temporary directory for use during tests.

  There is no need to delete the directory after the test.

  @compatibility(TF2)
  This function is removed in TF2. Please use `TestCase.get_temp_dir` instead
  in a test case.
  Outside of a unit test, obtain a temporary directory through Python's
  `tempfile` module.
  @end_compatibility

  Returns:
    The temporary directory.
  """
def test_src_dir_path(relative_path):
    '''Creates an absolute test srcdir path given a relative path.

  Args:
    relative_path: a path relative to tensorflow root.
      e.g. "core/platform".

  Returns:
    An absolute path to the linked in runfiles.
  '''
def is_built_with_cuda():
    '''Returns whether TensorFlow was built with CUDA (GPU) support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with CUDA (GPU).

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_gpu(self):
  ...     if not tf.test.is_built_with_cuda():
  ...       self.skipTest("test is only applicable on GPU")
  ...
  ...     with tf.device("GPU:0"):
  ...       self.assertEqual(tf.math.add(1.0, 2.0), 3.0)

  TensorFlow official binary is built with CUDA.
  '''
def is_built_with_rocm():
    '''Returns whether TensorFlow was built with ROCm (GPU) support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with ROCm (GPU).

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_gpu(self):
  ...     if not tf.test.is_built_with_rocm():
  ...       self.skipTest("test is only applicable on GPU")
  ...
  ...     with tf.device("GPU:0"):
  ...       self.assertEqual(tf.math.add(1.0, 2.0), 3.0)

  TensorFlow official binary is NOT built with ROCm.
  '''
def disable_with_predicate(pred, skip_message):
    """Disables the test if pred is true."""
def is_built_with_gpu_support():
    '''Returns whether TensorFlow was built with GPU (CUDA or ROCm) support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with GPU.

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_gpu(self):
  ...     if not tf.test.is_built_with_gpu_support():
  ...       self.skipTest("test is only applicable on GPU")
  ...
  ...     with tf.device("GPU:0"):
  ...       self.assertEqual(tf.math.add(1.0, 2.0), 3.0)

  TensorFlow official binary is built with CUDA GPU support.
  '''
def is_built_with_xla():
    '''Returns whether TensorFlow was built with XLA support.

  This method should only be used in tests written with `tf.test.TestCase`. A
  typical usage is to skip tests that should only run with XLA.

  >>> class MyTest(tf.test.TestCase):
  ...
  ...   def test_add_on_xla(self):
  ...     if not tf.test.is_built_with_xla():
  ...       self.skipTest("test is only applicable on XLA")

  ...     @tf.function(jit_compile=True)
  ...     def add(x, y):
  ...       return tf.math.add(x, y)
  ...
  ...     self.assertEqual(add(tf.ones(()), tf.ones(())), 2.0)

  TensorFlow official binary is built with XLA.
  '''
