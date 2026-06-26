from _typeshed import Incomplete
from tensorflow.python.eager import context as context
from tensorflow.python.framework import ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, backend as backend, constraints as constraints, initializers as initializers, regularizers as regularizers
from tensorflow.python.keras.engine.base_layer import Layer as Layer
from tensorflow.python.keras.engine.input_spec import InputSpec as InputSpec
from tensorflow.python.keras.saving.saved_model import layer_serialization as layer_serialization
from tensorflow.python.keras.utils import control_flow_util as control_flow_util, generic_utils as generic_utils, tf_utils as tf_utils
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops, state_ops as state_ops
from tensorflow.python.util import nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from tensorflow.tools.docs import doc_controls as doc_controls

RECURRENT_DROPOUT_WARNING_MSG: str

class StackedRNNCells(Layer):
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
    def build(self, input_shape) -> None: ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class RNN(Layer):
    '''Base class for recurrent layers.

  See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
  for details about the usage of RNN API.

  Args:
    cell: A RNN cell instance or a list of RNN cell instances.
      A RNN cell is a class that has:
      - A `call(input_at_t, states_at_t)` method, returning
        `(output_at_t, states_at_t_plus_1)`. The call method of the
        cell can also take the optional argument `constants`, see
        section "Note on passing external constants" below.
      - A `state_size` attribute. This can be a single integer
        (single state) in which case it is the size of the recurrent
        state. This can also be a list/tuple of integers (one size per state).
        The `state_size` can also be TensorShape or tuple/list of
        TensorShape, to represent high dimension state.
      - A `output_size` attribute. This can be a single integer or a
        TensorShape, which represent the shape of the output. For backward
        compatible reason, if this attribute is not available for the
        cell, the value will be inferred by the first element of the
        `state_size`.
      - A `get_initial_state(inputs=None, batch_size=None, dtype=None)`
        method that creates a tensor meant to be fed to `call()` as the
        initial state, if the user didn\'t specify any initial state via other
        means. The returned initial state should have a shape of
        [batch_size, cell.state_size]. The cell might choose to create a
        tensor full of zeros, or full of other values based on the cell\'s
        implementation.
        `inputs` is the input tensor to the RNN layer, which should
        contain the batch size as its shape[0], and also dtype. Note that
        the shape[0] might be `None` during the graph construction. Either
        the `inputs` or the pair of `batch_size` and `dtype` are provided.
        `batch_size` is a scalar tensor that represents the batch size
        of the inputs. `dtype` is `tf.DType` that represents the dtype of
        the inputs.
        For backward compatibility, if this method is not implemented
        by the cell, the RNN layer will create a zero filled tensor with the
        size of [batch_size, cell.state_size].
      In the case that `cell` is a list of RNN cell instances, the cells
      will be stacked on top of each other in the RNN, resulting in an
      efficient stacked RNN.
    return_sequences: Boolean (default `False`). Whether to return the last
      output in the output sequence, or the full sequence.
    return_state: Boolean (default `False`). Whether to return the last state
      in addition to the output.
    go_backwards: Boolean (default `False`).
      If True, process the input sequence backwards and return the
      reversed sequence.
    stateful: Boolean (default `False`). If True, the last state
      for each sample at index i in a batch will be used as initial
      state for the sample of index i in the following batch.
    unroll: Boolean (default `False`).
      If True, the network will be unrolled, else a symbolic loop will be used.
      Unrolling can speed-up a RNN, although it tends to be more
      memory-intensive. Unrolling is only suitable for short sequences.
    time_major: The shape format of the `inputs` and `outputs` tensors.
      If True, the inputs and outputs will be in shape
      `(timesteps, batch, ...)`, whereas in the False case, it will be
      `(batch, timesteps, ...)`. Using `time_major = True` is a bit more
      efficient because it avoids transposes at the beginning and end of the
      RNN calculation. However, most TensorFlow data is batch-major, so by
      default this function accepts input and emits output in batch-major
      form.
    zero_output_for_mask: Boolean (default `False`).
      Whether the output should use zeros for the masked timesteps. Note that
      this field is only used when `return_sequences` is True and mask is
      provided. It can useful if you want to reuse the raw output sequence of
      the RNN without interference from the masked timesteps, eg, merging
      bidirectional RNNs.

  Call arguments:
    inputs: Input tensor.
    mask: Binary tensor of shape `[batch_size, timesteps]` indicating whether
      a given timestep should be masked. An individual `True` entry indicates
      that the corresponding timestep should be utilized, while a `False`
      entry indicates that the corresponding timestep should be ignored.
    training: Python boolean indicating whether the layer should behave in
      training mode or in inference mode. This argument is passed to the cell
      when calling it. This is for use with cells that use dropout.
    initial_state: List of initial state tensors to be passed to the first
      call of the cell.
    constants: List of constant tensors to be passed to the cell at each
      timestep.

  Input shape:
    N-D tensor with shape `[batch_size, timesteps, ...]` or
    `[timesteps, batch_size, ...]` when time_major is True.

  Output shape:
    - If `return_state`: a list of tensors. The first tensor is
      the output. The remaining tensors are the last states,
      each with shape `[batch_size, state_size]`, where `state_size` could
      be a high dimension tensor shape.
    - If `return_sequences`: N-D tensor with shape
      `[batch_size, timesteps, output_size]`, where `output_size` could
      be a high dimension tensor shape, or
      `[timesteps, batch_size, output_size]` when `time_major` is True.
    - Else, N-D tensor with shape `[batch_size, output_size]`, where
      `output_size` could be a high dimension tensor shape.

  Masking:
    This layer supports masking for input data with a variable number
    of timesteps. To introduce masks to your data,
    use an [tf.keras.layers.Embedding] layer with the `mask_zero` parameter
    set to `True`.

  Note on using statefulness in RNNs:
    You can set RNN layers to be \'stateful\', which means that the states
    computed for the samples in one batch will be reused as initial states
    for the samples in the next batch. This assumes a one-to-one mapping
    between samples in different successive batches.

    To enable statefulness:
      - Specify `stateful=True` in the layer constructor.
      - Specify a fixed batch size for your model, by passing
        If sequential model:
          `batch_input_shape=(...)` to the first layer in your model.
        Else for functional model with 1 or more Input layers:
          `batch_shape=(...)` to all the first layers in your model.
        This is the expected shape of your inputs
        *including the batch size*.
        It should be a tuple of integers, e.g. `(32, 10, 100)`.
      - Specify `shuffle=False` when calling `fit()`.

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

  Examples:

  ```python
  # First, let\'s define a RNN Cell, as a layer subclass.

  class MinimalRNNCell(keras.layers.Layer):

      def __init__(self, units, **kwargs):
          self.units = units
          self.state_size = units
          super(MinimalRNNCell, self).__init__(**kwargs)

      def build(self, input_shape):
          self.kernel = self.add_weight(shape=(input_shape[-1], self.units),
                                        initializer=\'uniform\',
                                        name=\'kernel\')
          self.recurrent_kernel = self.add_weight(
              shape=(self.units, self.units),
              initializer=\'uniform\',
              name=\'recurrent_kernel\')
          self.built = True

      def call(self, inputs, states):
          prev_output = states[0]
          h = backend.dot(inputs, self.kernel)
          output = h + backend.dot(prev_output, self.recurrent_kernel)
          return output, [output]

  # Let\'s use this cell in a RNN layer:

  cell = MinimalRNNCell(32)
  x = keras.Input((None, 5))
  layer = RNN(cell)
  y = layer(x)

  # Here\'s how to use the cell to build a stacked RNN:

  cells = [MinimalRNNCell(32), MinimalRNNCell(64)]
  x = keras.Input((None, 5))
  layer = RNN(cells)
  y = layer(x)
  ```
  '''
    zero_output_for_mask: Incomplete
    cell: Incomplete
    return_sequences: Incomplete
    return_state: Incomplete
    go_backwards: Incomplete
    stateful: Incomplete
    unroll: Incomplete
    time_major: Incomplete
    supports_masking: bool
    input_spec: Incomplete
    state_spec: Incomplete
    constants_spec: Incomplete
    def __init__(self, cell, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, unroll: bool = False, time_major: bool = False, **kwargs) -> None: ...
    @property
    def states(self): ...
    @states.setter
    def states(self, states) -> None: ...
    def compute_output_shape(self, input_shape): ...
    def compute_mask(self, inputs, mask): ...
    built: bool
    def build(self, input_shape): ...
    def get_initial_state(self, inputs): ...
    def __call__(self, inputs, initial_state: Incomplete | None = None, constants: Incomplete | None = None, **kwargs): ...
    def call(self, inputs, mask: Incomplete | None = None, training: Incomplete | None = None, initial_state: Incomplete | None = None, constants: Incomplete | None = None): ...
    def reset_states(self, states: Incomplete | None = None) -> None:
        """Reset the recorded states for the stateful RNN layer.

    Can only be used when RNN layer is constructed with `stateful` = `True`.
    Args:
      states: Numpy arrays that contains the value for the initial state, which
        will be feed to cell at the first time step. When the value is None,
        zero filled numpy array will be created based on the cell state size.

    Raises:
      AttributeError: When the RNN layer is not stateful.
      ValueError: When the batch size of the RNN layer is unknown.
      ValueError: When the input numpy array is not compatible with the RNN
        layer state, either size wise or dtype wise.
    """
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class AbstractRNNCell(Layer):
    """Abstract object representing an RNN cell.

  See [the Keras RNN API guide](https://www.tensorflow.org/guide/keras/rnn)
  for details about the usage of RNN API.

  This is the base class for implementing RNN cells with custom behavior.

  Every `RNNCell` must have the properties below and implement `call` with
  the signature `(output, next_state) = call(input, state)`.

  Examples:

  ```python
    class MinimalRNNCell(AbstractRNNCell):

      def __init__(self, units, **kwargs):
        self.units = units
        super(MinimalRNNCell, self).__init__(**kwargs)

      @property
      def state_size(self):
        return self.units

      def build(self, input_shape):
        self.kernel = self.add_weight(shape=(input_shape[-1], self.units),
                                      initializer='uniform',
                                      name='kernel')
        self.recurrent_kernel = self.add_weight(
            shape=(self.units, self.units),
            initializer='uniform',
            name='recurrent_kernel')
        self.built = True

      def call(self, inputs, states):
        prev_output = states[0]
        h = backend.dot(inputs, self.kernel)
        output = h + backend.dot(prev_output, self.recurrent_kernel)
        return output, output
  ```

  This definition of cell differs from the definition used in the literature.
  In the literature, 'cell' refers to an object with a single scalar output.
  This definition refers to a horizontal array of such units.

  An RNN cell, in the most abstract setting, is anything that has
  a state and performs some operation that takes a matrix of inputs.
  This operation results in an output matrix with `self.output_size` columns.
  If `self.state_size` is an integer, this operation also results in a new
  state matrix with `self.state_size` columns.  If `self.state_size` is a
  (possibly nested tuple of) TensorShape object(s), then it should return a
  matching structure of Tensors having shape `[batch_size].concatenate(s)`
  for each `s` in `self.batch_size`.
  """
    def call(self, inputs, states) -> None:
        """The function that contains the logic for one RNN step calculation.

    Args:
      inputs: the input tensor, which is a slide from the overall RNN input by
        the time dimension (usually the second dimension).
      states: the state tensor from previous step, which has the same shape
        as `(batch, state_size)`. In the case of timestep 0, it will be the
        initial state user specified, or zero filled tensor otherwise.

    Returns:
      A tuple of two tensors:
        1. output tensor for the current timestep, with size `output_size`.
        2. state tensor for next step, which has the shape of `state_size`.
    """
    @property
    def state_size(self) -> None:
        """size(s) of state(s) used by this cell.

    It can be represented by an Integer, a TensorShape or a tuple of Integers
    or TensorShapes.
    """
    @property
    def output_size(self) -> None:
        """Integer or TensorShape: size of outputs produced by this cell."""
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...

