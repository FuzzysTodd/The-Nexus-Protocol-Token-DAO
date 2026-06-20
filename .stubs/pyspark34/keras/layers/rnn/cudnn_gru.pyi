from _typeshed import Incomplete
from keras import constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.layers.rnn import gru_lstm_utils as gru_lstm_utils
from keras.layers.rnn.base_cudnn_rnn import _CuDNNRNN

class CuDNNGRU(_CuDNNRNN):
    '''Fast GRU implementation backed by cuDNN.

    More information about cuDNN can be found on the [NVIDIA
    developer website](https://developer.nvidia.com/cudnn).
    Can only be run on GPU.

    Args:
        units: Positive integer, dimensionality of the output space.
        kernel_initializer: Initializer for the `kernel` weights matrix, used
          for the linear transformation of the inputs.
        recurrent_initializer: Initializer for the `recurrent_kernel` weights
          matrix, used for the linear transformation of the recurrent state.
        bias_initializer: Initializer for the bias vector.
        kernel_regularizer: Regularizer function applied to the `kernel` weights
          matrix.
        recurrent_regularizer: Regularizer function applied to the
          `recurrent_kernel` weights matrix.
        bias_regularizer: Regularizer function applied to the bias vector.
        activity_regularizer: Regularizer function applied to the output of the
          layer (its "activation").
        kernel_constraint: Constraint function applied to the `kernel` weights
          matrix.
        recurrent_constraint: Constraint function applied to the
          `recurrent_kernel` weights matrix.
        bias_constraint: Constraint function applied to the bias vector.
        return_sequences: Boolean. Whether to return the last output in the
          output sequence, or the full sequence.
        return_state: Boolean. Whether to return the last state in addition to
          the output.
        go_backwards: Boolean (default False). If True, process the input
          sequence backwards and return the reversed sequence.
        stateful: Boolean (default False). If True, the last state for each
          sample at index i in a batch will be used as initial state for the
          sample of index i in the following batch.
    '''
    units: Incomplete
    kernel_initializer: Incomplete
    recurrent_initializer: Incomplete
    bias_initializer: Incomplete
    kernel_regularizer: Incomplete
    recurrent_regularizer: Incomplete
    bias_regularizer: Incomplete
    activity_regularizer: Incomplete
    kernel_constraint: Incomplete
    recurrent_constraint: Incomplete
    bias_constraint: Incomplete
    def __init__(self, units, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, **kwargs) -> None: ...
    @property
    def cell(self): ...
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def get_config(self): ...
