from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def verify_tensor_all_finite(t: Incomplete | None = None, msg: Incomplete | None = None, name: Incomplete | None = None, x: Incomplete | None = None, message: Incomplete | None = None):
    """Assert that the tensor does not contain any NaN's or Inf's.

  Args:
    t: Tensor to check.
    msg: Message to log on failure.
    name: A name for this operation (optional).
    x: Alias for t.
    message: Alias for msg.

  Returns:
    Same tensor as `t`.
  """
def verify_tensor_all_finite_v2(x, message, name: Incomplete | None = None):
    """Assert that the tensor does not contain any NaN's or Inf's.

  >>> @tf.function
  ... def f(x):
  ...   x = tf.debugging.assert_all_finite(x, 'Input x must be all finite')
  ...   return x + 1

  >>> f(tf.constant([np.inf, 1, 2]))
  Traceback (most recent call last):
     ...
  InvalidArgumentError: ...

  Args:
    x: Tensor to check.
    message: Message to log on failure.
    name: A name for this operation (optional).

  Returns:
    Same tensor as `x`.
  """
def add_check_numerics_ops():
    """Connect a `tf.debugging.check_numerics` to every floating point tensor.

  `check_numerics` operations themselves are added for each `half`, `float`,
  or `double` tensor in the current default graph. For all ops in the graph, the
  `check_numerics` op for all of its (`half`, `float`, or `double`) inputs
  is guaranteed to run before the `check_numerics` op on any of its outputs.

  Note: This API is not compatible with the use of `tf.cond` or
  `tf.while_loop`, and will raise a `ValueError` if you attempt to call it
  in such a graph.

  Returns:
    A `group` op depending on all `check_numerics` ops added.

  Raises:
    ValueError: If the graph contains any numeric operations in a control flow
      structure.
    RuntimeError: If called with eager execution enabled.

  @compatibility(eager)
  Not compatible with eager execution. To check for `Inf`s and `NaN`s under
  eager execution, call `tf.debugging.enable_check_numerics()` once before
  executing the checked operations.
  @end_compatibility
  """
