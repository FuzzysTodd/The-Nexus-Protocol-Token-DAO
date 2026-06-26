from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_array_ops as ragged_array_ops, ragged_dispatch as ragged_dispatch, ragged_operators as ragged_operators, ragged_tensor as ragged_tensor, ragged_tensor_shape as ragged_tensor_shape, ragged_where_op as ragged_where_op

def batch_gather_with_default(params, indices, default_value: str = '', name: Incomplete | None = None):
    """Same as `batch_gather` but inserts `default_value` for invalid indices.

  This operation is similar to `batch_gather` except that it will substitute
  the value for invalid indices with `default_value` as the contents.
  See `batch_gather` for more details.


  Args:
    params: A potentially ragged tensor with shape `[B1...BN, P1...PM]` (`N>=0`,
      `M>0`).
    indices: A potentially ragged tensor with shape `[B1...BN, I]` (`N>=0`).
    default_value: A value to be inserted in places where `indices` are out of
      bounds. Must be the same dtype as params and either a scalar or rank 1.
    name: A name for the operation (optional).

  Returns:
    A potentially ragged tensor with shape `[B1...BN, I, P2...PM]`.
    `result.ragged_rank = max(indices.ragged_rank, params.ragged_rank)`.

  #### Example:

  >>> params = tf.ragged.constant([['a', 'b', 'c'], ['d'], [], ['e']])
  >>> indices = tf.ragged.constant([[1, 2, -1], [], [], [0, 10]])
  >>> batch_gather_with_default(params, indices, 'FOO')
  <tf.RaggedTensor [[b'b', b'c', b'FOO'], [], [], [b'e', b'FOO']]>

  """
