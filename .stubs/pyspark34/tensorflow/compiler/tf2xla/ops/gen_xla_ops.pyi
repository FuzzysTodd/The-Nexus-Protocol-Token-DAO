from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def xla_all_reduce(input, group_assignment, reduce_op, mode, name: Incomplete | None = None):
    '''Wraps the XLA AllReduce operator

    documented at https://www.tensorflow.org/xla/operation_semantics#allreduce.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `int32`, `uint32`.
      Array or a non-empty tuple of arrays to reduce across replicas.
    group_assignment: A `Tensor` of type `int32`.
      Groups between which the reductions are performed.
    reduce_op: A `string` from: `"Min", "Max", "Mul", "Add", "Mean"`.
      Reduction computation.
    mode: A `string` from: `"CrossReplica", "CrossReplicaAndPartition"`.
      group mode.
      CrossReplica: group_assignment contains replica_id. Each group contains the
        replicas for the current partition.
      CrossReplicaAndPartition: group_assignment contains replica_id. Each group
        contains the replicas for all partitions.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

XlaAllReduce: Incomplete

def xla_all_reduce_eager_fallback(input, group_assignment, reduce_op, mode, name, ctx): ...

class _XlaBroadcastHelperOutput(NamedTuple):
    lhs_output: Incomplete
    rhs_output: Incomplete

def xla_broadcast_helper(lhs, rhs, broadcast_dims, name: Incomplete | None = None):
    """Helper operator for performing XLA-style broadcasts

  Broadcasts `lhs` and `rhs` to the same rank, by adding size 1 dimensions to
  whichever of `lhs` and `rhs` has the lower rank, using XLA's broadcasting rules
  for binary operators.

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the LHS input tensor
    rhs: A `Tensor`. Must have the same type as `lhs`. the RHS input tensor
    broadcast_dims: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      an XLA-style broadcast dimension specification
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (lhs_output, rhs_output).

    lhs_output: A `Tensor`. Has the same type as `lhs`. the broadcasted LHS tensor
    rhs_output: A `Tensor`. Has the same type as `lhs`. the broadcasted RHS tensor
  """

XlaBroadcastHelper: Incomplete

def xla_broadcast_helper_eager_fallback(lhs, rhs, broadcast_dims, name, ctx): ...
def xla_call_module(args, version, module, Sout, Tout, dim_args_spec, name: Incomplete | None = None):
    '''Temporary op for experimenting with jax2tf.

  DO NOT USE THIS OP. It has no backwards compatibility guarantees. It is also
  very likely to change. This op will be used only in jax2tf under an
  experimental flag.

  This is an experimental op to allow a smooth evolution of jax2tf towards
  emitting and serializing StableHLO directly from JAX.

  The serialized module must return a tuple if and only if the Sout is an empty
  list or a list with more than 1 elements. The length of Tout and Sout must
  match. This op always returns a tuple of results, even if the module returns
  a single result.

  The handling of dynamic shapes is work-in-progress. At the moment, the
  JAX lowering for dynamic shapes will prepend one dimension parameter to the
  serialized module for each dimension whose value must be passed in.
  The "args" correspond to the non-dimension arguments. During compilation
  we compute the values of the dimension arguments based on the static shapes of
  the "args". In order to do this, we encode for each dimension argument a
  specification of how to compute its value, as a string, in the form
  "<arg_idx>.<axis_idx>".
  E.g., the specification "2.1" denotes the value args[2].shape[1].

  Args:
    args: A list of `Tensor` objects.
      A list of `Tensor` with possibly different types to be passed as arguments
      to the HLO module. These are all non-dimension arguments. The dimension
      arguments are computed at JIT time.
    version: An `int`.
      Changes when we change the semantics of the op, to support backwards
      compatibility. Version 1 carries an MHLO text or bytecode `module`. From
      version 2, the op carries a StableHLO text or bytecode `module`.
    module: A `string`.
      A serialized computation, a text or bytecode representation of
      an mlir.Module.
    Sout: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      List of output tensor shapes.
    Tout: A list of `tf.DTypes`. List of output tensor data types.
    dim_args_spec: A list of `strings`.
      the specification for the dimension arguments, one for each
      dimension argument. In absence of dynamic shapes this list is empty.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
  '''

XlaCallModule: Incomplete

def xla_call_module_eager_fallback(args, version, module, Sout, Tout, dim_args_spec, name, ctx): ...
def xla_conv(lhs, rhs, window_strides, padding, lhs_dilation, rhs_dilation, feature_group_count, dimension_numbers, precision_config, name: Incomplete | None = None):
    """Wraps the XLA ConvGeneralDilated operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#conv_convolution
  .

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the input tensor
    rhs: A `Tensor`. Must have the same type as `lhs`. the kernel tensor
    window_strides: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      the inter-window strides
    padding: A `Tensor`. Must have the same type as `window_strides`.
      the padding to apply at the start and end of each input dimensions
    lhs_dilation: A `Tensor`. Must have the same type as `window_strides`.
      dilation to apply between input elements
    rhs_dilation: A `Tensor`. Must have the same type as `window_strides`.
      dilation to apply between kernel elements
    feature_group_count: A `Tensor`. Must have the same type as `window_strides`.
      number of feature groups for grouped convolution.
    dimension_numbers: A `string`.
      a serialized xla::ConvolutionDimensionNumbers proto.
    precision_config: A `string`. a serialized xla::PrecisionConfig proto.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `lhs`.
  """

XlaConv: Incomplete

def xla_conv_eager_fallback(lhs, rhs, window_strides, padding, lhs_dilation, rhs_dilation, feature_group_count, dimension_numbers, precision_config, name, ctx): ...
def xla_conv_v2(lhs, rhs, window_strides, padding, lhs_dilation, rhs_dilation, feature_group_count, dimension_numbers, precision_config, preferred_element_type, batch_group_count: int = 1, name: Incomplete | None = None):
    """Wraps the XLA ConvGeneralDilated operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#conv_convolution
  .

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      input tensor
    rhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      kernel tensor
    window_strides: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      inter-window strides
    padding: A `Tensor`. Must have the same type as `window_strides`.
      padding to apply at the start and end of each input dimensions
    lhs_dilation: A `Tensor`. Must have the same type as `window_strides`.
      dilation to apply between input elements
    rhs_dilation: A `Tensor`. Must have the same type as `window_strides`.
      dilation to apply between kernel elements
    feature_group_count: A `Tensor`. Must have the same type as `window_strides`.
      number of feature groups for grouped convolution.
    dimension_numbers: A `string`.
      serialized xla::ConvolutionDimensionNumbers proto.
    precision_config: A `string`. serialized xla::PrecisionConfig proto.
    preferred_element_type: A `tf.DType` from: `tf.float32, tf.float64, tf.int32, tf.uint8, tf.int16, tf.int8, tf.complex64, tf.int64, tf.qint8, tf.quint8, tf.qint32, tf.bfloat16, tf.qint16, tf.quint16, tf.uint16, tf.complex128, tf.half, tf.uint32, tf.uint64`.
      type of the tensor.
    batch_group_count: An optional `int`. Defaults to `1`.
      number of batch groups or grouped filters.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `preferred_element_type`.
  """

XlaConvV2: Incomplete

def xla_conv_v2_eager_fallback(lhs, rhs, window_strides, padding, lhs_dilation, rhs_dilation, feature_group_count, dimension_numbers, precision_config, preferred_element_type, batch_group_count, name, ctx): ...
def xla_custom_call(args, target_name, backend_config, dtype, shape, name: Incomplete | None = None):
    """Wraps the XLA CustomCall operator

    documented at https://www.tensorflow.org/xla/operation_semantics#customcall.

  Args:
    args: A list of `Tensor` objects.
      A list of `Tensor` with possibly different types.
    target_name: A `string`.
      Name of the function. A call instruction will be emitted which
      targets this symbol name.
    backend_config: A `string`.
      String, used to encode serialized metadata to the backend.
    dtype: A `tf.DType`. Output tensor data type.
    shape: A `tf.TensorShape` or list of `ints`. Output tensor shape.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`.
  """

XlaCustomCall: Incomplete

def xla_custom_call_eager_fallback(args, target_name, backend_config, dtype, shape, name, ctx): ...
def xla_custom_call_v2(operands, call_target_name, backend_config, has_side_effect, result_dtypes, result_shapes, name: Incomplete | None = None):
    """Emits an HLO `CustomCall` operation with multiple outputs.

  As opposed to `XlaCustomCall`, this operation supports multiple outputs.

  See `CustomCall` specification at
    https://tensorflow.org/xla/operation_semantics#customcall,
  and `mhlo.custom_call` specification at
    https://tensorflow.org/mlir/hlo_ops#mhlocustom_call_mlirmhlocustomcallop.

  Args:
    operands: A list of `Tensor` objects.
      A sequence of tensors with possibly different types.
    call_target_name: A `string`.
      Name of the user function. The function signature must conform
      to version 3 of the API, see `API_VERSION_STATUS_RETURNING_UNIFIED`. All
      operands and results assumed to be in the default layout.
    backend_config: A `string`.
      A string that encodes a metadata for the backend.
    has_side_effect: A `bool`.
      Indicates whether the custom call has side effects.
    result_dtypes: A list of `tf.DTypes`. Types of all results.
    result_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      Shapes of all results.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `result_dtypes`.
  """

XlaCustomCallV2: Incomplete

def xla_custom_call_v2_eager_fallback(operands, call_target_name, backend_config, has_side_effect, result_dtypes, result_shapes, name, ctx): ...
def xla_dequantize(input, min_range, max_range, mode, transpose_output, name: Incomplete | None = None):
    '''Takes the packed uint32 input and unpacks the input to uint8 to do

  Dequantization on device.

  Args:
    input: A `Tensor` of type `uint32`.
      Input tensors whose types is uint32, shape is [d0, ..., dn].
    min_range: A `float`.
      The minimum scalar value possibly produced for the input.
    max_range: A `float`.
      The maximum scalar value possibly produced for the input.
    mode: A `string`.
      String to determine the dequantize mode in {"MIN_COMBINED", "MIN_FIRST", "SCALED"}.
    transpose_output: A `bool`.
      Boolean to determine if output is transposed. transpose_output
      is faster when input is large and rank of input is higher than 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bfloat16`.
    Output tensors whose types is bfloat16. If transpose_output is true,
    output shape is [dn * 4, dn-1, ..., d1, d0]. If transpose_output
    is false, output shape is [d0,..., dn * 4].
  '''

XlaDequantize: Incomplete

def xla_dequantize_eager_fallback(input, min_range, max_range, mode, transpose_output, name, ctx): ...
def xla_dot(lhs, rhs, dimension_numbers, precision_config, name: Incomplete | None = None):
    """Wraps the XLA DotGeneral operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#dotgeneral
  .

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the LHS tensor
    rhs: A `Tensor`. Must have the same type as `lhs`. the RHS tensor
    dimension_numbers: A `string`.
      a serialized xla::DotDimensionNumbers proto.
    precision_config: A `string`. a serialized xla::PrecisionConfig proto.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `lhs`.
  """

XlaDot: Incomplete

def xla_dot_eager_fallback(lhs, rhs, dimension_numbers, precision_config, name, ctx): ...
def xla_dot_v2(lhs, rhs, dimension_numbers, precision_config, preferred_element_type, name: Incomplete | None = None):
    """Wraps the XLA DotGeneral operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#dotgeneral
  .

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the LHS tensor
    rhs: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the RHS tensor
    dimension_numbers: A `string`.
      a serialized xla::DotDimensionNumbers proto.
    precision_config: A `string`. a serialized xla::PrecisionConfig proto.
    preferred_element_type: A `tf.DType` from: `tf.float32, tf.float64, tf.int32, tf.uint8, tf.int16, tf.int8, tf.complex64, tf.int64, tf.qint8, tf.quint8, tf.qint32, tf.bfloat16, tf.qint16, tf.quint16, tf.uint16, tf.complex128, tf.half, tf.uint32, tf.uint64`.
      The type of the tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `preferred_element_type`.
  """

XlaDotV2: Incomplete

def xla_dot_v2_eager_fallback(lhs, rhs, dimension_numbers, precision_config, preferred_element_type, name, ctx): ...
def xla_dynamic_slice(input, start_indices, size_indices, name: Incomplete | None = None):
    """Wraps the XLA DynamicSlice operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#dynamicslice
  .

  DynamicSlice extracts a sub-array from the input array at dynamic
  start_indices. The size of the slice in each dimension is passed in
  size_indices, which specify the end point of exclusive slice intervals in each
  dimension -- [start, start + size). The shape of start_indices must have rank 1,
  with dimension size equal to the rank of operand.

  Args:
    input: A `Tensor`. A `Tensor` of type T.
    start_indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      List of N integers containing the slice size for each
      dimension. Each value must be strictly greater than zero, and start + size
      must be less than or equal to the size of the dimension to avoid
      implementation defined behavior.
    size_indices: A `Tensor`. Must have the same type as `start_indices`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaDynamicSlice: Incomplete

def xla_dynamic_slice_eager_fallback(input, start_indices, size_indices, name, ctx): ...
def xla_dynamic_update_slice(input, update, indices, name: Incomplete | None = None):
    """Wraps the XLA DynamicUpdateSlice operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#dynamicupdateslice
  .

  XlaDynamicUpdateSlice generates a result which is the value of the `input`
  operand, with a slice update overwritten at `indices`. The shape of `update`
  determines the shape of the sub-array of the result which is updated. The shape
  of indices must be rank == 1, with dimension size equal to the rank of `input`.

  Handling of out-of-bounds slice indices is implementation-defined.

  Args:
    input: A `Tensor`. A `Tensor` of type T.
    update: A `Tensor`. Must have the same type as `input`.
      A `Tensor` of type T. Same rank as `input`.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A vector of indices into `input`. Must have length equal to the rank of
      `input`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`. A `Tensor` of type T.
  """

XlaDynamicUpdateSlice: Incomplete

def xla_dynamic_update_slice_eager_fallback(input, update, indices, name, ctx): ...
def xla_einsum(a, b, equation, name: Incomplete | None = None):
    """An op which supports basic einsum op with 2 inputs and 1 output.

  This op has better TPU performance since it doesn't have explicitly reshape and
  transpose operations as tf.einsum does.

  Args:
    a: A `Tensor`. Must be one of the following types: `complex64`, `bfloat16`, `float32`.
    b: A `Tensor`. Must have the same type as `a`.
    equation: A `string`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `a`.
  """

XlaEinsum: Incomplete

def xla_einsum_eager_fallback(a, b, equation, name, ctx): ...
def xla_gather(operand, start_indices, slice_sizes, dimension_numbers, indices_are_sorted, name: Incomplete | None = None):
    """Wraps the XLA Gather operator documented at

    https://www.tensorflow.org/xla/operation_semantics#gather

  Args:
    operand: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
      The array we're gathering from.
    start_indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Array containing the starting indices of the slices we gather.
    slice_sizes: A `Tensor`. Must have the same type as `start_indices`.
      slice_sizes[i] is the bounds for the slice on dimension i.
    dimension_numbers: A `string`.
      A serialized xla::GatherDimensionNumbers proto.
    indices_are_sorted: A `bool`.
      Boolean indicating if the indices are sorted.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `operand`.
  """

XlaGather: Incomplete

def xla_gather_eager_fallback(operand, start_indices, slice_sizes, dimension_numbers, indices_are_sorted, name, ctx): ...
def xla_if(cond, inputs, then_branch, else_branch, Tout, name: Incomplete | None = None):
    """output = cond ? then_branch(inputs) : else_branch(inputs).

  Args:
    cond: A `Tensor`. A boolean scalar.
    inputs: A list of `Tensor` objects. A list of input tensors.
    then_branch: A function decorated with @Defun.
      A function takes 'inputs' and returns a list of tensors,
      whose types are the same as what else_branch returns.
    else_branch: A function decorated with @Defun.
      A function takes 'inputs' and returns a list of tensors.
      whose types are the same as what then_branch returns.
    Tout: A list of `tf.DTypes`.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects of type `Tout`.
    A list of tensors returned by either then_branch(inputs) or
    else_branch(inputs). The input shapes of the then_branch and
    else_branch must match.
  """

XlaIf: Incomplete

def xla_if_eager_fallback(cond, inputs, then_branch, else_branch, Tout, name, ctx): ...

class _XlaKeyValueSortOutput(NamedTuple):
    sorted_keys: Incomplete
    sorted_values: Incomplete

def xla_key_value_sort(keys, values, name: Incomplete | None = None):
    """Wraps the XLA Sort operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#sort
  .

  Sorts a tensor. Currently only sorts in ascending order are supported.

  Args:
    keys: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
      A `Tensor` of type K.
    values: A `Tensor`. A `Tensor` of type V.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sorted_keys, sorted_values).

    sorted_keys: A `Tensor`. Has the same type as `keys`. A `Tensor` of type K.
    sorted_values: A `Tensor`. Has the same type as `values`. A `Tensor` of type V.
  """

XlaKeyValueSort: Incomplete

def xla_key_value_sort_eager_fallback(keys, values, name, ctx): ...
def xla_optimization_barrier(input, name: Incomplete | None = None):
    """Wraps the XLA OptimizationBarrier operator.

  Documented at https://www.tensorflow.org/xla/operation_semantics#optimizationbarrier.

  Args:
    input: A list of `Tensor` objects. A Tuple of Arrays of any type.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `input`.
  """

XlaOptimizationBarrier: Incomplete

def xla_optimization_barrier_eager_fallback(input, name, ctx): ...
def xla_pad(input, padding_value, padding_low, padding_high, padding_interior, name: Incomplete | None = None):
    """Wraps the XLA Pad operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#pad
  .

  Args:
    input: A `Tensor`. A `Tensor` of type T.
    padding_value: A `Tensor`. Must have the same type as `input`.
      A scalar `Tensor` of type T.
    padding_low: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      the padding to apply at the start of each input dimensions. Must
      be a compile-time constant 1D tensor of length equal to rank of input.
    padding_high: A `Tensor`. Must have the same type as `padding_low`.
      the padding to apply at the end of each input dimension. Must
      be a compile-time constant 1D tensor of length equal to rank of input.
    padding_interior: A `Tensor`. Must have the same type as `padding_low`.
      the padding to apply between each input element. Must
      be a compile-time constant 1D tensor of length equal to rank of input,
      containing only non-negative values.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`. A `Tensor` of type T.
  """

XlaPad: Incomplete

def xla_pad_eager_fallback(input, padding_value, padding_low, padding_high, padding_interior, name, ctx): ...
def xla_recv(dtype, tensor_name, shape, name: Incomplete | None = None):
    """Receives the named tensor from another XLA computation. Wraps the XLA Recv

  operator documented at
   https://www.tensorflow.org/performance/xla/operation_semantics#recv .

  Args:
    dtype: A `tf.DType`. The type of the tensor.
    tensor_name: A `string`. A string key that identifies the channel.
    shape: A `tf.TensorShape` or list of `ints`. The shape of the tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `dtype`. The tensor to receive.
  """

XlaRecv: Incomplete

def xla_recv_eager_fallback(dtype, tensor_name, shape, name, ctx): ...
def xla_reduce(input, init_value, dimensions_to_reduce, reducer, name: Incomplete | None = None):
    """Wraps the XLA Reduce operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#reduce .

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
      the input tensor
    init_value: A `Tensor`. Must have the same type as `input`.
      a scalar representing the initial value for the reduction
    dimensions_to_reduce: A list of `ints`.
      dimension numbers over which to reduce
    reducer: A function decorated with @Defun. a reducer function to apply
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaReduce: Incomplete

def xla_reduce_eager_fallback(input, init_value, dimensions_to_reduce, reducer, name, ctx): ...
def xla_reduce_precision(operand, exponent_bits, mantissa_bits, name: Incomplete | None = None):
    """Wraps the XLA ReducePrecision operator

    documented at https://www.tensorflow.org/xla/operation_semantics#reduceprecision.

  Args:
    operand: A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`.
      array of floating-point type.
    exponent_bits: An `int`. number of exponent bits in lower-precision format
    mantissa_bits: An `int`. number of mantissa bits in lower-precision format
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `operand`.
  """

XlaReducePrecision: Incomplete

def xla_reduce_precision_eager_fallback(operand, exponent_bits, mantissa_bits, name, ctx): ...
def xla_reduce_scatter(input, group_assignment, scatter_dimension, reduce_op, name: Incomplete | None = None):
    '''Wraps the XLA ReduceScatter operator

    documented at https://www.tensorflow.org/xla/operation_semantics#reducescatter.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`, `int32`, `uint32`.
      Array or a non-empty tuple of arrays to reduce across replicas.
    group_assignment: A `Tensor` of type `int32`.
      Groups between which the reductions are performed.
    scatter_dimension: A `Tensor` of type `int32`. Dimension to scatter.
    reduce_op: A `string` from: `"Min", "Max", "Mul", "Add", "Mean"`.
      Reduction computation.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

XlaReduceScatter: Incomplete

def xla_reduce_scatter_eager_fallback(input, group_assignment, scatter_dimension, reduce_op, name, ctx): ...
def xla_reduce_window(input, init_value, window_dimensions, window_strides, base_dilations, window_dilations, padding, computation, name: Incomplete | None = None):
    """Wraps the XLA ReduceWindow operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#reducewindow .

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
      the input tensor
    init_value: A `Tensor`. Must have the same type as `input`.
      a scalar representing the initial value for the reduction
    window_dimensions: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      the shape of the window
    window_strides: A `Tensor`. Must have the same type as `window_dimensions`.
      the inter-window strides
    base_dilations: A `Tensor`. Must have the same type as `window_dimensions`.
    window_dilations: A `Tensor`. Must have the same type as `window_dimensions`.
    padding: A `Tensor`. Must have the same type as `window_dimensions`.
      the padding to apply at the start and end of each input dimensions
    computation: A function decorated with @Defun. a reducer function to apply
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaReduceWindow: Incomplete

