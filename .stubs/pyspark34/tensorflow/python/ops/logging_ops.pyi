from tensorflow.python.ops.gen_logging_ops import *
from _typeshed import Incomplete
from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.framework import dtypes as dtypes, ops as ops, sparse_tensor as sparse_tensor, tensor_util as tensor_util
from tensorflow.python.ops import gen_logging_ops as gen_logging_ops, string_ops as string_ops
from tensorflow.python.platform import tf_logging as tf_logging
from tensorflow.python.util import dispatch as dispatch, nest as nest
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export

def enable_interactive_logging() -> None: ...
def Print(input_, data, message: Incomplete | None = None, first_n: Incomplete | None = None, summarize: Incomplete | None = None, name: Incomplete | None = None):
    """Prints a list of tensors.

  This is an identity op (behaves like `tf.identity`) with the side effect
  of printing `data` when evaluating.

  Note: This op prints to the standard error. It is not currently compatible
    with jupyter notebook (printing to the notebook *server's* output, not into
    the notebook).

  @compatibility(TF2)
  This API is deprecated. Use `tf.print` instead. `tf.print` does not need the
  `input_` argument.

  `tf.print` works in TF2 when executing eagerly and inside a `tf.function`.

  In TF1-styled sessions, an explicit control dependency declaration is needed
  to execute the `tf.print` operation. Refer to the documentation of
  `tf.print` for more details.
  @end_compatibility

  Args:
    input_: A tensor passed through this op.
    data: A list of tensors to print out when op is evaluated.
    message: A string, prefix of the error message.
    first_n: Only log `first_n` number of times. Negative numbers log always;
      this is the default.
    summarize: Only print this many entries of each tensor. If None, then a
      maximum of 3 elements are printed per input tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type and contents as `input_`.

    ```python
    sess = tf.compat.v1.Session()
    with sess.as_default():
        tensor = tf.range(10)
        print_op = tf.print(tensor)
        with tf.control_dependencies([print_op]):
          out = tf.add(tensor, tensor)
        sess.run(out)
    ```
  """
def print_v2(*inputs, **kwargs):
    '''Print the specified inputs.

  A TensorFlow operator that prints the specified inputs to a desired
  output stream or logging level. The inputs may be dense or sparse Tensors,
  primitive python objects, data structures that contain tensors, and printable
  Python objects. Printed tensors will recursively show the first and last
  elements of each dimension to summarize.

  Example:
    Single-input usage:

    ```python
    tensor = tf.range(10)
    tf.print(tensor, output_stream=sys.stderr)
    ```

    (This prints "[0 1 2 ... 7 8 9]" to sys.stderr)

    Multi-input usage:

    ```python
    tensor = tf.range(10)
    tf.print("tensors:", tensor, {2: tensor * 2}, output_stream=sys.stdout)
    ```

    (This prints "tensors: [0 1 2 ... 7 8 9] {2: [0 2 4 ... 14 16 18]}" to
    sys.stdout)

    Changing the input separator:
    ```python
    tensor_a = tf.range(2)
    tensor_b = tensor_a * 2
    tf.print(tensor_a, tensor_b, output_stream=sys.stderr, sep=\',\')
    ```

    (This prints "[0 1],[0 2]" to sys.stderr)

    Usage in a `tf.function`:

    ```python
    @tf.function
    def f():
        tensor = tf.range(10)
        tf.print(tensor, output_stream=sys.stderr)
        return tensor

    range_tensor = f()
    ```

    (This prints "[0 1 2 ... 7 8 9]" to sys.stderr)

  *Compatibility usage in TF 1.x graphs*:

    In graphs manually created outside of `tf.function`, this method returns
    the created TF operator that prints the data. To make sure the
    operator runs, users need to pass the produced op to
    `tf.compat.v1.Session`\'s run method, or to use the op as a control
    dependency for executed ops by specifying
    `with tf.compat.v1.control_dependencies([print_op])`.

    ```python
    tf.compat.v1.disable_v2_behavior()  # for TF1 compatibility only

    sess = tf.compat.v1.Session()
    with sess.as_default():
      tensor = tf.range(10)
      print_op = tf.print("tensors:", tensor, {2: tensor * 2},
                          output_stream=sys.stdout)
      with tf.control_dependencies([print_op]):
        tripled_tensor = tensor * 3

      sess.run(tripled_tensor)
    ```

    (This prints "tensors: [0 1 2 ... 7 8 9] {2: [0 2 4 ... 14 16 18]}" to
    sys.stdout)

  Note: In Jupyter notebooks and colabs, `tf.print` prints to the notebook
    cell outputs. It will not write to the notebook kernel\'s console logs.

  Args:
    *inputs: Positional arguments that are the inputs to print. Inputs in the
      printed output will be separated by spaces. Inputs may be python
      primitives, tensors, data structures such as dicts and lists that may
      contain tensors (with the data structures possibly nested in arbitrary
      ways), and printable python objects.
    output_stream: The output stream, logging level, or file to print to.
      Defaults to sys.stderr, but sys.stdout, tf.compat.v1.logging.info,
      tf.compat.v1.logging.warning, tf.compat.v1.logging.error,
      absl.logging.info, absl.logging.warning and absl.logging.error are also
      supported. To print to a file, pass a string started with "file://"
      followed by the file path, e.g., "file:///tmp/foo.out".
    summarize: The first and last `summarize` elements within each dimension are
      recursively printed per Tensor. If None, then the first 3 and last 3
      elements of each dimension are printed for each tensor. If set to -1, it
      will print all elements of every tensor.
    sep: The string to use to separate the inputs. Defaults to " ".
    end: End character that is appended at the end the printed string. Defaults
      to the newline character.
    name: A name for the operation (optional).

  Returns:
    None when executing eagerly. During graph tracing this returns
    a TF operator that prints the specified inputs in the specified output
    stream or logging level. This operator will be automatically executed
    except inside of `tf.compat.v1` graphs and sessions.

  Raises:
    ValueError: If an unsupported output stream is specified.
  '''
