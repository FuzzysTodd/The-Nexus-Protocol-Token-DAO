from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, data_flow_ops as data_flow_ops, gen_ragged_array_ops as gen_ragged_array_ops, math_ops as math_ops, sort_ops as sort_ops
from tensorflow.python.ops.ragged import dynamic_ragged_shape as dynamic_ragged_shape, ragged_functional_ops as ragged_functional_ops, ragged_math_ops as ragged_math_ops, ragged_tensor as ragged_tensor, ragged_util as ragged_util, segment_id_ops as segment_id_ops
from tensorflow.python.types import core as core_types
from tensorflow.python.util import dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Optional, Union

def boolean_mask(data, mask, name: Incomplete | None = None):
    """Applies a boolean mask to `data` without flattening the mask dimensions.

  Returns a potentially ragged tensor that is formed by retaining the elements
  in `data` where the corresponding value in `mask` is `True`.

  * `output[a1...aA, i, b1...bB] = data[a1...aA, j, b1...bB]`

     Where `j` is the `i`th `True` entry of `mask[a1...aA]`.

  Note that `output` preserves the mask dimensions `a1...aA`; this differs
  from `tf.boolean_mask`, which flattens those dimensions.

  Args:
    data: A potentially ragged tensor.
    mask: A potentially ragged boolean tensor.  `mask`'s shape must be a prefix
      of `data`'s shape.  `rank(mask)` must be known statically.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A potentially ragged tensor that is formed by retaining the elements in
    `data` where the corresponding value in `mask` is `True`.

    * `rank(output) = rank(data)`.
    * `output.ragged_rank = max(data.ragged_rank, rank(mask) - 1)`.

  Raises:
    ValueError: if `rank(mask)` is not known statically; or if `mask.shape` is
      not a prefix of `data.shape`.

  #### Examples:

  >>> # Aliases for True & False so data and mask line up.
  >>> T, F = (True, False)

  >>> tf.ragged.boolean_mask(  # Mask a 2D Tensor.
  ...     data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
  ...     mask=[[T, F, T], [F, F, F], [T, F, F]]).to_list()
  [[1, 3], [], [7]]

  >>> tf.ragged.boolean_mask(  # Mask a 2D RaggedTensor.
  ...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
  ...     tf.ragged.constant([[F, F, T], [F], [T, T]])).to_list()
  [[3], [], [5, 6]]

  >>> tf.ragged.boolean_mask(  # Mask rows of a 2D RaggedTensor.
  ...     tf.ragged.constant([[1, 2, 3], [4], [5, 6]]),
  ...     tf.ragged.constant([True, False, True])).to_list()
  [[1, 2, 3], [5, 6]]
  """
def tile(input: ragged_tensor.Ragged, multiples, name: Incomplete | None = None):
    """Constructs a `RaggedTensor` by tiling a given `RaggedTensor`.

  The values of `input` are replicated `multiples[i]` times along the
  `i`th dimension (for each dimension `i`).  For every dimension `axis` in
  `input`, the length of each output element in that dimension is the
  length of corresponding input element multiplied by `multiples[axis]`.

  Args:
    input: A `RaggedTensor`.
    multiples: A 1-D integer `Tensor`.  Length must be the same as the number of
      dimensions in `input`.
    name: A name for the operation (optional).

  Returns:
    A `RaggedTensor` with the same type, rank, and ragged_rank as `input`.

  #### Example:

  >>> rt = tf.ragged.constant([[1, 2], [3]])
  >>> tf.tile(rt, [3, 2]).to_list()
  [[1, 2, 1, 2], [3, 3], [1, 2, 1, 2], [3, 3], [1, 2, 1, 2], [3, 3]]
  """
