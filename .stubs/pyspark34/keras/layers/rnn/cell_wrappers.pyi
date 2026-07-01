from _typeshed import Incomplete
from keras.layers.rnn import lstm as lstm
from keras.layers.rnn.abstract_rnn_cell import AbstractRNNCell as AbstractRNNCell
from keras.saving import serialization_lib as serialization_lib
from keras.utils import generic_utils as generic_utils, tf_inspect as tf_inspect

class _RNNCellWrapper(AbstractRNNCell):
    """Base class for cells wrappers V2 compatibility.

    This class along with `rnn_cell_impl._RNNCellWrapperV1` allows to define
    wrappers that are compatible with V1 and V2, and defines helper methods for
    this purpose.
    """
    cell: Incomplete
    def __init__(self, cell, *args, **kwargs) -> None: ...
    def call(self, inputs, state, **kwargs):
        """Runs the RNN cell step computation.

        When `call` is being used, we assume that the wrapper object has been
        built, and therefore the wrapped cells has been built via its `build`
        method and its `call` method can be used directly.

        This allows to use the wrapped cell and the non-wrapped cell
        equivalently when using `call` and `build`.

        Args:
          inputs: A tensor with wrapped cell's input.
          state: A tensor or tuple of tensors with wrapped cell's state.
          **kwargs: Additional arguments passed to the wrapped cell's `call`.

        Returns:
          A pair containing:

          - Output: A tensor with cell's output.
          - New state: A tensor or tuple of tensors with new wrapped cell's
            state.
        """
    built: bool
    def build(self, inputs_shape) -> None:
        """Builds the wrapped cell."""
    @property
    def wrapped_cell(self): ...
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class DropoutWrapper(_RNNCellWrapper):
    """Operator adding dropout to inputs and outputs of the given cell."""
    def __init__(self, cell, input_keep_prob: float = 1.0, output_keep_prob: float = 1.0, state_keep_prob: float = 1.0, variational_recurrent: bool = False, input_size: Incomplete | None = None, dtype: Incomplete | None = None, seed: Incomplete | None = None, dropout_state_filter_visitor: Incomplete | None = None, **kwargs) -> None:
        """Create a cell with added input, state, and/or output dropout.

        If `variational_recurrent` is set to `True` (**NOT** the default
        behavior), then the same dropout mask is applied at every step, as
        described in: [A Theoretically Grounded Application of Dropout in
        Recurrent Neural Networks. Y. Gal, Z.
        Ghahramani](https://arxiv.org/abs/1512.05287).

        Otherwise a different dropout mask is applied at every time step.

        Note, by default (unless a custom `dropout_state_filter` is provided),
        the memory state (`c` component of any `LSTMStateTuple`) passing through
        a `DropoutWrapper` is never modified.  This behavior is described in the
        above article.

        Args:
          cell: an RNNCell, a projection to output_size is added to it.
          input_keep_prob: unit Tensor or float between 0 and 1, input keep
            probability; if it is constant and 1, no input dropout will be
            added.
          output_keep_prob: unit Tensor or float between 0 and 1, output keep
            probability; if it is constant and 1, no output dropout will be
            added.
          state_keep_prob: unit Tensor or float between 0 and 1, output keep
            probability; if it is constant and 1, no output dropout will be
            added.  State dropout is performed on the outgoing states of the
            cell. **Note** the state components to which dropout is applied when
            `state_keep_prob` is in `(0, 1)` are also determined by the argument
            `dropout_state_filter_visitor` (e.g. by default dropout is never
            applied to the `c` component of an `LSTMStateTuple`).
          variational_recurrent: Python bool.  If `True`, then the same dropout
            pattern is applied across all time steps per run call. If this
            parameter is set, `input_size` **must** be provided.
          input_size: (optional) (possibly nested tuple of) `TensorShape`
            objects containing the depth(s) of the input tensors expected to be
            passed in to the `DropoutWrapper`.  Required and used **iff**
            `variational_recurrent = True` and `input_keep_prob < 1`.
          dtype: (optional) The `dtype` of the input, state, and output tensors.
            Required and used **iff** `variational_recurrent = True`.
          seed: (optional) integer, the randomness seed.
          dropout_state_filter_visitor: (optional), default: (see below).
            Function that takes any hierarchical level of the state and returns
            a scalar or depth=1 structure of Python booleans describing which
            terms in the state should be dropped out.  In addition, if the
            function returns `True`, dropout is applied across this sublevel.
            If the function returns `False`, dropout is not applied across this
            entire sublevel.  Default behavior: perform dropout on all terms
            except the memory (`c`) state of `LSTMCellState` objects, and don't
            try to apply dropout to
            `TensorArray` objects:
            ```
            def dropout_state_filter_visitor(s):
              # Never perform dropout on the c state.
              if isinstance(s, LSTMCellState):
                return LSTMCellState(c=False, h=True)
              elif isinstance(s, TensorArray):
                return False
              return True
            ```
          **kwargs: dict of keyword arguments for base layer.

        Raises:
          TypeError: if `cell` is not an `RNNCell`, or `keep_state_fn` is
            provided but not `callable`.
          ValueError: if any of the keep_probs are not between 0 and 1.
        """
    def get_config(self):
        """Returns the config of the dropout wrapper."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class ResidualWrapper(_RNNCellWrapper):
    """RNNCell wrapper that ensures cell inputs are added to the outputs."""
    def __init__(self, cell, residual_fn: Incomplete | None = None, **kwargs) -> None:
        """Constructs a `ResidualWrapper` for `cell`.

        Args:
          cell: An instance of `RNNCell`.
          residual_fn: (Optional) The function to map raw cell inputs and raw
            cell outputs to the actual cell outputs of the residual network.
            Defaults to calling nest.map_structure on (lambda i, o: i + o),
            inputs and outputs.
          **kwargs: dict of keyword arguments for base layer.
        """
    def get_config(self):
        """Returns the config of the residual wrapper."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class DeviceWrapper(_RNNCellWrapper):
    """Operator that ensures an RNNCell runs on a particular device."""
    def __init__(self, cell, device, **kwargs) -> None:
        """Construct a `DeviceWrapper` for `cell` with device `device`.

        Ensures the wrapped `cell` is called with `tf.device(device)`.

        Args:
          cell: An instance of `RNNCell`.
          device: A device string or function, for passing to `tf.device`.
          **kwargs: dict of keyword arguments for base layer.
        """
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...
