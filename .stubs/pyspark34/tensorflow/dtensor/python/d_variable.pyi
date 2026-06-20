from _typeshed import Incomplete
from tensorflow.dtensor.python import api as api
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import dtypes as dtypes, errors as errors, ops as ops
from tensorflow.python.ops import math_ops as math_ops, resource_variable_ops as resource_variable_ops
from tensorflow.python.training.saving import saveable_object as saveable_object
from tensorflow.python.util.tf_export import tf_export as tf_export

class DSaveSpec(saveable_object.SaveSpec):
    """DTensor SaveSpec that additionaly captures global_shape and layout."""
    global_shape: Incomplete
    layout: Incomplete
    def __init__(self, tensor, slice_spec, name, global_shape, layout, dtype: Incomplete | None = None, device: Incomplete | None = None) -> None: ...

class _DVariableSaveable(saveable_object.SaveableObject):
    """Class for defining how to save/restore DTensor variable."""
    def __init__(self, dvariable, name) -> None: ...
    def should_cast(self, v):
        """Returns True if v has float32 dtype and is intructed to save as bf16.

    Args:
      v : The variable that determines whether to cast.

    Returns:
      True if current savable DVariable is instructed to save as bfloat16 and
        the variable has dtype float32.
    """
    def restore(self, restored_tensors, restored_shapes):
        """Restores the same value into all variables."""

class DVariable(resource_variable_ops.ResourceVariable):
    """A replacement for tf.Variable which follows initial value placement.

    The class also handles restore/save operations in DTensor. Note that,
    DVariable may fall back to normal tf.Variable at this moment if
    `initial_value` is not a DTensor.
  """
    layout: Incomplete
    def __init__(self, initial_value, *args, dtype: Incomplete | None = None, **kwargs) -> None:
        """Overrides tf.Variable to fix VarHandleOp placements."""
    @property
    def save_as_bf16(self): ...
    @save_as_bf16.setter
    def save_as_bf16(self, save_as_bf16) -> None:
        """Enables saving float32 as bfloat16."""
