from tensorflow.python.ops.gen_nn_ops import *
from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import config as config, constant_op as constant_op, dtypes as dtypes, errors_impl as errors_impl, graph_util as graph_util, ops as ops, random_seed as random_seed, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, gen_math_ops as gen_math_ops, gen_nn_ops as gen_nn_ops, math_ops as math_ops, random_ops as random_ops, stateless_random_ops as stateless_random_ops
from tensorflow.python.platform import device_context as device_context
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.compat import collections_abc as collections_abc
from tensorflow.python.util.deprecation import deprecated_args as deprecated_args, deprecated_argument_lookup as deprecated_argument_lookup
from tensorflow.python.util.tf_export import tf_export as tf_export

local_response_normalization = gen_nn_ops.lrn

class _NonAtrousConvolution:
    """Helper class for _non_atrous_convolution.

  Note that this class assumes that shapes of input and filter passed to
  `__call__` are compatible with `input_shape` and filter_shape passed to the
  constructor.

  Args:
    input_shape: static input shape, i.e. input.shape.
    filter_shape: static filter shape, i.e. filter.shape.
    padding: see _non_atrous_convolution.
    data_format: see _non_atrous_convolution.
    strides: see _non_atrous_convolution.
    name: see _non_atrous_convolution.
    num_batch_dims: (Optional.)  The number of batch dimensions in the input;
     if not provided, the default of `1` is used.
  """
    padding: Incomplete
    name: Incomplete
    strides: Incomplete
    data_format: Incomplete
    conv_op: Incomplete
    def __init__(self, input_shape, filter_shape, padding, data_format: Incomplete | None = None, strides: Incomplete | None = None, name: Incomplete | None = None, num_batch_dims: int = 1) -> None: ...
    def __call__(self, inp, filter): ...

def squeeze_batch_dims(inp, op, inner_rank, name: Incomplete | None = None):
    """Returns `unsqueeze_batch(op(squeeze_batch(inp)))`.

  Where `squeeze_batch` reshapes `inp` to shape
  `[prod(inp.shape[:-inner_rank])] + inp.shape[-inner_rank:]`
  and `unsqueeze_batch` does the reverse reshape but on the output.

  Args:
    inp: A tensor with dims `batch_shape + inner_shape` where `inner_shape`
      is length `inner_rank`.
    op: A callable that takes a single input tensor and returns a single.
      output tensor.
    inner_rank: A python integer.
    name: A string.

  Returns:
    `unsqueeze_batch_op(squeeze_batch(inp))`.
  """
