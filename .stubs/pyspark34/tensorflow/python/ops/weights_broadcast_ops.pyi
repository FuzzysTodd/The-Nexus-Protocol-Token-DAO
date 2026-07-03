from tensorflow.python.framework import ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, sets as sets
from tensorflow.python.util.tf_export import tf_export as tf_export

def assert_broadcastable(weights, values):
    """Asserts `weights` can be broadcast to `values`.

  In `tf.losses` and `tf.metrics`, we support limited weight broadcasting. We
  let weights be either scalar, or the same rank as the target values, with each
  dimension either 1, or the same as the corresponding values dimension.

  Args:
    weights: `Tensor` of weights.
    values: `Tensor` of values to which weights are applied.

  Returns:
    `Operation` raising `InvalidArgumentError` if `weights` has incorrect shape.
    `no_op` if static checks determine `weights` has correct shape.

  Raises:
    ValueError:  If static checks determine `weights` has incorrect shape.
  """
def broadcast_weights(weights, values):
    """Broadcast `weights` to the same shape as `values`.

  This returns a version of `weights` following the same broadcast rules as
  `mul(weights, values)`, but limited to the weights shapes allowed by
  `assert_broadcastable`. When computing a weighted average, use this function
  to broadcast `weights` before summing them; e.g.,
  `reduce_sum(w * v) / reduce_sum(_broadcast_weights(w, v))`.

  Args:
    weights: `Tensor` whose shape is broadcastable to `values` according to the
      rules of `assert_broadcastable`.
    values: `Tensor` of any shape.

  Returns:
    `weights` broadcast to `values` shape according to the rules of
      `assert_broadcastable`.
  """