class DropoutRNNCellMixin:
    """Object that hold dropout related fields for RNN Cell.

  This class is not a standalone RNN cell. It suppose to be used with a RNN cell
  by multiple inheritance. Any cell that mix with class should have following
  fields:
    dropout: a float number within range [0, 1). The ratio that the input
      tensor need to dropout.
    recurrent_dropout: a float number within range [0, 1). The ratio that the
      recurrent state weights need to dropout.
  This object will create and cache created dropout masks, and reuse them for
  the incoming data, so that the same mask is used for every batch input.
  """
    def __init__(self, *args, **kwargs) -> None: ...
    def reset_dropout_mask(self) -> None:
        """Reset the cached dropout masks if any.

    This is important for the RNN layer to invoke this in it `call()` method so
    that the cached mask is cleared before calling the `cell.call()`. The mask
    should be cached across the timestep within the same batch, but shouldn't
    be cached between batches. Otherwise it will introduce unreasonable bias
    against certain index of data within the batch.
    """
    def reset_recurrent_dropout_mask(self) -> None:
        """Reset the cached recurrent dropout masks if any.

    This is important for the RNN layer to invoke this in it call() method so
    that the cached mask is cleared before calling the cell.call(). The mask
    should be cached across the timestep within the same batch, but shouldn't
    be cached between batches. Otherwise it will introduce unreasonable bias
    against certain index of data within the batch.
    """
    def get_dropout_mask_for_cell(self, inputs, training, count: int = 1):
        """Get the dropout mask for RNN cell's input.

    It will create mask based on context if there isn't any existing cached
    mask. If a new mask is generated, it will update the cache in the cell.

    Args:
      inputs: The input tensor whose shape will be used to generate dropout
        mask.
      training: Boolean tensor, whether its in training mode, dropout will be
        ignored in non-training mode.
      count: Int, how many dropout mask will be generated. It is useful for cell
        that has internal weights fused together.
    Returns:
      List of mask tensor, generated or cached mask based on context.
    """
    def get_recurrent_dropout_mask_for_cell(self, inputs, training, count: int = 1):
        """Get the recurrent dropout mask for RNN cell.

    It will create mask based on context if there isn't any existing cached
    mask. If a new mask is generated, it will update the cache in the cell.

    Args:
      inputs: The input tensor whose shape will be used to generate dropout
        mask.
      training: Boolean tensor, whether its in training mode, dropout will be
        ignored in non-training mode.
      count: Int, how many dropout mask will be generated. It is useful for cell
        that has internal weights fused together.
    Returns:
      List of mask tensor, generated or cached mask based on context.
    """

