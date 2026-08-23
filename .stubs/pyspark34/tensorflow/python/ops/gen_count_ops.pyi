from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _DenseCountSparseOutputOutput(NamedTuple):
    output_indices: Incomplete
    output_values: Incomplete
    output_dense_shape: Incomplete

def dense_count_sparse_output(values, weights, binary_output, minlength: int = -1, maxlength: int = -1, name: Incomplete | None = None):
    """Performs sparse-output bin counting for a tf.tensor input.

    Counts the number of times each value occurs in the input.

  Args:
    values: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Tensor containing data to count.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      A Tensor of the same shape as indices containing per-index weight values. May
      also be the empty tensor if no weights are used.
    binary_output: A `bool`.
      Whether to output the number of occurrences of each value or 1.
    minlength: An optional `int` that is `>= -1`. Defaults to `-1`.
      Minimum value to count. Can be set to -1 for no minimum.
    maxlength: An optional `int` that is `>= -1`. Defaults to `-1`.
      Maximum value to count. Can be set to -1 for no maximum.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_indices, output_values, output_dense_shape).

    output_indices: A `Tensor` of type `int64`.
    output_values: A `Tensor`. Has the same type as `weights`.
    output_dense_shape: A `Tensor` of type `int64`.
  """

DenseCountSparseOutput: Incomplete

def dense_count_sparse_output_eager_fallback(values, weights, binary_output, minlength, maxlength, name, ctx): ...

class _RaggedCountSparseOutputOutput(NamedTuple):
    output_indices: Incomplete
    output_values: Incomplete
    output_dense_shape: Incomplete

def ragged_count_sparse_output(splits, values, weights, binary_output, minlength: int = -1, maxlength: int = -1, name: Incomplete | None = None):
    """Performs sparse-output bin counting for a ragged tensor input.

    Counts the number of times each value occurs in the input.

  Args:
    splits: A `Tensor` of type `int64`.
      Tensor containing the row splits of the ragged tensor to count.
    values: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Tensor containing values of the sparse tensor to count.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      A Tensor of the same shape as indices containing per-index weight values.
      May also be the empty tensor if no weights are used.
    binary_output: A `bool`.
      Whether to output the number of occurrences of each value or 1.
    minlength: An optional `int` that is `>= -1`. Defaults to `-1`.
      Minimum value to count. Can be set to -1 for no minimum.
    maxlength: An optional `int` that is `>= -1`. Defaults to `-1`.
      Maximum value to count. Can be set to -1 for no maximum.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_indices, output_values, output_dense_shape).

    output_indices: A `Tensor` of type `int64`.
    output_values: A `Tensor`. Has the same type as `weights`.
    output_dense_shape: A `Tensor` of type `int64`.
  """

RaggedCountSparseOutput: Incomplete

def ragged_count_sparse_output_eager_fallback(splits, values, weights, binary_output, minlength, maxlength, name, ctx): ...

class _SparseCountSparseOutputOutput(NamedTuple):
    output_indices: Incomplete
    output_values: Incomplete
    output_dense_shape: Incomplete

def sparse_count_sparse_output(indices, values, dense_shape, weights, binary_output, minlength: int = -1, maxlength: int = -1, name: Incomplete | None = None):
    """Performs sparse-output bin counting for a sparse tensor input.

    Counts the number of times each value occurs in the input.

  Args:
    indices: A `Tensor` of type `int64`.
      Tensor containing the indices of the sparse tensor to count.
    values: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Tensor containing values of the sparse tensor to count.
    dense_shape: A `Tensor` of type `int64`.
      Tensor containing the dense shape of the sparse tensor to count.
    weights: A `Tensor`. Must be one of the following types: `int32`, `int64`, `float32`, `float64`.
      A Tensor of the same shape as indices containing per-index weight values.
      May also be the empty tensor if no weights are used.
    binary_output: A `bool`.
      Whether to output the number of occurrences of each value or 1.
    minlength: An optional `int` that is `>= -1`. Defaults to `-1`.
      Minimum value to count. Can be set to -1 for no minimum.
    maxlength: An optional `int` that is `>= -1`. Defaults to `-1`.
      Maximum value to count. Can be set to -1 for no maximum.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_indices, output_values, output_dense_shape).

    output_indices: A `Tensor` of type `int64`.
    output_values: A `Tensor`. Has the same type as `weights`.
    output_dense_shape: A `Tensor` of type `int64`.
  """

SparseCountSparseOutput: Incomplete

def sparse_count_sparse_output_eager_fallback(indices, values, dense_shape, weights, binary_output, minlength, maxlength, name, ctx): ...
