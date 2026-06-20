from _typeshed import Incomplete
from keras import activations as activations, backend as backend, initializers as initializers
from keras.engine import base_layer_utils as base_layer_utils, input_spec as input_spec
from keras.legacy_tf_layers import base as base_layer
from keras.utils import tf_utils as tf_utils
from typing import NamedTuple

class RNNCell(base_layer.Layer):
    """Abstract object representing an RNN cell.

    Every `RNNCell` must have the properties below and implement `call` with
    the signature `(output, next_state) = call(input, state)`.  The optional
    third input argument, `scope`, is allowed for backwards compatibility
    purposes; but should be left off for new subclasses.

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
    def __init__(self, trainable: bool = True, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, inputs, state, scope: Incomplete | None = None):
        """Run this RNN cell on inputs, starting from the given state.

        Args:
          inputs: `2-D` tensor with shape `[batch_size, input_size]`.
          state: if `self.state_size` is an integer, this should be a
            `2-D Tensor` with shape `[batch_size, self.state_size]`. Otherwise,
            if `self.state_size` is a tuple of integers, this should be a tuple
            with shapes `[batch_size, s] for s in self.state_size`.
          scope: VariableScope for the created subgraph; defaults to class name.

        Returns:
          A pair containing:

          - Output: A `2-D` tensor with shape `[batch_size, self.output_size]`.
          - New state: Either a single `2-D` tensor, or a tuple of tensors
            matching the arity and shapes of `state`.
        """
    @property
    def state_size(self) -> None:
        """size(s) of state(s) used by this cell.

        It can be represented by an Integer, a TensorShape or a tuple of
        Integers or TensorShapes.
        """
    @property
    def output_size(self) -> None:
        """Integer or TensorShape: size of outputs produced by this cell."""
    def build(self, _) -> None: ...
    def get_initial_state(self, inputs: Incomplete | None = None, batch_size: Incomplete | None = None, dtype: Incomplete | None = None): ...
    def zero_state(self, batch_size, dtype):
        """Return zero-filled state tensor(s).

        Args:
          batch_size: int, float, or unit Tensor representing the batch size.
          dtype: the data type to use for the state.

        Returns:
          If `state_size` is an int or TensorShape, then the return value is a
          `N-D` tensor of shape `[batch_size, state_size]` filled with zeros.

          If `state_size` is a nested list or tuple, then the return value is
          a nested list or tuple (of the same structure) of `2-D` tensors with
          the shapes `[batch_size, s]` for each s in `state_size`.
        """
    def get_config(self): ...

class LayerRNNCell(RNNCell):
    """Subclass of RNNCells that act like proper `tf.Layer` objects.

    For backwards compatibility purposes, most `RNNCell` instances allow their
    `call` methods to instantiate variables via `tf.compat.v1.get_variable`.
    The underlying variable scope thus keeps track of any variables, and
    returning cached versions.  This is atypical of `tf.layer` objects, which
    separate this part of layer building into a `build` method that is only
    called once.

    Here we provide a subclass for `RNNCell` objects that act exactly as
    `Layer` objects do.  They must provide a `build` method and their
    `call` methods do not access Variables `tf.compat.v1.get_variable`.
    """
    def __call__(self, inputs, state, scope: Incomplete | None = None, *args, **kwargs):
        """Run this RNN cell on inputs, starting from the given state.

        Args:
          inputs: `2-D` tensor with shape `[batch_size, input_size]`.
          state: if `self.state_size` is an integer, this should be a `2-D
            Tensor` with shape `[batch_size, self.state_size]`.  Otherwise, if
            `self.state_size` is a tuple of integers, this should be a tuple
            with shapes `[batch_size, s] for s in self.state_size`.
          scope: optional cell scope.
          *args: Additional positional arguments.
          **kwargs: Additional keyword arguments.

        Returns:
          A pair containing:

          - Output: A `2-D` tensor with shape `[batch_size, self.output_size]`.
          - New state: Either a single `2-D` tensor, or a tuple of tensors
            matching the arity and shapes of `state`.
        """

class BasicRNNCell(LayerRNNCell):
    """The most basic RNN cell.

    Note that this cell is not optimized for performance.

    Args:
      num_units: int, The number of units in the RNN cell.
      activation: Nonlinearity to use.  Default: `tanh`. It could also be string
        that is within Keras activation function names.
      reuse: (optional) Python boolean describing whether to reuse variables in
        an existing scope. If not `True`, and the existing scope already has the
        given variables, an error is raised.
      name: String, the name of the layer. Layers with the same name will share
        weights, but to avoid mistakes we require reuse=True in such cases.
      dtype: Default dtype of the layer (default of `None` means use the type of
        the first input). Required when `build` is called before `call`.
      **kwargs: Dict, keyword named properties for common layer attributes, like
        `trainable` etc when constructing the cell from configs of get_config().
    """
    input_spec: Incomplete
    def __init__(self, num_units, activation: Incomplete | None = None, reuse: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state):
        """Most basic RNN: output = new_state = act(W * input + U * state +
        B)."""
    def get_config(self): ...

class GRUCell(LayerRNNCell):
    """Gated Recurrent Unit cell.

    Note that this cell is not optimized for performance. Please use
    `tf.compat.v1.keras.layers.CuDNNGRU` for better performance on GPU, or
    `tf.raw_ops.GRUBlockCell` for better performance on CPU.

    Args:
      num_units: int, The number of units in the GRU cell.
      activation: Nonlinearity to use.  Default: `tanh`.
      reuse: (optional) Python boolean describing whether to reuse variables in
        an existing scope. If not `True`, and the existing scope already has
        the given variables, an error is raised.
      kernel_initializer: (optional) The initializer to use for the weight and
        projection matrices.
      bias_initializer: (optional) The initializer to use for the bias.
      name: String, the name of the layer. Layers with the same name will share
        weights, but to avoid mistakes we require reuse=True in such cases.
      dtype: Default dtype of the layer (default of `None` means use the type of
        the first input). Required when `build` is called before `call`.
      **kwargs: Dict, keyword named properties for common layer attributes, like
        `trainable` etc when constructing the cell from configs of get_config().
        References: Learning Phrase Representations using RNN Encoder Decoder
        for Statistical Machine Translation: [Cho et al., 2014]
        (https://aclanthology.coli.uni-saarland.de/papers/D14-1179/d14-1179)
        ([pdf](http://emnlp2014.org/papers/pdf/EMNLP2014179.pdf))
    """
    input_spec: Incomplete
    def __init__(self, num_units, activation: Incomplete | None = None, reuse: Incomplete | None = None, kernel_initializer: Incomplete | None = None, bias_initializer: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state):
        """Gated recurrent unit (GRU) with nunits cells."""
    def get_config(self): ...

class _LSTMStateTuple(NamedTuple):
    c: Incomplete
    h: Incomplete

class LSTMStateTuple(_LSTMStateTuple):
    """Tuple used by LSTM Cells for `state_size`, `zero_state`, & output state.

    Stores two elements: `(c, h)`, in that order. Where `c` is the hidden state
    and `h` is the output.

    Only used when `state_is_tuple=True`.
    """
    @property
    def dtype(self): ...

class BasicLSTMCell(LayerRNNCell):
    """DEPRECATED: Please use `tf.compat.v1.nn.rnn_cell.LSTMCell` instead.

    Basic LSTM recurrent network cell.

    The implementation is based on

    We add forget_bias (default: 1) to the biases of the forget gate in order to
    reduce the scale of forgetting in the beginning of the training.

    It does not allow cell clipping, a projection layer, and does not
    use peep-hole connections: it is the basic baseline.

    For advanced models, please use the full `tf.compat.v1.nn.rnn_cell.LSTMCell`
    that follows.

    Note that this cell is not optimized for performance. Please use
    `tf.compat.v1.keras.layers.CuDNNLSTM` for better performance on GPU, or
    `tf.raw_ops.LSTMBlockCell` for better performance on CPU.
    """
    input_spec: Incomplete
    def __init__(self, num_units, forget_bias: float = 1.0, state_is_tuple: bool = True, activation: Incomplete | None = None, reuse: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None:
        """Initialize the basic LSTM cell.

        Args:
          num_units: int, The number of units in the LSTM cell.
          forget_bias: float, The bias added to forget gates (see above). Must
            set to `0.0` manually when restoring from CudnnLSTM-trained
            checkpoints.
          state_is_tuple: If True, accepted and returned states are 2-tuples of
            the `c_state` and `m_state`.  If False, they are concatenated along
            the column axis.  The latter behavior will soon be deprecated.
          activation: Activation function of the inner states.  Default: `tanh`.
            It could also be string that is within Keras activation function
            names.
          reuse: (optional) Python boolean describing whether to reuse variables
            in an existing scope.  If not `True`, and the existing scope already
            has the given variables, an error is raised.
          name: String, the name of the layer. Layers with the same name will
            share weights, but to avoid mistakes we require reuse=True in such
            cases.
          dtype: Default dtype of the layer (default of `None` means use the
            type of the first input). Required when `build` is called before
            `call`.
          **kwargs: Dict, keyword named properties for common layer attributes,
            like `trainable` etc when constructing the cell from configs of
            get_config().  When restoring from CudnnLSTM-trained checkpoints,
            must use `CudnnCompatibleLSTMCell` instead.
        """
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state):
        """Long short-term memory cell (LSTM).

        Args:
          inputs: `2-D` tensor with shape `[batch_size, input_size]`.
          state: An `LSTMStateTuple` of state tensors, each shaped `[batch_size,
            num_units]`, if `state_is_tuple` has been set to `True`.  Otherwise,
            a `Tensor` shaped `[batch_size, 2 * num_units]`.

        Returns:
          A pair containing the new hidden state, and the new state (either a
            `LSTMStateTuple` or a concatenated state, depending on
            `state_is_tuple`).
        """
    def get_config(self): ...

class LSTMCell(LayerRNNCell):
    """Long short-term memory unit (LSTM) recurrent network cell.

    The default non-peephole implementation is based on (Gers et al., 1999).
    The peephole implementation is based on (Sak et al., 2014).

    The class uses optional peep-hole connections, optional cell clipping, and
    an optional projection layer.

    Note that this cell is not optimized for performance. Please use
    `tf.compat.v1.keras.layers.CuDNNLSTM` for better performance on GPU, or
    `tf.raw_ops.LSTMBlockCell` for better performance on CPU.
    References:
      Long short-term memory recurrent neural network architectures for large
      scale acoustic modeling:
        [Sak et al., 2014]
        (https://www.isca-speech.org/archive/interspeech_2014/i14_0338.html)
        ([pdf]
        (https://www.isca-speech.org/archive/archive_papers/interspeech_2014/i14_0338.pdf))
      Learning to forget:
        [Gers et al., 1999]
        (http://digital-library.theiet.org/content/conferences/10.1049/cp_19991218)
        ([pdf](https://arxiv.org/pdf/1409.2329.pdf))
      Long Short-Term Memory:
        [Hochreiter et al., 1997]
        (https://www.mitpressjournals.org/doi/abs/10.1162/neco.1997.9.8.1735)
        ([pdf](http://ml.jku.at/publications/older/3504.pdf))
    """
    input_spec: Incomplete
    def __init__(self, num_units, use_peepholes: bool = False, cell_clip: Incomplete | None = None, initializer: Incomplete | None = None, num_proj: Incomplete | None = None, proj_clip: Incomplete | None = None, num_unit_shards: Incomplete | None = None, num_proj_shards: Incomplete | None = None, forget_bias: float = 1.0, state_is_tuple: bool = True, activation: Incomplete | None = None, reuse: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None:
        """Initialize the parameters for an LSTM cell.

        Args:
          num_units: int, The number of units in the LSTM cell.
          use_peepholes: bool, set True to enable diagonal/peephole connections.
          cell_clip: (optional) A float value, if provided the cell state is
            clipped by this value prior to the cell output activation.
          initializer: (optional) The initializer to use for the weight and
            projection matrices.
          num_proj: (optional) int, The output dimensionality for the projection
            matrices.  If None, no projection is performed.
          proj_clip: (optional) A float value.  If `num_proj > 0` and
            `proj_clip` is provided, then the projected values are clipped
            elementwise to within `[-proj_clip, proj_clip]`.
          num_unit_shards: Deprecated, will be removed by Jan. 2017. Use a
            variable_scope partitioner instead.
          num_proj_shards: Deprecated, will be removed by Jan. 2017. Use a
            variable_scope partitioner instead.
          forget_bias: Biases of the forget gate are initialized by default to 1
            in order to reduce the scale of forgetting at the beginning of the
            training. Must set it manually to `0.0` when restoring from
            CudnnLSTM trained checkpoints.
          state_is_tuple: If True, accepted and returned states are 2-tuples of
            the `c_state` and `m_state`.  If False, they are concatenated along
            the column axis.  This latter behavior will soon be deprecated.
          activation: Activation function of the inner states.  Default: `tanh`.
            It could also be string that is within Keras activation function
            names.
          reuse: (optional) Python boolean describing whether to reuse variables
            in an existing scope.  If not `True`, and the existing scope already
            has the given variables, an error is raised.
          name: String, the name of the layer. Layers with the same name will
            share weights, but to avoid mistakes we require reuse=True in such
            cases.
          dtype: Default dtype of the layer (default of `None` means use the
            type of the first input). Required when `build` is called before
            `call`.
          **kwargs: Dict, keyword named properties for common layer attributes,
            like `trainable` etc when constructing the cell from configs of
            get_config().  When restoring from CudnnLSTM-trained checkpoints,
            use `CudnnCompatibleLSTMCell` instead.
        """
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def call(self, inputs, state):
        """Run one step of LSTM.

        Args:
          inputs: input Tensor, must be 2-D, `[batch, input_size]`.
          state: if `state_is_tuple` is False, this must be a state Tensor,
            `2-D, [batch, state_size]`.  If `state_is_tuple` is True, this must
            be a tuple of state Tensors, both `2-D`, with column sizes `c_state`
            and `m_state`.

        Returns:
          A tuple containing:

          - A `2-D, [batch, output_dim]`, Tensor representing the output of the
            LSTM after reading `inputs` when previous state was `state`.
            Here output_dim is:
               num_proj if num_proj was set,
               num_units otherwise.
          - Tensor(s) representing the new state of LSTM after reading `inputs`
            when the previous state was `state`.  Same type and shape(s) as
            `state`.

        Raises:
          ValueError: If input size cannot be inferred from inputs via
            static shape inference.
        """
    def get_config(self): ...

class MultiRNNCell(RNNCell):
    """RNN cell composed sequentially of multiple simple cells.

    Example:

    ```python
    num_units = [128, 64]
    cells = [BasicLSTMCell(num_units=n) for n in num_units]
    stacked_rnn_cell = MultiRNNCell(cells)
    ```
    """
    def __init__(self, cells, state_is_tuple: bool = True) -> None:
        """Create a RNN cell composed sequentially of a number of RNNCells.

        Args:
          cells: list of RNNCells that will be composed in this order.
          state_is_tuple: If True, accepted and returned states are n-tuples,
            where `n = len(cells)`.  If False, the states are all concatenated
            along the column axis.  This latter behavior will soon be
            deprecated.

        Raises:
          ValueError: if cells is empty (not allowed), or at least one of the
            cells returns a state tuple but the flag `state_is_tuple` is
            `False`.
        """
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size, dtype): ...
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    def call(self, inputs, state):
        """Run this multi-layer cell on inputs, starting from state."""
