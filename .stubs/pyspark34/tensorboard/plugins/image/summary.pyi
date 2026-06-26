from _typeshed import Incomplete
from tensorboard.plugins.image import metadata as metadata, summary_v2 as summary_v2
from tensorboard.util import encoder as encoder

image = summary_v2.image

def op(name, images, max_outputs: int = 3, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None):
    """Create a legacy image summary op for use in a TensorFlow graph.

    Arguments:
      name: A unique name for the generated summary node.
      images: A `Tensor` representing pixel data with shape `[k, h, w, c]`,
        where `k` is the number of images, `h` and `w` are the height and
        width of the images, and `c` is the number of channels, which
        should be 1, 3, or 4. Any of the dimensions may be statically
        unknown (i.e., `None`).
      max_outputs: Optional `int` or rank-0 integer `Tensor`. At most this
        many images will be emitted at each step. When more than
        `max_outputs` many images are provided, the first `max_outputs` many
        images will be used and the rest silently discarded.
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
def pb(name, images, max_outputs: int = 3, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Create a legacy image summary protobuf.

    This behaves as if you were to create an `op` with the same arguments
    (wrapped with constant tensors where appropriate) and then execute
    that summary op in a TensorFlow session.

    Arguments:
      name: A unique name for the generated summary, including any desired
        name scopes.
      images: An `np.array` representing pixel data with shape
        `[k, h, w, c]`, where `k` is the number of images, `w` and `h` are
        the width and height of the images, and `c` is the number of
        channels, which should be 1, 3, or 4.
      max_outputs: Optional `int`. At most this many images will be
        emitted. If more than this many images are provided, the first
        `max_outputs` many images will be used and the rest silently
        discarded.
      display_name: Optional name for this summary in TensorBoard, as a
        `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
        `str`. Markdown is supported. Defaults to empty.

    Returns:
      A `tf.Summary` protobuf object.
    """
