from _typeshed import Incomplete
from keras import backend as backend
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.rnn.base_rnn import RNN as RNN

class _CuDNNRNN(RNN):
    """Private base class for CuDNNGRU and CuDNNLSTM layers.

    Args:
      return_sequences: Boolean. Whether to return the last output
          in the output sequence, or the full sequence.
      return_state: Boolean. Whether to return the last state
          in addition to the output.
      go_backwards: Boolean (default False).
          If True, process the input sequence backwards and return the
          reversed sequence.
      stateful: Boolean (default False). If True, the last state
          for each sample at index i in a batch will be used as initial
          state for the sample of index i in the following batch.
      time_major: Boolean (default False). If true, the inputs and outputs will
          be in shape `(timesteps, batch, ...)`, whereas in the False case, it
          will be `(batch, timesteps, ...)`.
    """
    return_sequences: Incomplete
    return_state: Incomplete
    go_backwards: Incomplete
    stateful: Incomplete
    time_major: Incomplete
    supports_masking: bool
    input_spec: Incomplete
    state_spec: Incomplete
    constants_spec: Incomplete
    def __init__(self, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, time_major: bool = False, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, initial_state: Incomplete | None = None): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    @property
    def losses(self): ...
    def get_losses_for(self, inputs: Incomplete | None = None): ...
