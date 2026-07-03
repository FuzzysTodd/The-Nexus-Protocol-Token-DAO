from _typeshed import Incomplete
from sympy.assumptions.refine import refine as refine
from sympy.core import Add as Add, SympifyError as SympifyError
from sympy.core.basic import Atom as Atom
from sympy.core.decorators import call_highest_priority as call_highest_priority
from sympy.core.kind import Kind as Kind, NumberKind as NumberKind
from sympy.core.logic import FuzzyBool as FuzzyBool, fuzzy_and as fuzzy_and
from sympy.core.mod import Mod as Mod
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.complexes import Abs as Abs, im as im, re as re
from sympy.polys.polytools import Poly as Poly
from sympy.tensor.array import NDimArray as NDimArray
from sympy.utilities.iterables import flatten as flatten, is_sequence as is_sequence
from sympy.utilities.misc import as_int as as_int, filldedent as filldedent

class MatrixError(Exception): ...
class ShapeError(ValueError, MatrixError):
    """Wrong matrix shape"""
class NonSquareMatrixError(ShapeError): ...
class NonInvertibleMatrixError(ValueError, MatrixError):
    """The matrix in not invertible (division by multidimensional zero error)."""
class NonPositiveDefiniteMatrixError(ValueError, MatrixError):
    """The matrix is not a positive-definite matrix."""

class MatrixRequired:
    """All subclasses of matrix objects must implement the
    required matrix properties listed here."""
    rows: int
    cols: int
    def __eq__(self, other): ...
    def __getitem__(self, key) -> None:
        """Implementations of __getitem__ should accept ints, in which
        case the matrix is indexed as a flat list, tuples (i,j) in which
        case the (i,j) entry is returned, slices, or mixed tuples (a,b)
        where a and b are any combination of slices and integers."""
    def __len__(self) -> int:
        """The total number of entries in the matrix."""
    @property
    def shape(self) -> None: ...

class MatrixShaping(MatrixRequired):
    """Provides basic matrix shaping and extracting of submatrices"""
    def col_del(self, col):
        """Delete the specified column."""
    def col_insert(self, pos, other):
        """Insert one or more columns at the given column position.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(3, 1)
        >>> M.col_insert(1, V)
        Matrix([
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]])

        See Also
        ========

        col
        row_insert
        """
    def col_join(self, other):
        """Concatenates two matrices along self's last and other's first row.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(1, 3)
        >>> M.col_join(V)
        Matrix([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]])

        See Also
        ========

        col
        row_join
        """
    def col(self, j):
        """Elementary column selector.

        Examples
        ========

        >>> from sympy import eye
        >>> eye(2).col(0)
        Matrix([
        [1],
        [0]])

        See Also
        ========

        row
        col_del
        col_join
        col_insert
        """
    def extract(self, rowsList, colsList):
        """Return a submatrix by specifying a list of rows and columns.
        Negative indices can be given. All indices must be in the range
        $-n \\le i < n$ where $n$ is the number of rows or columns.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(4, 3, range(12))
        >>> m
        Matrix([
        [0,  1,  2],
        [3,  4,  5],
        [6,  7,  8],
        [9, 10, 11]])
        >>> m.extract([0, 1, 3], [0, 1])
        Matrix([
        [0,  1],
        [3,  4],
        [9, 10]])

        Rows or columns can be repeated:

        >>> m.extract([0, 0, 1], [-1])
        Matrix([
        [2],
        [2],
        [5]])

        Every other row can be taken by using range to provide the indices:

        >>> m.extract(range(0, m.rows, 2), [-1])
        Matrix([
        [2],
        [8]])

        RowsList or colsList can also be a list of booleans, in which case
        the rows or columns corresponding to the True values will be selected:

        >>> m.extract([0, 1, 2, 3], [True, False, True])
        Matrix([
        [0,  2],
        [3,  5],
        [6,  8],
        [9, 11]])
        """
    def get_diag_blocks(self):
        """Obtains the square sub-matrices on the main diagonal of a square matrix.

        Useful for inverting symbolic matrices or solving systems of
        linear equations which may be decoupled by having a block diagonal
        structure.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y, z
        >>> A = Matrix([[1, 3, 0, 0], [y, z*z, 0, 0], [0, 0, x, 0], [0, 0, 0, 0]])
        >>> a1, a2, a3 = A.get_diag_blocks()
        >>> a1
        Matrix([
        [1,    3],
        [y, z**2]])
        >>> a2
        Matrix([[x]])
        >>> a3
        Matrix([[0]])

        """
    @classmethod
    def hstack(cls, *args):
        """Return a matrix formed by joining args horizontally (i.e.
        by repeated application of row_join).

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> Matrix.hstack(eye(2), 2*eye(2))
        Matrix([
        [1, 0, 2, 0],
        [0, 1, 0, 2]])
        """
    def reshape(self, rows, cols):
        """Reshape the matrix. Total number of elements must remain the same.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 3, lambda i, j: 1)
        >>> m
        Matrix([
        [1, 1, 1],
        [1, 1, 1]])
        >>> m.reshape(1, 6)
        Matrix([[1, 1, 1, 1, 1, 1]])
        >>> m.reshape(3, 2)
        Matrix([
        [1, 1],
        [1, 1],
        [1, 1]])

        """
    def row_del(self, row):
        """Delete the specified row."""
    def row_insert(self, pos, other):
        """Insert one or more rows at the given row position.

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(1, 3)
        >>> M.row_insert(1, V)
        Matrix([
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]])

        See Also
        ========

        row
        col_insert
        """
    def row_join(self, other):
        """Concatenates two matrices along self's last and rhs's first column

        Examples
        ========

        >>> from sympy import zeros, ones
        >>> M = zeros(3)
        >>> V = ones(3, 1)
        >>> M.row_join(V)
        Matrix([
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1]])

        See Also
        ========

        row
        col_join
        """
    def diagonal(self, k: int = 0):
        """Returns the kth diagonal of self. The main diagonal
        corresponds to `k=0`; diagonals above and below correspond to
        `k > 0` and `k < 0`, respectively. The values of `self[i, j]`
        for which `j - i = k`, are returned in order of increasing
        `i + j`, starting with `i + j = |k|`.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(3, 3, lambda i, j: j - i); m
        Matrix([
        [ 0,  1, 2],
        [-1,  0, 1],
        [-2, -1, 0]])
        >>> _.diagonal()
        Matrix([[0, 0, 0]])
        >>> m.diagonal(1)
        Matrix([[1, 1]])
        >>> m.diagonal(-2)
        Matrix([[-2]])

        Even though the diagonal is returned as a Matrix, the element
        retrieval can be done with a single index:

        >>> Matrix.diag(1, 2, 3).diagonal()[1]  # instead of [0, 1]
        2

        See Also
        ========

        diag
        """
    def row(self, i):
        """Elementary row selector.

        Examples
        ========

        >>> from sympy import eye
        >>> eye(2).row(0)
        Matrix([[1, 0]])

        See Also
        ========

        col
        row_del
        row_join
        row_insert
        """
    @property
    def shape(self):
        """The shape (dimensions) of the matrix as the 2-tuple (rows, cols).

        Examples
        ========

        >>> from sympy import zeros
        >>> M = zeros(2, 3)
        >>> M.shape
        (2, 3)
        >>> M.rows
        2
        >>> M.cols
        3
        """
    def todok(self):
        """Return the matrix as dictionary of keys.

        Examples
        ========

        >>> from sympy import Matrix
        >>> M = Matrix.eye(3)
        >>> M.todok()
        {(0, 0): 1, (1, 1): 1, (2, 2): 1}
        """
    def tolist(self):
        """Return the Matrix as a nested Python list.

        Examples
        ========

        >>> from sympy import Matrix, ones
        >>> m = Matrix(3, 3, range(9))
        >>> m
        Matrix([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])
        >>> m.tolist()
        [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        >>> ones(3, 0).tolist()
        [[], [], []]

        When there are no rows then it will not be possible to tell how
        many columns were in the original matrix:

        >>> ones(0, 3).tolist()
        []

        """
    def todod(M):
        """Returns matrix as dict of dicts containing non-zero elements of the Matrix

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[0, 1],[0, 3]])
        >>> A
        Matrix([
        [0, 1],
        [0, 3]])
        >>> A.todod()
        {0: {1: 1}, 1: {1: 3}}


        """
    def vec(self):
        """Return the Matrix converted into a one column matrix by stacking columns

        Examples
        ========

        >>> from sympy import Matrix
        >>> m=Matrix([[1, 3], [2, 4]])
        >>> m
        Matrix([
        [1, 3],
        [2, 4]])
        >>> m.vec()
        Matrix([
        [1],
        [2],
        [3],
        [4]])

        See Also
        ========

        vech
        """
    def vech(self, diagonal: bool = True, check_symmetry: bool = True):
        """Reshapes the matrix into a column vector by stacking the
        elements in the lower triangle.

        Parameters
        ==========

        diagonal : bool, optional
            If ``True``, it includes the diagonal elements.

        check_symmetry : bool, optional
            If ``True``, it checks whether the matrix is symmetric.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m=Matrix([[1, 2], [2, 3]])
        >>> m
        Matrix([
        [1, 2],
        [2, 3]])
        >>> m.vech()
        Matrix([
        [1],
        [2],
        [3]])
        >>> m.vech(diagonal=False)
        Matrix([[2]])

        Notes
        =====

        This should work for symmetric matrices and ``vech`` can
        represent symmetric matrices in vector form with less size than
        ``vec``.

        See Also
        ========

        vec
        """
    @classmethod
    def vstack(cls, *args):
        """Return a matrix formed by joining args vertically (i.e.
        by repeated application of col_join).

        Examples
        ========

        >>> from sympy import Matrix, eye
        >>> Matrix.vstack(eye(2), 2*eye(2))
        Matrix([
        [1, 0],
        [0, 1],
        [2, 0],
        [0, 2]])
        """