def expand_dims(input: ragged_tensor.Ragged, axis, name: Incomplete | None = None):
    """Inserts a dimension with shape 1 into a potentially ragged tensor's shape.

  Given a potentially ragged tenor `input`, this operation inserts a
  dimension with size 1 at the dimension `axis` of `input`'s shape.

  The following table gives some examples showing how `ragged.expand_dims`
  impacts the shapes of different input tensors.  Ragged dimensions are
  indicated by enclosing them in parentheses.

  input.shape             | axis | result.shape
  ----------------------- | ---- | -----------------------------
  `[D1, D2]`              |  `0` | `[1, D1, D2]`
  `[D1, D2]`              |  `1` | `[D1, 1, D2]`
  `[D1, D2]`              |  `2` | `[D1, D2, 1]`
  `[D1, (D2), (D3), D4]`  |  `0` | `[1, D1, (D2), (D3), D4]`
  `[D1, (D2), (D3), D4]`  |  `1` | `[D1, 1, (D2), (D3), D4]`
  `[D1, (D2), (D3), D4]`  |  `2` | `[D1, (D2), 1, (D3), D4]`
  `[D1, (D2), (D3), D4]`  |  `3` | `[D1, (D2), (D3), 1, D4]`
  `[D1, (D2), (D3), D4]`  |  `4` | `[D1, (D2), (D3), D4, 1]`

  Args:
    input: The potentially tensor that should be expanded with a new dimension.
    axis: An integer constant indicating where the new dimension should be
      inserted.
    name: A name for the operation (optional).

  Returns:
    A tensor with the same values as `input`, with an added dimension of
    size 1 at `axis`.

  #### Examples:

  >>> rt = tf.ragged.constant([[1, 2], [3]])
  >>> print(rt.shape)
  (2, None)

  >>> expanded = tf.expand_dims(rt, axis=0)
  >>> print(expanded.shape, expanded)
  (1, 2, None) <tf.RaggedTensor [[[1, 2], [3]]]>

  >>> expanded = tf.expand_dims(rt, axis=1)
  >>> print(expanded.shape, expanded)
  (2, 1, None) <tf.RaggedTensor [[[1, 2]], [[3]]]>

  >>> expanded = tf.expand_dims(rt, axis=2)
  >>> print(expanded.shape, expanded)
  (2, None, 1) <tf.RaggedTensor [[[1], [2]], [[3]]]>
  """
def size(input: ragged_tensor.Ragged, out_type=..., name: Incomplete | None = None):
    """Returns the size of a potentially ragged tensor.

  The size of a ragged tensor is the size of its inner values.

  #### Example:

  >>> tf.size(tf.ragged.constant([[1, 2], [3]])).numpy()
  3

  Args:
    input: A potentially ragged `Tensor`.
    out_type: The numeric output type for the operation.
    name: A name for the operation (optional).

  Returns:
    A Tensor of type `out_type`.
  """
def rank(input: ragged_tensor.Ragged, name: Incomplete | None = None):
    """Returns the rank of a RaggedTensor.

  Returns a 0-D `int32` `Tensor` representing the rank of `input`.

  #### Example:

  >>> # shape of tensor 't' is [2, None, None]
  >>> t = tf.ragged.constant([[[1], [2, 2]], [[3, 3, 3], [4, 4, 4, 4]]])
  >>> tf.rank(t).numpy()
  3

  Args:
    input: A `RaggedTensor`
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """
def ragged_one_hot(indices: ragged_tensor.Ragged, depth, on_value: Incomplete | None = None, off_value: Incomplete | None = None, axis: Incomplete | None = None, dtype: Incomplete | None = None, name: Incomplete | None = None):
    """Applies tf.one_hot along the values of a RaggedTensor."""
