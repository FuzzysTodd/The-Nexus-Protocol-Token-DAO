from _typeshed import Incomplete
from tensorflow.lite.python import convert as convert, lite as lite
from tensorflow.lite.python.metrics import converter_error_data_pb2 as converter_error_data_pb2

class CompatibilityError(Exception):
    """Raised when an error occurs with TFLite compatibility."""

class _Compatible:
    """A decorator class to check TFLite compatibility created by `lite.experimental.authoring.compatible`."""
    def __init__(self, target, converter_target_spec: Incomplete | None = None, converter_allow_custom_ops: Incomplete | None = None, raise_exception: bool = False) -> None:
        """Initialize the decorator object.

    Here is the description of the object variables.
    - _func     : decorated function.
    - _obj_func : for class object, we need to use this object to provide `self`
                  instance as 1 first argument.
    - _verified : whether the compatibility is checked or not.

    Args:
      target: decorated function.
      converter_target_spec : target_spec of TFLite converter parameter.
      converter_allow_custom_ops : allow_custom_ops of TFLite converter
          parameter.
      raise_exception : to raise an exception on compatibility issues.
          User need to use get_compatibility_log() to check details.
    """
    def __get__(self, instance, cls):
        """A Python descriptor interface."""
    def __call__(self, *args, **kwargs):
        """Calls decorated function object.

    Also verifies if the function is compatible with TFLite.

    Returns:
      A execution result of the decorated function.
    """
    def get_concrete_function(self, *args, **kwargs):
        """Returns a concrete function of the decorated function."""
    def get_compatibility_log(self):
        """Returns list of compatibility log messages.

    WARNING: This method should only be used for unit tests.

    Returns:
      The list of log messages by the recent compatibility check.
    Raises:
      RuntimeError: when the compatibility was NOT checked.
    """

def compatible(target: Incomplete | None = None, converter_target_spec: Incomplete | None = None, **kwargs):
    '''Wraps `tf.function` into a callable function with TFLite compatibility checking.

  Example:

  ```python
  @tf.lite.experimental.authoring.compatible
  @tf.function(input_signature=[
      tf.TensorSpec(shape=[None], dtype=tf.float32)
  ])
  def f(x):
      return tf.cosh(x)

  result = f(tf.constant([0.0]))
  # COMPATIBILITY WARNING: op \'tf.Cosh\' require(s) "Select TF Ops" for model
  # conversion for TensorFlow Lite.
  # Op: tf.Cosh
  #   - tensorflow/python/framework/op_def_library.py:748
  #   - tensorflow/python/ops/gen_math_ops.py:2458
  #   - <stdin>:6
  ```

  WARNING: Experimental interface, subject to change.

  Args:
    target: A `tf.function` to decorate.
    converter_target_spec : target_spec of TFLite converter parameter.
    **kwargs: The keyword arguments of the decorator class _Compatible.

  Returns:
     A callable object of `tf.lite.experimental.authoring._Compatible`.
  '''