def xla_reduce_window_eager_fallback(input, init_value, window_dimensions, window_strides, base_dilations, window_dilations, padding, computation, name, ctx): ...
def xla_remove_dynamic_dimension_size(input, dim_index, name: Incomplete | None = None):
    """Inverse of XlaSetDynamicDimensionSize.

  Make an xla bounded dynamic dimension into a static dimension. The bound of the
  size of dimension `dim_index` becomes the static dimension size.

  Args:
    input: A `Tensor`.
    dim_index: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaRemoveDynamicDimensionSize: Incomplete

def xla_remove_dynamic_dimension_size_eager_fallback(input, dim_index, name, ctx): ...
def xla_replica_id(name: Incomplete | None = None):
    """Replica ID.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

XlaReplicaId: Incomplete

def xla_replica_id_eager_fallback(name, ctx): ...

class _XlaRngBitGeneratorOutput(NamedTuple):
    output_key: Incomplete
    output: Incomplete

def xla_rng_bit_generator(algorithm, initial_state, shape, dtype=..., name: Incomplete | None = None):
    """Stateless PRNG bit generator.

  Wraps the XLA RngBitGenerator operator, documented at
   https://www.tensorflow.org/performance/xla/operation_semantics#rngbitgenerator.

  Args:
    algorithm: A `Tensor` of type `int32`. The PRNG algorithm to use, one of
      tf.random.Algorithm.{PHILOX, THREEFRY, AUTO_SELECT}.
    initial_state: A `Tensor` of type `uint64`.
      Initial state for the PRNG algorithm. For THREEFRY, it should be
      a u64[2] and for PHILOX a u64[3].
    shape: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      The output shape of the generated data.
    dtype: An optional `tf.DType` from: `tf.int32, tf.int64, tf.uint32, tf.uint64`. Defaults to `tf.uint64`.
      The type of the tensor.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_key, output).

    output_key: A `Tensor` of type `uint64`.
    output: A `Tensor` of type `dtype`.
  """

