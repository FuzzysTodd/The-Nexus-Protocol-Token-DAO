import enum
import numpy as np
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from jax import tree_util as tree_util
from jax._src import ad_util as ad_util, api as api, api_util as api_util, array as array, core as core, dispatch as dispatch, dtypes as dtypes, effects as effects, source_info_util as source_info_util, util as util, xla_bridge as xla_bridge
from jax._src.abstract_arrays import array_types as array_types
from jax._src.config import config as config
from jax._src.core import ConcreteArray as ConcreteArray, Primitive as Primitive, ShapedArray as ShapedArray, UnshapedArray as UnshapedArray, abstract_token as abstract_token, canonicalize_shape as canonicalize_shape, raise_to_shaped as raise_to_shaped
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla, xla as xla
from jax._src.interpreters.batching import RaggedAxis as RaggedAxis
from jax._src.lax import slicing as slicing
from jax._src.lax.utils import dtype_to_string as dtype_to_string, standard_abstract_eval as standard_abstract_eval, standard_multi_result_abstract_eval as standard_multi_result_abstract_eval, standard_named_shape_rule as standard_named_shape_rule, standard_primitive as standard_primitive
from jax._src.lib import xla_client as xla_client
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import chlo as chlo, hlo as hlo
from jax._src.sharding_impls import PmapSharding as PmapSharding
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike, DuckTypedArray as DuckTypedArray, Shape as Shape
from jax._src.util import NumpyComplexWarning as NumpyComplexWarning, cache as cache, canonicalize_axis as canonicalize_axis, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list
from jax.tree_util import tree_map as tree_map
from typing import Any, Callable, TypeVar, overload

xb = xla_bridge
xc = xla_client
xops: Incomplete
xe: Incomplete
T = TypeVar('T')
map: Incomplete
unsafe_map: Incomplete
zip: Incomplete
unsafe_zip: Incomplete

def asarray(x: ArrayLike) -> Array:
    """Lightweight conversion of ArrayLike input to Array output."""
@overload
def broadcast_shapes(*shapes: tuple[int, ...]) -> tuple[int, ...]: ...
@overload
def broadcast_shapes(*shapes: tuple[int | core.Tracer, ...]) -> tuple[int | core.Tracer, ...]: ...
def neg(x: ArrayLike) -> Array:
    """Elementwise negation: :math:`-x`."""
def sign(x: ArrayLike) -> Array:
    """Elementwise sign.

  For floating-point inputs, returns
  :math:`\\mathrm{sign}(x) = \\begin{cases}
  -1 & x < 0\\\\\n  -0 & x = -0\\\\\n  \\mathit{NaN} & x = \\mathit{NaN}\\\\\n  +0 & x = +0\\\\\n  1 & x > 0
  \\end{cases}`

  For signed integer inputs, returns
  :math:`\\mathrm{sign}(x) = \\begin{cases}
  -1 & x < 0\\\\\n  0 & x = 0\\\\\n  1 & x > 0
  \\end{cases}`

  For complex inputs, returns the complex phase, i.e.
  :math:`\\mathrm{sign}(x) = \\frac{x}{|x|}`.
  """
def nextafter(x1: ArrayLike, x2: ArrayLike) -> Array:
    """Returns the next representable value after `x1` in the direction of `x2`.

  Note that in some environments flush-denormal-to-zero semantics is used.
  This means that, around zero, this function returns strictly non-zero
  values which appear as zero in any operations. Consider this example::

    >>> jnp.nextafter(0, 1)  # denormal numbers are representable
    Array(1.e-45, dtype=float32, weak_type=True)
    >>> jnp.nextafter(0, 1) * 1  # but are flushed to zero
    Array(0., dtype=float32, weak_type=True)

  For the smallest usable (i.e. normal) float, use ``tiny`` of ``jnp.finfo``.
  """
def floor(x: ArrayLike) -> Array:
    """Elementwise floor: :math:`\\left\\lfloor x \\right\\rfloor`."""
def ceil(x: ArrayLike) -> Array:
    """Elementwise ceiling: :math:`\\left\\lceil x \\right\\rceil`."""

class RoundingMethod(enum.IntEnum):
    AWAY_FROM_ZERO: int
    TO_NEAREST_EVEN: int

def round(x: ArrayLike, rounding_method: RoundingMethod = ...) -> Array:
    """Elementwise round.

  Rounds values to the nearest integer.

  Args:
    x: an array or scalar value to round.
    rounding_method: the method to use when rounding halfway values
      (e.g., `0.5`). See ``lax.RoundingMethod`` for the list of possible
      values.

  Returns:
    An array containing the elementwise rounding of x.
  """
