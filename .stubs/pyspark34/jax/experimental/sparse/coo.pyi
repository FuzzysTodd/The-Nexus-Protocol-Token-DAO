import jax
from _typeshed import Incomplete
from jax import lax as lax, tree_util as tree_util
from jax._src import core as core, dispatch as dispatch
from jax._src.interpreters import ad as ad
from jax._src.lib import gpu_sparse as gpu_sparse
from jax._src.lib.mlir.dialects import hlo as hlo
from jax._src.numpy.util import promote_dtypes as promote_dtypes
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike
from jax.experimental.sparse._base import JAXSparse as JAXSparse
from jax.experimental.sparse.util import CuSparseEfficiencyWarning as CuSparseEfficiencyWarning
from jax.interpreters import mlir as mlir
from typing import Any, NamedTuple

Dtype = Any
Shape = tuple[int, ...]

class COOInfo(NamedTuple):
    shape: Shape
    rows_sorted: bool = ...
    cols_sorted: bool = ...

class COO(JAXSparse):
    """Experimental COO matrix implemented in JAX.

  Note: this class has minimal compatibility with JAX transforms such as
  grad and autodiff, and offers very little functionality. In general you
  should prefer :class:`jax.experimental.sparse.BCOO`.

  Additionally, there are known failures in the case that `nse` is larger
  than the true number of nonzeros in the represented matrix. This situation
  is better handled in BCOO.
  """
    data: jax.Array
    row: jax.Array
    col: jax.Array
    shape: tuple[int, int]
    nse: Incomplete
    dtype: Incomplete
    def __init__(self, args: tuple[Array, Array, Array], *, shape: Shape, rows_sorted: bool = False, cols_sorted: bool = False) -> None: ...
    @classmethod
    def fromdense(cls, mat: Array, *, nse: int | None = None, index_dtype: DTypeLike = ...) -> COO: ...
    def todense(self) -> Array: ...
    def transpose(self, axes: tuple[int, ...] | None = None) -> COO: ...
    def tree_flatten(self) -> tuple[tuple[Array, Array, Array], dict[str, Any]]: ...
    @classmethod
    def tree_unflatten(cls, aux_data, children): ...
    def __matmul__(self, other: ArrayLike) -> Array: ...

coo_todense_p: Incomplete

def coo_todense(mat: COO) -> Array:
    """Convert a COO-format sparse matrix to a dense matrix.

  Args:
    mat : COO matrix
  Returns:
    mat_dense: dense version of ``mat``
  """

coo_fromdense_p: Incomplete

def coo_fromdense(mat: Array, *, nse: int | None = None, index_dtype: DTypeLike = ...) -> COO:
    """Create a COO-format sparse matrix from a dense matrix.

  Args:
    mat : array to be converted to COO.
    nse : number of specified entries in ``mat``. If not specified,
      it will be computed from the input matrix.
    index_dtype : dtype of sparse indices

  Returns:
    mat_coo : COO representation of the matrix.
  """

coo_matvec_p: Incomplete

def coo_matvec(mat: COO, v: Array, transpose: bool = False) -> Array:
    """Product of COO sparse matrix and a dense vector.

  Args:
    mat : COO matrix
    v : one-dimensional array of size ``(shape[0] if transpose else shape[1],)`` and
      dtype ``mat.dtype``
    transpose : boolean specifying whether to transpose the sparse matrix
      before computing.

  Returns:
    y : array of shape ``(mat.shape[1] if transpose else mat.shape[0],)`` representing
      the matrix vector product.
  """

coo_matmat_p: Incomplete

def coo_matmat(mat: COO, B: Array, *, transpose: bool = False) -> Array:
    """Product of COO sparse matrix and a dense matrix.

  Args:
    mat : COO matrix
    B : array of shape ``(mat.shape[0] if transpose else mat.shape[1], cols)`` and
      dtype ``mat.dtype``
    transpose : boolean specifying whether to transpose the sparse matrix
      before computing.

  Returns:
    C : array of shape ``(mat.shape[1] if transpose else mat.shape[0], cols)``
      representing the matrix vector product.
  """
