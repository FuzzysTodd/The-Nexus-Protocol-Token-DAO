import dataclasses
from _typeshed import Incomplete
from jax import lax as lax
from jax._src import core as core, dtypes as dtypes, util as util
from jax.experimental.jax2tf import jax2tf as jax2tf
from typing import Any, Callable

tf_impl_no_xla: dict[core.Primitive, Callable[..., Any]]
TfVal = Any
DType = Any
PrecisionType = Any

def pads_to_padtype(in_shape, window_shape, window_strides, padding) -> str: ...

@dataclasses.dataclass
class GatherArgs:
    operand: TfVal
    start_indices: TfVal
    dnums: lax.GatherDimensionNumbers
    slice_sizes: TfVal
    op_shape: core.Shape
    start_indices_shape: core.Shape
    out_aval: core.ShapedArray
    def __post_init__(self) -> None: ...
    @property
    def batch_dims(self): ...
    def __init__(self, operand, start_indices, dnums, slice_sizes, op_shape, start_indices_shape, out_aval) -> None: ...

def gather_precondition(precondition_fn: Callable[[GatherArgs], None]):
    """Decorator for specifying a precondition function.

  This decorator should be put on a function with argument `arg` of type
  `GatherArgs`. It will first call `precondition_fn` with `arg` (which may throw
  an exception), and then call the function it is decorating with `arg` as well.
  """
def shift_axes_forward(operand, axes: tuple[int, ...], inverse: bool = False, forward: bool = True):
    """Shifts the tuple of axes to the front of an array"""
def convert_scatter_jax_to_tf(update_op, unsorted_segment_op: Incomplete | None = None): ...