def dilation2d_v2(input, filters, strides, padding, data_format, dilations, name: Incomplete | None = None):
    '''Computes the grayscale dilation of 4-D `input` and 3-D `filters` tensors.

  The `input` tensor has shape `[batch, in_height, in_width, depth]` and the
  `filters` tensor has shape `[filter_height, filter_width, depth]`, i.e., each
  input channel is processed independently of the others with its own
  structuring function. The `output` tensor has shape
  `[batch, out_height, out_width, depth]`. The spatial dimensions of the output
  tensor depend on the `padding` algorithm. We currently only support the
  default "NHWC" `data_format`.

  In detail, the grayscale morphological 2-D dilation is the max-sum correlation
  (for consistency with `conv2d`, we use unmirrored filters):

      output[b, y, x, c] =
         max_{dy, dx} input[b,
                            strides[1] * y + rates[1] * dy,
                            strides[2] * x + rates[2] * dx,
                            c] +
                      filters[dy, dx, c]

  Max-pooling is a special case when the filter has size equal to the pooling
  kernel size and contains all zeros.

  Note on duality: The dilation of `input` by the `filters` is equal to the
  negation of the erosion of `-input` by the reflected `filters`.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`,
      `uint32`, `uint64`.
      4-D with shape `[batch, in_height, in_width, depth]`.
    filters: A `Tensor`. Must have the same type as `input`.
      3-D with shape `[filter_height, filter_width, depth]`.
    strides: A list of `ints` that has length `>= 4`.
      The stride of the sliding window for each dimension of the input
      tensor. Must be: `[1, stride_height, stride_width, 1]`.
    padding: A `string` from: `"SAME", "VALID"`.
      The type of padding algorithm to use. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A `string`, only `"NHWC"` is currently supported.
    dilations: A list of `ints` that has length `>= 4`.
      The input stride for atrous morphological dilation. Must be:
      `[1, rate_height, rate_width, 1]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''
def dilation2d_v1(input, filter: Incomplete | None = None, strides: Incomplete | None = None, rates: Incomplete | None = None, padding: Incomplete | None = None, name: Incomplete | None = None, filters: Incomplete | None = None, dilations: Incomplete | None = None): ...
def with_space_to_batch(input, dilation_rate, padding, op, filter_shape: Incomplete | None = None, spatial_dims: Incomplete | None = None, data_format: Incomplete | None = None):
    '''Performs `op` on the space-to-batch representation of `input`.

  This has the effect of transforming sliding window operations into the
  corresponding "atrous" operation in which the input is sampled at the
  specified `dilation_rate`.

  In the special case that `dilation_rate` is uniformly 1, this simply returns:

    op(input, num_spatial_dims, padding)

  Otherwise, it returns:

    batch_to_space_nd(
      op(space_to_batch_nd(input, adjusted_dilation_rate, adjusted_paddings),
         num_spatial_dims,
         "VALID")
      adjusted_dilation_rate,
      adjusted_crops),

  where:

    adjusted_dilation_rate is an int64 tensor of shape [max(spatial_dims)],
    adjusted_{paddings,crops} are int64 tensors of shape [max(spatial_dims), 2]

  defined as follows:

  We first define two int64 tensors `paddings` and `crops` of shape
  `[num_spatial_dims, 2]` based on the value of `padding` and the spatial
  dimensions of the `input`:

  If `padding = "VALID"`, then:

    paddings, crops = required_space_to_batch_paddings(
      input_shape[spatial_dims],
      dilation_rate)

  If `padding = "SAME"`, then:

    dilated_filter_shape =
      filter_shape + (filter_shape - 1) * (dilation_rate - 1)

    paddings, crops = required_space_to_batch_paddings(
      input_shape[spatial_dims],
      dilation_rate,
      [(dilated_filter_shape - 1) // 2,
       dilated_filter_shape - 1 - (dilated_filter_shape - 1) // 2])

  Because `space_to_batch_nd` and `batch_to_space_nd` assume that the spatial
  dimensions are contiguous starting at the second dimension, but the specified
  `spatial_dims` may not be, we must adjust `dilation_rate`, `paddings` and
  `crops` in order to be usable with these operations.  For a given dimension,
  if the block size is 1, and both the starting and ending padding and crop
  amounts are 0, then space_to_batch_nd effectively leaves that dimension alone,
  which is what is needed for dimensions not part of `spatial_dims`.
  Furthermore, `space_to_batch_nd` and `batch_to_space_nd` handle this case
  efficiently for any number of leading and trailing dimensions.

  For 0 <= i < len(spatial_dims), we assign:

    adjusted_dilation_rate[spatial_dims[i] - 1] = dilation_rate[i]
    adjusted_paddings[spatial_dims[i] - 1, :] = paddings[i, :]
    adjusted_crops[spatial_dims[i] - 1, :] = crops[i, :]

  All unassigned values of `adjusted_dilation_rate` default to 1, while all
  unassigned values of `adjusted_paddings` and `adjusted_crops` default to 0.

  Note in the case that `dilation_rate` is not uniformly 1, specifying "VALID"
  padding is equivalent to specifying `padding = "SAME"` with a filter_shape of
  `[1]*N`.

  Advanced usage. Note the following optimization: A sequence of
  `with_space_to_batch` operations with identical (not uniformly 1)
  `dilation_rate` parameters and "VALID" padding

    net = with_space_to_batch(net, dilation_rate, "VALID", op_1)
    ...
    net = with_space_to_batch(net, dilation_rate, "VALID", op_k)

  can be combined into a single `with_space_to_batch` operation as follows:

    def combined_op(converted_input, num_spatial_dims, _):
      result = op_1(converted_input, num_spatial_dims, "VALID")
      ...
      result = op_k(result, num_spatial_dims, "VALID")

    net = with_space_to_batch(net, dilation_rate, "VALID", combined_op)

  This eliminates the overhead of `k-1` calls to `space_to_batch_nd` and
  `batch_to_space_nd`.

  Similarly, a sequence of `with_space_to_batch` operations with identical (not
  uniformly 1) `dilation_rate` parameters, "SAME" padding, and odd filter
  dimensions

    net = with_space_to_batch(net, dilation_rate, "SAME", op_1, filter_shape_1)
    ...
    net = with_space_to_batch(net, dilation_rate, "SAME", op_k, filter_shape_k)

  can be combined into a single `with_space_to_batch` operation as follows:

    def combined_op(converted_input, num_spatial_dims, _):
      result = op_1(converted_input, num_spatial_dims, "SAME")
      ...
      result = op_k(result, num_spatial_dims, "SAME")

    net = with_space_to_batch(net, dilation_rate, "VALID", combined_op)

  Args:
    input: Tensor of rank > max(spatial_dims).
    dilation_rate: int32 Tensor of *known* shape [num_spatial_dims].
    padding: str constant equal to "VALID" or "SAME"
    op: Function that maps (input, num_spatial_dims, padding) -> output
    filter_shape: If padding = "SAME", specifies the shape of the convolution
      kernel/pooling window as an integer Tensor of shape [>=num_spatial_dims].
      If padding = "VALID", filter_shape is ignored and need not be specified.
    spatial_dims: Monotonically increasing sequence of `num_spatial_dims`
      integers (which are >= 1) specifying the spatial dimensions of `input`
      and output.  Defaults to: `range(1, num_spatial_dims+1)`.
    data_format: A string or None.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (default, or if `data_format`
      does not start with "NC"), or the second dimension (if `data_format`
      starts with "NC").  For N=1, the valid values are "NWC" (default) and
      "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
      For N=3, the valid values are "NDHWC" (default) and "NCDHW".

  Returns:
    The output Tensor as described above, dimensions will vary based on the op
    provided.

  Raises:
    ValueError: if `padding` is invalid or the arguments are incompatible.
    ValueError: if `spatial_dims` are invalid.
  '''

class _WithSpaceToBatch:
    """Helper class for with_space_to_batch.

  Note that this class assumes that shapes of input and filter passed to
  `__call__` are compatible with `input_shape`, `filter_shape`, and
  `spatial_dims` passed to the constructor.

  Arguments
    input_shape: static shape of input. i.e. input.shape.
    dilation_rate: see `with_space_to_batch`.
    padding: see `with_space_to_batch`.
    build_op: Function that maps (num_spatial_dims, paddings) -> (function that
      maps (input, filter) -> output).
    filter_shape: see `with_space_to_batch`.
    spatial_dims: `see with_space_to_batch`.
    data_format: see `with_space_to_batch`.
    num_batch_dims: (Optional).  Number of batch dims in `input_shape`.
  """
    call: Incomplete
    base_paddings: Incomplete
    num_spatial_dims: Incomplete
    rate_or_const_rate: Incomplete
    input_shape: Incomplete
    spatial_dims: Incomplete
    dilation_rate: Incomplete
    data_format: Incomplete
    op: Incomplete
    def __init__(self, input_shape, dilation_rate, padding, build_op, filter_shape: Incomplete | None = None, spatial_dims: Incomplete | None = None, data_format: Incomplete | None = None, num_batch_dims: int = 1) -> None:
        """Helper class for _with_space_to_batch."""
    def __call__(self, inp, filter): ...

def convolution(input, filter, padding, strides: Incomplete | None = None, dilation_rate: Incomplete | None = None, name: Incomplete | None = None, data_format: Incomplete | None = None, filters: Incomplete | None = None, dilations: Incomplete | None = None):
    '''Computes sums of N-D convolutions (actually cross-correlation).

  This also supports either output striding via the optional `strides` parameter
  or atrous convolution (also known as convolution with holes or dilated
  convolution, based on the French word "trous" meaning holes in English) via
  the optional `dilation_rate` parameter.  Currently, however, output striding
  is not supported for atrous convolutions.

  Specifically, in the case that `data_format` does not start with "NC", given
  a rank (N+2) `input` Tensor of shape

    [num_batches,
     input_spatial_shape[0],
     ...,
     input_spatial_shape[N-1],
     num_input_channels],

  a rank (N+2) `filter` Tensor of shape

    [spatial_filter_shape[0],
     ...,
     spatial_filter_shape[N-1],
     num_input_channels,
     num_output_channels],

  an optional `dilation_rate` tensor of shape N (defaults to `[1]*N`) specifying
  the filter upsampling/input downsampling rate, and an optional list of N
  `strides` (defaults to `[1]*N`), this computes for each N-D spatial output
  position `(x[0], ..., x[N-1])`:

  ```
  output[b, x[0], ..., x[N-1], k] =
      sum_{z[0], ..., z[N-1], q}
          filter[z[0], ..., z[N-1], q, k] *
          padded_input[b,
                       x[0]*strides[0] + dilation_rate[0]*z[0],
                       ...,
                       x[N-1]*strides[N-1] + dilation_rate[N-1]*z[N-1],
                       q]
  ```

  where b is the index into the batch, k is the output channel number, q is the
  input channel number, and z is the N-D spatial offset within the filter. Here,
  `padded_input` is obtained by zero padding the input using an effective
  spatial filter shape of `(spatial_filter_shape-1) * dilation_rate + 1` and
  output striding `strides`.

  In the case that `data_format` does start with `"NC"`, the `input` and output
  (but not the `filter`) are simply transposed as follows:

  ```python
  convolution(input, data_format, **kwargs) =
    tf.transpose(convolution(tf.transpose(input, [0] + range(2,N+2) + [1]),
                             **kwargs),
                 [0, N+1] + range(1, N+1))
  ```

  It is required that 1 <= N <= 3.

  Args:
    input: An (N+2)-D `Tensor` of type `T`, of shape
      `[batch_size] + input_spatial_shape + [in_channels]` if data_format does
      not start with "NC" (default), or
      `[batch_size, in_channels] + input_spatial_shape` if data_format starts
      with "NC".
    filter: An (N+2)-D `Tensor` with the same type as `input` and shape
      `spatial_filter_shape + [in_channels, out_channels]`.
    padding: A string, either `"VALID"` or `"SAME"`. The padding algorithm.
      `"valid"` means no padding. `"same"` results in padding evenly to
      the left/right or up/down of the input such that output has the same
      height/width dimension as the input when the strides are 1. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    strides: Optional.  Sequence of N ints >= 1.  Specifies the output stride.
      Defaults to `[1]*N`.  If any value of strides is > 1, then all values of
      dilation_rate must be 1.
    dilation_rate: Optional.  Sequence of N ints >= 1.  Specifies the filter
      upsampling/input downsampling rate.  In the literature, the same parameter
      is sometimes called `input stride` or `dilation`.  The effective filter
      size used for the convolution will be `spatial_filter_shape +
      (spatial_filter_shape - 1) * (rate - 1)`, obtained by inserting
      (dilation_rate[i]-1) zeros between consecutive elements of the original
      filter in each spatial dimension i.  If any value of dilation_rate is > 1,
      then all values of strides must be 1.
    name: Optional name for the returned tensor.
    data_format: A string or None.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (default, or if `data_format`
      does not start with "NC"), or the second dimension (if `data_format`
      starts with "NC").  For N=1, the valid values are "NWC" (default) and
      "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
      For N=3, the valid values are "NDHWC" (default) and "NCDHW".

  Returns:
    A `Tensor` with the same type as `input` of shape

        `[batch_size] + output_spatial_shape + [out_channels]`

    if data_format is None or does not start with "NC", or

        `[batch_size, out_channels] + output_spatial_shape`

    if data_format starts with "NC",
    where `output_spatial_shape` depends on the value of `padding`.

    If padding == "SAME":
      output_spatial_shape[i] = ceil(input_spatial_shape[i] / strides[i])

    If padding == "VALID":
      output_spatial_shape[i] =
        ceil((input_spatial_shape[i] -
              (spatial_filter_shape[i]-1) * dilation_rate[i])
             / strides[i]).

  Raises:
    ValueError: If input/output depth does not match `filter` shape, if padding
      is other than `"VALID"` or `"SAME"`, or if data_format is invalid.

  '''
def convolution_v2(input, filters, strides: Incomplete | None = None, padding: str = 'VALID', data_format: Incomplete | None = None, dilations: Incomplete | None = None, name: Incomplete | None = None): ...
def convolution_internal(input, filters, strides: Incomplete | None = None, padding: str = 'VALID', data_format: Incomplete | None = None, dilations: Incomplete | None = None, name: Incomplete | None = None, call_from_convolution: bool = True, num_spatial_dims: Incomplete | None = None):
    """Internal function which performs rank agnostic convolution.

  Args:
    input: See `convolution`.
    filters: See `convolution`.
    strides: See `convolution`.
    padding: See `convolution`.
    data_format: See `convolution`.
    dilations: See `convolution`.
    name: See `convolution`.
    call_from_convolution: See `convolution`.
    num_spatial_dims: (Optional.).  It is a integer describing the
      rank of the spatial dimensions.  For `1-D`, `2-D` and `3-D` convolutions,
      the value of `num_spatial_dims` is `1`, `2`, and `3`, respectively.
      This argument is only required to disambiguate the rank of `batch_shape`
      when `filter_shape.ndims is None` and `len(batch_shape) > 1`.  For
      backwards compatibility, if `num_spatial_dims is None` and
     `filter_shape.ndims is None`, then `len(batch_shape)` is assumed to be
     `1` (i.e., the input is expected to be
     `[batch_size, num_channels] + input_spatial_shape`
     or `[batch_size] + input_spatial_shape + [num_channels]`.

  Returns:
    A tensor of shape and dtype matching that of `input`.

  Raises:
    ValueError: If input and filter both have unknown shapes, or if
      `num_spatial_dims` is provided and incompatible with the value
      estimated from `filters.shape`.
  """

class Convolution:
    '''Helper class for convolution.

  Note that this class assumes that shapes of input and filter passed to
  `__call__` are compatible with `input_shape`, `filter_shape`, and
  `num_spatial_dims` passed to the constructor.

  Arguments
    input_shape: static shape of input. i.e. input.shape.  Its length is
      `batch_shape + input_spatial_shape + [num_channels]` if `data_format`
      does not start with `NC`, or
      `batch_shape + [num_channels] + input_spatial_shape` if `data_format`
      starts with `NC`.
    filter_shape: static shape of the filter. i.e. filter.shape.
    padding: The padding algorithm, must be "SAME" or "VALID".
    strides: see convolution.
    dilation_rate: see convolution.
    name: see convolution.
    data_format: A string or `None`.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (if `data_format` is `None`
      or does not start with `NC`), or the first post-batch dimension (i.e. if
      `data_format` starts with `NC`).
    num_spatial_dims: (Usually optional.)  Python integer, the rank of the
      spatial and channel dimensions.  For `1-D`, `2-D` and `3-D` convolutions,
      the value of `num_spatial_dims` is `1`, `2`, and `3`, respectively.
      This argument is only required to disambiguate the rank of `batch_shape`
      when `filter_shape.ndims is None` and `len(batch_shape) > 1`.  For
      backwards compatibility, if `num_spatial_dims is None` and
      `filter_shape.ndims is None`, then `len(batch_shape)` is assumed to be
      `1` (i.e., the input is expected to be
      `[batch_size, num_channels] + input_spatial_shape`
      or `[batch_size] + input_spatial_shape + [num_channels]`.
  '''
    input_shape: Incomplete
    filter_shape: Incomplete
    data_format: Incomplete
    strides: Incomplete
    padding: Incomplete
    name: Incomplete
    dilation_rate: Incomplete
    num_batch_dims: Incomplete
    num_spatial_dims: Incomplete
    conv_op: Incomplete
    def __init__(self, input_shape, filter_shape, padding, strides: Incomplete | None = None, dilation_rate: Incomplete | None = None, name: Incomplete | None = None, data_format: Incomplete | None = None, num_spatial_dims: Incomplete | None = None) -> None:
        """Helper function for convolution."""
    def __call__(self, inp, filter): ...

def pool(input, window_shape, pooling_type, padding, dilation_rate: Incomplete | None = None, strides: Incomplete | None = None, name: Incomplete | None = None, data_format: Incomplete | None = None, dilations: Incomplete | None = None):
    '''Performs an N-D pooling operation.

  In the case that `data_format` does not start with "NC", computes for
      0 <= b < batch_size,
      0 <= x[i] < output_spatial_shape[i],
      0 <= c < num_channels:

  ```
  output[b, x[0], ..., x[N-1], c] =
    REDUCE_{z[0], ..., z[N-1]}
      input[b,
            x[0] * strides[0] - pad_before[0] + dilation_rate[0]*z[0],
            ...
            x[N-1]*strides[N-1] - pad_before[N-1] + dilation_rate[N-1]*z[N-1],
            c],
  ```

  where the reduction function REDUCE depends on the value of `pooling_type`,
  and pad_before is defined based on the value of `padding` as described in
  the "returns" section of `tf.nn.convolution` for details.
  The reduction never includes out-of-bounds positions.

  In the case that `data_format` starts with `"NC"`, the `input` and output are
  simply transposed as follows:

  ```python
  pool(input, data_format, **kwargs) =
    tf.transpose(pool(tf.transpose(input, [0] + range(2,N+2) + [1]),
                      **kwargs),
                 [0, N+1] + range(1, N+1))
  ```

  Args:
    input: Tensor of rank N+2, of shape
      `[batch_size] + input_spatial_shape + [num_channels]` if data_format does
      not start with "NC" (default), or
      `[batch_size, num_channels] + input_spatial_shape` if data_format starts
      with "NC".  Pooling happens over the spatial dimensions only.
    window_shape: Sequence of N ints >= 1.
    pooling_type: Specifies pooling operation, must be "AVG" or "MAX".
    padding: The padding algorithm, must be "SAME" or "VALID".
      See the "returns" section of `tf.nn.convolution` for details.
    dilation_rate: Optional.  Dilation rate.  List of N ints >= 1.
      Defaults to `[1]*N`.  If any value of dilation_rate is > 1, then all
      values of strides must be 1.
    strides: Optional.  Sequence of N ints >= 1.  Defaults to `[1]*N`.
      If any value of strides is > 1, then all values of dilation_rate must be
      1.
    name: Optional. Name of the op.
    data_format: A string or None.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (default, or if `data_format`
      does not start with "NC"), or the second dimension (if `data_format`
      starts with "NC").  For N=1, the valid values are "NWC" (default) and
      "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
      For N=3, the valid values are "NDHWC" (default) and "NCDHW".
    dilations: Alias for dilation_rate

  Returns:
    Tensor of rank N+2, of shape
      [batch_size] + output_spatial_shape + [num_channels]

    if data_format is None or does not start with "NC", or

      [batch_size, num_channels] + output_spatial_shape

    if data_format starts with "NC",
    where `output_spatial_shape` depends on the value of padding:

    If padding = "SAME":
      output_spatial_shape[i] = ceil(input_spatial_shape[i] / strides[i])

    If padding = "VALID":
      output_spatial_shape[i] =
        ceil((input_spatial_shape[i] - (window_shape[i] - 1) * dilation_rate[i])
             / strides[i]).

  Raises:
    ValueError: if arguments are invalid.

  '''
def pool_v2(input, window_shape, pooling_type, strides: Incomplete | None = None, padding: str = 'VALID', data_format: Incomplete | None = None, dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''Performs an N-D pooling operation.

  In the case that `data_format` does not start with "NC", computes for
      0 <= b < batch_size,
      0 <= x[i] < output_spatial_shape[i],
      0 <= c < num_channels:

  ```
  output[b, x[0], ..., x[N-1], c] =
    REDUCE_{z[0], ..., z[N-1]}
      input[b,
            x[0] * strides[0] - pad_before[0] + dilation_rate[0]*z[0],
            ...
            x[N-1]*strides[N-1] - pad_before[N-1] + dilation_rate[N-1]*z[N-1],
            c],
  ```

  where the reduction function REDUCE depends on the value of `pooling_type`,
  and pad_before is defined based on the value of `padding` as described in
  the "returns" section of `tf.nn.convolution` for details.
  The reduction never includes out-of-bounds positions.

  In the case that `data_format` starts with `"NC"`, the `input` and output are
  simply transposed as follows:

  ```python
  pool(input, data_format, **kwargs) =
    tf.transpose(pool(tf.transpose(input, [0] + range(2,N+2) + [1]),
                      **kwargs),
                 [0, N+1] + range(1, N+1))
  ```

  Args:
    input: Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape +
      [num_channels]` if data_format does not start with "NC" (default), or
      `[batch_size, num_channels] + input_spatial_shape` if data_format starts
      with "NC".  Pooling happens over the spatial dimensions only.
    window_shape: Sequence of N ints >= 1.
    pooling_type: Specifies pooling operation, must be "AVG" or "MAX".
    strides: Optional. Sequence of N ints >= 1.  Defaults to `[1]*N`. If any value of
      strides is > 1, then all values of dilation_rate must be 1.
    padding: The padding algorithm, must be "SAME" or "VALID". Defaults to "SAME".
      See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string or None.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (default, or if `data_format`
      does not start with "NC"), or the second dimension (if `data_format`
      starts with "NC").  For N=1, the valid values are "NWC" (default) and
      "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW". For
      N=3, the valid values are "NDHWC" (default) and "NCDHW".
    dilations: Optional.  Dilation rate.  List of N ints >= 1. Defaults to
      `[1]*N`.  If any value of dilation_rate is > 1, then all values of strides
      must be 1.
    name: Optional. Name of the op.

  Returns:
    Tensor of rank N+2, of shape
      [batch_size] + output_spatial_shape + [num_channels]

    if data_format is None or does not start with "NC", or

      [batch_size, num_channels] + output_spatial_shape

    if data_format starts with "NC",
    where `output_spatial_shape` depends on the value of padding:

    If padding = "SAME":
      output_spatial_shape[i] = ceil(input_spatial_shape[i] / strides[i])

    If padding = "VALID":
      output_spatial_shape[i] =
        ceil((input_spatial_shape[i] - (window_shape[i] - 1) * dilation_rate[i])
             / strides[i]).

  Raises:
    ValueError: if arguments are invalid.
  '''
def atrous_conv2d(value, filters, rate, padding, name: Incomplete | None = None):
    '''Atrous convolution (a.k.a. convolution with holes or dilated convolution).

  This function is a simpler wrapper around the more general
  `tf.nn.convolution`, and exists only for backwards compatibility. You can
  use `tf.nn.convolution` to perform 1-D, 2-D, or 3-D atrous convolution.

  Computes a 2-D atrous convolution, also known as convolution with holes or
  dilated convolution, given 4-D `value` and `filters` tensors. If the `rate`
  parameter is equal to one, it performs regular 2-D convolution. If the `rate`
  parameter is greater than one, it performs convolution with holes, sampling
  the input values every `rate` pixels in the `height` and `width` dimensions.
  This is equivalent to convolving the input with a set of upsampled filters,
  produced by inserting `rate - 1` zeros between two consecutive values of the
  filters along the `height` and `width` dimensions, hence the name atrous
  convolution or convolution with holes (the French word trous means holes in
  English).

  More specifically:

  ```
  output[batch, height, width, out_channel] =
      sum_{dheight, dwidth, in_channel} (
          filters[dheight, dwidth, in_channel, out_channel] *
          value[batch, height + rate*dheight, width + rate*dwidth, in_channel]
      )
  ```

  Atrous convolution allows us to explicitly control how densely to compute
  feature responses in fully convolutional networks. Used in conjunction with
  bilinear interpolation, it offers an alternative to `conv2d_transpose` in
  dense prediction tasks such as semantic image segmentation, optical flow
  computation, or depth estimation. It also allows us to effectively enlarge
  the field of view of filters without increasing the number of parameters or
  the amount of computation.

  For a description of atrous convolution and how it can be used for dense
  feature extraction, please see: (Chen et al., 2015). The same operation is
  investigated further in (Yu et al., 2016). Previous works that effectively
  use atrous convolution in different ways are, among others,
  (Sermanet et al., 2014) and (Giusti et al., 2013).
  Atrous convolution is also closely related to the so-called noble identities
  in multi-rate signal processing.

  There are many different ways to implement atrous convolution (see the refs
  above). The implementation here reduces

  ```python
  atrous_conv2d(value, filters, rate, padding=padding)
  ```

  to the following three operations:

  ```python
  paddings = ...
  net = space_to_batch(value, paddings, block_size=rate)
  net = conv2d(net, filters, strides=[1, 1, 1, 1], padding="VALID")
  crops = ...
  net = batch_to_space(net, crops, block_size=rate)
  ```

  Advanced usage. Note the following optimization: A sequence of `atrous_conv2d`
  operations with identical `rate` parameters, \'SAME\' `padding`, and filters
  with odd heights/ widths:

  ```python
  net = atrous_conv2d(net, filters1, rate, padding="SAME")
  net = atrous_conv2d(net, filters2, rate, padding="SAME")
  ...
  net = atrous_conv2d(net, filtersK, rate, padding="SAME")
  ```

  can be equivalently performed cheaper in terms of computation and memory as:

  ```python
  pad = ...  # padding so that the input dims are multiples of rate
  net = space_to_batch(net, paddings=pad, block_size=rate)
  net = conv2d(net, filters1, strides=[1, 1, 1, 1], padding="SAME")
  net = conv2d(net, filters2, strides=[1, 1, 1, 1], padding="SAME")
  ...
  net = conv2d(net, filtersK, strides=[1, 1, 1, 1], padding="SAME")
  net = batch_to_space(net, crops=pad, block_size=rate)
  ```

  because a pair of consecutive `space_to_batch` and `batch_to_space` ops with
  the same `block_size` cancel out when their respective `paddings` and `crops`
  inputs are identical.

  Args:
    value: A 4-D `Tensor` of type `float`. It needs to be in the default "NHWC"
      format. Its shape is `[batch, in_height, in_width, in_channels]`.
    filters: A 4-D `Tensor` with the same type as `value` and shape
      `[filter_height, filter_width, in_channels, out_channels]`. `filters`\'
      `in_channels` dimension must match that of `value`. Atrous convolution is
      equivalent to standard convolution with upsampled filters with effective
      height `filter_height + (filter_height - 1) * (rate - 1)` and effective
      width `filter_width + (filter_width - 1) * (rate - 1)`, produced by
      inserting `rate - 1` zeros along consecutive elements across the
      `filters`\' spatial dimensions.
    rate: A positive int32. The stride with which we sample input values across
      the `height` and `width` dimensions. Equivalently, the rate by which we
      upsample the filter values by inserting zeros across the `height` and
      `width` dimensions. In the literature, the same parameter is sometimes
      called `input stride` or `dilation`.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    name: Optional name for the returned tensor.

  Returns:
    A `Tensor` with the same type as `value`.
    Output shape with `\'VALID\'` padding is:

        [batch, height - rate * (filter_width - 1),
         width - rate * (filter_height - 1), out_channels].

    Output shape with `\'SAME\'` padding is:

        [batch, height, width, out_channels].

  Raises:
    ValueError: If input/output depth does not match `filters`\' shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`.

  References:
    Multi-Scale Context Aggregation by Dilated Convolutions:
      [Yu et al., 2016](https://arxiv.org/abs/1511.07122)
      ([pdf](https://arxiv.org/pdf/1511.07122.pdf))
    Semantic Image Segmentation with Deep Convolutional Nets and Fully
    Connected CRFs:
      [Chen et al., 2015](http://arxiv.org/abs/1412.7062)
      ([pdf](https://arxiv.org/pdf/1412.7062))
    OverFeat - Integrated Recognition, Localization and Detection using
    Convolutional Networks:
      [Sermanet et al., 2014](https://arxiv.org/abs/1312.6229)
      ([pdf](https://arxiv.org/pdf/1312.6229.pdf))
    Fast Image Scanning with Deep Max-Pooling Convolutional Neural Networks:
      [Giusti et al., 2013]
      (https://ieeexplore.ieee.org/abstract/document/6738831)
      ([pdf](https://arxiv.org/pdf/1302.1700.pdf))
  '''
def convert_padding(padding, expected_length: int = 4):
    """Converts Python padding to C++ padding for ops which take EXPLICIT padding.

  Args:
    padding: the `padding` argument for a Python op which supports EXPLICIT
      padding.
    expected_length: Expected number of entries in the padding list when
      explicit padding is used.

  Returns:
    (padding, explicit_paddings) pair, which should be passed as attributes to a
    C++ op.

  Raises:
    ValueError: If padding is invalid.
  """
def conv1d(value: Incomplete | None = None, filters: Incomplete | None = None, stride: Incomplete | None = None, padding: Incomplete | None = None, use_cudnn_on_gpu: Incomplete | None = None, data_format: Incomplete | None = None, name: Incomplete | None = None, input: Incomplete | None = None, dilations: Incomplete | None = None):
    '''Computes a 1-D convolution of input with rank `>=3` and a `3-D` filter.

  Given an input tensor of shape
    `batch_shape + [in_width, in_channels]`
  if `data_format` is `"NWC"`, or
    `batch_shape + [in_channels, in_width]`
  if `data_format` is `"NCW"`,
  and a filter / kernel tensor of shape
  `[filter_width, in_channels, out_channels]`, this op reshapes
  the arguments to pass them to `conv2d` to perform the equivalent
  convolution operation.

  Internally, this op reshapes the input tensors and invokes `tf.nn.conv2d`.
  For example, if `data_format` does not start with "NC", a tensor of shape
    `batch_shape + [in_width, in_channels]`
  is reshaped to
    `batch_shape + [1, in_width, in_channels]`,
  and the filter is reshaped to
    `[1, filter_width, in_channels, out_channels]`.
  The result is then reshaped back to
    `batch_shape + [out_width, out_channels]`
  \\(where out_width is a function of the stride and padding as in conv2d\\) and
  returned to the caller.

  Args:
    value: A Tensor of rank at least 3. Must be of type `float16`, `float32`, or
      `float64`.
    filters: A Tensor of rank at least 3.  Must have the same type as `value`.
    stride: An int or list of `ints` that has length `1` or `3`.  The number of
      entries by which the filter is moved right at each step.
    padding: \'SAME\' or \'VALID\'
    use_cudnn_on_gpu: An optional `bool`.  Defaults to `True`.
    data_format: An optional `string` from `"NWC", "NCW"`.  Defaults to `"NWC"`,
      the data is stored in the order of `batch_shape + [in_width,
      in_channels]`.  The `"NCW"` format stores data as `batch_shape +
      [in_channels, in_width]`.
    name: A name for the operation (optional).
    input: Alias for value.
    dilations: An int or list of `ints` that has length `1` or `3` which
      defaults to 1. The dilation factor for each dimension of input. If set to
      k > 1, there will be k-1 skipped cells between each filter element on that
      dimension. Dilations in the batch and depth dimensions must be 1.

  Returns:
    A `Tensor`.  Has the same type as input.

  Raises:
    ValueError: if `data_format` is invalid.
  '''
def conv1d_v2(input, filters, stride, padding, data_format: str = 'NWC', dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''Computes a 1-D convolution given 3-D input and filter tensors.

  Given an input tensor of shape
    `batch_shape + [in_width, in_channels]`
  if `data_format` is `"NWC"`, or
    `batch_shape + [in_channels, in_width]`
  if `data_format` is `"NCW"`,
  and a filter / kernel tensor of shape
  `[filter_width, in_channels, out_channels]`, this op reshapes
  the arguments to pass them to `conv2d` to perform the equivalent
  convolution operation.

  Internally, this op reshapes the input tensors and invokes `tf.nn.conv2d`.
  For example, if `data_format` does not start with `"NC"`, a tensor of shape
    `batch_shape + [in_width, in_channels]`
  is reshaped to
    `batch_shape + [1, in_width, in_channels]`,
  and the filter is reshaped to
    `[1, filter_width, in_channels, out_channels]`.
  The result is then reshaped back to
    `batch_shape + [out_width, out_channels]`
  \\(where out_width is a function of the stride and padding as in conv2d\\) and
  returned to the caller.

  Args:
    input: A Tensor of rank at least 3. Must be of type `float16`, `float32`, or
      `float64`.
    filters: A Tensor of rank at least 3.  Must have the same type as `input`.
    stride: An int or list of `ints` that has length `1` or `3`.  The number of
      entries by which the filter is moved right at each step.
    padding: \'SAME\' or \'VALID\'. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: An optional `string` from `"NWC", "NCW"`.  Defaults to `"NWC"`,
      the data is stored in the order of
      `batch_shape + [in_width, in_channels]`.  The `"NCW"` format stores data
      as `batch_shape + [in_channels, in_width]`.
    dilations: An int or list of `ints` that has length `1` or `3` which
      defaults to 1. The dilation factor for each dimension of input. If set to
      k > 1, there will be k-1 skipped cells between each filter element on that
      dimension. Dilations in the batch and depth dimensions must be 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`.  Has the same type as input.

  Raises:
    ValueError: if `data_format` is invalid.
  '''
def conv1d_transpose(input, filters, output_shape, strides, padding: str = 'SAME', data_format: str = 'NWC', dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''The transpose of `conv1d`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is actually the transpose (gradient) of `conv1d`
  rather than an actual deconvolution.

  Args:
    input: A 3-D `Tensor` of type `float` and shape
      `[batch, in_width, in_channels]` for `NWC` data format or
      `[batch, in_channels, in_width]` for `NCW` data format.
    filters: A 3-D `Tensor` with the same type as `input` and shape
      `[filter_width, output_channels, in_channels]`.  `filter`\'s
      `in_channels` dimension must match that of `input`.
    output_shape: A 1-D `Tensor`, containing three elements, representing the
      output shape of the deconvolution op.
    strides: An int or list of `ints` that has length `1` or `3`.  The number of
      entries by which the filter is moved right at each step.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string. `\'NWC\'` and `\'NCW\'` are supported.
    dilations: An int or list of `ints` that has length `1` or `3` which
      defaults to 1. The dilation factor for each dimension of input. If set to
      k > 1, there will be k-1 skipped cells between each filter element on that
      dimension. Dilations in the batch and depth dimensions must be 1.
    name: Optional name for the returned tensor.

  Returns:
    A `Tensor` with the same type as `input`.

  Raises:
    ValueError: If input/output depth does not match `filter`\'s shape, if
      `output_shape` is not at 3-element vector, if `padding` is other than
      `\'VALID\'` or `\'SAME\'`, or if `data_format` is invalid.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''
def conv2d_v2(input, filters, strides, padding, data_format: str = 'NHWC', dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''Computes a 2-D convolution given `input` and 4-D `filters` tensors.

  The `input` tensor may have rank `4` or higher, where shape dimensions `[:-3]`
  are considered batch dimensions (`batch_shape`).

  Given an input tensor of shape
  `batch_shape + [in_height, in_width, in_channels]` and a filter / kernel
  tensor of shape `[filter_height, filter_width, in_channels, out_channels]`,
  this op performs the following:

  1. Flattens the filter to a 2-D matrix with shape
     `[filter_height * filter_width * in_channels, output_channels]`.
  2. Extracts image patches from the input tensor to form a *virtual*
     tensor of shape `[batch, out_height, out_width,
     filter_height * filter_width * in_channels]`.
  3. For each patch, right-multiplies the filter matrix and the image patch
     vector.

  In detail, with the default NHWC format,

      output[b, i, j, k] =
          sum_{di, dj, q} input[b, strides[1] * i + di, strides[2] * j + dj, q] *
                          filter[di, dj, q, k]

  Must have `strides[0] = strides[3] = 1`.  For the most common case of the same
  horizontal and vertical strides, `strides = [1, stride, stride, 1]`.

  Usage Example:

  >>> x_in = np.array([[
  ...   [[2], [1], [2], [0], [1]],
  ...   [[1], [3], [2], [2], [3]],
  ...   [[1], [1], [3], [3], [0]],
  ...   [[2], [2], [0], [1], [1]],
  ...   [[0], [0], [3], [1], [2]], ]])
  >>> kernel_in = np.array([
  ...  [ [[2, 0.1]], [[3, 0.2]] ],
  ...  [ [[0, 0.3]], [[1, 0.4]] ], ])
  >>> x = tf.constant(x_in, dtype=tf.float32)
  >>> kernel = tf.constant(kernel_in, dtype=tf.float32)
  >>> tf.nn.conv2d(x, kernel, strides=[1, 1, 1, 1], padding=\'VALID\')
  <tf.Tensor: shape=(1, 4, 4, 2), dtype=float32, numpy=..., dtype=float32)>

  Args:
    input: A `Tensor`. Must be one of the following types:
      `half`, `bfloat16`, `float32`, `float64`.
      A Tensor of rank at least 4. The dimension order is interpreted according
      to the value of `data_format`; with the all-but-inner-3 dimensions acting
      as batch dimensions. See below for details.
    filters: A `Tensor`. Must have the same type as `input`.
      A 4-D tensor of shape
      `[filter_height, filter_width, in_channels, out_channels]`
    strides: An int or list of `ints` that has length `1`, `2` or `4`.  The
      stride of the sliding window for each dimension of `input`. If a single
      value is given it is replicated in the `H` and `W` dimension. By default
      the `N` and `C` dimensions are set to 1. The dimension order is determined
      by the value of `data_format`, see below for details.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information. When explicit padding is used and data_format is
      `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
      [pad_left, pad_right], [0, 0]]`. When explicit padding used and
      data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`.
      Defaults to `"NHWC"`.
      Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of:
          `batch_shape + [height, width, channels]`.
      Alternatively, the format could be "NCHW", the data storage order of:
          `batch_shape + [channels, height, width]`.
    dilations: An int or list of `ints` that has length `1`, `2` or `4`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the `H` and `W` dimension. By
      default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details. Dilations in the batch and depth dimensions if a 4-d tensor
      must be 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input` and the same outer batch shape.
  '''
def conv2d(input, filter: Incomplete | None = None, strides: Incomplete | None = None, padding: Incomplete | None = None, use_cudnn_on_gpu: bool = True, data_format: str = 'NHWC', dilations=[1, 1, 1, 1], name: Incomplete | None = None, filters: Incomplete | None = None):
    '''Computes a 2-D convolution given 4-D `input` and `filter` tensors.

  Given an input tensor of shape `[batch, in_height, in_width, in_channels]`
  and a filter / kernel tensor of shape
  `[filter_height, filter_width, in_channels, out_channels]`, this op
  performs the following:

  1. Flattens the filter to a 2-D matrix with shape
     `[filter_height * filter_width * in_channels, output_channels]`.
  2. Extracts image patches from the input tensor to form a *virtual*
     tensor of shape `[batch, out_height, out_width,
     filter_height * filter_width * in_channels]`.
  3. For each patch, right-multiplies the filter matrix and the image patch
     vector.

  In detail, with the default NHWC format,

      output[b, i, j, k] =
          sum_{di, dj, q} input[b, strides[1] * i + di, strides[2] * j + dj, q]
                          * filter[di, dj, q, k]

  Must have `strides[0] = strides[3] = 1`.  For the most common case of the same
  horizontal and vertical strides, `strides = [1, stride, stride, 1]`.

  Args:
    input: A `Tensor`. Must be one of the following types:
      `half`, `bfloat16`, `float32`, `float64`.
      A 4-D tensor. The dimension order is interpreted according to the value
      of `data_format`, see below for details.
    filter: A `Tensor`. Must have the same type as `input`.
      A 4-D tensor of shape
      `[filter_height, filter_width, in_channels, out_channels]`
    strides: An int or list of `ints` that has length `1`, `2` or `4`.  The
      stride of the sliding window for each dimension of `input`. If a single
      value is given it is replicated in the `H` and `W` dimension. By default
      the `N` and `C` dimensions are set to 1. The dimension order is determined
      by the value of `data_format`, see below for details.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. When explicit padding is used and
      data_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top,
      pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used
      and data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    use_cudnn_on_gpu: An optional `bool`. Defaults to `True`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`.
      Defaults to `"NHWC"`.
      Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of:
          [batch, height, width, channels].
      Alternatively, the format could be "NCHW", the data storage order of:
          [batch, channels, height, width].
    dilations: An int or list of `ints` that has length `1`, `2` or `4`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the `H` and `W` dimension. By
      default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details. Dilations in the batch and depth dimensions if a 4-d tensor
      must be 1.
    name: A name for the operation (optional).
    filters: Alias for filter.

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''
def conv2d_backprop_filter(input, filter_sizes, out_backprop, strides, padding, use_cudnn_on_gpu: bool = True, data_format: str = 'NHWC', dilations=[1, 1, 1, 1], name: Incomplete | None = None):
    '''Computes the gradients of convolution with respect to the filter.

  Args:
    input: A `Tensor`. Must be one of the following types:
      `half`, `bfloat16`, `float32`, `float64`.
      4-D with shape `[batch, in_height, in_width, in_channels]`.
    filter_sizes: A `Tensor` of type `int32`.
      An integer vector representing the tensor shape of `filter`,
      where `filter` is a 4-D
      `[filter_height, filter_width, in_channels, out_channels]` tensor.
    out_backprop: A `Tensor`. Must have the same type as `input`.
      4-D with shape `[batch, out_height, out_width, out_channels]`.
      Gradients w.r.t. the output of the convolution.
    strides: A list of `ints`.
      The stride of the sliding window for each dimension of the input
      of the convolution. Must be in the same order as the dimension specified
      with format.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. When explicit padding is used and
      data_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top,
      pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used
      and data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    use_cudnn_on_gpu: An optional `bool`. Defaults to `True`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`.
      Defaults to `"NHWC"`.
      Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of:
          [batch, in_height, in_width, in_channels].
      Alternatively, the format could be "NCHW", the data storage order of:
          [batch, in_channels, in_height, in_width].
    dilations: An optional list of `ints`. Defaults to `[1, 1, 1, 1]`.
      1-D tensor of length 4.  The dilation factor for each dimension of
      `input`. If set to k > 1, there will be k-1 skipped cells between each
      filter element on that dimension. The dimension order is determined by
      the value of `data_format`, see above for details. Dilations in the batch
      and depth dimensions must be 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''
def conv2d_backprop_input(input_sizes, filter: Incomplete | None = None, out_backprop: Incomplete | None = None, strides: Incomplete | None = None, padding: Incomplete | None = None, use_cudnn_on_gpu: bool = True, data_format: str = 'NHWC', dilations=[1, 1, 1, 1], name: Incomplete | None = None, filters: Incomplete | None = None):
    '''Computes the gradients of convolution with respect to the input.

  Args:
    input_sizes: A `Tensor` of type `int32`.
      An integer vector representing the shape of `input`,
      where `input` is a 4-D `[batch, height, width, channels]` tensor.
    filter: A `Tensor`. Must be one of the following types:
      `half`, `bfloat16`, `float32`, `float64`.
      4-D with shape
      `[filter_height, filter_width, in_channels, out_channels]`.
    out_backprop: A `Tensor`. Must have the same type as `filter`.
      4-D with shape `[batch, out_height, out_width, out_channels]`.
      Gradients w.r.t. the output of the convolution.
    strides: A list of `ints`.
      The stride of the sliding window for each dimension of the input
      of the convolution. Must be in the same order as the dimension specified
      with format.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. When explicit padding is used and
      data_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top,
      pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used
      and data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    use_cudnn_on_gpu: An optional `bool`. Defaults to `True`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`.
      Defaults to `"NHWC"`.
      Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of:
          [batch, in_height, in_width, in_channels].
      Alternatively, the format could be "NCHW", the data storage order of:
          [batch, in_channels, in_height, in_width].
    dilations: An optional list of `ints`. Defaults to `[1, 1, 1, 1]`.
      1-D tensor of length 4.  The dilation factor for each dimension of
      `input`. If set to k > 1, there will be k-1 skipped cells between each
      filter element on that dimension. The dimension order is determined by
      the value of `data_format`, see above for details. Dilations in the batch
      and depth dimensions must be 1.
    name: A name for the operation (optional).
    filters: Alias for filter.

  Returns:
    A `Tensor`. Has the same type as `filter`.
  '''
def conv2d_transpose(value: Incomplete | None = None, filter: Incomplete | None = None, output_shape: Incomplete | None = None, strides: Incomplete | None = None, padding: str = 'SAME', data_format: str = 'NHWC', name: Incomplete | None = None, input: Incomplete | None = None, filters: Incomplete | None = None, dilations: Incomplete | None = None):
    '''The transpose of `conv2d`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is really the transpose (gradient) of `conv2d`
  rather than an actual deconvolution.

  Args:
    value: A 4-D `Tensor` of type `float` and shape
      `[batch, height, width, in_channels]` for `NHWC` data format or
      `[batch, in_channels, height, width]` for `NCHW` data format.
    filter: A 4-D `Tensor` with the same type as `value` and shape
      `[height, width, output_channels, in_channels]`.  `filter`\'s
      `in_channels` dimension must match that of `value`.
    output_shape: A 1-D `Tensor` representing the output shape of the
      deconvolution op.
    strides: An int or list of `ints` that has length `1`, `2` or `4`.  The
      stride of the sliding window for each dimension of `input`. If a single
      value is given it is replicated in the `H` and `W` dimension. By default
      the `N` and `C` dimensions are set to 0. The dimension order is determined
      by the value of `data_format`, see below for details.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm.
      See the "returns" section of `tf.nn.convolution` for details.
    data_format: A string. \'NHWC\' and \'NCHW\' are supported.
    name: Optional name for the returned tensor.
    input: Alias for value.
    filters: Alias for filter.
    dilations: An int or list of `ints` that has length `1`, `2` or `4`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the `H` and `W` dimension. By
      default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details. Dilations in the batch and depth dimensions if a 4-d tensor
      must be 1.

  Returns:
    A `Tensor` with the same type as `value`.

  Raises:
    ValueError: If input/output depth does not match `filter`\'s shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''
def conv2d_transpose_v2(input, filters, output_shape, strides, padding: str = 'SAME', data_format: str = 'NHWC', dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''The transpose of `conv2d`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is really the transpose (gradient) of
  `atrous_conv2d` rather than an actual deconvolution.

  Args:
    input: A 4-D `Tensor` of type `float` and shape `[batch, height, width,
      in_channels]` for `NHWC` data format or `[batch, in_channels, height,
      width]` for `NCHW` data format.
    filters: A 4-D `Tensor` with the same type as `input` and shape `[height,
      width, output_channels, in_channels]`.  `filter`\'s `in_channels` dimension
      must match that of `input`.
    output_shape: A 1-D `Tensor` representing the output shape of the
      deconvolution op.
    strides: An int or list of `ints` that has length `1`, `2` or `4`.  The
      stride of the sliding window for each dimension of `input`. If a single
      value is given it is replicated in the `H` and `W` dimension. By default
      the `N` and `C` dimensions are set to 0. The dimension order is determined
      by the value of `data_format`, see below for details.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.  When explicit padding is used and data_format is
      `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
      [pad_left, pad_right], [0, 0]]`. When explicit padding used and
      data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    data_format: A string. \'NHWC\' and \'NCHW\' are supported.
    dilations: An int or list of `ints` that has length `1`, `2` or `4`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the `H` and `W` dimension. By
      default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details. Dilations in the batch and depth dimensions if a 4-d tensor
      must be 1.
    name: Optional name for the returned tensor.

  Returns:
    A `Tensor` with the same type as `input`.

  Raises:
    ValueError: If input/output depth does not match `filter`\'s shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''
def atrous_conv2d_transpose(value, filters, output_shape, rate, padding, name: Incomplete | None = None):
    '''The transpose of `atrous_conv2d`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is really the transpose (gradient) of
  `atrous_conv2d` rather than an actual deconvolution.

  Args:
    value: A 4-D `Tensor` of type `float`. It needs to be in the default `NHWC`
      format. Its shape is `[batch, in_height, in_width, in_channels]`.
    filters: A 4-D `Tensor` with the same type as `value` and shape
      `[filter_height, filter_width, out_channels, in_channels]`. `filters`\'
      `in_channels` dimension must match that of `value`. Atrous convolution is
      equivalent to standard convolution with upsampled filters with effective
      height `filter_height + (filter_height - 1) * (rate - 1)` and effective
      width `filter_width + (filter_width - 1) * (rate - 1)`, produced by
      inserting `rate - 1` zeros along consecutive elements across the
      `filters`\' spatial dimensions.
    output_shape: A 1-D `Tensor` of shape representing the output shape of the
      deconvolution op, of form `[batch, out_height, out_width, out_channels]`.
    rate: A positive int32. The stride with which we sample input values across
      the `height` and `width` dimensions. Equivalently, the rate by which we
      upsample the filter values by inserting zeros across the `height` and
      `width` dimensions. In the literature, the same parameter is sometimes
      called `input stride` or `dilation`.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    name: Optional name for the returned tensor.

  Returns:
    A `Tensor` with the same type as `value`.

  Raises:
    ValueError: If input/output depth does not match `filters`\' shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`, or if the `rate` is less
      than one, or if the output_shape is not a tensor with 4 elements.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''
def depthwise_conv2d_native(input, filter, strides, padding, data_format: str = 'NHWC', dilations=[1, 1, 1, 1], name: Incomplete | None = None):
    '''Computes a 2-D depthwise convolution.

  Given an input tensor of shape `[batch, in_height, in_width, in_channels]`
  and a filter / kernel tensor of shape
  `[filter_height, filter_width, in_channels, channel_multiplier]`, containing
  `in_channels` convolutional filters of depth 1, `depthwise_conv2d` applies
  a different filter to each input channel (expanding from 1 channel to
  `channel_multiplier` channels for each), then concatenates the results
  together. Thus, the output has `in_channels * channel_multiplier` channels.

  ```
  for k in 0..in_channels-1
    for q in 0..channel_multiplier-1
      output[b, i, j, k * channel_multiplier + q] =
        sum_{di, dj} input[b, strides[1] * i + di, strides[2] * j + dj, k] *
                          filter[di, dj, k, q]
  ```

  Must have `strides[0] = strides[3] = 1`.  For the most common case of the same
  horizontal and vertices strides, `strides = [1, stride, stride, 1]`.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `bfloat16`,
      `float32`, `float64`.
    filter: A `Tensor`. Must have the same type as `input`.
    strides: A list of `ints`. 1-D of length 4.  The stride of the sliding
      window for each dimension of `input`.
    padding: Controls how to pad the image before applying the convolution. Can
      be the string `"SAME"` or `"VALID"` indicating the type of padding
      algorithm to use, or a list indicating the explicit paddings at the start
      and end of each dimension. When explicit padding is used and data_format
      is `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
      [pad_left, pad_right], [0, 0]]`. When explicit padding used and
      data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`. Defaults to
      `"NHWC"`. Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of: [batch, height,
        width, channels].
      Alternatively, the format could be "NCHW", the data storage order of:
        [batch, channels, height, width].
    dilations: An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D
      tensor of length 4.  The dilation factor for each dimension of `input`. If
      set to k > 1, there will be k-1 skipped cells between each filter element
      on that dimension. The dimension order is determined by the value of
      `data_format`, see above for details. Dilations in the batch and depth
      dimensions must be 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''
def depthwise_conv2d_native_backprop_input(input_sizes, filter, out_backprop, strides, padding, data_format: str = 'NHWC', dilations=[1, 1, 1, 1], name: Incomplete | None = None):
    '''Computes the gradients of depthwise convolution with respect to the input.

  Args:
    input_sizes: A `Tensor` of type `int32`. An integer vector representing the
      shape of `input`, based on `data_format`.  For example, if `data_format`
      is \'NHWC\' then `input` is a 4-D `[batch, height, width, channels]` tensor.
    filter: A `Tensor`. Must be one of the following types: `half`, `bfloat16`,
      `float32`, `float64`. 4-D with shape `[filter_height, filter_width,
      in_channels, depthwise_multiplier]`.
    out_backprop: A `Tensor`. Must have the same type as `filter`. 4-D with
      shape  based on `data_format`. For example, if `data_format` is \'NHWC\'
      then out_backprop shape is `[batch, out_height, out_width, out_channels]`.
      Gradients w.r.t. the output of the convolution.
    strides: A list of `ints`. The stride of the sliding window for each
      dimension of the input of the convolution.
    padding: Controls how to pad the image before applying the convolution. Can
      be the string `"SAME"` or `"VALID"` indicating the type of padding
      algorithm to use, or a list indicating the explicit paddings at the start
      and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information. When explicit padding is used and data_format is
      `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
      [pad_left, pad_right], [0, 0]]`. When explicit padding used and
      data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`. Defaults to
      `"NHWC"`. Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of: [batch, height,
        width, channels].
      Alternatively, the format could be "NCHW", the data storage order of:
        [batch, channels, height, width].
    dilations: An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D
      tensor of length 4.  The dilation factor for each dimension of `input`. If
      set to k > 1, there will be k-1 skipped cells between each filter element
      on that dimension. The dimension order is determined by the value of
      `data_format`, see above for details. Dilations in the batch and depth
      dimensions must be 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `filter`.
  '''
def depthwise_conv2d_native_backprop_filter(input, filter_sizes, out_backprop, strides, padding, data_format: str = 'NHWC', dilations=[1, 1, 1, 1], name: Incomplete | None = None):
    '''Computes the gradients of depthwise convolution with respect to the filter.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `bfloat16`,
      `float32`, `float64`. 4-D with shape based on `data_format`.  For example,
      if `data_format` is \'NHWC\' then `input` is a 4-D `[batch, in_height,
      in_width, in_channels]` tensor.
    filter_sizes: A `Tensor` of type `int32`. An integer vector representing the
      tensor shape of `filter`, where `filter` is a 4-D `[filter_height,
      filter_width, in_channels, depthwise_multiplier]` tensor.
    out_backprop: A `Tensor`. Must have the same type as `input`. 4-D with shape
      based on `data_format`. For example, if `data_format` is \'NHWC\' then
      out_backprop shape is `[batch, out_height, out_width, out_channels]`.
      Gradients w.r.t. the output of the convolution.
    strides: A list of `ints`. The stride of the sliding window for each
      dimension of the input of the convolution.
    padding: Controls how to pad the image before applying the convolution. Can
      be the string `"SAME"` or `"VALID"` indicating the type of padding
      algorithm to use, or a list indicating the explicit paddings at the start
      and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information. When explicit padding is used and data_format is
      `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
      [pad_left, pad_right], [0, 0]]`. When explicit padding used and
      data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`.
    data_format: An optional `string` from: `"NHWC", "NCHW"`. Defaults to
      `"NHWC"`. Specify the data format of the input and output data. With the
      default format "NHWC", the data is stored in the order of: [batch, height,
        width, channels].
      Alternatively, the format could be "NCHW", the data storage order of:
        [batch, channels, height, width].
    dilations: An optional list of `ints`. Defaults to `[1, 1, 1, 1]`. 1-D
      tensor of length 4.  The dilation factor for each dimension of `input`. If
      set to k > 1, there will be k-1 skipped cells between each filter element
      on that dimension. The dimension order is determined by the value of
      `data_format`, see above for details. Dilations in the batch and depth
      dimensions must be 1.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  '''
def conv3d_v2(input, filters, strides, padding, data_format: str = 'NDHWC', dilations: Incomplete | None = None, name: Incomplete | None = None): ...
def conv3d_v1(input, filter: Incomplete | None = None, strides: Incomplete | None = None, padding: Incomplete | None = None, data_format: str = 'NDHWC', dilations=[1, 1, 1, 1, 1], name: Incomplete | None = None, filters: Incomplete | None = None): ...
def conv3d_transpose(value, filter: Incomplete | None = None, output_shape: Incomplete | None = None, strides: Incomplete | None = None, padding: str = 'SAME', data_format: str = 'NDHWC', name: Incomplete | None = None, input: Incomplete | None = None, filters: Incomplete | None = None, dilations: Incomplete | None = None):
    '''The transpose of `conv3d`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d`
  rather than an actual deconvolution.

  Args:
    value: A 5-D `Tensor` of type `float` and shape
      `[batch, depth, height, width, in_channels]`.
    filter: A 5-D `Tensor` with the same type as `value` and shape
      `[depth, height, width, output_channels, in_channels]`.  `filter`\'s
      `in_channels` dimension must match that of `value`.
    output_shape: A 1-D `Tensor` representing the output shape of the
      deconvolution op.
    strides: A list of ints. The stride of the sliding window for each
      dimension of the input tensor.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm.
      See the "returns" section of `tf.nn.convolution` for details.
    data_format: A string, either `\'NDHWC\'` or `\'NCDHW`\' specifying the layout
      of the input and output tensors. Defaults to `\'NDHWC\'`.
    name: Optional name for the returned tensor.
    input: Alias of value.
    filters: Alias of filter.
    dilations: An int or list of `ints` that has length `1`, `3` or `5`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the `D`, `H` and `W` dimension.
      By default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details. Dilations in the batch and depth dimensions if a 5-d tensor
      must be 1.

  Returns:
    A `Tensor` with the same type as `value`.

  Raises:
    ValueError: If input/output depth does not match `filter`\'s shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''
def conv3d_transpose_v2(input, filters, output_shape, strides, padding: str = 'SAME', data_format: str = 'NDHWC', dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''The transpose of `conv3d`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d`
  rather than an actual deconvolution.

  Args:
    input: A 5-D `Tensor` of type `float` and shape `[batch, depth, height,
      width, in_channels]` for `NDHWC` data format or `[batch, in_channels,
      depth, height, width]` for `NCDHW` data format.
    filters: A 5-D `Tensor` with the same type as `input` and shape `[depth,
      height, width, output_channels, in_channels]`.  `filter`\'s `in_channels`
      dimension must match that of `input`.
    output_shape: A 1-D `Tensor` representing the output shape of the
      deconvolution op.
    strides: An int or list of `ints` that has length `1`, `3` or `5`.  The
      stride of the sliding window for each dimension of `input`. If a single
      value is given it is replicated in the `D`, `H` and `W` dimension. By
      default the `N` and `C` dimensions are set to 0. The dimension order is
      determined by the value of `data_format`, see below for details.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string. \'NDHWC\' and \'NCDHW\' are supported.
    dilations: An int or list of `ints` that has length `1`, `3` or `5`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the `D`, `H` and `W` dimension.
      By default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details. Dilations in the batch and depth dimensions if a 5-d tensor
      must be 1.
    name: Optional name for the returned tensor.

  Returns:
    A `Tensor` with the same type as `input`.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''

CONV_TRANSPOSE_OPS: Incomplete

def conv_transpose(input, filters, output_shape, strides, padding: str = 'SAME', data_format: Incomplete | None = None, dilations: Incomplete | None = None, name: Incomplete | None = None):
    '''The transpose of `convolution`.

  This operation is sometimes called "deconvolution" after
  (Zeiler et al., 2010), but is really the transpose (gradient) of `conv3d`
  rather than an actual deconvolution.

  Args:
    input: An N+2 dimensional `Tensor` of shape
      `[batch_size] + input_spatial_shape + [in_channels]` if data_format does
      not start with "NC" (default), or
      `[batch_size, in_channels] + input_spatial_shape` if data_format starts
      with "NC". It must be one of the following types:
      `half`, `bfloat16`, `float32`, `float64`.
    filters: An N+2 dimensional `Tensor` with the same type as `input` and
      shape `spatial_filter_shape + [in_channels, out_channels]`.
    output_shape: A 1-D `Tensor` representing the output shape of the
      deconvolution op.
    strides: An int or list of `ints` that has length `1`, `N` or `N+2`.  The
      stride of the sliding window for each dimension of `input`. If a single
      value is given it is replicated in the spatial dimensions. By default
      the `N` and `C` dimensions are set to 0. The dimension order is determined
      by the value of `data_format`, see below for details.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string or None.  Specifies whether the channel dimension of
      the `input` and output is the last dimension (default, or if `data_format`
      does not start with "NC"), or the second dimension (if `data_format`
      starts with "NC").  For N=1, the valid values are "NWC" (default) and
      "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
      For N=3, the valid values are "NDHWC" (default) and "NCDHW".
    dilations: An int or list of `ints` that has length `1`, `N` or `N+2`,
      defaults to 1. The dilation factor for each dimension of`input`. If a
      single value is given it is replicated in the spatial dimensions. By
      default the `N` and `C` dimensions are set to 1. If set to k > 1, there
      will be k-1 skipped cells between each filter element on that dimension.
      The dimension order is determined by the value of `data_format`, see above
      for details.
    name: A name for the operation (optional). If not specified "conv_transpose"
      is used.

  Returns:
    A `Tensor` with the same type as `value`.

  References:
    Deconvolutional Networks:
      [Zeiler et al., 2010]
      (https://ieeexplore.ieee.org/abstract/document/5539957)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.232.4023&rep=rep1&type=pdf))
  '''
def bias_add(value, bias, data_format: Incomplete | None = None, name: Incomplete | None = None):
    """Adds `bias` to `value`.

  This is (mostly) a special case of `tf.add` where `bias` is restricted to 1-D.
  Broadcasting is supported, so `value` may have any number of dimensions.
  Unlike `tf.add`, the type of `bias` is allowed to differ from `value` in the
  case where both types are quantized.

  Args:
    value: A `Tensor` with type `float`, `double`, `int64`, `int32`, `uint8`,
      `int16`, `int8`, `complex64`, or `complex128`.
    bias: A 1-D `Tensor` with size matching the channel dimension of `value`.
      Must be the same type as `value` unless `value` is a quantized type,
      in which case a different quantized type may be used.
    data_format: A string. 'N...C' and 'NC...' are supported. If `None` (the
      default) is specified then 'N..C' is assumed.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with the same type as `value`.

  Raises:
    ValueError if data format is unrecognized, if `value` has less than two
    dimensions when `data_format` is 'N..C'/`None` or `value` has less
    then three dimensions when `data_format` is `NC..`, if `bias` does not
    have exactly one dimension (is a vector), or if the size of `bias`
    does not match the size of the channel dimension of `value`.
  """
def bias_add_v1(value, bias, name: Incomplete | None = None):
    """Adds `bias` to `value`.

  This is a deprecated version of bias_add and will soon to be removed.

  This is (mostly) a special case of `tf.add` where `bias` is restricted to 1-D.
  Broadcasting is supported, so `value` may have any number of dimensions.
  Unlike `tf.add`, the type of `bias` is allowed to differ from `value` in the
  case where both types are quantized.

  Args:
    value: A `Tensor` with type `float`, `double`, `int64`, `int32`, `uint8`,
      `int16`, `int8`, `complex64`, or `complex128`.
    bias: A 1-D `Tensor` with size matching the last dimension of `value`.
      Must be the same type as `value` unless `value` is a quantized type,
      in which case a different quantized type may be used.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with the same type as `value`.
  """
def crelu(features, name: Incomplete | None = None, axis: int = -1):
    """Computes Concatenated ReLU.

  Concatenates a ReLU which selects only the positive part of the activation
  with a ReLU which selects only the *negative* part of the activation.
  Note that as a result this non-linearity doubles the depth of the activations.
  Source: [Understanding and Improving Convolutional Neural Networks via
  Concatenated Rectified Linear Units. W. Shang, et
  al.](https://arxiv.org/abs/1603.05201)

  Args:
    features: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
      `int16`, or `int8`.
    name: A name for the operation (optional).
    axis: The axis that the output values are concatenated along. Default is -1.

  Returns:
    A `Tensor` with the same type as `features`.

  References:
    Understanding and Improving Convolutional Neural Networks via Concatenated
    Rectified Linear Units:
      [Shang et al., 2016](http://proceedings.mlr.press/v48/shang16)
      ([pdf](http://proceedings.mlr.press/v48/shang16.pdf))
  """
def crelu_v2(features, axis: int = -1, name: Incomplete | None = None): ...
def relu6(features, name: Incomplete | None = None):
    """Computes Rectified Linear 6: `min(max(features, 0), 6)`.

  In comparison with `tf.nn.relu`, relu6 activation functions have shown to
  empirically perform better under low-precision conditions (e.g. fixed point
  inference) by encouraging the model to learn sparse features earlier.
  Source: [Convolutional Deep Belief Networks on CIFAR-10: Krizhevsky et al.,
  2010](http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf).

  For example:

  >>> x = tf.constant([-3.0, -1.0, 0.0, 6.0, 10.0], dtype=tf.float32)
  >>> y = tf.nn.relu6(x)
  >>> y.numpy()
  array([0., 0., 0., 6., 6.], dtype=float32)

  Args:
    features: A `Tensor` with type `float`, `double`, `int32`, `int64`, `uint8`,
      `int16`, or `int8`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with the same type as `features`.

  References:
    Convolutional Deep Belief Networks on CIFAR-10:
      Krizhevsky et al., 2010
      ([pdf](http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf))
  """
def leaky_relu(features, alpha: float = 0.2, name: Incomplete | None = None):
    """Compute the Leaky ReLU activation function.

  Source: [Rectifier Nonlinearities Improve Neural Network Acoustic Models.
  AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013]
  (https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf).

  Args:
    features: A `Tensor` representing preactivation values. Must be one of
      the following types: `float16`, `float32`, `float64`, `int32`, `int64`.
    alpha: Slope of the activation function at x < 0.
    name: A name for the operation (optional).

  Returns:
    The activation value.

  References:
    Rectifier Nonlinearities Improve Neural Network Acoustic Models:
      [Maas et al., 2013]
      (http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.693.1422)
      ([pdf]
      (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.693.1422&rep=rep1&type=pdf))
  """
def gelu(features, approximate: bool = False, name: Incomplete | None = None):
    """Compute the Gaussian Error Linear Unit (GELU) activation function.

  Gaussian error linear unit (GELU) computes
  `x * P(X <= x)`, where `P(X) ~ N(0, 1)`.
  The (GELU) nonlinearity weights inputs by their value, rather than gates
  inputs by their sign as in ReLU.

  For example:

  >>> x = tf.constant([-3.0, -1.0, 0.0, 1.0, 3.0], dtype=tf.float32)
  >>> y = tf.nn.gelu(x)
  >>> y.numpy()
  array([-0.00404951, -0.15865529,  0.        ,  0.8413447 ,  2.9959507 ],
      dtype=float32)
  >>> y = tf.nn.gelu(x, approximate=True)
  >>> y.numpy()
  array([-0.00363752, -0.15880796,  0.        ,  0.841192  ,  2.9963627 ],
      dtype=float32)

  Args:
    features: A `float Tensor` representing preactivation values.
    approximate: An optional `bool`. Defaults to `False`. Whether to enable
      approximation.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with the same type as `features`.

  Raises:
    ValueError: if `features` is not a floating point `Tensor`.

  References:
    [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415).
  """
def softmax_v2(logits, axis: Incomplete | None = None, name: Incomplete | None = None):
    """Computes softmax activations.

  Used for multi-class predictions. The sum of all outputs generated by softmax
  is 1.

  This function performs the equivalent of

  ```python
  softmax = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis, keepdims=True)
  ```
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
def softmax(logits, axis: Incomplete | None = None, name: Incomplete | None = None, dim: Incomplete | None = None): ...
def log_softmax(logits, axis: Incomplete | None = None, name: Incomplete | None = None, dim: Incomplete | None = None):
    """Computes log softmax activations.

  For each batch `i` and class `j` we have

      logsoftmax = logits - log(reduce_sum(exp(logits), axis))

  Args:
    logits: A non-empty `Tensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    axis: The dimension softmax would be performed on. The default is -1 which
      indicates the last dimension.
    name: A name for the operation (optional).
    dim: Deprecated alias for `axis`.

  Returns:
    A `Tensor`. Has the same type as `logits`. Same shape as `logits`.

  Raises:
    InvalidArgumentError: if `logits` is empty or `axis` is beyond the last
      dimension of `logits`.
  """
def log_softmax_v2(logits, axis: Incomplete | None = None, name: Incomplete | None = None):
    """Computes log softmax activations.

  For each batch `i` and class `j` we have

      logsoftmax = logits - log(reduce_sum(exp(logits), axis))

  Args:
    logits: A non-empty `Tensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    axis: The dimension softmax would be performed on. The default is -1 which
      indicates the last dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `logits`. Same shape as `logits`.

  Raises:
    InvalidArgumentError: if `logits` is empty or `axis` is beyond the last
      dimension of `logits`.
  """
def softmax_cross_entropy_with_logits_v2(labels, logits, axis: int = -1, name: Incomplete | None = None):
    """Computes softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  **NOTE:**  While the classes are mutually exclusive, their probabilities
  need not be.  All that is required is that each row of `labels` is
  a valid probability distribution.  If they are not, the computation of the
  gradient will be incorrect.

  If using exclusive `labels` (wherein one and only
  one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

  Usage:

  >>> logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]
  >>> labels = [[1.0, 0.0, 0.0], [0.0, 0.8, 0.2]]
  >>> tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits)
  <tf.Tensor: shape=(2,), dtype=float32,
  numpy=array([0.16984604, 0.82474494], dtype=float32)>

  **WARNING:** This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  A common use case is to have logits and labels of shape
  `[batch_size, num_classes]`, but higher dimensions are supported, with
  the `axis` argument specifying the class dimension.

  `logits` and `labels` must have the same dtype (either `float16`, `float32`,
  or `float64`).

  Backpropagation will happen into both `logits` and `labels`.  To disallow
  backpropagation into `labels`, pass label tensors through `tf.stop_gradient`
  before feeding it to this function.

  **Note that to avoid confusion, it is required to pass only named arguments to
  this function.**

  Args:
    labels: Each vector along the class dimension should hold a valid
      probability distribution e.g. for the case in which labels are of shape
      `[batch_size, num_classes]`, each row of `labels[i]` must be a valid
      probability distribution.
    logits: Per-label activations, typically a linear output. These activation
      energies are interpreted as unnormalized log probabilities.
    axis: The class dimension. Defaulted to -1 which is the last dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` that contains the softmax cross entropy loss. Its type is the
    same as `logits` and its shape is the same as `labels` except that it does
    not have the last dimension of `labels`.
  """
def softmax_cross_entropy_with_logits_v2_helper(labels, logits, axis: Incomplete | None = None, name: Incomplete | None = None, dim: Incomplete | None = None):
    """Computes softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  **NOTE:**  While the classes are mutually exclusive, their probabilities
  need not be.  All that is required is that each row of `labels` is
  a valid probability distribution.  If they are not, the computation of the
  gradient will be incorrect.

  If using exclusive `labels` (wherein one and only
  one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

  **WARNING:** This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  A common use case is to have logits and labels of shape
  `[batch_size, num_classes]`, but higher dimensions are supported, with
  the `axis` argument specifying the class dimension.

  `logits` and `labels` must have the same dtype (either `float16`, `float32`,
  or `float64`).

  Backpropagation will happen into both `logits` and `labels`.  To disallow
  backpropagation into `labels`, pass label tensors through `tf.stop_gradient`
  before feeding it to this function.

  **Note that to avoid confusion, it is required to pass only named arguments to
  this function.**

  Args:
    labels: Each vector along the class dimension should hold a valid
      probability distribution e.g. for the case in which labels are of shape
      `[batch_size, num_classes]`, each row of `labels[i]` must be a valid
      probability distribution.
    logits: Unscaled log probabilities.
    axis: The class dimension. Defaulted to -1 which is the last dimension.
    name: A name for the operation (optional).
    dim: Deprecated alias for axis.

  Returns:
    A `Tensor` that contains the softmax cross entropy loss. Its type is the
    same as `logits` and its shape is the same as `labels` except that it does
    not have the last dimension of `labels`.
  """
def softmax_cross_entropy_with_logits(labels: Incomplete | None = None, logits: Incomplete | None = None, dim: int = -1, name: Incomplete | None = None, axis: Incomplete | None = None):
    """Computes softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  **NOTE:**  While the classes are mutually exclusive, their probabilities
  need not be.  All that is required is that each row of `labels` is
  a valid probability distribution.  If they are not, the computation of the
  gradient will be incorrect.

  If using exclusive `labels` (wherein one and only
  one class is true at a time), see `sparse_softmax_cross_entropy_with_logits`.

  **WARNING:** This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  A common use case is to have logits and labels of shape
  `[batch_size, num_classes]`, but higher dimensions are supported, with
  the `dim` argument specifying the class dimension.

  Backpropagation will happen only into `logits`.  To calculate a cross entropy
  loss that allows backpropagation into both `logits` and `labels`, see
  `tf.nn.softmax_cross_entropy_with_logits_v2`.

  **Note that to avoid confusion, it is required to pass only named arguments to
  this function.**

  Args:
    labels: Each vector along the class dimension should hold a valid
      probability distribution e.g. for the case in which labels are of shape
      `[batch_size, num_classes]`, each row of `labels[i]` must be a valid
      probability distribution.
    logits: Per-label activations, typically a linear output. These activation
      energies are interpreted as unnormalized log probabilities.
    dim: The class dimension. Defaulted to -1 which is the last dimension.
    name: A name for the operation (optional).
    axis: Alias for dim.

  Returns:
    A `Tensor` that contains the softmax cross entropy loss. Its type is the
    same as `logits` and its shape is the same as `labels` except that it does
    not have the last dimension of `labels`.
  """
def sparse_softmax_cross_entropy_with_logits(labels: Incomplete | None = None, logits: Incomplete | None = None, name: Incomplete | None = None):
    """Computes sparse softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  **NOTE:**  For this operation, the probability of a given label is considered
  exclusive.  That is, soft classes are not allowed, and the `labels` vector
  must provide a single specific index for the true class for each row of
  `logits` (each minibatch entry).  For soft softmax classification with
  a probability distribution for each entry, see
  `softmax_cross_entropy_with_logits_v2`.

  **WARNING:** This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  A common use case is to have logits of shape
  `[batch_size, num_classes]` and have labels of shape
  `[batch_size]`, but higher dimensions are supported, in which
  case the `dim`-th dimension is assumed to be of size `num_classes`.
  `logits` must have the dtype of `float16`, `float32`, or `float64`, and
  `labels` must have the dtype of `int32` or `int64`.

  **Note that to avoid confusion, it is required to pass only named arguments to
  this function.**

  Args:
    labels: `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of
      `labels` and result) and dtype `int32` or `int64`. Each entry in `labels`
      must be an index in `[0, num_classes)`. Other values will raise an
      exception when this op is run on CPU, and return `NaN` for corresponding
      loss and gradient rows on GPU.
    logits: Per-label activations (typically a linear output) of shape
      `[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float16`, `float32`, or
      `float64`. These activation energies are interpreted as unnormalized log
      probabilities.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of the same shape as `labels` and of the same type as `logits`
    with the softmax cross entropy loss.

  Raises:
    ValueError: If logits are scalars (need to have rank >= 1) or if the rank
      of the labels is not equal to the rank of the logits minus one.
  """
def sparse_softmax_cross_entropy_with_logits_v2(labels, logits, name: Incomplete | None = None):
    """Computes sparse softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  Note:  For this operation, the probability of a given label is considered
  exclusive.  That is, soft classes are not allowed, and the `labels` vector
  must provide a single specific index for the true class for each row of
  `logits` (each minibatch entry).  For soft softmax classification with
  a probability distribution for each entry, see
  `softmax_cross_entropy_with_logits_v2`.

  Warning: This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  A common use case is to have logits of shape
  `[batch_size, num_classes]` and have labels of shape
  `[batch_size]`, but higher dimensions are supported, in which
  case the `dim`-th dimension is assumed to be of size `num_classes`.
  `logits` must have the dtype of `float16`, `float32`, or `float64`, and
  `labels` must have the dtype of `int32` or `int64`.

  >>> logits = tf.constant([[2., -5., .5, -.1],
  ...                       [0., 0., 1.9, 1.4],
  ...                       [-100., 100., -100., -100.]])
  >>> labels = tf.constant([0, 3, 1])
  >>> tf.nn.sparse_softmax_cross_entropy_with_logits(
  ...     labels=labels, logits=logits).numpy()
  array([0.29750752, 1.1448325 , 0.        ], dtype=float32)

  To avoid confusion, passing only named arguments to this function is
  recommended.

  Args:
    labels: `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of
      `labels` and result) and dtype `int32` or `int64`. Each entry in `labels`
      must be an index in `[0, num_classes)`. Other values will raise an
      exception when this op is run on CPU, and return `NaN` for corresponding
      loss and gradient rows on GPU.
    logits: Unscaled log probabilities of shape `[d_0, d_1, ..., d_{r-1},
      num_classes]` and dtype `float16`, `float32`, or `float64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of the same shape as `labels` and of the same type as `logits`
    with the softmax cross entropy loss.

  Raises:
    ValueError: If logits are scalars (need to have rank >= 1) or if the rank
      of the labels is not equal to the rank of the logits minus one.
  """
def avg_pool_v2(input, ksize, strides, padding, data_format: Incomplete | None = None, name: Incomplete | None = None):
    '''Performs the avg pooling on the input.

  Each entry in `output` is the mean of the corresponding size `ksize`
  window in `value`.

  Args:
    input:  Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape +
      [num_channels]` if `data_format` does not start with "NC" (default), or
      `[batch_size, num_channels] + input_spatial_shape` if data_format starts
      with "NC". Pooling happens over the spatial dimensions only.
    ksize: An int or list of `ints` that has length `1`, `N` or `N+2`. The size
      of the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `N` or `N+2`. The
      stride of the sliding window for each dimension of the input tensor.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string. Specifies the channel dimension. For N=1 it can be
      either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default)
      or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW".
    name: Optional name for the operation.

  Returns:
    A `Tensor` of format specified by `data_format`.
    The average pooled output tensor.
  '''
def avg_pool(value, ksize, strides, padding, data_format: str = 'NHWC', name: Incomplete | None = None, input: Incomplete | None = None):
    '''Performs the average pooling on the input.

  Each entry in `output` is the mean of the corresponding size `ksize`
  window in `value`.

  Args:
    value: A 4-D `Tensor` of shape `[batch, height, width, channels]` and type
      `float32`, `float64`, `qint8`, `quint8`, or `qint32`.
    ksize: An int or list of `ints` that has length `1`, `2` or `4`. The size of
      the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `2` or `4`. The
      stride of the sliding window for each dimension of the input tensor.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm.
      See the "returns" section of `tf.nn.convolution` for details.
    data_format: A string. \'NHWC\' and \'NCHW\' are supported.
    name: Optional name for the operation.
    input: Alias for value.

  Returns:
    A `Tensor` with the same type as `value`.  The average pooled output tensor.
  '''
def avg_pool2d(input, ksize, strides, padding, data_format: str = 'NHWC', name: Incomplete | None = None):
    """Performs the average pooling on the input.

  Each entry in `output` is the mean of the corresponding size `ksize`
  window in `value`.

  Args:
    input: A 4-D `Tensor` of shape `[batch, height, width, channels]` and type
      `float32`, `float64`, `qint8`, `quint8`, or `qint32`.
    ksize: An int or list of `ints` that has length `1`, `2` or `4`. The size of
      the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `2` or `4`. The
      stride of the sliding window for each dimension of the input tensor.
    padding: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string. 'NHWC' and 'NCHW' are supported.
    name: Optional name for the operation.

  Returns:
    A `Tensor` with the same type as `value`.  The average pooled output tensor.
  """
def avg_pool1d(input, ksize, strides, padding, data_format: str = 'NWC', name: Incomplete | None = None):
    '''Performs the average pooling on the input.

  Each entry in `output` is the mean of the corresponding size `ksize`
  window in `value`.

  Note internally this op reshapes and uses the underlying 2d operation.

  Args:
    input: A 3-D `Tensor` of the format specified by `data_format`.
    ksize: An int or list of `ints` that has length `1` or `3`. The size of the
      window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1` or `3`. The stride of
      the sliding window for each dimension of the input tensor.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: An optional string from: "NWC", "NCW". Defaults to "NWC".
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.
  '''
def avg_pool3d(input, ksize, strides, padding, data_format: str = 'NDHWC', name: Incomplete | None = None):
    """Performs the average pooling on the input.

  Each entry in `output` is the mean of the corresponding size `ksize`
  window in `value`.

  Args:
    input: A 5-D `Tensor` of shape `[batch, depth, height, width, channels]`
      and type `float32`, `float64`, `qint8`, `quint8`, or `qint32`.
    ksize: An int or list of `ints` that has length `1`, `3` or `5`. The size of
      the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `3` or `5`. The
      stride of the sliding window for each dimension of the input tensor.
    padding: A string, either `'VALID'` or `'SAME'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A string. 'NDHWC' and 'NCDHW' are supported.
    name: Optional name for the operation.

  Returns:
    A `Tensor` with the same type as `value`.  The average pooled output tensor.
  """
def max_pool_v2(input, ksize, strides, padding, data_format: Incomplete | None = None, name: Incomplete | None = None):
    '''Performs max pooling on the input.

  For a given window of `ksize`, takes the maximum value within that window.
  Used for reducing computation and preventing overfitting.

  Consider an example of pooling with 2x2, non-overlapping windows:

  >>> matrix = tf.constant([
  ...     [0, 0, 1, 7],
  ...     [0, 2, 0, 0],
  ...     [5, 2, 0, 0],
  ...     [0, 0, 9, 8],
  ... ])
  >>> reshaped = tf.reshape(matrix, (1, 4, 4, 1))
  >>> tf.nn.max_pool(reshaped, ksize=2, strides=2, padding="SAME")
  <tf.Tensor: shape=(1, 2, 2, 1), dtype=int32, numpy=
  array([[[[2],
           [7]],
          [[5],
           [9]]]], dtype=int32)>

  We can adjust the window size using the `ksize` parameter. For example, if we
  were to expand the window to 3:

  >>> tf.nn.max_pool(reshaped, ksize=3, strides=2, padding="SAME")
  <tf.Tensor: shape=(1, 2, 2, 1), dtype=int32, numpy=
  array([[[[5],
           [7]],
          [[9],
           [9]]]], dtype=int32)>

  We\'ve now picked up two additional large numbers (5 and 9) in two of the
  pooled spots.

  Note that our windows are now overlapping, since we\'re still moving by 2 units
  on each iteration. This is causing us to see the same 9 repeated twice, since
  it is part of two overlapping windows.

  We can adjust how far we move our window with each iteration using the
  `strides` parameter. Updating this to the same value as our window size
  eliminates the overlap:

  >>> tf.nn.max_pool(reshaped, ksize=3, strides=3, padding="SAME")
  <tf.Tensor: shape=(1, 2, 2, 1), dtype=int32, numpy=
  array([[[[2],
           [7]],
          [[5],
           [9]]]], dtype=int32)>

  Because the window does not neatly fit into our input, padding is added around
  the edges, giving us the same result as when we used a 2x2 window. We can skip
  padding altogether and simply drop the windows that do not fully fit into our
  input by instead passing `"VALID"` to the `padding` argument:

  >>> tf.nn.max_pool(reshaped, ksize=3, strides=3, padding="VALID")
  <tf.Tensor: shape=(1, 1, 1, 1), dtype=int32, numpy=array([[[[5]]]],
   dtype=int32)>

  Now we\'ve grabbed the largest value in the 3x3 window starting from the upper-
  left corner. Since no other windows fit in our input, they are dropped.

  Args:
    input:  Tensor of rank N+2, of shape `[batch_size] + input_spatial_shape +
      [num_channels]` if `data_format` does not start with "NC" (default), or
      `[batch_size, num_channels] + input_spatial_shape` if data_format starts
      with "NC". Pooling happens over the spatial dimensions only.
    ksize: An int or list of `ints` that has length `1`, `N` or `N+2`. The size
      of the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `N` or `N+2`. The
      stride of the sliding window for each dimension of the input tensor.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information. When explicit padding is used and data_format is
      `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
      [pad_left, pad_right], [0, 0]]`. When explicit padding used and
      data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit
      padding, the size of the paddings cannot be greater than the sliding
      window size.
    data_format: A string. Specifies the channel dimension. For N=1 it can be
      either "NWC" (default) or "NCW", for N=2 it can be either "NHWC" (default)
      or "NCHW" and for N=3 either "NDHWC" (default) or "NCDHW".
    name: Optional name for the operation.

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.

  Raises:
    ValueError: If
      - explicit padding is used with an input tensor of rank 5.
      - explicit padding is used with data_format=\'NCHW_VECT_C\'.
  '''
def max_pool(value, ksize, strides, padding, data_format: str = 'NHWC', name: Incomplete | None = None, input: Incomplete | None = None):
    '''Performs the max pooling on the input.

  Args:
    value: A 4-D `Tensor` of the format specified by `data_format`.
    ksize: An int or list of `ints` that has length `1`, `2` or `4`.
      The size of the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `2` or `4`.
      The stride of the sliding window for each dimension of the input tensor.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. When explicit padding is used and
      data_format is `"NHWC"`, this should be in the form `[[0, 0], [pad_top,
      pad_bottom], [pad_left, pad_right], [0, 0]]`. When explicit padding used
      and data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
      [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit
      padding, the size of the paddings cannot be greater than the sliding
      window size.
    data_format: A string. \'NHWC\', \'NCHW\' and \'NCHW_VECT_C\' are supported.
    name: Optional name for the operation.
    input: Alias for value.

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.
  '''
def max_pool1d(input, ksize, strides, padding, data_format: str = 'NWC', name: Incomplete | None = None):
    '''Performs the max pooling on the input.

  Note internally this op reshapes and uses the underlying 2d operation.

  Args:
    input: A 3-D `Tensor` of the format specified by `data_format`.
    ksize: An int or list of `ints` that has length `1` or `3`. The size of the
      window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1` or `3`. The stride of
      the sliding window for each dimension of the input tensor.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information. When explicit padding is used and data_format is
      `"NWC"`, this should be in the form `[[0, 0], [pad_left, pad_right], [0,
      0]]`. When explicit padding used and data_format is `"NCW"`, this should
      be in the form `[[0, 0], [0, 0], [pad_left, pad_right]]`. When using
      explicit padding, the size of the paddings cannot be greater than the
      sliding window size.
    data_format: An optional string from: "NWC", "NCW". Defaults to "NWC".
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.
  '''
def max_pool2d(input, ksize, strides, padding, data_format: str = 'NHWC', name: Incomplete | None = None):
    '''Performs max pooling on 2D spatial data such as images.

  This is a more specific version of `tf.nn.max_pool` where the input tensor
  is 4D, representing 2D spatial data such as images. Using these APIs are
  equivalent

  Downsamples the input images along theirs spatial dimensions (height and
  width) by taking its maximum over an input window defined by `ksize`.
  The window is shifted by `strides` along each dimension.

  For example, for `strides=(2, 2)` and `padding=VALID` windows that extend
  outside of the input are not included in the output:

  >>> x = tf.constant([[1., 2., 3., 4.],
  ...                  [5., 6., 7., 8.],
  ...                  [9., 10., 11., 12.]])
  >>> # Add the `batch` and `channels` dimensions.
  >>> x = x[tf.newaxis, :, :, tf.newaxis]
  >>> result = tf.nn.max_pool2d(x, ksize=(2, 2), strides=(2, 2),
  ...                           padding="VALID")
  >>> result[0, :, :, 0]
  <tf.Tensor: shape=(1, 2), dtype=float32, numpy=
  array([[6., 8.]], dtype=float32)>

  With `padding=SAME`, we get:

  >>> x = tf.constant([[1., 2., 3., 4.],
  ...                  [5., 6., 7., 8.],
  ...                  [9., 10., 11., 12.]])
  >>> x = x[tf.newaxis, :, :, tf.newaxis]
  >>> result = tf.nn.max_pool2d(x, ksize=(2, 2), strides=(2, 2),
  ...                           padding=\'SAME\')
  >>> result[0, :, :, 0]
  <tf.Tensor: shape=(2, 2), dtype=float32, numpy=
  array([[ 6., 8.],
         [10.,12.]], dtype=float32)>

  We can also specify padding explicitly. The following example adds width-1
  padding on all sides (top, bottom, left, right):

  >>> x = tf.constant([[1., 2., 3., 4.],
  ...                  [5., 6., 7., 8.],
  ...                  [9., 10., 11., 12.]])
  >>> x = x[tf.newaxis, :, :, tf.newaxis]
  >>> result = tf.nn.max_pool2d(x, ksize=(2, 2), strides=(2, 2),
  ...                           padding=[[0, 0], [1, 1], [1, 1], [0, 0]])
  >>> result[0, :, :, 0]
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
  array([[ 1., 3., 4.],
         [ 9., 11., 12.]], dtype=float32)>

  For more examples and detail, see `tf.nn.max_pool`.

  Args:
    input: A 4-D `Tensor` of the format specified by `data_format`.
    ksize: An int or list of `ints` that has length `1`, `2` or `4`. The size of
      the window for each dimension of the input tensor. If only one integer is
      specified, then we apply the same window for all 4 dims. If two are
      provided then we use those for H, W dimensions and keep N, C dimension
      window size = 1.
    strides: An int or list of `ints` that has length `1`, `2` or `4`. The
      stride of the sliding window for each dimension of the input tensor. If
      only one integer is specified, we apply the same stride to all 4 dims. If
      two are provided we use those for the H, W dimensions and keep N, C of
      stride = 1.
    padding: Either the `string` `"SAME"` or `"VALID"` indicating the type of
      padding algorithm to use, or a list indicating the explicit paddings at
      the start and end of each dimension. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
        for more information. When explicit padding is used and data_format is
        `"NHWC"`, this should be in the form `[[0, 0], [pad_top, pad_bottom],
        [pad_left, pad_right], [0, 0]]`. When explicit padding used and
        data_format is `"NCHW"`, this should be in the form `[[0, 0], [0, 0],
        [pad_top, pad_bottom], [pad_left, pad_right]]`. When using explicit
        padding, the size of the paddings cannot be greater than the sliding
        window size.
    data_format: A string. \'NHWC\', \'NCHW\' and \'NCHW_VECT_C\' are supported.
    name: Optional name for the operation.

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.

  Raises:
    ValueError: If explicit padding is used with data_format=\'NCHW_VECT_C\'.
  '''
def max_pool3d(input, ksize, strides, padding, data_format: str = 'NDHWC', name: Incomplete | None = None):
    '''Performs the max pooling on the input.

  Args:
    input: A 5-D `Tensor` of the format specified by `data_format`.
    ksize: An int or list of `ints` that has length `1`, `3` or `5`. The size of
      the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `3` or `5`. The
      stride of the sliding window for each dimension of the input tensor.
    padding: A string, either `\'VALID\'` or `\'SAME\'`. The padding algorithm. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: An optional string from: "NDHWC", "NCDHW". Defaults to "NDHWC".
      The data format of the input and output data. With the default format
      "NDHWC", the data is stored in the order of: [batch, in_depth, in_height,
        in_width, in_channels]. Alternatively, the format could be "NCDHW", the
      data storage order is: [batch, in_channels, in_depth, in_height,
        in_width].
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of format specified by `data_format`.
    The max pooled output tensor.
  '''
def max_pool_with_argmax_v2(input, ksize, strides, padding, data_format: str = 'NHWC', output_dtype=..., include_batch_in_index: bool = False, name: Incomplete | None = None):
    '''Performs max pooling on the input and outputs both max values and indices.

  The indices in `argmax` are flattened, so that a maximum value at position
  `[b, y, x, c]` becomes flattened index: `(y * width + x) * channels + c` if
  `include_batch_in_index` is False;
  `((b * height + y) * width + x) * channels + c`
  if `include_batch_in_index` is True.

  The indices returned are always in `[0, height) x [0, width)` before
  flattening, even if padding is involved and the mathematically correct answer
  is outside (either negative or too large).  This is a bug, but fixing it is
  difficult to do in a safe backwards compatible way, especially due to
  flattening.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`,
      `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`,
      `uint32`, `uint64`.
      4-D with shape `[batch, height, width, channels]`.  Input to pool over.
    ksize: An int or list of `ints` that has length `1`, `2` or `4`.
      The size of the window for each dimension of the input tensor.
    strides: An int or list of `ints` that has length `1`, `2` or `4`.
      The stride of the sliding window for each dimension of the
      input tensor.
    padding: A `string` from: `"SAME", "VALID"`.
      The type of padding algorithm to use. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: An optional `string`, must be set to `"NHWC"`. Defaults to
      `"NHWC"`.
      Specify the data format of the input and output data.
    output_dtype: An optional `tf.DType` from: `tf.int32, tf.int64`.
      Defaults to `tf.int64`.
      The dtype of the returned argmax tensor.
    include_batch_in_index: An optional `boolean`. Defaults to `False`.
      Whether to include batch dimension in flattened index of `argmax`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, argmax).

    output: A `Tensor`. Has the same type as `input`.
    argmax: A `Tensor` of type `output_dtype`.
  '''
def max_pool_with_argmax_v1(input, ksize, strides, padding, data_format: str = 'NHWC', Targmax: Incomplete | None = None, name: Incomplete | None = None, output_dtype: Incomplete | None = None, include_batch_in_index: bool = False): ...
def xw_plus_b(x, weights, biases, name: Incomplete | None = None):
    '''Computes matmul(x, weights) + biases.

  Args:
    x: a 2D tensor.  Dimensions typically: batch, in_units
    weights: a 2D tensor.  Dimensions typically: in_units, out_units
    biases: a 1D tensor.  Dimensions: out_units
    name: A name for the operation (optional).  If not specified
      "xw_plus_b" is used.

  Returns:
    A 2-D Tensor computing matmul(x, weights) + biases.
    Dimensions typically: batch, out_units.
  '''
def xw_plus_b_v1(x, weights, biases, name: Incomplete | None = None):
    '''Computes matmul(x, weights) + biases.

  This is a deprecated version of that will soon be removed.

  Args:
    x: a 2D tensor.  Dimensions typically: batch, in_units
    weights: a 2D tensor.  Dimensions typically: in_units, out_units
    biases: a 1D tensor.  Dimensions: out_units
    name: A name for the operation (optional).  If not specified
      "xw_plus_b_v1" is used.

  Returns:
    A 2-D Tensor computing matmul(x, weights) + biases.
    Dimensions typically: batch, out_units.
  '''
def dropout(x, keep_prob: Incomplete | None = None, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None, rate: Incomplete | None = None):
    """Computes dropout.

  For each element of `x`, with probability `rate`, outputs `0`, and otherwise
  scales up the input by `1 / (1-rate)`. The scaling is such that the expected
  sum is unchanged.

  By default, each element is kept or dropped independently.  If `noise_shape`
  is specified, it must be
  [broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
  will make independent decisions.  For example, if `shape(x) = [k, l, m, n]`
  and `noise_shape = [k, 1, 1, n]`, each batch and channel component will be
  kept independently and each row and column will be kept or not kept together.

  Args:
    x: A floating point tensor.
    keep_prob: (deprecated) A deprecated alias for `(1-rate)`.
    noise_shape: A 1-D integer `Tensor`, representing the
      shape for randomly generated keep/drop flags.
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.
    name: A name for this operation (optional).
    rate: A scalar `Tensor` with the same type as `x`. The probability that each
      element of `x` is discarded.

  Returns:
    A Tensor of the same shape of `x`.

  Raises:
    ValueError: If `rate` is not in `[0, 1)` or if `x` is not a floating
      point tensor.
  """
def dropout_v2(x, rate, noise_shape: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None):
    """Computes dropout: randomly sets elements to zero to prevent overfitting.

  Warning: You should consider using
  `tf.nn.experimental.stateless_dropout` instead of this function. The
  difference between `tf.nn.experimental.stateless_dropout` and this
  function is analogous to the difference between
  `tf.random.stateless_uniform` and `tf.random.uniform`. Please see
  [Random number
  generation](https://www.tensorflow.org/guide/random_numbers) guide
  for a detailed description of the various RNG systems in TF. As the
  guide states, legacy stateful RNG ops like `tf.random.uniform` and
  `tf.nn.dropout` are not deprecated yet but highly discouraged,
  because their states are hard to control.

  Note: The behavior of dropout has changed between TensorFlow 1.x and 2.x.
  When converting 1.x code, please use named arguments to ensure behavior stays
  consistent.

  See also: `tf.keras.layers.Dropout` for a dropout layer.

  [Dropout](https://arxiv.org/abs/1207.0580) is useful for regularizing DNN
  models. Inputs elements are randomly set to zero (and the other elements are
  rescaled). This encourages each node to be independently useful, as it cannot
  rely on the output of other nodes.

  More precisely: With probability `rate` elements of `x` are set to `0`.
  The remaining elements are scaled up by `1.0 / (1 - rate)`, so that the
  expected value is preserved.

  >>> tf.random.set_seed(0)
  >>> x = tf.ones([3,5])
  >>> tf.nn.dropout(x, rate = 0.5, seed = 1).numpy()
  array([[2., 0., 0., 2., 2.],
       [2., 2., 2., 2., 2.],
       [2., 0., 2., 0., 2.]], dtype=float32)

  >>> tf.random.set_seed(0)
  >>> x = tf.ones([3,5])
  >>> tf.nn.dropout(x, rate = 0.8, seed = 1).numpy()
  array([[0., 0., 0., 5., 5.],
       [0., 5., 0., 5., 0.],
       [5., 0., 5., 0., 5.]], dtype=float32)

  >>> tf.nn.dropout(x, rate = 0.0) == x
  <tf.Tensor: shape=(3, 5), dtype=bool, numpy=
    array([[ True,  True,  True,  True,  True],
           [ True,  True,  True,  True,  True],
           [ True,  True,  True,  True,  True]])>


  By default, each element is kept or dropped independently.  If `noise_shape`
  is specified, it must be
  [broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
  will make independent decisions. This is useful for dropping whole
  channels from an image or sequence. For example:

  >>> tf.random.set_seed(0)
  >>> x = tf.ones([3,10])
  >>> tf.nn.dropout(x, rate = 2/3, noise_shape=[1,10], seed=1).numpy()
  array([[0., 0., 0., 3., 3., 0., 3., 3., 3., 0.],
       [0., 0., 0., 3., 3., 0., 3., 3., 3., 0.],
       [0., 0., 0., 3., 3., 0., 3., 3., 3., 0.]], dtype=float32)

  Args:
    x: A floating point tensor.
    rate: A scalar `Tensor` with the same type as x. The probability
      that each element is dropped. For example, setting rate=0.1 would drop
      10% of input elements.
    noise_shape: A 1-D integer `Tensor`, representing the
      shape for randomly generated keep/drop flags.
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.
    name: A name for this operation (optional).

  Returns:
    A Tensor of the same shape of `x`.

  Raises:
    ValueError: If `rate` is not in `[0, 1)` or if `x` is not a floating point
      tensor. `rate=1` is disallowed, because the output would be all zeros,
      which is likely not what was intended.
  """
def stateless_dropout(x, rate, seed, rng_alg: Incomplete | None = None, noise_shape: Incomplete | None = None, name: Incomplete | None = None):
    '''Computes dropout: randomly sets elements to zero to prevent overfitting.

  [Dropout](https://arxiv.org/abs/1207.0580) is useful for regularizing DNN
  models. Inputs elements are randomly set to zero (and the other elements are
  rescaled). This encourages each node to be independently useful, as it cannot
  rely on the output of other nodes.

  More precisely: With probability `rate` elements of `x` are set to `0`.
  The remaining elements are scaled up by `1.0 / (1 - rate)`, so that the
  expected value is preserved.

  >>> x = tf.ones([3,5])
  >>> tf.nn.experimental.stateless_dropout(x, rate=0.5, seed=[1, 0])
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[2., 0., 2., 0., 0.],
         [0., 0., 2., 0., 2.],
         [0., 0., 0., 0., 2.]], dtype=float32)>

  >>> x = tf.ones([3,5])
  >>> tf.nn.experimental.stateless_dropout(x, rate=0.8, seed=[1, 0])
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[5., 0., 0., 0., 0.],
         [0., 0., 0., 0., 5.],
         [0., 0., 0., 0., 5.]], dtype=float32)>

  >>> tf.nn.experimental.stateless_dropout(x, rate=0.0, seed=[1, 0]) == x
  <tf.Tensor: shape=(3, 5), dtype=bool, numpy=
  array([[ True,  True,  True,  True,  True],
         [ True,  True,  True,  True,  True],
         [ True,  True,  True,  True,  True]])>


  This function is a stateless version of `tf.nn.dropout`, in the
  sense that no matter how many times you call this function, the same
  `seed` will lead to the same results, and different `seed` will lead
  to different results.

  >>> x = tf.ones([3,5])
  >>> tf.nn.experimental.stateless_dropout(x, rate=0.8, seed=[1, 0])
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[5., 0., 0., 0., 0.],
         [0., 0., 0., 0., 5.],
         [0., 0., 0., 0., 5.]], dtype=float32)>
  >>> tf.nn.experimental.stateless_dropout(x, rate=0.8, seed=[1, 0])
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[5., 0., 0., 0., 0.],
         [0., 0., 0., 0., 5.],
         [0., 0., 0., 0., 5.]], dtype=float32)>
  >>> tf.nn.experimental.stateless_dropout(x, rate=0.8, seed=[2, 0])
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[5., 0., 0., 0., 0.],
         [0., 0., 0., 5., 0.],
         [0., 0., 0., 0., 0.]], dtype=float32)>
  >>> tf.nn.experimental.stateless_dropout(x, rate=0.8, seed=[2, 0])
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[5., 0., 0., 0., 0.],
         [0., 0., 0., 5., 0.],
         [0., 0., 0., 0., 0.]], dtype=float32)>

  Compare the above results to those of `tf.nn.dropout` below. The
  second time `tf.nn.dropout` is called with the same seed, it will
  give a different output.

  >>> tf.random.set_seed(0)
  >>> x = tf.ones([3,5])
  >>> tf.nn.dropout(x, rate=0.8, seed=1)
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[0., 0., 0., 5., 5.],
         [0., 5., 0., 5., 0.],
         [5., 0., 5., 0., 5.]], dtype=float32)>
  >>> tf.nn.dropout(x, rate=0.8, seed=1)
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[0., 0., 0., 0., 0.],
         [0., 0., 0., 5., 0.],
         [0., 0., 0., 0., 0.]], dtype=float32)>
  >>> tf.nn.dropout(x, rate=0.8, seed=2)
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[0., 0., 0., 0., 0.],
         [0., 5., 0., 5., 0.],
         [0., 0., 0., 0., 0.]], dtype=float32)>
  >>> tf.nn.dropout(x, rate=0.8, seed=2)
  <tf.Tensor: shape=(3, 5), dtype=float32, numpy=
  array([[0., 0., 0., 0., 0.],
         [5., 0., 5., 0., 5.],
         [0., 5., 0., 0., 5.]], dtype=float32)>

  The difference between this function and `tf.nn.dropout` is
  analogous to the difference between `tf.random.stateless_uniform`
  and `tf.random.uniform`. Please see [Random number
  generation](https://www.tensorflow.org/guide/random_numbers) guide
  for a detailed description of the various RNG systems in TF. As the
  guide states, legacy stateful RNG ops like `tf.random.uniform` and
  `tf.nn.dropout` are not deprecated yet but highly discouraged,
  because their states are hard to control.

  By default, each element is kept or dropped independently.  If `noise_shape`
  is specified, it must be
  [broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
  will make independent decisions. This is useful for dropping whole
  channels from an image or sequence. For example:

  >>> x = tf.ones([3,10])
  >>> tf.nn.experimental.stateless_dropout(x, rate=2/3, noise_shape=[1,10],
  ...                                      seed=[1, 0])
  <tf.Tensor: shape=(3, 10), dtype=float32, numpy=
  array([[3., 0., 0., 0., 0., 0., 0., 3., 0., 3.],
         [3., 0., 0., 0., 0., 0., 0., 3., 0., 3.],
         [3., 0., 0., 0., 0., 0., 0., 3., 0., 3.]], dtype=float32)>

  Args:
    x: A floating point tensor.
    rate: A scalar `Tensor` with the same type as x. The probability
      that each element is dropped. For example, setting rate=0.1 would drop
      10% of input elements.
    seed: An integer tensor of shape `[2]`. The seed of the random numbers.
    rng_alg: The algorithm used to generate the random numbers
      (default to `"auto_select"`). See the `alg` argument of
      `tf.random.stateless_uniform` for the supported values.
    noise_shape: A 1-D integer `Tensor`, representing the
      shape for randomly generated keep/drop flags.
    name: A name for this operation.

  Returns:
    A Tensor of the same shape and dtype of `x`.

  Raises:
    ValueError: If `rate` is not in `[0, 1)` or if `x` is not a floating point
      tensor. `rate=1` is disallowed, because the output would be all zeros,
      which is likely not what was intended.
  '''
def general_dropout(x, rate, uniform_sampler, noise_shape: Incomplete | None = None, name: Incomplete | None = None):
    """Computes dropout: randomly sets elements to zero to prevent overfitting.

  Please see `tf.nn.experimental.stateless_dropout` for an overview
  of dropout.

  Unlike `tf.nn.experimental.stateless_dropout`, here you can supply a
  custom sampler function `uniform_sampler` that (given a shape and a
  dtype) generates a random, `Uniform[0, 1)`-distributed tensor (of
  that shape and dtype).  `uniform_sampler` can be
  e.g. `tf.random.stateless_random_uniform` or
  `tf.random.Generator.uniform`.

  For example, if you are using `tf.random.Generator` to generate
  random numbers, you can use this code to do dropouts:

  >>> g = tf.random.Generator.from_seed(7)
  >>> sampler = g.uniform
  >>> x = tf.constant([1.1, 2.2, 3.3, 4.4, 5.5])
  >>> rate = 0.5
  >>> tf.nn.experimental.general_dropout(x, rate, sampler)
  <tf.Tensor: shape=(5,), ..., numpy=array([ 0. ,  4.4,  6.6,  8.8, 11. ], ...)>
  >>> tf.nn.experimental.general_dropout(x, rate, sampler)
  <tf.Tensor: shape=(5,), ..., numpy=array([2.2, 0. , 0. , 8.8, 0. ], ...)>

  It has better performance than using
  `tf.nn.experimental.stateless_dropout` and
  `tf.random.Generator.make_seeds`:

  >>> g = tf.random.Generator.from_seed(7)
  >>> x = tf.constant([1.1, 2.2, 3.3, 4.4, 5.5])
  >>> rate = 0.5
  >>> tf.nn.experimental.stateless_dropout(x, rate, g.make_seeds(1)[:, 0])
  <tf.Tensor: shape=(5,), ..., numpy=array([ 2.2,  4.4,  6.6,  0. , 11. ], ...)>
  >>> tf.nn.experimental.stateless_dropout(x, rate, g.make_seeds(1)[:, 0])
  <tf.Tensor: shape=(5,), ..., numpy=array([2.2, 0. , 6.6, 8.8, 0. ], ...>

  because generating and consuming seeds cost extra
  computation. `tf.nn.experimental.general_dropout` can let you avoid
  them.

  Args:
    x: A floating point tensor.
    rate: A scalar `Tensor` with the same type as x. The probability
      that each element is dropped. For example, setting rate=0.1 would drop
      10% of input elements.
    uniform_sampler: a callable of signature `(shape, dtype) ->
      Tensor[shape, dtype]`, used to generate a tensor of uniformly-distributed
      random numbers in the range `[0, 1)`, of the given shape and dtype.
    noise_shape: A 1-D integer `Tensor`, representing the
      shape for randomly generated keep/drop flags.
    name: A name for this operation.

  Returns:
    A Tensor of the same shape and dtype of `x`.

  Raises:
    ValueError: If `rate` is not in `[0, 1)` or if `x` is not a floating point
      tensor. `rate=1` is disallowed, because the output would be all zeros,
      which is likely not what was intended.
  """
def top_k(input, k: int = 1, sorted: bool = True, name: Incomplete | None = None):
    """Finds values and indices of the `k` largest entries for the last dimension.

  If the input is a vector (rank=1), finds the `k` largest entries in the vector
  and outputs their values and indices as vectors.  Thus `values[j]` is the
  `j`-th largest entry in `input`, and its index is `indices[j]`.

  >>> result = tf.math.top_k([1, 2, 98, 1, 1, 99, 3, 1, 3, 96, 4, 1],
  ...                         k=3)
  >>> result.values.numpy()
  array([99, 98, 96], dtype=int32)
  >>> result.indices.numpy()
  array([5, 2, 9], dtype=int32)

  For matrices (resp. higher rank input), computes the top `k` entries in each
  row (resp. vector along the last dimension).  Thus,

  >>> input = tf.random.normal(shape=(3,4,5,6))
  >>> k = 2
  >>> values, indices  = tf.math.top_k(input, k=k)
  >>> values.shape.as_list()
  [3, 4, 5, 2]
  >>>
  >>> values.shape == indices.shape == input.shape[:-1] + [k]
  True

  The indices can be used to `gather` from a tensor who's shape matches `input`.

  >>> gathered_values = tf.gather(input, indices, batch_dims=-1)
  >>> assert tf.reduce_all(gathered_values == values)

  If two elements are equal, the lower-index element appears first.

  >>> result = tf.math.top_k([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
  ...                        k=3)
  >>> result.indices.numpy()
  array([0, 1, 3], dtype=int32)

  Args:
    input: 1-D or higher `Tensor` with last dimension at least `k`.
    k: 0-D `int32` `Tensor`.  Number of top elements to look for along the last
      dimension (along each row for matrices).
    sorted: If true the resulting `k` elements will be sorted by the values in
      descending order.
    name: Optional name for the operation.

  Returns:
    A tuple with two named fields:
    values: The `k` largest elements along each last dimensional slice.
    indices: The indices of `values` within the last dimension of `input`.
  """
def approx_max_k(operand, k, reduction_dimension: int = -1, recall_target: float = 0.95, reduction_input_size_override: int = -1, aggregate_to_topk: bool = True, name: Incomplete | None = None):
    """Returns max `k` values and their indices of the input `operand` in an approximate manner.

  See https://arxiv.org/abs/2206.14286 for the algorithm details. This op is
  only optimized on TPU currently.

  Args:
    operand : Array to search for max-k. Must be a floating number type.
    k : Specifies the number of max-k.
    reduction_dimension : Integer dimension along which to search. Default: -1.
    recall_target : Recall target for the approximation.
    reduction_input_size_override : When set to a positive value, it overrides
      the size determined by `operand[reduction_dim]` for evaluating the recall.
      This option is useful when the given `operand` is only a subset of the
      overall computation in SPMD or distributed pipelines, where the true input
      size cannot be deferred by the `operand` shape.
    aggregate_to_topk : When true, aggregates approximate results to top-k. When
      false, returns the approximate results. The number of the approximate
      results is implementation defined and is greater equals to the specified
      `k`.
    name: Optional name for the operation.

  Returns:
    Tuple of two arrays. The arrays are the max `k` values and the
    corresponding indices along the `reduction_dimension` of the input
    `operand`. The arrays' dimensions are the same as the input `operand`
    except for the `reduction_dimension`: when `aggregate_to_topk` is true,
    the reduction dimension is `k`; otherwise, it is greater equals to `k`
    where the size is implementation-defined.

  We encourage users to wrap `approx_max_k` with jit. See the following
  example for maximal inner production search (MIPS):

  >>> import tensorflow as tf
  >>> @tf.function(jit_compile=True)
  ... def mips(qy, db, k=10, recall_target=0.95):
  ...   dists = tf.einsum('ik,jk->ij', qy, db)
  ...   # returns (f32[qy_size, k], i32[qy_size, k])
  ...   return tf.nn.approx_max_k(dists, k=k, recall_target=recall_target)
  >>>
  >>> qy = tf.random.uniform((256,128))
  >>> db = tf.random.uniform((2048,128))
  >>> dot_products, neighbors = mips(qy, db, k=20)
  """
def approx_min_k(operand, k, reduction_dimension: int = -1, recall_target: float = 0.95, reduction_input_size_override: int = -1, aggregate_to_topk: bool = True, name: Incomplete | None = None):
    """Returns min `k` values and their indices of the input `operand` in an approximate manner.

  See https://arxiv.org/abs/2206.14286 for the algorithm details. This op is
  only optimized on TPU currently.

  Args:
    operand : Array to search for min-k. Must be a floating number type.
    k : Specifies the number of min-k.
    reduction_dimension: Integer dimension along which to search. Default: -1.
    recall_target: Recall target for the approximation.
    reduction_input_size_override : When set to a positive value, it overrides
      the size determined by `operand[reduction_dim]` for evaluating the recall.
      This option is useful when the given `operand` is only a subset of the
      overall computation in SPMD or distributed pipelines, where the true input
      size cannot be deferred by the `operand` shape.
    aggregate_to_topk: When true, aggregates approximate results to top-k. When
      false, returns the approximate results. The number of the approximate
      results is implementation defined and is greater equals to the specified
      `k`.
    name: Optional name for the operation.

  Returns:
    Tuple of two arrays. The arrays are the least `k` values and the
    corresponding indices along the `reduction_dimension` of the input
    `operand`.  The arrays' dimensions are the same as the input `operand`
    except for the `reduction_dimension`: when `aggregate_to_topk` is true,
    the reduction dimension is `k`; otherwise, it is greater equals to `k`
    where the size is implementation-defined.

  We encourage users to wrap `approx_min_k` with jit. See the following example
  for nearest neighbor search over the squared l2 distance:

  >>> import tensorflow as tf
  >>> @tf.function(jit_compile=True)
  ... def l2_ann(qy, db, half_db_norms, k=10, recall_target=0.95):
  ...   dists = half_db_norms - tf.einsum('ik,jk->ij', qy, db)
  ...   return tf.nn.approx_min_k(dists, k=k, recall_target=recall_target)
  >>>
  >>> qy = tf.random.uniform((256,128))
  >>> db = tf.random.uniform((2048,128))
  >>> half_db_norms = tf.norm(db, axis=1) / 2
  >>> dists, neighbors = l2_ann(qy, db, half_db_norms)

  In the example above, we compute `db_norms/2 - dot(qy, db^T)` instead of
  `qy^2 - 2 dot(qy, db^T) + db^2` for performance reason. The former uses less
  arithmetics and produces the same set of neighbors.
  """
def nth_element(input, n, reverse: bool = False, name: Incomplete | None = None):
    """Finds values of the `n`-th smallest value for the last dimension.

  Note that n is zero-indexed.

  If the input is a vector (rank-1), finds the entries which is the nth-smallest
  value in the vector and outputs their values as scalar tensor.

  For matrices (resp. higher rank input), computes the entries which is the
  nth-smallest value in each row (resp. vector along the last dimension). Thus,

      values.shape = input.shape[:-1]

  Args:
    input: 1-D or higher `Tensor` with last dimension at least `n+1`.
    n: A `Tensor` of type `int32`.
      0-D. Position of sorted vector to select along the last dimension (along
      each row for matrices). Valid range of n is `[0, input.shape[:-1])`
    reverse: An optional `bool`. Defaults to `False`.
      When set to True, find the nth-largest value in the vector and vice
      versa.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
    The `n`-th order statistic along each last dimensional slice.
  """
def fractional_max_pool(value, pooling_ratio, pseudo_random: bool = False, overlapping: bool = False, deterministic: bool = False, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    '''Performs fractional max pooling on the input.

  This is a deprecated version of `fractional_max_pool`.

  Fractional max pooling is slightly different than regular max pooling.  In
  regular max pooling, you downsize an input set by taking the maximum value of
  smaller N x N subsections of the set (often 2x2), and try to reduce the set by
  a factor of N, where N is an integer.  Fractional max pooling, as you might
  expect from the word "fractional", means that the overall reduction ratio N
  does not have to be an integer.

  The sizes of the pooling regions are generated randomly but are fairly
  uniform.  For example, let\'s look at the height dimension, and the constraints
  on the list of rows that will be pool boundaries.

  First we define the following:

  1.  input_row_length : the number of rows from the input set
  2.  output_row_length : which will be smaller than the input
  3.  alpha = input_row_length / output_row_length : our reduction ratio
  4.  K = floor(alpha)
  5.  row_pooling_sequence : this is the result list of pool boundary rows

  Then, row_pooling_sequence should satisfy:

  1.  a[0] = 0 : the first value of the sequence is 0
  2.  a[end] = input_row_length : the last value of the sequence is the size
  3.  K <= (a[i+1] - a[i]) <= K+1 : all intervals are K or K+1 size
  4.  length(row_pooling_sequence) = output_row_length+1

  Args:
    value: A `Tensor`. 4-D with shape `[batch, height, width, channels]`.
    pooling_ratio: A list of `floats` that has length >= 4.  Pooling ratio for
      each dimension of `value`, currently only supports row and col dimension
      and should be >= 1.0. For example, a valid pooling ratio looks like [1.0,
      1.44, 1.73, 1.0]. The first and last elements must be 1.0 because we don\'t
      allow pooling on batch and channels dimensions.  1.44 and 1.73 are pooling
      ratio on height and width dimensions respectively.
    pseudo_random: An optional `bool`.  Defaults to `False`. When set to `True`,
      generates the pooling sequence in a pseudorandom fashion, otherwise, in a
      random fashion. Check (Graham, 2015) for difference between
      pseudorandom and random.
    overlapping: An optional `bool`.  Defaults to `False`.  When set to `True`,
      it means when pooling, the values at the boundary of adjacent pooling
      cells are used by both cells. For example:
      `index  0  1  2  3  4`
      `value  20 5  16 3  7`
      If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used
      twice.  The result would be [20, 16] for fractional max pooling.
    deterministic: An optional `bool`.  Deprecated; use `fractional_max_pool_v2`
      instead.
    seed: An optional `int`.  Defaults to `0`.  If set to be non-zero, the
      random number generator is seeded by the given seed.  Otherwise it is
      seeded by a random seed.
    seed2: An optional `int`.  Deprecated; use `fractional_max_pool_v2` instead.
    name: A name for the operation (optional).

  Returns:
  A tuple of `Tensor` objects (`output`, `row_pooling_sequence`,
  `col_pooling_sequence`).
    output: Output `Tensor` after fractional max pooling.  Has the same type as
      `value`.
    row_pooling_sequence: A `Tensor` of type `int64`.
    col_pooling_sequence: A `Tensor` of type `int64`.

  Raises:
    ValueError: If op determinism is enabled and either the seeds are not set or
      the "deterministic" argument is False.

  References:
    Fractional Max-Pooling:
      [Graham, 2015](https://arxiv.org/abs/1412.6071)
      ([pdf](https://arxiv.org/pdf/1412.6071.pdf))
  '''
def fractional_max_pool_v2(value, pooling_ratio, pseudo_random: bool = False, overlapping: bool = False, seed: int = 0, name: Incomplete | None = None):
    '''Performs fractional max pooling on the input.

  Fractional max pooling is slightly different than regular max pooling.  In
  regular max pooling, you downsize an input set by taking the maximum value of
  smaller N x N subsections of the set (often 2x2), and try to reduce the set by
  a factor of N, where N is an integer.  Fractional max pooling, as you might
  expect from the word "fractional", means that the overall reduction ratio N
  does not have to be an integer.

  The sizes of the pooling regions are generated randomly but are fairly
  uniform.  For example, let\'s look at the height dimension, and the constraints
  on the list of rows that will be pool boundaries.

  First we define the following:

  1.  input_row_length : the number of rows from the input set
  2.  output_row_length : which will be smaller than the input
  3.  alpha = input_row_length / output_row_length : our reduction ratio
  4.  K = floor(alpha)
  5.  row_pooling_sequence : this is the result list of pool boundary rows

  Then, row_pooling_sequence should satisfy:

  1.  a[0] = 0 : the first value of the sequence is 0
  2.  a[end] = input_row_length : the last value of the sequence is the size
  3.  K <= (a[i+1] - a[i]) <= K+1 : all intervals are K or K+1 size
  4.  length(row_pooling_sequence) = output_row_length+1

  Args:
    value: A `Tensor`. 4-D with shape `[batch, height, width, channels]`.
    pooling_ratio: An int or list of `ints` that has length `1`, `2` or `4`.
      Pooling ratio for each dimension of `value`, currently only supports row
      and col dimension and should be >= 1.0. For example, a valid pooling ratio
      looks like [1.0, 1.44, 1.73, 1.0]. The first and last elements must be 1.0
      because we don\'t allow pooling on batch and channels dimensions.  1.44 and
      1.73 are pooling ratio on height and width dimensions respectively.
    pseudo_random: An optional `bool`.  Defaults to `False`. When set to `True`,
      generates the pooling sequence in a pseudorandom fashion, otherwise, in a
      random fashion. Check paper (Graham, 2015) for difference between
      pseudorandom and random.
    overlapping: An optional `bool`.  Defaults to `False`.  When set to `True`,
      it means when pooling, the values at the boundary of adjacent pooling
      cells are used by both cells. For example:
      `index  0  1  2  3  4`
      `value  20 5  16 3  7`
      If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used
      twice.  The result would be [20, 16] for fractional max pooling.
    seed: An optional `int`.  Defaults to `0`.  If set to be non-zero, the
      random number generator is seeded by the given seed.  Otherwise it is
      seeded by a random seed.
    name: A name for the operation (optional).

  Returns:
  A tuple of `Tensor` objects (`output`, `row_pooling_sequence`,
  `col_pooling_sequence`).
    output: Output `Tensor` after fractional max pooling.  Has the same type as
      `value`.
    row_pooling_sequence: A `Tensor` of type `int64`.
    col_pooling_sequence: A `Tensor` of type `int64`.

  Raises:
    ValueError: If no seed is specified and op determinism is enabled.

  References:
    Fractional Max-Pooling:
      [Graham, 2015](https://arxiv.org/abs/1412.6071)
      ([pdf](https://arxiv.org/pdf/1412.6071.pdf))
  '''
def fractional_avg_pool(value, pooling_ratio, pseudo_random: bool = False, overlapping: bool = False, deterministic: bool = False, seed: int = 0, seed2: int = 0, name: Incomplete | None = None):
    """Performs fractional average pooling on the input.

  This is a deprecated version of `fractional_avg_pool`.

  Fractional average pooling is similar to Fractional max pooling in the pooling
  region generation step. The only difference is that after pooling regions are
  generated, a mean operation is performed instead of a max operation in each
  pooling region.

  Args:
    value: A `Tensor`. 4-D with shape `[batch, height, width, channels]`.
    pooling_ratio: A list of `floats` that has length >= 4.  Pooling ratio for
      each dimension of `value`, currently only supports row and col dimension
      and should be >= 1.0. For example, a valid pooling ratio looks like [1.0,
      1.44, 1.73, 1.0]. The first and last elements must be 1.0 because we don't
      allow pooling on batch and channels dimensions.  1.44 and 1.73 are pooling
      ratio on height and width dimensions respectively.
    pseudo_random: An optional `bool`.  Defaults to `False`. When set to `True`,
      generates the pooling sequence in a pseudorandom fashion, otherwise, in a
      random fashion. Check paper (Graham, 2015) for difference between
      pseudorandom and random.
    overlapping: An optional `bool`.  Defaults to `False`.  When set to `True`,
      it means when pooling, the values at the boundary of adjacent pooling
      cells are used by both cells. For example:
      `index  0  1  2  3  4`
      `value  20 5  16 3  7`
      If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used
      twice.  The result would be [20, 16] for fractional avg pooling.
    deterministic: An optional `bool`.  Deprecated; use `fractional_avg_pool_v2`
      instead.
    seed: An optional `int`.  Defaults to `0`.  If set to be non-zero, the
      random number generator is seeded by the given seed.  Otherwise it is
      seeded by a random seed.
    seed2: An optional `int`.  Deprecated; use `fractional_avg_pool_v2` instead.
    name: A name for the operation (optional).

  Returns:
  A tuple of `Tensor` objects (`output`, `row_pooling_sequence`,
  `col_pooling_sequence`).
    output: Output `Tensor` after fractional avg pooling.  Has the same type as
      `value`.
    row_pooling_sequence: A `Tensor` of type `int64`.
    col_pooling_sequence: A `Tensor` of type `int64`.

  References:
    Fractional Max-Pooling:
      [Graham, 2015](https://arxiv.org/abs/1412.6071)
      ([pdf](https://arxiv.org/pdf/1412.6071.pdf))
  """
def fractional_avg_pool_v2(value, pooling_ratio, pseudo_random: bool = False, overlapping: bool = False, seed: int = 0, name: Incomplete | None = None):
    """Performs fractional average pooling on the input.

  Fractional average pooling is similar to Fractional max pooling in the pooling
  region generation step. The only difference is that after pooling regions are
  generated, a mean operation is performed instead of a max operation in each
  pooling region.

  Args:
    value: A `Tensor`. 4-D with shape `[batch, height, width, channels]`.
    pooling_ratio: A list of `floats` that has length >= 4.  Pooling ratio for
      each dimension of `value`, currently only supports row and col dimension
      and should be >= 1.0. For example, a valid pooling ratio looks like [1.0,
      1.44, 1.73, 1.0]. The first and last elements must be 1.0 because we don't
      allow pooling on batch and channels dimensions.  1.44 and 1.73 are pooling
      ratio on height and width dimensions respectively.
    pseudo_random: An optional `bool`.  Defaults to `False`. When set to `True`,
      generates the pooling sequence in a pseudorandom fashion, otherwise, in a
      random fashion. Check paper (Graham, 2015) for difference between
      pseudorandom and random.
    overlapping: An optional `bool`.  Defaults to `False`.  When set to `True`,
      it means when pooling, the values at the boundary of adjacent pooling
      cells are used by both cells. For example:
      `index  0  1  2  3  4`
      `value  20 5  16 3  7`
      If the pooling sequence is [0, 2, 4], then 16, at index 2 will be used
      twice.  The result would be [20, 16] for fractional avg pooling.
    seed: An optional `int`.  Defaults to `0`.  If set to be non-zero, the
      random number generator is seeded by the given seed.  Otherwise it is
      seeded by a random seed.
    name: A name for the operation (optional).

  Returns:
  A tuple of `Tensor` objects (`output`, `row_pooling_sequence`,
  `col_pooling_sequence`).
    output: Output `Tensor` after fractional avg pooling.  Has the same type as
      `value`.
    row_pooling_sequence: A `Tensor` of type `int64`.
    col_pooling_sequence: A `Tensor` of type `int64`.

  References:
    Fractional Max-Pooling:
      [Graham, 2015](https://arxiv.org/abs/1412.6071)
      ([pdf](https://arxiv.org/pdf/1412.6071.pdf))
  """
def erosion2d(value, kernel, strides, rates, padding, name: Incomplete | None = None):
    '''Computes the grayscale erosion of 4-D `value` and 3-D `kernel` tensors.

  The `value` tensor has shape `[batch, in_height, in_width, depth]` and the
  `kernel` tensor has shape `[kernel_height, kernel_width, depth]`, i.e.,
  each input channel is processed independently of the others with its own
  structuring function. The `output` tensor has shape
  `[batch, out_height, out_width, depth]`. The spatial dimensions of the
  output tensor depend on the `padding` algorithm. We currently only support the
  default "NHWC" `data_format`.

  In detail, the grayscale morphological 2-D erosion is given by:

      output[b, y, x, c] =
         min_{dy, dx} value[b,
                            strides[1] * y - rates[1] * dy,
                            strides[2] * x - rates[2] * dx,
                            c] -
                      kernel[dy, dx, c]

  Duality: The erosion of `value` by the `kernel` is equal to the negation of
  the dilation of `-value` by the reflected `kernel`.

  Args:
    value: A `Tensor`. 4-D with shape `[batch, in_height, in_width, depth]`.
    kernel: A `Tensor`. Must have the same type as `value`.
      3-D with shape `[kernel_height, kernel_width, depth]`.
    strides: A list of `ints` that has length `>= 4`.
      1-D of length 4. The stride of the sliding window for each dimension of
      the input tensor. Must be: `[1, stride_height, stride_width, 1]`.
    rates: A list of `ints` that has length `>= 4`.
      1-D of length 4. The input stride for atrous morphological dilation.
      Must be: `[1, rate_height, rate_width, 1]`.
    padding: A `string` from: `"SAME", "VALID"`.
      The type of padding algorithm to use.
    name: A name for the operation (optional). If not specified "erosion2d"
      is used.

  Returns:
    A `Tensor`. Has the same type as `value`.
    4-D with shape `[batch, out_height, out_width, depth]`.
  Raises:
    ValueError: If the `value` depth does not match `kernel`\' shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`.
  '''
def erosion2d_v2(value, filters, strides, padding, data_format, dilations, name: Incomplete | None = None):
    '''Computes the grayscale erosion of 4-D `value` and 3-D `filters` tensors.

  The `value` tensor has shape `[batch, in_height, in_width, depth]` and the
  `filters` tensor has shape `[filters_height, filters_width, depth]`, i.e.,
  each input channel is processed independently of the others with its own
  structuring function. The `output` tensor has shape
  `[batch, out_height, out_width, depth]`. The spatial dimensions of the
  output tensor depend on the `padding` algorithm. We currently only support the
  default "NHWC" `data_format`.

  In detail, the grayscale morphological 2-D erosion is given by:

      output[b, y, x, c] =
         min_{dy, dx} value[b,
                            strides[1] * y - dilations[1] * dy,
                            strides[2] * x - dilations[2] * dx,
                            c] -
                      filters[dy, dx, c]

  Duality: The erosion of `value` by the `filters` is equal to the negation of
  the dilation of `-value` by the reflected `filters`.

  Args:
    value: A `Tensor`. 4-D with shape `[batch, in_height, in_width, depth]`.
    filters: A `Tensor`. Must have the same type as `value`.
      3-D with shape `[filters_height, filters_width, depth]`.
    strides: A list of `ints` that has length `>= 4`.
      1-D of length 4. The stride of the sliding window for each dimension of
      the input tensor. Must be: `[1, stride_height, stride_width, 1]`.
    padding: A `string` from: `"SAME", "VALID"`.
      The type of padding algorithm to use. See
      [here](https://www.tensorflow.org/api_docs/python/tf/nn#notes_on_padding_2)
      for more information.
    data_format: A `string`, only `"NHWC"` is currently supported.
    dilations: A list of `ints` that has length `>= 4`.
      1-D of length 4. The input stride for atrous morphological dilation.
      Must be: `[1, rate_height, rate_width, 1]`.
    name: A name for the operation (optional). If not specified "erosion2d"
      is used.

  Returns:
    A `Tensor`. Has the same type as `value`.
    4-D with shape `[batch, out_height, out_width, depth]`.

  Raises:
    ValueError: If the `value` depth does not match `filters`\' shape, or if
      padding is other than `\'VALID\'` or `\'SAME\'`.
  '''
def in_top_k(predictions, targets, k, name: Incomplete | None = None):
    """Says whether the targets are in the top `K` predictions.

  This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the
  prediction for the target class is finite (not inf, -inf, or nan) and among
  the top `k` predictions among all predictions for example `i`. Note that the
  behavior of `InTopK` differs from the `TopK` op in its handling of ties; if
  multiple classes have the same prediction value and straddle the top-`k`
  boundary, all of those classes are considered to be in the top `k`.

  More formally, let

    \\\\(predictions_i\\\\) be the predictions for all classes for example `i`,
    \\\\(targets_i\\\\) be the target class for example `i`,
    \\\\(out_i\\\\) be the output for example `i`,

  $$out_i = predictions_{i, targets_i} \\in TopKIncludingTies(predictions_i)$$

  Args:
    predictions: A `Tensor` of type `float32`.
      A `batch_size` x `classes` tensor.
    targets: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A `batch_size` vector of class ids.
    k: An `int`. Number of top elements to look at for computing precision.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`. Computed Precision at `k` as a `bool Tensor`.
  """
def in_top_k_v2(targets, predictions, k, name: Incomplete | None = None):
    """Outputs whether the targets are in the top `K` predictions.

  This outputs a `batch_size` bool array, an entry `out[i]` is `true` if the
  prediction for the target class is finite (not inf, -inf, or nan) and among
  the top `k` predictions among all predictions for example `i`.
  `predictions` does not have to be normalized.

  Note that the behavior of `InTopK` differs from the `TopK` op in its handling
  of ties; if multiple classes have the same prediction value and straddle the
  top-`k` boundary, all of those classes are considered to be in the top `k`.

  >>> target = tf.constant([0, 1, 3])
  >>> pred = tf.constant([
  ...  [1.2, -0.3, 2.8, 5.2],
  ...  [0.1, 0.0, 0.0, 0.0],
  ...  [0.0, 0.5, 0.3, 0.3]],
  ...  dtype=tf.float32)
  >>> print(tf.math.in_top_k(target, pred, 2))
  tf.Tensor([False  True  True], shape=(3,), dtype=bool)

  Args:
    targets: A `batch_size` vector of class ids. Must be `int32` or `int64`.
    predictions: A `batch_size` x `classes` tensor of type `float32`.
    k: An `int`. The parameter to specify search space.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` with the same shape of `targets` with type of `bool`. Each
      element specifies if the target falls into top-k predictions.
  """
def isotonic_regression(inputs, decreasing: bool = True, axis: int = -1):
    """Solves isotonic regression problems along the given axis.

  For each vector x, the problem solved is

  $$\\argmin_{y_1 >= y_2 >= ... >= y_n} \\sum_i (x_i - y_i)^2.$$

  As the solution is component-wise constant, a second tensor is returned that
  encodes the segments. The problems are solved over the given axis.

  Consider the following example, where we solve a batch of two problems. The
  first input is [3, 1, 2], while the second [1, 3, 4] (as the axis is 1).
  >>> x = tf.constant([[3, 1, 2], [1, 3, 4]], dtype=tf.float32)
  >>> y, segments = tf.nn.isotonic_regression(x, axis=1)
  >>> y  # The solution.
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
  array([[3.       , 1.5      , 1.5      ],
         [2.6666667, 2.6666667, 2.6666667]], dtype=float32)>

  Note that the first solution has two blocks [2] and [1.5, 1.5]. The second
  solution is constant, and thus has a single segment. These segments are
  exactly what the second returned tensor encodes:

  >>> segments
  <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
  array([[0, 1, 1],
         [0, 0, 0]], dtype=int32)>


  Args:
    inputs: A tensor holding the inputs.
    decreasing: If set to False, the inequalities in the optimizing constrained
      are flipped.
    axis: The axis along which the problems should be solved.

  Returns:
    output: The solutions, same shape as type as the input.
    segments: An int32 tensor, same shape as the input indicating the segments
      that have the same value. Specifically, those positions that have the same
      value correspond to the same segment. These values start at zero, and are
      monotonously increasing for each solution.
  """
