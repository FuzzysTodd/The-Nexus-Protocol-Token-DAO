import enum
import numpy as np
from _typeshed import Incomplete
from collections.abc import Sequence
from jax._src import ad_util as ad_util, core as core, dispatch as dispatch, dtypes as dtypes, source_info_util as source_info_util, util as util
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lax import lax as lax
from jax._src.lax.utils import standard_primitive as standard_primitive
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, Shape as Shape
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from typing import Callable, NamedTuple

map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

def slice(operand: ArrayLike, start_indices: Sequence[int], limit_indices: Sequence[int], strides: Sequence[int] | None = None) -> Array:
    """Wraps XLA's `Slice
  <https://www.tensorflow.org/xla/operation_semantics#slice>`_
  operator.

  Args:
    operand: an array to slice
    start_indices: a sequence of ``operand.ndim`` start indices.
    limit_indices: a sequence of ``operand.ndim`` limit indices.
    strides: an optional sequence of ``operand.ndim`` strides.

  Returns:
    The sliced array

  Examples:
    Here are some examples of simple two-dimensional slices:

    >>> x = jnp.arange(12).reshape(3, 4)
    >>> x
    Array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    >>> lax.slice(x, (1, 0), (3, 2))
    Array([[4, 5],
           [8, 9]], dtype=int32)

    >>> lax.slice(x, (0, 0), (3, 4), (1, 2))
    Array([[ 0,  2],
           [ 4,  6],
           [ 8, 10]], dtype=int32)

    These two examples are equivalent to the following Python slicing syntax:

    >>> x[1:3, 0:2]
    Array([[4, 5],
           [8, 9]], dtype=int32)

    >>> x[0:3, 0:4:2]
    Array([[ 0,  2],
           [ 4,  6],
           [ 8, 10]], dtype=int32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.slice_in_dim`
    - :func:`jax.lax.index_in_dim`
    - :func:`jax.lax.dynamic_slice`
  """
def dynamic_slice(operand: Array | np.ndarray, start_indices: Array | np.ndarray | Sequence[ArrayLike], slice_sizes: Shape) -> Array:
    """Wraps XLA's `DynamicSlice
  <https://www.tensorflow.org/xla/operation_semantics#dynamicslice>`_
  operator.

  Args:
    operand: an array to slice.
    start_indices: a list of scalar indices, one per dimension. These values
      may be dynamic.
    slice_sizes: the size of the slice. Must be a sequence of non-negative
      integers with length equal to `ndim(operand)`. Inside a JIT compiled
      function, only static values are supported (all JAX arrays inside JIT
      must have statically known size).

  Returns:
    An array containing the slice.

  Examples:
    Here is a simple two-dimensional dynamic slice:

    >>> x = jnp.arange(12).reshape(3, 4)
    >>> x
    Array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    >>> dynamic_slice(x, (1, 1), (2, 3))
    Array([[ 5,  6,  7],
           [ 9, 10, 11]], dtype=int32)

    Note the potentially surprising behavior for the case where the requested slice
    overruns the bounds of the array; in this case the start index is adjusted to
    return a slice of the requested size:

    >>> dynamic_slice(x, (1, 1), (2, 4))
    Array([[ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.slice`
    - :func:`jax.lax.dynamic_slice_in_dim`
    - :func:`jax.lax.dynamic_index_in_dim`
  """
def dynamic_update_slice(operand: Array | np.ndarray, update: ArrayLike, start_indices: Array | Sequence[ArrayLike]) -> Array:
    """Wraps XLA's `DynamicUpdateSlice
  <https://www.tensorflow.org/xla/operation_semantics#dynamicupdateslice>`_
  operator.

  Args:
    operand: an array to slice.
    update: an array containing the new values to write onto `operand`.
    start_indices: a list of scalar indices, one per dimension.

  Returns:
    An array containing the slice.

  Examples:
    Here is an example of updating a one-dimensional slice update:

    >>> x = jnp.zeros(6)
    >>> y = jnp.ones(3)
    >>> dynamic_update_slice(x, y, (2,))
    Array([0., 0., 1., 1., 1., 0.], dtype=float32)

    If the update slice is too large to fit in the array, the start
    index will be adjusted to make it fit

    >>> dynamic_update_slice(x, y, (3,))
    Array([0., 0., 0., 1., 1., 1.], dtype=float32)
    >>> dynamic_update_slice(x, y, (5,))
    Array([0., 0., 0., 1., 1., 1.], dtype=float32)

    Here is an example of a two-dimensional slice update:

    >>> x = jnp.zeros((4, 4))
    >>> y = jnp.ones((2, 2))
    >>> dynamic_update_slice(x, y, (1, 2))
    Array([[0., 0., 0., 0.],
           [0., 0., 1., 1.],
           [0., 0., 1., 1.],
           [0., 0., 0., 0.]], dtype=float32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :attr:`lax.dynamic_update_index_in_dim`
    - :attr:`lax.dynamic_update_slice_in_dim`
  """

