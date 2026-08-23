from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def uniform_dequantize(input, scales, zero_points, Tout, quantization_min_val, quantization_max_val, quantization_axis: int = -1, name: Incomplete | None = None):
    """Perform dequantization on the quantized Tensor `input`.

  Given quantized `input` which was quantized using `scales` and `zero_points`, performs dequantization using the formula:
  dequantized_data = (quantized_data - zero_point) * scale.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `qint32`.
      Must be a Tensor of Tin.
    scales: A `Tensor` of type `float32`.
      The float value(s) used as scale(s) when quantizing original data that input represents.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (input.dim_size(quantization_axis),) (per-axis quantization).
    zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point(s) when quantizing original data that input represents.
      Same shape condition as scales.
    Tout: A `tf.DType` from: `tf.float32`.
      The type of output Tensor. A tf.DType from: tf.qint8, tf.qint32
    quantization_min_val: An `int`.
      The quantization min value that was used when input was quantized.
      The purpose of this attribute is typically (but not limited to) to indicate narrow range, where this is set to:
      `(Tin lowest) + 1` if narrow range, and `(Tin lowest)` otherwise.
      For example, if Tin is qint8, this is set to -127 if narrow range quantized or -128 if not.
    quantization_max_val: An `int`.
      The quantization max value that was used when input was quantized.
      The purpose of this attribute is typically (but not limited to) indicate narrow range, where this is set to:
      `(Tout max)` for both narrow range and not narrow range.
      For example, if Tin is qint8, this is set to 127.
    quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization. Otherwise, it must be set within range [0, input.dims()).
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

UniformDequantize: Incomplete

def uniform_dequantize_eager_fallback(input, scales, zero_points, Tout, quantization_min_val, quantization_max_val, quantization_axis, name, ctx): ...
def uniform_quantize(input, scales, zero_points, Tout, quantization_min_val, quantization_max_val, quantization_axis: int = -1, name: Incomplete | None = None):
    """Perform quantization on Tensor `input`.

  Given `input`, `scales` and `zero_points`, performs quantization using the formula:
  quantized_data = floor(input_data * (1.0f / scale) + 0.5f) + zero_point

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`.
      Must be a Tensor of Tin.
    scales: A `Tensor` of type `float32`.
      The float value(s) to use as scale(s) to quantize `input`.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (input.dim_size(quantization_axis),) (per-axis quantization).
    zero_points: A `Tensor` of type `int32`.
      The int32 value(s) to use as zero_point(s) to quantize `input`.
      Same shape condition as scales.
    Tout: A `tf.DType` from: `tf.qint8, tf.qint32`.
      The type of output Tensor. A tf.DType from: tf.float32
    quantization_min_val: An `int`.
      The quantization min value to quantize `input`.
      The purpose of this attribute is typically (but not limited to) to indicate narrow range, where this is set to:
      `(Tin lowest) + 1` if narrow range, and `(Tin lowest)` otherwise.
      For example, if Tin is qint8, this is set to -127 if narrow range quantized or -128 if not.
    quantization_max_val: An `int`.
      The quantization max value to quantize `input`.
      The purpose of this attribute is typically (but not limited to) indicate narrow range, where this is set to:
      `(Tout max)` for both narrow range and not narrow range.
      For example, if Tin is qint8, this is set to 127.
    quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization. Otherwise, it must be set within range [0, input.dims()).
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

UniformQuantize: Incomplete

def uniform_quantize_eager_fallback(input, scales, zero_points, Tout, quantization_min_val, quantization_max_val, quantization_axis, name, ctx): ...
def uniform_quantized_add(lhs, rhs, lhs_scales, lhs_zero_points, rhs_scales, rhs_zero_points, output_scales, output_zero_points, lhs_quantization_min_val, lhs_quantization_max_val, rhs_quantization_min_val, rhs_quantization_max_val, output_quantization_min_val, output_quantization_max_val, lhs_quantization_axis: int = -1, rhs_quantization_axis: int = -1, output_quantization_axis: int = -1, name: Incomplete | None = None):
    """Perform quantized add of quantized Tensor `lhs` and quantized Tensor `rhs` to make quantized `output`.

  Given quantized `lhs` and quantized `rhs`, performs quantized add on `lhs` and `rhs` to make quantized `output`.

  `UniformQuantizedAdd` follows Numpy broadcasting rules.
  The two input array shapes are compared element-wise.
  Starting with the trailing dimensions, the two dimensions either have to be equal or one of them needs to be 1.

  `lhs` and `rhs` must be quantized Tensor, where data value is quantized using the formula:
  ```
  quantized_data = clip(original_data / scale + zero_point, quantization_min_val, quantization_max_val)
  ```
  `output` is also quantized, using the same formula.

  If `lhs` and `output` is both per-axis quantized, the quantization axis must match.
  Also, if `rhs` and `output` is both per-axis quantized, the quantization axis must match.
  *Match* means the axis must match when adding, regarding the broadcasting.
  i.e. For both operands `lhs` and `rhs`,
  if `operand.quantization_axis` >= 0 and `output.quantization_axis` >= 0,
  `operand.dims` - `operand.quantization_axis` must be equal to `output.dims` - `output.quantization_axis`.

  Args:
    lhs: A `Tensor`. Must be one of the following types: `qint32`.
      Must be a quantized tensor.
    rhs: A `Tensor`. Must have the same type as `lhs`.
      Must be a quantized tensor.
    lhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale factors when quantizing the original data that `lhs` represents.
    lhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero points when quantizing original data that `lhs` represents.
      Must have same shape with `lhs_scales`.
    rhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale factors when quantizing the original data that `rhs` represents.
    rhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero points when quantizing original data that `rhs` represents.
      Must have same shape with `rhs_scales`.
    output_scales: A `Tensor` of type `float32`.
      The float value(s) to use as scale factors when quantizing original data that `output` represents.
    output_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero points when quantizing original data that output represents.
      Must have same shape with `output_scales`.
    lhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in `lhs`.
      For example, if `Tin` is `qint8`, this must be set to -127 if narrow range quantized or -128 if not.
    lhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in `lhs`.
      For example, if `Tin` is `qint8`, this must be set to 127.
    rhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in `rhs`.
      For example, if `Tin` is `qint8`, this must be set to -127 if narrow range quantized or -128 if not.
    rhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in `rhs`.
      For example, if `Tin` is `qint8`, this must be set to 127.
    output_quantization_min_val: An `int`.
      The min value of the quantized data stored in `output`.
      For example, if  `Tout` is `qint8`, this must be set to -127 if narrow range quantized or -128 if not.
    output_quantization_max_val: An `int`.
      The max value of the quantized data stored in `output`.
      For example, if `Tout` is `qint8`, this must be set to 127.
    lhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `lhs`, only per-tensor quantization is supported.
      Thus, this must be set to -1.
      Other values will raise error at OpKernel construction.
    rhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `rhs`, only per-tensor quantization
      or per-channel quantization along `kernel_output_feature_dimension` is supported.
      Thus, this must be set to -1 or `dimension_numbers.kernel_output_feature_dimension`.
      Other values will raise error at OpKernel construction.
    output_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `output`, only per-tensor quantization or per-channel quantization along `output_feature_dimension` is supported.
      Thus, this must be set to -1 or `dimension_numbers.output_feature_dimension`.
      Other values will raise error at OpKernel construction.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `lhs`.
  """

UniformQuantizedAdd: Incomplete

def uniform_quantized_add_eager_fallback(lhs, rhs, lhs_scales, lhs_zero_points, rhs_scales, rhs_zero_points, output_scales, output_zero_points, lhs_quantization_min_val, lhs_quantization_max_val, rhs_quantization_min_val, rhs_quantization_max_val, output_quantization_min_val, output_quantization_max_val, lhs_quantization_axis, rhs_quantization_axis, output_quantization_axis, name, ctx): ...
def uniform_quantized_clip_by_value(operand, min, max, scales, zero_points, quantization_min_val, quantization_max_val, quantization_axis: int = -1, name: Incomplete | None = None):
    """Perform clip by value on the quantized Tensor `operand`.

  Given quantized `operand` which was quantized using `scales` and `zero_points`, performs clip by value using `min` and `max` values.
  If quantization_axis is -1 (per-tensor quantized), the entire operand is clipped using scalar min, max.
  Otherwise (per-channel quantized), the clipping is also done per-channel.

  Args:
    operand: A `Tensor`. Must be one of the following types: `qint32`.
      Must be a Tensor of T.
    min: A `Tensor`. Must have the same type as `operand`.
      The min value(s) to clip operand. Must be a Tensor of T.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (operand.dim_size(quantization_axis),) (per-axis quantization).
    max: A `Tensor`. Must have the same type as `operand`.
      The min value(s) to clip operand. Must be a Tensor of T.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (operand.dim_size(quantization_axis),) (per-axis quantization).
    scales: A `Tensor` of type `float32`.
      The float value(s) used as scale(s) when quantizing `operand`, `min` and `max`.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (operand.dim_size(quantization_axis),) (per-axis quantization).
    zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point(s) when quantizing `operand`, `min` and `max`.
      Same shape condition as scales.
    quantization_min_val: An `int`.
      The quantization min value that was used when operand was quantized.
    quantization_max_val: An `int`.
      The quantization max value that was used when operand was quantized.
    quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization. Otherwise, it must be set within range [0, operand.dims()).
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `operand`.
  """

UniformQuantizedClipByValue: Incomplete

def uniform_quantized_clip_by_value_eager_fallback(operand, min, max, scales, zero_points, quantization_min_val, quantization_max_val, quantization_axis, name, ctx): ...
def uniform_quantized_convolution(lhs, rhs, lhs_scales, lhs_zero_points, rhs_scales, rhs_zero_points, output_scales, output_zero_points, Tout, padding, lhs_quantization_min_val, lhs_quantization_max_val, rhs_quantization_min_val, rhs_quantization_max_val, output_quantization_min_val, output_quantization_max_val, window_strides=[], explicit_padding=[], lhs_dilation=[], rhs_dilation=[], batch_group_count: int = 1, feature_group_count: int = 1, dimension_numbers: str = '', lhs_quantization_axis: int = -1, rhs_quantization_axis: int = -1, output_quantization_axis: int = -1, name: Incomplete | None = None):
    '''Perform quantized convolution of quantized Tensor `lhs` and quantized Tensor `rhs`. to make quantized `output`.

  Given quantized `lhs` and quantized `rhs`, performs quantized dot on `lhs` and `rhs` to make quantized `output`.

  `lhs` and `rhs` must be Tensors of same rank, and meet following shape conditions.
  - `lhs_feature` % `feature_group_count` == 0
  - `lhs_feature` % `rhs_input_feature` == 0
  - `lhs_feature` / `feature_group_count` == `rhs_input_feature`
  - `rhs_output_feature` % `feature_group_count` == 0
  - `lhs_batch` % `batch_group_count` == 0
  - `rhs_output_feature` % `batch_group_count` == 0

  `lhs` and `rhs` must be quantized Tensor, where data value is quantized using the formula:
  ```
  quantized_data = clip(original_data / scale + zero_point, quantization_min_val, quantization_max_val)
  ```
  `output` is also quantized, using the same formula.
  If `rhs` is per-tensor quantized, `output` must be also per-tensor quantized.

  Args:
    lhs: A `Tensor`. Must be one of the following types: `qint8`.
      Must be a quantized tensor, rank >= 3.
    rhs: A `Tensor`. Must have the same type as `lhs`.
      Must be a quantized tensor, same rank as `lhs`.
    lhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale factors when quantizing the original data that `lhs` represents.
      Must be a scalar `Tensor` (`lhs` supports only per-tensor quantization).
    lhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero points when quantizing original data that `lhs` represents.
      Same shape condition as `lhs_scales`.
    rhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale factors when quantizing the original data that `rhs` represents.
      Must be a scalar `Tensor` for per-tensor quantization,
      or 1D `Tensor` of size `rhs.dim_size(kernel_output_feature_dimension)`, for per-channel quantization.
    rhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero points when quantizing original data that `rhs` represents.
      Same shape condition as `rhs_scales`.
    output_scales: A `Tensor` of type `float32`.
      The float value(s) to use as scale factors when quantizing original data that `output` represents.
      Must be a scalar `Tensor` for per-tensor quantization,
      or 1D `Tensor` of size `rhs.dim_size(kernel_output_feature_dimension)`
      - which is equal to `output.dim_size(output_feature_dimension)`,
      for per-channel quantization.
      If `rhs` is per-tensor quantized, output must be also per-tensor quantized.
      This means that if `rhs_scales` and `rhs_zero_points` are scalar `Tensor`s, `output_scales` and `output_zero_points` must be scalar `Tensor`s as well.
    output_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero points when quantizing original data that output represents.
      Same shape condition as `output_scales`.
    Tout: A `tf.DType` from: `tf.qint32`. The type of `output` `Tensor`.
    padding: A `string`.
      string from: `"SAME"`, `"VALID"`, or `"EXPLICIT"`, indicating the type of padding algorithm to use.
    lhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in `lhs`.
      For example, if `Tin` is `qint8`, this must be set to -127 if narrow range quantized or -128 if not.
    lhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in `lhs`.
      For example, if `Tin` is `qint8`, this must be set to 127.
    rhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in `rhs`.
      For example, if `Tin` is `qint8`, this must be set to -127 if narrow range quantized or -128 if not.
    rhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in `rhs`.
      For example, if `Tin` is `qint8`, this must be set to 127.
    output_quantization_min_val: An `int`.
      The min value of the quantized data stored in `output`.
      For example, if  `Tout` is `qint8`, this must be set to -127 if narrow range quantized or -128 if not.
    output_quantization_max_val: An `int`.
      The max value of the quantized data stored in `output`.
      For example, if `Tout` is `qint8`, this must be set to 127.
    window_strides: An optional list of `ints`. Defaults to `[]`.
      The stride of the sliding window for each spatial dimension of `lhs`.
      Must be an empty list (default) or a list of size (number of spatial dimensions).
      If an empty list is provided, the stride for each spatial dimension is set to 1.
    explicit_padding: An optional list of `ints`. Defaults to `[]`.
      If `padding` is `"EXPLICIT"`, must be set as a list indicating
      the explicit paddings at the start and end of each `lhs` spatial dimension.
      Otherwise, this must be empty.

      (If used,) Must be a list of size `2 * (number of lhs spatial dimensions)`,
      where `(explicit_padding[2 * i], explicit_padding[2 * i + 1])` indicates
      `(start_padding, end_padding)` of `spatial_dimensions[i]`.
    lhs_dilation: An optional list of `ints`. Defaults to `[]`.
      The dilation factor to apply in each spatial dimension of `lhs`.
      Must be an empty list (default) or a list of size (number of `lhs` spatial dimensions).
      If empty list, the dilation for each `lhs` spatial dimension is set to 1.
    rhs_dilation: An optional list of `ints`. Defaults to `[]`.
      The dilation factor to apply in each spatial dimension of `rhs`.
      Must be an empty list (default) or a list of size (number of `rhs` spatial dimensions).
      If empty list, the dilation for each `rhs` spatial dimension is set to 1.
    batch_group_count: An optional `int`. Defaults to `1`.
      The number of batch groups. Used for grouped filters.
      Must be a divisor of `output_feature`.
    feature_group_count: An optional `int`. Defaults to `1`.
      The number of feature groups. Used for grouped convolutions.
      Must be a divisor of both `lhs_feature` and `output_feature`.
    dimension_numbers: An optional `string`. Defaults to `""`.
      Structure of dimension information for the convolution op.
      Must be an empty string (default) or a serialized string of `tensorflow.UniformQuantizedConvolutionDimensionNumbersAttr` proto.
      If empty string, the default is `("NCHW", "OIHW", "NCHW")` (for a 2D convolution).
    lhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `lhs`, only per-tensor quantization is supported.
      Thus, this must be set to -1.
      Other values will raise error at OpKernel construction.
    rhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `rhs`, only per-tensor quantization
      or per-channel quantization along `kernel_output_feature_dimension` is supported.
      Thus, this must be set to -1 or `dimension_numbers.kernel_output_feature_dimension`.
      Other values will raise error at OpKernel construction.
    output_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `output`, only per-tensor quantization or per-channel quantization along `output_feature_dimension` is supported.
      Thus, this must be set to -1 or `dimension_numbers.output_feature_dimension`.
      Other values will raise error at OpKernel construction.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  '''

UniformQuantizedConvolution: Incomplete

def uniform_quantized_convolution_eager_fallback(lhs, rhs, lhs_scales, lhs_zero_points, rhs_scales, rhs_zero_points, output_scales, output_zero_points, Tout, padding, lhs_quantization_min_val, lhs_quantization_max_val, rhs_quantization_min_val, rhs_quantization_max_val, output_quantization_min_val, output_quantization_max_val, window_strides, explicit_padding, lhs_dilation, rhs_dilation, batch_group_count, feature_group_count, dimension_numbers, lhs_quantization_axis, rhs_quantization_axis, output_quantization_axis, name, ctx): ...
def uniform_quantized_convolution_hybrid(lhs, rhs, rhs_scales, rhs_zero_points, Tout, padding, rhs_quantization_min_val, rhs_quantization_max_val, window_strides=[], explicit_padding=[], lhs_dilation=[], rhs_dilation=[], batch_group_count: int = 1, feature_group_count: int = 1, dimension_numbers: str = '', rhs_quantization_axis: int = -1, name: Incomplete | None = None):
    '''Perform hybrid quantized convolution of float Tensor `lhs` and quantized Tensor `rhs`.

  Given float `lhs` and quantized `rhs`, internally performs quantization on `lhs`,
  and then performs quantized convolution on quantized `lhs` and `rhs`.

  The internal quantization on `lhs` is a quantization to `Trhs`, dynamic range,
  per-batch (per-axis along axis `dimension_numbers.input_batch_dimension`), asymmetric,
  and not narrow range (the range is [Trhs_MIN, Trhs_MAX]).

  `lhs` and `rhs` must be Tensors of same rank, and meet following shape conditions.
  - lhs_feature % feature_group_count == 0
  - lhs_feature % rhs_input_feature == 0
  - lhs_feature / feature_group_count == rhs_input_feature
  - rhs_output_feature % feature_group_count == 0
  - lhs_batch % batch_group_count == 0
  - rhs_output_feature % batch_group_count == 0

  `rhs` must be quantized Tensor, where its data value is quantized using the formula:
  quantized_data = clip(original_data / scale + zero_point, quantization_min_val, quantization_max_val).

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`.
      Must be a non-quantized Tensor of `Tlhs`, rank >= 3.
    rhs: A `Tensor`. Must be one of the following types: `qint8`.
      Must be a quantized Tensor of `Trhs`, same rank as `lhs`.
    rhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale factors when quantizing the original data that `rhs` represents.
      Must be a scalar Tensor for per-tensor quantization,
      or 1D Tensor of size `rhs.dim_size(kernel_output_feature_dimension)`, for per-channel quantization.
    rhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point when quantizing original data that `rhs` represents.
      Same shape condition as `rhs_scales`.
    Tout: A `tf.DType` from: `tf.float32`. The type of output Tensor.
    padding: A `string`.
      string from: `"SAME"`, `"VALID"`, or `"EXPLICIT"`, indicating the type of padding algorithm to use.
    rhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in `rhs`.
      For example, if `Trhs` is qint8, this must be set to -127 if narrow range quantized or -128 if not.
    rhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in `rhs`.
      For example, if `Trhs` is qint8, this must be set to 127.
    window_strides: An optional list of `ints`. Defaults to `[]`.
      The stride of the sliding window for each spatial dimension of `lhs`.
      Must be an empty list (default) or a list of size (number of spatial dimensions).
      If an empty list is provided, the stride for each spatial dimension is set to 1.
    explicit_padding: An optional list of `ints`. Defaults to `[]`.
      If `padding` Attr is `"EXPLICIT"`, must be set as a list indicating
      the explicit paddings at the start and end of each lhs spatial dimension.
      Otherwise, this Attr is must be empty.

      (If used,) Must be a list of size 2 * (number of lhs spatial dimensions),
      where (explicit_padding[2 * i], explicit_padding[2 * i + 1]) indicates
      spatial_dimensions[i] (start_padding, end_padding).
    lhs_dilation: An optional list of `ints`. Defaults to `[]`.
      The dilation factor to apply in each spatial dimension of `lhs`.
      Must be an empty list (default) or a list of size (number of lhs spatial dimensions).
      If empty list, the dilation for each lhs spatial dimension is set to 1.
    rhs_dilation: An optional list of `ints`. Defaults to `[]`.
      The dilation factor to apply in each spatial dimension of `rhs`.
      Must be an empty list (default) or a list of size (number of rhs spatial dimensions).
      If empty list, the dilation for each rhs spatial dimension is set to 1.
    batch_group_count: An optional `int`. Defaults to `1`.
      The number of batch groups. Used for grouped filters.
      Must be a divisor of output_feature.
    feature_group_count: An optional `int`. Defaults to `1`.
      The number of feature groups. Used for grouped convolutions.
      Must be a divisor of both lhs_feature and output_feature.
    dimension_numbers: An optional `string`. Defaults to `""`.
      Structure of dimension information for the convolution op.
      Must be an empty string (default) or a serialized string of tensorflow.UniformQuantizedConvolutionDimensionNumbersAttr proto.
      If empty string, the default is `("NCHW", "OIHW", "NCHW")` (for a 2D convolution).
    rhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For the `rhs`, only per-tensor quantization
      or per-channel quantization along kernel_output_feature_dimension is supported.
      Thus, this attribute must be set to -1 or `dimension_numbers.kernel_output_feature_dimension`.
      Other values will raise error at OpKernel construction.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  '''

UniformQuantizedConvolutionHybrid: Incomplete

def uniform_quantized_convolution_hybrid_eager_fallback(lhs, rhs, rhs_scales, rhs_zero_points, Tout, padding, rhs_quantization_min_val, rhs_quantization_max_val, window_strides, explicit_padding, lhs_dilation, rhs_dilation, batch_group_count, feature_group_count, dimension_numbers, rhs_quantization_axis, name, ctx): ...
def uniform_quantized_dot(lhs, rhs, lhs_scales, lhs_zero_points, rhs_scales, rhs_zero_points, output_scales, output_zero_points, Tout, lhs_quantization_min_val, lhs_quantization_max_val, rhs_quantization_min_val, rhs_quantization_max_val, output_quantization_min_val, output_quantization_max_val, lhs_quantization_axis: int = -1, rhs_quantization_axis: int = -1, output_quantization_axis: int = -1, name: Incomplete | None = None):
    """Perform quantized dot of quantized Tensor `lhs` and quantized Tensor `rhs` to make quantized `output`.

  Given quantized `lhs` and quantized `rhs`, performs quantized dot on `lhs` and `rhs` to make quantized `output`.
  `lhs` and `rhs` must be 2D Tensors and the lhs.dim_size(1) must match rhs.dim_size(0).
  `lhs` and `rhs` must be quantized Tensor, where data value is quantized using the formula:
  quantized_data = clip(original_data / scale + zero_point, quantization_min_val, quantization_max_val).
  `output` is also quantized, using the same formula.
  If `rhs` is per-tensor quantized, `output` must be also per-tensor quantized.

  Args:
    lhs: A `Tensor`. Must be one of the following types: `qint8`.
      Must be a 2D Tensor of Tin.
    rhs: A `Tensor`. Must have the same type as `lhs`.
      Must be a 2D Tensor of Tin.
    lhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale when quantizing original data that lhs represents.
      Must be a scalar Tensor (lhs supports only per-tensor quantization).
    lhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point when quantizing original data that lhs represents.
      Same shape condition as lhs_scales.
    rhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale when quantizing original data that rhs represents.
      Must be a scalar Tensor (per-tensor quantization) or 1D Tensor of size (rhs.dim_size(1),) (per-channel quantization).
    rhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point when quantizing original data that rhs represents.
      Same shape condition as rhs_scales.
    output_scales: A `Tensor` of type `float32`.
      The float value(s) to use as scales when quantizing original data that output represents.
      Must be a scalar Tensor (per-tensor quantization) or 1D Tensor of size (output.dim_size(1),) (per-channel quantization).
      If rhs is per-tensor quantized, output must be also per-tensor quantized.
      This means that if rhs_scales and rhs_zero_points are scalar Tensors, output_scales and output_zero_points must be scalar Tensors as well.
    output_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point when quantizing original data that output represents.
      Same shape condition as rhs_scales.
    Tout: A `tf.DType` from: `tf.qint32`. The type of output Tensor.
    lhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in lhs.
      For example, if Tin is qint8, this must be set to -127 if narrow range quantized or -128 if not.
    lhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in rhs.
      For example, if Tin is qint8, this must be set to 127.
    rhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in rhs.
      For example, if Trhs is qint8, this must be set to -127 if narrow range quantized or -128 if not.
    rhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in rhs.
      For example, if Trhs is qint8, this must be set to 127.
    output_quantization_min_val: An `int`.
      The min value of the quantized data stored in output.
      For example, if Tout is qint8, this must be set to -127 if narrow range quantized or -128 if not.
    output_quantization_max_val: An `int`.
      The max value of the quantized data stored in output.
      For example, if Tout is qint8, this must be set to 127.
    lhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For dot op lhs, only per-tensor quantization is supported.
      Thus, this attribute must be set to -1. Other values are rejected.
    rhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For dot op rhs, only per-tensor quantization or per-channel quantization along dimension 1 is supported.
      Thus, this attribute must be set to -1 or 1. Other values are rejected.
    output_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For dot op output, only per-tensor quantization or per-channel quantization along dimension 1 is supported.
      Thus, this attribute must be set to -1 or 1. Other values are rejected.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

UniformQuantizedDot: Incomplete

def uniform_quantized_dot_eager_fallback(lhs, rhs, lhs_scales, lhs_zero_points, rhs_scales, rhs_zero_points, output_scales, output_zero_points, Tout, lhs_quantization_min_val, lhs_quantization_max_val, rhs_quantization_min_val, rhs_quantization_max_val, output_quantization_min_val, output_quantization_max_val, lhs_quantization_axis, rhs_quantization_axis, output_quantization_axis, name, ctx): ...
def uniform_quantized_dot_hybrid(lhs, rhs, rhs_scales, rhs_zero_points, Tout, rhs_quantization_min_val, rhs_quantization_max_val, rhs_quantization_axis: int = -1, name: Incomplete | None = None):
    """Perform hybrid quantized dot of float Tensor `lhs` and quantized Tensor `rhs`.

  Given float `lhs` and quantized `rhs`, internally performs quantization on `lhs`, and then performs quantized dot on quantized lhs and `rhs`.
  The internal quantization on `lhs` is a quantization to qint8, dynamic range, per-batch (per-axis along axis 0), asymmetric, and not narrow range (the range is [-128, 127]).
  `lhs` and `rhs` must be 2D Tensors and the lhs.dim_size(1) must match rhs.dim_size(0).
  `rhs` must be quantized Tensor, where its data value is quantized using the formula:
  quantized_data = clip(original_data / scale + zero_point, quantization_min_val, quantization_max_val).

  Args:
    lhs: A `Tensor`. Must be one of the following types: `float32`.
      Must be a 2D Tensor of Tlhs.
    rhs: A `Tensor`. Must be one of the following types: `qint8`.
      Must be a 2D Tensor of Trhs.
    rhs_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale when quantizing original data that rhs represents.
      Must be a scalar Tensor (per-tensor quantization) or 1D Tensor of size (rhs.dim_size(1),) (per-channel quantization).
    rhs_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point when quantizing original data that rhs represents.
      Same shape condition as rhs_scales.
    Tout: A `tf.DType` from: `tf.float32`. The type of output Tensor.
    rhs_quantization_min_val: An `int`.
      The min value of the quantized data stored in rhs.
      For example, if Trhs is qint8, this must be set to -127 if narrow range quantized or -128 if not.
    rhs_quantization_max_val: An `int`.
      The max value of the quantized data stored in rhs.
      For example, if Trhs is qint8, this must be set to 127.
    rhs_quantization_axis: An optional `int`. Defaults to `-1`.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization.
      For dot op rhs, only per-tensor quantization or per-channel quantization along dimension 1 is supported.
      Thus, this attribute must be set to -1 or 1. Other values are rejected.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

UniformQuantizedDotHybrid: Incomplete

def uniform_quantized_dot_hybrid_eager_fallback(lhs, rhs, rhs_scales, rhs_zero_points, Tout, rhs_quantization_min_val, rhs_quantization_max_val, rhs_quantization_axis, name, ctx): ...
def uniform_requantize(input, input_scales, input_zero_points, output_scales, output_zero_points, Tout, input_quantization_min_val, input_quantization_max_val, output_quantization_min_val, output_quantization_max_val, input_quantization_axis: int = -1, output_quantization_axis: int = -1, name: Incomplete | None = None):
    """Given quantized tensor `input`, requantize it with new quantization parameters.

  Given quantized tensor `input`, which was quantized using {input_scales, input_zero_points, input_quantization_axis, input_quantization_min_val, input_quantization_max_val},
  requantize it to a tensor, which is quantized using {output_scales, output_zero_points, output_quantization_axis, output_quantization_min_val, output_quantization_max_val}.
  The requantization is done by using the formula:
  output_quantized_data = clip(
    (input_quantized_data - input_zero_point) * (input_scale / output_scale) + output_zero_point,
    output_quantization_min_val,
    output_quantization_max_val)

  Per-tensor and per-axis quantization supported cases are followings:
  * per-tensor -> per-tensor
  * per-tensor -> per-axis
  * per-axis -> per-axis where input_quantization_axis equals output_quantization_axis.
  i.e. At least one among input_quantization_axis and output_quantization_axis must be -1, or two must be equal.

  Args:
    input: A `Tensor`. Must be one of the following types: `qint8`, `qint32`.
      Must be a Tensor of Tin.
    input_scales: A `Tensor` of type `float32`.
      The float value(s) used as scale(s) when quantizing original data that `input` represents.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (input.dim_size(quantization_axis),) (per-axis quantization).
    input_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) used as zero_point(s) when quantizing original data that `input` represents.
      Same shape condition as scales.
    output_scales: A `Tensor` of type `float32`.
      The float value(s) to use as new scale(s) to quantize original data that `input` represents.
      Must be a scalar Tensor if quantization_axis is -1 (per-tensor quantization), otherwise 1D Tensor of size (input.dim_size(quantization_axis),) (per-axis quantization).
    output_zero_points: A `Tensor` of type `int32`.
      The int32 value(s) to use as new zero_point(s) to quantize original data that `input` represents.
      Same shape condition as scales.
    Tout: A `tf.DType` from: `tf.qint8, tf.qint32`.
      The type of output Tensor. A tf.DType from: tf.qint8, tf.qint32
    input_quantization_min_val: An `int`.
      The quantization min value that was used when quantizing original data that `input` represents.
      The purpose of this attribute is typically (but not limited to) to indicate narrow range, where this is set to:
      `(Tin lowest) + 1` if narrow range, and `(Tin lowest)` otherwise.
      For example, if Tin is qint8, this is set to -127 if narrow range quantized or -128 if not.
    input_quantization_max_val: An `int`.
      The quantization max value that was used when quantizing original data that `input` represents.
      The purpose of this attribute is typically (but not limited to) indicate narrow range, where this is set to:
      `(Tout max)` for both narrow range and not narrow range.
      For example, if Tin is qint8, this is set to 127.
    output_quantization_min_val: An `int`.
      The new quantization min value to quantize original data that `input` represents.
    output_quantization_max_val: An `int`.
      The new quantization max value to quantize original data that `input` represents.
    input_quantization_axis: An optional `int`. Defaults to `-1`.
      The quantization axis that was used when quantizing original data that `input` represents.
      Indicates the dimension index of the tensor where per-axis quantization is applied for the slices along that dimension.
      If set to -1 (default), this indicates per-tensor quantization. Otherwise, it must be set within range [0, input.dims()).
    output_quantization_axis: An optional `int`. Defaults to `-1`.
      The new quantization axis to use to quantize original data that `input` represents.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `Tout`.
  """

UniformRequantize: Incomplete

def uniform_requantize_eager_fallback(input, input_scales, input_zero_points, output_scales, output_zero_points, Tout, input_quantization_min_val, input_quantization_max_val, output_quantization_min_val, output_quantization_max_val, input_quantization_axis, output_quantization_axis, name, ctx): ...