XlaRngBitGenerator: Incomplete

def xla_rng_bit_generator_eager_fallback(algorithm, initial_state, shape, dtype, name, ctx): ...
def xla_scatter(operand, scatter_indices, updates, update_computation, dimension_numbers, indices_are_sorted, name: Incomplete | None = None):
    """Wraps the XLA Scatter operator documented at

    https://www.tensorflow.org/xla/operation_semantics#scatter.

  Args:
    operand: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
      Array to be scattered into.
    scatter_indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      Array containing the starting indices of the slices that must
      be scattered to.
    updates: A `Tensor`. Must have the same type as `operand`.
      Array containing the values that must be used for scattering.
    update_computation: A function decorated with @Defun.
      Computation to be used for combining the existing values in
      the input array and the updates during scatter.
    dimension_numbers: A `string`.
      A serialized xla::ScatterDimensionNumbers proto.
    indices_are_sorted: A `bool`.
      Boolean indicating if the indices are sorted.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `operand`.
  """

XlaScatter: Incomplete

def xla_scatter_eager_fallback(operand, scatter_indices, updates, update_computation, dimension_numbers, indices_are_sorted, name, ctx): ...
def xla_select_and_scatter(operand, window_dimensions, window_strides, padding, source, init_value, select, scatter, name: Incomplete | None = None):
    """Wraps the XLA SelectAndScatter operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#selectandscatter
  .

  Args:
    operand: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the input tensor
    window_dimensions: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      the shape of the window
    window_strides: A `Tensor`. Must have the same type as `window_dimensions`.
      the inter-window strides
    padding: A `Tensor`. Must have the same type as `window_dimensions`.
      the padding to apply at the start and end of each input dimensions
    source: A `Tensor`. Must have the same type as `operand`.
      a tensor of values to scatter
    init_value: A `Tensor`. Must have the same type as `operand`.
      a scalar representing the initial value for the output tensor
    select: A function decorated with @Defun. a selection function to apply
    scatter: A function decorated with @Defun. a scatter function to apply
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `operand`.
  """

