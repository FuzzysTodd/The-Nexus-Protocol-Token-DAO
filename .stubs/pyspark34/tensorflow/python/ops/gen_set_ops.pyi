from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _DenseToDenseSetOperationOutput(NamedTuple):
    result_indices: Incomplete
    result_values: Incomplete
    result_shape: Incomplete

def dense_to_dense_set_operation(set1, set2, set_operation, validate_indices: bool = True, name: Incomplete | None = None):
    """Applies set operation along last dimension of 2 `Tensor` inputs.

  See SetOperationOp::SetOperationFromContext for values of `set_operation`.

  Output `result` is a `SparseTensor` represented by `result_indices`,
  `result_values`, and `result_shape`. For `set1` and `set2` ranked `n`, this
  has rank `n` and the same 1st `n-1` dimensions as `set1` and `set2`. The `nth`
  dimension contains the result of `set_operation` applied to the corresponding
  `[0...n-1]` dimension of `set`.

  Args:
    set1: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `string`.
      `Tensor` with rank `n`. 1st `n-1` dimensions must be the same as `set2`.
      Dimension `n` contains values in a set, duplicates are allowed but ignored.
    set2: A `Tensor`. Must have the same type as `set1`.
      `Tensor` with rank `n`. 1st `n-1` dimensions must be the same as `set1`.
      Dimension `n` contains values in a set, duplicates are allowed but ignored.
    set_operation: A `string`.
    validate_indices: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (result_indices, result_values, result_shape).

    result_indices: A `Tensor` of type `int64`.
    result_values: A `Tensor`. Has the same type as `set1`.
    result_shape: A `Tensor` of type `int64`.
  """

DenseToDenseSetOperation: Incomplete

def dense_to_dense_set_operation_eager_fallback(set1, set2, set_operation, validate_indices, name, ctx): ...

class _DenseToSparseSetOperationOutput(NamedTuple):
    result_indices: Incomplete
    result_values: Incomplete
    result_shape: Incomplete

def dense_to_sparse_set_operation(set1, set2_indices, set2_values, set2_shape, set_operation, validate_indices: bool = True, name: Incomplete | None = None):
    """Applies set operation along last dimension of `Tensor` and `SparseTensor`.

  See SetOperationOp::SetOperationFromContext for values of `set_operation`.

  Input `set2` is a `SparseTensor` represented by `set2_indices`, `set2_values`,
  and `set2_shape`. For `set2` ranked `n`, 1st `n-1` dimensions must be the same
  as `set1`. Dimension `n` contains values in a set, duplicates are allowed but
  ignored.

  If `validate_indices` is `True`, this op validates the order and range of `set2`
  indices.

  Output `result` is a `SparseTensor` represented by `result_indices`,
  `result_values`, and `result_shape`. For `set1` and `set2` ranked `n`, this
  has rank `n` and the same 1st `n-1` dimensions as `set1` and `set2`. The `nth`
  dimension contains the result of `set_operation` applied to the corresponding
  `[0...n-1]` dimension of `set`.

  Args:
    set1: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `string`.
      `Tensor` with rank `n`. 1st `n-1` dimensions must be the same as `set2`.
      Dimension `n` contains values in a set, duplicates are allowed but ignored.
    set2_indices: A `Tensor` of type `int64`.
      2D `Tensor`, indices of a `SparseTensor`. Must be in row-major
      order.
    set2_values: A `Tensor`. Must have the same type as `set1`.
      1D `Tensor`, values of a `SparseTensor`. Must be in row-major
      order.
    set2_shape: A `Tensor` of type `int64`.
      1D `Tensor`, shape of a `SparseTensor`. `set2_shape[0...n-1]` must
      be the same as the 1st `n-1` dimensions of `set1`, `result_shape[n]` is the
      max set size across `n-1` dimensions.
    set_operation: A `string`.
    validate_indices: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (result_indices, result_values, result_shape).

    result_indices: A `Tensor` of type `int64`.
    result_values: A `Tensor`. Has the same type as `set1`.
    result_shape: A `Tensor` of type `int64`.
  """

DenseToSparseSetOperation: Incomplete

