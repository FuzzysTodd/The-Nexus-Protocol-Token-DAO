from _typeshed import Incomplete
from collections.abc import Sequence
from jax import config as config, lax as lax, tree_util as tree_util, vmap as vmap
from jax._src import api_util as api_util, core as core, dispatch as dispatch
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lax.lax import DotDimensionNumbers as DotDimensionNumbers, ranges_like as ranges_like, remaining as remaining
from jax._src.lax.slicing import GatherDimensionNumbers as GatherDimensionNumbers, GatherScatterMode as GatherScatterMode
from jax._src.lib import gpu_sparse as gpu_sparse
from jax._src.lib.mlir import ir as ir
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike
from jax._src.util import canonicalize_axis as canonicalize_axis
from jax.experimental.sparse._base import JAXSparse as JAXSparse
from jax.experimental.sparse._lowerings import coo_spmm_p as coo_spmm_p, coo_spmv_p as coo_spmv_p
from jax.experimental.sparse.util import CuSparseEfficiencyWarning as CuSparseEfficiencyWarning, Shape as Shape, SparseEfficiencyError as SparseEfficiencyError, SparseEfficiencyWarning as SparseEfficiencyWarning, SparseInfo as SparseInfo, nfold_vmap as nfold_vmap
from jax.util import safe_zip as safe_zip, split_list as split_list, unzip2 as unzip2
from typing import Any, NamedTuple, Protocol

CUSPARSE_DATA_DTYPES: Incomplete
CUSPARSE_INDEX_DTYPES: Incomplete

def bcoo_eliminate_zeros(mat: BCOO, nse: int | None = None) -> BCOO: ...

class BCOOProperties(NamedTuple):
    n_batch: int
    n_sparse: int
    n_dense: int
    nse: int

class Buffer(Protocol):
    @property
    def shape(self) -> Shape: ...
    @property
    def dtype(self) -> Any: ...

bcoo_todense_p: Incomplete

def bcoo_todense(mat: BCOO) -> Array:
    """Convert batched sparse matrix to a dense matrix.

  Args:
    mat: BCOO matrix.

  Returns:
    mat_dense: dense version of ``mat``.
  """

bcoo_fromdense_p: Incomplete

def bcoo_fromdense(mat: Array, *, nse: int | None = None, n_batch: int = 0, n_dense: int = 0, index_dtype: DTypeLike = ...) -> BCOO:
    """Create BCOO-format sparse matrix from a dense matrix.

  Args:
    mat : array to be converted to BCOO.
    nse : number of specified elements in each batch
    n_batch : number of batch dimensions (default: 0)
    n_dense : number of block_dimensions (default: 0)
    index_dtype : dtype of sparse indices (default: int32)

  Returns:
    mat_bcoo: BCOO representation of the matrix.
  """

bcoo_extract_p: Incomplete

def bcoo_extract(sparr: BCOO, arr: ArrayLike, *, assume_unique: bool | None = None) -> BCOO:
    """Extract values from a dense array according to the sparse array's indices.

  Args:
    sparr : BCOO array whose indices will be used for the output.
    arr : ArrayLike with shape equal to self.shape
    assume_unique : bool, defaults to sparr.unique_indices
      If True, extract values for every index, even if index contains duplicates.
      If False, duplicate indices will have their values summed and returned in
      the position of the first index.

  Returns:
    extracted : a BCOO array with the same sparsity pattern as self.
  """

bcoo_transpose_p: Incomplete

def bcoo_transpose(mat: BCOO, *, permutation: Sequence[int]) -> BCOO:
    """Transpose a BCOO-format array.

  Args:
    mat: A BCOO-format array.
    permutation:  A tuple or list or ndarray which contains a permutation of
      [0,1,..,N-1] where N is the number of axes of ``mat`` in the order of
      batch, sparse, and dense dimensions. The i’th axis of the returned array
      corresponds to the axis numbered permutation[i] of ``mat``. Transpose
      permutation currently does not support permuting batch axes with non-batch
      axes nor permutating dense axes with non-dense axes.

  Returns:
    A BCOO-format array.
  """

bcoo_dot_general_p: Incomplete

def bcoo_dot_general(lhs: BCOO | Array, rhs: BCOO | Array, *, dimension_numbers: DotDimensionNumbers, precision: None = None, preferred_element_type: None = None) -> BCOO | Array:
    """A general contraction operation.

  Args:
    lhs: An ndarray or BCOO-format sparse array.
    rhs: An ndarray or BCOO-format sparse array..
    dimension_numbers: a tuple of tuples of the form
      `((lhs_contracting_dims, rhs_contracting_dims),
      (lhs_batch_dims, rhs_batch_dims))`.
    precision: unused
    preferred_element_type: unused

  Returns:
    An ndarray or BCOO-format sparse array containing the result. If both inputs
    are sparse, the result will be sparse, of type BCOO. If either input is dense,
    the result will be dense, of type ndarray.
  """