def stack_dynamic_partitions(data, partitions, num_partitions, name: Incomplete | None = None):
    """Stacks dynamic partitions of a Tensor or RaggedTensor.

  Returns a RaggedTensor `output` with `num_partitions` rows, where the row
  `output[i]` is formed by stacking all slices `data[j1...jN]` such that
  `partitions[j1...jN] = i`.  Slices of `data` are stacked in row-major
  order.

  If `num_partitions` is an `int` (not a `Tensor`), then this is equivalent to
  `tf.ragged.stack(tf.dynamic_partition(data, partitions, num_partitions))`.

  #### Example:

  >>> data           = ['a', 'b', 'c', 'd', 'e']
  >>> partitions     = [  3,   0,   2,   2,   3]
  >>> num_partitions = 5
  >>> tf.ragged.stack_dynamic_partitions(data, partitions, num_partitions)
  <tf.RaggedTensor [[b'b'], [], [b'c', b'd'], [b'a', b'e'], []]>

  Args:
    data: A `Tensor` or `RaggedTensor` containing the values to stack.
    partitions: An `int32` or `int64` `Tensor` or `RaggedTensor` specifying the
      partition that each slice of `data` should be added to. `partitions.shape`
      must be a prefix of `data.shape`.  Values must be greater than or equal to
      zero, and less than `num_partitions`. `partitions` is not required to be
      sorted.
    num_partitions: An `int32` or `int64` scalar specifying the number of
      partitions to output.  This determines the number of rows in `output`.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` containing the stacked partitions.  The returned tensor
    has the same dtype as `data`, and its shape is
    `[num_partitions, (D)] + data.shape[partitions.rank:]`, where `(D)` is a
    ragged dimension whose length is the number of data slices stacked for
    each `partition`.
  """
def reverse(tensor: ragged_tensor.Ragged, axis, name: Incomplete | None = None):
    """Reverses a RaggedTensor along the specified axes.

  #### Example:

  >>> data = tf.ragged.constant([
  ...   [[1, 2], [3, 4]], [[5, 6]], [[7, 8], [9, 10], [11, 12]]])
  >>> tf.reverse(data, axis=[0, 2])
  <tf.RaggedTensor [[[8, 7], [10, 9], [12, 11]], [[6, 5]], [[2, 1], [4, 3]]]>

  Args:
    tensor: A 'RaggedTensor' to reverse.
    axis: A list or tuple of 'int' or a constant 1D 'tf.Tensor'. The indices of
      the axes to reverse.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A 'RaggedTensor'.
  """
def cross(inputs, name: Incomplete | None = None):
    """Generates feature cross from a list of tensors.

  The input tensors must have `rank=2`, and must all have the same number of
  rows.  The result is a `RaggedTensor` with the same number of rows as the
  inputs, where `result[row]` contains a list of all combinations of values
  formed by taking a single value from each input's corresponding row
  (`inputs[i][row]`).  Values are combined by joining their strings with '_X_'.
  E.g.:

  >>> tf.ragged.cross([tf.ragged.constant([['a'], ['b', 'c']]),
  ...                  tf.ragged.constant([['d'], ['e']]),
  ...                  tf.ragged.constant([['f'], ['g']])])
  <tf.RaggedTensor [[b'a_X_d_X_f'], [b'b_X_e_X_g', b'c_X_e_X_g']]>

  Args:
    inputs: A list of `RaggedTensor` or `Tensor` or `SparseTensor`.
    name: Optional name for the op.

  Returns:
    A 2D `RaggedTensor` of type `string`.
  """
