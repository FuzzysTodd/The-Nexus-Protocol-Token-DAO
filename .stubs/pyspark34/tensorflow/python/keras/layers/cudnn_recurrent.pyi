from _typeshed import Incomplete
from tensorflow.python.framework import constant_op as constant_op
from tensorflow.python.keras import backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers import recurrent_v2 as recurrent_v2
from tensorflow.python.keras.layers.recurrent import RNN as RNN
from tensorflow.python.ops import array_ops as array_ops, gen_cudnn_rnn_ops as gen_cudnn_rnn_ops, state_ops as state_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

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
    time_major: Boolean (default False). If true, the inputs and outputs will be
        in shape `(timesteps, batch, ...)`, whereas in the False case, it will
        be `(batch, timesteps, ...)`.
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

class CuDNNGRU(_CuDNNRNN):
    '''Fast GRU implementation backed by cuDNN.

  More information about cuDNN can be found on the [NVIDIA
  developer website](https://developer.nvidia.com/cudnn).
  Can only be run on GPU.

  Args:
      units: Positive integer, dimensionality of the output space.
      kernel_initializer: Initializer for the `kernel` weights matrix, used for
        the linear transformation of the inputs.
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
      return_sequences: Boolean. Whether to return the last output in the output
        sequence, or the full sequence.
      return_state: Boolean. Whether to return the last state in addition to the
        output.
      go_backwards: Boolean (default False). If True, process the input sequence
        backwards and return the reversed sequence.
      stateful: Boolean (default False). If True, the last state for each sample
        at index i in a batch will be used as initial state for the sample of
        index i in the following batch.
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

class CuDNNLSTM(_CuDNNRNN):
    '''Fast LSTM implementation backed by cuDNN.

  More information about cuDNN can be found on the [NVIDIA
  developer website](https://developer.nvidia.com/cudnn).
  Can only be run on GPU.

  Args:
      units: Positive integer, dimensionality of the output space.
      kernel_initializer: Initializer for the `kernel` weights matrix, used for
        the linear transformation of the inputs.
      unit_forget_bias: Boolean. If True, add 1 to the bias of the forget gate
        at initialization. Setting it to true will also force
        `bias_initializer="zeros"`. This is recommended in [Jozefowicz et
        al.](http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
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
      return_sequences: Boolean. Whether to return the last output. in the
        output sequence, or the full sequence.
      return_state: Boolean. Whether to return the last state in addition to the
        output.
      go_backwards: Boolean (default False). If True, process the input sequence
        backwards and return the reversed sequence.
      stateful: Boolean (default False). If True, the last state for each sample
        at index i in a batch will be used as initial state for the sample of
        index i in the following batch.
  '''
    units: Incomplete
    kernel_initializer: Incomplete
    recurrent_initializer: Incomplete
    bias_initializer: Incomplete
    unit_forget_bias: Incomplete
    kernel_regularizer: Incomplete
    recurrent_regularizer: Incomplete
    bias_regularizer: Incomplete
    activity_regularizer: Incomplete
    kernel_constraint: Incomplete
    recurrent_constraint: Incomplete
    bias_constraint: Incomplete
    def __init__(self, units, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, **kwargs) -> None: ...
    @property
    def cell(self): ...
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape): ...
    def get_config(self): ...