bcoo_dot_general_sampled_p: Incomplete

def bcoo_dot_general_sampled(A: Array, B: Array, indices: Array, *, dimension_numbers: DotDimensionNumbers) -> Array:
    """A contraction operation with output computed at given sparse indices.

  Args:
    lhs: An ndarray.
    rhs: An ndarray.
    indices: BCOO indices.
    dimension_numbers: a tuple of tuples of the form
      `((lhs_contracting_dims, rhs_contracting_dims),
      (lhs_batch_dims, rhs_batch_dims))`.

  Returns:
    BCOO data, an ndarray containing the result.
  """

bcoo_spdot_general_p: Incomplete
bcoo_sort_indices_p: Incomplete

def bcoo_sort_indices(mat: BCOO) -> BCOO:
    """Sort indices of a BCOO array.

  Args:
    mat : BCOO array

  Returns:
    mat_out : BCOO array with sorted indices.
  """

bcoo_sum_duplicates_p: Incomplete

def bcoo_sum_duplicates(mat: BCOO, nse: int | None = None) -> BCOO:
    """Sums duplicate indices within a BCOO array, returning an array with sorted indices.

  Args:
    mat : BCOO array
    nse : integer (optional). The number of specified elements in the output matrix. This must
      be specified for bcoo_sum_duplicates to be compatible with JIT and other JAX transformations.
      If not specified, the optimal nse will be computed based on the contents of the data and
      index arrays. If specified nse is larger than necessary, data and index arrays will be padded
      with standard fill values. If smaller than necessary, data elements will be dropped from the
      output matrix.

  Returns:
    mat_out : BCOO array with sorted indices and no duplicate indices.
  """
def bcoo_update_layout(mat: BCOO, *, n_batch: int | None = None, n_dense: int | None = None, on_inefficient: str | None = 'error') -> BCOO:
    """Update the storage layout (i.e. n_batch & n_dense) of a BCOO matrix.

  In many cases this can be done without introducing undue storage overhead. However,
  increasing ``mat.n_batch`` or ``mat.n_dense`` will lead to very inefficient storage,
  with many explicitly-stored zeros, unless the new batch or dense dimensions have size
  0 or 1. In such cases, ``bcoo_update_layout`` will raise a :class:`SparseEfficiencyError`.
  This can be silenced by specifying the ``on_inefficient`` argument.

  Args:
    mat : BCOO array
    n_batch : optional(int) the number of batch dimensions in the output matrix. If None,
      then n_batch = mat.n_batch.
    n_dense : optional(int) the number of dense dimensions in the output matrix. If None,
      then n_dense = mat.n_dense.
    on_inefficient : optional(string), one of ``['error', 'warn', None]``. Specify the
      behavior in case of an inefficient reconfiguration. This is defined as a reconfiguration
      where the size of the resulting representation is much larger than the size of the
      input representation.

  Returns:
    mat_out : BCOO array
      A BCOO array representing the same sparse array as the input, with the specified
      layout. ``mat_out.todense()`` will match ``mat.todense()`` up to appropriate precision.
  """
def bcoo_broadcast_in_dim(mat: BCOO, *, shape: Shape, broadcast_dimensions: Sequence[int]) -> BCOO:
    """Expand the size and rank of a BCOO array by duplicating the data.

  A BCOO equivalence to jax.lax.broadcast_in_dim.

  Args:
    mat: A BCOO-format array.
    shape: The shape of the target array.
    broadcast_dimensions: The dimension in the shape of the target array which
      each dimension of the operand (``mat``) shape corresponds to.

  Returns:
    A BCOO-format array containing the target array.
  """
def bcoo_concatenate(operands: Sequence[BCOO], *, dimension: int) -> BCOO:
    """Sparse implementation of :func:`jax.lax.concatenate`

  Args:
    operands : Sequence of BCOO arrays to concatenate. The arrays must have equal
      shapes, except in the `dimension` axis. Additionally, the arrays must have
      have equivalent batch, sparse, and dense dimensions.
    dimension : Positive integer specifying the dimension along which to concatenate
      the arrays. The dimension must be among batch or sparse dimensions of the input;
      concatenation along dense dimensions is not supported.

  Returns:
    A BCOO array containing the concatenation of the inputs.
  """
