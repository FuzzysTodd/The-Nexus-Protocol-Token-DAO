from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.histogram import metadata as metadata
from tensorboard.util import lazy_tensor_creator as lazy_tensor_creator, tensor_util as tensor_util

DEFAULT_BUCKET_COUNT: int

def histogram_pb(tag, data, buckets: Incomplete | None = None, description: Incomplete | None = None):
    """Create a histogram summary protobuf.

    Arguments:
      tag: String tag for the summary.
      data: A `np.array` or array-like form of any shape. Must have type
        castable to `float`.
      buckets: Optional positive `int`. The output shape will always be
        [buckets, 3]. If there is no data, then an all-zero array of shape
        [buckets, 3] will be returned. If there is data but all points have
        the same value, then all buckets' left and right endpoints are the
        same and only the last bucket has nonzero count. Defaults to 30 if
        not specified.
      description: Optional long-form description for this summary, as a
        `str`. Markdown is supported. Defaults to empty.

    Returns:
      A `summary_pb2.Summary` protobuf object.
    """
def histogram(name, data, step: Incomplete | None = None, buckets: Incomplete | None = None, description: Incomplete | None = None):
    '''Write a histogram summary.

    See also `tf.summary.scalar`, `tf.summary.SummaryWriter`.

    Writes a histogram to the current default summary writer, for later analysis
    in TensorBoard\'s \'Histograms\' and \'Distributions\' dashboards (data written
    using this API will appear in both places). Like `tf.summary.scalar` points,
    each histogram is associated with a `step` and a `name`. All the histograms
    with the same `name` constitute a time series of histograms.

    The histogram is calculated over all the elements of the given `Tensor`
    without regard to its shape or rank.

    This example writes 2 histograms:

    ```python
    w = tf.summary.create_file_writer(\'test/logs\')
    with w.as_default():
        tf.summary.histogram("activations", tf.random.uniform([100, 50]), step=0)
        tf.summary.histogram("initial_weights", tf.random.normal([1000]), step=0)
    ```

    A common use case is to examine the changing activation patterns (or lack
    thereof) at specific layers in a neural network, over time.

    ```python
    w = tf.summary.create_file_writer(\'test/logs\')
    with w.as_default():
    for step in range(100):
        # Generate fake "activations".
        activations = [
            tf.random.normal([1000], mean=step, stddev=1),
            tf.random.normal([1000], mean=step, stddev=10),
            tf.random.normal([1000], mean=step, stddev=100),
        ]

        tf.summary.histogram("layer1/activate", activations[0], step=step)
        tf.summary.histogram("layer2/activate", activations[1], step=step)
        tf.summary.histogram("layer3/activate", activations[2], step=step)
    ```

    Arguments:
      name: A name for this summary. The summary tag used for TensorBoard will
        be this name prefixed by any active name scopes.
      data: A `Tensor` of any shape. The histogram is computed over its elements,
        which must be castable to `float64`.
      step: Explicit `int64`-castable monotonic step value for this summary. If
        omitted, this defaults to `tf.summary.experimental.get_step()`, which must
        not be None.
      buckets: Optional positive `int`. The output will have this
        many buckets, except in two edge cases. If there is no data, then
        there are no buckets. If there is data but all points have the
        same value, then all buckets\' left and right endpoints are the same
        and only the last bucket has nonzero count. Defaults to 30 if not
        specified.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.

    Returns:
      True on success, or false if no summary was emitted because no default
      summary writer was available.

    Raises:
      ValueError: if a default writer exists, but no step was provided and
        `tf.summary.experimental.get_step()` is None.
    '''
