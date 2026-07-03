from _typeshed import Incomplete
from tensorflow.compiler.tf2xla.ops import gen_xla_ops as gen_xla_ops
from tensorflow.compiler.xla import xla_data_pb2 as xla_data_pb2
from tensorflow.core.framework import attr_value_pb2 as attr_value_pb2
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, bitwise_ops as bitwise_ops, gen_math_ops as gen_math_ops, gen_random_ops as gen_random_ops, math_ops as math_ops, random_ops as random_ops, special_math_ops as special_math_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.ops.numpy_ops import np_utils as np_utils

constant = constant_op.constant
abs: Incomplete
conj: Incomplete
cos: Incomplete
ceil: Incomplete
digamma: Incomplete
erf: Incomplete
erfc: Incomplete
erfinv: Incomplete
ndtri: Incomplete
exp: Incomplete
expm1: Incomplete
floor: Incomplete
imag: Incomplete
is_finite: Incomplete
lgamma: Incomplete
log: Incomplete
log1p: Incomplete
logical_not: Incomplete
neg: Incomplete
real: Incomplete
round: Incomplete
sin: Incomplete
sign: Incomplete
tan: Incomplete
tanh: Incomplete
bessel_i0e: Incomplete
bessel_i1e: Incomplete
add: Incomplete
sub: Incomplete
mul: Incomplete
div: Incomplete
rem: Incomplete
max: Incomplete
min: Incomplete
atan2: Incomplete
complex: Incomplete
logical_and: Incomplete
logical_or: Incomplete
logical_xor: Incomplete
eq: Incomplete
ne: Incomplete
ge: Incomplete
gt: Incomplete
le: Incomplete
lt: Incomplete
pow: Incomplete
shift_left: Incomplete
shift_right_logical: Incomplete
shift_right_arithmetic: Incomplete
igamma: Incomplete
igamma_grad_a: Incomplete
random_gamma_grad: Incomplete
igammac: Incomplete
polygamma: Incomplete
zeta: Incomplete
transpose: Incomplete
rev: Incomplete
bitcast_convert_type = array_ops.bitcast

def broadcast(x, dims, name: Incomplete | None = None): ...
def clamp(a, x, b, name: Incomplete | None = None): ...
concatenate = array_ops.concat

def conv(lhs, rhs, window_strides, padding, lhs_dilation, rhs_dilation, dimension_numbers, feature_group_count: int = 1, precision_config: Incomplete | None = None, preferred_element_type: Incomplete | None = None, name: Incomplete | None = None, use_v2: bool = False, batch_group_count: int = 1):
    """Wraps the XLA ConvGeneralDilated operator.

  ConvGeneralDilated is the most general form of XLA convolution and is
  documented at
  https://www.tensorflow.org/performance/xla/operation_semantics#conv_convolution

  Args:
    lhs: the input tensor
    rhs: the kernel tensor
    window_strides: the inter-window strides
    padding: the padding to apply at the start and end of each input dimensions
    lhs_dilation: dilation to apply between input elements
    rhs_dilation: dilation to apply between kernel elements
    dimension_numbers: a `ConvolutionDimensionNumbers` proto.
    feature_group_count: number of feature groups for grouped convolution.
    precision_config: a `xla.PrecisionConfig` proto.
    preferred_element_type: the result `dtype`.
    name: an optional name for the operator.
    use_v2: an optional request to use the XlaConvV2 op even if not necessary.
    batch_group_count: number of batch groups or grouped filters.

  Returns:
    A tensor representing the output of the convolution.
  """
convert_element_type = math_ops.cast

def dot(lhs, rhs, name: Incomplete | None = None): ...

DotDimensionNumbers: Incomplete
PrecisionConfig: Incomplete

def dot_general(lhs, rhs, dimension_numbers, precision_config: Incomplete | None = None, preferred_element_type: Incomplete | None = None, name: Incomplete | None = None, use_v2: bool = False): ...
def self_adjoint_eig(a, lower, max_iter, epsilon): ...
def svd(a, max_iter, epsilon, precision_config: Incomplete | None = None): ...
dynamic_slice = gen_xla_ops.xla_dynamic_slice
dynamic_update_slice = gen_xla_ops.xla_dynamic_update_slice
einsum = gen_xla_ops.xla_einsum
pad = gen_xla_ops.xla_pad

