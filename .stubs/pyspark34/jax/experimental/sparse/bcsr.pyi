import jax
from _typeshed import Incomplete
from collections.abc import Sequence
from jax import config as config, lax as lax, tree_util as tree_util
from jax._src import api_util as api_util, core as core, dispatch as dispatch
from jax._src.interpreters import ad as ad, batching as batching, mlir as mlir
from jax._src.lax.lax import DotDimensionNumbers as DotDimensionNumbers
from jax._src.lib import gpu_sparse as gpu_sparse
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike
from jax.experimental.sparse import bcoo as bcoo
from jax.experimental.sparse._base import JAXSparse as JAXSparse
from jax.experimental.sparse.util import CuSparseEfficiencyWarning as CuSparseEfficiencyWarning, Shape as Shape, SparseInfo as SparseInfo, nfold_vmap as nfold_vmap
from jax.util import safe_zip as safe_zip, split_list as split_list
from typing import NamedTuple

def bcsr_eliminate_zeros(mat: BCSR, nse: int | None = None) -> BCSR:
    """Eliminate zeros in BCSR representation."""
def bcsr_sum_duplicates(mat: BCSR, nse: int | None = None) -> BCSR:
    """Sums duplicate indices within a BCSR array, returning an array with sorted indices.

  Args:
    mat : BCSR array
    nse : integer (optional). The number of specified elements in the output matrix. This must
      be specified for bcoo_sum_duplicates to be compatible with JIT and other JAX transformations.
      If not specified, the optimal nse will be computed based on the contents of the data and
      index arrays. If specified nse is larger than necessary, data and index arrays will be padded
      with standard fill values. If smaller than necessary, data elements will be dropped from the
      output matrix.

  Returns:
    mat_out : BCSR array with sorted indices and no duplicate indices.
  """

class BCSRProperties(NamedTuple):
    n_batch: int
    n_dense: int
    nse: int

bcsr_fromdense_p: Incomplete

def bcsr_fromdense(mat: ArrayLike, *, nse: int | None = None, n_batch: int = 0, n_dense: int = 0, index_dtype: DTypeLike = ...) -> BCSR:
    """Create BCSR-format sparse matrix from a dense matrix.

  Args:
    mat : array to be converted to BCOO.
    nse : number of stored elements in each batch
    n_batch : number of batch dimensions (default: 0)
    n_dense : number of dense dimensions (default: 0)
    index_dtype : dtype of sparse indices (default: int32)

  Returns:
    mat_bcsr: BCSR representation of the matrix.
  """

bcsr_todense_p: Incomplete

def bcsr_todense(mat: BCSR) -> Array:
    """Convert batched sparse matrix to a dense matrix.

  Args:
    mat: BCSR matrix.

  Returns:
    The dense version of ``mat``.
  """

bcsr_extract_p: Incomplete

def bcsr_extract(indices: ArrayLike, indptr: ArrayLike, mat: ArrayLike) -> Array:
    """Extract values from a dense matrix at given BCSR (indices, indptr).

  Args:
    indices: An ndarray; see BCSR indices.
    indptr: An ndarray; see BCSR indptr.
    mat: A dense matrix.

  Returns:
    An ndarray; see BCSR data.
  """

bcsr_dot_general_p: Incomplete

def bcsr_dot_general(lhs: BCSR | Array, rhs: Array, *, dimension_numbers: DotDimensionNumbers, precision: None = None, preferred_element_type: None = None) -> Array:
    """A general contraction operation.

  Args:
    lhs: An ndarray or BCSR-format sparse array.
    rhs: An ndarray or BCSR-format sparse array..
    dimension_numbers: a tuple of tuples of the form
      `((lhs_contracting_dims, rhs_contracting_dims),
      (lhs_batch_dims, rhs_batch_dims))`.
    precision: unused
    preferred_element_type: unused

  Returns:
    An ndarray or BCSR-format sparse array containing the result. If both inputs
    are sparse, the result will be sparse, of type BCSR. If either input is
    dense, the result will be dense, of type ndarray.
  """
def bcsr_broadcast_in_dim(mat: BCSR, *, shape: Shape, broadcast_dimensions: Sequence[int]) -> BCSR: ...
def bcsr_concatenate(operands: Sequence[BCSR], *, dimension: int) -> BCSR:
    """Sparse implementation of :func:`jax.lax.concatenate`

  Args:
    operands : Sequence of BCSR arrays to concatenate. The arrays must have equal
      shapes, except in the `dimension` axis. Additionally, the arrays must have
      have equivalent batch, sparse, and dense dimensions.
    dimension : Positive integer specifying the dimension along which to concatenate
      the arrays. The dimension must be among batch or sparse dimensions of the input;
      concatenation along dense dimensions is not supported.

  Returns:
    A BCSR array containing the concatenation of the inputs.
  """

class BCSR(JAXSparse):
    """Experimental batched CSR matrix implemented in JAX."""
    data: jax.Array
    indices: jax.Array
    indptr: jax.Array
    shape: Shape
    nse: Incomplete
    dtype: Incomplete
    n_batch: Incomplete
    n_sparse: Incomplete
    n_dense: Incomplete
    indices_sorted: bool
    unique_indices: bool
    def __init__(self, args: tuple[Array, Array, Array], *, shape: Sequence[int], indices_sorted: bool = False, unique_indices: bool = False) -> None: ...
    def transpose(self, *args, **kwargs) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, aux_data, children): ...
    def sum_duplicates(self, nse: int | None = None, remove_zeros: bool = True) -> BCSR:
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
    @classmethod
    def fromdense(cls, mat, *, nse: Incomplete | None = None, index_dtype=..., n_dense: int = 0, n_batch: int = 0):
        """Create a BCSR array from a (dense) :class:`Array`."""
    def todense(self):
        """Create a dense version of the array."""
    def to_bcoo(self) -> bcoo.BCOO: ...
    @classmethod
    def from_bcoo(cls, arr: bcoo.BCOO) -> BCSR: ...
    @classmethod
    def from_scipy_sparse(cls, mat, *, index_dtype: Incomplete | None = None, n_dense: int = 0, n_batch: int = 0):
        """Create a BCSR array from a :mod:`scipy.sparse` array."""
