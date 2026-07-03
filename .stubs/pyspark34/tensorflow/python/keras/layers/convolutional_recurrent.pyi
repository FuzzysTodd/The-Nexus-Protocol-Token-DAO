from _typeshed import Incomplete
from tensorflow.python.keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.layers.recurrent import DropoutRNNCellMixin as DropoutRNNCellMixin, RNN as RNN
from tensorflow.python.keras.utils import conv_utils as conv_utils, generic_utils as generic_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops
from tensorflow.python.util.tf_export import keras_export as keras_export

class ConvRNN2D(RNN):
    '''Base class for convolutional-recurrent layers.

  Args:
    cell: A RNN cell instance. A RNN cell is a class that has:
      - a `call(input_at_t, states_at_t)` method, returning
        `(output_at_t, states_at_t_plus_1)`. The call method of the
        cell can also take the optional argument `constants`, see
        section "Note on passing external constants" below.
      - a `state_size` attribute. This can be a single integer
        (single state) in which case it is
        the number of channels of the recurrent state
        (which should be the same as the number of channels of the cell
        output). This can also be a list/tuple of integers
        (one size per state). In this case, the first entry
        (`state_size[0]`) should be the same as
        the size of the cell output.
    return_sequences: Boolean. Whether to return the last output.
      in the output sequence, or the full sequence.
    return_state: Boolean. Whether to return the last state
      in addition to the output.
    go_backwards: Boolean (default False).
      If True, process the input sequence backwards and return the
      reversed sequence.
    stateful: Boolean (default False). If True, the last state
      for each sample at index i in a batch will be used as initial
      state for the sample of index i in the following batch.
    input_shape: Use this argument to specify the shape of the
      input when this layer is the first one in a model.

  Call arguments:
    inputs: A 5D tensor.
    mask: Binary tensor of shape `(samples, timesteps)` indicating whether
      a given timestep should be masked.
    training: Python boolean indicating whether the layer should behave in
      training mode or in inference mode. This argument is passed to the cell
      when calling it. This is for use with cells that use dropout.
    initial_state: List of initial state tensors to be passed to the first
      call of the cell.
    constants: List of constant tensors to be passed to the cell at each
      timestep.

  Input shape:
    5D tensor with shape:
    `(samples, timesteps, channels, rows, cols)`
    if data_format=\'channels_first\' or 5D tensor with shape:
    `(samples, timesteps, rows, cols, channels)`
    if data_format=\'channels_last\'.

  Output shape:
    - If `return_state`: a list of tensors. The first tensor is
      the output. The remaining tensors are the last states,
      each 4D tensor with shape:
      `(samples, filters, new_rows, new_cols)`
      if data_format=\'channels_first\'
      or 4D tensor with shape:
      `(samples, new_rows, new_cols, filters)`
      if data_format=\'channels_last\'.
      `rows` and `cols` values might have changed due to padding.
    - If `return_sequences`: 5D tensor with shape:
      `(samples, timesteps, filters, new_rows, new_cols)`
      if data_format=\'channels_first\'
      or 5D tensor with shape:
      `(samples, timesteps, new_rows, new_cols, filters)`
      if data_format=\'channels_last\'.
    - Else, 4D tensor with shape:
      `(samples, filters, new_rows, new_cols)`
      if data_format=\'channels_first\'
      or 4D tensor with shape:
      `(samples, new_rows, new_cols, filters)`
      if data_format=\'channels_last\'.

  Masking:
    This layer supports masking for input data with a variable number
    of timesteps.

  Note on using statefulness in RNNs:
    You can set RNN layers to be \'stateful\', which means that the states
    computed for the samples in one batch will be reused as initial states
    for the samples in the next batch. This assumes a one-to-one mapping
    between samples in different successive batches.
    To enable statefulness:
      - Specify `stateful=True` in the layer constructor.
      - Specify a fixed batch size for your model, by passing
         - If sequential model:
            `batch_input_shape=(...)` to the first layer in your model.
         - If functional model with 1 or more Input layers:
            `batch_shape=(...)` to all the first layers in your model.
            This is the expected shape of your inputs
            *including the batch size*.
            It should be a tuple of integers,
            e.g. `(32, 10, 100, 100, 32)`.
            Note that the number of rows and columns should be specified
            too.
      - Specify `shuffle=False` when calling fit().
    To reset the states of your model, call `.reset_states()` on either
    a specific layer, or on your entire model.

  Note on specifying the initial state of RNNs:
    You can specify the initial state of RNN layers symbolically by
    calling them with the keyword argument `initial_state`. The value of
    `initial_state` should be a tensor or list of tensors representing
    the initial state of the RNN layer.
    You can specify the initial state of RNN layers numerically by
    calling `reset_states` with the keyword argument `states`. The value of
    `states` should be a numpy array or list of numpy arrays representing
    the initial state of the RNN layer.

  Note on passing external constants to RNNs:
    You can pass "external" constants to the cell using the `constants`
    keyword argument of `RNN.__call__` (as well as `RNN.call`) method. This
    requires that the `cell.call` method accepts the same keyword argument
    `constants`. Such constants can be used to condition the cell
    transformation on additional static inputs (not changing over time),
    a.k.a. an attention mechanism.
  '''
    input_spec: Incomplete
    states: Incomplete
    def __init__(self, cell, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, unroll: bool = False, **kwargs) -> None: ...
    def compute_output_shape(self, input_shape): ...
    state_spec: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def get_initial_state(self, inputs): ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, initial_state: Incomplete | None = None, constants: Incomplete | None = None): ...
    def reset_states(self, states: Incomplete | None = None): ...

