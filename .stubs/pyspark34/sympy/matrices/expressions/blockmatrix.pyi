from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.core import Add as Add, Basic as Basic, Mul as Mul, S as S
from sympy.functions import adjoint as adjoint
from sympy.functions.elementary.complexes import im as im, re as re
from sympy.matrices import Matrix as Matrix, ShapeError as ShapeError
from sympy.matrices.common import NonInvertibleMatrixError as NonInvertibleMatrixError
from sympy.matrices.expressions.determinant import Determinant as Determinant, det as det
from sympy.matrices.expressions.inverse import Inverse as Inverse
from sympy.matrices.expressions.matadd import MatAdd as MatAdd
from sympy.matrices.expressions.matexpr import MatrixElement as MatrixElement, MatrixExpr as MatrixExpr
from sympy.matrices.expressions.matmul import MatMul as MatMul
from sympy.matrices.expressions.matpow import MatPow as MatPow
from sympy.matrices.expressions.slice import MatrixSlice as MatrixSlice
from sympy.matrices.expressions.special import Identity as Identity, ZeroMatrix as ZeroMatrix
from sympy.matrices.expressions.trace import trace as trace
from sympy.matrices.expressions.transpose import Transpose as Transpose, transpose as transpose
from sympy.strategies import condition as condition, do_one as do_one, exhaust as exhaust, typed as typed, unpack as unpack
from sympy.strategies.traverse import bottom_up as bottom_up
from sympy.utilities.iterables import is_sequence as is_sequence, sift as sift
from sympy.utilities.misc import filldedent as filldedent

