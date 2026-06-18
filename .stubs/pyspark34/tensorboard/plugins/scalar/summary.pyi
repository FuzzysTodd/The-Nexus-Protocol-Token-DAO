from _typeshed import Incomplete
from tensorboard.plugins.scalar import metadata as metadata, summary_v2 as summary_v2

scalar = summary_v2.scalar
scalar_pb = summary_v2.scalar_pb

def op(name, data, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None):
    """Create a legacy scalar summary op.

    Arguments:
      name: A unique name for the generated summary node.
      data: A real numeric rank-0 `Tensor`. Must have `dtype` castable
        to `float32`.
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
def pb(name, data, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Create a legacy scalar summary protobuf.

    Arguments:
      name: A unique name for the generated summary, including any desired
        name scopes.
      data: A rank-0 `np.array` or array-like form (so raw `int`s and
        `float`s are fine, too).
      display_name: Optional name for this summary in TensorBoard, as a
        `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
        `str`. Markdown is supported. Defaults to empty.

    Returns:
      A `tf.Summary` protobuf object.
    """