def dense_to_sparse_set_operation_eager_fallback(set1, set2_indices, set2_values, set2_shape, set_operation, validate_indices, name, ctx): ...
def set_size(set_indices, set_values, set_shape, validate_indices: bool = True, name: Incomplete | None = None):
    """Number of unique elements along last dimension of input `set`.

  Input `set` is a `SparseTensor` represented by `set_indices`, `set_values`,
  and `set_shape`. The last dimension contains values in a set, duplicates are
  allowed but ignored.

  If `validate_indices` is `True`, this op validates the order and range of `set`
  indices.

  Args:
    set_indices: A `Tensor` of type `int64`.
      2D `Tensor`, indices of a `SparseTensor`.
    set_values: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `string`.
      1D `Tensor`, values of a `SparseTensor`.
    set_shape: A `Tensor` of type `int64`.
      1D `Tensor`, shape of a `SparseTensor`.
    validate_indices: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

SetSize: Incomplete

def set_size_eager_fallback(set_indices, set_values, set_shape, validate_indices, name, ctx): ...

class _SparseToSparseSetOperationOutput(NamedTuple):
    result_indices: Incomplete
    result_values: Incomplete
    result_shape: Incomplete

def sparse_to_sparse_set_operation(set1_indices, set1_values, set1_shape, set2_indices, set2_values, set2_shape, set_operation, validate_indices: bool = True, name: Incomplete | None = None):
    """Applies set operation along last dimension of 2 `SparseTensor` inputs.

  See SetOperationOp::SetOperationFromContext for values of `set_operation`.

  If `validate_indices` is `True`, `SparseToSparseSetOperation` validates the
  order and range of `set1` and `set2` indices.

  Input `set1` is a `SparseTensor` represented by `set1_indices`, `set1_values`,
  and `set1_shape`. For `set1` ranked `n`, 1st `n-1` dimensions must be the same
  as `set2`. Dimension `n` contains values in a set, duplicates are allowed but
  ignored.

  Input `set2` is a `SparseTensor` represented by `set2_indices`, `set2_values`,
  and `set2_shape`. For `set2` ranked `n`, 1st `n-1` dimensions must be the same
  as `set1`. Dimension `n` contains values in a set, duplicates are allowed but
  ignored.

  If `validate_indices` is `True`, this op validates the order and range of `set1`
  and `set2` indices.

  Output `result` is a `SparseTensor` represented by `result_indices`,
  `result_values`, and `result_shape`. For `set1` and `set2` ranked `n`, this
  has rank `n` and the same 1st `n-1` dimensions as `set1` and `set2`. The `nth`
  dimension contains the result of `set_operation` applied to the corresponding
  `[0...n-1]` dimension of `set`.

  Args:
    set1_indices: A `Tensor` of type `int64`.
      2D `Tensor`, indices of a `SparseTensor`. Must be in row-major
      order.
    set1_values: A `Tensor`. Must be one of the following types: `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `string`.
      1D `Tensor`, values of a `SparseTensor`. Must be in row-major
      order.
    set1_shape: A `Tensor` of type `int64`.
      1D `Tensor`, shape of a `SparseTensor`. `set1_shape[0...n-1]` must
      be the same as `set2_shape[0...n-1]`, `set1_shape[n]` is the
      max set size across `0...n-1` dimensions.
    set2_indices: A `Tensor` of type `int64`.
      2D `Tensor`, indices of a `SparseTensor`. Must be in row-major
      order.
    set2_values: A `Tensor`. Must have the same type as `set1_values`.
      1D `Tensor`, values of a `SparseTensor`. Must be in row-major
      order.
    set2_shape: A `Tensor` of type `int64`.
      1D `Tensor`, shape of a `SparseTensor`. `set2_shape[0...n-1]` must
      be the same as `set1_shape[0...n-1]`, `set2_shape[n]` is the
      max set size across `0...n-1` dimensions.
    set_operation: A `string`.
    validate_indices: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (result_indices, result_values, result_shape).

    result_indices: A `Tensor` of type `int64`.
    result_values: A `Tensor`. Has the same type as `set1_values`.
    result_shape: A `Tensor` of type `int64`.
  """

SparseToSparseSetOperation: Incomplete

def sparse_to_sparse_set_operation_eager_fallback(set1_indices, set1_values, set1_shape, set2_indices, set2_values, set2_shape, set_operation, validate_indices, name, ctx): ...