class GatherDimensionNumbers(NamedTuple):
    """
  Describes the dimension number arguments to an `XLA's Gather operator
  <https://www.tensorflow.org/xla/operation_semantics#gather>`_. See the XLA
  documentation for more details of what the dimension numbers mean.

  Args:
    offset_dims: the set of dimensions in the `gather` output that offset into
      an array sliced from `operand`. Must be a tuple of integers in ascending
      order, each representing a dimension number of the output.
    collapsed_slice_dims: the set of dimensions `i` in `operand` that have
      `slice_sizes[i] == 1` and that should not have a corresponding dimension
      in the output of the gather. Must be a tuple of integers in ascending
      order.
    start_index_map: for each dimension in `start_indices`, gives the
      corresponding dimension in `operand` that is to be sliced. Must be a
      tuple of integers with size equal to `start_indices.shape[-1]`.

  Unlike XLA's `GatherDimensionNumbers` structure, `index_vector_dim` is
  implicit; there is always an index vector dimension and it must always be the
  last dimension. To gather scalar indices, add a trailing dimension of size 1.
  """
    offset_dims: tuple[int, ...]
    collapsed_slice_dims: tuple[int, ...]
    start_index_map: tuple[int, ...]

class GatherScatterMode(enum.Enum):
    """
  Describes how to handle out-of-bounds indices in a gather or scatter.

  Possible values are:

  CLIP:
    Indices will be clamped to the nearest in-range value, i.e., such that the
    entire window to be gathered is in-range.
  FILL_OR_DROP:
    If any part of a gathered window is out of bounds, the entire window
    that is returned, even those elements that were otherwise in-bounds, will be
    filled with a constant.
    If any part of a scattered window is out of bounds, the entire window
    will be discarded.
  PROMISE_IN_BOUNDS:
    The user promises that indices are in bounds. No additional checking will be
    performed. In practice, with the current XLA  implementation this means
    that, out-of-bounds gathers will be clamped but out-of-bounds scatters will
    be discarded. Gradients will not be correct if indices are out-of-bounds.
  """
    CLIP: Incomplete
    FILL_OR_DROP: Incomplete
    PROMISE_IN_BOUNDS: Incomplete
    @staticmethod
    def from_any(s: str | GatherScatterMode | None): ...

def gather(operand: ArrayLike, start_indices: ArrayLike, dimension_numbers: GatherDimensionNumbers, slice_sizes: Shape, *, unique_indices: bool = False, indices_are_sorted: bool = False, mode: str | GatherScatterMode | None = None, fill_value: Incomplete | None = None) -> Array:
    """Gather operator.

  Wraps `XLA's Gather operator
  <https://www.tensorflow.org/xla/operation_semantics#gather>`_.

  The semantics of gather are complicated, and its API might change in the
  future. For most use cases, you should prefer `Numpy-style indexing
  <https://numpy.org/doc/stable/reference/arrays.indexing.html>`_
  (e.g., `x[:, (1,4,7), ...]`), rather than using `gather` directly.

  Args:
    operand: an array from which slices should be taken
    start_indices: the indices at which slices should be taken
    dimension_numbers: a `lax.GatherDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices` and the output relate.
    slice_sizes: the size of each slice. Must be a sequence of non-negative
      integers with length equal to `ndim(operand)`.
    indices_are_sorted: whether `indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements gathered from ``operand`` are
      guaranteed not to overlap with each other. If ``True``, this may improve
      performance on some backends. JAX does not check this promise: if
      the elements overlap the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to ``'clip'``,
      indices are clamped so that the slice is within bounds, and when
      set to ``'fill'`` or ``'drop'`` gather returns a slice full of
      ``fill_value`` for the affected slice. The behavior for out-of-bounds
      indices when set to ``'promise_in_bounds'`` is implementation-defined.
    fill_value: the fill value to return for out-of-bounds slices when `mode`
      is ``'fill'``. Ignored otherwise. Defaults to ``NaN`` for inexact types,
      the largest negative value for signed types, the largest positive value
      for unsigned types, and ``True`` for booleans.

  Returns:
    An array containing the gather output.
  """

