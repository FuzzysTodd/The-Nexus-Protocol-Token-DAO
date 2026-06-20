from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export

def close_summary_writer(writer, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    writer: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

CloseSummaryWriter: Incomplete

def close_summary_writer_eager_fallback(writer, name, ctx): ...
def create_summary_db_writer(writer, db_uri, experiment_name, run_name, user_name, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    writer: A `Tensor` of type `resource`.
    db_uri: A `Tensor` of type `string`.
    experiment_name: A `Tensor` of type `string`.
    run_name: A `Tensor` of type `string`.
    user_name: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

CreateSummaryDbWriter: Incomplete

def create_summary_db_writer_eager_fallback(writer, db_uri, experiment_name, run_name, user_name, name, ctx): ...
def create_summary_file_writer(writer, logdir, max_queue, flush_millis, filename_suffix, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    writer: A `Tensor` of type `resource`.
    logdir: A `Tensor` of type `string`.
    max_queue: A `Tensor` of type `int32`.
    flush_millis: A `Tensor` of type `int32`.
    filename_suffix: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

CreateSummaryFileWriter: Incomplete

def create_summary_file_writer_eager_fallback(writer, logdir, max_queue, flush_millis, filename_suffix, name, ctx): ...
def flush_summary_writer(writer, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    writer: A `Tensor` of type `resource`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

FlushSummaryWriter: Incomplete

def flush_summary_writer_eager_fallback(writer, name, ctx): ...
def import_event(writer, event, name: Incomplete | None = None):
    """TODO: add doc.

  Args:
    writer: A `Tensor` of type `resource`.
    event: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

ImportEvent: Incomplete

def import_event_eager_fallback(writer, event, name, ctx): ...
def summary_writer(shared_name: str = '', container: str = '', name: Incomplete | None = None):
    '''TODO: add doc.

  Args:
    shared_name: An optional `string`. Defaults to `""`.
    container: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

SummaryWriter: Incomplete

def summary_writer_eager_fallback(shared_name, container, name, ctx): ...
def write_audio_summary(writer, step, tag, tensor, sample_rate, max_outputs: int = 3, name: Incomplete | None = None):
    """Writes an audio summary.

  Writes encoded audio summary `tensor` at `step` with `tag` using summary `writer`.
  `sample_rate` is the audio sample rate is Hz.

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tag: A `Tensor` of type `string`.
    tensor: A `Tensor` of type `float32`.
    sample_rate: A `Tensor` of type `float32`.
    max_outputs: An optional `int` that is `>= 1`. Defaults to `3`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteAudioSummary: Incomplete

def write_audio_summary_eager_fallback(writer, step, tag, tensor, sample_rate, max_outputs, name, ctx): ...
def write_graph_summary(writer, step, tensor, name: Incomplete | None = None):
    """Writes a graph summary.

  Writes TensorFlow graph `tensor` at `step` using summary `writer`.

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tensor: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteGraphSummary: Incomplete

def write_graph_summary_eager_fallback(writer, step, tensor, name, ctx): ...
def write_histogram_summary(writer, step, tag, values, name: Incomplete | None = None):
    """Writes a histogram summary.

  Writes histogram `values` at `step` with `tag` using summary `writer`.

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tag: A `Tensor` of type `string`.
    values: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`, `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteHistogramSummary: Incomplete

def write_histogram_summary_eager_fallback(writer, step, tag, values, name, ctx): ...
def write_image_summary(writer, step, tag, tensor, bad_color, max_images: int = 3, name: Incomplete | None = None):
    """Writes an image summary.

  Writes image `tensor` at `step` with `tag` using summary `writer`.
  `tensor` is image with shape [height, width, channels].

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tag: A `Tensor` of type `string`.
    tensor: A `Tensor`. Must be one of the following types: `uint8`, `float64`, `float32`, `half`.
    bad_color: A `Tensor` of type `uint8`.
    max_images: An optional `int` that is `>= 1`. Defaults to `3`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteImageSummary: Incomplete

def write_image_summary_eager_fallback(writer, step, tag, tensor, bad_color, max_images, name, ctx): ...
def write_raw_proto_summary(writer, step, tensor, name: Incomplete | None = None):
    """Writes a serialized proto summary.

  Writes `tensor`, a serialized proto at `step` using summary `writer`.

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tensor: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteRawProtoSummary: Incomplete

def write_raw_proto_summary_eager_fallback(writer, step, tensor, name, ctx): ...
def write_scalar_summary(writer, step, tag, value, name: Incomplete | None = None):
    """Writes a scalar summary.

  Writes scalar `value` at `step` with `tag` using summary `writer`.

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tag: A `Tensor` of type `string`.
    value: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int32`, `uint8`, `int16`, `int8`, `int64`, `bfloat16`, `uint16`, `half`, `uint32`, `uint64`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteScalarSummary: Incomplete

def write_scalar_summary_eager_fallback(writer, step, tag, value, name, ctx): ...
def write_summary(writer, step, tensor, tag, summary_metadata, name: Incomplete | None = None):
    """Writes a tensor summary.

  Writes `tensor` at `step` with `tag` using summary `writer`.

  Args:
    writer: A `Tensor` of type `resource`.
    step: A `Tensor` of type `int64`.
    tensor: A `Tensor`.
    tag: A `Tensor` of type `string`.
    summary_metadata: A `Tensor` of type `string`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

WriteSummary: Incomplete

def write_summary_eager_fallback(writer, step, tensor, tag, summary_metadata, name, ctx): ...
