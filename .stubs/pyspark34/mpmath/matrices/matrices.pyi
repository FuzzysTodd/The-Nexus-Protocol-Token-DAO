from ..libmp.backend import xrange as xrange
from _typeshed import Incomplete

rowsep: str
colsep: str

class _matrix:
    '''
    Numerical matrix.

    Specify the dimensions or the data as a nested list.
    Elements default to zero.
    Use a flat list to create a column vector easily.

    The datatype of the context (mpf for mp, mpi for iv, and float for fp) is used to store the data.

    Creating matrices
    -----------------

    Matrices in mpmath are implemented using dictionaries. Only non-zero values
    are stored, so it is cheap to represent sparse matrices.

    The most basic way to create one is to use the ``matrix`` class directly.
    You can create an empty matrix specifying the dimensions:

        >>> from mpmath import *
        >>> mp.dps = 15
        >>> matrix(2)
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> matrix(2, 3)
        matrix(
        [[\'0.0\', \'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\', \'0.0\']])

    Calling ``matrix`` with one dimension will create a square matrix.

    To access the dimensions of a matrix, use the ``rows`` or ``cols`` keyword:

        >>> A = matrix(3, 2)
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> A.rows
        3
        >>> A.cols
        2

    You can also change the dimension of an existing matrix. This will set the
    new elements to 0. If the new dimension is smaller than before, the
    concerning elements are discarded:

        >>> A.rows = 2
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])

    Internally ``mpmathify`` is used every time an element is set. This
    is done using the syntax A[row,column], counting from 0:

        >>> A = matrix(2)
        >>> A[1,1] = 1 + 1j
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', mpc(real=\'1.0\', imag=\'1.0\')]])

    A more comfortable way to create a matrix lets you use nested lists:

        >>> matrix([[1, 2], [3, 4]])
        matrix(
        [[\'1.0\', \'2.0\'],
         [\'3.0\', \'4.0\']])

    Convenient advanced functions are available for creating various standard
    matrices, see ``zeros``, ``ones``, ``diag``, ``eye``, ``randmatrix`` and
    ``hilbert``.

    Vectors
    .......

    Vectors may also be represented by the ``matrix`` class (with rows = 1 or cols = 1).
    For vectors there are some things which make life easier. A column vector can
    be created using a flat list, a row vectors using an almost flat nested list::

        >>> matrix([1, 2, 3])
        matrix(
        [[\'1.0\'],
         [\'2.0\'],
         [\'3.0\']])
        >>> matrix([[1, 2, 3]])
        matrix(
        [[\'1.0\', \'2.0\', \'3.0\']])

    Optionally vectors can be accessed like lists, using only a single index::

        >>> x = matrix([1, 2, 3])
        >>> x[1]
        mpf(\'2.0\')
        >>> x[1,0]
        mpf(\'2.0\')

    Other
    .....

    Like you probably expected, matrices can be printed::

        >>> print randmatrix(3) # doctest:+SKIP
        [ 0.782963853573023  0.802057689719883  0.427895717335467]
        [0.0541876859348597  0.708243266653103  0.615134039977379]
        [ 0.856151514955773  0.544759264818486  0.686210904770947]

    Use ``nstr`` or ``nprint`` to specify the number of digits to print::

        >>> nprint(randmatrix(5), 3) # doctest:+SKIP
        [2.07e-1  1.66e-1  5.06e-1  1.89e-1  8.29e-1]
        [6.62e-1  6.55e-1  4.47e-1  4.82e-1  2.06e-2]
        [4.33e-1  7.75e-1  6.93e-2  2.86e-1  5.71e-1]
        [1.01e-1  2.53e-1  6.13e-1  3.32e-1  2.59e-1]
        [1.56e-1  7.27e-2  6.05e-1  6.67e-2  2.79e-1]

    As matrices are mutable, you will need to copy them sometimes::

        >>> A = matrix(2)
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> B = A.copy()
        >>> B[0,0] = 1
        >>> B
        matrix(
        [[\'1.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])
        >>> A
        matrix(
        [[\'0.0\', \'0.0\'],
         [\'0.0\', \'0.0\']])

    Finally, it is possible to convert a matrix to a nested list. This is very useful,
    as most Python libraries involving matrices or arrays (namely NumPy or SymPy)
    support this format::

        >>> B.tolist()
        [[mpf(\'1.0\'), mpf(\'0.0\')], [mpf(\'0.0\'), mpf(\'0.0\')]]


    Matrix operations
    -----------------

    You can add and subtract matrices of compatible dimensions::

        >>> A = matrix([[1, 2], [3, 4]])
        >>> B = matrix([[-2, 4], [5, 9]])
        >>> A + B
        matrix(
        [[\'-1.0\', \'6.0\'],
         [\'8.0\', \'13.0\']])
        >>> A - B
        matrix(
        [[\'3.0\', \'-2.0\'],
         [\'-2.0\', \'-5.0\']])
        >>> A + ones(3) # doctest:+ELLIPSIS
        Traceback (most recent call last):
          ...
        ValueError: incompatible dimensions for addition

    It is possible to multiply or add matrices and scalars. In the latter case the
    operation will be done element-wise::

        >>> A * 2
        matrix(
        [[\'2.0\', \'4.0\'],
         [\'6.0\', \'8.0\']])
        >>> A / 4
        matrix(
        [[\'0.25\', \'0.5\'],
         [\'0.75\', \'1.0\']])
        >>> A - 1
        matrix(
        [[\'0.0\', \'1.0\'],
         [\'2.0\', \'3.0\']])

    Of course you can perform matrix multiplication, if the dimensions are
    compatible, using ``@`` (for Python >= 3.5) or ``*``. For clarity, ``@`` is
    recommended (`PEP 465 <https://www.python.org/dev/peps/pep-0465/>`), because
    the meaning of ``*`` is different in many other Python libraries such as NumPy.

        >>> A @ B # doctest:+SKIP
        matrix(
        [[\'8.0\', \'22.0\'],
         [\'14.0\', \'48.0\']])
        >>> A * B # same as A @ B
        matrix(
        [[\'8.0\', \'22.0\'],
         [\'14.0\', \'48.0\']])
        >>> matrix([[1, 2, 3]]) * matrix([[-6], [7], [-2]])
        matrix(
        [[\'2.0\']])

    ..
        COMMENT: TODO: the above "doctest:+SKIP" may be removed as soon as we
        have dropped support for Python 3.5 and below.

    You can raise powers of square matrices::

        >>> A**2
        matrix(
        [[\'7.0\', \'10.0\'],
         [\'15.0\', \'22.0\']])

    Negative powers will calculate the inverse::

        >>> A**-1
        matrix(
        [[\'-2.0\', \'1.0\'],
         [\'1.5\', \'-0.5\']])
        >>> A * A**-1
        matrix(
        [[\'1.0\', \'1.0842021724855e-19\'],
         [\'-2.16840434497101e-19\', \'1.0\']])



    Matrix transposition is straightforward::

        >>> A = ones(2, 3)
        >>> A
        matrix(
        [[\'1.0\', \'1.0\', \'1.0\'],
         [\'1.0\', \'1.0\', \'1.0\']])
        >>> A.T
        matrix(
        [[\'1.0\', \'1.0\'],
         [\'1.0\', \'1.0\'],
         [\'1.0\', \'1.0\']])

    Norms
    .....

    Sometimes you need to know how "large" a matrix or vector is. Due to their
    multidimensional nature it\'s not possible to compare them, but there are
    several functions to map a matrix or a vector to a positive real number, the
    so called norms.

    For vectors the p-norm is intended, usually the 1-, the 2- and the oo-norm are
    used.

        >>> x = matrix([-10, 2, 100])
        >>> norm(x, 1)
        mpf(\'112.0\')
        >>> norm(x, 2)
        mpf(\'100.5186549850325\')
        >>> norm(x, inf)
        mpf(\'100.0\')

    Please note that the 2-norm is the most used one, though it is more expensive
    to calculate than the 1- or oo-norm.

    It is possible to generalize some vector norms to matrix norm::

        >>> A = matrix([[1, -1000], [100, 50]])
        >>> mnorm(A, 1)
        mpf(\'1050.0\')
        >>> mnorm(A, inf)
        mpf(\'1001.0\')
        >>> mnorm(A, \'F\')
        mpf(\'1006.2310867787777\')

    The last norm (the "Frobenius-norm") is an approximation for the 2-norm, which
    is hard to calculate and not available. The Frobenius-norm lacks some
    mathematical properties you might expect from a norm.
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def apply(self, f):
        """
        Return a copy of self with the function `f` applied elementwise.
        """
    def __nstr__(self, n: Incomplete | None = None, **kwargs): ...
    def tolist(self):
        """
        Convert the matrix to a nested list.
        """
    def __getitem__(self, key):
        """
            Getitem function for mp matrix class with slice index enabled
            it allows the following assingments
            scalar to a slice of the matrix
         B = A[:,2:6]
        """
    def __setitem__(self, key, value) -> None: ...
    def __iter__(self): ...
    def __mul__(self, other): ...
    def __matmul__(self, other): ...
    def __rmul__(self, other): ...
    def __pow__(self, other): ...
    def __div__(self, other): ...
    __truediv__ = __div__
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __pos__(self):
        """
        +M returns a copy of M, rounded to current working precision.
        """
    def __neg__(self): ...
    def __rsub__(self, other): ...
    def __eq__(self, other): ...
    def __len__(self) -> int: ...
    rows: Incomplete
    cols: Incomplete
    def transpose(self): ...
    T: Incomplete
    def conjugate(self): ...
    def transpose_conj(self): ...
    H: Incomplete
    def copy(self): ...
    __copy__ = copy
    def column(self, n): ...

class MatrixMethods:
    def __init__(ctx) -> None: ...
    def eye(ctx, n, **kwargs):
        """
        Create square identity matrix n x n.
        """
    def diag(ctx, diagonal, **kwargs):
        """
        Create square diagonal matrix using given list.

        Example:
        >>> from mpmath import diag, mp
        >>> mp.pretty = False
        >>> diag([1, 2, 3])
        matrix(
        [['1.0', '0.0', '0.0'],
         ['0.0', '2.0', '0.0'],
         ['0.0', '0.0', '3.0']])
        """
    def zeros(ctx, *args, **kwargs):
        """
        Create matrix m x n filled with zeros.
        One given dimension will create square matrix n x n.

        Example:
        >>> from mpmath import zeros, mp
        >>> mp.pretty = False
        >>> zeros(2)
        matrix(
        [['0.0', '0.0'],
         ['0.0', '0.0']])
        """
    def ones(ctx, *args, **kwargs):
        """
        Create matrix m x n filled with ones.
        One given dimension will create square matrix n x n.

        Example:
        >>> from mpmath import ones, mp
        >>> mp.pretty = False
        >>> ones(2)
        matrix(
        [['1.0', '1.0'],
         ['1.0', '1.0']])
        """
    def hilbert(ctx, m, n: Incomplete | None = None):
        """
        Create (pseudo) hilbert matrix m x n.
        One given dimension will create hilbert matrix n x n.

        The matrix is very ill-conditioned and symmetric, positive definite if
        square.
        """
    def randmatrix(ctx, m, n: Incomplete | None = None, min: int = 0, max: int = 1, **kwargs):
        """
        Create a random m x n matrix.

        All values are >= min and <max.
        n defaults to m.

        Example:
        >>> from mpmath import randmatrix
        >>> randmatrix(2) # doctest:+SKIP
        matrix(
        [['0.53491598236191806', '0.57195669543302752'],
         ['0.85589992269513615', '0.82444367501382143']])
        """
    def swap_row(ctx, A, i, j) -> None:
        """
        Swap row i with row j.
        """
    def extend(ctx, A, b):
        """
        Extend matrix A with column b and return result.
        """
    def norm(ctx, x, p: int = 2):
        """
        Gives the entrywise `p`-norm of an iterable *x*, i.e. the vector norm
        `\\left(\\sum_k |x_k|^p\\right)^{1/p}`, for any given `1 \\le p \\le \\infty`.

        Special cases:

        If *x* is not iterable, this just returns ``absmax(x)``.

        ``p=1`` gives the sum of absolute values.

        ``p=2`` is the standard Euclidean vector norm.

        ``p=inf`` gives the magnitude of the largest element.

        For *x* a matrix, ``p=2`` is the Frobenius norm.
        For operator matrix norms, use :func:`~mpmath.mnorm` instead.

        You can use the string 'inf' as well as float('inf') or mpf('inf')
        to specify the infinity norm.

        **Examples**

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> x = matrix([-10, 2, 100])
            >>> norm(x, 1)
            mpf('112.0')
            >>> norm(x, 2)
            mpf('100.5186549850325')
            >>> norm(x, inf)
            mpf('100.0')

        """
    def mnorm(ctx, A, p: int = 1):
        """
        Gives the matrix (operator) `p`-norm of A. Currently ``p=1`` and ``p=inf``
        are supported:

        ``p=1`` gives the 1-norm (maximal column sum)

        ``p=inf`` gives the `\\infty`-norm (maximal row sum).
        You can use the string 'inf' as well as float('inf') or mpf('inf')

        ``p=2`` (not implemented) for a square matrix is the usual spectral
        matrix norm, i.e. the largest singular value.

        ``p='f'`` (or 'F', 'fro', 'Frobenius, 'frobenius') gives the
        Frobenius norm, which is the elementwise 2-norm. The Frobenius norm is an
        approximation of the spectral norm and satisfies

        .. math ::

            \\frac{1}{\\sqrt{\\mathrm{rank}(A)}} \\|A\\|_F \\le \\|A\\|_2 \\le \\|A\\|_F

        The Frobenius norm lacks some mathematical properties that might
        be expected of a norm.

        For general elementwise `p`-norms, use :func:`~mpmath.norm` instead.

        **Examples**

            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> A = matrix([[1, -1000], [100, 50]])
            >>> mnorm(A, 1)
            mpf('1050.0')
            >>> mnorm(A, inf)
            mpf('1001.0')
            >>> mnorm(A, 'F')
            mpf('1006.2310867787777')

        """
