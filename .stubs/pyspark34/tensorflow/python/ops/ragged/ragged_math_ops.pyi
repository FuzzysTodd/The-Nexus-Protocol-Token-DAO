import typing
from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, errors as errors, ops as ops, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, gen_ragged_math_ops as gen_ragged_math_ops, map_fn as map_fn, math_ops as math_ops, nn_ops as nn_ops
from tensorflow.python.ops.ragged import ragged_functional_ops as ragged_functional_ops, ragged_tensor as ragged_tensor, segment_id_ops as segment_id_ops
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def range(starts, limits: Incomplete | None = None, deltas: int = 1, dtype: Incomplete | None = None, name: Incomplete | None = None, row_splits_dtype=...):
    """Returns a `RaggedTensor` containing the specified sequences of numbers.

  Each row of the returned `RaggedTensor` contains a single sequence:

  ```python
  ragged.range(starts, limits, deltas)[i] ==
      tf.range(starts[i], limits[i], deltas[i])
  ```

  If `start[i] < limits[i] and deltas[i] > 0`, then `output[i]` will be an
  empty list.  Similarly, if `start[i] > limits[i] and deltas[i] < 0`, then
  `output[i]` will be an empty list.  This behavior is consistent with the
  Python `range` function, but differs from the `tf.range` op, which returns
  an error for these cases.

  Examples:

  >>> tf.ragged.range([3, 5, 2]).to_list()
  [[0, 1, 2], [0, 1, 2, 3, 4], [0, 1]]
  >>> tf.ragged.range([0, 5, 8], [3, 3, 12]).to_list()
  [[0, 1, 2], [], [8, 9, 10, 11]]
  >>> tf.ragged.range([0, 5, 8], [3, 3, 12], 2).to_list()
  [[0, 2], [], [8, 10]]

  The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors.
  The vector inputs must all have the same size.  Scalar inputs are broadcast
  to match the size of the vector inputs.

  Args:
    starts: Vector or scalar `Tensor`.  Specifies the first entry for each range
      if `limits` is not `None`; otherwise, specifies the range limits, and the
      first entries default to `0`.
    limits: Vector or scalar `Tensor`.  Specifies the exclusive upper limits for
      each range.
    deltas: Vector or scalar `Tensor`.  Specifies the increment for each range.
      Defaults to `1`.
    dtype: The type of the elements of the resulting tensor.  If not specified,
      then a value is chosen based on the other args.
    name: A name for the operation.
    row_splits_dtype: `dtype` for the returned `RaggedTensor`'s `row_splits`
      tensor.  One of `tf.int32` or `tf.int64`.

  Returns:
    A `RaggedTensor` of type `dtype` with `ragged_rank=1`.
  """
def segment_sum(data: ragged_tensor.RaggedOrDense, segment_ids: ragged_tensor.RaggedOrDense, num_segments, name: Incomplete | None = None): ...
def segment_prod(data: ragged_tensor.RaggedOrDense, segment_ids: ragged_tensor.RaggedOrDense, num_segments, name: Incomplete | None = None): ...
def segment_min(data: ragged_tensor.RaggedOrDense, segment_ids: ragged_tensor.RaggedOrDense, num_segments, name: Incomplete | None = None): ...
def segment_max(data: ragged_tensor.RaggedOrDense, segment_ids: ragged_tensor.RaggedOrDense, num_segments, name: Incomplete | None = None): ...
def segment_mean(data: ragged_tensor.RaggedOrDense, segment_ids: ragged_tensor.RaggedOrDense, num_segments, name: Incomplete | None = None):
    """For docs, see: _RAGGED_SEGMENT_DOCSTRING."""
def segment_sqrt_n(data: ragged_tensor.RaggedOrDense, segment_ids: ragged_tensor.RaggedOrDense, num_segments, name: Incomplete | None = None):
    """For docs, see: _RAGGED_SEGMENT_DOCSTRING."""
def ragged_reduce_aggregate(reduce_op, unsorted_segment_op, rt_input, axis, keepdims, separator: Incomplete | None = None, name: Incomplete | None = None):
    """Aggregates across axes of a RaggedTensor using the given `Tensor` ops.

  Reduces `rt_input` along the dimensions given in `axis`.  The rank of the
  tensor is reduced by 1 for each entry in `axis`.  If `axis` is not specified,
  then all dimensions are reduced, and a scalar value is returned.

  This op assumes that `reduce_op` and `unsorted_segment_op` are associative;
  if not, then reducing multiple axes will return incorrect results.  (In
  particular, reducing multiple axes is currently implemented by reducing the
  axes one at a time.)

  Args:
    reduce_op: The tensorflow `op` that should be used to reduce values in
      uniform dimensions.  Must have the same signature and basic behavior as
      `reduce_sum`, `reduce_max`, etc.
    unsorted_segment_op: The tensorflow `op` that should be used to combine
      values in ragged dimensions.  Must have the same signature and basic
      behavior as `unsorted_segment_sum`, `unsorted_segment_max`, etc.
    rt_input: A `Tensor` or `RaggedTensor` containing the values to be reduced.
    axis: The axis or axes to reduce.  May be `None` (to reduce all axes), an
      `int` (to reduce a single axis), a `list` or `tuple` of `int` (to reduce a
      given set of axes), or a `Tensor` with a constant value.  Must be in the
      range `[0, rt_input.rank)`.
    keepdims: If true, retains reduced dimensions with length 1.
    separator: An optional string. Defaults to None. The separator to use when
      joining. The separator must not be set for non-string data types. (i.e. if
      separator is not None then it uses string ops)
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` containing the reduced values.  The returned tensor
    has the same dtype as `data`, and its shape is given by removing the
    dimensions specified in `axis` from `rt_input.shape`.  The `ragged_rank`
    of the returned tensor is given by substracting any ragged dimensions
    specified in `axis` from `rt_input.ragged_rank`.
  Raises:
    ValueError: If `axis` contains a `Tensor` whose value is not constant.
  """
