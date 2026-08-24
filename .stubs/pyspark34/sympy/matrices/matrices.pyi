from .common import MatrixCommon as MatrixCommon, MatrixError as MatrixError, MatrixKind as MatrixKind, NonInvertibleMatrixError as NonInvertibleMatrixError, NonSquareMatrixError as NonSquareMatrixError, ShapeError as ShapeError, a2idx as a2idx
from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.expr import Expr as Expr
from sympy.core.function import diff as diff
from sympy.core.kind import UndefinedKind as UndefinedKind
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol, uniquely_named_symbol as uniquely_named_symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import binomial as binomial, factorial as factorial
from sympy.functions.elementary.complexes import re as re
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min, sqrt as sqrt
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta, LeviCivita as LeviCivita
from sympy.polys import cancel as cancel
from sympy.printing import sstr as sstr
from sympy.printing.defaults import Printable as Printable
from sympy.printing.str import StrPrinter as StrPrinter
from sympy.utilities.iterables import NotIterable as NotIterable, flatten as flatten, is_sequence as is_sequence, reshape as reshape
from sympy.utilities.misc import as_int as as_int, filldedent as filldedent

class DeferredVector(Symbol, NotIterable):
    """A vector whose components are deferred (e.g. for use with lambdify).

    Examples
    ========

    >>> from sympy import DeferredVector, lambdify
    >>> X = DeferredVector( 'X' )
    >>> X
    X
    >>> expr = (X[0] + 2, X[2] + 3)
    >>> func = lambdify( X, expr)
    >>> func( [1, 2, 3] )
    (3, 6)
    """
    def __getitem__(self, i): ...

class MatrixDeterminant(MatrixCommon):
    """Provides basic matrix determinant operations. Should not be instantiated
    directly. See ``determinant.py`` for their implementations."""
    def adjugate(self, method: str = 'berkowitz'): ...
    def charpoly(self, x: str = 'lambda', simplify=...): ...
    def cofactor(self, i, j, method: str = 'berkowitz'): ...
    def cofactor_matrix(self, method: str = 'berkowitz'): ...
    def det(self, method: str = 'bareiss', iszerofunc: Incomplete | None = None): ...
    def per(self): ...
    def minor(self, i, j, method: str = 'berkowitz'): ...
    def minor_submatrix(self, i, j): ...

class MatrixReductions(MatrixDeterminant):
    """Provides basic matrix row/column operations. Should not be instantiated
    directly. See ``reductions.py`` for some of their implementations."""
    def echelon_form(self, iszerofunc=..., simplify: bool = False, with_pivots: bool = False): ...
    @property
    def is_echelon(self): ...
    def rank(self, iszerofunc=..., simplify: bool = False): ...
    def rref(self, iszerofunc=..., simplify: bool = False, pivots: bool = True, normalize_last: bool = True): ...
    def elementary_col_op(self, op: str = 'n->kn', col: Incomplete | None = None, k: Incomplete | None = None, col1: Incomplete | None = None, col2: Incomplete | None = None):
        '''Performs the elementary column operation `op`.

        `op` may be one of

            * ``"n->kn"`` (column n goes to k*n)
            * ``"n<->m"`` (swap column n and column m)
            * ``"n->n+km"`` (column n goes to column n + k*column m)

        Parameters
        ==========

        op : string; the elementary row operation
        col : the column to apply the column operation
        k : the multiple to apply in the column operation
        col1 : one column of a column swap
        col2 : second column of a column swap or column "m" in the column operation
               "n->n+km"
        '''
    def elementary_row_op(self, op: str = 'n->kn', row: Incomplete | None = None, k: Incomplete | None = None, row1: Incomplete | None = None, row2: Incomplete | None = None):
        '''Performs the elementary row operation `op`.

        `op` may be one of

            * ``"n->kn"`` (row n goes to k*n)
            * ``"n<->m"`` (swap row n and row m)
            * ``"n->n+km"`` (row n goes to row n + k*row m)

        Parameters
        ==========

        op : string; the elementary row operation
        row : the row to apply the row operation
        k : the multiple to apply in the row operation
        row1 : one row of a row swap
        row2 : second row of a row swap or row "m" in the row operation
               "n->n+km"
        '''

