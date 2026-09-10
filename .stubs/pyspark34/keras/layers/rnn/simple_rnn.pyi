from _typeshed import Incomplete
from keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from keras.engine import base_layer as base_layer
from keras.engine.input_spec import InputSpec as InputSpec
from keras.layers.rnn import rnn_utils as rnn_utils
from keras.layers.rnn.base_rnn import RNN as RNN
from keras.layers.rnn.dropout_rnn_cell_mixin import DropoutRNNCellMixin as DropoutRNNCellMixin
from keras.utils import tf_utils as tf_utils

class SimpleRNNCell(DropoutRNNCellMixin, base_layer.BaseRandomLayer):
    '''Cell class for SimpleRNN.

    See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
    for details about the usage of RNN API.

    This class processes one step within the whole time sequence input, whereas
    `tf.keras.layer.SimpleRNN` processes the whole sequence.

    Args:
      units: Positive integer, dimensionality of the output space.
      activation: Activation function to use.
        Default: hyperbolic tangent (`tanh`).
        If you pass `None`, no activation is applied
        (ie. "linear" activation: `a(x) = x`).
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

    Call arguments:
      inputs: A 2D tensor, with shape of `[batch, feature]`.
      states: A 2D tensor with shape of `[batch, units]`, which is the state
        from the previous time step. For timestep 0, the initial state provided
        by user will be feed to cell.
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode. Only relevant when `dropout` or
        `recurrent_dropout` is used.

    Examples:

    ```python
    inputs = np.random.random([32, 10, 8]).astype(np.float32)
    rnn = tf.keras.layers.RNN(tf.keras.layers.SimpleRNNCell(4))

    output = rnn(inputs)  # The output has shape `[32, 4]`.

    rnn = tf.keras.layers.RNN(
        tf.keras.layers.SimpleRNNCell(4),
        return_sequences=True,
        return_state=True)

    # whole_sequence_output has shape `[32, 10, 4]`.
    # final_state has shape `[32, 4]`.
    whole_sequence_output, final_state = rnn(inputs)
    ```
    '''
    units: Incomplete
    activation: Incomplete
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
    state_size: Incomplete
    output_size: Incomplete
    def __init__(self, units, activation: str = 'tanh', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs, states, training: Incomplete | None = None): ...
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...
    def get_config(self): ...

class SimpleRNN(RNN):
    '''Fully-connected RNN where the output is to be fed back to input.

    See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
    for details about the usage of RNN API.

    Args:
      units: Positive integer, dimensionality of the output space.
      activation: Activation function to use.
        Default: hyperbolic tangent (`tanh`).
        If you pass None, no activation is applied
        (ie. "linear" activation: `a(x) = x`).
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
      activity_regularizer: Regularizer function applied to the output of the
        layer (its "activation"). Default: `None`.
      kernel_constraint: Constraint function applied to the `kernel` weights
        matrix. Default: `None`.
      recurrent_constraint: Constraint function applied to the
        `recurrent_kernel` weights matrix.  Default: `None`.
      bias_constraint: Constraint function applied to the bias vector. Default:
        `None`.
      dropout: Float between 0 and 1.
        Fraction of the units to drop for the linear transformation of the
        inputs. Default: 0.
      recurrent_dropout: Float between 0 and 1.
        Fraction of the units to drop for the linear transformation of the
        recurrent state. Default: 0.
      return_sequences: Boolean. Whether to return the last output
        in the output sequence, or the full sequence. Default: `False`.
      return_state: Boolean. Whether to return the last state
        in addition to the output. Default: `False`
      go_backwards: Boolean (default False).
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

    Call arguments:
      inputs: A 3D tensor, with shape `[batch, timesteps, feature]`.
      mask: Binary tensor of shape `[batch, timesteps]` indicating whether
        a given timestep should be masked. An individual `True` entry indicates
        that the corresponding timestep should be utilized, while a `False`
        entry indicates that the corresponding timestep should be ignored.
      training: Python boolean indicating whether the layer should behave in
        training mode or in inference mode. This argument is passed to the cell
        when calling it. This is only relevant if `dropout` or
        `recurrent_dropout` is used.
      initial_state: List of initial state tensors to be passed to the first
        call of the cell.

    Examples:

    ```python
    inputs = np.random.random([32, 10, 8]).astype(np.float32)
    simple_rnn = tf.keras.layers.SimpleRNN(4)

    output = simple_rnn(inputs)  # The output has shape `[32, 4]`.

    simple_rnn = tf.keras.layers.SimpleRNN(
        4, return_sequences=True, return_state=True)

    # whole_sequence_output has shape `[32, 10, 4]`.
    # final_state has shape `[32, 4]`.
    whole_sequence_output, final_state = simple_rnn(inputs)
    ```
    '''
    activity_regularizer: Incomplete
    input_spec: Incomplete
    def __init__(self, units, activation: str = 'tanh', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, unroll: bool = False, **kwargs) -> None: ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, initial_state: Incomplete | None = None): ...
    @property
    def units(self): ...
    @property
    def activation(self): ...
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
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
