from .common import ShapeError as ShapeError
from .matrices import MatrixBase as MatrixBase
from .repmatrix import MutableRepMatrix as MutableRepMatrix, RepMatrix as RepMatrix
from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning
from sympy.utilities.iterables import is_sequence as is_sequence

class DenseMatrix(RepMatrix):
    """Matrix implementation based on DomainMatrix as the internal representation"""
    is_MatrixExpr: bool
    def as_immutable(self):
        """Returns an Immutable version of this Matrix
        """
    def as_mutable(self):
        """Returns a mutable version of this matrix

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
    def cholesky(self, hermitian: bool = True): ...
    def LDLdecomposition(self, hermitian: bool = True): ...
    def lower_triangular_solve(self, rhs): ...
    def upper_triangular_solve(self, rhs): ...

class MutableDenseMatrix(DenseMatrix, MutableRepMatrix):
    def simplify(self, **kwargs) -> None:
        """Applies simplify to the elements of a matrix in place.

        This is a shortcut for M.applyfunc(lambda x: simplify(x, ratio, measure))

        See Also
        ========

        sympy.simplify.simplify.simplify
        """
MutableMatrix = MutableDenseMatrix
Matrix = MutableDenseMatrix

def list2numpy(l, dtype=...):
    """Converts Python list of SymPy expressions to a NumPy array.

    See Also
    ========

    matrix2numpy
    """
def matrix2numpy(m, dtype=...):
    """Converts SymPy's matrix to a NumPy array.

    See Also
    ========

    list2numpy
    """
def rot_givens(i, j, theta, dim: int = 3):
    """Returns a a Givens rotation matrix, a a rotation in the
    plane spanned by two coordinates axes.

    Explanation
    ===========

    The Givens rotation corresponds to a generalization of rotation
    matrices to any number of dimensions, given by:

    .. math::
        G(i, j, \\theta) =
            \\begin{bmatrix}
                1   & \\cdots &    0   & \\cdots &    0   & \\cdots &    0   \\\\\n                \\vdots & \\ddots & \\vdots &        & \\vdots &        & \\vdots \\\\\n                0   & \\cdots &    c   & \\cdots &   -s   & \\cdots &    0   \\\\\n                \\vdots &        & \\vdots & \\ddots & \\vdots &        & \\vdots \\\\\n                0   & \\cdots &    s   & \\cdots &    c   & \\cdots &    0   \\\\\n                \\vdots &        & \\vdots &        & \\vdots & \\ddots & \\vdots \\\\\n                0   & \\cdots &    0   & \\cdots &    0   & \\cdots &    1
            \\end{bmatrix}

    Where $c = \\cos(\\theta)$ and $s = \\sin(\\theta)$ appear at the intersections
    ``i``\\th and ``j``\\th rows and columns.

    For fixed ``i > j``\\, the non-zero elements of a Givens matrix are
    given by:

    - $g_{kk} = 1$ for $k \\ne i,\\,j$
    - $g_{kk} = c$ for $k = i,\\,j$
    - $g_{ji} = -g_{ij} = -s$

    Parameters
    ==========

    i : int between ``0`` and ``dim - 1``
        Represents first axis
    j : int between ``0`` and ``dim - 1``
        Represents second axis
    dim : int bigger than 1
        Number of dimentions. Defaults to 3.

    Examples
    ========

    >>> from sympy import pi, rot_givens

    A counterclockwise rotation of pi/3 (60 degrees) around
    the third axis (z-axis):

    >>> rot_givens(1, 0, pi/3)
    Matrix([
    [      1/2, -sqrt(3)/2, 0],
    [sqrt(3)/2,        1/2, 0],
    [        0,          0, 1]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_givens(1, 0, pi/2)
    Matrix([
    [0, -1, 0],
    [1,  0, 0],
    [0,  0, 1]])

    This can be generalized to any number
    of dimensions:

    >>> rot_givens(1, 0, pi/2, dim=4)
    Matrix([
    [0, -1, 0, 0],
    [1,  0, 0, 0],
    [0,  0, 1, 0],
    [0,  0, 0, 1]])

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Givens_rotation

    See Also
    ========

    rot_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (clockwise around the x axis)
    rot_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (clockwise around the y axis)
    rot_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (clockwise around the z axis)
    rot_ccw_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (counterclockwise around the x axis)
    rot_ccw_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (counterclockwise around the y axis)
    rot_ccw_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (counterclockwise around the z axis)
    """
def rot_axis3(theta):
    """Returns a rotation matrix for a rotation of theta (in radians)
    about the 3-axis.

    Explanation
    ===========

    For a right-handed coordinate system, this corresponds to a
    clockwise rotation around the `z`-axis, given by:

    .. math::

        R  = \\begin{bmatrix}
                 \\cos(\\theta) & \\sin(\\theta) & 0 \\\\\n                -\\sin(\\theta) & \\cos(\\theta) & 0 \\\\\n                            0 &            0 & 1
            \\end{bmatrix}

    Examples
    ========

    >>> from sympy import pi, rot_axis3

    A rotation of pi/3 (60 degrees):

    >>> theta = pi/3
    >>> rot_axis3(theta)
    Matrix([
    [       1/2, sqrt(3)/2, 0],
    [-sqrt(3)/2,       1/2, 0],
    [         0,         0, 1]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_axis3(pi/2)
    Matrix([
    [ 0, 1, 0],
    [-1, 0, 0],
    [ 0, 0, 1]])

    See Also
    ========

    rot_givens: Returns a Givens rotation matrix (generalized rotation for
        any number of dimensions)
    rot_ccw_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (counterclockwise around the z axis)
    rot_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (clockwise around the x axis)
    rot_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (clockwise around the y axis)
    """
def rot_axis2(theta):
    """Returns a rotation matrix for a rotation of theta (in radians)
    about the 2-axis.

    Explanation
    ===========

    For a right-handed coordinate system, this corresponds to a
    clockwise rotation around the `y`-axis, given by:

    .. math::

        R  = \\begin{bmatrix}
                \\cos(\\theta) & 0 & -\\sin(\\theta) \\\\\n                           0 & 1 &             0 \\\\\n                \\sin(\\theta) & 0 &  \\cos(\\theta)
            \\end{bmatrix}

    Examples
    ========

    >>> from sympy import pi, rot_axis2

    A rotation of pi/3 (60 degrees):

    >>> theta = pi/3
    >>> rot_axis2(theta)
    Matrix([
    [      1/2, 0, -sqrt(3)/2],
    [        0, 1,          0],
    [sqrt(3)/2, 0,        1/2]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_axis2(pi/2)
    Matrix([
    [0, 0, -1],
    [0, 1,  0],
    [1, 0,  0]])

    See Also
    ========

    rot_givens: Returns a Givens rotation matrix (generalized rotation for
        any number of dimensions)
    rot_ccw_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (clockwise around the y axis)
    rot_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (counterclockwise around the x axis)
    rot_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (counterclockwise around the z axis)
    """
def rot_axis1(theta):
    """Returns a rotation matrix for a rotation of theta (in radians)
    about the 1-axis.

    Explanation
    ===========

    For a right-handed coordinate system, this corresponds to a
    clockwise rotation around the `x`-axis, given by:

    .. math::

        R  = \\begin{bmatrix}
                1 &             0 &            0 \\\\\n                0 &  \\cos(\\theta) & \\sin(\\theta) \\\\\n                0 & -\\sin(\\theta) & \\cos(\\theta)
            \\end{bmatrix}

    Examples
    ========

    >>> from sympy import pi, rot_axis1

    A rotation of pi/3 (60 degrees):

    >>> theta = pi/3
    >>> rot_axis1(theta)
    Matrix([
    [1,          0,         0],
    [0,        1/2, sqrt(3)/2],
    [0, -sqrt(3)/2,       1/2]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_axis1(pi/2)
    Matrix([
    [1,  0, 0],
    [0,  0, 1],
    [0, -1, 0]])

    See Also
    ========

    rot_givens: Returns a Givens rotation matrix (generalized rotation for
        any number of dimensions)
    rot_ccw_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (counterclockwise around the x axis)
    rot_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (clockwise around the y axis)
    rot_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (clockwise around the z axis)
    """
def rot_ccw_axis3(theta):
    """Returns a rotation matrix for a rotation of theta (in radians)
    about the 3-axis.

    Explanation
    ===========

    For a right-handed coordinate system, this corresponds to a
    counterclockwise rotation around the `z`-axis, given by:

    .. math::

        R  = \\begin{bmatrix}
                \\cos(\\theta) & -\\sin(\\theta) & 0 \\\\\n                \\sin(\\theta) &  \\cos(\\theta) & 0 \\\\\n                           0 &             0 & 1
            \\end{bmatrix}

    Examples
    ========

    >>> from sympy import pi, rot_ccw_axis3

    A rotation of pi/3 (60 degrees):

    >>> theta = pi/3
    >>> rot_ccw_axis3(theta)
    Matrix([
    [      1/2, -sqrt(3)/2, 0],
    [sqrt(3)/2,        1/2, 0],
    [        0,          0, 1]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_ccw_axis3(pi/2)
    Matrix([
    [0, -1, 0],
    [1,  0, 0],
    [0,  0, 1]])

    See Also
    ========

    rot_givens: Returns a Givens rotation matrix (generalized rotation for
        any number of dimensions)
    rot_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (clockwise around the z axis)
    rot_ccw_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (counterclockwise around the x axis)
    rot_ccw_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (counterclockwise around the y axis)
    """
def rot_ccw_axis2(theta):
    """Returns a rotation matrix for a rotation of theta (in radians)
    about the 2-axis.

    Explanation
    ===========

    For a right-handed coordinate system, this corresponds to a
    counterclockwise rotation around the `y`-axis, given by:

    .. math::

        R  = \\begin{bmatrix}
                 \\cos(\\theta) & 0 & \\sin(\\theta) \\\\\n                            0 & 1 &            0 \\\\\n                -\\sin(\\theta) & 0 & \\cos(\\theta)
            \\end{bmatrix}

    Examples
    ========

    >>> from sympy import pi, rot_ccw_axis2

    A rotation of pi/3 (60 degrees):

    >>> theta = pi/3
    >>> rot_ccw_axis2(theta)
    Matrix([
    [       1/2, 0, sqrt(3)/2],
    [         0, 1,         0],
    [-sqrt(3)/2, 0,       1/2]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_ccw_axis2(pi/2)
    Matrix([
    [ 0,  0,  1],
    [ 0,  1,  0],
    [-1,  0,  0]])

    See Also
    ========

    rot_givens: Returns a Givens rotation matrix (generalized rotation for
        any number of dimensions)
    rot_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (clockwise around the y axis)
    rot_ccw_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (counterclockwise around the x axis)
    rot_ccw_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (counterclockwise around the z axis)
    """
def rot_ccw_axis1(theta):
    """Returns a rotation matrix for a rotation of theta (in radians)
    about the 1-axis.

    Explanation
    ===========

    For a right-handed coordinate system, this corresponds to a
    counterclockwise rotation around the `x`-axis, given by:

    .. math::

        R  = \\begin{bmatrix}
                1 &            0 &             0 \\\\\n                0 & \\cos(\\theta) & -\\sin(\\theta) \\\\\n                0 & \\sin(\\theta) &  \\cos(\\theta)
            \\end{bmatrix}

    Examples
    ========

    >>> from sympy import pi, rot_ccw_axis1

    A rotation of pi/3 (60 degrees):

    >>> theta = pi/3
    >>> rot_ccw_axis1(theta)
    Matrix([
    [1,         0,          0],
    [0,       1/2, -sqrt(3)/2],
    [0, sqrt(3)/2,        1/2]])

    If we rotate by pi/2 (90 degrees):

    >>> rot_ccw_axis1(pi/2)
    Matrix([
    [1, 0,  0],
    [0, 0, -1],
    [0, 1,  0]])

    See Also
    ========

    rot_givens: Returns a Givens rotation matrix (generalized rotation for
        any number of dimensions)
    rot_axis1: Returns a rotation matrix for a rotation of theta (in radians)
        about the 1-axis (clockwise around the x axis)
    rot_ccw_axis2: Returns a rotation matrix for a rotation of theta (in radians)
        about the 2-axis (counterclockwise around the y axis)
    rot_ccw_axis3: Returns a rotation matrix for a rotation of theta (in radians)
        about the 3-axis (counterclockwise around the z axis)
    """
def symarray(prefix, shape, **kwargs):
    """Create a numpy ndarray of symbols (as an object array).

    The created symbols are named ``prefix_i1_i2_``...  You should thus provide a
    non-empty prefix if you want your symbols to be unique for different output
    arrays, as SymPy symbols with identical names are the same object.

    Parameters
    ----------

    prefix : string
      A prefix prepended to the name of every symbol.

    shape : int or tuple
      Shape of the created array.  If an int, the array is one-dimensional; for
      more than one dimension the shape must be a tuple.

    \\*\\*kwargs : dict
      keyword arguments passed on to Symbol

    Examples
    ========
    These doctests require numpy.

    >>> from sympy import symarray
    >>> symarray('', 3)
    [_0 _1 _2]

    If you want multiple symarrays to contain distinct symbols, you *must*
    provide unique prefixes:

    >>> a = symarray('', 3)
    >>> b = symarray('', 3)
    >>> a[0] == b[0]
    True
    >>> a = symarray('a', 3)
    >>> b = symarray('b', 3)
    >>> a[0] == b[0]
    False

    Creating symarrays with a prefix:

    >>> symarray('a', 3)
    [a_0 a_1 a_2]

    For more than one dimension, the shape must be given as a tuple:

    >>> symarray('a', (2, 3))
    [[a_0_0 a_0_1 a_0_2]
     [a_1_0 a_1_1 a_1_2]]
    >>> symarray('a', (2, 3, 2))
    [[[a_0_0_0 a_0_0_1]
      [a_0_1_0 a_0_1_1]
      [a_0_2_0 a_0_2_1]]
    <BLANKLINE>
     [[a_1_0_0 a_1_0_1]
      [a_1_1_0 a_1_1_1]
      [a_1_2_0 a_1_2_1]]]

    For setting assumptions of the underlying Symbols:

    >>> [s.is_real for s in symarray('a', 2, real=True)]
    [True, True]
    """
def casoratian(seqs, n, zero: bool = True):
    """Given linear difference operator L of order 'k' and homogeneous
       equation Ly = 0 we want to compute kernel of L, which is a set
       of 'k' sequences: a(n), b(n), ... z(n).

       Solutions of L are linearly independent iff their Casoratian,
       denoted as C(a, b, ..., z), do not vanish for n = 0.

       Casoratian is defined by k x k determinant::

                  +  a(n)     b(n)     . . . z(n)     +
                  |  a(n+1)   b(n+1)   . . . z(n+1)   |
                  |    .         .     .        .     |
                  |    .         .       .      .     |
                  |    .         .         .    .     |
                  +  a(n+k-1) b(n+k-1) . . . z(n+k-1) +

       It proves very useful in rsolve_hyper() where it is applied
       to a generating set of a recurrence to factor out linearly
       dependent solutions and return a basis:

       >>> from sympy import Symbol, casoratian, factorial
       >>> n = Symbol('n', integer=True)

       Exponential and factorial are linearly independent:

       >>> casoratian([2**n, factorial(n)], n) != 0
       True

    """
def eye(*args, **kwargs):
    """Create square identity matrix n x n

    See Also
    ========

    diag
    zeros
    ones
    """
def diag(*values, strict: bool = True, unpack: bool = False, **kwargs):
    """Returns a matrix with the provided values placed on the
    diagonal. If non-square matrices are included, they will
    produce a block-diagonal matrix.

    Examples
    ========

    This version of diag is a thin wrapper to Matrix.diag that differs
    in that it treats all lists like matrices -- even when a single list
    is given. If this is not desired, either put a `*` before the list or
    set `unpack=True`.

    >>> from sympy import diag

    >>> diag([1, 2, 3], unpack=True)  # = diag(1,2,3) or diag(*[1,2,3])
    Matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]])

    >>> diag([1, 2, 3])  # a column vector
    Matrix([
    [1],
    [2],
    [3]])

    See Also
    ========
    .common.MatrixCommon.eye
    .common.MatrixCommon.diagonal
    .common.MatrixCommon.diag
    .expressions.blockmatrix.BlockMatrix
    """
def GramSchmidt(vlist, orthonormal: bool = False):
    """Apply the Gram-Schmidt process to a set of vectors.

    Parameters
    ==========

    vlist : List of Matrix
        Vectors to be orthogonalized for.

    orthonormal : Bool, optional
        If true, return an orthonormal basis.

    Returns
    =======

    vlist : List of Matrix
        Orthogonalized vectors

    Notes
    =====

    This routine is mostly duplicate from ``Matrix.orthogonalize``,
    except for some difference that this always raises error when
    linearly dependent vectors are found, and the keyword ``normalize``
    has been named as ``orthonormal`` in this function.

    See Also
    ========

    .matrices.MatrixSubspaces.orthogonalize

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process
    """
def hessian(f, varlist, constraints=()):
    """Compute Hessian matrix for a function f wrt parameters in varlist
    which may be given as a sequence or a row/column vector. A list of
    constraints may optionally be given.

    Examples
    ========

    >>> from sympy import Function, hessian, pprint
    >>> from sympy.abc import x, y
    >>> f = Function('f')(x, y)
    >>> g1 = Function('g')(x, y)
    >>> g2 = x**2 + 3*y
    >>> pprint(hessian(f, (x, y), [g1, g2]))
    [                   d               d            ]
    [     0        0    --(g(x, y))     --(g(x, y))  ]
    [                   dx              dy           ]
    [                                                ]
    [     0        0        2*x              3       ]
    [                                                ]
    [                     2               2          ]
    [d                   d               d           ]
    [--(g(x, y))  2*x   ---(f(x, y))   -----(f(x, y))]
    [dx                   2            dy dx         ]
    [                   dx                           ]
    [                                                ]
    [                     2               2          ]
    [d                   d               d           ]
    [--(g(x, y))   3   -----(f(x, y))   ---(f(x, y)) ]
    [dy                dy dx              2          ]
    [                                   dy           ]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hessian_matrix

    See Also
    ========

    sympy.matrices.matrices.MatrixCalculus.jacobian
    wronskian
    """
def jordan_cell(eigenval, n):
    """
    Create a Jordan block:

    Examples
    ========

    >>> from sympy import jordan_cell
    >>> from sympy.abc import x
    >>> jordan_cell(x, 4)
    Matrix([
    [x, 1, 0, 0],
    [0, x, 1, 0],
    [0, 0, x, 1],
    [0, 0, 0, x]])
    """
def matrix_multiply_elementwise(A, B):
    """Return the Hadamard product (elementwise product) of A and B

    >>> from sympy import Matrix, matrix_multiply_elementwise
    >>> A = Matrix([[0, 1, 2], [3, 4, 5]])
    >>> B = Matrix([[1, 10, 100], [100, 10, 1]])
    >>> matrix_multiply_elementwise(A, B)
    Matrix([
    [  0, 10, 200],
    [300, 40,   5]])

    See Also
    ========

    sympy.matrices.common.MatrixCommon.__mul__
    """
def ones(*args, **kwargs):
    """Returns a matrix of ones with ``rows`` rows and ``cols`` columns;
    if ``cols`` is omitted a square matrix will be returned.

    See Also
    ========

    zeros
    eye
    diag
    """
def randMatrix(r, c: Incomplete | None = None, min: int = 0, max: int = 99, seed: Incomplete | None = None, symmetric: bool = False, percent: int = 100, prng: Incomplete | None = None):
    """Create random matrix with dimensions ``r`` x ``c``. If ``c`` is omitted
    the matrix will be square. If ``symmetric`` is True the matrix must be
    square. If ``percent`` is less than 100 then only approximately the given
    percentage of elements will be non-zero.

    The pseudo-random number generator used to generate matrix is chosen in the
    following way.

    * If ``prng`` is supplied, it will be used as random number generator.
      It should be an instance of ``random.Random``, or at least have
      ``randint`` and ``shuffle`` methods with same signatures.
    * if ``prng`` is not supplied but ``seed`` is supplied, then new
      ``random.Random`` with given ``seed`` will be created;
    * otherwise, a new ``random.Random`` with default seed will be used.

    Examples
    ========

    >>> from sympy import randMatrix
    >>> randMatrix(3) # doctest:+SKIP
    [25, 45, 27]
    [44, 54,  9]
    [23, 96, 46]
    >>> randMatrix(3, 2) # doctest:+SKIP
    [87, 29]
    [23, 37]
    [90, 26]
    >>> randMatrix(3, 3, 0, 2) # doctest:+SKIP
    [0, 2, 0]
    [2, 0, 1]
    [0, 0, 1]
    >>> randMatrix(3, symmetric=True) # doctest:+SKIP
    [85, 26, 29]
    [26, 71, 43]
    [29, 43, 57]
    >>> A = randMatrix(3, seed=1)
    >>> B = randMatrix(3, seed=2)
    >>> A == B
    False
    >>> A == randMatrix(3, seed=1)
    True
    >>> randMatrix(3, symmetric=True, percent=50) # doctest:+SKIP
    [77, 70,  0],
    [70,  0,  0],
    [ 0,  0, 88]
    """
def wronskian(functions, var, method: str = 'bareiss'):
    """
    Compute Wronskian for [] of functions

    ::

                         | f1       f2        ...   fn      |
                         | f1'      f2'       ...   fn'     |
                         |  .        .        .      .      |
        W(f1, ..., fn) = |  .        .         .     .      |
                         |  .        .          .    .      |
                         |  (n)      (n)            (n)     |
                         | D   (f1) D   (f2)  ...  D   (fn) |

    see: https://en.wikipedia.org/wiki/Wronskian

    See Also
    ========

    sympy.matrices.matrices.MatrixCalculus.jacobian
    hessian
    """
def zeros(*args, **kwargs):
    """Returns a matrix of zeros with ``rows`` rows and ``cols`` columns;
    if ``cols`` is omitted a square matrix will be returned.

    See Also
    ========

    ones
    eye
    diag
    """
