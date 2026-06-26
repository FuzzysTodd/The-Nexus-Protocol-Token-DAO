import jax
from _typeshed import Incomplete
from jax import lax as lax, tree_util as tree_util
from jax._src import core as core, dispatch as dispatch
from jax._src.interpreters import ad as ad
from jax._src.lib import gpu_sparse as gpu_sparse
from jax._src.numpy.util import promote_dtypes as promote_dtypes
from jax._src.typing import Array as Array, ArrayLike as ArrayLike, DTypeLike as DTypeLike
from jax.experimental.sparse._base import JAXSparse as JAXSparse
from jax.experimental.sparse.coo import COOInfo as COOInfo
from jax.experimental.sparse.util import CuSparseEfficiencyWarning as CuSparseEfficiencyWarning
from jax.interpreters import mlir as mlir

Shape = tuple[int, ...]

class CSR(JAXSparse):
    """Experimental CSR matrix implemented in JAX.

  Note: this class has minimal compatibility with JAX transforms such as
  grad and autodiff, and offers very little functionality. In general you
  should prefer :class:`jax.experimental.sparse.BCOO`.

  Additionally, there are known failures in the case that `nse` is larger
  than the true number of nonzeros in the represented matrix. This situation
  is better handled in BCOO.
  """
    data: jax.Array
    indices: jax.Array
    indptr: jax.Array
    shape: tuple[int, int]
    nse: Incomplete
    dtype: Incomplete
    def __init__(self, args, *, shape) -> None: ...
    @classmethod
    def fromdense(cls, mat, *, nse: Incomplete | None = None, index_dtype=...): ...
    def todense(self): ...
    def transpose(self, axes: Incomplete | None = None): ...
    def __matmul__(self, other): ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, aux_data, children): ...

class CSC(JAXSparse):
    """Experimental CSC matrix implemented in JAX; API subject to change."""
    data: jax.Array
    indices: jax.Array
    indptr: jax.Array
    shape: tuple[int, int]
    nse: Incomplete
    dtype: Incomplete
    def __init__(self, args, *, shape) -> None: ...
    @classmethod
    def fromdense(cls, mat, *, nse: Incomplete | None = None, index_dtype=...): ...
    def todense(self): ...
    def transpose(self, axes: Incomplete | None = None): ...
    def __matmul__(self, other): ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, aux_data, children): ...

csr_todense_p: Incomplete

def csr_todense(mat: CSR) -> Array:
    """Convert a CSR-format sparse matrix to a dense matrix.

  Args:
    mat : CSR matrix
  Returns:
    mat_dense: dense version of ``mat``
  """

csr_fromdense_p: Incomplete

def csr_fromdense(mat: Array, *, nse: int | None = None, index_dtype: DTypeLike = ...) -> CSR:
    """Create a CSR-format sparse matrix from a dense matrix.

  Args:
    mat : array to be converted to CSR.
    nse : number of specified entries in ``mat``. If not specified,
      it will be computed from the input matrix.
    index_dtype : dtype of sparse indices

  Returns:
    mat_coo : CSR representation of the matrix.
  """

csr_matvec_p: Incomplete

def csr_matvec(mat: CSR, v: Array, transpose: bool = False) -> Array:
    """Product of CSR sparse matrix and a dense vector.

  Args:
    mat : CSR matrix
    v : one-dimensional array of size ``(shape[0] if transpose else shape[1],)`` and
      dtype ``mat.dtype``
    transpose : boolean specifying whether to transpose the sparse matrix
      before computing.

  Returns:
    y : array of shape ``(mat.shape[1] if transpose else mat.shape[0],)`` representing
      the matrix vector product.
  """

csr_matmat_p: Incomplete

def csr_matmat(mat: CSR, B: Array, *, transpose: bool = False) -> Array:
    """Product of CSR sparse matrix and a dense matrix.

  Args:
    mat : CSR matrix
    B : array of shape ``(mat.shape[0] if transpose else mat.shape[1], cols)`` and
      dtype ``mat.dtype``
    transpose : boolean specifying whether to transpose the sparse matrix
      before computing.

  Returns:
    C : array of shape ``(mat.shape[1] if transpose else mat.shape[0], cols)``
      representing the matrix vector product.
  """