class SimpleRNNCell(DropoutRNNCellMixin, Layer):
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
      weights matrix, used for the linear transformation of the recurrent state.
      Default: `orthogonal`.
    bias_initializer: Initializer for the bias vector. Default: `zeros`.
    kernel_regularizer: Regularizer function applied to the `kernel` weights
      matrix. Default: `None`.
    recurrent_regularizer: Regularizer function applied to the
      `recurrent_kernel` weights matrix. Default: `None`.
    bias_regularizer: Regularizer function applied to the bias vector. Default:
      `None`.
    kernel_constraint: Constraint function applied to the `kernel` weights
      matrix. Default: `None`.
    recurrent_constraint: Constraint function applied to the `recurrent_kernel`
      weights matrix. Default: `None`.
    bias_constraint: Constraint function applied to the bias vector. Default:
      `None`.
    dropout: Float between 0 and 1. Fraction of the units to drop for the linear
      transformation of the inputs. Default: 0.
    recurrent_dropout: Float between 0 and 1. Fraction of the units to drop for
      the linear transformation of the recurrent state. Default: 0.

  Call arguments:
    inputs: A 2D tensor, with shape of `[batch, feature]`.
    states: A 2D tensor with shape of `[batch, units]`, which is the state from
      the previous time step. For timestep 0, the initial state provided by user
      will be feed to cell.
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
      weights matrix, used for the linear transformation of the recurrent state.
      Default: `orthogonal`.
    bias_initializer: Initializer for the bias vector. Default: `zeros`.
    kernel_regularizer: Regularizer function applied to the `kernel` weights
      matrix. Default: `None`.
    recurrent_regularizer: Regularizer function applied to the
      `recurrent_kernel` weights matrix. Default: `None`.
    bias_regularizer: Regularizer function applied to the bias vector. Default:
      `None`.
    activity_regularizer: Regularizer function applied to the output of the
      layer (its "activation"). Default: `None`.
    kernel_constraint: Constraint function applied to the `kernel` weights
      matrix. Default: `None`.
    recurrent_constraint: Constraint function applied to the `recurrent_kernel`
      weights matrix.  Default: `None`.
    bias_constraint: Constraint function applied to the bias vector. Default:
      `None`.
    dropout: Float between 0 and 1.
      Fraction of the units to drop for the linear transformation of the inputs.
      Default: 0.
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
      that the corresponding timestep should be utilized, while a `False` entry
      indicates that the corresponding timestep should be ignored.
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

