from _typeshed import Incomplete
from tensorboard.plugins.audio import metadata as metadata, summary_v2 as summary_v2

audio = summary_v2.audio

def op(name, audio, sample_rate, labels: Incomplete | None = None, max_outputs: int = 3, encoding: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None):
    '''Create a legacy audio summary op for use in a TensorFlow graph.

    Arguments:
      name: A unique name for the generated summary node.
      audio: A `Tensor` representing audio data with shape `[k, t, c]`,
        where `k` is the number of audio clips, `t` is the number of
        frames, and `c` is the number of channels. Elements should be
        floating-point values in `[-1.0, 1.0]`. Any of the dimensions may
        be statically unknown (i.e., `None`).
      sample_rate: An `int` or rank-0 `int32` `Tensor` that represents the
        sample rate, in Hz. Must be positive.
      labels: Deprecated. Do not set.
      max_outputs: Optional `int` or rank-0 integer `Tensor`. At most this
        many audio clips will be emitted at each step. When more than
        `max_outputs` many clips are provided, the first `max_outputs`
        many clips will be used and the rest silently discarded.
      encoding: A constant `str` (not string tensor) indicating the
        desired encoding. You can choose any format you like, as long as
        it\'s "wav". Please see the "API compatibility note" below.
      display_name: Optional name for this summary in TensorBoard, as a
        constant `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
        constant `str`. Markdown is supported. Defaults to empty.
      collections: Optional list of graph collections keys. The new
        summary op is added to these collections. Defaults to
        `[Graph Keys.SUMMARIES]`.

    Returns:
      A TensorFlow summary op.

    API compatibility note: The default value of the `encoding`
    argument is _not_ guaranteed to remain unchanged across TensorBoard
    versions. In the future, we will by default encode as FLAC instead of
    as WAV. If the specific format is important to you, please provide a
    file format explicitly.
    '''
def pb(name, audio, sample_rate, labels: Incomplete | None = None, max_outputs: int = 3, encoding: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None):
    '''Create a legacy audio summary protobuf.

    This behaves as if you were to create an `op` with the same arguments
    (wrapped with constant tensors where appropriate) and then execute
    that summary op in a TensorFlow session.

    Arguments:
      name: A unique name for the generated summary node.
      audio: An `np.array` representing audio data with shape `[k, t, c]`,
        where `k` is the number of audio clips, `t` is the number of
        frames, and `c` is the number of channels. Elements should be
        floating-point values in `[-1.0, 1.0]`.
      sample_rate: An `int` that represents the sample rate, in Hz.
        Must be positive.
      labels: Deprecated. Do not set.
      max_outputs: Optional `int`. At most this many audio clips will be
        emitted. When more than `max_outputs` many clips are provided, the
        first `max_outputs` many clips will be used and the rest silently
        discarded.
      encoding: A constant `str` indicating the desired encoding. You
        can choose any format you like, as long as it\'s "wav". Please see
        the "API compatibility note" below.
      display_name: Optional name for this summary in TensorBoard, as a
        `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
        `str`. Markdown is supported. Defaults to empty.

    Returns:
      A `tf.Summary` protobuf object.

    API compatibility note: The default value of the `encoding`
    argument is _not_ guaranteed to remain unchanged across TensorBoard
    versions. In the future, we will by default encode as FLAC instead of
    as WAV. If the specific format is important to you, please provide a
    file format explicitly.
    '''