def is_finite(x: ArrayLike) -> Array:
    """Elementwise :math:`\\mathrm{isfinite}`.

  For each element x returns `True` if and only if x is not :math:`\\pm\\infty` or
  :math:`\\mathit{NaN}`.
  """
def exp(x: ArrayLike) -> Array:
    """Elementwise exponential: :math:`e^x`."""
def exp2(x: ArrayLike) -> Array:
    """Elementwise base-2 exponential: :math:`2^x`."""
def expm1(x: ArrayLike) -> Array:
    """Elementwise :math:`e^{x} - 1`."""
def log(x: ArrayLike) -> Array:
    """Elementwise natural logarithm: :math:`\\mathrm{log}(x)`."""
def log1p(x: ArrayLike) -> Array:
    """Elementwise :math:`\\mathrm{log}(1 + x)`."""
def tanh(x: ArrayLike) -> Array:
    """Elementwise hyperbolic tangent: :math:`\\mathrm{tanh}(x)`."""
def logistic(x: ArrayLike) -> Array:
    """Elementwise logistic (sigmoid) function: :math:`\\frac{1}{1 + e^{-x}}`."""
def sin(x: ArrayLike) -> Array:
    """Elementwise sine: :math:`\\mathrm{sin}(x)`."""
def cos(x: ArrayLike) -> Array:
    """Elementwise cosine: :math:`\\mathrm{cos}(x)`."""