class MatrixSpecial(MatrixRequired):
    """Construction of special matrices"""
    @classmethod
    def diag(kls, *args, strict: bool = False, unpack: bool = True, rows: Incomplete | None = None, cols: Incomplete | None = None, **kwargs):
        '''Returns a matrix with the specified diagonal.
        If matrices are passed, a block-diagonal matrix
        is created (i.e. the "direct sum" of the matrices).

        kwargs
        ======

        rows : rows of the resulting matrix; computed if
               not given.

        cols : columns of the resulting matrix; computed if
               not given.

        cls : class for the resulting matrix

        unpack : bool which, when True (default), unpacks a single
        sequence rather than interpreting it as a Matrix.

        strict : bool which, when False (default), allows Matrices to
        have variable-length rows.

        Examples
        ========

        >>> from sympy import Matrix
        >>> Matrix.diag(1, 2, 3)
        Matrix([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]])

        The current default is to unpack a single sequence. If this is
        not desired, set `unpack=False` and it will be interpreted as
        a matrix.

        >>> Matrix.diag([1, 2, 3]) == Matrix.diag(1, 2, 3)
        True

        When more than one element is passed, each is interpreted as
        something to put on the diagonal. Lists are converted to
        matrices. Filling of the diagonal always continues from
        the bottom right hand corner of the previous item: this
        will create a block-diagonal matrix whether the matrices
        are square or not.

        >>> col = [1, 2, 3]
        >>> row = [[4, 5]]
        >>> Matrix.diag(col, row)
        Matrix([
        [1, 0, 0],
        [2, 0, 0],
        [3, 0, 0],
        [0, 4, 5]])

        When `unpack` is False, elements within a list need not all be
        of the same length. Setting `strict` to True would raise a
        ValueError for the following:

        >>> Matrix.diag([[1, 2, 3], [4, 5], [6]], unpack=False)
        Matrix([
        [1, 2, 3],
        [4, 5, 0],
        [6, 0, 0]])

        The type of the returned matrix can be set with the ``cls``
        keyword.

        >>> from sympy import ImmutableMatrix
        >>> from sympy.utilities.misc import func_name
        >>> func_name(Matrix.diag(1, cls=ImmutableMatrix))
        \'ImmutableDenseMatrix\'

        A zero dimension matrix can be used to position the start of
        the filling at the start of an arbitrary row or column:

        >>> from sympy import ones
        >>> r2 = ones(0, 2)
        >>> Matrix.diag(r2, 1, 2)
        Matrix([
        [0, 0, 1, 0],
        [0, 0, 0, 2]])

        See Also
        ========
        eye
        diagonal
        .dense.diag
        .expressions.blockmatrix.BlockMatrix
        .sparsetools.banded
       '''
    @classmethod
    def eye(kls, rows, cols: Incomplete | None = None, **kwargs):
        """Returns an identity matrix.

        Parameters
        ==========

        rows : rows of the matrix
        cols : cols of the matrix (if None, cols=rows)

        kwargs
        ======
        cls : class of the returned matrix
        """
    @classmethod
    def jordan_block(kls, size: Incomplete | None = None, eigenvalue: Incomplete | None = None, *, band: str = 'upper', **kwargs):
        """Returns a Jordan block

        Parameters
        ==========

        size : Integer, optional
            Specifies the shape of the Jordan block matrix.

        eigenvalue : Number or Symbol
            Specifies the value for the main diagonal of the matrix.

            .. note::
                The keyword ``eigenval`` is also specified as an alias
                of this keyword, but it is not recommended to use.

                We may deprecate the alias in later release.

        band : 'upper' or 'lower', optional
            Specifies the position of the off-diagonal to put `1` s on.

        cls : Matrix, optional
            Specifies the matrix class of the output form.

            If it is not specified, the class type where the method is
            being executed on will be returned.

        Returns
        =======

        Matrix
            A Jordan block matrix.

        Raises
        ======

        ValueError
            If insufficient arguments are given for matrix size
            specification, or no eigenvalue is given.

        Examples
        ========

        Creating a default Jordan block:

        >>> from sympy import Matrix
        >>> from sympy.abc import x
        >>> Matrix.jordan_block(4, x)
        Matrix([
        [x, 1, 0, 0],
        [0, x, 1, 0],
        [0, 0, x, 1],
        [0, 0, 0, x]])

        Creating an alternative Jordan block matrix where `1` is on
        lower off-diagonal:

        >>> Matrix.jordan_block(4, x, band='lower')
        Matrix([
        [x, 0, 0, 0],
        [1, x, 0, 0],
        [0, 1, x, 0],
        [0, 0, 1, x]])

        Creating a Jordan block with keyword arguments

        >>> Matrix.jordan_block(size=4, eigenvalue=x)
        Matrix([
        [x, 1, 0, 0],
        [0, x, 1, 0],
        [0, 0, x, 1],
        [0, 0, 0, x]])

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Jordan_matrix
        """
    @classmethod
    def ones(kls, rows, cols: Incomplete | None = None, **kwargs):
        """Returns a matrix of ones.

        Parameters
        ==========

        rows : rows of the matrix
        cols : cols of the matrix (if None, cols=rows)

        kwargs
        ======
        cls : class of the returned matrix
        """
    @classmethod
    def zeros(kls, rows, cols: Incomplete | None = None, **kwargs):
        """Returns a matrix of zeros.

        Parameters
        ==========

        rows : rows of the matrix
        cols : cols of the matrix (if None, cols=rows)

        kwargs
        ======
        cls : class of the returned matrix
        """
    @classmethod
    def companion(kls, poly):
        """Returns a companion matrix of a polynomial.

        Examples
        ========

        >>> from sympy import Matrix, Poly, Symbol, symbols
        >>> x = Symbol('x')
        >>> c0, c1, c2, c3, c4 = symbols('c0:5')
        >>> p = Poly(c0 + c1*x + c2*x**2 + c3*x**3 + c4*x**4 + x**5, x)
        >>> Matrix.companion(p)
        Matrix([
        [0, 0, 0, 0, -c0],
        [1, 0, 0, 0, -c1],
        [0, 1, 0, 0, -c2],
        [0, 0, 1, 0, -c3],
        [0, 0, 0, 1, -c4]])
        """
    @classmethod
    def wilkinson(kls, n, **kwargs):
        """Returns two square Wilkinson Matrix of size 2*n + 1
        $W_{2n + 1}^-, W_{2n + 1}^+ =$ Wilkinson(n)

        Examples
        ========

        >>> from sympy import Matrix
        >>> wminus, wplus = Matrix.wilkinson(3)
        >>> wminus
        Matrix([
        [-3,  1,  0, 0, 0, 0, 0],
        [ 1, -2,  1, 0, 0, 0, 0],
        [ 0,  1, -1, 1, 0, 0, 0],
        [ 0,  0,  1, 0, 1, 0, 0],
        [ 0,  0,  0, 1, 1, 1, 0],
        [ 0,  0,  0, 0, 1, 2, 1],
        [ 0,  0,  0, 0, 0, 1, 3]])
        >>> wplus
        Matrix([
        [3, 1, 0, 0, 0, 0, 0],
        [1, 2, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 2, 1],
        [0, 0, 0, 0, 0, 1, 3]])

        References
        ==========

        .. [1] https://blogs.mathworks.com/cleve/2013/04/15/wilkinsons-matrices-2/
        .. [2] J. H. Wilkinson, The Algebraic Eigenvalue Problem, Claredon Press, Oxford, 1965, 662 pp.

        """

