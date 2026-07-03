from _typeshed import Incomplete
from tensorboard.util import op_evaluator as op_evaluator

class _TensorFlowPngEncoder(op_evaluator.PersistentOpEvaluator):
    """Encode an image to PNG.

    This function is thread-safe, and has high performance when run in
    parallel. See `encode_png_benchmark.py` for details.

    Arguments:
      image: A numpy array of shape `[height, width, channels]`, where
        `channels` is 1, 3, or 4, and of dtype uint8.

    Returns:
      A bytestring with PNG-encoded data.
    """
    def __init__(self) -> None: ...
    def initialize_graph(self) -> None: ...
    def run(self, image): ...

encode_png: Incomplete

class _TensorFlowWavEncoder(op_evaluator.PersistentOpEvaluator):
    """Encode an audio clip to WAV.

    This function is thread-safe and exhibits good parallel performance.

    Arguments:
      audio: A numpy array of shape `[samples, channels]`.
      samples_per_second: A positive `int`, in Hz.

    Returns:
      A bytestring with WAV-encoded data.
    """
    def __init__(self) -> None: ...
    def initialize_graph(self) -> None: ...
    def run(self, audio, samples_per_second): ...

encode_wav: Incomplete
