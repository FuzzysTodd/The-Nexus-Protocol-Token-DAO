from _typeshed import Incomplete
from keras.layers.rnn.legacy_cells import RNNCell as RNNCell

ASSERT_LIKE_RNNCELL_ERROR_REGEXP: str

def assert_like_rnncell(cell_name, cell) -> None:
    """Raises a TypeError if cell is not like an RNNCell.

    NOTE: Do not rely on the error message (in particular in tests) which can be
    subject to change to increase readability. Use
    ASSERT_LIKE_RNNCELL_ERROR_REGEXP.

    Args:
      cell_name: A string to give a meaningful error referencing to the name of
        the functionargument.
      cell: The object which should behave like an RNNCell.

    Raises:
      TypeError: A human-friendly exception.
    """

class _RNNCellWrapperV1(RNNCell):
    """Base class for cells wrappers V1 compatibility.

    This class along with `_RNNCellWrapperV2` allows to define cells wrappers
    that are compatible with V1 and V2, and defines helper methods for this
    purpose.
    """
    cell: Incomplete
    def __init__(self, cell, *args, **kwargs) -> None: ...
    def __call__(self, inputs, state, scope: Incomplete | None = None):
        """Runs the RNN cell step computation.

        We assume that the wrapped RNNCell is being built within its `__call__`
        method. We directly use the wrapped cell's `__call__` in the overridden
        wrapper `__call__` method.

        This allows to use the wrapped cell and the non-wrapped cell
        equivalently when using `__call__`.

        Args:
          inputs: A tensor with wrapped cell's input.
          state: A tensor or tuple of tensors with wrapped cell's state.
          scope: VariableScope for the subgraph created in the wrapped cells'
            `__call__`.

        Returns:
          A pair containing:

          - Output: A tensor with cell's output.
          - New state: A tensor or tuple of tensors with new wrapped cell's
            state.
        """
    @property
    def state_size(self): ...
    @property
    def output_size(self): ...
    def zero_state(self, batch_size, dtype): ...
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class DropoutWrapper(_RNNCellWrapperV1):
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
            added. State dropout is performed on the outgoing states of the
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
            try to apply dropout to `TensorArray` objects:
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
    @property
    def wrapped_cell(self): ...
    built: bool
    def build(self, inputs_shape) -> None: ...
    def get_config(self):
        """Returns the config of the dropout wrapper."""
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class ResidualWrapper(_RNNCellWrapperV1):
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

class DeviceWrapper(_RNNCellWrapperV1):
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