def bcoo_reshape(mat: BCOO, *, new_sizes: Sequence[int], dimensions: Sequence[int] | None = None) -> BCOO:
    """Sparse implementation of {func}`jax.lax.reshape`.

  Args:
    operand: BCOO array to be reshaped.
    new_sizes: sequence of integers specifying the resulting shape. The size
      of the final array must match the size of the input. This must be specified
      such that batch, sparse, and dense dimensions do not mix.
    dimensions: optional sequence of integers specifying the permutation order of
      the input shape. If specified, the length must match ``operand.shape``.
      Additionally, dimensions must only permute among like dimensions of mat:
      batch, sparse, and dense dimensions cannot be permuted.

  Returns:
    out: reshaped array.
  """
def bcoo_rev(operand, dimensions):
    """Sparse implementation of {func}`jax.lax.rev`"""
def bcoo_squeeze(arr: BCOO, *, dimensions: Sequence[int]) -> BCOO:
    """Sparse implementation of {func}`jax.lax.squeeze`.

  Squeeze any number of size 1 dimensions from an array.

  Args:
    arr: BCOO array to be reshaped.
    dimensions: sequence of integers specifying dimensions to squeeze.

  Returns:
    out: reshaped array.
  """
def bcoo_slice(mat: BCOO, *, start_indices: Sequence[int], limit_indices: Sequence[int], strides: Sequence[int] | None = None) -> BCOO:
    """Sparse implementation of {func}`jax.lax.slice`.

  Args:
    mat: BCOO array to be reshaped.
    start_indices: sequence of integers of length `mat.ndim` specifying the starting
      indices of each slice.
    limit_indices: sequence of integers of length `mat.ndim` specifying the ending
      indices of each slice
    strides: (not implemented) sequence of integers of length `mat.ndim` specifying
      the stride for each slice

  Returns:
    out: BCOO array containing the slice.
  """
def bcoo_dynamic_slice(mat: BCOO, start_indices: Sequence[Any], slice_sizes: Sequence[int]) -> BCOO:
    """Sparse implementation of {func}`jax.lax.dynamic_slice`.

  Args:
    mat: BCOO array to slice.
    start_indices: a list of scalar indices, one per dimension. These values
      may be dynamic.
    slice_sizes: the size of the slice. Must be a sequence of non-negative
      integers with length equal to `ndim(operand)`. Inside a JIT compiled
      function, only static values are supported (all JAX arrays inside JIT
      must have statically known size).

  Returns:
    out: BCOO array containing the slice.
  """
def bcoo_reduce_sum(mat: BCOO, *, axes: Sequence[int]) -> BCOO:
    """Sum array element over given axes.

  Args:
    mat: A BCOO-format array.
    shape: The shape of the target array.
    axes:  A tuple or list or ndarray which contains axes of ``mat`` over which
      sum is performed.

  Returns:
    A BCOO-format array containing the result.
  """
def bcoo_multiply_sparse(lhs: BCOO, rhs: BCOO) -> BCOO:
    """An element-wise multiplication of two sparse arrays.

  Args:
    lhs: A BCOO-format array.
    rhs: A BCOO-format array.

  Returns:
    An BCOO-format array containing the result.
  """
def bcoo_multiply_dense(sp_mat: BCOO, v: Array) -> Array:
    """An element-wise multiplication between a sparse and a dense array.

  Args:
    lhs: A BCOO-format array.
    rhs: An ndarray.

  Returns:
    An ndarray containing the result.
  """
def bcoo_gather(operand: BCOO, start_indices: Array, dimension_numbers: GatherDimensionNumbers, slice_sizes: Shape, *, unique_indices: bool = False, indices_are_sorted: bool = False, mode: str | GatherScatterMode | None = None, fill_value: Incomplete | None = None) -> BCOO:
    """BCOO version of lax.gather."""
def bcoo_conv_general_dilated(lhs, rhs, *, window_strides, padding, lhs_dilation: Incomplete | None = None, rhs_dilation: Incomplete | None = None, dimension_numbers: Incomplete | None = None, feature_group_count: int = 1, batch_group_count: int = 1, precision: Incomplete | None = None, preferred_element_type: Incomplete | None = None) -> BCOO: ...

