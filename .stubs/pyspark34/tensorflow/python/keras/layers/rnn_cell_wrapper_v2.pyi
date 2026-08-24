from _typeshed import Incomplete
from tensorflow.python.keras.layers import recurrent as recurrent
from tensorflow.python.keras.layers.legacy_rnn import rnn_cell_wrapper_impl as rnn_cell_wrapper_impl
from tensorflow.python.keras.utils import tf_inspect as tf_inspect
from tensorflow.python.util.deprecation import deprecated as deprecated
from tensorflow.python.util.tf_export import tf_export as tf_export

class _RNNCellWrapperV2(recurrent.AbstractRNNCell):
    """Base class for cells wrappers V2 compatibility.

  This class along with `rnn_cell_impl._RNNCellWrapperV1` allows to define
  wrappers that are compatible with V1 and V2, and defines helper methods for
  this purpose.
  """
    cell: Incomplete
    def __init__(self, cell, *args, **kwargs) -> None: ...
    def call(self, inputs, state, **kwargs):
        """Runs the RNN cell step computation.

    When `call` is being used, we assume that the wrapper object has been built,
    and therefore the wrapped cells has been built via its `build` method and
    its `call` method can be used directly.

    This allows to use the wrapped cell and the non-wrapped cell equivalently
    when using `call` and `build`.

    Args:
      inputs: A tensor with wrapped cell's input.
      state: A tensor or tuple of tensors with wrapped cell's state.
      **kwargs: Additional arguments passed to the wrapped cell's `call`.

    Returns:
      A pair containing:

      - Output: A tensor with cell's output.
      - New state: A tensor or tuple of tensors with new wrapped cell's state.
    """
    built: bool
    def build(self, inputs_shape) -> None:
        """Builds the wrapped cell."""
    def get_config(self): ...
    @classmethod
    def from_config(cls, config, custom_objects: Incomplete | None = None): ...

class DropoutWrapper(rnn_cell_wrapper_impl.DropoutWrapperBase, _RNNCellWrapperV2):
    """Operator adding dropout to inputs and outputs of the given cell."""
    def __init__(self, *args, **kwargs) -> None: ...

class ResidualWrapper(rnn_cell_wrapper_impl.ResidualWrapperBase, _RNNCellWrapperV2):
    """RNNCell wrapper that ensures cell inputs are added to the outputs."""
    def __init__(self, *args, **kwargs) -> None: ...

class DeviceWrapper(rnn_cell_wrapper_impl.DeviceWrapperBase, _RNNCellWrapperV2):
    """Operator that ensures an RNNCell runs on a particular device."""
    def __init__(self, *args, **kwargs) -> None: ...
