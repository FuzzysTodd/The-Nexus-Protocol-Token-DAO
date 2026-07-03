import keras
import tensorflow.compat.v2 as tf
from _typeshed import Incomplete

class LayerBenchmark(tf.test.Benchmark):
    """Benchmark the layer forward pass."""
    def report(self, name, keras_time, fc_time, iters) -> None:
        """Calculate and report benchmark statistics."""

class StepTimingCallback(keras.callbacks.Callback):
    """A callback that times non-warmup steps of a Keras predict call."""
    t0: Incomplete
    steps: int
    def __init__(self) -> None: ...
    def on_predict_batch_begin(self, batch_index, _) -> None: ...
    tn: Incomplete
    t_avg: Incomplete
    def on_predict_end(self, _) -> None: ...

def create_data(length, num_entries, max_value, dtype):
    """Create a ragged tensor with random data entries."""
def create_string_data(length, num_entries, vocabulary, pct_oov, oov_string: str = '__OOV__'):
    """Create a ragged tensor with random data entries."""
def create_vocabulary(vocab_size): ...
def run_keras(data, model, batch_size, num_runs, steps_per_repeat: int = 100):
    """Benchmark a Keras model."""
def run_fc(data, fc_fn, batch_size, num_runs, steps_per_repeat: int = 100):
    """Benchmark a Feature Column."""