def reduce_sum(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_prod(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_min(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_max(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_mean(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_variance(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_std(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: bool = False, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_all(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def reduce_any(input_tensor: ragged_tensor.Ragged, axis: Incomplete | None = None, keepdims: Incomplete | None = None, name: Incomplete | None = None):
    """For docs, see: _RAGGED_REDUCE_DOCSTRING."""
def matmul(a: ragged_tensor.RaggedOrDense, b: ragged_tensor.RaggedOrDense, transpose_a: bool = False, transpose_b: bool = False, adjoint_a: bool = False, adjoint_b: bool = False, a_is_sparse: bool = False, b_is_sparse: bool = False, output_type: Incomplete | None = None, name: Incomplete | None = None):
    """Multiplies matrix `a` by matrix `b`.

  If all transpose or adjoint attributes are `False` then:

  ```
  output[..., i, j] = sum_k (a[..., i, k] * b[..., k, j]), for all indices i, j.
  ```

  The inputs `a` and `b` must have `rank >= 2`, where the outermost `rank - 2`
  dimensions are batch dimensions.  The inputs must have the same dtype.  See
  `tf.matmul` for more information.

  Args:
    a: `tf.Tensor` or `RaggedTensor` with `rank > 1`.
    b: `tf.Tensor` or `RaggedTensor` with same type and rank as `a`.
    transpose_a: If `True`, `a` is transposed before multiplication.
    transpose_b: If `True`, `b` is transposed before multiplication.
    adjoint_a: If `True`, `a` is conjugated & transposed before multiplication.
    adjoint_b: If `True`, `b` is conjugated & transposed before multiplication.
    a_is_sparse: If `True`, optimize assuming `a` is mostly zero.
    b_is_sparse: If `True`, optimize assuming `b` is mostly zero.
    output_type: The output datatype (optional).
    name: Name for the operation (optional).

  Returns:
    A `Tensor` or `RaggedTensor` with the same rank and shape as `a`, where
    each inner-most matrix is the product of the corresponding matrices in `a`
    and `b`.
  """
def softmax(logits: ragged_tensor.Ragged, axis: Incomplete | None = None, name: Incomplete | None = None):
    """Computes softmax activations.

  Used for multi-class predictions. The sum of all outputs generated by softmax
  is 1.

  This function performs the equivalent of

      softmax = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis)

  Example usage:

  >>> softmax = tf.nn.softmax([-1, 0., 1.])
  >>> softmax
  <tf.Tensor: shape=(3,), dtype=float32,
  numpy=array([0.09003057, 0.24472848, 0.66524094], dtype=float32)>
  >>> sum(softmax)
  <tf.Tensor: shape=(), dtype=float32, numpy=1.0>

  Args:
    logits: A non-empty `Tensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    axis: The dimension softmax would be performed on. The default is -1 which
      indicates the last dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type and shape as `logits`.

  Raises:
    InvalidArgumentError: if `logits` is empty or `axis` is beyond the last
      dimension of `logits`.
  """
def add_n(inputs: typing.List[ragged_tensor.RaggedOrDense], name: Incomplete | None = None):
    """RaggedTensor implementation for tf.math.add_n."""
def dropout_v1(x: ragged_tensor.Ragged, keep_prob: Incomplete | None = None, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None, rate: Incomplete | None = None):
    """Ragged dispatch target for tf.nn.dropout."""
def dropout_v2(x: ragged_tensor.Ragged, rate, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Ragged dispatch target for tf.nn.dropout."""
def stateless_dropout(x: ragged_tensor.Ragged, rate, seed, rng_alg: Incomplete | None = None, noise_shape: Incomplete | None = None, name: Incomplete | None = None):
    """Ragged dispatch target for tf.nn.experimental.stateless_dropout."""
def tensor_equals(self, other: ragged_tensor.RaggedOrDense):
    """Ragged version of the operation invoked by `Tensor.__eq__`."""
def tensor_not_equals(self, other: ragged_tensor.RaggedOrDense):
    """Ragged version of the operation invoked by `Tensor.__ne__`."""
def ragged_cumsum(x: ragged_tensor.Ragged, axis: int = 0, exclusive: bool = False, reverse: bool = False, name: typing.Optional[str] = None):
    """Calculate math_ops.cumsum for a RaggedTensor.

  Given a ragged tensor `x`, the `result` is a ragged tensor with the same
  shape. One can calculate the value of `result[i_1...i_k]` as follows:
  ```
  dense_result=tf.math.cumsum(rt.to_tensor(), axis=axis, exclusive=exclusive,
                              reverse=reverse)
  result[i_1...i_k]=dense_result[i_1...i_k]
  ```

  Args:
    x: the original ragged tensor to sum.
    axis: the axis along which to sum, can range -rank<=axis<rank.
    exclusive: is the sum exclusive or inclusive? If True, then result[0]=0.
        If False, then result[0]=x[0].
    reverse: If True, sum from back to front.
    name: the name of the op.
  Returns:
    the cumulative sum.
  """