XlaSelectAndScatter: Incomplete

def xla_select_and_scatter_eager_fallback(operand, window_dimensions, window_strides, padding, source, init_value, select, scatter, name, ctx): ...

class _XlaSelfAdjointEigOutput(NamedTuple):
    w: Incomplete
    v: Incomplete

def xla_self_adjoint_eig(a, lower, max_iter, epsilon, name: Incomplete | None = None):
    '''Computes the eigen decomposition of a batch of self-adjoint matrices

  (Note: Only real inputs are supported).

  Computes the eigenvalues and eigenvectors of the innermost N-by-N matrices in
  tensor such that tensor[...,:,:] * v[..., :,i] = e[..., i] * v[...,:,i], for
  i=0...N-1.

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the input tensor.
    lower: A `bool`.
      a boolean specifies whether the calculation is done with the lower
      triangular part or the upper triangular part.
    max_iter: An `int`.
      maximum number of sweep update, i.e., the whole lower triangular
      part or upper triangular part based on parameter lower. Heuristically, it has
      been argued that approximately logN sweeps are needed in practice (Ref: Golub &
      van Loan "Matrix Computation").
    epsilon: A `float`. the tolerance ratio.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (w, v).

    w: A `Tensor`. Has the same type as `a`. The eigenvalues in ascending order, each repeated according to its
      multiplicity.
    v: A `Tensor`. Has the same type as `a`. The column v[..., :, i] is the normalized eigenvector corresponding to the
      eigenvalue w[..., i].
  '''

