from _typeshed import Incomplete
from jax import config as config
from jax._src import ad_checkpoint as ad_checkpoint, ad_util as ad_util, api as api, core as core, dispatch as dispatch, dtypes as dtypes, effects as effects, source_info_util as source_info_util, state as state, util as util
from jax._src.api_util import shaped_abstractify as shaped_abstractify
from jax._src.core import ConcreteArray as ConcreteArray, ShapedArray as ShapedArray, raise_to_shaped as raise_to_shaped
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, xla as xla
from jax._src.lax import lax as lax, slicing as slicing, windowed_reductions as windowed_reductions
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.numpy.ufuncs import logaddexp as logaddexp
from jax._src.traceback_util import api_boundary as api_boundary
from jax._src.tree_util import equality_errors as equality_errors
from jax._src.typing import Array as Array
from jax._src.util import merge_lists as merge_lists, partition_list as partition_list, safe_map as safe_map, safe_zip as safe_zip, split_list as split_list, unzip2 as unzip2, weakref_lru_cache as weakref_lru_cache
from jax.tree_util import keystr as keystr, tree_flatten as tree_flatten, tree_flatten_with_path as tree_flatten_with_path, tree_map as tree_map, tree_unflatten as tree_unflatten, treedef_is_leaf as treedef_is_leaf
from typing import Any, Callable, TypeVar

zip = safe_zip
T = TypeVar('T')
BooleanNumeric = Any
Carry = TypeVar('Carry')
X = TypeVar('X')
Y = TypeVar('Y')

def scan(f: Callable[[Carry, X], tuple[Carry, Y]], init: Carry, xs: X, length: int | None = None, reverse: bool = False, unroll: int = 1) -> tuple[Carry, Y]:
    """Scan a function over leading array axes while carrying along state.

  The `Haskell-like type signature`_ in brief is

  .. code-block:: haskell

    scan :: (c -> a -> (c, b)) -> c -> [a] -> (c, [b])

  where for any array type specifier ``t``, ``[t]`` represents the type with an additional
  leading axis, and if ``t`` is a pytree (container) type with array leaves then ``[t]``
  represents the type with the same pytree structure and corresponding leaves
  each with an additional leading axis.

  When the type of ``xs`` (denoted `a` above) is an array type or None, and the type
  of ``ys`` (denoted `b` above) is an array type, the semantics of :func:`~scan` are
  given roughly by this Python implementation::

    def scan(f, init, xs, length=None):
      if xs is None:
        xs = [None] * length
      carry = init
      ys = []
      for x in xs:
        carry, y = f(carry, x)
        ys.append(y)
      return carry, np.stack(ys)

  Unlike that Python version, both ``xs`` and ``ys`` may be arbitrary pytree
  values, and so multiple arrays can be scanned over at once and produce multiple
  output arrays. ``None`` is actually a special case of this, as it represents an
  empty pytree.

  Also unlike that Python version, :func:`~scan` is a JAX primitive and is
  lowered to a single WhileOp. That makes it useful for reducing
  compilation times for JIT-compiled functions, since native Python
  loop constructs in an :func:`~jax.jit` function are unrolled, leading to large
  XLA computations.

  Finally, the loop-carried value ``carry`` must hold a fixed shape and dtype
  across all iterations (and not just be consistent up to NumPy rank/shape
  broadcasting and dtype promotion rules, for example). In other words, the type
  ``c`` in the type signature above represents an array with a fixed shape and
  dtype (or a nested tuple/list/dict container data structure with a fixed
  structure and arrays with fixed shape and dtype at the leaves).

  .. note::
    :py:func:`scan` compiles ``f``, so while it can be combined with
    :py:func:`jit`, it's usually unnecessary.

  Args:
    f: a Python function to be scanned of type ``c -> a -> (c, b)``, meaning
      that ``f`` accepts two arguments where the first is a value of the loop
      carry and the second is a slice of ``xs`` along its leading axis, and that
      ``f`` returns a pair where the first element represents a new value for
      the loop carry and the second represents a slice of the output.
    init: an initial loop carry value of type ``c``, which can be a scalar,
      array, or any pytree (nested Python tuple/list/dict) thereof, representing
      the initial loop carry value. This value must have the same structure as
      the first element of the pair returned by ``f``.
    xs: the value of type ``[a]`` over which to scan along the leading axis,
      where ``[a]`` can be an array or any pytree (nested Python
      tuple/list/dict) thereof with consistent leading axis sizes.
    length: optional integer specifying the number of loop iterations, which
      must agree with the sizes of leading axes of the arrays in ``xs`` (but can
      be used to perform scans where no input ``xs`` are needed).
    reverse: optional boolean specifying whether to run the scan iteration
      forward (the default) or in reverse, equivalent to reversing the leading
      axes of the arrays in both ``xs`` and in ``ys``.
    unroll: optional positive int specifying, in the underlying operation of the
      scan primitive, how many scan iterations to unroll within a single
      iteration of a loop.

  Returns:
    A pair of type ``(c, [b])`` where the first element represents the final
    loop carry value and the second element represents the stacked outputs of
    the second output of ``f`` when scanned over the leading axis of the inputs.

  .. _Haskell-like type signature: https://wiki.haskell.org/Type_signature
  """
