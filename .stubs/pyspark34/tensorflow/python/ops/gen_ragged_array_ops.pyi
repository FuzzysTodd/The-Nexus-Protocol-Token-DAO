from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

class _RaggedCrossOutput(NamedTuple):
    output_values: Incomplete
    output_row_splits: Incomplete

def ragged_cross(ragged_values, ragged_row_splits, sparse_indices, sparse_values, sparse_shape, dense_inputs, input_order, hashed_output, num_buckets, hash_key, out_values_type, out_row_splits_type, name: Incomplete | None = None):
    """Generates a feature cross from a list of tensors, and returns it as a
RaggedTensor.  See `tf.ragged.cross` for more details.

  Args:
    ragged_values: A list of `Tensor` objects with types from: `int64`, `string`.
      The values tensor for each RaggedTensor input.
    ragged_row_splits: A list of `Tensor` objects with types from: `int32`, `int64`.
      The row_splits tensor for each RaggedTensor input.
    sparse_indices: A list of `Tensor` objects with type `int64`.
      The indices tensor for each SparseTensor input.
    sparse_values: A list of `Tensor` objects with types from: `int64`, `string`.
      The values tensor for each SparseTensor input.
    sparse_shape: A list with the same length as `sparse_indices` of `Tensor` objects with type `int64`.
      The dense_shape tensor for each SparseTensor input.
    dense_inputs: A list of `Tensor` objects with types from: `int64`, `string`.
      The tf.Tensor inputs.
    input_order: A `string`.
      String specifying the tensor type for each input.  The `i`th character in
      this string specifies the type of the `i`th input, and is one of: 'R' (ragged),
      'D' (dense), or 'S' (sparse).  This attr is used to ensure that the crossed
      values are combined in the order of the inputs from the call to tf.ragged.cross.
    hashed_output: A `bool`.
    num_buckets: An `int` that is `>= 0`.
    hash_key: An `int`.
    out_values_type: A `tf.DType` from: `tf.int64, tf.string`.
    out_row_splits_type: A `tf.DType` from: `tf.int32, tf.int64`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_values, output_row_splits).

    output_values: A `Tensor` of type `out_values_type`.
    output_row_splits: A `Tensor` of type `out_row_splits_type`.
  """

RaggedCross: Incomplete

def ragged_cross_eager_fallback(ragged_values, ragged_row_splits, sparse_indices, sparse_values, sparse_shape, dense_inputs, input_order, hashed_output, num_buckets, hash_key, out_values_type, out_row_splits_type, name, ctx): ...

class _RaggedGatherOutput(NamedTuple):
    output_nested_splits: Incomplete
    output_dense_values: Incomplete

def ragged_gather(params_nested_splits, params_dense_values, indices, OUTPUT_RAGGED_RANK, name: Incomplete | None = None):
    """Gather ragged slices from `params` axis `0` according to `indices`.

  Outputs a `RaggedTensor` output composed from `output_dense_values` and
  `output_nested_splits`, such that:

  ```python
  output.shape = indices.shape + params.shape[1:]
  output.ragged_rank = indices.shape.ndims + params.ragged_rank
  output[i...j, d0...dn] = params[indices[i...j], d0...dn]
  ```

  where

  * `params =
     ragged.from_nested_row_splits(params_dense_values, params_nested_splits)`
     provides the values that should be gathered.
  * `indices` ia a dense tensor with dtype `int32` or `int64`, indicating which
     values should be gathered.
  * `output =
     ragged.from_nested_row_splits(output_dense_values, output_nested_splits)`
     is the output tensor.

  (Note: This c++ op is used to implement the higher-level python
  `tf.ragged.gather` op, which also supports ragged indices.)

  Args:
    params_nested_splits: A list of at least 1 `Tensor` objects with the same type in: `int32`, `int64`.
      The `nested_row_splits` tensors that define the row-partitioning for the
      `params` RaggedTensor input.
    params_dense_values: A `Tensor`.
      The `flat_values` for the `params` RaggedTensor. There was a terminology change
      at the python level from dense_values to flat_values, so dense_values is the
      deprecated name.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Indices in the outermost dimension of `params` of the values that should be
      gathered.
    OUTPUT_RAGGED_RANK: An `int` that is `>= 0`.
      The ragged rank of the output RaggedTensor. `output_nested_splits` will contain
      this number of `row_splits` tensors. This value should equal
      `indices.shape.ndims + params.ragged_rank - 1`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_nested_splits, output_dense_values).

    output_nested_splits: A list of `OUTPUT_RAGGED_RANK` `Tensor` objects with the same type as `params_nested_splits`.
    output_dense_values: A `Tensor`. Has the same type as `params_dense_values`.
  """

RaggedGather: Incomplete

def ragged_gather_eager_fallback(params_nested_splits, params_dense_values, indices, OUTPUT_RAGGED_RANK, name, ctx): ...
