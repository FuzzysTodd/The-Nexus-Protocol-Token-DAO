from .common import classof as classof
from .matrices import MatrixBase as MatrixBase, MatrixKind as MatrixKind, ShapeError as ShapeError
from sympy.core.expr import Expr as Expr
from sympy.core.kind import Kind as Kind, NumberKind as NumberKind, UndefinedKind as UndefinedKind
from sympy.core.numbers import Integer as Integer, Rational as Rational
from sympy.core.singleton import S as S
from sympy.core.sympify import SympifyError as SympifyError
from sympy.polys.domains import EXRAW as EXRAW, QQ as QQ, ZZ as ZZ
from sympy.polys.matrices import DomainMatrix as DomainMatrix
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence
from sympy.utilities.misc import filldedent as filldedent

class RepMatrix(MatrixBase):
    """Matrix implementation based on DomainMatrix as an internal representation.

    The RepMatrix class is a superclass for Matrix, ImmutableMatrix,
    SparseMatrix and ImmutableSparseMatrix which are the main usable matrix
    classes in SymPy. Most methods on this class are simply forwarded to
    DomainMatrix.
    """
    def __eq__(self, other): ...
    def flat(self): ...
    def copy(self): ...
    @property
    def kind(self) -> MatrixKind: ...
    def __getitem__(self, key): ...
    def equals(self, other, failing_expression: bool = False):
        """Applies ``equals`` to corresponding elements of the matrices,
        trying to prove that the elements are equivalent, returning True
        if they are, False if any pair is not, and None (or the first
        failing expression if failing_expression is True) if it cannot
        be decided if the expressions are equivalent or not. This is, in
        general, an expensive operation.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x
        >>> A = Matrix([x*(x - 1), 0])
        >>> B = Matrix([x**2 - x, 0])
        >>> A == B
        False
        >>> A.simplify() == B.simplify()
        True
        >>> A.equals(B)
        True
        >>> A.equals(2)
        False

        See Also
        ========
        sympy.core.expr.Expr.equals
        """

class MutableRepMatrix(RepMatrix):
    """Mutable matrix based on DomainMatrix as the internal representation"""
    is_zero: bool
    def __new__(cls, *args, **kwargs): ...
    def copy(self): ...
    def as_mutable(self): ...
    def __setitem__(self, key, value) -> None:
        """

        Examples
        ========

        >>> from sympy import Matrix, I, zeros, ones
        >>> m = Matrix(((1, 2+I), (3, 4)))
        >>> m
        Matrix([
        [1, 2 + I],
        [3,     4]])
        >>> m[1, 0] = 9
        >>> m
        Matrix([
        [1, 2 + I],
        [9,     4]])
        >>> m[1, 0] = [[0, 1]]

        To replace row r you assign to position r*m where m
        is the number of columns:

        >>> M = zeros(4)
        >>> m = M.cols
        >>> M[3*m] = ones(1, m)*2; M
        Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [2, 2, 2, 2]])

        And to replace column c you can assign to position c:

        >>> M[2] = ones(m, 1)*4; M
        Matrix([
        [0, 0, 4, 0],
        [0, 0, 4, 0],
        [0, 0, 4, 0],
        [2, 2, 4, 2]])
        """
    def col_op(self, j, f) -> None:
        """In-place operation on col j using two-arg functor whose args are
        interpreted as (self[i, j], i).

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.col_op(1, lambda v, i: v + 2*M[i, 0]); M
        Matrix([
        [1, 2, 0],
        [0, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        col
        row_op
        """
    def col_swap(self, i, j) -> None:
        """Swap the two given columns of the matrix in-place.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 0], [1, 0]])
        >>> M
        Matrix([
        [1, 0],
        [1, 0]])
        >>> M.col_swap(0, 1)
        >>> M
        Matrix([
        [0, 1],
        [0, 1]])

        See Also
        ========

        col
        row_swap
        """
    def row_op(self, i, f) -> None:
        """In-place operation on row ``i`` using two-arg functor whose args are
        interpreted as ``(self[i, j], j)``.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.row_op(1, lambda v, j: v + 2*M[0, j]); M
        Matrix([
        [1, 0, 0],
        [2, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        row
        zip_row_op
        col_op

        """
    def row_swap(self, i, j) -> None:
        """Swap the two given rows of the matrix in-place.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[0, 1], [1, 0]])
        >>> M
        Matrix([
        [0, 1],
        [1, 0]])
        >>> M.row_swap(0, 1)
        >>> M
        Matrix([
        [1, 0],
        [0, 1]])

        See Also
        ========

        row
        col_swap
        """
    def zip_row_op(self, i, k, f) -> None:
        """In-place operation on row ``i`` using two-arg functor whose args are
        interpreted as ``(self[i, j], self[k, j])``.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.zip_row_op(1, 0, lambda v, u: v + 2*u); M
        Matrix([
        [1, 0, 0],
        [2, 1, 0],
        [0, 0, 1]])

        See Also
        ========
        row
        row_op
        col_op

        """
    def copyin_list(self, key, value):
        """Copy in elements from a list.

        Parameters
        ==========

        key : slice
            The section of this matrix to replace.
        value : iterable
            The iterable to copy values from.

        Examples
        ========

        >>> from sympy import eye
        >>> I = eye(3)
        >>> I[:2, 0] = [1, 2] # col
        >>> I
        Matrix([
        [1, 0, 0],
        [2, 1, 0],
        [0, 0, 1]])
        >>> I[1, :2] = [[3, 4]]
        >>> I
        Matrix([
        [1, 0, 0],
        [3, 4, 0],
        [0, 0, 1]])

        See Also
        ========

        copyin_matrix
        """
    def copyin_matrix(self, key, value) -> None:
        """Copy in values from a matrix into the given bounds.

        Parameters
        ==========

        key : slice
            The section of this matrix to replace.
        value : Matrix
            The matrix to copy values from.

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> M = Matrix([[0, 1], [2, 3], [4, 5]])
        >>> I = eye(3)
        >>> I[:3, :2] = M
        >>> I
        Matrix([
        [0, 1, 0],
        [2, 3, 0],
        [4, 5, 1]])
        >>> I[0, 1] = M
        >>> I
        Matrix([
        [0, 0, 1],
        [2, 2, 3],
        [4, 4, 5]])

        See Also
        ========

        copyin_list
        """
    def fill(self, value) -> None:
        """Fill self with the given value.

        Notes
        =====

        Unless many values are going to be deleted (i.e. set to zero)
        this will create a matrix that is slower than a dense matrix in
        operations.

        Examples
        ========

        >>> from sympy import SparseMatrix
        >>> M = SparseMatrix.zeros(3); M
        Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]])
        >>> M.fill(1); M
        Matrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]])

        See Also
        ========

        zeros
        ones
        """
