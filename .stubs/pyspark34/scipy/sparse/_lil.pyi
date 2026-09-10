from ._base import spmatrix
from ._index import IndexMixin
from _typeshed import Incomplete

__all__ = ['lil_matrix', 'isspmatrix_lil']

class lil_matrix(spmatrix, IndexMixin):
    """Row-based LIst of Lists sparse matrix

    This is a structure for constructing sparse matrices incrementally.
    Note that inserting a single item can take linear time in the worst case;
    to construct a matrix efficiently, make sure the items are pre-sorted by
    index, per row.

    This can be instantiated in several ways:
        lil_matrix(D)
            with a dense matrix or rank-2 ndarray D

        lil_matrix(S)
            with another sparse matrix S (equivalent to S.tolil())

        lil_matrix((M, N), [dtype])
            to construct an empty matrix with shape (M, N)
            dtype is optional, defaulting to dtype='d'.

    Attributes
    ----------
    dtype : dtype
        Data type of the matrix
    shape : 2-tuple
        Shape of the matrix
    ndim : int
        Number of dimensions (this is always 2)
    nnz
        Number of stored values, including explicit zeros
    data
        LIL format data array of the matrix
    rows
        LIL format row index array of the matrix

    Notes
    -----
    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    Advantages of the LIL format
        - supports flexible slicing
        - changes to the matrix sparsity structure are efficient

    Disadvantages of the LIL format
        - arithmetic operations LIL + LIL are slow (consider CSR or CSC)
        - slow column slicing (consider CSC)
        - slow matrix vector products (consider CSR or CSC)

    Intended Usage
        - LIL is a convenient format for constructing sparse matrices
        - once a matrix has been constructed, convert to CSR or
          CSC format for fast arithmetic and matrix vector operations
        - consider using the COO format when constructing large matrices

    Data Structure
        - An array (``self.rows``) of rows, each of which is a sorted
          list of column indices of non-zero elements.
        - The corresponding nonzero values are stored in similar
          fashion in ``self.data``.


    """
    format: str
    dtype: Incomplete
    rows: Incomplete
    data: Incomplete
    def __init__(self, arg1, shape: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False) -> None: ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def __imul__(self, other): ...
    def __itruediv__(self, other): ...
    def getnnz(self, axis: Incomplete | None = None): ...
    def count_nonzero(self): ...
    def getrowview(self, i):
        """Returns a view of the 'i'th row (without copying).
        """
    def getrow(self, i):
        """Returns a copy of the 'i'th row.
        """
    def __getitem__(self, key): ...
    def __setitem__(self, key, x) -> None: ...
    def __truediv__(self, other): ...
    def copy(self): ...
    def reshape(self, *args, **kwargs): ...
    def resize(self, *shape) -> None: ...
    def toarray(self, order: Incomplete | None = None, out: Incomplete | None = None): ...
    def transpose(self, axes: Incomplete | None = None, copy: bool = False): ...
    def tolil(self, copy: bool = False): ...
    def tocsr(self, copy: bool = False): ...

def isspmatrix_lil(x):
    """Is x of lil_matrix type?

    Parameters
    ----------
    x
        object to check for being a lil matrix

    Returns
    -------
    bool
        True if x is a lil matrix, False otherwise

    Examples
    --------
    >>> from scipy.sparse import lil_matrix, isspmatrix_lil
    >>> isspmatrix_lil(lil_matrix([[5]]))
    True

    >>> from scipy.sparse import lil_matrix, csr_matrix, isspmatrix_lil
    >>> isspmatrix_lil(csr_matrix([[5]]))
    False
    """