class ScatterDimensionNumbers(NamedTuple):
    """
  Describes the dimension number arguments to an `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_. See the XLA
  documentation for more details of what the dimension numbers mean.

  Args:
    update_window_dims: the set of dimensions in the `updates` that are window
      dimensions. Must be a tuple of integers in ascending
      order, each representing a dimension number.
    inserted_window_dims: the set of size 1 window dimensions that must be
      inserted into the shape of `updates`. Must be a tuple of integers in
      ascending order, each representing a dimension number of the output. These
      are the mirror image of `collapsed_slice_dims` in the case of `gather`.
    scatter_dims_to_operand_dims: for each dimension in `scatter_indices`, gives
      the corresponding dimension in `operand`. Must be a sequence of integers
      with size equal to indices.shape[-1].

  Unlike XLA's `ScatterDimensionNumbers` structure, `index_vector_dim` is
  implicit; there is always an index vector dimension and it must always be the
  last dimension. To scatter scalar indices, add a trailing dimension of size 1.
  """
    update_window_dims: Sequence[int]
    inserted_window_dims: Sequence[int]
    scatter_dims_to_operand_dims: Sequence[int]

def scatter_add(operand: ArrayLike, scatter_indices: ArrayLike, updates: ArrayLike, dimension_numbers: ScatterDimensionNumbers, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: str | GatherScatterMode | None = None) -> Array:
    """Scatter-add operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where
  addition is used to combine updates and values from `operand`.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    updates: the updates that should be scattered onto `operand`.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends. JAX does not check this promise: if the updated elements
      overlap when ``unique_indices`` is ``True`` the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the sum of `operand` and the scattered updates.
  """
def scatter_mul(operand: ArrayLike, scatter_indices: ArrayLike, updates: ArrayLike, dimension_numbers: ScatterDimensionNumbers, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: str | GatherScatterMode | None = None) -> Array:
    """Scatter-multiply operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where
  multiplication is used to combine updates and values from `operand`.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    updates: the updates that should be scattered onto `operand`.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends. JAX does not check this promise: if the updated elements
      overlap when ``unique_indices`` is ``True`` the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the sum of `operand` and the scattered updates.
  """
def scatter_min(operand: ArrayLike, scatter_indices: ArrayLike, updates: ArrayLike, dimension_numbers: ScatterDimensionNumbers, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: str | GatherScatterMode | None = None) -> Array:
    """Scatter-min operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where
  the `min` function is used to combine updates and values from `operand`.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    updates: the updates that should be scattered onto `operand`.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends. JAX does not check this promise: if the updated elements
      overlap when ``unique_indices`` is ``True`` the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the sum of `operand` and the scattered updates.
  """
def scatter_max(operand: ArrayLike, scatter_indices: ArrayLike, updates: ArrayLike, dimension_numbers: ScatterDimensionNumbers, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: str | GatherScatterMode | None = None) -> Array:
    """Scatter-max operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where
  the `max` function is used to combine updates and values from `operand`.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    updates: the updates that should be scattered onto `operand`.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends. JAX does not check this promise: if the updated elements
      overlap when ``unique_indices`` is ``True`` the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the sum of `operand` and the scattered updates.
  """
