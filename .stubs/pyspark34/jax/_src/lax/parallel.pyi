from _typeshed import Incomplete
from jax import tree_util as tree_util
from jax._src import core as core, dtypes as dtypes, sharding_impls as sharding_impls, util as util
from jax._src.core import AxisName as AxisName, ShapedArray as ShapedArray, raise_to_shaped as raise_to_shaped
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir, pxla as pxla
from jax._src.lax import lax as lax, slicing as slicing
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.numpy import lax_numpy as lax_numpy
from jax._src.util import canonicalize_axis as canonicalize_axis, moveaxis as moveaxis, safe_map as safe_map, safe_zip as safe_zip, unzip2 as unzip2

unsafe_map: Incomplete
map: Incomplete

def psum(x, axis_name, *, axis_index_groups: Incomplete | None = None):
    """Compute an all-reduce sum on ``x`` over the pmapped axis ``axis_name``.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  Inputs of boolean dtype are converted to integers before the reduction.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would perform psums over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once.

  Returns:
    Array(s) with the same shape as ``x`` representing the result of an
    all-reduce sum along the axis ``axis_name``.

  Examples:
    For example, with 4 XLA devices available:

    >>> x = np.arange(4)
    >>> y = jax.pmap(lambda x: jax.lax.psum(x, 'i'), axis_name='i')(x)
    >>> print(y)
    [6 6 6 6]
    >>> y = jax.pmap(lambda x: x / jax.lax.psum(x, 'i'), axis_name='i')(x)
    >>> print(y)
    [0.         0.16666667 0.33333334 0.5       ]

    Suppose we want to perform ``psum`` among two groups, one with ``device0`` and ``device1``, the other with `device2` and `device3`,

    >>> y = jax.pmap(lambda x: jax.lax.psum(x, 'i', axis_index_groups=[[0, 1], [2, 3]]), axis_name='i')(x)
    >>> print(y)
    [1 1 5 5]

    An example using 2D-shaped x. Each row is data from one device.

    >>> x = np.arange(16).reshape(4, 4)
    >>> print(x)
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]]

    Full ``psum`` across all devices:

    >>> y = jax.pmap(lambda x: jax.lax.psum(x, 'i'), axis_name='i')(x)
    >>> print(y)
    [[24 28 32 36]
     [24 28 32 36]
     [24 28 32 36]
     [24 28 32 36]]

    Perform ``psum`` among two groups:

    >>> y = jax.pmap(lambda x: jax.lax.psum(x, 'i', axis_index_groups=[[0, 1], [2, 3]]), axis_name='i')(x)
    >>> print(y)
    [[ 4  6  8 10]
     [ 4  6  8 10]
     [20 22 24 26]
     [20 22 24 26]]
  """
def pmean(x, axis_name, *, axis_index_groups: Incomplete | None = None):
    """Compute an all-reduce mean on ``x`` over the pmapped axis ``axis_name``.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would perform pmeans over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once, and on TPUs all groups must be the same size.

  Returns:
    Array(s) with the same shape as ``x`` representing the result of an
    all-reduce mean along the axis ``axis_name``.

  For example, with 4 XLA devices available:

  >>> x = np.arange(4)
  >>> y = jax.pmap(lambda x: jax.lax.pmean(x, 'i'), axis_name='i')(x)
  >>> print(y)
  [1.5 1.5 1.5 1.5]
  >>> y = jax.pmap(lambda x: x / jax.lax.pmean(x, 'i'), axis_name='i')(x)
  >>> print(y)
  [0.        0.6666667 1.3333334 2.       ]
  """
def pmax(x, axis_name, *, axis_index_groups: Incomplete | None = None):
    """Compute an all-reduce max on ``x`` over the pmapped axis ``axis_name``.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would perform pmaxes over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once, and on TPUs all groups must be the same size.

  Returns:
    Array(s) with the same shape as ``x`` representing the result of an
    all-reduce max along the axis ``axis_name``.
  """
def pmin(x, axis_name, *, axis_index_groups: Incomplete | None = None):
    """Compute an all-reduce min on ``x`` over the pmapped axis ``axis_name``.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would perform pmins over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once, and on TPUs all groups must be the same size.

  Returns:
    Array(s) with the same shape as ``x`` representing the result of an
    all-reduce min along the axis ``axis_name``.
  """
def pargmin(x, axis_name): ...
def pargmax(x, axis_name): ...
def ppermute(x, axis_name, perm):
    """Perform a collective permutation according to the permutation ``perm``.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  This function is an analog of the CollectivePermute HLO.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    perm: list of pairs of ints, representing
      ``(source_index, destination_index)``
      pairs that encode how the mapped axis named ``axis_name`` should be
      shuffled. The integer values are treated as indices into the mapped axis
      ``axis_name``. Any two pairs should not have the same source index or the
      same destination index. For each index of the axis ``axis_name`` that does
      not correspond to a destination index in ``perm``, the corresponding
      values in the result are filled with zeros of the appropriate type.

  Returns:
    Array(s) with the same shape as ``x`` with slices along the axis
    ``axis_name`` gathered from ``x`` according to the permutation ``perm``.
  """