class MatrixSubspaces(MatrixReductions):
    """Provides methods relating to the fundamental subspaces of a matrix.
    Should not be instantiated directly. See ``subspaces.py`` for their
    implementations."""
    def columnspace(self, simplify: bool = False): ...
    def nullspace(self, simplify: bool = False, iszerofunc=...): ...
    def rowspace(self, simplify: bool = False): ...
    def orthogonalize(cls, *vecs, **kwargs): ...
    orthogonalize: Incomplete

class MatrixEigen(MatrixSubspaces):
    """Provides basic matrix eigenvalue/vector operations.
    Should not be instantiated directly. See ``eigen.py`` for their
    implementations."""
    def eigenvals(self, error_when_incomplete: bool = True, **flags): ...
    def eigenvects(self, error_when_incomplete: bool = True, iszerofunc=..., **flags): ...
    def is_diagonalizable(self, reals_only: bool = False, **kwargs): ...
    def diagonalize(self, reals_only: bool = False, sort: bool = False, normalize: bool = False): ...
    def bidiagonalize(self, upper: bool = True): ...
    def bidiagonal_decomposition(self, upper: bool = True): ...
    @property
    def is_positive_definite(self): ...
    @property
    def is_positive_semidefinite(self): ...
    @property
    def is_negative_definite(self): ...
    @property
    def is_negative_semidefinite(self): ...
    @property
    def is_indefinite(self): ...
    def jordan_form(self, calc_transform: bool = True, **kwargs): ...
    def left_eigenvects(self, **flags): ...
    def singular_values(self): ...

class MatrixCalculus(MatrixCommon):
    """Provides calculus-related matrix operations."""
    def diff(self, *args, **kwargs):
        """Calculate the derivative of each element in the matrix.
        ``args`` will be passed to the ``integrate`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.diff(x)
        Matrix([
        [1, 0],
        [0, 0]])

        See Also
        ========

        integrate
        limit
        """
    def integrate(self, *args, **kwargs):
        """Integrate each element of the matrix.  ``args`` will
        be passed to the ``integrate`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.integrate((x, ))
        Matrix([
        [x**2/2, x*y],
        [     x,   0]])
        >>> M.integrate((x, 0, 2))
        Matrix([
        [2, 2*y],
        [2,   0]])

        See Also
        ========

        limit
        diff
        """
    def jacobian(self, X):
        """Calculates the Jacobian matrix (derivative of a vector-valued function).

        Parameters
        ==========

        ``self`` : vector of expressions representing functions f_i(x_1, ..., x_n).
        X : set of x_i's in order, it can be a list or a Matrix

        Both ``self`` and X can be a row or a column matrix in any order
        (i.e., jacobian() should always work).

        Examples
        ========

        >>> from sympy import sin, cos, Matrix
        >>> from sympy.abc import rho, phi
        >>> X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
        >>> Y = Matrix([rho, phi])
        >>> X.jacobian(Y)
        Matrix([
        [cos(phi), -rho*sin(phi)],
        [sin(phi),  rho*cos(phi)],
        [   2*rho,             0]])
        >>> X = Matrix([rho*cos(phi), rho*sin(phi)])
        >>> X.jacobian(Y)
        Matrix([
        [cos(phi), -rho*sin(phi)],
        [sin(phi),  rho*cos(phi)]])

        See Also
        ========

        hessian
        wronskian
        """
    def limit(self, *args):
        """Calculate the limit of each element in the matrix.
        ``args`` will be passed to the ``limit`` function.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.limit(x, 2)
        Matrix([
        [2, y],
        [1, 0]])

        See Also
        ========

        integrate
        diff
        """

