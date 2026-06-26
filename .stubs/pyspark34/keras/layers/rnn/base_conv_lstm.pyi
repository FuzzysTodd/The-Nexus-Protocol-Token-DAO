from _typeshed import Incomplete
from keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine import base_layer as base_layer
from keras.layers.rnn.base_conv_rnn import ConvRNN as ConvRNN
from keras.layers.rnn.dropout_rnn_cell_mixin import DropoutRNNCellMixin as DropoutRNNCellMixin
from keras.utils import conv_utils as conv_utils

class ConvLSTMCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    '''Cell class for the ConvLSTM layer.

    Args:
      rank: Integer, rank of the convolution, e.g. "2" for 2D convolutions.
      filters: Integer, the dimensionality of the output space (i.e. the number
        of output filters in the convolution).
      kernel_size: An integer or tuple/list of n integers, specifying the
        dimensions of the convolution window.
      strides: An integer or tuple/list of n integers, specifying the strides of
        the convolution. Specifying any stride value != 1 is incompatible with
        specifying any `dilation_rate` value != 1.
      padding: One of `"valid"` or `"same"` (case-insensitive). `"valid"` means
        no padding. `"same"` results in padding evenly to the left/right or
        up/down of the input such that output has the same height/width
        dimension as the input.
      data_format: A string, one of `channels_last` (default) or
        `channels_first`.  It defaults to the `image_data_format` value found in
        your Keras config file at `~/.keras/keras.json`. If you never set it,
        then it will be "channels_last".
      dilation_rate: An integer or tuple/list of n integers, specifying the
        dilation rate to use for dilated convolution. Currently, specifying any
        `dilation_rate` value != 1 is incompatible with specifying any `strides`
        value != 1.
      activation: Activation function to use. If you don\'t specify anything, no
        activation is applied
        (ie. "linear" activation: `a(x) = x`).
      recurrent_activation: Activation function to use for the recurrent step.
      use_bias: Boolean, whether the layer uses a bias vector.
      kernel_initializer: Initializer for the `kernel` weights matrix, used for
        the linear transformation of the inputs.
      recurrent_initializer: Initializer for the `recurrent_kernel` weights
        matrix, used for the linear transformation of the recurrent state.
      bias_initializer: Initializer for the bias vector.
      unit_forget_bias: Boolean. If True, add 1 to the bias of the forget gate
      at initialization. Use in combination with `bias_initializer="zeros"`.
      This is recommended in [Jozefowicz et al., 2015](
      http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
      kernel_regularizer: Regularizer function applied to the `kernel` weights
        matrix.
      recurrent_regularizer: Regularizer function applied to the
        `recurrent_kernel` weights matrix.
      bias_regularizer: Regularizer function applied to the bias vector.
      kernel_constraint: Constraint function applied to the `kernel` weights
        matrix.
      recurrent_constraint: Constraint function applied to the
        `recurrent_kernel` weights matrix.
      bias_constraint: Constraint function applied to the bias vector.
      dropout: Float between 0 and 1. Fraction of the units to drop for the
        linear transformation of the inputs.
      recurrent_dropout: Float between 0 and 1. Fraction of the units to drop
        for the linear transformation of the recurrent state.
    Call arguments:
      inputs: A (2+ `rank`)D tensor.
      states:  List of state tensors corresponding to the previous timestep.
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode. Only relevant when `dropout` or
        `recurrent_dropout` is used.
    '''
    rank: Incomplete
    filters: Incomplete
    kernel_size: Incomplete
    strides: Incomplete
    padding: Incomplete
    data_format: Incomplete
    dilation_rate: Incomplete
    activation: Incomplete
    recurrent_activation: Incomplete
    use_bias: Incomplete
    kernel_initializer: Incomplete
    recurrent_initializer: Incomplete
    bias_initializer: Incomplete
    unit_forget_bias: Incomplete
    kernel_regularizer: Incomplete
    recurrent_regularizer: Incomplete
    bias_regularizer: Incomplete
    kernel_constraint: Incomplete
    recurrent_constraint: Incomplete
    bias_constraint: Incomplete
    dropout: Incomplete
    recurrent_dropout: Incomplete
    state_size: Incomplete
    def __init__(self, rank, filters, kernel_size, strides: int = 1, padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate: int = 1, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
    kernel_shape: Incomplete
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape): ...
    def call(self, inputs, states, training: Incomplete | None = None): ...
    def input_conv(self, x, w, b: Incomplete | None = None, padding: str = 'valid'): ...
    def recurrent_conv(self, x, w): ...
    def get_config(self): ...