def scatter_apply(operand: Array, scatter_indices: Array, func: Callable[[Array], Array], dimension_numbers: ScatterDimensionNumbers, *, update_shape: Shape = (), indices_are_sorted: bool = False, unique_indices: bool = False, mode: str | GatherScatterMode | None = None) -> Array:
    """Scatter-apply operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where values
  from ``operand`` are replaced with ``func(operand)``, with duplicate indices
  resulting in multiple applications of ``func``.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Note that in the current implementation, ``scatter_apply`` is not compatible
  with automatic differentiation.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    func: unary function that will be applied at each index.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    update_shape: the shape of the updates at the given indices.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends. JAX does not check this promise: if the updated elements
      overlap when ``unique_indices`` is ``True`` the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the result of applying `func` to `operand` at the given indices.
  """
def scatter(operand: ArrayLike, scatter_indices: ArrayLike, updates: ArrayLike, dimension_numbers: ScatterDimensionNumbers, *, indices_are_sorted: bool = False, unique_indices: bool = False, mode: str | GatherScatterMode | None = None) -> Array:
    """Scatter-update operator.

  Wraps `XLA's Scatter operator
  <https://www.tensorflow.org/xla/operation_semantics#scatter>`_, where updates
  replace values from `operand`.

  If multiple updates are performed to the same index of operand, they may be
  applied in any order.

  The semantics of scatter are complicated, and its API might change in the
  future. For most use cases, you should prefer the
  :attr:`jax.numpy.ndarray.at` property on JAX arrays which uses
  the familiar NumPy indexing syntax.

  Args:
    operand: an array to which the scatter should be applied
    scatter_indices: an array that gives the indices in `operand` to which each
      update in `updates` should be applied.
    updates: the updates that should be scattered onto `operand`.
    dimension_numbers: a `lax.ScatterDimensionNumbers` object that describes
      how dimensions of `operand`, `start_indices`, `updates` and the output
      relate.
    indices_are_sorted: whether `scatter_indices` is known to be sorted. If
      true, may improve performance on some backends.
    unique_indices: whether the elements to be updated in ``operand`` are
      guaranteed to not overlap with each other. If true, may improve performance on
      some backends. JAX does not check this promise: if the updated elements
      overlap when ``unique_indices`` is ``True`` the behavior is undefined.
    mode: how to handle indices that are out of bounds: when set to 'clip',
      indices are clamped so that the slice is within bounds, and when
      set to 'fill' or 'drop' out-of-bounds updates are dropped. The behavior
      for out-of-bounds indices when set to 'promise_in_bounds' is
      implementation-defined.

  Returns:
    An array containing the sum of `operand` and the scattered updates.
  """
def index_take(src: Array, idxs: Array, axes: Sequence[int]) -> Array: ...
def slice_in_dim(operand: Array | np.ndarray, start_index: int | None, limit_index: int | None, stride: int = 1, axis: int = 0) -> Array:
    """Convenience wrapper around :func:`lax.slice` applying to only one dimension.

  This is effectively equivalent to ``operand[..., start_index:limit_index:stride]``
  with the indexing applied on the specified axis.

  Args:
    operand: an array to slice.
    start_index: an optional start index (defaults to zero)
    limit_index: an optional end index (defaults to operand.shape[axis])
    stride: an optional stride (defaults to 1)
    axis: the axis along which to apply the slice (defaults to 0)

  Returns:
    An array containing the slice.

  Examples:
    Here is a one-dimensional example:

    >>> x = jnp.arange(4)
    >>> lax.slice_in_dim(x, 1, 3)
    Array([1, 2], dtype=int32)

    Here are some two-dimensional examples:

    >>> x = jnp.arange(12).reshape(4, 3)
    >>> x
    Array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]], dtype=int32)

    >>> lax.slice_in_dim(x, 1, 3)
    Array([[3, 4, 5],
           [6, 7, 8]], dtype=int32)

    >>> lax.slice_in_dim(x, 1, 3, axis=1)
    Array([[ 1,  2],
           [ 4,  5],
           [ 7,  8],
           [10, 11]], dtype=int32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.slice`
    - :func:`jax.lax.index_in_dim`
    - :func:`jax.lax.dynamic_slice_in_dim`
  """