class MatrixDeprecated(MatrixCommon):
    """A class to house deprecated matrix methods."""
    def berkowitz_charpoly(self, x=..., simplify=...): ...
    def berkowitz_det(self):
        """Computes determinant using Berkowitz method.

        See Also
        ========

        det
        berkowitz
        """
    def berkowitz_eigenvals(self, **flags):
        """Computes eigenvalues of a Matrix using Berkowitz method.

        See Also
        ========

        berkowitz
        """
    def berkowitz_minors(self):
        """Computes principal minors using Berkowitz method.

        See Also
        ========

        berkowitz
        """
    def berkowitz(self): ...
    def cofactorMatrix(self, method: str = 'berkowitz'): ...
    def det_bareis(self): ...
    def det_LU_decomposition(self):
        """Compute matrix determinant using LU decomposition.


        Note that this method fails if the LU decomposition itself
        fails. In particular, if the matrix has no inverse this method
        will fail.

        TODO: Implement algorithm for sparse matrices (SFF),
        http://www.eecis.udel.edu/~saunders/papers/sffge/it5.ps.

        See Also
        ========


        det
        det_bareiss
        berkowitz_det
        """
    def jordan_cell(self, eigenval, n): ...
    def jordan_cells(self, calc_transformation: bool = True): ...
    def minorEntry(self, i, j, method: str = 'berkowitz'): ...
    def minorMatrix(self, i, j): ...
    def permuteBkwd(self, perm):
        """Permute the rows of the matrix with the given permutation in reverse."""
    def permuteFwd(self, perm):
        """Permute the rows of the matrix with the given permutation."""

def num_mat_mul(k1, k2):
    """
    Return MatrixKind. The element kind is selected by recursive dispatching.
    Do not need to dispatch in reversed order because KindDispatcher
    searches for this automatically.
    """
def mat_mat_mul(k1, k2):
    """
    Return MatrixKind. The element kind is selected by recursive dispatching.
    """

