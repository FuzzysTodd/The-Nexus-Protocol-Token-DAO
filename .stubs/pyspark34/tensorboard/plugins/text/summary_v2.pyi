from _typeshed import Incomplete
from tensorboard.compat.proto import summary_pb2 as summary_pb2
from tensorboard.plugins.text import metadata as metadata
from tensorboard.util import tensor_util as tensor_util

def text(name, data, step: Incomplete | None = None, description: Incomplete | None = None):
    '''Write a text summary.

    See also `tf.summary.scalar`, `tf.summary.SummaryWriter`, `tf.summary.image`.

    Writes text Tensor values for later visualization and analysis in TensorBoard.
    Writes go to the current default summary writer.  Like `tf.summary.scalar`
    points, text points are each associated with a `step` and a `name`.
    All the points with the same `name` constitute a time series of text values.

    For Example:
    ```python
    test_summary_writer = tf.summary.create_file_writer(\'test/logdir\')
    with test_summary_writer.as_default():
        tf.summary.text(\'first_text\', \'hello world!\', step=0)
        tf.summary.text(\'first_text\', \'nice to meet you!\', step=1)
    ```

    The text summary can also contain Markdown, and TensorBoard will render the text
    as such.

    ```python
    with test_summary_writer.as_default():
        text_data = \'\'\'
              | *hello* | *there* |
              |---------|---------|
              | this    | is      |
              | a       | table   |
        \'\'\'
        text_data = \'\\n\'.join(l.strip() for l in text_data.splitlines())
        tf.summary.text(\'markdown_text\', text_data, step=0)
    ```

    Since text is Tensor valued, each text point may be a Tensor of string values.
    rank-1 and rank-2 Tensors are rendered as tables in TensorBoard.  For higher ranked
    Tensors, you\'ll see just a 2D slice of the data.  To avoid this, reshape the Tensor
    to at most rank-2 prior to passing it to this function.

    Demo notebook at
    ["Displaying text data in TensorBoard"](https://www.tensorflow.org/tensorboard/text_summaries).

    Arguments:
      name: A name for this summary. The summary tag used for TensorBoard will
        be this name prefixed by any active name scopes.
      data: A UTF-8 string Tensor value.
      step: Explicit `int64`-castable monotonic step value for this summary. If
        omitted, this defaults to `tf.summary.experimental.get_step()`, which must
        not be None.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.

    Returns:
      True on success, or false if no summary was emitted because no default
      summary writer was available.

    Raises:
      ValueError: if a default writer exists, but no step was provided and
        `tf.summary.experimental.get_step()` is None.
    '''
def text_pb(tag, data, description: Incomplete | None = None):
    """Create a text tf.Summary protobuf.

    Arguments:
      tag: String tag for the summary.
      data: A Python bytestring (of type bytes), a Unicode string, or a numpy data
        array of those types.
      description: Optional long-form description for this summary, as a `str`.
        Markdown is supported. Defaults to empty.

    Raises:
      TypeError: If the type of the data is unsupported.

    Returns:
      A `tf.Summary` protobuf object.
    """
