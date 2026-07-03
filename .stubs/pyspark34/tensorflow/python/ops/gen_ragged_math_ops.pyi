from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _RaggedRangeOutput(NamedTuple):
    rt_nested_splits: Incomplete
    rt_dense_values: Incomplete

def ragged_range(starts, limits, deltas, Tsplits=..., name: Incomplete | None = None):
    """Returns a `RaggedTensor` containing the specified sequences of numbers.

  
  Returns a `RaggedTensor` `result` composed from `rt_dense_values` and
  `rt_nested_splits`, such that
  `result[i] = range(starts[i], limits[i], deltas[i])`.

  ```python
  (rt_nested_splits, rt_dense_values) = ragged_range(
        starts=[2, 5, 8], limits=[3, 5, 12], deltas=1)
  result = tf.ragged.from_row_splits(rt_dense_values, rt_nested_splits)
  print(result)
  <tf.RaggedTensor [[2], [], [8, 9, 10, 11]] >
  ```

  The input tensors `starts`, `limits`, and `deltas` may be scalars or vectors.
  The vector inputs must all have the same size.  Scalar inputs are broadcast
  to match the size of the vector inputs.

  Args:
    starts: A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`, `int32`, `int64`.
      The starts of each range.
    limits: A `Tensor`. Must have the same type as `starts`.
      The limits of each range.
    deltas: A `Tensor`. Must have the same type as `starts`.
      The deltas of each range.
    Tsplits: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (rt_nested_splits, rt_dense_values).

    rt_nested_splits: A `Tensor` of type `Tsplits`.
    rt_dense_values: A `Tensor`. Has the same type as `starts`.
  """

RaggedRange: Incomplete

def ragged_range_eager_fallback(starts, limits, deltas, Tsplits, name, ctx): ...