def scan_bind(*args, **params): ...

scan_p: Incomplete

def while_loop(cond_fun: Callable[[T], BooleanNumeric], body_fun: Callable[[T], T], init_val: T) -> T:
    """Call ``body_fun`` repeatedly in a loop while ``cond_fun`` is True.

  The `Haskell-like type signature`_ in brief is

  .. code-block:: haskell

    while_loop :: (a -> Bool) -> (a -> a) -> a -> a

  The semantics of ``while_loop`` are given by this Python implementation::

    def while_loop(cond_fun, body_fun, init_val):
      val = init_val
      while cond_fun(val):
        val = body_fun(val)
      return val

  Unlike that Python version, ``while_loop`` is a JAX primitive and is lowered
  to a single WhileOp. That makes it useful for reducing compilation times
  for jit-compiled functions, since native Python loop constructs in an ``@jit``
  function are unrolled, leading to large XLA computations.

  Also unlike the Python analogue, the loop-carried value ``val`` must hold a
  fixed shape and dtype across all iterations (and not just be consistent up to
  NumPy rank/shape broadcasting and dtype promotion rules, for example). In
  other words, the type ``a`` in the type signature above represents an array
  with a fixed shape and dtype (or a nested tuple/list/dict container data
  structure with a fixed structure and arrays with fixed shape and dtype at the
  leaves).

  Another difference from using Python-native loop constructs is that
  ``while_loop`` is not reverse-mode differentiable because XLA computations
  require static bounds on memory requirements.

  .. note::
    :py:func:`while_loop` compiles ``cond_fun`` and ``body_fun``, so while it
    can be combined with :py:func:`jit`, it's usually unnecessary.

  Args:
    cond_fun: function of type ``a -> Bool``.
    body_fun: function of type ``a -> a``.
    init_val: value of type ``a``, a type that can be a scalar, array, or any
      pytree (nested Python tuple/list/dict) thereof, representing the initial
      loop carry value.

  Returns:
    The output from the final iteration of body_fun, of type ``a``.

  .. _Haskell-like type signature: https://wiki.haskell.org/Type_signature
  """

while_p: Incomplete

def fori_loop(lower, upper, body_fun, init_val):
    """Loop from ``lower`` to ``upper`` by reduction to :func:`jax.lax.while_loop`.

  The `Haskell-like type signature`_ in brief is

  .. code-block:: haskell

    fori_loop :: Int -> Int -> ((Int, a) -> a) -> a -> a

  The semantics of ``fori_loop`` are given by this Python implementation::

    def fori_loop(lower, upper, body_fun, init_val):
      val = init_val
      for i in range(lower, upper):
        val = body_fun(i, val)
      return val

  As the Python version suggests, setting ``upper <= lower`` will produce no
  iterations. Negative or custom increments are not supported.

  Unlike that Python version, ``fori_loop`` is implemented in terms of either a
  call to :func:`jax.lax.while_loop` or a call to :func:`jax.lax.scan`. If the
  trip count is static (meaning known at tracing time, perhaps because ``lower``
  and ``upper`` are Python integer literals) then the ``fori_loop`` is
  implemented in terms of :func:`~scan` and reverse-mode autodiff is supported;
  otherwise, a ``while_loop`` is used and reverse-mode autodiff is not
  supported.  See those functions' docstrings for more information.

  Also unlike the Python analogue, the loop-carried value ``val`` must hold a
  fixed shape and dtype across all iterations (and not just be consistent up to
  NumPy rank/shape broadcasting and dtype promotion rules, for example). In
  other words, the type ``a`` in the type signature above represents an array
  with a fixed shape and dtype (or a nested tuple/list/dict container data
  structure with a fixed structure and arrays with fixed shape and dtype at the
  leaves).

  .. note::
    :py:func:`fori_loop` compiles ``body_fun``, so while it can be combined with
    :py:func:`jit`, it's usually unnecessary.

  Args:
    lower: an integer representing the loop index lower bound (inclusive)
    upper: an integer representing the loop index upper bound (exclusive)
    body_fun: function of type ``(int, a) -> a``.
    init_val: initial loop carry value of type ``a``.

  Returns:
    Loop value from the final iteration, of type ``a``.

  .. _Haskell-like type signature: https://wiki.haskell.org/Type_signature
  """