class MatrixProperties(MatrixRequired):
    """Provides basic properties of a matrix."""
    def atoms(self, *types):
        """Returns the atoms that form the current object.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import Matrix
        >>> Matrix([[x]])
        Matrix([[x]])
        >>> _.atoms()
        {x}
        >>> Matrix([[x, y], [y, x]])
        Matrix([
        [x, y],
        [y, x]])
        >>> _.atoms()
        {x, y}
        """
    @property
    def free_symbols(self):
        """Returns the free symbols within the matrix.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import Matrix
        >>> Matrix([[x], [1]]).free_symbols
        {x}
        """
    def has(self, *patterns):
        """Test whether any subexpression matches any of the patterns.

        Examples
        ========

        >>> from sympy import Matrix, SparseMatrix, Float
        >>> from sympy.abc import x, y
        >>> A = Matrix(((1, x), (0.2, 3)))
        >>> B = SparseMatrix(((1, x), (0.2, 3)))
        >>> A.has(x)
        True
        >>> A.has(y)
        False
        >>> A.has(Float)
        True
        >>> B.has(x)
        True
        >>> B.has(y)
        False
        >>> B.has(Float)
        True
        """
    def is_anti_symmetric(self, simplify: bool = True):
        """Check if matrix M is an antisymmetric matrix,
        that is, M is a square matrix with all M[i, j] == -M[j, i].

        When ``simplify=True`` (default), the sum M[i, j] + M[j, i] is
        simplified before testing to see if it is zero. By default,
        the SymPy simplify function is used. To use a custom function
        set simplify to a function that accepts a single argument which
        returns a simplified expression. To skip simplification, set
        simplify to False but note that although this will be faster,
        it may induce false negatives.

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> m = Matrix(2, 2, [0, 1, -1, 0])
        >>> m
        Matrix([
        [ 0, 1],
        [-1, 0]])
        >>> m.is_anti_symmetric()
        True
        >>> x, y = symbols('x y')
        >>> m = Matrix(2, 3, [0, 0, x, -y, 0, 0])
        >>> m
        Matrix([
        [ 0, 0, x],
        [-y, 0, 0]])
        >>> m.is_anti_symmetric()
        False

        >>> from sympy.abc import x, y
        >>> m = Matrix(3, 3, [0, x**2 + 2*x + 1, y,
        ...                   -(x + 1)**2, 0, x*y,
        ...                   -y, -x*y, 0])

        Simplification of matrix elements is done by default so even
        though two elements which should be equal and opposite would not
        pass an equality test, the matrix is still reported as
        anti-symmetric:

        >>> m[0, 1] == -m[1, 0]
        False
        >>> m.is_anti_symmetric()
        True

        If ``simplify=False`` is used for the case when a Matrix is already
        simplified, this will speed things up. Here, we see that without
        simplification the matrix does not appear anti-symmetric:

        >>> m.is_anti_symmetric(simplify=False)
        False

        But if the matrix were already expanded, then it would appear
        anti-symmetric and simplification in the is_anti_symmetric routine
        is not needed:

        >>> m = m.expand()
        >>> m.is_anti_symmetric(simplify=False)
        True
        """
    def is_diagonal(self):
        """Check if matrix is diagonal,
        that is matrix in which the entries outside the main diagonal are all zero.

        Examples
        ========

        >>> from sympy import Matrix, diag
        >>> m = Matrix(2, 2, [1, 0, 0, 2])
        >>> m
        Matrix([
        [1, 0],
        [0, 2]])
        >>> m.is_diagonal()
        True

        >>> m = Matrix(2, 2, [1, 1, 0, 2])
        >>> m
        Matrix([
        [1, 1],
        [0, 2]])
        >>> m.is_diagonal()
        False

        >>> m = diag(1, 2, 3)
        >>> m
        Matrix([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]])
        >>> m.is_diagonal()
        True

        See Also
        ========

        is_lower
        is_upper
        sympy.matrices.matrices.MatrixEigen.is_diagonalizable
        diagonalize
        """
    @property
    def is_weakly_diagonally_dominant(self):
        """Tests if the matrix is row weakly diagonally dominant.

        Explanation
        ===========

        A $n, n$ matrix $A$ is row weakly diagonally dominant if

        .. math::
            \\left|A_{i, i}\\right| \\ge \\sum_{j = 0, j \\neq i}^{n-1}
            \\left|A_{i, j}\\right| \\quad {\\text{for all }}
            i \\in \\{ 0, ..., n-1 \\}

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[3, -2, 1], [1, -3, 2], [-1, 2, 4]])
        >>> A.is_weakly_diagonally_dominant
        True

        >>> A = Matrix([[-2, 2, 1], [1, 3, 2], [1, -2, 0]])
        >>> A.is_weakly_diagonally_dominant
        False

        >>> A = Matrix([[-4, 2, 1], [1, 6, 2], [1, -2, 5]])
        >>> A.is_weakly_diagonally_dominant
        True

        Notes
        =====

        If you want to test whether a matrix is column diagonally
        dominant, you can apply the test after transposing the matrix.
        """
    @property
    def is_strongly_diagonally_dominant(self):
        """Tests if the matrix is row strongly diagonally dominant.

        Explanation
        ===========

        A $n, n$ matrix $A$ is row strongly diagonally dominant if

        .. math::
            \\left|A_{i, i}\\right| > \\sum_{j = 0, j \\neq i}^{n-1}
            \\left|A_{i, j}\\right| \\quad {\\text{for all }}
            i \\in \\{ 0, ..., n-1 \\}

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[3, -2, 1], [1, -3, 2], [-1, 2, 4]])
        >>> A.is_strongly_diagonally_dominant
        False

        >>> A = Matrix([[-2, 2, 1], [1, 3, 2], [1, -2, 0]])
        >>> A.is_strongly_diagonally_dominant
        False

        >>> A = Matrix([[-4, 2, 1], [1, 6, 2], [1, -2, 5]])
        >>> A.is_strongly_diagonally_dominant
        True

        Notes
        =====

        If you want to test whether a matrix is column diagonally
        dominant, you can apply the test after transposing the matrix.
        """
    @property
    def is_hermitian(self):
        """Checks if the matrix is Hermitian.

        In a Hermitian matrix element i,j is the complex conjugate of
        element j,i.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy import I
        >>> from sympy.abc import x
        >>> a = Matrix([[1, I], [-I, 1]])
        >>> a
        Matrix([
        [ 1, I],
        [-I, 1]])
        >>> a.is_hermitian
        True
        >>> a[0, 0] = 2*I
        >>> a.is_hermitian
        False
        >>> a[0, 0] = x
        >>> a.is_hermitian
        >>> a[0, 1] = a[1, 0]*I
        >>> a.is_hermitian
        False
        """
    @property
    def is_Identity(self) -> FuzzyBool: ...
    @property
    def is_lower_hessenberg(self):
        """Checks if the matrix is in the lower-Hessenberg form.

        The lower hessenberg matrix has zero entries
        above the first superdiagonal.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[1, 2, 0, 0], [5, 2, 3, 0], [3, 4, 3, 7], [5, 6, 1, 1]])
        >>> a
        Matrix([
        [1, 2, 0, 0],
        [5, 2, 3, 0],
        [3, 4, 3, 7],
        [5, 6, 1, 1]])
        >>> a.is_lower_hessenberg
        True

        See Also
        ========

        is_upper_hessenberg
        is_lower
        """
    @property
    def is_lower(self):
        """Check if matrix is a lower triangular matrix. True can be returned
        even if the matrix is not square.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [1, 0, 0, 1])
        >>> m
        Matrix([
        [1, 0],
        [0, 1]])
        >>> m.is_lower
        True

        >>> m = Matrix(4, 3, [0, 0, 0, 2, 0, 0, 1, 4, 0, 6, 6, 5])
        >>> m
        Matrix([
        [0, 0, 0],
        [2, 0, 0],
        [1, 4, 0],
        [6, 6, 5]])
        >>> m.is_lower
        True

        >>> from sympy.abc import x, y
        >>> m = Matrix(2, 2, [x**2 + y, y**2 + x, 0, x + y])
        >>> m
        Matrix([
        [x**2 + y, x + y**2],
        [       0,    x + y]])
        >>> m.is_lower
        False

        See Also
        ========

        is_upper
        is_diagonal
        is_lower_hessenberg
        """
    @property
    def is_square(self):
        """Checks if a matrix is square.

        A matrix is square if the number of rows equals the number of columns.
        The empty matrix is square by definition, since the number of rows and
        the number of columns are both zero.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> c = Matrix([])
        >>> a.is_square
        False
        >>> b.is_square
        True
        >>> c.is_square
        True
        """
    def is_symbolic(self):
        """Checks if any elements contain Symbols.

        Examples
        ========

        >>> from sympy import Matrix
        >>> from sympy.abc import x, y
        >>> M = Matrix([[x, y], [1, 0]])
        >>> M.is_symbolic()
        True

        """
    def is_symmetric(self, simplify: bool = True):
        """Check if matrix is symmetric matrix,
        that is square matrix and is equal to its transpose.

        By default, simplifications occur before testing symmetry.
        They can be skipped using 'simplify=False'; while speeding things a bit,
        this may however induce false negatives.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [0, 1, 1, 2])
        >>> m
        Matrix([
        [0, 1],
        [1, 2]])
        >>> m.is_symmetric()
        True

        >>> m = Matrix(2, 2, [0, 1, 2, 0])
        >>> m
        Matrix([
        [0, 1],
        [2, 0]])
        >>> m.is_symmetric()
        False

        >>> m = Matrix(2, 3, [0, 0, 0, 0, 0, 0])
        >>> m
        Matrix([
        [0, 0, 0],
        [0, 0, 0]])
        >>> m.is_symmetric()
        False

        >>> from sympy.abc import x, y
        >>> m = Matrix(3, 3, [1, x**2 + 2*x + 1, y, (x + 1)**2, 2, 0, y, 0, 3])
        >>> m
        Matrix([
        [         1, x**2 + 2*x + 1, y],
        [(x + 1)**2,              2, 0],
        [         y,              0, 3]])
        >>> m.is_symmetric()
        True

        If the matrix is already simplified, you may speed-up is_symmetric()
        test by using 'simplify=False'.

        >>> bool(m.is_symmetric(simplify=False))
        False
        >>> m1 = m.expand()
        >>> m1.is_symmetric(simplify=False)
        True
        """
    @property
    def is_upper_hessenberg(self):
        """Checks if the matrix is the upper-Hessenberg form.

        The upper hessenberg matrix has zero entries
        below the first subdiagonal.

        Examples
        ========

        >>> from sympy import Matrix
        >>> a = Matrix([[1, 4, 2, 3], [3, 4, 1, 7], [0, 2, 3, 4], [0, 0, 1, 3]])
        >>> a
        Matrix([
        [1, 4, 2, 3],
        [3, 4, 1, 7],
        [0, 2, 3, 4],
        [0, 0, 1, 3]])
        >>> a.is_upper_hessenberg
        True

        See Also
        ========

        is_lower_hessenberg
        is_upper
        """
    @property
    def is_upper(self):
        """Check if matrix is an upper triangular matrix. True can be returned
        even if the matrix is not square.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, [1, 0, 0, 1])
        >>> m
        Matrix([
        [1, 0],
        [0, 1]])
        >>> m.is_upper
        True

        >>> m = Matrix(4, 3, [5, 1, 9, 0, 4, 6, 0, 0, 5, 0, 0, 0])
        >>> m
        Matrix([
        [5, 1, 9],
        [0, 4, 6],
        [0, 0, 5],
        [0, 0, 0]])
        >>> m.is_upper
        True

        >>> m = Matrix(2, 3, [4, 2, 5, 6, 1, 1])
        >>> m
        Matrix([
        [4, 2, 5],
        [6, 1, 1]])
        >>> m.is_upper
        False

        See Also
        ========

        is_lower
        is_diagonal
        is_upper_hessenberg
        """
    @property
    def is_zero_matrix(self):
        """Checks if a matrix is a zero matrix.

        A matrix is zero if every element is zero.  A matrix need not be square
        to be considered zero.  The empty matrix is zero by the principle of
        vacuous truth.  For a matrix that may or may not be zero (e.g.
        contains a symbol), this will be None

        Examples
        ========

        >>> from sympy import Matrix, zeros
        >>> from sympy.abc import x
        >>> a = Matrix([[0, 0], [0, 0]])
        >>> b = zeros(3, 4)
        >>> c = Matrix([[0, 1], [0, 0]])
        >>> d = Matrix([])
        >>> e = Matrix([[x, 0], [0, 0]])
        >>> a.is_zero_matrix
        True
        >>> b.is_zero_matrix
        True
        >>> c.is_zero_matrix
        False
        >>> d.is_zero_matrix
        True
        >>> e.is_zero_matrix
        """
    def values(self):
        """Return non-zero values of self."""