class ConvLSTM2DCell(DropoutRNNCellMixin, Layer):
    '''Cell class for the ConvLSTM2D layer.

  Args:
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
      It defaults to the `image_data_format` value found in your
      Keras config file at `~/.keras/keras.json`.
      If you never set it, then it will be "channels_last".
    dilation_rate: An integer or tuple/list of n integers, specifying
      the dilation rate to use for dilated convolution.
      Currently, specifying any `dilation_rate` value != 1 is
      incompatible with specifying any `strides` value != 1.
    activation: Activation function to use.
      If you don\'t specify anything, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
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
    kernel_constraint: Constraint function applied to
      the `kernel` weights matrix.
    recurrent_constraint: Constraint function applied to
      the `recurrent_kernel` weights matrix.
    bias_constraint: Constraint function applied to the bias vector.
    dropout: Float between 0 and 1.
      Fraction of the units to drop for
      the linear transformation of the inputs.
    recurrent_dropout: Float between 0 and 1.
      Fraction of the units to drop for
      the linear transformation of the recurrent state.

  Call arguments:
    inputs: A 4D tensor.
    states:  List of state tensors corresponding to the previous timestep.
    training: Python boolean indicating whether the layer should behave in
      training mode or in inference mode. Only relevant when `dropout` or
      `recurrent_dropout` is used.
  '''
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
    def __init__(self, filters, kernel_size, strides=(1, 1), padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate=(1, 1), activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
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

class ConvLSTM2D(ConvRNN2D):
    '''2D Convolutional LSTM layer.

  A convolutional LSTM is similar to an LSTM, but the input transformations
  and recurrent transformations are both convolutional. This layer is typically
  used to process timeseries of images (i.e. video-like data).

  It is known to perform well for weather data forecasting,
  using inputs that are timeseries of 2D grids of sensor values.
  It isn\'t usually applied to regular video data, due to its high computational
  cost.

  Args:
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

  Call arguments:
    inputs: A 5D float tensor (see input shape description below).
    mask: Binary tensor of shape `(samples, timesteps)` indicating whether
      a given timestep should be masked.
    training: Python boolean indicating whether the layer should behave in
      training mode or in inference mode. This argument is passed to the cell
      when calling it. This is only relevant if `dropout` or `recurrent_dropout`
      are set.
    initial_state: List of initial state tensors to be passed to the first
      call of the cell.

  Input shape:
    - If data_format=\'channels_first\'
        5D tensor with shape:
        `(samples, time, channels, rows, cols)`
    - If data_format=\'channels_last\'
        5D tensor with shape:
        `(samples, time, rows, cols, channels)`

  Output shape:
    - If `return_state`: a list of tensors. The first tensor is
      the output. The remaining tensors are the last states,
      each 4D tensor with shape:
      `(samples, filters, new_rows, new_cols)`
      if data_format=\'channels_first\'
      or 4D tensor with shape:
      `(samples, new_rows, new_cols, filters)`
      if data_format=\'channels_last\'.
      `rows` and `cols` values might have changed due to padding.
    - If `return_sequences`: 5D tensor with shape:
      `(samples, timesteps, filters, new_rows, new_cols)`
      if data_format=\'channels_first\'
      or 5D tensor with shape:
      `(samples, timesteps, new_rows, new_cols, filters)`
      if data_format=\'channels_last\'.
    - Else, 4D tensor with shape:
      `(samples, filters, new_rows, new_cols)`
      if data_format=\'channels_first\'
      or 4D tensor with shape:
      `(samples, new_rows, new_cols, filters)`
      if data_format=\'channels_last\'.

  Raises:
    ValueError: in case of invalid constructor arguments.

  References:
    - [Shi et al., 2015](http://arxiv.org/abs/1506.04214v1)
    (the current implementation does not include the feedback loop on the
    cells output).

  Example:

  ```python
  steps = 10
  height = 32
  width = 32
  input_channels = 3
  output_channels = 6

  inputs = tf.keras.Input(shape=(steps, height, width, input_channels))
  layer = tf.keras.layers.ConvLSTM2D(filters=output_channels, kernel_size=3)
  outputs = layer(inputs)
  ```
  '''
    activity_regularizer: Incomplete
    def __init__(self, filters, kernel_size, strides=(1, 1), padding: str = 'valid', data_format: Incomplete | None = None, dilation_rate=(1, 1), activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
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
