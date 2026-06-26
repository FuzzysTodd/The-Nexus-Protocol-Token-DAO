from _typeshed import Incomplete
from jax import tree_util as tree_util
from jax._src import core as core, dtypes as dtypes
from jax._src.interpreters import ad as ad, batching as batching
from jax._src.typing import Array as Array, DTypeLike as DTypeLike, Shape as Shape
from jax.experimental.sparse._base import JAXSparse as JAXSparse
from jax.experimental.sparse.bcoo import BCOO as BCOO
from jax.experimental.sparse.bcsr import BCSR as BCSR
from jax.experimental.sparse.coo import COO as COO
from jax.experimental.sparse.csr import CSC as CSC, CSR as CSR
from jax.interpreters import mlir as mlir

todense_p: Incomplete

def todense(arr: JAXSparse | Array) -> Array:
    """Convert input to a dense matrix. If input is already dense, pass through."""
def empty(shape: Shape, dtype: DTypeLike | None = None, index_dtype: DTypeLike = 'int32', sparse_format: str = 'bcoo', **kwds) -> JAXSparse:
    """Create an empty sparse array.

  Args:
    shape: sequence of integers giving the array shape.
    dtype: (optional) dtype of the array.
    index_dtype: (optional) dtype of the index arrays.
    format: string specifying the matrix format (e.g. ['bcoo']).
    **kwds: additional keywords passed to the format-specific _empty constructor.
  Returns:
    mat: empty sparse matrix.
  """
def eye(N: int, M: int | None = None, k: int = 0, dtype: DTypeLike | None = None, index_dtype: DTypeLike = 'int32', sparse_format: str = 'bcoo', **kwds) -> JAXSparse:
    """Create 2D sparse identity matrix.

  Args:
    N: int. Number of rows in the output.
    M: int, optional. Number of columns in the output. If None, defaults to `N`.
    k: int, optional. Index of the diagonal: 0 (the default) refers to the main
       diagonal, a positive value refers to an upper diagonal, and a negative value
       to a lower diagonal.
    dtype: data-type, optional. Data-type of the returned array.
    index_dtype: (optional) dtype of the index arrays.
    format: string specifying the matrix format (e.g. ['bcoo']).
    **kwds: additional keywords passed to the format-specific _empty constructor.

  Returns:
    I: two-dimensional sparse matrix with ones along the k-th diagonal.
  """