class MatrixOperations(MatrixRequired):
    """Provides basic matrix shape and elementwise
    operations.  Should not be instantiated directly."""
    def adjoint(self):
        """Conjugate transpose or Hermitian conjugation."""
    def applyfunc(self, f):
        """Apply a function to each element of the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> m = Matrix(2, 2, lambda i, j: i*2+j)
        >>> m
        Matrix([
        [0, 1],
        [2, 3]])
        >>> m.applyfunc(lambda i: 2*i)
        Matrix([
        [0, 2],
        [4, 6]])

        """
    def as_real_imag(self, deep: bool = True, **hints):
        """Returns a tuple containing the (real, imaginary) part of matrix."""
    def conjugate(self):
        """Return the by-element conjugation.

        Examples
        ========

        >>> from sympy import SparseMatrix, I
        >>> a = SparseMatrix(((1, 2 + I), (3, 4), (I, -I)))
        >>> a
        Matrix([
        [1, 2 + I],
        [3,     4],
        [I,    -I]])
        >>> a.C
        Matrix([
        [ 1, 2 - I],
        [ 3,     4],
        [-I,     I]])

        See Also
        ========

        transpose: Matrix transposition
        H: Hermite conjugation
        sympy.matrices.matrices.MatrixBase.D: Dirac conjugation
        """
    def doit(self, **hints): ...
    def evalf(self, n: int = 15, subs: Incomplete | None = None, maxn: int = 100, chop: bool = False, strict: bool = False, quad: Incomplete | None = None, verbose: bool = False):
        """Apply evalf() to each element of self."""
    def expand(self, deep: bool = True, modulus: Incomplete | None = None, power_base: bool = True, power_exp: bool = True, mul: bool = True, log: bool = True, multinomial: bool = True, basic: bool = True, **hints):
        """Apply core.function.expand to each entry of the matrix.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import Matrix
        >>> Matrix(1, 1, [x*(x+1)])
        Matrix([[x*(x + 1)]])
        >>> _.expand()
        Matrix([[x**2 + x]])

        """
    @property
    def H(self):
        """Return Hermite conjugate.

        Examples
        ========

        >>> from sympy import Matrix, I
        >>> m = Matrix((0, 1 + I, 2, 3))
        >>> m
        Matrix([
        [    0],
        [1 + I],
        [    2],
        [    3]])
        >>> m.H
        Matrix([[0, 1 - I, 2, 3]])

        See Also
        ========

        conjugate: By-element conjugation
        sympy.matrices.matrices.MatrixBase.D: Dirac conjugation
        """
    def permute(self, perm, orientation: str = 'rows', direction: str = 'forward'):
        """Permute the rows or columns of a matrix by the given list of
        swaps.

        Parameters
        ==========

        perm : Permutation, list, or list of lists
            A representation for the permutation.

            If it is ``Permutation``, it is used directly with some
            resizing with respect to the matrix size.

            If it is specified as list of lists,
            (e.g., ``[[0, 1], [0, 2]]``), then the permutation is formed
            from applying the product of cycles. The direction how the
            cyclic product is applied is described in below.

            If it is specified as a list, the list should represent
            an array form of a permutation. (e.g., ``[1, 2, 0]``) which
            would would form the swapping function
            `0 \\mapsto 1, 1 \\mapsto 2, 2\\mapsto 0`.

        orientation : 'rows', 'cols'
            A flag to control whether to permute the rows or the columns

        direction : 'forward', 'backward'
            A flag to control whether to apply the permutations from
            the start of the list first, or from the back of the list
            first.

            For example, if the permutation specification is
            ``[[0, 1], [0, 2]]``,

            If the flag is set to ``'forward'``, the cycle would be
            formed as `0 \\mapsto 2, 2 \\mapsto 1, 1 \\mapsto 0`.

            If the flag is set to ``'backward'``, the cycle would be
            formed as `0 \\mapsto 1, 1 \\mapsto 2, 2 \\mapsto 0`.

            If the argument ``perm`` is not in a form of list of lists,
            this flag takes no effect.

        Examples
        ========

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.permute([[0, 1], [0, 2]], orientation='rows', direction='forward')
        Matrix([
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]])

        >>> from sympy import eye
        >>> M = eye(3)
        >>> M.permute([[0, 1], [0, 2]], orientation='rows', direction='backward')
        Matrix([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]])

        Notes
        =====

        If a bijective function
        `\\sigma : \\mathbb{N}_0 \\rightarrow \\mathbb{N}_0` denotes the
        permutation.

        If the matrix `A` is the matrix to permute, represented as
        a horizontal or a vertical stack of vectors:

        .. math::
            A =
            \\begin{bmatrix}
            a_0 \\\\ a_1 \\\\ \\vdots \\\\ a_{n-1}
            \\end{bmatrix} =
            \\begin{bmatrix}
            \\alpha_0 & \\alpha_1 & \\cdots & \\alpha_{n-1}
            \\end{bmatrix}

        If the matrix `B` is the result, the permutation of matrix rows
        is defined as:

        .. math::
            B := \\begin{bmatrix}
            a_{\\sigma(0)} \\\\ a_{\\sigma(1)} \\\\ \\vdots \\\\ a_{\\sigma(n-1)}
            \\end{bmatrix}

        And the permutation of matrix columns is defined as:

        .. math::
            B := \\begin{bmatrix}
            \\alpha_{\\sigma(0)} & \\alpha_{\\sigma(1)} &
            \\cdots & \\alpha_{\\sigma(n-1)}
            \\end{bmatrix}
        """
    def permute_cols(self, swaps, direction: str = 'forward'):
        """Alias for
        ``self.permute(swaps, orientation='cols', direction=direction)``

        See Also
        ========

        permute
        """
    def permute_rows(self, swaps, direction: str = 'forward'):
        """Alias for
        ``self.permute(swaps, orientation='rows', direction=direction)``

        See Also
        ========

        permute
        """
    def refine(self, assumptions: bool = True):
        """Apply refine to each element of the matrix.

        Examples
        ========

        >>> from sympy import Symbol, Matrix, Abs, sqrt, Q
        >>> x = Symbol('x')
        >>> Matrix([[Abs(x)**2, sqrt(x**2)],[sqrt(x**2), Abs(x)**2]])
        Matrix([
        [ Abs(x)**2, sqrt(x**2)],
        [sqrt(x**2),  Abs(x)**2]])
        >>> _.refine(Q.real(x))
        Matrix([
        [  x**2, Abs(x)],
        [Abs(x),   x**2]])

        """
    def replace(self, F, G, map: bool = False, simultaneous: bool = True, exact: Incomplete | None = None):
        """Replaces Function F in Matrix entries with Function G.

        Examples
        ========

        >>> from sympy import symbols, Function, Matrix
        >>> F, G = symbols('F, G', cls=Function)
        >>> M = Matrix(2, 2, lambda i, j: F(i+j)) ; M
        Matrix([
        [F(0), F(1)],
        [F(1), F(2)]])
        >>> N = M.replace(F,G)
        >>> N
        Matrix([
        [G(0), G(1)],
        [G(1), G(2)]])
        """
    def rot90(self, k: int = 1):
        """Rotates Matrix by 90 degrees

        Parameters
        ==========

        k : int
            Specifies how many times the matrix is rotated by 90 degrees
            (clockwise when positive, counter-clockwise when negative).

        Examples
        ========

        >>> from sympy import Matrix, symbols
        >>> A = Matrix(2, 2, symbols('a:d'))
        >>> A
        Matrix([
        [a, b],
        [c, d]])

        Rotating the matrix clockwise one time:

        >>> A.rot90(1)
        Matrix([
        [c, a],
        [d, b]])

        Rotating the matrix anticlockwise two times:

        >>> A.rot90(-2)
        Matrix([
        [d, c],
        [b, a]])
        """
    def simplify(self, **kwargs):
        """Apply simplify to each element of the matrix.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, sin, cos
        >>> SparseMatrix(1, 1, [x*sin(y)**2 + x*cos(y)**2])
        Matrix([[x*sin(y)**2 + x*cos(y)**2]])
        >>> _.simplify()
        Matrix([[x]])
        """
    def subs(self, *args, **kwargs):
        """Return a new matrix with subs applied to each entry.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, Matrix
        >>> SparseMatrix(1, 1, [x])
        Matrix([[x]])
        >>> _.subs(x, y)
        Matrix([[y]])
        >>> Matrix(_).subs(y, x)
        Matrix([[x]])
        """
    def trace(self):
        """
        Returns the trace of a square matrix i.e. the sum of the
        diagonal elements.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.trace()
        5

        """
    def transpose(self):
        """
        Returns the transpose of the matrix.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.transpose()
        Matrix([
        [1, 3],
        [2, 4]])

        >>> from sympy import Matrix, I
        >>> m=Matrix(((1, 2+I), (3, 4)))
        >>> m
        Matrix([
        [1, 2 + I],
        [3,     4]])
        >>> m.transpose()
        Matrix([
        [    1, 3],
        [2 + I, 4]])
        >>> m.T == m.transpose()
        True

        See Also
        ========

        conjugate: By-element conjugation

        """
    @property
    def T(self):
        """Matrix transposition"""
    @property
    def C(self):
        """By-element conjugation"""
    def n(self, *args, **kwargs):
        """Apply evalf() to each element of self."""
    def xreplace(self, rule):
        """Return a new matrix with xreplace applied to each entry.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import SparseMatrix, Matrix
        >>> SparseMatrix(1, 1, [x])
        Matrix([[x]])
        >>> _.xreplace({x: y})
        Matrix([[y]])
        >>> Matrix(_).xreplace({y: x})
        Matrix([[x]])
        """
    def upper_triangular(self, k: int = 0):
        """Return the elements on and above the kth diagonal of a matrix.
        If k is not specified then simply returns upper-triangular portion
        of a matrix

        Examples
        ========

        >>> from sympy import ones
        >>> A = ones(4)
        >>> A.upper_triangular()
        Matrix([
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 1]])

        >>> A.upper_triangular(2)
        Matrix([
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])

        >>> A.upper_triangular(-1)
        Matrix([
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]])

        """
    def lower_triangular(self, k: int = 0):
        """Return the elements on and below the kth diagonal of a matrix.
        If k is not specified then simply returns lower-triangular portion
        of a matrix

        Examples
        ========

        >>> from sympy import ones
        >>> A = ones(4)
        >>> A.lower_triangular()
        Matrix([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]])

        >>> A.lower_triangular(-2)
        Matrix([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0]])

        >>> A.lower_triangular(1)
        Matrix([
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1]])

        """

