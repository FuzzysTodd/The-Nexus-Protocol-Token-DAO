from _typeshed import Incomplete
from scipy.sparse.linalg._interface import LinearOperator

__all__ = ['expm', 'inv']

def inv(A):
    """
    Compute the inverse of a sparse matrix

    Parameters
    ----------
    A : (M, M) sparse matrix
        square matrix to be inverted

    Returns
    -------
    Ainv : (M, M) sparse matrix
        inverse of `A`

    Notes
    -----
    This computes the sparse inverse of `A`. If the inverse of `A` is expected
    to be non-sparse, it will likely be faster to convert `A` to dense and use
    `scipy.linalg.inv`.

    Examples
    --------
    >>> from scipy.sparse import csc_matrix
    >>> from scipy.sparse.linalg import inv
    >>> A = csc_matrix([[1., 0.], [1., 2.]])
    >>> Ainv = inv(A)
    >>> Ainv
    <2x2 sparse matrix of type '<class 'numpy.float64'>'
        with 3 stored elements in Compressed Sparse Column format>
    >>> A.dot(Ainv)
    <2x2 sparse matrix of type '<class 'numpy.float64'>'
        with 2 stored elements in Compressed Sparse Column format>
    >>> A.dot(Ainv).toarray()
    array([[ 1.,  0.],
           [ 0.,  1.]])

    .. versionadded:: 0.12.0

    """

class MatrixPowerOperator(LinearOperator):
    dtype: Incomplete
    ndim: Incomplete
    shape: Incomplete
    def __init__(self, A, p, structure: Incomplete | None = None) -> None: ...
    @property
    def T(self): ...

class ProductOperator(LinearOperator):
    """
    For now, this is limited to products of multiple square matrices.
    """
    shape: Incomplete
    ndim: Incomplete
    dtype: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def T(self): ...

class _ExpmPadeHelper:
    """
    Help lazily evaluate a matrix exponential.

    The idea is to not do more work than we need for high expm precision,
    so we lazily compute matrix powers and store or precompute
    other properties of the matrix.

    """
    A: Incomplete
    ident: Incomplete
    structure: Incomplete
    use_exact_onenorm: Incomplete
    def __init__(self, A, structure: Incomplete | None = None, use_exact_onenorm: bool = False) -> None:
        """
        Initialize the object.

        Parameters
        ----------
        A : a dense or sparse square numpy matrix or ndarray
            The matrix to be exponentiated.
        structure : str, optional
            A string describing the structure of matrix `A`.
            Only `upper_triangular` is currently supported.
        use_exact_onenorm : bool, optional
            If True then only the exact one-norm of matrix powers and products
            will be used. Otherwise, the one-norm of powers and products
            may initially be estimated.
        """
    @property
    def A2(self): ...
    @property
    def A4(self): ...
    @property
    def A6(self): ...
    @property
    def A8(self): ...
    @property
    def A10(self): ...
    @property
    def d4_tight(self): ...
    @property
    def d6_tight(self): ...
    @property
    def d8_tight(self): ...
    @property
    def d10_tight(self): ...
    @property
    def d4_loose(self): ...
    @property
    def d6_loose(self): ...
    @property
    def d8_loose(self): ...
    @property
    def d10_loose(self): ...
    def pade3(self): ...
    def pade5(self): ...
    def pade7(self): ...
    def pade9(self): ...
    def pade13_scaled(self, s): ...

def expm(A):
    '''
    Compute the matrix exponential using Pade approximation.

    Parameters
    ----------
    A : (M,M) array_like or sparse matrix
        2D Array or Matrix (sparse or dense) to be exponentiated

    Returns
    -------
    expA : (M,M) ndarray
        Matrix exponential of `A`

    Notes
    -----
    This is algorithm (6.1) which is a simplification of algorithm (5.1).

    .. versionadded:: 0.12.0

    References
    ----------
    .. [1] Awad H. Al-Mohy and Nicholas J. Higham (2009)
           "A New Scaling and Squaring Algorithm for the Matrix Exponential."
           SIAM Journal on Matrix Analysis and Applications.
           31 (3). pp. 970-989. ISSN 1095-7162

    Examples
    --------
    >>> from scipy.sparse import csc_matrix
    >>> from scipy.sparse.linalg import expm
    >>> A = csc_matrix([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    >>> A.toarray()
    array([[1, 0, 0],
           [0, 2, 0],
           [0, 0, 3]], dtype=int64)
    >>> Aexp = expm(A)
    >>> Aexp
    <3x3 sparse matrix of type \'<class \'numpy.float64\'>\'
        with 3 stored elements in Compressed Sparse Column format>
    >>> Aexp.toarray()
    array([[  2.71828183,   0.        ,   0.        ],
           [  0.        ,   7.3890561 ,   0.        ],
           [  0.        ,   0.        ,  20.08553692]])
    '''
