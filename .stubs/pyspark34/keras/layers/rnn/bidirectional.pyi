from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.base_layer import Layer as Layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.rnn import rnn_utils as rnn_utils
from keras.layers.rnn.base_wrapper import Wrapper as Wrapper
from keras.saving.legacy import serialization as serialization
from keras.utils import generic_utils as generic_utils, tf_inspect as tf_inspect, tf_utils as tf_utils

class Bidirectional(Wrapper):
    """Bidirectional wrapper for RNNs.

    Args:
      layer: `keras.layers.RNN` instance, such as `keras.layers.LSTM` or
        `keras.layers.GRU`. It could also be a `keras.layers.Layer` instance
        that meets the following criteria:
        1. Be a sequence-processing layer (accepts 3D+ inputs).
        2. Have a `go_backwards`, `return_sequences` and `return_state`
          attribute (with the same semantics as for the `RNN` class).
        3. Have an `input_spec` attribute.
        4. Implement serialization via `get_config()` and `from_config()`.
        Note that the recommended way to create new RNN layers is to write a
        custom RNN cell and use it with `keras.layers.RNN`, instead of
        subclassing `keras.layers.Layer` directly.
        - When the `returns_sequences` is true, the output of the masked
        timestep will be zero regardless of the layer's original
        `zero_output_for_mask` value.
      merge_mode: Mode by which outputs of the forward and backward RNNs will be
        combined. One of {'sum', 'mul', 'concat', 'ave', None}. If None, the
        outputs will not be combined, they will be returned as a list. Default
        value is 'concat'.
      backward_layer: Optional `keras.layers.RNN`, or `keras.layers.Layer`
        instance to be used to handle backwards input processing.
        If `backward_layer` is not provided, the layer instance passed as the
        `layer` argument will be used to generate the backward layer
        automatically.
        Note that the provided `backward_layer` layer should have properties
        matching those of the `layer` argument, in particular it should have the
        same values for `stateful`, `return_states`, `return_sequences`, etc.
        In addition, `backward_layer` and `layer` should have different
        `go_backwards` argument values.
        A `ValueError` will be raised if these requirements are not met.

    Call arguments:
      The call arguments for this layer are the same as those of the wrapped RNN
        layer.
      Beware that when passing the `initial_state` argument during the call of
      this layer, the first half in the list of elements in the `initial_state`
      list will be passed to the forward RNN call and the last half in the list
      of elements will be passed to the backward RNN call.

    Raises:
      ValueError:
        1. If `layer` or `backward_layer` is not a `Layer` instance.
        2. In case of invalid `merge_mode` argument.
        3. If `backward_layer` has mismatched properties compared to `layer`.

    Examples:

    ```python
    model = Sequential()
    model.add(Bidirectional(LSTM(10, return_sequences=True),
                                 input_shape=(5, 10)))
    model.add(Bidirectional(LSTM(10)))
    model.add(Dense(5))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

    # With custom backward layer
    model = Sequential()
    forward_layer = LSTM(10, return_sequences=True)
    backward_layer = LSTM(10, activation='relu', return_sequences=True,
                          go_backwards=True)
    model.add(Bidirectional(forward_layer, backward_layer=backward_layer,
                            input_shape=(5, 10)))
    model.add(Dense(5))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    ```
    """
    forward_layer: Incomplete
    backward_layer: Incomplete
    merge_mode: Incomplete
    stateful: Incomplete
    return_sequences: Incomplete
    return_state: Incomplete
    supports_masking: bool
    input_spec: Incomplete
    def __init__(self, layer, merge_mode: str = 'concat', weights: Incomplete | None = None, backward_layer: Incomplete | None = None, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def __call__(self, inputs, initial_state: Incomplete | None = None, constants: Incomplete | None = None, **kwargs):
        """`Bidirectional.__call__` implements the same API as the wrapped
        `RNN`."""
    def call(self, inputs, training: Incomplete | None = None, mask: Incomplete | None = None, initial_state: Incomplete | None = None, constants: Incomplete | None = None):
        """`Bidirectional.call` implements the same API as the wrapped `RNN`."""
    def reset_states(self) -> None: ...
    built: bool
    def build(self, input_shape) -> None: ...
    def compute_mask(self, inputs, mask): ...
    @property
    def constraints(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...