def cross_hashed(inputs, num_buckets: int = 0, hash_key: Incomplete | None = None, name: Incomplete | None = None):
    """Generates hashed feature cross from a list of tensors.

  The input tensors must have `rank=2`, and must all have the same number of
  rows.  The result is a `RaggedTensor` with the same number of rows as the
  inputs, where `result[row]` contains a list of all combinations of values
  formed by taking a single value from each input's corresponding row
  (`inputs[i][row]`).  Values are combined by hashing together their
  fingerprints. E.g.:

  >>> tf.ragged.cross_hashed([tf.ragged.constant([['a'], ['b', 'c']]),
  ...                         tf.ragged.constant([['d'], ['e']]),
  ...                         tf.ragged.constant([['f'], ['g']])],
  ...                        num_buckets=100)
  <tf.RaggedTensor [[78], [66, 74]]>

  Args:
    inputs: A list of `RaggedTensor` or `Tensor` or `SparseTensor`.
    num_buckets: A non-negative `int` that used to bucket the hashed values. If
      `num_buckets != 0`, then `output = hashed_value % num_buckets`.
    hash_key: Integer hash_key that will be used by the `FingerprintCat64`
      function. If not given, a default key is used.
    name: Optional name for the op.

  Returns:
    A 2D `RaggedTensor` of type `int64`.
  """
def dynamic_partition(data: ragged_tensor.RaggedOrDense, partitions: ragged_tensor.RaggedOrDense, num_partitions, name: Incomplete | None = None):
    """RaggedTensor dispatch override for tf.dynamic_partition."""
def split(value: ragged_tensor.Ragged, num_or_size_splits, axis: int = 0, num: Incomplete | None = None, name: Incomplete | None = None):
    """Splits a RaggedTensor `value` into a list of sub RaggedTensors.

  If `num_or_size_splits` is an `int`,  then it splits `value` along the
  dimension `axis` into `num_or_size_splits` smaller RaggedTensors. This
  requires that `value.shape[axis]` is divisible by `num_or_size_splits`.

  If `num_or_size_splits` is a 1-D Tensor (or list), then `value` is split into
  `len(num_or_size_splits)` elements. The shape of the `i`-th element has the
  same size as the `value` except along dimension `axis` where the size is
  `num_or_size_splits[i]`.

  Splits along a ragged dimension is not allowed.

  For example:

  >>> rt = tf.RaggedTensor.from_row_lengths(
  ...      np.arange(6 * 3).reshape(6, 3), row_lengths=[1, 2, 2, 1])
  >>> rt.shape
  TensorShape([4, None, 3])
  >>>
  >>> rt1, rt2 = tf.split(rt, 2)  # uniform splits
  >>> rt1.shape
  TensorShape([2, None, 3])
  >>> rt2.shape
  TensorShape([2, None, 3])
  >>>
  >>> rt3, rt4, rt5 = tf.split(rt, [1, 2, 1])  # ragged splits
  >>> rt3.shape
  TensorShape([1, None, 3])
  >>> rt4.shape
  TensorShape([2, None, 3])
  >>> rt5.shape
  TensorShape([1, None, 3])
  >>>
  >>> rt6, rt7 = tf.split(rt, [1, 2], axis=2)  # splits along axis 2
  >>> rt6.shape
  TensorShape([4, None, 1])
  >>> rt7.shape
  TensorShape([4, None, 2])

  Args:
    value: The `RaggedTensor` to split.
    num_or_size_splits: Either an `int` indicating the number of splits
      along `axis` or a 1-D integer `Tensor` or Python list containing the sizes
      of each output tensor along `axis`. If a Python int, then it must evenly
      divide `value.shape[axis]`; otherwise the sum of sizes along the split
      axis must match that of the `value`.
    axis: An `int` or scalar `int32` `Tensor`. The dimension along which
      to split. Must be in the range `[-rank(value), rank(value))`. Defaults to
      0.
    num: An `int` used to specify the number of outputs when
      `num_or_size_splits` is a 1-D list or `Tensor` and its length is
      statically unknown, e.g., specifying `tf.TensorSepc(None)` with
      the `input_signature` argument of `tf.function` (optional).
    name: A name for the operation (optional).

  Returns:
    if `num_or_size_splits` is an `int` returns a list of `num_or_size_splits`
    `RaggedTensor` objects; if `num_or_size_splits` is a 1-D Tensor returns
    `num_or_size_splits.get_shape[0]` `RaggedTensor` objects resulting from
    splitting `value`.

  Raises:
    ValueError: If the dimension `axis` of `value` is a ragged dimension.
    ValueError: If `num` is unspecified and cannot be inferred.
    ValueError: If `num` is specified but doesn't match the length of
      `num_or_size_splits`.
    ValueError: If `num_or_size_splits` is an `int` and less than 1.
    TypeError: If `num_or_size_splits` is not an `int` or 1-D
      list or 1-D `Tensor`.
    InvalidArgumentError: If the `axis` of `value` cannot be exactly splitted
      by `num_or_size_splits`.
    InvalidArgumentError: If `num_or_size_splits` is contains negative integers.
    InvalidArgumentError: If `num_or_size_splits`'s static shape is unknown and
      its dynamic shape is inconsistent `num`.
    InvalidArgumentError: If `num_or_size_splits`'s static rank is unknown and
      `axis` is a negative integer.
  """
