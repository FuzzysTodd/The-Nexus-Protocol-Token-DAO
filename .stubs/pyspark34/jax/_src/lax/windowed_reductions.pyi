from _typeshed import Incomplete
from collections.abc import Sequence
from jax import tree_util as tree_util
from jax._src import ad_util as ad_util, core as core, dispatch as dispatch, dtypes as dtypes, util as util
from jax._src.core import ConcreteArray as ConcreteArray, ShapedArray as ShapedArray
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lax import convolution as convolution, lax as lax, slicing as slicing
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.numpy.ufuncs import logaddexp as logaddexp
from jax._src.typing import Array as Array
from typing import Callable

map: Incomplete
zip: Incomplete

def reduce_window(operand, init_value, computation: Callable, window_dimensions: core.Shape, window_strides: Sequence[int], padding: str | Sequence[tuple[int, int]], base_dilation: Sequence[int] | None = None, window_dilation: Sequence[int] | None = None) -> Array:
    """Wraps XLA's `ReduceWindowWithGeneralPadding
  <https://www.tensorflow.org/xla/operation_semantics#reducewindow>`_
  operator.
  """

reduce_window_p: Incomplete
reduce_window_sum_p: Incomplete

def reduce_window_shape_tuple(operand_shape, window_dimensions, window_strides, padding, base_dilation: Incomplete | None = None, window_dilation: Incomplete | None = None): ...

reduce_window_max_p: Incomplete
reduce_window_min_p: Incomplete
select_and_scatter_p: Incomplete
select_and_scatter_add_p: Incomplete
select_and_gather_add_p: Incomplete