def index_in_dim(operand: Array | np.ndarray, index: int, axis: int = 0, keepdims: bool = True) -> Array:
    """Convenience wrapper around :func:`lax.slice` to perform int indexing.

  This is effectively equivalent to ``operand[..., start_index:limit_index:stride]``
  with the indexing applied on the specified axis.

  Args:
    operand: an array to index.
    index: integer index
    axis: the axis along which to apply the index (defaults to 0)
    keepdims: boolean specifying whether the output array should preserve the
      rank of the input (default=True)

  Returns:
    The subarray at the specified index.

  Examples:
    Here is a one-dimensional example:

    >>> x = jnp.arange(4)
    >>> lax.index_in_dim(x, 2)
    Array([2], dtype=int32)

    >>> lax.index_in_dim(x, 2, keepdims=False)
    Array(2, dtype=int32)

    Here are some two-dimensional examples:

    >>> x = jnp.arange(12).reshape(3, 4)
    >>> x
    Array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    >>> lax.index_in_dim(x, 1)
    Array([[4, 5, 6, 7]], dtype=int32)

    >>> lax.index_in_dim(x, 1, axis=1, keepdims=False)
    Array([1, 5, 9], dtype=int32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.slice`
    - :func:`jax.lax.slice_in_dim`
    - :func:`jax.lax.dynamic_index_in_dim`
  """
def dynamic_slice_in_dim(operand: Array | np.ndarray, start_index: ArrayLike, slice_size: int, axis: int = 0) -> Array:
    """Convenience wrapper around :func:`lax.dynamic_slice` applied to one dimension.

  This is roughly equivalent to the following Python indexing syntax applied
  along the specified axis: ``operand[..., start_index:start_index + slice_size]``.

  Args:
    operand: an array to slice.
    start_index: the (possibly dynamic) start index
    slice_size: the static slice size
    axis: the axis along which to apply the slice (defaults to 0)

  Returns:
    An array containing the slice.

  Examples:
    Here is a one-dimensional example:

    >>> x = jnp.arange(5)
    >>> dynamic_slice_in_dim(x, 1, 3)
    Array([1, 2, 3], dtype=int32)

    Like `jax.lax.dynamic_slice`, out-of-bound slices will be clipped to the
    valid range:

    >>> dynamic_slice_in_dim(x, 4, 3)
    Array([2, 3, 4], dtype=int32)

    Here is a two-dimensional example:

    >>> x = jnp.arange(12).reshape(3, 4)
    >>> x
    Array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    >>> dynamic_slice_in_dim(x, 1, 2, axis=1)
    Array([[ 1,  2],
           [ 5,  6],
           [ 9, 10]], dtype=int32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.slice_in_dim`
    - :func:`jax.lax.dynamic_slice`
    - :func:`jax.lax.dynamic_index_in_dim`
  """
def dynamic_index_in_dim(operand: Array | np.ndarray, index: int | Array, axis: int = 0, keepdims: bool = True) -> Array:
    """Convenience wrapper around dynamic_slice to perform int indexing.

  This is roughly equivalent to the following Python indexing syntax applied
  along the specified axis: ``operand[..., index]``.

  Args:
    operand: an array to slice.
    index: the (possibly dynamic) start index
    axis: the axis along which to apply the slice (defaults to 0)
    keepdims: boolean specifying whether the output should have the same rank as
      the input (default = True)

  Returns:
    An array containing the slice.

  Examples:
    Here is a one-dimensional example:

    >>> x = jnp.arange(5)
    >>> dynamic_index_in_dim(x, 1)
    Array([1], dtype=int32)

    >>> dynamic_index_in_dim(x, 1, keepdims=False)
    Array(1, dtype=int32)

    Here is a two-dimensional example:

    >>> x = jnp.arange(12).reshape(3, 4)
    >>> x
    Array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]], dtype=int32)

    >>> dynamic_index_in_dim(x, 1, axis=1, keepdims=False)
    Array([1, 5, 9], dtype=int32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.index_in_dim`
    - :func:`jax.lax.dynamic_slice`
    - :func:`jax.lax.dynamic_slice_in_dim`
  """