class GRUCell(DropoutRNNCellMixin, Layer):
    '''Cell class for the GRU layer.

  Args:
    units: Positive integer, dimensionality of the output space.
    activation: Activation function to use.
      Default: hyperbolic tangent (`tanh`).
      If you pass None, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    recurrent_activation: Activation function to use
      for the recurrent step.
      Default: hard sigmoid (`hard_sigmoid`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix,
      used for the linear transformation of the inputs.
    recurrent_initializer: Initializer for the `recurrent_kernel`
      weights matrix,
      used for the linear transformation of the recurrent state.
    bias_initializer: Initializer for the bias vector.
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
      Fraction of the units to drop for the linear transformation of the inputs.
    recurrent_dropout: Float between 0 and 1.
      Fraction of the units to drop for
      the linear transformation of the recurrent state.
    reset_after: GRU convention (whether to apply reset gate after or
      before matrix multiplication). False = "before" (default),
      True = "after" (CuDNN compatible).

  Call arguments:
    inputs: A 2D tensor.
    states: List of state tensors corresponding to the previous timestep.
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
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, reset_after: bool = False, **kwargs) -> None: ...
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape) -> None: ...
    def call(self, inputs, states, training: Incomplete | None = None): ...
    def get_config(self): ...
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...

class GRU(RNN):
    '''Gated Recurrent Unit - Cho et al. 2014.

  There are two variants. The default one is based on 1406.1078v3 and
  has reset gate applied to hidden state before matrix multiplication. The
  other one is based on original 1406.1078v1 and has the order reversed.

  The second variant is compatible with CuDNNGRU (GPU-only) and allows
  inference on CPU. Thus it has separate biases for `kernel` and
  `recurrent_kernel`. Use `\'reset_after\'=True` and
  `recurrent_activation=\'sigmoid\'`.

  Args:
    units: Positive integer, dimensionality of the output space.
    activation: Activation function to use.
      Default: hyperbolic tangent (`tanh`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    recurrent_activation: Activation function to use
      for the recurrent step.
      Default: hard sigmoid (`hard_sigmoid`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix,
      used for the linear transformation of the inputs.
    recurrent_initializer: Initializer for the `recurrent_kernel`
      weights matrix, used for the linear transformation of the recurrent state.
    bias_initializer: Initializer for the bias vector.
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix.
    recurrent_regularizer: Regularizer function applied to
      the `recurrent_kernel` weights matrix.
    bias_regularizer: Regularizer function applied to the bias vector.
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation")..
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
    unroll: Boolean (default False).
      If True, the network will be unrolled,
      else a symbolic loop will be used.
      Unrolling can speed-up a RNN,
      although it tends to be more memory-intensive.
      Unrolling is only suitable for short sequences.
    time_major: The shape format of the `inputs` and `outputs` tensors.
      If True, the inputs and outputs will be in shape
      `(timesteps, batch, ...)`, whereas in the False case, it will be
      `(batch, timesteps, ...)`. Using `time_major = True` is a bit more
      efficient because it avoids transposes at the beginning and end of the
      RNN calculation. However, most TensorFlow data is batch-major, so by
      default this function accepts input and emits output in batch-major
      form.
    reset_after: GRU convention (whether to apply reset gate after or
      before matrix multiplication). False = "before" (default),
      True = "after" (CuDNN compatible).

  Call arguments:
    inputs: A 3D tensor.
    mask: Binary tensor of shape `(samples, timesteps)` indicating whether
      a given timestep should be masked. An individual `True` entry indicates
      that the corresponding timestep should be utilized, while a `False`
      entry indicates that the corresponding timestep should be ignored.
    training: Python boolean indicating whether the layer should behave in
      training mode or in inference mode. This argument is passed to the cell
      when calling it. This is only relevant if `dropout` or
      `recurrent_dropout` is used.
    initial_state: List of initial state tensors to be passed to the first
      call of the cell.
  '''
    activity_regularizer: Incomplete
    input_spec: Incomplete
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, unroll: bool = False, reset_after: bool = False, **kwargs) -> None: ...
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

class LSTMCell(DropoutRNNCellMixin, Layer):
    '''Cell class for the LSTM layer.

  Args:
    units: Positive integer, dimensionality of the output space.
    activation: Activation function to use.
      Default: hyperbolic tangent (`tanh`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    recurrent_activation: Activation function to use
      for the recurrent step.
      Default: hard sigmoid (`hard_sigmoid`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix,
      used for the linear transformation of the inputs.
    recurrent_initializer: Initializer for the `recurrent_kernel`
      weights matrix,
      used for the linear transformation of the recurrent state.
    bias_initializer: Initializer for the bias vector.
    unit_forget_bias: Boolean.
      If True, add 1 to the bias of the forget gate at initialization.
      Setting it to true will also force `bias_initializer="zeros"`.
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
    inputs: A 2D tensor.
    states: List of state tensors corresponding to the previous timestep.
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
    unit_forget_bias: Incomplete
    kernel_regularizer: Incomplete
    recurrent_regularizer: Incomplete
    bias_regularizer: Incomplete
    kernel_constraint: Incomplete
    recurrent_constraint: Incomplete
    bias_constraint: Incomplete
    dropout: Incomplete
    recurrent_dropout: Incomplete
    implementation: int
    state_size: Incomplete
    output_size: Incomplete
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
    kernel: Incomplete
    recurrent_kernel: Incomplete
    bias: Incomplete
    built: bool
    def build(self, input_shape): ...
    def call(self, inputs, states, training: Incomplete | None = None): ...
    def get_config(self): ...
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...

class PeepholeLSTMCell(LSTMCell):
    '''Equivalent to LSTMCell class but adds peephole connections.

  Peephole connections allow the gates to utilize the previous internal state as
  well as the previous hidden state (which is what LSTMCell is limited to).
  This allows PeepholeLSTMCell to better learn precise timings over LSTMCell.

  From [Gers et al., 2002](
    http://www.jmlr.org/papers/volume3/gers02a/gers02a.pdf):

  "We find that LSTM augmented by \'peephole connections\' from its internal
  cells to its multiplicative gates can learn the fine distinction between
  sequences of spikes spaced either 50 or 49 time steps apart without the help
  of any short training exemplars."

  The peephole implementation is based on:

  [Sak et al., 2014](https://research.google.com/pubs/archive/43905.pdf)

  Example:

  ```python
  # Create 2 PeepholeLSTMCells
  peephole_lstm_cells = [PeepholeLSTMCell(size) for size in [128, 256]]
  # Create a layer composed sequentially of the peephole LSTM cells.
  layer = RNN(peephole_lstm_cells)
  input = keras.Input((timesteps, input_dim))
  output = layer(input)
  ```
  '''
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, **kwargs) -> None: ...
    input_gate_peephole_weights: Incomplete
    forget_gate_peephole_weights: Incomplete
    output_gate_peephole_weights: Incomplete
    def build(self, input_shape) -> None: ...

class LSTM(RNN):
    '''Long Short-Term Memory layer - Hochreiter 1997.

   Note that this cell is not optimized for performance on GPU. Please use
  `tf.compat.v1.keras.layers.CuDNNLSTM` for better performance on GPU.

  Args:
    units: Positive integer, dimensionality of the output space.
    activation: Activation function to use.
      Default: hyperbolic tangent (`tanh`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    recurrent_activation: Activation function to use
      for the recurrent step.
      Default: hard sigmoid (`hard_sigmoid`).
      If you pass `None`, no activation is applied
      (ie. "linear" activation: `a(x) = x`).
    use_bias: Boolean, whether the layer uses a bias vector.
    kernel_initializer: Initializer for the `kernel` weights matrix,
      used for the linear transformation of the inputs..
    recurrent_initializer: Initializer for the `recurrent_kernel`
      weights matrix,
      used for the linear transformation of the recurrent state.
    bias_initializer: Initializer for the bias vector.
    unit_forget_bias: Boolean.
      If True, add 1 to the bias of the forget gate at initialization.
      Setting it to true will also force `bias_initializer="zeros"`.
      This is recommended in [Jozefowicz et al., 2015](
        http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf).
    kernel_regularizer: Regularizer function applied to
      the `kernel` weights matrix.
    recurrent_regularizer: Regularizer function applied to
      the `recurrent_kernel` weights matrix.
    bias_regularizer: Regularizer function applied to the bias vector.
    activity_regularizer: Regularizer function applied to
      the output of the layer (its "activation").
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
    unroll: Boolean (default False).
      If True, the network will be unrolled,
      else a symbolic loop will be used.
      Unrolling can speed-up a RNN,
      although it tends to be more memory-intensive.
      Unrolling is only suitable for short sequences.
    time_major: The shape format of the `inputs` and `outputs` tensors.
      If True, the inputs and outputs will be in shape
      `(timesteps, batch, ...)`, whereas in the False case, it will be
      `(batch, timesteps, ...)`. Using `time_major = True` is a bit more
      efficient because it avoids transposes at the beginning and end of the
      RNN calculation. However, most TensorFlow data is batch-major, so by
      default this function accepts input and emits output in batch-major
      form.

  Call arguments:
    inputs: A 3D tensor.
    mask: Binary tensor of shape `(samples, timesteps)` indicating whether
      a given timestep should be masked. An individual `True` entry indicates
      that the corresponding timestep should be utilized, while a `False`
      entry indicates that the corresponding timestep should be ignored.
    training: Python boolean indicating whether the layer should behave in
      training mode or in inference mode. This argument is passed to the cell
      when calling it. This is only relevant if `dropout` or
      `recurrent_dropout` is used.
    initial_state: List of initial state tensors to be passed to the first
      call of the cell.
  '''
    activity_regularizer: Incomplete
    input_spec: Incomplete
    def __init__(self, units, activation: str = 'tanh', recurrent_activation: str = 'hard_sigmoid', use_bias: bool = True, kernel_initializer: str = 'glorot_uniform', recurrent_initializer: str = 'orthogonal', bias_initializer: str = 'zeros', unit_forget_bias: bool = True, kernel_regularizer: Incomplete | None = None, recurrent_regularizer: Incomplete | None = None, bias_regularizer: Incomplete | None = None, activity_regularizer: Incomplete | None = None, kernel_constraint: Incomplete | None = None, recurrent_constraint: Incomplete | None = None, bias_constraint: Incomplete | None = None, dropout: float = 0.0, recurrent_dropout: float = 0.0, return_sequences: bool = False, return_state: bool = False, go_backwards: bool = False, stateful: bool = False, unroll: bool = False, **kwargs) -> None: ...
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
    @property
    def implementation(self): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...