class MatrixBase(MatrixDeprecated, MatrixCalculus, MatrixEigen, MatrixCommon, Printable):
    """Base class for matrix objects."""
    __array_priority__: int
    is_Matrix: bool
    zero: Incomplete
    one: Incomplete
    @property
    def kind(self) -> MatrixKind: ...
    def flat(self): ...
    def __array__(self, dtype=...): ...
    def __len__(self) -> int:
        """Return the number of elements of ``self``.

        Implemented mainly so bool(Matrix()) == False.
        """
    @classmethod
    def irregular(cls, ntop, *matrices, **kwargs):
        """Return a matrix filled by the given matrices which
      are listed in order of appearance from left to right, top to
      bottom as they first appear in the matrix. They must fill the
      matrix completely.

      Examples
      ========

      >>> from sympy import ones, Matrix
      >>> Matrix.irregular(3, ones(2,1), ones(3,3)*2, ones(2,2)*3,
      ...   ones(1,1)*4, ones(2,2)*5, ones(1,2)*6, ones(1,2)*7)
      Matrix([
        [1, 2, 2, 2, 3, 3],
        [1, 2, 2, 2, 3, 3],
        [4, 2, 2, 2, 5, 5],
        [6, 6, 7, 7, 5, 5]])
      """
    def add(self, b):
        """Return self + b."""
    def condition_number(self):
        """Returns the condition number of a matrix.

        This is the maximum singular value divided by the minimum singular value

        Examples
        ========

        >>> from sympy import Matrix, S
        >>> A = Matrix([[1, 0, 0], [0, 10, 0], [0, 0, S.One/10]])
        >>> A.condition_number()
        100

        See Also
        ========

        singular_values
        """
    def copy(self):
        """
        Returns the copy of a matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.copy()
        Matrix([
        [1, 2],
        [3, 4]])

        """
    def cross(self, b):
        """
        Return the cross product of ``self`` and ``b`` relaxing the condition
        of compatible dimensions: if each has 3 elements, a matrix of the
        same type and shape as ``self`` will be returned. If ``b`` has the same
        shape as ``self`` then common identities for the cross product (like
        `a \\times b = - b \\times a`) will hold.

        Parameters
        ==========
            b : 3x1 or 1x3 Matrix

        See Also
        ========

        dot
        multiply
        multiply_elementwise
        """
    @property
    def D(self):
        """Return Dirac conjugate (if ``self.rows == 4``).

        Examples
        ========

        >>> from sympy import Matrix, I, eye
        >>> m = Matrix((0, 1 + I, 2, 3))
        >>> m.D
        Matrix([[0, 1 - I, -2, -3]])
        >>> m = (eye(4) + I*eye(4))
        >>> m[0, 3] = 2
        >>> m.D
        Matrix([
        [1 - I,     0,      0,      0],
        [    0, 1 - I,      0,      0],
        [    0,     0, -1 + I,      0],
        [    2,     0,      0, -1 + I]])

        If the matrix does not have 4 rows an AttributeError will be raised
        because this property is only defined for matrices with 4 rows.

        >>> Matrix(eye(2)).D
        Traceback (most recent call last):
        ...
        AttributeError: Matrix has no attribute D.

        See Also
        ========

        sympy.matrices.common.MatrixCommon.conjugate: By-element conjugation
        sympy.matrices.common.MatrixCommon.H: Hermite conjugation
        """
    def dot(self, b, hermitian: Incomplete | None = None, conjugate_convention: Incomplete | None = None):
        '''Return the dot or inner product of two vectors of equal length.
        Here ``self`` must be a ``Matrix`` of size 1 x n or n x 1, and ``b``
        must be either a matrix of size 1 x n, n x 1, or a list/tuple of length n.
        A scalar is returned.

        By default, ``dot`` does not conjugate ``self`` or ``b``, even if there are
        complex entries. Set ``hermitian=True`` (and optionally a ``conjugate_convention``)
        to compute the hermitian inner product.

        Possible kwargs are ``hermitian`` and ``conjugate_convention``.

        If ``conjugate_convention`` is ``"left"``, ``"math"`` or ``"maths"``,
        the conjugate of the first vector (``self``) is used.  If ``"right"``
        or ``"physics"`` is specified, the conjugate of the second vector ``b`` is used.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> v = Matrix([1, 1, 1])
        >>> M.row(0).dot(v)
        6
        >>> M.col(0).dot(v)
        12
        >>> v = [3, 2, 1]
        >>> M.row(0).dot(v)
        10

        >>> from sympy import I
        >>> q = Matrix([1*I, 1*I, 1*I])
        >>> q.dot(q, hermitian=False)
        -3

        >>> q.dot(q, hermitian=True)
        3

        >>> q1 = Matrix([1, 1, 1*I])
        >>> q.dot(q1, hermitian=True, conjugate_convention="maths")
        1 - 2*I
        >>> q.dot(q1, hermitian=True, conjugate_convention="physics")
        1 + 2*I


        See Also
        ========

        cross
        multiply
        multiply_elementwise
        '''
    def dual(self):
        """Returns the dual of a matrix.

        A dual of a matrix is:

        ``(1/2)*levicivita(i, j, k, l)*M(k, l)`` summed over indices `k` and `l`

        Since the levicivita method is anti_symmetric for any pairwise
        exchange of indices, the dual of a symmetric matrix is the zero
        matrix. Strictly speaking the dual defined here assumes that the
        'matrix' `M` is a contravariant anti_symmetric second rank tensor,
        so that the dual is a covariant second rank tensor.

        """
    def analytic_func(self, f, x):
        """
        Computes f(A) where A is a Square Matrix
        and f is an analytic function.

        Examples
        ========

        >>> from sympy import Symbol, Matrix, S, log

        >>> x = Symbol('x')
        >>> m = Matrix([[S(5)/4, S(3)/4], [S(3)/4, S(5)/4]])
        >>> f = log(x)
        >>> m.analytic_func(f, x)
        Matrix([
        [     0, log(2)],
        [log(2),      0]])

        Parameters
        ==========

        f : Expr
            Analytic Function
        x : Symbol
            parameter of f

        """
    def exp(self):
        """Return the exponential of a square matrix.

        Examples
        ========

        >>> from sympy import Symbol, Matrix

        >>> t = Symbol('t')
        >>> m = Matrix([[0, 1], [-1, 0]]) * t
        >>> m.exp()
        Matrix([
        [    exp(I*t)/2 + exp(-I*t)/2, -I*exp(I*t)/2 + I*exp(-I*t)/2],
        [I*exp(I*t)/2 - I*exp(-I*t)/2,      exp(I*t)/2 + exp(-I*t)/2]])
        """
    def log(self, simplify=...):
        """Return the logarithm of a square matrix.

        Parameters
        ==========

        simplify : function, bool
            The function to simplify the result with.

            Default is ``cancel``, which is effective to reduce the
            expression growing for taking reciprocals and inverses for
            symbolic matrices.

        Examples
        ========

        >>> from sympy import S, Matrix

        Examples for positive-definite matrices:

        >>> m = Matrix([[1, 1], [0, 1]])
        >>> m.log()
        Matrix([
        [0, 1],
        [0, 0]])

        >>> m = Matrix([[S(5)/4, S(3)/4], [S(3)/4, S(5)/4]])
        >>> m.log()
        Matrix([
        [     0, log(2)],
        [log(2),      0]])

        Examples for non positive-definite matrices:

        >>> m = Matrix([[S(3)/4, S(5)/4], [S(5)/4, S(3)/4]])
        >>> m.log()
        Matrix([
        [         I*pi/2, log(2) - I*pi/2],
        [log(2) - I*pi/2,          I*pi/2]])

        >>> m = Matrix(
        ...     [[0, 0, 0, 1],
        ...      [0, 0, 1, 0],
        ...      [0, 1, 0, 0],
        ...      [1, 0, 0, 0]])
        >>> m.log()
        Matrix([
        [ I*pi/2,       0,       0, -I*pi/2],
        [      0,  I*pi/2, -I*pi/2,       0],
        [      0, -I*pi/2,  I*pi/2,       0],
        [-I*pi/2,       0,       0,  I*pi/2]])
        """
    def is_nilpotent(self):
        """Checks if a matrix is nilpotent.

        A matrix B is nilpotent if for some integer k, B**k is
        a zero matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
        >>> a.is_nilpotent()
        True

        >>> a = Matrix([[1, 0, 1], [1, 0, 0], [1, 1, 0]])
        >>> a.is_nilpotent()
        False
        """
    def key2bounds(self, keys):
        """Converts a key with potentially mixed types of keys (integer and slice)
        into a tuple of ranges and raises an error if any index is out of ``self``'s
        range.

        See Also
        ========

        key2ij
        """
    def key2ij(self, key):
        """Converts key into canonical form, converting integers or indexable
        items into valid integers for ``self``'s range or returning slices
        unchanged.

        See Also
        ========

        key2bounds
        """
    def normalized(self, iszerofunc=...):
        """Return the normalized version of ``self``.

        Parameters
        ==========

        iszerofunc : Function, optional
            A function to determine whether ``self`` is a zero vector.
            The default ``_iszero`` tests to see if each element is
            exactly zero.

        Returns
        =======

        Matrix
            Normalized vector form of ``self``.
            It has the same length as a unit vector. However, a zero vector
            will be returned for a vector with norm 0.

        Raises
        ======

        ShapeError
            If the matrix is not in a vector form.

        See Also
        ========

        norm
        """
    def norm(self, ord: Incomplete | None = None):
        """Return the Norm of a Matrix or Vector.

        In the simplest case this is the geometric size of the vector
        Other norms can be specified by the ord parameter


        =====  ============================  ==========================
        ord    norm for matrices             norm for vectors
        =====  ============================  ==========================
        None   Frobenius norm                2-norm
        'fro'  Frobenius norm                - does not exist
        inf    maximum row sum               max(abs(x))
        -inf   --                            min(abs(x))
        1      maximum column sum            as below
        -1     --                            as below
        2      2-norm (largest sing. value)  as below
        -2     smallest singular value       as below
        other  - does not exist              sum(abs(x)**ord)**(1./ord)
        =====  ============================  ==========================

        Examples
        ========

        >>> from sympy import Matrix, Symbol, trigsimp, cos, sin, oo
        >>> x = Symbol('x', real=True)
        >>> v = Matrix([cos(x), sin(x)])
        >>> trigsimp( v.norm() )
        1
        >>> v.norm(10)
        (sin(x)**10 + cos(x)**10)**(1/10)
        >>> A = Matrix([[1, 1], [1, 1]])
        >>> A.norm(1) # maximum sum of absolute values of A is 2
        2
        >>> A.norm(2) # Spectral norm (max of |Ax|/|x| under 2-vector-norm)
        2
        >>> A.norm(-2) # Inverse spectral norm (smallest singular value)
        0
        >>> A.norm() # Frobenius Norm
        2
        >>> A.norm(oo) # Infinity Norm
        2
        >>> Matrix([1, -2]).norm(oo)
        2
        >>> Matrix([-1, 2]).norm(-oo)
        1

        See Also
        ========

        normalized
        """
    def print_nonzero(self, symb: str = 'X') -> None:
        '''Shows location of non-zero entries for fast shape lookup.

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> m = Matrix(2, 3, lambda i, j: i*3+j)
        >>> m
        Matrix([
        [0, 1, 2],
        [3, 4, 5]])
        >>> m.print_nonzero()
        [ XX]
        [XXX]
        >>> m = eye(4)
        >>> m.print_nonzero("x")
        [x   ]
        [ x  ]
        [  x ]
        [   x]

        '''
    def project(self, v):
        """Return the projection of ``self`` onto the line containing ``v``.

        Examples
        ========

        >>> from sympy import Matrix, S, sqrt
        >>> V = Matrix([sqrt(3)/2, S.Half])
        >>> x = Matrix([[1, 0]])
        >>> V.project(x)
        Matrix([[sqrt(3)/2, 0]])
        >>> V.project(-x)
        Matrix([[sqrt(3)/2, 0]])
        """
    def table(self, printer, rowstart: str = '[', rowend: str = ']', rowsep: str = '\n', colsep: str = ', ', align: str = 'right'):
        """
        String form of Matrix as a table.

        ``printer`` is the printer to use for on the elements (generally
        something like StrPrinter())

        ``rowstart`` is the string used to start each row (by default '[').

        ``rowend`` is the string used to end each row (by default ']').

        ``rowsep`` is the string used to separate rows (by default a newline).

        ``colsep`` is the string used to separate columns (by default ', ').

        ``align`` defines how the elements are aligned. Must be one of 'left',
        'right', or 'center'.  You can also use '<', '>', and '^' to mean the
        same thing, respectively.

        This is used by the string printer for Matrix.

        Examples
        ========

        >>> from sympy import Matrix, StrPrinter
        >>> M = Matrix([[1, 2], [-33, 4]])
        >>> printer = StrPrinter()
        >>> M.table(printer)
        '[  1, 2]\\n[-33, 4]'
        >>> print(M.table(printer))
        [  1, 2]
        [-33, 4]
        >>> print(M.table(printer, rowsep=',\\n'))
        [  1, 2],
        [-33, 4]
        >>> print('[%s]' % M.table(printer, rowsep=',\\n'))
        [[  1, 2],
        [-33, 4]]
        >>> print(M.table(printer, colsep=' '))
        [  1 2]
        [-33 4]
        >>> print(M.table(printer, align='center'))
        [ 1 , 2]
        [-33, 4]
        >>> print(M.table(printer, rowstart='{', rowend='}'))
        {  1, 2}
        {-33, 4}
        """
    def rank_decomposition(self, iszerofunc=..., simplify: bool = False): ...
    def cholesky(self, hermitian: bool = True) -> None: ...
    def LDLdecomposition(self, hermitian: bool = True) -> None: ...
    def LUdecomposition(self, iszerofunc=..., simpfunc: Incomplete | None = None, rankcheck: bool = False): ...
    def LUdecomposition_Simple(self, iszerofunc=..., simpfunc: Incomplete | None = None, rankcheck: bool = False): ...
    def LUdecompositionFF(self): ...
    def singular_value_decomposition(self): ...
    def QRdecomposition(self): ...
    def upper_hessenberg_decomposition(self): ...
    def diagonal_solve(self, rhs): ...
    def lower_triangular_solve(self, rhs) -> None: ...
    def upper_triangular_solve(self, rhs) -> None: ...
    def cholesky_solve(self, rhs): ...
    def LDLsolve(self, rhs): ...
    def LUsolve(self, rhs, iszerofunc=...): ...
    def QRsolve(self, b): ...
    def gauss_jordan_solve(self, B, freevar: bool = False): ...
    def pinv_solve(self, B, arbitrary_matrix: Incomplete | None = None): ...
    def solve(self, rhs, method: str = 'GJ'): ...
    def solve_least_squares(self, rhs, method: str = 'CH'): ...
    def pinv(self, method: str = 'RD'): ...
    def inv_mod(self, m): ...
    def inverse_ADJ(self, iszerofunc=...): ...
    def inverse_BLOCK(self, iszerofunc=...): ...
    def inverse_GE(self, iszerofunc=...): ...
    def inverse_LU(self, iszerofunc=...): ...
    def inverse_CH(self, iszerofunc=...): ...
    def inverse_LDL(self, iszerofunc=...): ...
    def inverse_QR(self, iszerofunc=...): ...
    def inv(self, method: Incomplete | None = None, iszerofunc=..., try_block_diag: bool = False): ...
    def connected_components(self): ...
    def connected_components_decomposition(self): ...
    def strongly_connected_components(self): ...
    def strongly_connected_components_decomposition(self, lower: bool = True): ...
