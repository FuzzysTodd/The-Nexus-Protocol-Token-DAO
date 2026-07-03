from .matrices import MatrixBase as MatrixBase
from .repmatrix import MutableRepMatrix as MutableRepMatrix, RepMatrix as RepMatrix
from _typeshed import Incomplete
from sympy.core.containers import Dict as Dict
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.misc import as_int as as_int

class SparseRepMatrix(RepMatrix):
    """
    A sparse matrix (a matrix with a large number of zero elements).

    Examples
    ========

    >>> from sympy import SparseMatrix, ones
    >>> SparseMatrix(2, 2, range(4))
    Matrix([
    [0, 1],
    [2, 3]])
    >>> SparseMatrix(2, 2, {(1, 1): 2})
    Matrix([
    [0, 0],
    [0, 2]])

    A SparseMatrix can be instantiated from a ragged list of lists:

    >>> SparseMatrix([[1, 2, 3], [1, 2], [1]])
    Matrix([
    [1, 2, 3],
    [1, 2, 0],
    [1, 0, 0]])

    For safety, one may include the expected size and then an error
    will be raised if the indices of any element are out of range or
    (for a flat list) if the total number of elements does not match
    the expected shape:

    >>> SparseMatrix(2, 2, [1, 2])
    Traceback (most recent call last):
    ...
    ValueError: List length (2) != rows*columns (4)

    Here, an error is not raised because the list is not flat and no
    element is out of range:

    >>> SparseMatrix(2, 2, [[1, 2]])
    Matrix([
    [1, 2],
    [0, 0]])

    But adding another element to the first (and only) row will cause
    an error to be raised:

    >>> SparseMatrix(2, 2, [[1, 2, 3]])
    Traceback (most recent call last):
    ...
    ValueError: The location (0, 2) is out of designated range: (1, 1)

    To autosize the matrix, pass None for rows:

    >>> SparseMatrix(None, [[1, 2, 3]])
    Matrix([[1, 2, 3]])
    >>> SparseMatrix(None, {(1, 1): 1, (3, 3): 3})
    Matrix([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 3]])

    Values that are themselves a Matrix are automatically expanded:

    >>> SparseMatrix(4, 4, {(1, 1): ones(2)})
    Matrix([
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]])

    A ValueError is raised if the expanding matrix tries to overwrite
    a different element already present:

    >>> SparseMatrix(3, 3, {(0, 0): ones(2), (1, 1): 2})
    Traceback (most recent call last):
    ...
    ValueError: collision at (1, 1)

    See Also
    ========
    DenseMatrix
    MutableSparseMatrix
    ImmutableSparseMatrix
    """
    def applyfunc(self, f):
        """Apply a function to each element of the matrix.

        Examples
        ========

        >>> from sympy import SparseMatrix
        >>> m = SparseMatrix(2, 2, lambda i, j: i*2+j)
        >>> m
        Matrix([
        [0, 1],
        [2, 3]])
        >>> m.applyfunc(lambda i: 2*i)
        Matrix([
        [0, 2],
        [4, 6]])

        """
    def as_immutable(self):
        """Returns an Immutable version of this Matrix."""
    def as_mutable(self):
        """Returns a mutable version of this matrix.

        Examples
        ========

        >>> from sympy import ImmutableMatrix
        >>> X = ImmutableMatrix([[1, 2], [3, 4]])
        >>> Y = X.as_mutable()
        >>> Y[1, 1] = 5 # Can set values in Y
        >>> Y
        Matrix([
        [1, 2],
        [3, 5]])
        """
    def col_list(self):
        """Returns a column-sorted list of non-zero elements of the matrix.

        Examples
        ========

        >>> from sympy import SparseMatrix
        >>> a=SparseMatrix(((1, 2), (3, 4)))
        >>> a
        Matrix([
        [1, 2],
        [3, 4]])
        >>> a.CL
        [(0, 0, 1), (1, 0, 3), (0, 1, 2), (1, 1, 4)]

        See Also
        ========

        sympy.matrices.sparse.SparseMatrix.row_list
        """
    def nnz(self):
        """Returns the number of non-zero elements in Matrix."""
    def row_list(self):
        """Returns a row-sorted list of non-zero elements of the matrix.

        Examples
        ========

        >>> from sympy import SparseMatrix
        >>> a = SparseMatrix(((1, 2), (3, 4)))
        >>> a
        Matrix([
        [1, 2],
        [3, 4]])
        >>> a.RL
        [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4)]

        See Also
        ========

        sympy.matrices.sparse.SparseMatrix.col_list
        """
    def scalar_multiply(self, scalar):
        """Scalar element-wise multiplication"""
    def solve_least_squares(self, rhs, method: str = 'LDL'):
        """Return the least-square fit to the data.

        By default the cholesky_solve routine is used (method='CH'); other
        methods of matrix inversion can be used. To find out which are
        available, see the docstring of the .inv() method.

        Examples
        ========

        >>> from sympy import SparseMatrix, Matrix, ones
        >>> A = Matrix([1, 2, 3])
        >>> B = Matrix([2, 3, 4])
        >>> S = SparseMatrix(A.row_join(B))
        >>> S
        Matrix([
        [1, 2],
        [2, 3],
        [3, 4]])

        If each line of S represent coefficients of Ax + By
        and x and y are [2, 3] then S*xy is:

        >>> r = S*Matrix([2, 3]); r
        Matrix([
        [ 8],
        [13],
        [18]])

        But let's add 1 to the middle value and then solve for the
        least-squares value of xy:

        >>> xy = S.solve_least_squares(Matrix([8, 14, 18])); xy
        Matrix([
        [ 5/3],
        [10/3]])

        The error is given by S*xy - r:

        >>> S*xy - r
        Matrix([
        [1/3],
        [1/3],
        [1/3]])
        >>> _.norm().n(2)
        0.58

        If a different xy is used, the norm will be higher:

        >>> xy += ones(2, 1)/10
        >>> (S*xy - r).norm().n(2)
        1.5

        """
    def solve(self, rhs, method: str = 'LDL'):
        """Return solution to self*soln = rhs using given inversion method.

        For a list of possible inversion methods, see the .inv() docstring.
        """
    RL: Incomplete
    CL: Incomplete
    def liupc(self): ...
    def row_structure_symbolic_cholesky(self): ...
    def cholesky(self, hermitian: bool = True): ...
    def LDLdecomposition(self, hermitian: bool = True): ...
    def lower_triangular_solve(self, rhs): ...
    def upper_triangular_solve(self, rhs): ...

class MutableSparseMatrix(SparseRepMatrix, MutableRepMatrix): ...
SparseMatrix = MutableSparseMatrix