class MatrixArithmetic(MatrixRequired):
    """Provides basic matrix arithmetic operations.
    Should not be instantiated directly."""
    def __abs__(self):
        """Returns a new matrix with entry-wise absolute values."""
    def __add__(self, other):
        """Return self + other, raising ShapeError if shapes do not match."""
    def __truediv__(self, other): ...
    def __matmul__(self, other): ...
    def __mod__(self, other): ...
    def __mul__(self, other):
        """Return self*other where other is either a scalar or a matrix
        of compatible dimensions.

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> 2*A == A*2 == Matrix([[2, 4, 6], [8, 10, 12]])
        True
        >>> B = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> A*B
        Matrix([
        [30, 36, 42],
        [66, 81, 96]])
        >>> B*A
        Traceback (most recent call last):
        ...
        ShapeError: Matrices size mismatch.
        >>>

        See Also
        ========

        matrix_multiply_elementwise
        """
    def multiply(self, other, dotprodsimp: Incomplete | None = None):
        """Same as __mul__() but with optional simplification.

        Parameters
        ==========

        dotprodsimp : bool, optional
            Specifies whether intermediate term algebraic simplification is used
            during matrix multiplications to control expression blowup and thus
            speed up calculation. Default is off.
        """
    def multiply_elementwise(self, other):
        """Return the Hadamard product (elementwise product) of A and B

        Examples
        ========

        >>> from sympy import Matrix
        >>> A = Matrix([[0, 1, 2], [3, 4, 5]])
        >>> B = Matrix([[1, 10, 100], [100, 10, 1]])
        >>> A.multiply_elementwise(B)
        Matrix([
        [  0, 10, 200],
        [300, 40,   5]])

        See Also
        ========

        sympy.matrices.matrices.MatrixBase.cross
        sympy.matrices.matrices.MatrixBase.dot
        multiply
        """
    def __neg__(self): ...
    def __pow__(self, exp):
        """Return self**exp a scalar or symbol."""
    def pow(self, exp, method: Incomplete | None = None):
        """Return self**exp a scalar or symbol.

        Parameters
        ==========

        method : multiply, mulsimp, jordan, cayley
            If multiply then it returns exponentiation using recursion.
            If jordan then Jordan form exponentiation will be used.
            If cayley then the exponentiation is done using Cayley-Hamilton
            theorem.
            If mulsimp then the exponentiation is done using recursion
            with dotprodsimp. This specifies whether intermediate term
            algebraic simplification is used during naive matrix power to
            control expression blowup and thus speed up calculation.
            If None, then it heuristically decides which method to use.

        """
    def __radd__(self, other): ...
    def __rmatmul__(self, other): ...
    def __rmul__(self, other): ...
    def rmultiply(self, other, dotprodsimp: Incomplete | None = None):
        """Same as __rmul__() but with optional simplification.

        Parameters
        ==========

        dotprodsimp : bool, optional
            Specifies whether intermediate term algebraic simplification is used
            during matrix multiplications to control expression blowup and thus
            speed up calculation. Default is off.
        """
    def __rsub__(self, a): ...
    def __sub__(self, a): ...