def ragged_reshape(tensor: ragged_tensor.RaggedOrDense, shape: dynamic_ragged_shape.DenseOrRaggedShape) -> Union[ragged_tensor.RaggedTensor, ops.Tensor]:
    """Reshapes a tensor or ragged tensor."""
def broadcast_to(input: ragged_tensor.RaggedOrDense, shape: dynamic_ragged_shape.DynamicRaggedShape) -> Union[ragged_tensor.RaggedTensor, ops.Tensor]:
    """Broadcasts a potentially ragged tensor to a ragged shape.

  Tiles `input` as necessary to match the given shape.

  Behavior is undefined if `input` is not broadcast-compatible with `shape`.

  Args:
    input: The potentially ragged tensor to broadcast.
    shape: A `DynamicRaggedShape`

  Returns:
    A potentially ragged tensor whose values are taken from
    `input`, and whose shape matches `shape`.
  """
def ragged_shape(input: ragged_tensor.Ragged, name: Optional[str] = None, out_type=...) -> dynamic_ragged_shape.DynamicRaggedShape:
    """Returns the shape of a RaggedTensor.

  Args:
    input: A `RaggedTensor`
    name: A name for the operation (optional).
    out_type: dtype used to encode the shape.

  Returns:
    A `tf.experimental.DynamicRaggedShape`
  """
def broadcast_dynamic_shape(shape_x: dynamic_ragged_shape.DenseOrRaggedShape, shape_y: dynamic_ragged_shape.DenseOrRaggedShape) -> dynamic_ragged_shape.DynamicRaggedShape:
    """Returns the shape formed by broadcasting two shapes to be compatible.

  1. If shape_x and shape_y both have row_partitions, then fail if their dtypes
     don't match.
  2. If neither has row_partitions and they have different dtypes,
     go with int64.
  3. If one has row_partitions, go with that dtype.

  Args:
    shape_x: A `DynamicRaggedShape`
    shape_y: A `DynamicRaggedShape`

  Returns:
    A `DynamicRaggedShape`.
  Raises:
    ValueError: If `shape_x` and `shape_y` are not broadcast-compatible.
  """
def ones(shape: dynamic_ragged_shape.DynamicRaggedShape, dtype=..., name: Incomplete | None = None) -> ragged_tensor.RaggedOrDense:
    """Returns ones shaped like x."""
def zeros(shape: dynamic_ragged_shape.DynamicRaggedShape, dtype=..., name: Incomplete | None = None) -> ragged_tensor.RaggedOrDense:
    """Returns ones shaped like x."""
def fill(dims: dynamic_ragged_shape.DynamicRaggedShape, value: core_types.TensorLike, name: Optional[str] = None) -> ragged_tensor.RaggedOrDense:
    """Creates a tensor with shape `dims` and fills it with `value`."""
def bitcast(input: ragged_tensor.RaggedOrDense, type, name: Incomplete | None = None) -> ragged_tensor.RaggedOrDense:
    """RaggedTensor dispatch override for tf.bitcast."""
