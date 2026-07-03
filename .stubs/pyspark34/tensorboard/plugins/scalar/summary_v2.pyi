from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.scalar import metadata as metadata
from tensorboard.util import tensor_util as tensor_util

def scalar(name, data, step: Incomplete | None = None, description: Incomplete | None = None):
    """Write a scalar summary.

    See also `tf.summary.image`, `tf.summary.histogram`, `tf.summary.SummaryWriter`.

    Writes simple numeric values for later analysis in TensorBoard.  Writes go to
    the current default summary writer. Each summary point is associated with an
    integral `step` value. This enables the incremental logging of time series
    data.  A common usage of this API is to log loss during training to produce
    a loss curve.

    For example:

    ```python
    test_summary_writer = tf.summary.create_file_writer('test/logdir')
    with test_summary_writer.as_default():
        tf.summary.scalar('loss', 0.345, step=1)
        tf.summary.scalar('loss', 0.234, step=2)
        tf.summary.scalar('loss', 0.123, step=3)
    ```

    Multiple independent time series may be logged by giving each series a unique
    `name` value.

    See [Get started with TensorBoard](https://www.tensorflow.org/tensorboard/get_started)
    for more examples of effective usage of `tf.summary.scalar`.

    In general, this API expects that data points are logged iwth a monotonically
    increasing step value. Duplicate points for a single step or points logged out
    of order by step are not guaranteed to display as desired in TensorBoard.

    Arguments:
      name: A name for this summary. The summary tag used for TensorBoard will
        be this name prefixed by any active name scopes.
      data: A real numeric scalar value, convertible to a `float32` Tensor.
      step: Explicit `int64`-castable monotonic step value for this summary. If
        omitted, this defaults to `tf.summary.experimental.get_step()`, which must
        not be None.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.

    Returns:
      True on success, or false if no summary was written because no default
      summary writer was available.

    Raises:
      ValueError: if a default writer exists, but no step was provided and
        `tf.summary.experimental.get_step()` is None.
    """
def scalar_pb(tag, data, description: Incomplete | None = None):
    """Create a scalar summary_pb2.Summary protobuf.

    Arguments:
      tag: String tag for the summary.
      data: A 0-dimensional `np.array` or a compatible python number type.
      description: Optional long-form description for this summary, as a
        `str`. Markdown is supported. Defaults to empty.

    Raises:
      ValueError: If the type or shape of the data is unsupported.

    Returns:
      A `summary_pb2.Summary` protobuf object.
    """