def map(f, xs):
    """Map a function over leading array axes.

  Like Python's builtin map, except inputs and outputs are in the form of
  stacked arrays. Consider using the :func:`~jax.vmap` transform instead, unless you
  need to apply a function element by element for reduced memory usage or
  heterogeneous computation with other control flow primitives.

  When ``xs`` is an array type, the semantics of :func:`~map` are given by this
  Python implementation::

    def map(f, xs):
      return np.stack([f(x) for x in xs])

  Like :func:`~scan`, :func:`~map` is implemented in terms of JAX primitives so
  many of the same advantages over a Python loop apply: ``xs`` may be an
  arbitrary nested pytree type, and the mapped computation is compiled only
  once.

  Args:
    f: a Python function to apply element-wise over the first axis or axes of
      ``xs``.
    xs: values over which to map along the leading axis.

  Returns:
    Mapped values.
  """
def associative_scan(fn: Callable, elems, reverse: bool = False, axis: int = 0):
    '''Performs a scan with an associative binary operation, in parallel.

  For an introduction to associative scans, see [BLE1990]_.

  Args:
    fn: A Python callable implementing an associative binary operation with
      signature ``r = fn(a, b)``. Function `fn` must be associative, i.e., it
      must satisfy the equation
      ``fn(a, fn(b, c)) == fn(fn(a, b), c)``.

      The inputs and result are (possibly nested Python tree structures of)
      array(s) matching ``elems``. Each array has a dimension in place
      of the ``axis`` dimension. `fn` should be applied elementwise over
      the ``axis`` dimension (for example, by using :func:`jax.vmap` over the
      elementwise function.)

      The result ``r`` has the same shape (and structure) as the two inputs
      ``a`` and ``b``.
    elems: A (possibly nested Python tree structure of) array(s), each with
      an ``axis`` dimension of size ``num_elems``.
    reverse: A boolean stating if the scan should be reversed with respect to
      the ``axis`` dimension.
    axis: an integer identifying the axis over which the scan should occur.

  Returns:
    A (possibly nested Python tree structure of) array(s) of the same shape
    and structure as ``elems``, in which the ``k``\'th element of ``axis`` is the
    result of recursively applying ``fn`` to combine the first ``k`` elements
    of ``elems`` along ``axis``. For example, given ``elems = [a, b, c, ...]``,
    the result would be ``[a, fn(a, b), fn(fn(a, b), c), ...]``.

  Example 1: partial sums of an array of numbers:

  >>> lax.associative_scan(jnp.add, jnp.arange(0, 4))
  Array([0, 1, 3, 6], dtype=int32)

  Example 2: partial products of an array of matrices

  >>> mats = jax.random.uniform(jax.random.PRNGKey(0), (4, 2, 2))
  >>> partial_prods = lax.associative_scan(jnp.matmul, mats)
  >>> partial_prods.shape
  (4, 2, 2)

  Example 3: reversed partial sums of an array of numbers

  >>> lax.associative_scan(jnp.add, jnp.arange(0, 4), reverse=True)
  Array([6, 6, 5, 3], dtype=int32)

  .. [BLE1990] Blelloch, Guy E. 1990. "Prefix Sums and Their Applications.",
    Technical Report CMU-CS-90-190, School of Computer Science, Carnegie Mellon
    University.
  '''
def cumsum(operand: Array, axis: int = 0, reverse: bool = False) -> Array:
    """Computes a cumulative sum along `axis`."""
def cumprod(operand: Array, axis: int = 0, reverse: bool = False) -> Array:
    """Computes a cumulative product along `axis`."""
def cummax(operand: Array, axis: int = 0, reverse: bool = False) -> Array:
    """Computes a cumulative maximum along `axis`."""
def cummin(operand: Array, axis: int = 0, reverse: bool = False) -> Array:
    """Computes a cumulative minimum along `axis`."""
def cumlogsumexp(operand: Array, axis: int = 0, reverse: bool = False) -> Array:
    """Computes a cumulative logsumexp along `axis`."""
def cumred_reduce_window_impl(window_reduce: Callable, x, *, axis: int, reverse: bool): ...
def cumred_gpu_impl(window_reduce: Callable, reduce_fn: Callable, x, *, axis: int, reverse: bool): ...

cumsum_p: Incomplete
cumlogsumexp_p: Incomplete
cumprod_p: Incomplete
cummax_p: Incomplete
cummin_p: Incomplete