class MatrixCommon(MatrixArithmetic, MatrixOperations, MatrixProperties, MatrixSpecial, MatrixShaping):
    """All common matrix operations including basic arithmetic, shaping,
    and special matrices like `zeros`, and `eye`."""

class _MinimalMatrix:
    """Class providing the minimum functionality
    for a matrix-like object and implementing every method
    required for a `MatrixRequired`.  This class does not have everything
    needed to become a full-fledged SymPy object, but it will satisfy the
    requirements of anything inheriting from `MatrixRequired`.  If you wish
    to make a specialized matrix type, make sure to implement these
    methods and properties with the exception of `__init__` and `__repr__`
    which are included for convenience."""
    is_MatrixLike: bool
    zero: Incomplete
    one: Incomplete
    is_Matrix: bool
    is_MatrixExpr: bool
    mat: Incomplete
    def __init__(self, rows, cols: Incomplete | None = None, mat: Incomplete | None = None, copy: bool = False) -> None: ...
    def __getitem__(self, key): ...
    def __eq__(self, other): ...
    def __len__(self) -> int: ...
    @property
    def shape(self): ...

class _CastableMatrix:
    def as_mutable(self): ...
    def as_immutable(self): ...

class _MatrixWrapper:
    """Wrapper class providing the minimum functionality for a matrix-like
    object: .rows, .cols, .shape, indexability, and iterability. CommonMatrix
    math operations should work on matrix-like objects. This one is intended for
    matrix-like objects which use the same indexing format as SymPy with respect
    to returning matrix elements instead of rows for non-tuple indexes.
    """
    is_Matrix: bool
    is_MatrixLike: bool
    mat: Incomplete
    shape: Incomplete
    def __init__(self, mat, shape) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...