def histogram_summary(tag, values, collections: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with a histogram.

  This ops is deprecated. Please switch to tf.summary.histogram.

  For an explanation of why this op was deprecated, and information on how to
  migrate, look
  ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

  The generated
  [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
  has one summary value containing a histogram for `values`.

  This op reports an `InvalidArgument` error if any value is not finite.

  Args:
    tag: A `string` `Tensor`. 0-D.  Tag to use for the summary value.
    values: A real numeric `Tensor`. Any shape. Values to use to build the
      histogram.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.
  """
def image_summary(tag, tensor, max_images: int = 3, collections: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with images.

  For an explanation of why this op was deprecated, and information on how to
  migrate, look
  ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

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

  Args:
    tag: A scalar `Tensor` of type `string`. Used to build the `tag` of the
      summary values.
    tensor: A 4-D `uint8` or `float32` `Tensor` of shape `[batch_size, height,
      width, channels]` where `channels` is 1, 3, or 4.
    max_images: Max number of batch elements to generate images for.
    collections: Optional list of ops.GraphKeys.  The collections to add the
      summary to.  Defaults to [ops.GraphKeys.SUMMARIES]
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.
  """
def audio_summary(tag, tensor, sample_rate, max_outputs: int = 3, collections: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with audio.

  This op is deprecated. Please switch to tf.summary.audio.
  For an explanation of why this op was deprecated, and information on how to
  migrate, look
  ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

  The summary has up to `max_outputs` summary values containing audio. The
  audio is built from `tensor` which must be 3-D with shape `[batch_size,
  frames, channels]` or 2-D with shape `[batch_size, frames]`. The values are
  assumed to be in the range of `[-1.0, 1.0]` with a sample rate of
  `sample_rate`.

  The `tag` argument is a scalar `Tensor` of type `string`.  It is used to
  build the `tag` of the summary values:

  *  If `max_outputs` is 1, the summary value tag is '*tag*/audio'.
  *  If `max_outputs` is greater than 1, the summary value tags are
     generated sequentially as '*tag*/audio/0', '*tag*/audio/1', etc.

  Args:
    tag: A scalar `Tensor` of type `string`. Used to build the `tag` of the
      summary values.
    tensor: A 3-D `float32` `Tensor` of shape `[batch_size, frames, channels]`
      or a 2-D `float32` `Tensor` of shape `[batch_size, frames]`.
    sample_rate: A Scalar `float32` `Tensor` indicating the sample rate of the
      signal in hertz.
    max_outputs: Max number of batch elements to generate audio for.
    collections: Optional list of ops.GraphKeys.  The collections to add the
      summary to.  Defaults to [ops.GraphKeys.SUMMARIES]
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.
  """
def merge_summary(inputs, collections: Incomplete | None = None, name: Incomplete | None = None):
    """Merges summaries.

  This op is deprecated. Please switch to tf.compat.v1.summary.merge, which has
  identical
  behavior.

  This op creates a
  [`Summary`](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
  protocol buffer that contains the union of all the values in the input
  summaries.

  When the Op is run, it reports an `InvalidArgument` error if multiple values
  in the summaries to merge use the same tag.

  Args:
    inputs: A list of `string` `Tensor` objects containing serialized `Summary`
      protocol buffers.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer resulting from the merging.
  """
def merge_all_summaries(key=...):
    """Merges all summaries collected in the default graph.

  This op is deprecated. Please switch to tf.compat.v1.summary.merge_all, which
  has
  identical behavior.

  Args:
    key: `GraphKey` used to collect the summaries.  Defaults to
      `GraphKeys.SUMMARIES`.

  Returns:
    If no summaries were collected, returns None.  Otherwise returns a scalar
    `Tensor` of type `string` containing the serialized `Summary` protocol
    buffer resulting from the merging.
  """
def get_summary_op():
    """Returns a single Summary op that would run all summaries.

  Either existing one from `SUMMARY_OP` collection or merges all existing
  summaries.

  Returns:
    If no summaries were collected, returns None. Otherwise returns a scalar
    `Tensor` of type `string` containing the serialized `Summary` protocol
    buffer resulting from the merging.
  """
def scalar_summary(tags, values, collections: Incomplete | None = None, name: Incomplete | None = None):
    """Outputs a `Summary` protocol buffer with scalar values.

  This ops is deprecated. Please switch to tf.summary.scalar.
  For an explanation of why this op was deprecated, and information on how to
  migrate, look
  ['here'](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/deprecated/__init__.py)

  The input `tags` and `values` must have the same shape.  The generated
  summary has a summary value for each tag-value pair in `tags` and `values`.

  Args:
    tags: A `string` `Tensor`.  Tags for the summaries.
    values: A real numeric Tensor.  Values for the summaries.
    collections: Optional list of graph collections keys. The new summary op is
      added to these collections. Defaults to `[GraphKeys.SUMMARIES]`.
    name: A name for the operation (optional).

  Returns:
    A scalar `Tensor` of type `string`. The serialized `Summary` protocol
    buffer.
  """