class BlockMatrix(MatrixExpr):
    """A BlockMatrix is a Matrix comprised of other matrices.

    The submatrices are stored in a SymPy Matrix object but accessed as part of
    a Matrix Expression

    >>> from sympy import (MatrixSymbol, BlockMatrix, symbols,
    ...     Identity, ZeroMatrix, block_collapse)
    >>> n,m,l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> Z = MatrixSymbol('Z', n, m)
    >>> B = BlockMatrix([[X, Z], [ZeroMatrix(m,n), Y]])
    >>> print(B)
    Matrix([
    [X, Z],
    [0, Y]])

    >>> C = BlockMatrix([[Identity(n), Z]])
    >>> print(C)
    Matrix([[I, Z]])

    >>> print(block_collapse(C*B))
    Matrix([[X, Z + Z*Y]])

    Some matrices might be comprised of rows of blocks with
    the matrices in each row having the same height and the
    rows all having the same total number of columns but
    not having the same number of columns for each matrix
    in each row. In this case, the matrix is not a block
    matrix and should be instantiated by Matrix.

    >>> from sympy import ones, Matrix
    >>> dat = [
    ... [ones(3,2), ones(3,3)*2],
    ... [ones(2,3)*3, ones(2,2)*4]]
    ...
    >>> BlockMatrix(dat)
    Traceback (most recent call last):
    ...
    ValueError:
    Although this matrix is comprised of blocks, the blocks do not fill
    the matrix in a size-symmetric fashion. To create a full matrix from
    these arguments, pass them directly to Matrix.
    >>> Matrix(dat)
    Matrix([
    [1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [1, 1, 2, 2, 2],
    [3, 3, 3, 4, 4],
    [3, 3, 3, 4, 4]])

    See Also
    ========
    sympy.matrices.matrices.MatrixBase.irregular
    """
    def __new__(cls, *args, **kwargs): ...
    @property
    def shape(self): ...
    @property
    def blockshape(self): ...
    @property
    def blocks(self): ...
    @property
    def rowblocksizes(self): ...
    @property
    def colblocksizes(self): ...
    def structurally_equal(self, other): ...
    def transpose(self):
        """Return transpose of matrix.

        Examples
        ========

        >>> from sympy import MatrixSymbol, BlockMatrix, ZeroMatrix
        >>> from sympy.abc import m, n
        >>> X = MatrixSymbol('X', n, n)
        >>> Y = MatrixSymbol('Y', m, m)
        >>> Z = MatrixSymbol('Z', n, m)
        >>> B = BlockMatrix([[X, Z], [ZeroMatrix(m,n), Y]])
        >>> B.transpose()
        Matrix([
        [X.T,  0],
        [Z.T, Y.T]])
        >>> _.transpose()
        Matrix([
        [X, Z],
        [0, Y]])
        """
    def schur(self, mat: str = 'A', generalized: bool = False):
        '''Return the Schur Complement of the 2x2 BlockMatrix

        Parameters
        ==========

        mat : String, optional
            The matrix with respect to which the
            Schur Complement is calculated. \'A\' is
            used by default

        generalized : bool, optional
            If True, returns the generalized Schur
            Component which uses Moore-Penrose Inverse

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix
        >>> m, n = symbols(\'m n\')
        >>> A = MatrixSymbol(\'A\', n, n)
        >>> B = MatrixSymbol(\'B\', n, m)
        >>> C = MatrixSymbol(\'C\', m, n)
        >>> D = MatrixSymbol(\'D\', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])

        The default Schur Complement is evaluated with "A"

        >>> X.schur()
        -C*A**(-1)*B + D
        >>> X.schur(\'D\')
        A - B*D**(-1)*C

        Schur complement with non-invertible matrices is not
        defined. Instead, the generalized Schur complement can
        be calculated which uses the Moore-Penrose Inverse. To
        achieve this, `generalized` must be set to `True`

        >>> X.schur(\'B\', generalized=True)
        C - D*(B.T*B)**(-1)*B.T*A
        >>> X.schur(\'C\', generalized=True)
        -A*(C.T*C)**(-1)*C.T*D + B

        Returns
        =======

        M : Matrix
            The Schur Complement Matrix

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If given matrix is non-invertible

        References
        ==========

        .. [1] Wikipedia Article on Schur Component : https://en.wikipedia.org/wiki/Schur_complement

        See Also
        ========

        sympy.matrices.matrices.MatrixBase.pinv
        '''
    def LDUdecomposition(self):
        '''Returns the Block LDU decomposition of
        a 2x2 Block Matrix

        Returns
        =======

        (L, D, U) : Matrices
            L : Lower Diagonal Matrix
            D : Diagonal Matrix
            U : Upper Diagonal Matrix

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix, block_collapse
        >>> m, n = symbols(\'m n\')
        >>> A = MatrixSymbol(\'A\', n, n)
        >>> B = MatrixSymbol(\'B\', n, m)
        >>> C = MatrixSymbol(\'C\', m, n)
        >>> D = MatrixSymbol(\'D\', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])
        >>> L, D, U = X.LDUdecomposition()
        >>> block_collapse(L*D*U)
        Matrix([
        [A, B],
        [C, D]])

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If the matrix "A" is non-invertible

        See Also
        ========
        sympy.matrices.expressions.blockmatrix.BlockMatrix.UDLdecomposition
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LUdecomposition
        '''
    def UDLdecomposition(self):
        '''Returns the Block UDL decomposition of
        a 2x2 Block Matrix

        Returns
        =======

        (U, D, L) : Matrices
            U : Upper Diagonal Matrix
            D : Diagonal Matrix
            L : Lower Diagonal Matrix

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix, block_collapse
        >>> m, n = symbols(\'m n\')
        >>> A = MatrixSymbol(\'A\', n, n)
        >>> B = MatrixSymbol(\'B\', n, m)
        >>> C = MatrixSymbol(\'C\', m, n)
        >>> D = MatrixSymbol(\'D\', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])
        >>> U, D, L = X.UDLdecomposition()
        >>> block_collapse(U*D*L)
        Matrix([
        [A, B],
        [C, D]])

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If the matrix "D" is non-invertible

        See Also
        ========
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LDUdecomposition
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LUdecomposition
        '''
    def LUdecomposition(self):
        '''Returns the Block LU decomposition of
        a 2x2 Block Matrix

        Returns
        =======

        (L, U) : Matrices
            L : Lower Diagonal Matrix
            U : Upper Diagonal Matrix

        Examples
        ========

        >>> from sympy import symbols, MatrixSymbol, BlockMatrix, block_collapse
        >>> m, n = symbols(\'m n\')
        >>> A = MatrixSymbol(\'A\', n, n)
        >>> B = MatrixSymbol(\'B\', n, m)
        >>> C = MatrixSymbol(\'C\', m, n)
        >>> D = MatrixSymbol(\'D\', m, m)
        >>> X = BlockMatrix([[A, B], [C, D]])
        >>> L, U = X.LUdecomposition()
        >>> block_collapse(L*U)
        Matrix([
        [A, B],
        [C, D]])

        Raises
        ======

        ShapeError
            If the block matrix is not a 2x2 matrix

        NonInvertibleMatrixError
            If the matrix "A" is non-invertible

        See Also
        ========
        sympy.matrices.expressions.blockmatrix.BlockMatrix.UDLdecomposition
        sympy.matrices.expressions.blockmatrix.BlockMatrix.LDUdecomposition
        '''
    @property
    def is_Identity(self): ...
    @property
    def is_structurally_symmetric(self): ...
    def equals(self, other): ...

