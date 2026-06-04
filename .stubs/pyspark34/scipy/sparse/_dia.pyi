from ._data import _data_matrix
from _typeshed import Incomplete

__all__ = ['dia_matrix', 'isspmatrix_dia']

class dia_matrix(_data_matrix):
    """Sparse matrix with DIAgonal storage

    This can be instantiated in several ways:
        dia_matrix(D)
            with a dense matrix

        dia_matrix(S)
            with another sparse matrix S (equivalent to S.todia())

        dia_matrix((M, N), [dtype])
            to construct an empty matrix with shape (M, N),
            dtype is optional, defaulting to dtype='d'.

        dia_matrix((data, offsets), shape=(M, N))
            where the ``data[k,:]`` stores the diagonal entries for
            diagonal ``offsets[k]`` (See example below)

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
        DIA format data array of the matrix
    offsets
        DIA format offset array of the matrix

    Notes
    -----

    Sparse matrices can be used in arithmetic operations: they support
    addition, subtraction, multiplication, division, and matrix power.

    Examples
    --------

    >>> import numpy as np
    >>> from scipy.sparse import dia_matrix
    >>> dia_matrix((3, 4), dtype=np.int8).toarray()
    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]], dtype=int8)

    >>> data = np.array([[1, 2, 3, 4]]).repeat(3, axis=0)
    >>> offsets = np.array([0, -1, 2])
    >>> dia_matrix((data, offsets), shape=(4, 4)).toarray()
    array([[1, 0, 3, 0],
           [1, 2, 0, 4],
           [0, 2, 3, 0],
           [0, 0, 3, 4]])

    >>> from scipy.sparse import dia_matrix
    >>> n = 10
    >>> ex = np.ones(n)
    >>> data = np.array([ex, 2 * ex, ex])
    >>> offsets = np.array([-1, 0, 1])
    >>> dia_matrix((data, offsets), shape=(n, n)).toarray()
    array([[2., 1., 0., ..., 0., 0., 0.],
           [1., 2., 1., ..., 0., 0., 0.],
           [0., 1., 2., ..., 0., 0., 0.],
           ...,
           [0., 0., 0., ..., 2., 1., 0.],
           [0., 0., 0., ..., 1., 2., 1.],
           [0., 0., 0., ..., 0., 1., 2.]])
    """
    format: str
    data: Incomplete
    offsets: Incomplete
    def __init__(self, arg1, shape: Incomplete | None = None, dtype: Incomplete | None = None, copy: bool = False) -> None: ...
    def count_nonzero(self): ...
    def getnnz(self, axis: Incomplete | None = None): ...
    def sum(self, axis: Incomplete | None = None, dtype: Incomplete | None = None, out: Incomplete | None = None): ...
    def todia(self, copy: bool = False): ...
    def transpose(self, axes: Incomplete | None = None, copy: bool = False): ...
    def diagonal(self, k: int = 0): ...
    def tocsc(self, copy: bool = False): ...
    def tocoo(self, copy: bool = False): ...
    def resize(self, *shape) -> None: ...

def isspmatrix_dia(x):
    """Is x of dia_matrix type?

    Parameters
    ----------
    x
        object to check for being a dia matrix

    Returns
    -------
    bool
        True if x is a dia matrix, False otherwise

    Examples
    --------
    >>> from scipy.sparse import dia_matrix, isspmatrix_dia
    >>> isspmatrix_dia(dia_matrix([[5]]))
    True

    >>> from scipy.sparse import dia_matrix, csr_matrix, isspmatrix_dia
    >>> isspmatrix_dia(csr_matrix([[5]]))
    False
    """
