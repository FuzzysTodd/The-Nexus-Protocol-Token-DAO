from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def copy(input, tensor_name: str = '', debug_ops_spec=[], name: Incomplete | None = None):
    '''Copy a tensor from CPU-to-CPU or GPU-to-GPU.

  Performs CPU-to-CPU or GPU-to-GPU deep-copying of tensor, depending on the
  device on which the tensor is allocated.
  N.B.: If the all downstream attached debug ops are disabled given the current
  gRPC gating status, the output will simply forward the input tensor without
  deep-copying. See the documentation of Debug* ops for more details.

  Unlike the CopyHost Op, this op does not have HostMemory constraint on its
  input or output.

  Args:
    input: A `Tensor`. Input tensor.
    tensor_name: An optional `string`. Defaults to `""`.
      The name of the input tensor.
    debug_ops_spec: An optional list of `strings`. Defaults to `[]`.
      A list of debug op spec (op, url, gated_grpc) for attached debug
      ops. Each element of the list has the format
      <debug_op>;<grpc_url>;<gated_grpc>, wherein gated_grpc is boolean represented
      as 0/1. E.g., "DebugIdentity;grpc://foo:3333;1",
      "DebugIdentity;file:///tmp/tfdbg_1;0".
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

Copy: Incomplete

def copy_eager_fallback(input, tensor_name, debug_ops_spec, name, ctx): ...
def copy_host(input, tensor_name: str = '', debug_ops_spec=[], name: Incomplete | None = None):
    '''Copy a tensor to host.

  Performs CPU-to-CPU deep-copying of tensor.
  N.B.: If the all downstream attached debug ops are disabled given the current
  gRPC gating status, the output will simply forward the input tensor without
  deep-copying. See the documentation of Debug* ops for more details.

  Unlike the Copy Op, this op has HostMemory constraint on its input or output.

  Args:
    input: A `Tensor`. Input tensor.
    tensor_name: An optional `string`. Defaults to `""`.
      The name of the input tensor.
    debug_ops_spec: An optional list of `strings`. Defaults to `[]`.
      A list of debug op spec (op, url, gated_grpc) for attached debug
      ops. Each element of the list has the format
      <debug_op>;<grpc_url>;<gated_grpc>, wherein gated_grpc is boolean represented
      as 0/1. E.g., "DebugIdentity;grpc://foo:3333;1",
      "DebugIdentity;file:///tmp/tfdbg_1;0".
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

CopyHost: Incomplete

def copy_host_eager_fallback(input, tensor_name, debug_ops_spec, name, ctx): ...
def debug_identity(input, device_name: str = '', tensor_name: str = '', debug_urls=[], gated_grpc: bool = False, name: Incomplete | None = None):
    '''Provides an identity mapping of the non-Ref type input tensor for debugging.

  Provides an identity mapping of the non-Ref type input tensor for debugging.

  Args:
    input: A `Tensor`. Input tensor, non-Reference type
    device_name: An optional `string`. Defaults to `""`.
      Name of the device on which the tensor resides.
    tensor_name: An optional `string`. Defaults to `""`.
      Name of the input tensor.
    debug_urls: An optional list of `strings`. Defaults to `[]`.
      List of URLs to debug targets, e.g.,
        file:///foo/tfdbg_dump, grpc:://localhost:11011
    gated_grpc: An optional `bool`. Defaults to `False`.
      Whether this op will be gated. If any of the debug_urls of this
        debug node is of the grpc:// scheme, when the value of this attribute is set
        to True, the data will not actually be sent via the grpc stream unless this
        debug op has been enabled at the debug_url. If all of the debug_urls of this
        debug node are of the grpc:// scheme and the debug op is enabled at none of
        them, the output will be an empty Tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

DebugIdentity: Incomplete

def debug_identity_eager_fallback(input, device_name, tensor_name, debug_urls, gated_grpc, name, ctx): ...
def debug_identity_v2(input, tfdbg_context_id: str = '', op_name: str = '', output_slot: int = -1, tensor_debug_mode: int = -1, debug_urls=[], circular_buffer_size: int = 1000, tfdbg_run_id: str = '', name: Incomplete | None = None):
    '''Debug Identity V2 Op.

  Provides an identity mapping from input to output, while writing the content of
  the input tensor by calling DebugEventsWriter.

  The semantics of the input tensor depends on tensor_debug_mode. In typical
  usage, the input tensor comes directly from the user computation only when
  graph_debug_mode is FULL_TENSOR (see protobuf/debug_event.proto for a
  list of all the possible values of graph_debug_mode). For the other debug modes,
  the input tensor should be produced by an additional op or subgraph that
  computes summary information about one or more tensors.

  Args:
    input: A `Tensor`. Input tensor, non-Reference type
    tfdbg_context_id: An optional `string`. Defaults to `""`.
      A tfdbg-generated ID for the context that the op belongs to,
        e.g., a concrete compiled tf.function.
    op_name: An optional `string`. Defaults to `""`.
      Optional. Name of the op that the debug op is concerned with.
        Used only for single-tensor trace.
    output_slot: An optional `int`. Defaults to `-1`.
      Optional. Output slot index of the tensor that the debug op
        is concerned with. Used only for single-tensor trace.
    tensor_debug_mode: An optional `int`. Defaults to `-1`.
      TensorDebugMode enum value. See debug_event.proto for details.
    debug_urls: An optional list of `strings`. Defaults to `[]`.
      List of URLs to debug targets, e.g., file:///foo/tfdbg_dump.
    circular_buffer_size: An optional `int`. Defaults to `1000`.
    tfdbg_run_id: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''

