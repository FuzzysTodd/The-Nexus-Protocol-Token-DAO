from _typeshed import Incomplete
from keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine import base_layer as base_layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.rnn import gru_lstm_utils as gru_lstm_utils, rnn_utils as rnn_utils
from keras.layers.rnn.base_rnn import RNN as RNN
from keras.layers.rnn.dropout_rnn_cell_mixin import DropoutRNNCellMixin as DropoutRNNCellMixin
from keras.utils import tf_utils as tf_utils

RECURRENT_DROPOUT_WARNING_MSG: str

class GRUCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    '''Cell class for the GRU layer.

    See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
    for details about the usage of RNN API.

    This class processes one step within the whole time sequence input, whereas
    `tf.keras.layer.GRU` processes the whole sequence.

    For example:

    >>> inputs = tf.random.normal([32, 10, 8])
    >>> rnn = tf.keras.layers.RNN(tf.keras.layers.GRUCell(4))
    >>> output = rnn(inputs)
    >>> print(output.shape)
    (32, 4)
    >>> rnn = tf.keras.layers.RNN(
    ...    tf.keras.layers.GRUCell(4),
    ...    return_sequences=True,
    ...    return_state=True)
    >>> whole_sequence_output, final_state = rnn(inputs)
    >>> print(whole_sequence_output.shape)
    (32, 10, 4)
    >>> print(final_state.shape)
    (32, 4)

    Args:
      units: Positive integer, dimensionality of the output space.
      activation: Activation function to use. Default: hyperbolic tangent
        (`tanh`). If you pass None, no activation is applied
        (ie. "linear" activation: `a(x) = x`).
      recurrent_activation: Activation function to use for the recurrent step.
        Default: sigmoid (`sigmoid`). If you pass `None`, no activation is
        applied (ie. "linear" activation: `a(x) = x`).
      use_bias: Boolean, (default `True`), whether the layer uses a bias vector.
      kernel_initializer: Initializer for the `kernel` weights matrix,
        used for the linear transformation of the inputs. Default:
        `glorot_uniform`.
      recurrent_initializer: Initializer for the `recurrent_kernel`
        weights matrix, used for the linear transformation of the recurrent
        state.  Default: `orthogonal`.
      bias_initializer: Initializer for the bias vector. Default: `zeros`.
      kernel_regularizer: Regularizer function applied to the `kernel` weights
        matrix. Default: `None`.
      recurrent_regularizer: Regularizer function applied to the
        `recurrent_kernel` weights matrix. Default: `None`.
      bias_regularizer: Regularizer function applied to the bias vector.
        Default: `None`.
      kernel_constraint: Constraint function applied to the `kernel` weights
        matrix. Default: `None`.
      recurrent_constraint: Constraint function applied to the
        `recurrent_kernel` weights matrix. Default: `None`.
      bias_constraint: Constraint function applied to the bias vector. Default:
        `None`.
      dropout: Float between 0 and 1. Fraction of the units to drop for the
        linear transformation of the inputs. Default: 0.
      recurrent_dropout: Float between 0 and 1. Fraction of the units to drop
        for the linear transformation of the recurrent state. Default: 0.
      reset_after: GRU convention (whether to apply reset gate after or
        before matrix multiplication). False = "before",
        True = "after" (default and cuDNN compatible).

    Call arguments:
      inputs: A 2D tensor, with shape of `[batch, feature]`.
      states: A 2D tensor with shape of `[batch, units]`, which is the state
        from the previous time step. For timestep 0, the initial state provided
        by user will be feed to cell.
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode. Only relevant when `dropout` or
        `recurrent_dropout` is used.
    '''
    units: Incomplete
    activation: Incomplete
    recurrent_activation: Incomplete
    use_bias: Incomplete
    kernel_initializer: Incomplete
    recurrent_initializer: Incomplete
    bias_initializer: Incomplete
    kernel_regularizer: Incomplete
    recurrent_regularizer: Incomplete
    bias_regularizer: Incomplete
    kernel_constraint: Incomplete
    recurrent_constraint: Incomplete
    bias_constraint: Incomplete
    dropout: Incomplete
    recurrent_dropout: Incomplete
    implementation: int
    reset_after: Incomplete
    state_size: Incomplete
    output_size: Incomplete
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, reset_after: bool = True, **kwargs) -> None: ...
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs, states, training: Incomplete | None = None): ...
    def get_config(self): ...
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...

