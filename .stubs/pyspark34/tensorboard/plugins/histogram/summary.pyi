from _typeshed import Incomplete
from tensorboard.plugins.histogram import metadata as metadata, summary_v2 as summary_v2

histogram = summary_v2.histogram
histogram_pb = summary_v2.histogram_pb

def op(name, data, bucket_count: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None):
    """Create a legacy histogram summary op.

    Arguments:
      name: A unique name for the generated summary node.
      data: A `Tensor` of any shape. Must be castable to `float64`.
      bucket_count: Optional positive `int`. The output will have this
        many buckets, except in two edge cases. If there is no data, then
        there are no buckets. If there is data but all points have the
        same value, then there is one bucket whose left and right
        endpoints are the same.
      display_name: Optional name for this summary in TensorBoard, as a
        constant `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.
      collections: Optional list of graph collections keys. The new
        summary op is added to these collections. Defaults to
        `[Graph Keys.SUMMARIES]`.

    Returns:
      A TensorFlow summary op.
    """
def pb(name, data, bucket_count: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Create a legacy histogram summary protobuf.

    Arguments:
      name: A unique name for the generated summary, including any desired
        name scopes.
      data: A `np.array` or array-like form of any shape. Must have type
        castable to `float`.
      bucket_count: Optional positive `int`. The output will have this
        many buckets, except in two edge cases. If there is no data, then
        there are no buckets. If there is data but all points have the
        same value, then there is one bucket whose left and right
        endpoints are the same.
      display_name: Optional name for this summary in TensorBoard, as a
        `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
        `str`. Markdown is supported. Defaults to empty.

    Returns:
      A `tf.Summary` protobuf object.
    """