DebugIdentityV2: Incomplete

def debug_identity_v2_eager_fallback(input, tfdbg_context_id, op_name, output_slot, tensor_debug_mode, debug_urls, circular_buffer_size, tfdbg_run_id, name, ctx): ...
def debug_nan_count(input, device_name: str = '', tensor_name: str = '', debug_urls=[], gated_grpc: bool = False, name: Incomplete | None = None):
    '''Debug NaN Value Counter Op.

  Counts number of NaNs in the input tensor, for debugging.

  Args:
    input: A `Tensor`. Input tensor, non-Reference type.
    device_name: An optional `string`. Defaults to `""`.
    tensor_name: An optional `string`. Defaults to `""`.
      Name of the input tensor.
    debug_urls: An optional list of `strings`. Defaults to `[]`.
      List of URLs to debug targets, e.g.,
        file:///foo/tfdbg_dump, grpc:://localhost:11011.
    gated_grpc: An optional `bool`. Defaults to `False`.
       Whether this op will be gated. If any of the debug_urls of this
        debug node is of the grpc:// scheme, when the value of this attribute is set
        to True, the data will not actually be sent via the grpc stream unless this
        debug op has been enabled at the debug_url. If all of the debug_urls of this
        debug node are of the grpc:// scheme and the debug op is enabled at none of
        them, the output will be an empty Tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  '''

DebugNanCount: Incomplete

def debug_nan_count_eager_fallback(input, device_name, tensor_name, debug_urls, gated_grpc, name, ctx): ...
def debug_numeric_summary(input, device_name: str = '', tensor_name: str = '', debug_urls=[], lower_bound=..., upper_bound=..., mute_if_healthy: bool = False, gated_grpc: bool = False, name: Incomplete | None = None):
    '''Debug Numeric Summary Op.

  Provide a basic summary of numeric value types, range and distribution.

  output: A double tensor of shape [14 + nDimensions], where nDimensions is the
    number of dimensions of the tensor\'s shape. The elements of output are:
    [0]: is initialized (1.0) or not (0.0).
    [1]: total number of elements
    [2]: NaN element count
    [3]: generalized -inf count: elements <= lower_bound. lower_bound is -inf by
      default.
    [4]: negative element count (excluding -inf), if lower_bound is the default
      -inf. Otherwise, this is the count of elements > lower_bound and < 0.
    [5]: zero element count
    [6]: positive element count (excluding +inf), if upper_bound is the default
      +inf. Otherwise, this is the count of elements < upper_bound and > 0.
    [7]: generalized +inf count, elements >= upper_bound. upper_bound is +inf by
      default.
  Output elements [1:8] are all zero, if the tensor is uninitialized.
    [8]: minimum of all non-inf and non-NaN elements.
         If uninitialized or no such element exists: +inf.
    [9]: maximum of all non-inf and non-NaN elements.
         If uninitialized or no such element exists: -inf.
    [10]: mean of all non-inf and non-NaN elements.
          If uninitialized or no such element exists: NaN.
    [11]: variance of all non-inf and non-NaN elements.
          If uninitialized or no such element exists: NaN.
    [12]: Data type of the tensor encoded as an enum integer. See the DataType
          proto for more details.
    [13]: Number of dimensions of the tensor (ndims).
    [14+]: Sizes of the dimensions.

  Args:
    input: A `Tensor`. Input tensor, non-Reference type.
    device_name: An optional `string`. Defaults to `""`.
    tensor_name: An optional `string`. Defaults to `""`.
      Name of the input tensor.
    debug_urls: An optional list of `strings`. Defaults to `[]`.
      List of URLs to debug targets, e.g.,
        file:///foo/tfdbg_dump, grpc:://localhost:11011.
    lower_bound: An optional `float`. Defaults to `float(\'-inf\')`.
      (float) The lower bound <= which values will be included in the
        generalized -inf count. Default: -inf.
    upper_bound: An optional `float`. Defaults to `float(\'inf\')`.
      (float) The upper bound >= which values will be included in the
        generalized +inf count. Default: +inf.
    mute_if_healthy: An optional `bool`. Defaults to `False`.
      (bool) Do not send data to the debug URLs unless at least one
        of elements [2], [3] and [7] (i.e., the nan count and the generalized -inf and
        inf counts) is non-zero.
    gated_grpc: An optional `bool`. Defaults to `False`.
      Whether this op will be gated. If any of the debug_urls of this
        debug node is of the grpc:// scheme, when the value of this attribute is set
        to True, the data will not actually be sent via the grpc stream unless this
        debug op has been enabled at the debug_url. If all of the debug_urls of this
        debug node are of the grpc:// scheme and the debug op is enabled at none of
        them, the output will be an empty Tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float64`.
  '''