class GRU(DropoutRNNCellMixin, RNN, base_layer.BaseRandomLayer):
    '''Gated Recurrent Unit - Cho et al. 2014.

    See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
    for details about the usage of RNN API.

    Based on available runtime hardware and constraints, this layer
    will choose different implementations (cuDNN-based or pure-TensorFlow)
    to maximize the performance. If a GPU is available and all
    the arguments to the layer meet the requirement of the cuDNN kernel
    (see below for details), the layer will use a fast cuDNN implementation.

    The requirements to use the cuDNN implementation are:

    1. `activation` == `tanh`
    2. `recurrent_activation` == `sigmoid`
    3. `recurrent_dropout` == 0
    4. `unroll` is `False`
    5. `use_bias` is `True`
    6. `reset_after` is `True`
    7. Inputs, if use masking, are strictly right-padded.
    8. Eager execution is enabled in the outermost context.

    There are two variants of the GRU implementation. The default one is based
    on [v3](https://arxiv.org/abs/1406.1078v3) and has reset gate applied to
    hidden state before matrix multiplication. The other one is based on
    [original](https://arxiv.org/abs/1406.1078v1) and has the order reversed.

    The second variant is compatible with CuDNNGRU (GPU-only) and allows
    inference on CPU. Thus it has separate biases for `kernel` and
    `recurrent_kernel`. To use this variant, set `reset_after=True` and
    `recurrent_activation=\'sigmoid\'`.

    For example:

    >>> inputs = tf.random.normal([32, 10, 8])
    >>> gru = tf.keras.layers.GRU(4)
    >>> output = gru(inputs)
    >>> print(output.shape)
    (32, 4)
    >>> gru = tf.keras.layers.GRU(4, return_sequences=True, return_state=True)
    >>> whole_sequence_output, final_state = gru(inputs)
    >>> print(whole_sequence_output.shape)
    (32, 10, 4)
    >>> print(final_state.shape)
    (32, 4)

    Args:
      units: Positive integer, dimensionality of the output space.
      activation: Activation function to use.
        Default: hyperbolic tangent (`tanh`).
        If you pass `None`, no activation is applied
        (ie. "linear" activation: `a(x) = x`).
      recurrent_activation: Activation function to use
        for the recurrent step.
        Default: sigmoid (`sigmoid`).
        If you pass `None`, no activation is applied
        (ie. "linear" activation: `a(x) = x`).
      use_bias: Boolean, (default `True`), whether the layer uses a bias vector.
      kernel_initializer: Initializer for the `kernel` weights matrix,
        used for the linear transformation of the inputs. Default:
        `glorot_uniform`.
      recurrent_initializer: Initializer for the `recurrent_kernel`
         weights matrix, used for the linear transformation of the recurrent
         state. Default: `orthogonal`.
      bias_initializer: Initializer for the bias vector. Default: `zeros`.
      kernel_regularizer: Regularizer function applied to the `kernel` weights
        matrix. Default: `None`.
      recurrent_regularizer: Regularizer function applied to the
        `recurrent_kernel` weights matrix. Default: `None`.
      bias_regularizer: Regularizer function applied to the bias vector.
        Default: `None`.
      activity_regularizer: Regularizer function applied to the output of the
        layer (its "activation"). Default: `None`.
      kernel_constraint: Constraint function applied to the `kernel` weights
        matrix. Default: `None`.
      recurrent_constraint: Constraint function applied to the
        `recurrent_kernel` weights matrix. Default: `None`.
      bias_constraint: Constraint function applied to the bias vector. Default:
        `None`.
      dropout: Float between 0 and 1. Fraction of the units to drop for the
        linear transformation of the inputs. Default: 0.
      recurrent_dropout: Float between 0 and 1. Fraction of the units to drop
        for the linear transformation of the recurrent state. Default: 0.
      return_sequences: Boolean. Whether to return the last output
        in the output sequence, or the full sequence. Default: `False`.
      return_state: Boolean. Whether to return the last state in addition to the
        output. Default: `False`.
      go_backwards: Boolean (default `False`).
        If True, process the input sequence backwards and return the
        reversed sequence.
      stateful: Boolean (default False). If True, the last state
        for each sample at index i in a batch will be used as initial
        state for the sample of index i in the following batch.
      unroll: Boolean (default False).
        If True, the network will be unrolled,
        else a symbolic loop will be used.
        Unrolling can speed-up a RNN,
        although it tends to be more memory-intensive.
        Unrolling is only suitable for short sequences.
      time_major: The shape format of the `inputs` and `outputs` tensors.
        If True, the inputs and outputs will be in shape
        `[timesteps, batch, feature]`, whereas in the False case, it will be
        `[batch, timesteps, feature]`. Using `time_major = True` is a bit more
        efficient because it avoids transposes at the beginning and end of the
        RNN calculation. However, most TensorFlow data is batch-major, so by
        default this function accepts input and emits output in batch-major
        form.
      reset_after: GRU convention (whether to apply reset gate after or
        before matrix multiplication). False = "before",
        True = "after" (default and cuDNN compatible).

    Call arguments:
      inputs: A 3D tensor, with shape `[batch, timesteps, feature]`.
      mask: Binary tensor of shape `[samples, timesteps]` indicating whether
        a given timestep should be masked  (optional, defaults to `None`).
        An individual `True` entry indicates that the corresponding timestep
        should be utilized, while a `False` entry indicates that the
        corresponding timestep should be ignored.
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode. This argument is passed to the cell
        when calling it. This is only relevant if `dropout` or
        `recurrent_dropout` is used  (optional, defaults to `None`).
      initial_state: List of initial state tensors to be passed to the first
        call of the cell  (optional, defaults to `None` which causes creation
        of zero-filled initial state tensors).
    '''
    activity_regularizer: Incomplete
    input_spec: Incomplete
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, unroll: bool = False, time_major: bool = False, reset_after: bool = True, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, initial_state: Incomplete | None = None): ...
    @property
    def units(self): ...
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
    @property
    def implementation(self): ...
    @property
    def reset_after(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

def standard_gru(inputs, init_h, kernel, recurrent_kernel, bias, mask, time_major, go_backwards, sequence_lengths, zero_output_for_mask, return_sequences):
    """GRU with standard kernel implementation.

    This implementation can be run on all types of hardware.

    This implementation lifts out all the layer weights and make them function
    parameters. It has same number of tensor input params as the cuDNN
    counterpart. The RNN step logic has been simplified, eg dropout and mask is
    removed since cuDNN implementation does not support that.

    Args:
      inputs: Input tensor of GRU layer.
      init_h: Initial state tensor for the cell output.
      kernel: Weights for cell kernel.
      recurrent_kernel: Weights for cell recurrent kernel.
      bias: Weights for cell kernel bias and recurrent bias. The bias contains
        the combined input_bias and recurrent_bias.
      mask: Binary tensor of shape `(samples, timesteps)` indicating whether
        a given timestep should be masked. An individual `True` entry indicates
        that the corresponding timestep should be utilized, while a `False`
        entry indicates that the corresponding timestep should be ignored.
      time_major: Boolean, whether the inputs are in the format of
        [time, batch, feature] or [batch, time, feature].
      go_backwards: Boolean (default False). If True, process the input sequence
        backwards and return the reversed sequence.
      sequence_lengths: The lengths of all sequences coming from a variable
        length input, such as ragged tensors. If the input has a fixed timestep
        size, this should be None.
      zero_output_for_mask: Boolean, whether to output zero for masked timestep.
      return_sequences: Boolean. If True, return the recurrent outputs for all
        timesteps in the sequence. If False, only return the output for the
        last timestep (which consumes less memory).

    Returns:
      last_output: output tensor for the last timestep, which has shape
        [batch, units].
      outputs:
        - If `return_sequences=True`: output tensor for all timesteps,
          which has shape [batch, time, units].
        - Else, a tensor equal to `last_output` with shape [batch, 1, units]
      state_0: the cell output, which has same shape as init_h.
      runtime: constant string tensor which indicate real runtime hardware. This
        value is for testing purpose and should be used by user.
    """
def gpu_gru(inputs, init_h, kernel, recurrent_kernel, bias, mask, time_major, go_backwards, sequence_lengths, return_sequences):
    """GRU with cuDNN implementation which is only available for GPU."""
def gru_with_backend_selection(inputs, init_h, kernel, recurrent_kernel, bias, mask, time_major, go_backwards, sequence_lengths, zero_output_for_mask, return_sequences):
    """Call the GRU with optimized backend kernel selection.

    Under the hood, this function will create two TF function, one with the most
    generic kernel and can run on all device condition, and the second one with
    cuDNN specific kernel, which can only run on GPU.

    The first function will be called with normal_lstm_params, while the second
    function is not called, but only registered in the graph. The Grappler will
    do the proper graph rewrite and swap the optimized TF function based on the
    device placement.

    Args:
      inputs: Input tensor of GRU layer.
      init_h: Initial state tensor for the cell output.
      kernel: Weights for cell kernel.
      recurrent_kernel: Weights for cell recurrent kernel.
      bias: Weights for cell kernel bias and recurrent bias. Only recurrent bias
        is used in this case.
      mask: Boolean tensor for mask out the steps within sequence.
        An individual `True` entry indicates that the corresponding timestep
        should be utilized, while a `False` entry indicates that the
        corresponding timestep should be ignored.
      time_major: Boolean, whether the inputs are in the format of
        [time, batch, feature] or [batch, time, feature].
      go_backwards: Boolean (default False). If True, process the input sequence
        backwards and return the reversed sequence.
      sequence_lengths: The lengths of all sequences coming from a variable
        length input, such as ragged tensors. If the input has a fixed timestep
        size, this should be None.
      zero_output_for_mask: Boolean, whether to output zero for masked timestep.
      return_sequences: Boolean. If True, return the recurrent outputs for all
        timesteps in the sequence. If False, only return the output for the
        last timestep (which consumes less memory).

    Returns:
      List of output tensors, same as standard_gru.
    """
