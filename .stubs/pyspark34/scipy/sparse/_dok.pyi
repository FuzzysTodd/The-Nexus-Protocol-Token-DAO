from ._base import spmatrix
from ._index import IndexMixin
from _typeshed import Incomplete

__all__ = ['dok_matrix', 'isspmatrix_dok']

class dok_matrix(spmatrix, IndexMixin, dict):
    """
    Dictionary Of Keys based sparse matrix.

    This is an efficient structure for constructing sparse
    matrices incrementally.

    This can be instantiated in several ways:
        dok_matrix(D)
            with a dense matrix, D

        dok_matrix(S)
            with a sparse matrix, S

        dok_matrix((M,N), [dtype])
            create the matrix with initial shape (M,N)
            dtype is optional, defaulting to dtype='d'

    Attributes
    ----------
    dtype : dtype
        Data type of the matrix
    shape : 2-tuple
        Shape of the matrix
    ndim : int
        Number of dimensions (this is always 2)
    nnz
        Number of nonzero elements

    Notes
    -----

    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    Allows for efficient O(1) access of individual elements.
    Duplicates are not allowed.
    Can be efficiently converted to a coo_matrix once constructed.

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import dok_matrix
    >>> S = dok_matrix((5, 5), dtype=np.float32)
    >>> for i in range(5):
    ...     for j in range(5):
    ...         S[i, j] = i + j    # Update element

    """
    format: str
    dtype: Incomplete
    def __init__(self, arg1, shape: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False) -> None: ...
    def update(self, val) -> None: ...
    __dict__: Incomplete
    def set_shape(self, shape) -> None: ...
    shape: Incomplete
    def getnnz(self, axis: Incomplete | None = None): ...
    def count_nonzero(self): ...
    def __len__(self) -> int: ...
    def get(self, key, default: float = 0.0):
        """This overrides the dict.get method, providing type checking
        but otherwise equivalent functionality.
        """
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __neg__(self): ...
    def __imul__(self, other): ...
    def __truediv__(self, other): ...
    def __itruediv__(self, other): ...
    def __reduce__(self): ...
    def transpose(self, axes: Incomplete | None = None, copy: bool = False): ...
    def conjtransp(self):
        """Return the conjugate transpose."""
    def copy(self): ...
    def tocoo(self, copy: bool = False): ...
    def todok(self, copy: bool = False): ...
    def tocsc(self, copy: bool = False): ...
    def resize(self, *shape) -> None: ...

def isspmatrix_dok(x):
    """Is x of dok_matrix type?

    Parameters
    ----------
    x
        object to check for being a dok matrix

    Returns
    -------
    bool
        True if x is a dok matrix, False otherwise

    Examples
    --------
    >>> from scipy.sparse import dok_matrix, isspmatrix_dok
    >>> isspmatrix_dok(dok_matrix([[5]]))
    True

    >>> from scipy.sparse import dok_matrix, csr_matrix, isspmatrix_dok
    >>> isspmatrix_dok(csr_matrix([[5]]))
    False
    """