DebugNumericSummary: Incomplete

def debug_numeric_summary_eager_fallback(input, device_name, tensor_name, debug_urls, lower_bound, upper_bound, mute_if_healthy, gated_grpc, name, ctx): ...
def debug_numeric_summary_v2(input, output_dtype=..., tensor_debug_mode: int = -1, tensor_id: int = -1, name: Incomplete | None = None):
    """Debug Numeric Summary V2 Op.

  Computes a numeric summary of the input tensor. The shape of the output
  depends on the tensor_debug_mode attribute.
  This op is used internally by TensorFlow Debugger (tfdbg) v2.

  Args:
    input: A `Tensor`. Input tensor, to be summarized by the op.
    output_dtype: An optional `tf.DType` from: `tf.float32, tf.float64`. Defaults to `tf.float32`.
      Optional. The type of the output. Can be float32 or float64 (default: float32).
    tensor_debug_mode: An optional `int`. Defaults to `-1`.
      Tensor debug mode: the mode in which the input tensor is summarized
        by the op. See the TensorDebugMode enum in
        tensorflow/core/protobuf/debug_event.proto for details.

      Supported values:
        2 (CURT_HEALTH): Output a float32/64 tensor of shape [2]. The 1st
        element is the tensor_id, if provided, and -1 otherwise. The 2nd
        element is a bit which is set to 1 if the input tensor has an
        infinity or nan value, or zero otherwise.

        3 (CONCISE_HEALTH): Output a float32/64 tensor of shape [5]. The 1st
        element is the tensor_id, if provided, and -1 otherwise. The
        remaining four slots are the total number of elements, -infs,
        +infs, and nans in the input tensor respectively.

        4 (FULL_HEALTH): Output a float32/64 tensor of shape [11]. The 1st
        element is the tensor_id, if provided, and -1 otherwise. The 2nd
        element is the device_id, if provided, and -1 otherwise. The 3rd
        element holds the datatype value of the input tensor as according
        to the enumerated type in tensorflow/core/framework/types.proto.
        The remaining elements hold the total number of elements, -infs,
        +infs, nans, negative finite numbers, zeros, and positive finite
        numbers in the input tensor respectively.

        5 (SHAPE): Output a float32/64 tensor of shape [10]. The 1st
        element is the tensor_id, if provided, and -1 otherwise. The 2nd
        element holds the datatype value of the input tensor as according
        to the enumerated type in tensorflow/core/framework/types.proto.
        The 3rd element holds the rank of the tensor. The 4th element holds
        the number of elements within the tensor. Finally the remaining 6
        elements hold the shape of the tensor. If the rank of the tensor
        is lower than 6, the shape is right padded with zeros. If the rank
        is greater than 6, the head of the shape is truncated.

        6 (FULL_NUMERICS): Output a float32/64 tensor of shape [22]. The 1st
        element is the tensor_id, if provided, and -1 otherwise. The 2nd
        element is the device_id, if provided, and -1 otherwise. The 3rd
        element holds the datatype value of the input tensor as according
        to the enumerated type in tensorflow/core/framework/types.proto.
        The 4th element holds the rank of the tensor. The 5th to 11th
        elements hold the shape of the tensor. If the rank of the tensor
        is lower than 6, the shape is right padded with zeros. If the rank
        is greater than 6, the head of the shape is truncated. The 12th to
        18th elements hold the number of elements, -infs, +infs, nans,
        denormal floats, negative finite numbers, zeros, and positive
        finite numbers in the input tensor respectively. The final four
        elements hold the min value, max value, mean, and variance of the
        input tensor.

        8 (REDUCE_INF_NAN_THREE_SLOTS): Output a float32/64 tensor of shape
        [3]. The 1st element is -inf if any elements of the input tensor
        is -inf, or zero otherwise. The 2nd element is +inf if any elements
        of the input tensor is +inf, or zero otherwise.  The 3rd element is
        nan if any element of the input tensor is nan, or zero otherwise.
    tensor_id: An optional `int`. Defaults to `-1`.
      Optional. An integer identifier for the tensor being summarized by this op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `output_dtype`.
  """

DebugNumericSummaryV2: Incomplete

def debug_numeric_summary_v2_eager_fallback(input, output_dtype, tensor_debug_mode, tensor_id, name, ctx): ...