class ConvLSTM(ConvRNN):
    '''Abstract N-D Convolutional LSTM layer (used as implementation base).

    Similar to an LSTM layer, but the input transformations
    and recurrent transformations are both convolutional.

    Args:
      rank: Integer, rank of the convolution, e.g. "2" for 2D convolutions.
      filters: Integer, the dimensionality of the output space
        (i.e. the number of output filters in the convolution).
      kernel_size: An integer or tuple/list of n integers, specifying the
        dimensions of the convolution window.
      strides: An integer or tuple/list of n integers,
        specifying the strides of the convolution.
        Specifying any stride value != 1 is incompatible with specifying
        any `dilation_rate` value != 1.
      padding: One of `"valid"` or `"same"` (case-insensitive).
        `"valid"` means no padding. `"same"` results in padding evenly to
        the left/right or up/down of the input such that output has the same
        height/width dimension as the input.
      data_format: A string,
        one of `channels_last` (default) or `channels_first`.
        The ordering of the dimensions in the inputs.
        `channels_last` corresponds to inputs with shape
        `(batch, time, ..., channels)`
        while `channels_first` corresponds to
        inputs with shape `(batch, time, channels, ...)`.
        It defaults to the `image_data_format` value found in your
        Keras config file at `~/.keras/keras.json`.
        If you never set it, then it will be "channels_last".
      dilation_rate: An integer or tuple/list of n integers, specifying
        the dilation rate to use for dilated convolution.
        Currently, specifying any `dilation_rate` value != 1 is
        incompatible with specifying any `strides` value != 1.
      activation: Activation function to use.
        By default hyperbolic tangent activation function is applied
        (`tanh(x)`).
      recurrent_activation: Activation function to use
        for the recurrent step.
      use_bias: Boolean, whether the layer uses a bias vector.
      kernel_initializer: Initializer for the `kernel` weights matrix,
        used for the linear transformation of the inputs.
      recurrent_initializer: Initializer for the `recurrent_kernel`
        weights matrix,
        used for the linear transformation of the recurrent state.
      bias_initializer: Initializer for the bias vector.
      unit_forget_bias: Boolean.
        If True, add 1 to the bias of the forget gate at initialization.
        Use in combination with `bias_initializer="zeros"`.
        This is recommended in [Jozefowicz et al., 2015](
          http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
      kernel_regularizer: Regularizer function applied to
        the `kernel` weights matrix.
      recurrent_regularizer: Regularizer function applied to
        the `recurrent_kernel` weights matrix.
      bias_regularizer: Regularizer function applied to the bias vector.
      activity_regularizer: Regularizer function applied to.
      kernel_constraint: Constraint function applied to
        the `kernel` weights matrix.
      recurrent_constraint: Constraint function applied to
        the `recurrent_kernel` weights matrix.
      bias_constraint: Constraint function applied to the bias vector.
      return_sequences: Boolean. Whether to return the last output
        in the output sequence, or the full sequence. (default False)
      return_state: Boolean Whether to return the last state
        in addition to the output. (default False)
      go_backwards: Boolean (default False).
        If True, process the input sequence backwards.
      stateful: Boolean (default False). If True, the last state
        for each sample at index i in a batch will be used as initial
        state for the sample of index i in the following batch.
      dropout: Float between 0 and 1.
        Fraction of the units to drop for
        the linear transformation of the inputs.
      recurrent_dropout: Float between 0 and 1.
        Fraction of the units to drop for
        the linear transformation of the recurrent state.
    '''
    activity_regularizer: Incomplete
    def __init__(self, rank, filters, kernel_size, strides: int = 1, padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate: int = 1, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, initial_state: Incomplete | None = None): ...
    @property
    def filters(self): ...
    @property
    def kernel_size(self): ...
    @property
    def strides(self): ...
    @property
    def padding(self): ...
    @property
    def data_format(self): ...
    @property
    def dilation_rate(self): ...
    @property
    def activation(self): ...
    @property
    def recurrent_activation(self): ...
    @property
    def use_bias(self): ...
    @property
    def kernel_initializer(self): ...
    @property
    def recurrent_initializer(self): ...
    @property
    def bias_initializer(self): ...
    @property
    def unit_forget_bias(self): ...
    @property
    def kernel_regularizer(self): ...
    @property
    def recurrent_regularizer(self): ...
    @property
    def bias_regularizer(self): ...
    @property
    def kernel_constraint(self): ...
    @property
    def recurrent_constraint(self): ...
    @property
    def bias_constraint(self): ...
    @property
    def dropout(self): ...
    @property
    def recurrent_dropout(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