class MatrixKind(Kind):
    """
    Kind for all matrices in SymPy.

    Basic class for this kind is ``MatrixBase`` and ``MatrixExpr``,
    but any expression representing the matrix can have this.

    Parameters
    ==========

    element_kind : Kind
        Kind of the element. Default is
        :class:`sympy.core.kind.NumberKind`,
        which means that the matrix contains only numbers.

    Examples
    ========

    Any instance of matrix class has ``MatrixKind``:

    >>> from sympy import MatrixSymbol
    >>> A = MatrixSymbol('A', 2,2)
    >>> A.kind
    MatrixKind(NumberKind)

    Although expression representing a matrix may be not instance of
    matrix class, it will have ``MatrixKind`` as well:

    >>> from sympy import MatrixExpr, Integral
    >>> from sympy.abc import x
    >>> intM = Integral(A, x)
    >>> isinstance(intM, MatrixExpr)
    False
    >>> intM.kind
    MatrixKind(NumberKind)

    Use ``isinstance()`` to check for ``MatrixKind`` without specifying
    the element kind. Use ``is`` with specifying the element kind:

    >>> from sympy import Matrix
    >>> from sympy.core import NumberKind
    >>> from sympy.matrices import MatrixKind
    >>> M = Matrix([1, 2])
    >>> isinstance(M.kind, MatrixKind)
    True
    >>> M.kind is MatrixKind(NumberKind)
    True

    See Also
    ========

    sympy.core.kind.NumberKind
    sympy.core.kind.UndefinedKind
    sympy.core.containers.TupleKind
    sympy.sets.sets.SetKind

    """
    def __new__(cls, element_kind=...): ...

def a2idx(j, n: Incomplete | None = None):
    """Return integer after making positive and validating against n."""
def classof(A, B):
    """
    Get the type of the result when combining matrices of different types.

    Currently the strategy is that immutability is contagious.

    Examples
    ========

    >>> from sympy import Matrix, ImmutableMatrix
    >>> from sympy.matrices.common import classof
    >>> M = Matrix([[1, 2], [3, 4]]) # a Mutable Matrix
    >>> IM = ImmutableMatrix([[1, 2], [3, 4]])
    >>> classof(M, IM)
    <class 'sympy.matrices.immutable.ImmutableDenseMatrix'>
    """