def random_normal(mu, sigma, dims, name: Incomplete | None = None): ...
def random_uniform(minval, maxval, dims, name: Incomplete | None = None): ...
def rng_bit_generator(algorithm, initial_state, shape, dtype):
    """Stateless PRNG bit generator.

  Wraps the XLA RngBitGenerator operator, documented at
    https://www.tensorflow.org/performance/xla/operation_semantics#rngbitgenerator.

  Args:
    algorithm: The PRNG algorithm to use, one of tf.random.Algorithm.{PHILOX,
      THREEFRY, AUTO_SELECT}.
    initial_state: Initial state for the PRNG algorithm. For THREEFRY, it should
      be a u64[2] and for PHILOX a u64[3].
    shape: The output shape of the generated data.
    dtype: The type of the tensor.

  Returns:
    a tuple with a new state and generated data of the given shape.
  """
recv = gen_xla_ops.xla_recv
reduce = gen_xla_ops.xla_reduce
variadic_reduce = gen_xla_ops.xla_variadic_reduce_v2

def reduce_window(operand, init, reducer, window_dimensions, window_strides: Incomplete | None = None, base_dilations: Incomplete | None = None, window_dilations: Incomplete | None = None, padding: Incomplete | None = None, name: Incomplete | None = None):
    """Wraps the XLA ReduceWindow operator.

  ReduceWindow is documented at
  https://www.tensorflow.org/performance/xla/operation_semantics#reducewindow .

  Args:
    operand: the input tensor
    init: a scalar tensor representing the initial value for the reduction
    reducer: a reduction function that combines a pair of scalars.
    window_dimensions: shape of the window, as a list of integers
    window_strides: inter-window strides, as a list of integers. Optional; if
      omitted, defaults to strides of 1.
    padding: padding to apply to 'operand'. List of (low, high) pairs of
      integers that specify the padding to apply before and after each
      dimension. Optional; if omitted, defaults to no padding.
    name: the operator name, or None.

  Returns:
    A tensor that represents the output of the reduce_window operator.
  """
replica_id = gen_xla_ops.xla_replica_id
set_bound = gen_xla_ops.xla_set_bound
set_dynamic_dimension_size = gen_xla_ops.xla_set_dynamic_dimension_size
remove_dynamic_dimension_size = gen_xla_ops.xla_remove_dynamic_dimension_size

def reshape(x, new_sizes, dimensions: Incomplete | None = None, name: Incomplete | None = None): ...
def select(condition, x, y, name: Incomplete | None = None): ...
select_and_scatter = gen_xla_ops.xla_select_and_scatter
send = gen_xla_ops.xla_send

def slice(x, start_dims, limit_dims, strides): ...
sharding = gen_xla_ops.xla_sharding
spmd_full_to_shard_shape = gen_xla_ops.xla_spmd_full_to_shard_shape
spmd_shard_to_full_shape = gen_xla_ops.xla_spmd_shard_to_full_shape
sort = gen_xla_ops.xla_sort
key_value_sort = gen_xla_ops.xla_key_value_sort
variadic_sort = gen_xla_ops.xla_variadic_sort
while_loop = gen_xla_ops.xla_while
dequantize = gen_xla_ops.xla_dequantize
custom_call = gen_xla_ops.xla_custom_call

def custom_call_v2(call_target_name, operands, result_specs, backend_config: Incomplete | None = None, has_side_effect: Incomplete | None = None, name: Incomplete | None = None):
    """Emits an HLO `CustomCall` operation with multiple outputs.

  See `CustomCall` specification at
    https://tensorflow.org/xla/operation_semantics#customcall,
  and `mhlo.custom_call` specification at
    https://tensorflow.org/mlir/hlo_ops#mhlocustom_call_mlirmhlocustomcallop.

  Args:
    call_target_name: Name of the user function. The function signature must
      conform to version 3 of the API, see
      `API_VERSION_STATUS_RETURNING_UNIFIED`. All operands and results assumed
      to be in the default layout.
    operands: A sequence of tensors with possibly different types.
    result_specs: A sequence of tensor specs for all results.
    backend_config: A string that encodes a metadata for the backend. Empty
      string by default.
    has_side_effect: Indicates whether the custom call has side effects. `False`
      by default.
    name: Optional name of the operation.

  Returns:
    A tuple of output tensors.
  """
def call_module(args, *, version: int = 2, module, Tout, Sout, dim_args_spec=()): ...
def gather(operand, start_indices, dimension_numbers, slice_sizes, indices_are_sorted: bool = False, name: Incomplete | None = None): ...
def scatter(operand, scatter_indices, updates, update_computation, dimension_numbers, indices_are_sorted: bool = False, name: Incomplete | None = None): ...
def optimization_barrier(*args): ...
def reduce_precision(operand, exponent_bits, mantissa_bits): ...