def atan2(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise arc tangent of two variables:
    :math:`\\mathrm{atan}({x \\over y})`."""
def real(x: ArrayLike) -> Array:
    """Elementwise extract real part: :math:`\\mathrm{Re}(x)`.

  Returns the real part of a complex number.
  """
def imag(x: ArrayLike) -> Array:
    """Elementwise extract imaginary part: :math:`\\mathrm{Im}(x)`.

  Returns the imaginary part of a complex number.
  """
def complex(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise make complex number: :math:`x + jy`.

  Builds a complex number from real and imaginary parts.
  """
def conj(x: ArrayLike) -> Array:
    """Elementwise complex conjugate function: :math:`\\overline{x}`."""
def abs(x: ArrayLike) -> Array:
    """Elementwise absolute value: :math:`|x|`."""
def pow(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise power: :math:`x^y`."""
def integer_pow(x: ArrayLike, y: int) -> Array:
    """Elementwise power: :math:`x^y`, where :math:`y` is a fixed integer."""
def sqrt(x: ArrayLike) -> Array:
    """Elementwise square root: :math:`\\sqrt{x}`."""
def rsqrt(x: ArrayLike) -> Array:
    """Elementwise reciprocal square root:  :math:`1 \\over \\sqrt{x}`."""
def cbrt(x: ArrayLike) -> Array:
    """Elementwise cube root: :math:`\\sqrt[3]{x}`."""
def bitwise_not(x: ArrayLike) -> Array:
    """Elementwise NOT: :math:`\\neg x`."""
def bitwise_and(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise AND: :math:`x \\wedge y`."""
def bitwise_or(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise OR: :math:`x \\vee y`."""
def bitwise_xor(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise exclusive OR: :math:`x \\oplus y`."""
def population_count(x: ArrayLike) -> Array:
    """Elementwise popcount, count the number of set bits in each element."""
def clz(x: ArrayLike) -> Array:
    """Elementwise count-leading-zeros."""
def add(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise addition: :math:`x + y`."""
def sub(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise subtraction: :math:`x - y`."""
def mul(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise multiplication: :math:`x \\times y`."""
def div(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise division: :math:`x \\over y`.

  Integer division overflow
  (division by zero or signed division of INT_SMIN with -1)
  produces an implementation defined value.
  """
def rem(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise remainder: :math:`x \\bmod y`.

  The sign of the result is taken from the dividend,
  and the absolute value of the result is always
  less than the divisor's absolute value.

  Integer division overflow
  (remainder by zero or remainder of INT_SMIN with -1)
  produces an implementation defined value.
  """
def max(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise maximum: :math:`\\mathrm{max}(x, y)`

  For complex numbers, uses a lexicographic comparison on the
  `(real, imaginary)` pairs."""
def min(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise minimum:  :math:`\\mathrm{min}(x, y)`

  For complex numbers, uses a lexicographic comparison on the
  `(real, imaginary)` pairs."""
def shift_left(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise left shift: :math:`x \\ll y`."""
def shift_right_arithmetic(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise arithmetic right shift: :math:`x \\gg y`."""
def shift_right_logical(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise logical right shift: :math:`x \\gg y`."""
def eq(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise equals: :math:`x = y`."""
def ne(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise not-equals: :math:`x \\neq y`."""
def ge(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise greater-than-or-equals: :math:`x \\geq y`."""
def gt(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise greater-than: :math:`x > y`."""
def le(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise less-than-or-equals: :math:`x \\leq y`."""
def lt(x: ArrayLike, y: ArrayLike) -> Array:
    """Elementwise less-than: :math:`x < y`."""
def convert_element_type(operand: ArrayLike, new_dtype: DTypeLike) -> Array:
    """Elementwise cast.

  Wraps XLA's `ConvertElementType
  <https://www.tensorflow.org/xla/operation_semantics#convertelementtype>`_
  operator, which performs an elementwise conversion from one type to another.
  Similar to a C++ `static_cast`.

  Args:
    operand: an array or scalar value to be cast
    new_dtype: a NumPy dtype representing the target type.

  Returns:
    An array with the same shape as `operand`, cast elementwise to `new_dtype`.
  """
def bitcast_convert_type(operand: ArrayLike, new_dtype: DTypeLike) -> Array:
    """Elementwise bitcast.

  Wraps XLA's `BitcastConvertType
  <https://www.tensorflow.org/xla/operation_semantics#bitcastconverttype>`_
  operator, which performs a bit cast from one type to another.

  The output shape depends on the size of the input and output dtypes with
  the following logic::

    if new_dtype.itemsize == operand.dtype.itemsize:
      output_shape = operand.shape
    if new_dtype.itemsize < operand.dtype.itemsize:
      output_shape = (*operand.shape, operand.dtype.itemsize // new_dtype.itemsize)
    if new_dtype.itemsize > operand.dtype.itemsize:
      assert operand.shape[-1] * operand.dtype.itemsize == new_dtype.itemsize
      output_shape = operand.shape[:-1]

  Args:
    operand: an array or scalar value to be cast
    new_dtype: the new type. Should be a NumPy type.

  Returns:
    An array of shape `output_shape` (see above) and type `new_dtype`,
    constructed from the same bits as operand.
  """
def clamp(min: ArrayLike, x: ArrayLike, max: ArrayLike) -> Array:
    """Elementwise clamp.

  Returns :math:`\\mathrm{clamp}(x) = \\begin{cases}
  \\mathit{min} & \\text{if } x < \\mathit{min},\\\\\n  \\mathit{max} & \\text{if } x > \\mathit{max},\\\\\n  x & \\text{otherwise}
  \\end{cases}`.
  """
def concatenate(operands: Array | Sequence[ArrayLike], dimension: int) -> Array:
    """Concatenates a sequence of arrays along `dimension`.

  Wraps XLA's `Concatenate
  <https://www.tensorflow.org/xla/operation_semantics#concatenate>`_
  operator.

  Args:
    operands: a sequence of arrays to concatenate. The arrays must have equal
      shapes, except in the `dimension` axis.
    dimension: the dimension along which to concatenate the arrays.

  Returns:
    An array containing the concatenation.
  """

class _enum_descriptor:
    val: Incomplete
    def __init__(self, val) -> None: ...
    def __get__(self, _, owner): ...

class Precision(xla_client.PrecisionConfig.Precision):
    """Precision enum for lax functions

  The `precision` argument to JAX functions generally controls the tradeoff
  between speed and accuracy for array computations on accelerator backends,
  (i.e. TPU and GPU). Members are:

  DEFAULT:
    Fastest mode, but least accurate. Performs computations in bfloat16.
    Aliases: ``'default'``, ``'fastest'``, ``'bfloat16'``.
  HIGH:
    Slower but more accurate. Performs float32 computations in 3 bfloat16
    passes, or using tensorfloat32 where available. Aliases: ``'high'``,
    ``'bfloat16_3x'``, ``'tensorfloat32'``.
  HIGHEST:
    Slowest but most accurate. Performs computations in float32 or float64
    as applicable. Aliases: ``'highest'``, ``'float32'``.
  """
    DEFAULT: Incomplete
    HIGH: Incomplete
    HIGHEST: Incomplete
    def __init__(self, arg0) -> None: ...
PrecisionType = Precision
PrecisionLike = None | str | PrecisionType | tuple[str, str] | tuple[PrecisionType, PrecisionType]

def dot(lhs: Array, rhs: Array, precision: PrecisionLike = None, preferred_element_type: DTypeLike | None = None) -> Array:
    """Vector/vector, matrix/vector, and matrix/matrix multiplication.

  Wraps XLA's `Dot
  <https://www.tensorflow.org/xla/operation_semantics#dot>`_
  operator.

  For more general contraction, see the `dot_general` operator.

  Args:
    lhs: an array of dimension 1 or 2.
    rhs: an array of dimension 1 or 2.
    precision: Optional. Either ``None``, which means the default precision for
      the backend, a :class:`~jax.lax.Precision` enum value (``Precision.DEFAULT``,
      ``Precision.HIGH`` or ``Precision.HIGHEST``) or a tuple of two
      :class:`~jax.lax.Precision` enums indicating precision of ``lhs``` and ``rhs``.
    preferred_element_type: Optional. Either ``None``, which means the default
      accumulation type for the input types, or a datatype, indicating to
      accumulate results to and return a result with that datatype.

  Returns:
    An array containing the product.
  """
DotDimensionNumbers = tuple[tuple[Sequence[int], Sequence[int]], tuple[Sequence[int], Sequence[int]]]

def dot_general(lhs: ArrayLike, rhs: ArrayLike, dimension_numbers: DotDimensionNumbers, precision: PrecisionLike = None, preferred_element_type: DTypeLike | None = None) -> Array:
    """General dot product/contraction operator.

  Wraps XLA's `DotGeneral
  <https://www.tensorflow.org/xla/operation_semantics#dotgeneral>`_
  operator.

  The semantics of ``dot_general`` are complicated, but most users should not have to
  use it directly. Instead, you can use higher-level functions like :func:`jax.numpy.dot`,
  :func:`jax.numpy.matmul`, :func:`jax.numpy.tensordot`, :func:`jax.numpy.einsum`,
  and others which will construct appropriate calls to ``dot_general`` under the hood.
  If you really want to understand ``dot_general`` itself, we recommend reading XLA's
  `DotGeneral  <https://www.tensorflow.org/xla/operation_semantics#dotgeneral>`_
  operator documentation.

  Args:
    lhs: an array
    rhs: an array
    dimension_numbers: a tuple of tuples of sequences of ints of the form
      ``((lhs_contracting_dims, rhs_contracting_dims), (lhs_batch_dims, rhs_batch_dims))``
    precision: Optional. Either ``None``, which means the default precision for
      the backend, a :class:`~jax.lax.Precision` enum value (``Precision.DEFAULT``,
      ``Precision.HIGH`` or ``Precision.HIGHEST``) or a tuple of two
      :class:`~jax.lax.Precision` enums indicating precision of ``lhs``` and ``rhs``.
    preferred_element_type: Optional. Either ``None``, which means the default
      accumulation type for the input types, or a datatype, indicating to
      accumulate results to and return a result with that datatype.

  Returns:
    An array whose first dimensions are the (shared) batch dimensions, followed by
    the ``lhs`` non-contracting/non-batch dimensions, and finally the ``rhs``
    non-contracting/non-batch dimensions.
  """
def broadcast(operand: ArrayLike, sizes: Sequence[int]) -> Array:
    """Broadcasts an array, adding new leading dimensions

  Args:
    operand: an array
    sizes: a sequence of integers, giving the sizes of new leading dimensions
      to add to the front of the array.

  Returns:
    An array containing the result.

  See Also:
    jax.lax.broadcast_in_dim : add new dimensions at any location in the array shape.
  """
def broadcast_in_dim(operand: ArrayLike, shape: Shape, broadcast_dimensions: Sequence[int]) -> Array:
    """Wraps XLA's `BroadcastInDim
  <https://www.tensorflow.org/xla/operation_semantics#broadcastindim>`_
  operator.

  Args:
    operand: an array
    shape: the shape of the target array
    broadcast_dimensions: to which dimension in the target shape each dimension
      of the operand shape corresponds to.  That is, dimension i of the operand
      becomes dimension broadcast_dimensions[i] of the result.

  Returns:
    An array containing the result.

  See Also:
    jax.lax.broadcast : simpler interface to add new leading dimensions.
  """
def broadcast_to_rank(x: Array, rank: int) -> Array:
    """Adds leading dimensions of ``1`` to give ``x`` rank ``rank``."""
def reshape(operand: ArrayLike, new_sizes: Shape, dimensions: Sequence[int] | None = None) -> Array:
    """Wraps XLA's `Reshape
  <https://www.tensorflow.org/xla/operation_semantics#reshape>`_
  operator.

  For inserting/removing dimensions of size 1, prefer using ``lax.squeeze`` /
  ``lax.expand_dims``. These preserve information about axis identity that may
  be useful for advanced transformation rules.

  Args:
    operand: array to be reshaped.
    new_sizes: sequence of integers specifying the resulting shape. The size
      of the final array must match the size of the input.
    dimensions: optional sequence of integers specifying the permutation order of
      the input shape. If specified, the length must match ``operand.shape``.

  Returns:
    out: reshaped array.

  Examples:
    Simple reshaping from one to two dimensions:

    >>> x = jnp.arange(6)
    >>> y = reshape(x, (2, 3))
    >>> y
    Array([[0, 1, 2],
                 [3, 4, 5]], dtype=int32)

    Reshaping back to one dimension:

    >>> reshape(y, (6,))
    Array([0, 1, 2, 3, 4, 5], dtype=int32)

    Reshaping to one dimension with permutation of dimensions:

    >>> reshape(y, (6,), (1, 0))
    Array([0, 3, 1, 4, 2, 5], dtype=int32)
  """
def pad(operand: ArrayLike, padding_value: ArrayLike, padding_config: Sequence[tuple[int, int, int]]) -> Array:
    """Applies low, high, and/or interior padding to an array.

  Wraps XLA's `Pad
  <https://www.tensorflow.org/xla/operation_semantics#pad>`_
  operator.

  Args:
    operand: an array to be padded.
    padding_value: the value to be inserted as padding. Must have the same dtype
      as ``operand``.
    padding_config: a sequence of ``(low, high, interior)`` tuples of integers,
      giving the amount of low, high, and interior (dilation) padding to insert
      in each dimension.

  Returns:
    The ``operand`` array with padding value ``padding_value`` inserted in each
    dimension according to the ``padding_config``.
  """
def rev(operand: ArrayLike, dimensions: Sequence[int]) -> Array:
    """Wraps XLA's `Rev
  <https://www.tensorflow.org/xla/operation_semantics#rev_reverse>`_
  operator.
  """
def select(pred: ArrayLike, on_true: ArrayLike, on_false: ArrayLike) -> Array:
    """Selects between two branches based on a boolean predicate.

  Wraps XLA's `Select
  <https://www.tensorflow.org/xla/operation_semantics#select>`_
  operator.

  In general :func:`~jax.lax.select` leads to evaluation of both branches, although
  the compiler may elide computations if possible. For a similar function that
  usually evaluates only a single branch, see :func:`~jax.lax.cond`.

  Args:
    pred: boolean array
    on_true: array containing entries to return where ``pred`` is True. Must have
      the same shape as ``pred``, and the same shape and dtype as ``on_false``.
    on_false: array containing entries to return where ``pred`` is False. Must have
      the same shape as ``pred``, and the same shape and dtype as ``on_true``.

  Returns:
    result: array with same shape and dtype as ``on_true`` and ``on_false``.
  """
def select_n(which: ArrayLike, *cases: ArrayLike) -> Array:
    """Selects array values from multiple cases.

  Generalizes XLA's `Select
  <https://www.tensorflow.org/xla/operation_semantics#select>`_
  operator. Unlike XLA's version, the operator is variadic and can select
  from many cases using an integer `pred`.

  Args:
    which: determines which case should be returned. Must be an array containing
      either a boolean or integer values. May either be a scalar or have
      shape matching ``cases``. For each array element, the value of ``which``
      determines which of ``cases`` is taken. ``which`` must be in the range
      ``[0 .. len(cases))``; for values outside that range the behavior is
      implementation-defined.
    *cases: a non-empty list of array cases. All must have equal dtypes and
      equal shapes.
  Returns:
    An array with shape and dtype equal to the cases, whose values are chosen
    according to ``which``.
  """
def transpose(operand: ArrayLike, permutation: Sequence[int] | np.ndarray) -> Array:
    """Wraps XLA's `Transpose
  <https://www.tensorflow.org/xla/operation_semantics#transpose>`_
  operator.
  """
def argmin(operand: ArrayLike, axis: int, index_dtype: DTypeLike) -> Array:
    """Computes the index of the minimum element along ``axis``."""
def argmax(operand: ArrayLike, axis: int, index_dtype: DTypeLike) -> Array:
    """Computes the index of the maximum element along ``axis``."""
def reduce(operands: Any, init_values: Any, computation: Callable[[Any, Any], Any], dimensions: Sequence[int]) -> Any:
    """Wraps XLA's `Reduce
  <https://www.tensorflow.org/xla/operation_semantics#reduce>`_
  operator.

  ``init_values`` and ``computation`` together must form a `monoid
  <https://en.wikipedia.org/wiki/Monoid>`_
  for correctness. That is ``init_values`` must be an identity of
  ``computation``, and ``computation`` must be associative. XLA may exploit both
  of these properties during code generation; if either is violated the result
  is undefined.
  """
@overload
def sort(operand: Array, dimension: int = -1, is_stable: bool = True, num_keys: int = 1) -> Array: ...
@overload
def sort(operand: Sequence[Array], dimension: int = -1, is_stable: bool = True, num_keys: int = 1) -> tuple[Array, ...]: ...
def sort_key_val(keys: Array, values: ArrayLike, dimension: int = -1, is_stable: bool = True) -> tuple[Array, Array]:
    """Sorts ``keys`` along ``dimension`` and applies the same permutation to ``values``."""
def top_k(operand: ArrayLike, k: int) -> tuple[Array, Array]:
    """Returns top ``k`` values and their indices along the last axis of ``operand``.

  Args:
    operand: N-dimensional array of non-complex type.
    k: integer specifying the number of top entries.

  Returns:
    values: array containing the top k values along the last axis.
    indices: array containing the indices corresponding to values.

  See also:
  - :func:`jax.lax.approx_max_k`
  - :func:`jax.lax.approx_min_k`
  """
def tie_in(x: Any, y: T) -> T:
    """Deprecated. Ignores ``x`` and returns ``y``."""
def full(shape: Shape, fill_value: ArrayLike, dtype: DTypeLike | None = None) -> Array:
    """Returns an array of `shape` filled with `fill_value`.

  Args:
    shape: sequence of integers, describing the shape of the output array.
    fill_value: the value to fill the new array with.
    dtype: the type of the output array, or `None`. If not `None`, `fill_value`
      will be cast to `dtype`.
  """
def zeros_like_shaped_array(aval: ShapedArray) -> Array: ...
def iota(dtype: DTypeLike, size: int) -> Array:
    """Wraps XLA's `Iota
  <https://www.tensorflow.org/xla/operation_semantics#iota>`_
  operator.
  """
def broadcasted_iota(dtype: DTypeLike, shape: Shape, dimension: int) -> Array:
    """Convenience wrapper around ``iota``."""
def stop_gradient(x: T) -> T:
    """Stops gradient computation.

  Operationally ``stop_gradient`` is the identity function, that is, it returns
  argument `x` unchanged. However, ``stop_gradient`` prevents the flow of
  gradients during forward or reverse-mode automatic differentiation. If there
  are multiple nested gradient computations, ``stop_gradient`` stops gradients
  for all of them.

  For example:

  >>> jax.grad(lambda x: x**2)(3.)
  Array(6., dtype=float32, weak_type=True)
  >>> jax.grad(lambda x: jax.lax.stop_gradient(x)**2)(3.)
  Array(0., dtype=float32, weak_type=True)
  >>> jax.grad(jax.grad(lambda x: x**2))(3.)
  Array(2., dtype=float32, weak_type=True)
  >>> jax.grad(jax.grad(lambda x: jax.lax.stop_gradient(x)**2))(3.)
  Array(0., dtype=float32, weak_type=True)
  """
def reduce_precision(operand: float | ArrayLike, exponent_bits: int, mantissa_bits: int) -> Array:
    """Wraps XLA's `ReducePrecision
  <https://www.tensorflow.org/xla/operation_semantics#reduceprecision>`_
  operator.
  """
def squeeze(array: ArrayLike, dimensions: Sequence[int]) -> Array:
    """Squeeze any number of size 1 dimensions from an array."""
def expand_dims(array: ArrayLike, dimensions: Sequence[int]) -> Array:
    """Insert any number of size 1 dimensions into an array."""
def full_like(x: ArrayLike | DuckTypedArray, fill_value: ArrayLike, dtype: DTypeLike | None = None, shape: Shape | None = None) -> Array:
    """Create a full array like np.full based on the example array `x`.

  Args:
    x: example array-like, used for shape and dtype information.
    fill_value: a scalar value to fill the entries of the output array.
    dtype: optional, a dtype parameter for the output ndarray.
    shape: optional, a shape parameter for the output ndarray.

  Returns:
    An ndarray with the same shape as `x` with its entries set equal to
    `fill_value`, similar to the output of np.full.
  """
def collapse(operand: Array, start_dimension: int, stop_dimension: int | None = None) -> Array:
    """Collapses dimensions of an array into a single dimension.

  For example, if ``operand`` is an array with shape ``[2, 3, 4]``,
  ``collapse(operand, 0, 2).shape == [6, 4]``. The elements of the collapsed
  dimension are laid out major-to-minor, i.e., with the lowest-numbered
  dimension as the slowest varying dimension.

  Args:
    operand: an input array.
    start_dimension: the start of the dimensions to collapse (inclusive).
    stop_dimension: the end of the dimensions to collapse (exclusive). Pass None
      to collapse all the dimensions after start.

  Returns:
    An array where dimensions ``[start_dimension, stop_dimension)`` have been
    collapsed (raveled) into a single dimension.
  """
def batch_matmul(lhs: Array, rhs: Array, precision: PrecisionLike = None) -> Array:
    """Batch matrix multiplication."""
def square(x: ArrayLike) -> Array:
    """Elementwise square: :math:`x^2`."""
def reciprocal(x: ArrayLike) -> Array:
    """Elementwise reciprocal: :math:`1 \\over x`."""
def tan(x: ArrayLike) -> Array:
    """Elementwise tangent: :math:`\\mathrm{tan}(x)`."""
def asin(x: ArrayLike) -> Array:
    """Elementwise arc sine: :math:`\\mathrm{asin}(x)`."""
def acos(x: ArrayLike) -> Array:
    """Elementwise arc cosine: :math:`\\mathrm{acos}(x)`."""
def atan(x: ArrayLike) -> Array:
    """Elementwise arc tangent: :math:`\\mathrm{atan}(x)`."""
def sinh(x: ArrayLike) -> Array:
    """Elementwise hyperbolic sine: :math:`\\mathrm{sinh}(x)`."""
def cosh(x: ArrayLike) -> Array:
    """Elementwise hyperbolic cosine: :math:`\\mathrm{cosh}(x)`."""
def asinh(x: ArrayLike) -> Array:
    """Elementwise inverse hyperbolic sine: :math:`\\mathrm{asinh}(x)`."""
def acosh(x: ArrayLike) -> Array:
    """Elementwise inverse hyperbolic cosine: :math:`\\mathrm{acosh}(x)`."""
def atanh(x: ArrayLike) -> Array:
    """Elementwise inverse hyperbolic tangent: :math:`\\mathrm{atanh}(x)`."""
def zeros_like_array(x: ArrayLike) -> Array: ...
def unop_dtype_rule(result_dtype, accepted_dtypes, name, aval, **kwargs): ...
def unop(result_dtype, accepted_dtypes, name): ...

standard_unop: Incomplete

def naryop_dtype_rule(result_dtype, accepted_dtypes, name, *avals, require_same: bool = True, allow_extended_dtype: bool = False, **kwargs): ...
def broadcasting_shape_rule(name, *avals): ...
def naryop(result_dtype, accepted_dtypes, name, allow_extended_dtype: bool = False, require_same_dtypes: bool = False): ...

standard_naryop: Incomplete

def broadcast_hlo(aval_out: core.ShapedArray, avals: Sequence[core.ShapedArray], args: Sequence[ir.Value]) -> Sequence[ir.Value]:
    """Broadcasts HLO values with broadcast-compatible shapes to the same shape.
  """

neg_p: Incomplete
sign_p: Incomplete
nextafter_p: Incomplete
floor_p: Incomplete
ceil_p: Incomplete
round_p: Incomplete
is_finite_p: Incomplete
exp_p: Incomplete
exp2_p: Incomplete
log_p: Incomplete
expm1_p: Incomplete
log1p_p: Incomplete
tanh_p: Incomplete
logistic_p: Incomplete

def logistic_impl(x): ...

sin_p: Incomplete
cos_p: Incomplete
tan_p: Incomplete

def asin_impl(x): ...

asin_p: Incomplete

def acos_impl(x): ...

acos_p: Incomplete

def atan_impl(x): ...

atan_p: Incomplete
atan2_p: Incomplete
sinh_p: Incomplete
cosh_p: Incomplete
asinh_p: Incomplete
acosh_p: Incomplete
atanh_p: Incomplete
real_p: Incomplete
imag_p: Incomplete
complex_p: Incomplete
conj_p: Incomplete
abs_p: Incomplete
sqrt_p: Incomplete
rsqrt_p: Incomplete
cbrt_p: Incomplete
pow_p: Incomplete
integer_pow_p: Incomplete
not_p: Incomplete
and_p: Incomplete
or_p: Incomplete
xor_p: Incomplete
population_count_p: Incomplete
clz_p: Incomplete
add_p: Primitive
sub_p: Incomplete
mul_p: Incomplete
div_p: Incomplete
rem_p: Incomplete
max_p: core.Primitive
min_p: core.Primitive
shift_left_p: Incomplete
shift_right_arithmetic_p: Incomplete
shift_right_logical_p: Incomplete
eq_p: Incomplete
ne_p: Incomplete
ge_p: Incomplete
gt_p: Incomplete
le_p: Incomplete
lt_p: Incomplete
convert_element_type_p: Incomplete
bitcast_convert_type_p: Incomplete

def tuple_delete(tup, idx): ...

dot_general_p: Incomplete

def precision_attr(precision: PrecisionType) -> ir.ArrayAttr: ...

broadcast_in_dim_p: Incomplete
clamp_p: Incomplete
concatenate_p: Incomplete
pad_p: Incomplete
squeeze_p: Incomplete

def shape_as_value(shape: core.Shape):
    """Converts a shape that may contain Poly values into a JAX value."""

reshape_p: Incomplete
rev_p: Incomplete
transpose_p: Incomplete
select_n_p: Incomplete
reduce_p: Incomplete
reduce_sum_p: Incomplete
reduce_prod_p: Incomplete
reduce_max_p: Incomplete
reduce_min_p: Incomplete
argmin_p: Incomplete
argmax_p: Incomplete
reduce_or_p: Incomplete
reduce_and_p: Incomplete
reduce_xor_p: Incomplete
reduce_precision_p: Incomplete
sort_p: Incomplete
top_k_p: Incomplete

def create_token(_: Incomplete | None = None):
    """Creates an XLA token value with no preconditions for sequencing effects.

  Experimental.

  The argument is ignored. It exists for backward compatibility.
  """

create_token_p: Incomplete

def after_all(*operands):
    """Merges one or more XLA token values. Experimental.

  Wraps the XLA AfterAll operator."""

after_all_p: Incomplete

class InOutFeedEffect(effects.Effect): ...

infeed_effect: Incomplete
outfeed_effect: Incomplete

def infeed(token, shape: Incomplete | None = None, partitions: Incomplete | None = None):
    """Consumes an infeed value of `shape` from the host. Experimental.

  `token` is used to sequence infeed and outfeed effects.
  `partitions` may be specified inside a `sharded_jit` function.
  """

infeed_p: Incomplete

def outfeed(token, xs, partitions: Incomplete | None = None):
    """Outfeeds value `xs` to the host. Experimental.

  `token` is used to sequence infeed and outfeed effects.
  `partitions` may be specified inside a `sharded_jit` or `pjit` function.
  """

outfeed_p: Incomplete

def rng_uniform(a, b, shape):
    """Stateful PRNG generator. Experimental and its use is discouraged.

  Returns uniformly distributed random numbers in the range [a, b)

  You should use jax.random for most purposes; this function exists only for
  niche use cases with special performance requirements.

  This API may be removed at any time.
  """

rng_uniform_p: Incomplete
RandomAlgorithm: Incomplete
rng_bit_generator_p: Incomplete
copy_p: Incomplete

def rng_bit_generator(key, shape, dtype=..., algorithm=...):
    """Stateless PRNG bit generator. Experimental and its use is discouraged.

  Returns uniformly distributed random bits with the specified shape and dtype
  (what is required to be an integer type) using the platform specific
  default algorithm or the one specified.

  It provides direct access to the RngBitGenerator primitive exposed by XLA
  (https://www.tensorflow.org/xla/operation_semantics#rngbitgenerator) for low
  level API access.

  Most users should use `jax.random` instead for a stable and more user
  friendly API.
  """

iota_p: Incomplete

class PaddingType(enum.Enum):
    VALID: int
    SAME: int
    SAME_LOWER: int

def padtype_to_pads(in_shape, window_shape, window_strides, padding):
    """Convert padding string to list of pairs of pad values."""
def check_same_dtypes(name: str, *avals: core.UnshapedArray) -> None:
    """Check that dtypes agree, possibly ignoring float precision."""

dtype: Callable

def ranges_like(*xs) -> Generator[Incomplete, None, None]: ...
def remaining(original, *removed_lists): ...
def canonicalize_precision(precision: PrecisionLike) -> tuple[PrecisionType, PrecisionType] | None:
    """Turns an API precision specification, into a pair of enumeration values.

  The API can take the precision as a string, or int, and either as a single
  value to apply to both operands, or as a sequence of two values.
  """
def empty(dtype): ...

empty_p: Incomplete
tie_p: Incomplete

class BIntRules:
    @staticmethod
    def physical_element_aval(dtype) -> core.ShapedArray: ...
    @staticmethod
    def result_handler(sticky_device, aval): ...
    @staticmethod
    def global_sharded_result_handler(aval, out_sharding, committed, is_out_sharding_from_xla): ...
    @staticmethod
    def physical_hlo_sharding(aval, hlo_sharding: xc.HloSharding) -> xc.HloSharding: ...
