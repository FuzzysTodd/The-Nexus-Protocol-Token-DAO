from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

Assert: Incomplete

def audio_summary(tag, tensor, sample_rate, max_outputs: int = 3, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with audio.

  The summary has up to `max_outputs` summary values containing audio. The
  audio is built from `tensor` which must be 3-D with shape `[batch_size,
  frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
  assumed to be in the range of `[-1.0, 1.0]` with a sample rate of `sample_rate`.

  The `tag` argument is a scalar `Tensor` of type `string`.  It is used to
  build the `tag` of the summary values:

  *  If `max_outputs` is 1, the summary value tag is '*tag*/audio'.
  *  If `max_outputs` is greater than 1, the summary value tags are
     generated sequentially as '*tag*/audio/0', '*tag*/audio/1', etc.

  Args:
    tag: A `Tensor` of type `string`.
      Scalar. Used to build the `tag` attribute of the summary values.
    tensor: A `Tensor` of type `float32`. 2-D of shape `[batch_size, frames]`.
    sample_rate: A `float`. The sample rate of the signal in hertz.
    max_outputs: An optional `int` that is `>= 1`. Defaults to `3`.
      Max number of batch elements to generate audio for.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

AudioSummary: Incomplete

def audio_summary_eager_fallback(tag, tensor, sample_rate, max_outputs, name, ctx): ...
def audio_summary_v2(tag, tensor, sample_rate, max_outputs: int = 3, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with audio.

  The summary has up to `max_outputs` summary values containing audio. The
  audio is built from `tensor` which must be 3-D with shape `[batch_size,
  frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
  assumed to be in the range of `[-1.0, 1.0]` with a sample rate of `sample_rate`.

  The `tag` argument is a scalar `Tensor` of type `string`.  It is used to
  build the `tag` of the summary values:

  *  If `max_outputs` is 1, the summary value tag is '*tag*/audio'.
  *  If `max_outputs` is greater than 1, the summary value tags are
     generated sequentially as '*tag*/audio/0', '*tag*/audio/1', etc.

  Args:
    tag: A `Tensor` of type `string`.
      Scalar. Used to build the `tag` attribute of the summary values.
    tensor: A `Tensor` of type `float32`. 2-D of shape `[batch_size, frames]`.
    sample_rate: A `Tensor` of type `float32`.
      The sample rate of the signal in hertz.
    max_outputs: An optional `int` that is `>= 1`. Defaults to `3`.
      Max number of batch elements to generate audio for.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

AudioSummaryV2: Incomplete

def audio_summary_v2_eager_fallback(tag, tensor, sample_rate, max_outputs, name, ctx): ...
def histogram_summary(tag, values, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with a histogram.

  The generated
  [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
  has one summary value containing a histogram for `values`.

  This op reports an `InvalidArgument` error if any value is not finite.

  Args:
    tag: A `Tensor` of type `string`.
      Scalar.  Tag to use for the `Summary.Value`.
    values: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
      Any shape. Values to use to build the histogram.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

HistogramSummary: Incomplete

def histogram_summary_eager_fallback(tag, values, name, ctx): ...
def image_summary(tag, tensor, max_images: int = 3, bad_color=..., name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with images.

  The summary has up to `max_images` summary values containing images. The
  images are built from `tensor` which must be 4-D with shape `[batch_size,
  height, width, channels]` and where `channels` can be:

  *  1: `tensor` is interpreted as Grayscale.
  *  3: `tensor` is interpreted as RGB.
  *  4: `tensor` is interpreted as RGBA.

  The images have the same number of channels as the input tensor. For float
  input, the values are normalized one image at a time to fit in the range
  `[0, 255]`.  `uint8` values are unchanged.  The op uses two different
  normalization algorithms:

  *  If the input values are all positive, they are rescaled so the largest one
     is 255.

  *  If any input value is negative, the values are shifted so input value 0.0
     is at 127.  They are then rescaled so that either the smallest value is 0,
     or the largest one is 255.

  The `tag` argument is a scalar `Tensor` of type `string`.  It is used to
  build the `tag` of the summary values:

  *  If `max_images` is 1, the summary value tag is '*tag*/image'.
  *  If `max_images` is greater than 1, the summary value tags are
     generated sequentially as '*tag*/image/0', '*tag*/image/1', etc.

  The `bad_color` argument is the color to use in the generated images for
  non-finite input values.  It is a `uint8` 1-D tensor of length `channels`.
  Each element must be in the range `[0, 255]` (It represents the value of a
  pixel in the output image).  Non-finite values in the input tensor are
  replaced by this tensor in the output image.  The default value is the color
  red.

  Args:
    tag: A `Tensor` of type `string`.
      Scalar. Used to build the `tag` attribute of the summary values.
    tensor: A `Tensor`. Must be one of the following types: `uint8`, `float32`, `half`, `float64`.
      4-D of shape `[batch_size, height, width, channels]` where
      `channels` is 1, 3, or 4.
    max_images: An optional `int` that is `>= 1`. Defaults to `3`.
      Max number of batch elements to generate images for.
    bad_color: An optional `tf.TensorProto`. Defaults to `dtype: DT_UINT8 tensor_shape { dim { size: 4 } } int_val: 255 int_val: 0 int_val: 0 int_val: 255`.
      Color to use for pixels with non-finite values.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ImageSummary: Incomplete

def image_summary_eager_fallback(tag, tensor, max_images, bad_color, name, ctx): ...
def merge_summary(inputs, name: Incomplete | None = None):
    """Merges summaries.

  This op creates a
  [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
  protocol buffer that contains the union of all the values in the input
  summaries.

  When the Op is run, it reports an `InvalidArgument` error if multiple values
  in the summaries to merge use the same tag.

  Args:
    inputs: A list of at least 1 `Tensor` objects with type `string`.
      Can be of any shape.  Each must contain serialized `Summary` protocol
      buffers.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

MergeSummary: Incomplete

def merge_summary_eager_fallback(inputs, name, ctx): ...

Print: Incomplete

def print_v2(input, output_stream: str = 'stderr', end: str = '\n', name: Incomplete | None = None):
    '''Prints a string scalar.

  Prints a string scalar to the desired output_stream.

  Args:
    input: A `Tensor` of type `string`. The string scalar to print.
    output_stream: An optional `string`. Defaults to `"stderr"`.
      A string specifying the output stream or logging level to print to.
    end: An optional `string`. Defaults to `"\\n"`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  '''

PrintV2: Incomplete

def print_v2_eager_fallback(input, output_stream, end, name, ctx): ...
def scalar_summary(tags, values, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with scalar values.

  The input `tags` and `values` must have the same shape.  The generated summary
  has a summary value for each tag-value pair in `tags` and `values`.

  Args:
    tags: A `Tensor` of type `string`. Tags for the summary.
    values: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
      Same shape as `tags.  Values for the summary.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

ScalarSummary: Incomplete

def scalar_summary_eager_fallback(tags, values, name, ctx): ...
def tensor_summary(tensor, description: str = '', labels=[], display_name: str = '', name: Incomplete | None = None):
    '''Outputs a `Summary` protocol buffer with a tensor.

  This op is being phased out in favor of TensorSummaryV2, which lets callers pass
  a tag as well as a serialized SummaryMetadata proto string that contains
  plugin-specific data. We will keep this op to maintain backwards compatibility.

  Args:
    tensor: A `Tensor`. A tensor to serialize.
    description: An optional `string`. Defaults to `""`.
      A json-encoded SummaryDescription proto.
    labels: An optional list of `strings`. Defaults to `[]`.
      An unused list of strings.
    display_name: An optional `string`. Defaults to `""`. An unused string.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  '''

TensorSummary: Incomplete

def tensor_summary_eager_fallback(tensor, description, labels, display_name, name, ctx): ...
def tensor_summary_v2(tag, tensor, serialized_summary_metadata, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with a tensor and per-plugin data.

  Args:
    tag: A `Tensor` of type `string`.
      A string attached to this summary. Used for organization in TensorBoard.
    tensor: A `Tensor`. A tensor to serialize.
    serialized_summary_metadata: A `Tensor` of type `string`.
      A serialized SummaryMetadata proto. Contains plugin
      data.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

TensorSummaryV2: Incomplete

def tensor_summary_v2_eager_fallback(tag, tensor, serialized_summary_metadata, name, ctx): ...
def timestamp(name: Incomplete | None = None):
    """Provides the time since epoch in seconds.

  Returns the timestamp as a `float64` for seconds since the Unix epoch.

  Common usages include:
  * Logging
  * Providing a random number seed
  * Debugging graph execution
  * Generating timing information, mainly through comparison of timestamps

  Note: In graph mode, the timestamp is computed when the op is executed,
  not when it is added to the graph.  In eager mode, the timestamp is computed
  when the op is eagerly executed.

  Args:
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float64`.
  """

Timestamp: Incomplete

def timestamp_eager_fallback(name, ctx): ...
