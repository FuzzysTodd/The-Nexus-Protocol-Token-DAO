from _typeshed import Incomplete
from keras import backend as backend
from keras.engine import base_layer as base_layer
from keras.layers.rnn import rnn_utils as rnn_utils
from keras.saving.legacy import serialization as serialization
from keras.utils import generic_utils as generic_utils, tf_utils as tf_utils

class StackedRNNCells(base_layer.Layer):
    """Wrapper allowing a stack of RNN cells to behave as a single cell.

    Used to implement efficient stacked RNNs.

    Args:
      cells: List of RNN cell instances.

    Examples:

    ```python
    batch_size = 3
    sentence_max_length = 5
    n_features = 2
    new_shape = (batch_size, sentence_max_length, n_features)
    x = tf.constant(np.reshape(np.arange(30), new_shape), dtype = tf.float32)

    rnn_cells = [tf.keras.layers.LSTMCell(128) for _ in range(2)]
    stacked_lstm = tf.keras.layers.StackedRNNCells(rnn_cells)
    lstm_layer = tf.keras.layers.RNN(stacked_lstm)

    result = lstm_layer(x)
    ```
    """
    cells: Incomplete
    reverse_state_order: Incomplete
    def __init__(self, cells, **kwargs) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...
    def call(self, inputs, states, constants: Incomplete | None = None, training: Incomplete | None = None, **kwargs): ...
    built: bool
    def build(self, input_shape): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