class BlockDiagMatrix(BlockMatrix):
    """A sparse matrix with block matrices along its diagonals

    Examples
    ========

    >>> from sympy import MatrixSymbol, BlockDiagMatrix, symbols
    >>> n, m, l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> BlockDiagMatrix(X, Y)
    Matrix([
    [X, 0],
    [0, Y]])

    Notes
    =====

    If you want to get the individual diagonal blocks, use
    :meth:`get_diag_blocks`.

    See Also
    ========

    sympy.matrices.dense.diag
    """
    def __new__(cls, *mats): ...
    @property
    def diag(self): ...
    @property
    def blocks(self): ...
    @property
    def shape(self): ...
    @property
    def blockshape(self): ...
    @property
    def rowblocksizes(self): ...
    @property
    def colblocksizes(self): ...
    def get_diag_blocks(self):
        """Return the list of diagonal blocks of the matrix.

        Examples
        ========

        >>> from sympy import BlockDiagMatrix, Matrix

        >>> A = Matrix([[1, 2], [3, 4]])
        >>> B = Matrix([[5, 6], [7, 8]])
        >>> M = BlockDiagMatrix(A, B)

        How to get diagonal blocks from the block diagonal matrix:

        >>> diag_blocks = M.get_diag_blocks()
        >>> diag_blocks[0]
        Matrix([
        [1, 2],
        [3, 4]])
        >>> diag_blocks[1]
        Matrix([
        [5, 6],
        [7, 8]])
        """

def block_collapse(expr):
    """Evaluates a block matrix expression

    >>> from sympy import MatrixSymbol, BlockMatrix, symbols, Identity, ZeroMatrix, block_collapse
    >>> n,m,l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> Z = MatrixSymbol('Z', n, m)
    >>> B = BlockMatrix([[X, Z], [ZeroMatrix(m, n), Y]])
    >>> print(B)
    Matrix([
    [X, Z],
    [0, Y]])

    >>> C = BlockMatrix([[Identity(n), Z]])
    >>> print(C)
    Matrix([[I, Z]])

    >>> print(block_collapse(C*B))
    Matrix([[X, Z + Z*Y]])
    """
def bc_unpack(expr): ...
def bc_matadd(expr): ...
def bc_block_plus_ident(expr): ...
def bc_dist(expr):
    """ Turn  a*[X, Y] into [a*X, a*Y] """
def bc_matmul(expr): ...
def bc_transpose(expr): ...
def bc_inverse(expr): ...
def blockinverse_1x1(expr): ...
def blockinverse_2x2(expr): ...
def deblock(B):
    """ Flatten a BlockMatrix of BlockMatrices """
def reblock_2x2(expr):
    """
    Reblock a BlockMatrix so that it has 2x2 blocks of block matrices.  If
    possible in such a way that the matrix continues to be invertible using the
    classical 2x2 block inversion formulas.
    """
def bounds(sizes):
    """ Convert sequence of numbers into pairs of low-high pairs

    >>> from sympy.matrices.expressions.blockmatrix import bounds
    >>> bounds((1, 10, 50))
    [(0, 1), (1, 11), (11, 61)]
    """
def blockcut(expr, rowsizes, colsizes):
    """ Cut a matrix expression into Blocks

    >>> from sympy import ImmutableMatrix, blockcut
    >>> M = ImmutableMatrix(4, 4, range(16))
    >>> B = blockcut(M, (1, 3), (1, 3))
    >>> type(B).__name__
    'BlockMatrix'
    >>> ImmutableMatrix(B.blocks[0, 1])
    Matrix([[1, 2, 3]])
    """