def pshuffle(x, axis_name, perm):
    """Convenience wrapper of jax.lax.ppermute with alternate permutation encoding

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    perm: list of of ints encoding sources for the permutation to be applied to
      the axis named ``axis_name``, so that the output at axis index i
      comes from the input at axis index perm[i]. Every integer in [0, N) should
      be included exactly once for axis size N.

  Returns:
    Array(s) with the same shape as ``x`` with slices along the axis
    ``axis_name`` gathered from ``x`` according to the permutation ``perm``.
  """
def pswapaxes(x, axis_name, axis, *, axis_index_groups: Incomplete | None = None):
    """Swap the pmapped axis ``axis_name`` with the unmapped axis ``axis``.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  The group size of the mapped axis size must be equal to the size of the
  unmapped axis; that is, we must have
  ``lax.psum(1, axis_name, axis_index_groups=axis_index_groups) == x.shape[axis]``.
  By default, when ``axis_index_groups=None``, this encompasses all the devices.

  This function is a special case of ``all_to_all`` where the pmapped axis of
  the input is placed at the position ``axis`` in the output. That is, it is
  equivalent to ``all_to_all(x, axis_name, axis, axis)``.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    axis: int indicating the unmapped axis of ``x`` to map with the name
      ``axis_name``.
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would run pswapaxes over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once, and all groups must be the same size.

  Returns:
    Array(s) with the same shape as ``x``.
  """
def all_to_all(x, axis_name, split_axis, concat_axis, *, axis_index_groups: Incomplete | None = None, tiled: bool = False):
    """Materialize the mapped axis and map a different axis.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  In the output, the input mapped axis ``axis_name`` is materialized at the
  logical axis position ``concat_axis``, and the input unmapped axis at position
  ``split_axis`` is mapped with the name ``axis_name``.

  The group size of the mapped axis size must be equal to the size of the
  unmapped axis; that is, we must have
  ``lax.psum(1, axis_name, axis_index_groups=axis_index_groups) == x.shape[axis]``.
  By default, when ``axis_index_groups=None``, this encompasses all the devices.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    split_axis: int indicating the unmapped axis of ``x`` to map with the name
      ``axis_name``.
    concat_axis: int indicating the position in the output to materialize the
      mapped axis of the input with the name ``axis_name``.
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would run all_to_all over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once, and all groups must be the same size.
    tiled: when True, all_to_all will divide split_axis into chunks and concatenate
      them along concat_axis. In particular, no dimensions are added or removed.
      False by default.

  Returns:
    When tiled is False, array(s) with shape given by the expression::

      np.insert(np.delete(x.shape, split_axis), concat_axis, axis_size)

    where ``axis_size`` is the size of the mapped axis named ``axis_name`` in
    the input ``x``, i.e. ``axis_size = lax.psum(1, axis_name)``.

    Otherwise array with shape similar to the input shape, except with split_axis
    divided by axis size and concat_axis multiplied by axis size.
  """
def axis_index(axis_name):
    """Return the index along the mapped axis ``axis_name``.

  Args:
    axis_name: hashable Python object used to name the mapped axis.

  Returns:
    An integer representing the index.

  For example, with 8 XLA devices available:

  >>> from functools import partial
  >>> @partial(jax.pmap, axis_name='i')
  ... def f(_):
  ...   return lax.axis_index('i')
  ...
  >>> f(np.zeros(4))
  Array([0, 1, 2, 3], dtype=int32)
  >>> f(np.zeros(8))
  Array([0, 1, 2, 3, 4, 5, 6, 7], dtype=int32)
  >>> @partial(jax.pmap, axis_name='i')
  ... @partial(jax.pmap, axis_name='j')
  ... def f(_):
  ...   return lax.axis_index('i'), lax.axis_index('j')
  ...
  >>> x, y = f(np.zeros((4, 2)))
  >>> print(x)
  [[0 0]
  [1 1]
  [2 2]
  [3 3]]
  >>> print(y)
  [[0 1]
  [0 1]
  [0 1]
  [0 1]]
  """
def pdot(x, y, axis_name, pos_contract=((), ()), pos_batch=((), ()), precision: Incomplete | None = None): ...
def xeinsum(spec: str, *operands): ...

class XeinsumSpecParser:
    spec: str
    pos: int
    def __init__(self, spec: str) -> None: ...
    @property
    def eof(self): ...
    @property
    def cur(self): ...
    def parse_subscript(self): ...
    def parse_axis_name(self): ...
    def maybe_take(self, char: str, on_eof: bool = False): ...
    def parse_arg(self): ...
    def parse_args(self): ...

def pgather(src, idx, axes: int | AxisName):
    """Uses the last positional axis of idx to index into src's axes."""

psum_p: Incomplete

def psum_bind(*args, axes, axis_index_groups): ...