XlaSelfAdjointEig: Incomplete

def xla_self_adjoint_eig_eager_fallback(a, lower, max_iter, epsilon, name, ctx): ...
def xla_send(tensor, tensor_name, name: Incomplete | None = None):
    """Sends the named tensor to another XLA computation. Wraps the XLA Send operator

  documented at
   https://www.tensorflow.org/performance/xla/operation_semantics#send .

  Args:
    tensor: A `Tensor`. The tensor to send.
    tensor_name: A `string`. A string key that identifies the channel.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

XlaSend: Incomplete

def xla_send_eager_fallback(tensor, tensor_name, name, ctx): ...
def xla_set_bound(input, bound, name: Incomplete | None = None):
    """Set a bound for the given input value as a hint to Xla compiler,

          returns the same value.

  Args:
    input: A `Tensor` of type `int32`.
    bound: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int32`.
  """

XlaSetBound: Incomplete

def xla_set_bound_eager_fallback(input, bound, name, ctx): ...
def xla_set_dynamic_dimension_size(input, dim_index, size, name: Incomplete | None = None):
    """Make a static dimension into a xla bounded dynamic dimension.

          The current static dimension size will become the bound and the second
          operand becomes the dynamic size of the dimension.

  Args:
    input: A `Tensor`.
    dim_index: A `Tensor` of type `int32`.
    size: A `Tensor` of type `int32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaSetDynamicDimensionSize: Incomplete

def xla_set_dynamic_dimension_size_eager_fallback(input, dim_index, size, name, ctx): ...
def xla_sharding(input, sharding: str = '', unspecified_dims=[], name: Incomplete | None = None):
    '''An op which shards the input based on the given sharding attribute. It can

  selectively annotate a subset of tensor dimensions by skipping unspecified_dims,
  and the sharding annotation should be replicated in those dims.

  Args:
    input: A `Tensor`.
    sharding: An optional `string`. Defaults to `""`.
    unspecified_dims: An optional list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

XlaSharding: Incomplete

def xla_sharding_eager_fallback(input, sharding, unspecified_dims, name, ctx): ...
def xla_sort(input, name: Incomplete | None = None):
    """Wraps the XLA Sort operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#sort
  .

  Sorts a tensor. Currently only sorts in ascending order are supported.

  Args:
    input: A `Tensor`. A `Tensor` of type T.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`. A `Tensor` of type T.
  """

XlaSort: Incomplete

def xla_sort_eager_fallback(input, name, ctx): ...
def xla_spmd_full_to_shard_shape(input, manual_sharding, dim: int = -1, unspecified_dims=[], name: Incomplete | None = None):
    """An op used by XLA SPMD partitioner to switch from automatic partitioning to

  manual partitioning. It annotates the input (full-shape, to be automatically
  partitioned) with the same sharding used by manual partitioning, and outputs a
  shard-shaped tensor to be consumed by later manually-partitioned ops. If the
  shape is not evenly partitionable, the padding region will be masked with 0s.
  The conversion can happen partially in subgroups, by specifying the dim
  attribute, where only that dim will be converted.

  Args:
    input: A `Tensor`.
    manual_sharding: A `string`.
    dim: An optional `int`. Defaults to `-1`.
    unspecified_dims: An optional list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaSpmdFullToShardShape: Incomplete

def xla_spmd_full_to_shard_shape_eager_fallback(input, manual_sharding, dim, unspecified_dims, name, ctx): ...
def xla_spmd_shard_to_full_shape(input, manual_sharding, full_shape, dim: int = -1, unspecified_dims=[], name: Incomplete | None = None):
    """An op used by XLA SPMD partitioner to switch from manual partitioning to

  automatic partitioning. It converts the shard-shaped, manually partitioned input
  into full-shaped tensor to be partitioned automatically with the same sharding
  used by manual partitioning. The conversion can happen partially in subgroups,
  by specifying the dim attribute, where only that dim will be converted.

  Args:
    input: A `Tensor`.
    manual_sharding: A `string`.
    full_shape: A `tf.TensorShape` or list of `ints`.
    dim: An optional `int`. Defaults to `-1`.
    unspecified_dims: An optional list of `ints`. Defaults to `[]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """

XlaSpmdShardToFullShape: Incomplete

def xla_spmd_shard_to_full_shape_eager_fallback(input, manual_sharding, full_shape, dim, unspecified_dims, name, ctx): ...

class _XlaSvdOutput(NamedTuple):
    s: Incomplete
    u: Incomplete
    v: Incomplete

def xla_svd(a, max_iter, epsilon, precision_config, name: Incomplete | None = None):
    '''Computes the eigen decomposition of a batch of self-adjoint matrices

  (Note: Only real inputs are supported).

  Computes the eigenvalues and eigenvectors of the innermost M-by-N matrices in
  tensor such that tensor[...,:,:] = u[..., :, :] * Diag(s[..., :]) * Transpose(v[...,:,:]).

  Args:
    a: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`.
      the input tensor.
    max_iter: An `int`.
      maximum number of sweep update, i.e., the whole lower triangular
      part or upper triangular part based on parameter lower. Heuristically, it has
      been argued that approximately log(min (M, N)) sweeps are needed in practice
      (Ref: Golub & van Loan "Matrix Computation").
    epsilon: A `float`. the tolerance ratio.
    precision_config: A `string`. a serialized xla::PrecisionConfig proto.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (s, u, v).

    s: A `Tensor`. Has the same type as `a`. Singular values. The values are sorted in reverse order of magnitude, so
      s[..., 0] is the largest value, s[..., 1] is the second largest, etc.
    u: A `Tensor`. Has the same type as `a`. Left singular vectors.
    v: A `Tensor`. Has the same type as `a`. Right singular vectors.
  '''

XlaSvd: Incomplete

def xla_svd_eager_fallback(a, max_iter, epsilon, precision_config, name, ctx): ...
def xla_variadic_reduce(input, init_value, dimensions_to_reduce, reducer, name: Incomplete | None = None):
    """Wraps the variadic XLA Reduce operator.

  Semantics are documented at
   https://www.tensorflow.org/performance/xla/operation_semantics#variadic_reduce.

  This version is limited to operands of the same dtype.
  XlaVariadicReduceV2 is a version that supports heterogeneous operands.

  Args:
    input: A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `complex64`, `int64`, `qint8`, `quint8`, `qint32`, `bfloat16`, `qint16`, `quint16`, `uint16`, `complex128`, `half`, `uint32`, `uint64`, `bool`.
      the input tensor(s)
    init_value: A list with the same length as `input` of `Tensor` objects with the same type as `input`.
      scalar initial value(s) for the reduction
    dimensions_to_reduce: A list of `ints`.
      dimension numbers over which to reduce
    reducer: A function decorated with @Defun. a reducer function to apply
    name: A name for the operation (optional).

  Returns:
    A list with the same length as `input` of `Tensor` objects with the same type as `input`.
  """

XlaVariadicReduce: Incomplete

def xla_variadic_reduce_eager_fallback(input, init_value, dimensions_to_reduce, reducer, name, ctx): ...
def xla_variadic_reduce_v2(inputs, init_values, dimensions_to_reduce, reducer, name: Incomplete | None = None):
    """Wraps the variadic XLA Reduce operator.

  Semantics are documented at
   https://www.tensorflow.org/performance/xla/operation_semantics#variadic_reduce.

  This is an expanded version of XlaVariadicReduce, with support for
  operands of different dtypes, and improved shape inference.

  Args:
    inputs: A list of `Tensor` objects. the input tensor(s)
    init_values: A list of `Tensor` objects. Must have the same type as `inputs`.
      scalar initial value(s) for the reduction
    dimensions_to_reduce: A list of `ints`.
      dimension numbers over which to reduce
    reducer: A function decorated with @Defun. a reducer function to apply
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `inputs`.
  """

XlaVariadicReduceV2: Incomplete

def xla_variadic_reduce_v2_eager_fallback(inputs, init_values, dimensions_to_reduce, reducer, name, ctx): ...
def xla_variadic_sort(inputs, dimension, comparator, is_stable, name: Incomplete | None = None):
    """Wraps the XLA Sort operator, documented at

   https://www.tensorflow.org/performance/xla/operation_semantics#sort
  .

  Sorts one or more tensors, with support for custom comparator, dimension, and
  is_stable attributes.

  Args:
    inputs: A list of `Tensor` objects.
      A list of `Tensor` of identical shape but possibly different types.
    dimension: A `Tensor` of type `int32`.
      The dimension along which to sort. Must be a compile-time constant.
    comparator: A function decorated with @Defun.
      A comparator function to apply to 2*N scalars and returning a
      boolean. N is the number of sort inputs. If you want to sort in ascending
      order then the comparator should perform a less-than comparison.
    is_stable: A `bool`. Whether to use stable sort.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `inputs`.
    A list of `Tensor` of same shape and types as the `input`.
  """

XlaVariadicSort: Incomplete

def xla_variadic_sort_eager_fallback(inputs, dimension, comparator, is_stable, name, ctx): ...
def xla_while(input, cond, body, name: Incomplete | None = None):
    """output = input; While (Cond(output)) { output = Body(output) }

  Args:
    input: A list of `Tensor` objects.
      A list of input tensors whose types are T.
    cond: A function decorated with @Defun.
      A function takes 'input' and returns a tensor.  If the tensor is
      a scalar of non-boolean, the scalar is converted to a boolean
      according to the following rule: if the scalar is a numerical
      value, non-zero means True and zero means False; if the scalar is
      a string, non-empty means True and empty means False. If the
      tensor is not a scalar, non-emptiness means True and False
      otherwise.
    body: A function decorated with @Defun.
      A function that takes a list of tensors and returns another
      list of tensors. Both lists have the same types as specified by T.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `input`.
    A list of output tensors whose types are T.
  """

XlaWhile: Incomplete

def xla_while_eager_fallback(input, cond, body, name, ctx): ...