class BCOO(JAXSparse):
    """Experimental batched COO matrix implemented in JAX

  Args:
    (data, indices) : data and indices in batched COO format.
    shape : shape of sparse array.

  Attributes:
    data : ndarray of shape ``[*batch_dims, nse, *dense_dims]`` containing the
      explicitly stored data within the sparse matrix.
    indices : ndarray of shape ``[*batch_dims, nse, n_sparse]`` containing the
      indices of the explicitly stored data. Duplicate entries will be summed.

  Examples:
    Create a sparse array from a dense array:

    >>> M = jnp.array([[0., 2., 0.], [1., 0., 4.]])
    >>> M_sp = BCOO.fromdense(M)
    >>> M_sp
    BCOO(float32[2, 3], nse=3)

    Examine the internal representation:

    >>> M_sp.data
    Array([2., 1., 4.], dtype=float32)
    >>> M_sp.indices
    Array([[0, 1],
           [1, 0],
           [1, 2]], dtype=int32)

    Create a dense array from a sparse array:

    >>> M_sp.todense()
    Array([[0., 2., 0.],
           [1., 0., 4.]], dtype=float32)

    Create a sparse array from COO data & indices:

    >>> data = jnp.array([1., 3., 5.])
    >>> indices = jnp.array([[0, 0],
    ...                      [1, 1],
    ...                      [2, 2]])
    >>> mat = BCOO((data, indices), shape=(3, 3))
    >>> mat
    BCOO(float32[3, 3], nse=3)
    >>> mat.todense()
    Array([[1., 0., 0.],
           [0., 3., 0.],
           [0., 0., 5.]], dtype=float32)
  """
    data: Array
    indices: Array
    shape: Shape
    nse: Incomplete
    dtype: Incomplete
    n_batch: Incomplete
    n_sparse: Incomplete
    n_dense: Incomplete
    indices_sorted: bool
    unique_indices: bool
    def __init__(self, args: tuple[Array, Array], *, shape: Sequence[int], indices_sorted: bool = False, unique_indices: bool = False) -> None: ...
    def reshape(self, *args, **kwargs) -> BCOO: ...
    def astype(self, *args, **kwargs) -> BCOO: ...
    def sum(self) -> BCOO: ...
    @classmethod
    def fromdense(cls, mat: Array, *, nse: int | None = None, index_dtype: DTypeLike = ..., n_dense: int = 0, n_batch: int = 0) -> BCOO:
        """Create a BCOO array from a (dense) :class:`~jax.Array`."""
    @classmethod
    def from_scipy_sparse(cls, mat, *, index_dtype: DTypeLike | None = None, n_dense: int = 0, n_batch: int = 0) -> BCOO:
        """Create a BCOO array from a :mod:`scipy.sparse` array."""
    def update_layout(self, *, n_batch: int | None = None, n_dense: int | None = None, on_inefficient: str = 'error') -> BCOO:
        """Update the storage layout (i.e. n_batch & n_dense) of a BCOO matrix.

    In many cases this can be done without introducing undue storage overhead. However,
    increasing ``mat.n_batch`` or ``mat.n_dense`` will lead to very inefficient storage,
    with many explicitly-stored zeros, unless the new batch or dense dimensions have size
    0 or 1. In such cases, ``update_layout`` will raise a :class:`SparseEfficiencyError`.
    This can be silenced by specifying the ``on_inefficient`` argument.

    Args:
      n_batch : optional(int) the number of batch dimensions in the output matrix. If None,
        then n_batch = mat.n_batch.
      n_dense : optional(int) the number of dense dimensions in the output matrix. If None,
        then n_dense = mat.n_dense.
      on_inefficient : optional(string), one of ``['error', 'warn', None]``. Specify the
        behavior in case of an inefficient reconfiguration. This is defined as a reconfiguration
        where the size of the resulting representation is much larger than the size of the
        input representation.

    Returns:
      mat_out : BCOO array
        A BCOO array representing the same sparse array as the input, with the specified
        layout. ``mat_out.todense()`` will match ``mat.todense()`` up to appropriate precision.
    """
    def sum_duplicates(self, nse: int | None = None, remove_zeros: bool = True) -> BCOO:
        """Return a copy of the array with duplicate indices summed.

    Additionally, this operation will result in explicit zero entries removed, and
    indices being sorted in lexicographic order.

    Because the size of the resulting representation depends on the values in the
    arrays, this operation is not compatible with JIT or other transforms. To use
    ``sum_duplicates`` in such cases, you may pass a value to `nse` to specify the
    desired size of the output representation.

    Args:
      nse : integer (optional), if specified, gives the number of specified elements in
        the output sparse representation; if it is larger than the number required, data
        will be padded with zeros and indices will be padded with out-of-bounds values.
        If it is smaller than the number required, data will be silently discarded.
      remove_zeros : bool (default=True). If True, remove explicit zeros from the data
        as part of summing duplicates. If False, then explicit zeros at unique indices
        will remain among the specified elements. Note: remove_zeros=True is incompatible
        with autodiff.
    """
    def sort_indices(self) -> BCOO:
        """Return a copy of the matrix with indices sorted."""
    def todense(self) -> Array:
        """Create a dense version of the array."""
    def transpose(self, axes: Sequence[int] | None = None) -> BCOO:
        """Create a new array containing the transpose."""
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, aux_data, children): ...