def dynamic_update_slice_in_dim(operand: Array | np.ndarray, update: ArrayLike, start_index: ArrayLike, axis: int) -> Array:
    """Convenience wrapper around :func:`dynamic_update_slice` to update
  a slice in a single ``axis``.

  Args:
    operand: an array to slice.
    update: an array containing the new values to write onto `operand`.
    start_index: a single scalar index
    axis: the axis of the update.

  Returns:
    The updated array

  Examples:

    >>> x = jnp.zeros(6)
    >>> y = jnp.ones(3)
    >>> dynamic_update_slice_in_dim(x, y, 2, axis=0)
    Array([0., 0., 1., 1., 1., 0.], dtype=float32)

    If the update slice is too large to fit in the array, the start
    index will be adjusted to make it fit:

    >>> dynamic_update_slice_in_dim(x, y, 3, axis=0)
    Array([0., 0., 0., 1., 1., 1.], dtype=float32)
    >>> dynamic_update_slice_in_dim(x, y, 5, axis=0)
    Array([0., 0., 0., 1., 1., 1.], dtype=float32)

    Here is an example of a two-dimensional slice update:

    >>> x = jnp.zeros((4, 4))
    >>> y = jnp.ones((2, 4))
    >>> dynamic_update_slice_in_dim(x, y, 1, axis=0)
    Array([[0., 0., 0., 0.],
           [1., 1., 1., 1.],
           [1., 1., 1., 1.],
           [0., 0., 0., 0.]], dtype=float32)

    Note that the shape of the additional axes in ``update`` need not
    match the associated dimensions of the ``operand``:

    >>> y = jnp.ones((2, 3))
    >>> dynamic_update_slice_in_dim(x, y, 1, axis=0)
    Array([[0., 0., 0., 0.],
           [1., 1., 1., 0.],
           [1., 1., 1., 0.],
           [0., 0., 0., 0.]], dtype=float32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.dynamic_update_slice`
    - :func:`jax.lax.dynamic_update_index_in_dim`
    - :func:`jax.lax.dynamic_slice_in_dim`
  """
def dynamic_update_index_in_dim(operand: Array | np.ndarray, update: ArrayLike, index: ArrayLike, axis: int) -> Array:
    """Convenience wrapper around :func:`dynamic_update_slice` to update a slice
  of size 1 in a single ``axis``.

  Args:
    operand: an array to slice.
    update: an array containing the new values to write onto `operand`.
    index: a single scalar index
    axis: the axis of the update.

  Returns:
    The updated array

  Examples:

    >>> x = jnp.zeros(6)
    >>> y = 1.0
    >>> dynamic_update_index_in_dim(x, y, 2, axis=0)
    Array([0., 0., 1., 0., 0., 0.], dtype=float32)

    >>> y = jnp.array([1.0])
    >>> dynamic_update_index_in_dim(x, y, 2, axis=0)
    Array([0., 0., 1., 0., 0., 0.], dtype=float32)

    If the specified index is out of bounds, the index will be clipped to the
    valid range:

    >>> dynamic_update_index_in_dim(x, y, 10, axis=0)
    Array([0., 0., 0., 0., 0., 1.], dtype=float32)

    Here is an example of a two-dimensional dynamic index update:

    >>> x = jnp.zeros((4, 4))
    >>> y = jnp.ones(4)
    >>> dynamic_update_index_in_dim(x, y, 1, axis=0)
    Array([[0., 0., 0., 0.],
          [1., 1., 1., 1.],
          [0., 0., 0., 0.],
          [0., 0., 0., 0.]], dtype=float32)

    Note that the shape of the additional axes in ``update`` need not
    match the associated dimensions of the ``operand``:

    >>> y = jnp.ones((1, 3))
    >>> dynamic_update_index_in_dim(x, y, 1, 0)
    Array([[0., 0., 0., 0.],
           [1., 1., 1., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]], dtype=float32)

  See Also:
    - :attr:`jax.numpy.ndarray.at`
    - :func:`jax.lax.dynamic_update_slice`
    - :func:`jax.lax.dynamic_update_index_in_dim`
    - :func:`jax.lax.dynamic_index_in_dim`
  """

slice_p: Incomplete
dynamic_slice_p: Incomplete
dynamic_update_slice_p: Incomplete
gather_p: Incomplete
scatter_add_p: Incomplete
scatter_mul_p: Incomplete
scatter_min_p: Incomplete
scatter_max_p: Incomplete
scatter_p: Incomplete
