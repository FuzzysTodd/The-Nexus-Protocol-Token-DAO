import typing
from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_gather_ops as ragged_gather_ops, ragged_tensor as ragged_tensor, ragged_util as ragged_util
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def concat(values: typing.List[ragged_tensor.RaggedOrDense], axis, name: Incomplete | None = None):
    """Concatenates potentially ragged tensors along one dimension.

  Given a list of tensors with the same rank `K` (`K >= axis`), returns a
  rank-`K` `RaggedTensor` `result` such that `result[i0...iaxis]` is the
  concatenation of `[rt[i0...iaxis] for rt in values]`.

  Args:
    values: A list of potentially ragged tensors.  May not be empty. All
      `values` must have the same rank and the same dtype; but unlike
      `tf.concat`, they can have arbitrary shapes.
    axis: A python integer, indicating the dimension along which to concatenate.
      (Note: Unlike `tf.concat`, the `axis` parameter must be statically known.)
        Negative values are supported only if the rank of at least one
        `values` value is statically known.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` with rank `K`.
    `result.ragged_rank=max(axis, max(rt.ragged_rank for rt in values]))`.

  Raises:
    ValueError: If `values` is empty, if `axis` is out of bounds or if
      the input tensors have different ranks.

  #### Example:

  >>> t1 = tf.ragged.constant([[1, 2], [3, 4, 5]])
  >>> t2 = tf.ragged.constant([[6], [7, 8, 9]])
  >>> tf.concat([t1, t2], axis=0)
  <tf.RaggedTensor [[1, 2], [3, 4, 5], [6], [7, 8, 9]]>
  >>> tf.concat([t1, t2], axis=1)
  <tf.RaggedTensor [[1, 2, 6], [3, 4, 5, 7, 8, 9]]>
  """
def stack(values: typing.List[ragged_tensor.RaggedOrDense], axis: int = 0, name: Incomplete | None = None):
    """Stacks a list of rank-`R` tensors into one rank-`(R+1)` `RaggedTensor`.

  Given a list of tensors or ragged tensors with the same rank `R`
  (`R >= axis`), returns a rank-`R+1` `RaggedTensor` `result` such that
  `result[i0...iaxis]` is `[value[i0...iaxis] for value in values]`.

  #### Examples:

  >>> # Stacking two ragged tensors.
  >>> t1 = tf.ragged.constant([[1, 2], [3, 4, 5]])
  >>> t2 = tf.ragged.constant([[6], [7, 8, 9]])
  >>> tf.ragged.stack([t1, t2], axis=0)
  <tf.RaggedTensor [[[1, 2], [3, 4, 5]], [[6], [7, 8, 9]]]>
  >>> tf.ragged.stack([t1, t2], axis=1)
  <tf.RaggedTensor [[[1, 2], [6]], [[3, 4, 5], [7, 8, 9]]]>

  >>> # Stacking two dense tensors with different sizes.
  >>> t3 = tf.constant([[1, 2, 3], [4, 5, 6]])
  >>> t4 = tf.constant([[5], [6], [7]])
  >>> tf.ragged.stack([t3, t4], axis=0)
  <tf.RaggedTensor [[[1, 2, 3], [4, 5, 6]], [[5], [6], [7]]]>

  Args:
    values: A list of `tf.Tensor` or `tf.RaggedTensor`.  May not be empty. All
      `values` must have the same rank and the same dtype; but unlike
      `tf.stack`, they can have arbitrary dimension sizes.
    axis: A python integer, indicating the dimension along which to stack.
      (Note: Unlike `tf.stack`, the `axis` parameter must be statically known.)
      Negative values are supported only if the rank of at least one
      `values` value is statically known.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` with rank `R+1` (if `R>0`).
    If `R==0`, then the result will be returned as a 1D `Tensor`, since
    `RaggedTensor` can only be used when `rank>1`.
    `result.ragged_rank=1+max(axis, max(rt.ragged_rank for rt in values]))`.

  Raises:
    ValueError: If `values` is empty, if `axis` is out of bounds or if
      the input tensors have different ranks.
  """