pmax_p: Incomplete
pmin_p: Incomplete
ppermute_p: Incomplete
all_to_all_p: Incomplete

def all_gather(x, axis_name, *, axis_index_groups: Incomplete | None = None, axis: int = 0, tiled: bool = False):
    """Gather values of x across all replicas.

  If ``x`` is a pytree then the result is equivalent to mapping this function to
  each leaf in the tree.

  This is equivalent to, but faster than, all_to_all(broadcast(x)).

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would run all gather over the first
      two and last two replicas). Groups must cover all axis indices exactly
      once, and all groups must be the same size.
    axis: a positional axis into which the chunks along ``axis_name`` will be
      concatenated.
    tiled: when ``False``, the chunks will be stacked into a fresh positional
      axis at index ``axis`` in the output. When ``True``, ``axis`` has to
      refer to an existing positional dimension and the chunks will be
      concatenated into that dimension.

  Returns:
    Array(s) representing the result of an all-gather along the axis
    ``axis_name``. Shapes are the same as ``x.shape``, but:

    - when ``tiled`` is ``False``, there is a new dimension equal to the
      size of axis ``axis_name`` in position ``axis``,
    - when ``tiled`` is ``True``, the size of dimension in position ``axis``
      is multiplied by the size of axis ``axis_name``.

  For example, with 4 XLA devices available:

  >>> x = np.arange(4)
  >>> y = jax.pmap(lambda x: jax.lax.all_gather(x, 'i'), axis_name='i')(x)
  >>> print(y)
  [[0 1 2 3]
   [0 1 2 3]
   [0 1 2 3]
   [0 1 2 3]]

  An example of using axis_index_groups, groups split by even & odd device ids:

  >>> x = np.arange(16).reshape(4, 4)
  >>> print(x)
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]]
  >>> def f(x):
  ...   return jax.lax.all_gather(
  ...       x, 'i', axis_index_groups=[[0, 2], [3, 1]])
  >>> y = jax.pmap(f, axis_name='i')(x)
  >>> print(y)
  [[[ 0  1  2  3]
    [ 8  9 10 11]]
   [[12 13 14 15]
    [ 4  5  6  7]]
   [[ 0  1  2  3]
    [ 8  9 10 11]]
   [[12 13 14 15]
    [ 4  5  6  7]]]
  """

all_gather_p: Incomplete
reduce_scatter_p: Incomplete

def psum_scatter(x, axis_name, *, scatter_dimension: int = 0, axis_index_groups: Incomplete | None = None, tiled: bool = False):
    """Compute an all-reduce sum over the axis ``axis_name``, and scatter the result.

  Args:
    x: array(s) with a mapped axis named ``axis_name``.
    axis_name: hashable Python object used to name a pmapped axis (see the
      :func:`jax.pmap` documentation for more details).
    scatter_dimension: a positional axis into which the all reduce result along
      ``axis_name`` will be scattered.
    axis_index_groups: optional list of lists containing axis indices (e.g. for
      an axis of size 4, [[0, 1], [2, 3]] would run reduce-scatter over the
      first two and the last two replicas). Groups must cover all axis indices
      exactly once, and all groups must be the same size.
    tiled: when ``False``, the size of dimension in ``scatter_dimension`` must
      match the size of axis ``axis_name`` (or the group size if
      ``axis_index_groups`` is given). After scattering the all reduce result
      along ``scatter_dimension``, the output is sequeezed by removing
      ``scatter_dimension``. When ``True``, the size of dimension in
      ``scatter_dimension` must be dividible by the size of axis ``axis_name``
      (or the group size if ``axis_index_groups`` is given),
      and ``scatter_dimension`` is preserved.

  Returns:
    Array(s) with the similar shape as ``x``, except the size of dimension in
    position``scatter_dimension`` is divided by the size of axis ``axis_name``.

  For example, with 4 XLA devices available:

  >>> x = np.arange(16).reshape(4, 4)
  >>> print(x)
  [[ 0  1  2  3]
   [ 4  5  6  7]
   [ 8  9 10 11]
   [12 13 14 15]]
  >>> y = jax.pmap(lambda x: jax.lax.psum_scatter(x, 'i'), axis_name='i')(x)
  >>> print(y)
  [24 28 32 36]

  if using tiled:

  >>> y = jax.pmap(lambda x: jax.lax.psum_scatter(x, 'i', tiled=True), axis_name='i')(x)
  >>> print(y)
  [[24]
   [28]
   [32]
   [36]]

  An example of using axis_index_groups:

  >>> def f(x):
  ...   return jax.lax.psum_scatter(
  ...       x, 'i', axis_index_groups=[[0, 2], [3, 1]], tiled=True)
  >>> y = jax.pmap(f, axis_name='i')(x)
  >>> print(y)
  [[ 8 10]
   [20 22]
   [12 14]
   [16 18]]
  """

axis_index_p: Incomplete
pdot_p: Incomplete
pgather_p: Incomplete
