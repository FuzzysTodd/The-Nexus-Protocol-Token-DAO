from _typeshed import Incomplete
from sympy.core._print_helpers import Printable as Printable
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import diff as diff
from sympy.core.singleton import S as S
from sympy.tensor.array.dense_ndim_array import DenseNDimArray as DenseNDimArray, ImmutableDenseNDimArray as ImmutableDenseNDimArray
from sympy.tensor.array.ndim_array import NDimArray as NDimArray
from sympy.tensor.array.sparse_ndim_array import SparseNDimArray as SparseNDimArray

def tensorproduct(*args):
    """
    Tensor product among scalars or array-like objects.

    The equivalent operator for array expressions is ``ArrayTensorProduct``,
    which can be used to keep the expression unevaluated.

    Examples
    ========

    >>> from sympy.tensor.array import tensorproduct, Array
    >>> from sympy.abc import x, y, z, t
    >>> A = Array([[1, 2], [3, 4]])
    >>> B = Array([x, y])
    >>> tensorproduct(A, B)
    [[[x, y], [2*x, 2*y]], [[3*x, 3*y], [4*x, 4*y]]]
    >>> tensorproduct(A, x)
    [[x, 2*x], [3*x, 4*x]]
    >>> tensorproduct(A, B, B)
    [[[[x**2, x*y], [x*y, y**2]], [[2*x**2, 2*x*y], [2*x*y, 2*y**2]]], [[[3*x**2, 3*x*y], [3*x*y, 3*y**2]], [[4*x**2, 4*x*y], [4*x*y, 4*y**2]]]]

    Applying this function on two matrices will result in a rank 4 array.

    >>> from sympy import Matrix, eye
    >>> m = Matrix([[x, y], [z, t]])
    >>> p = tensorproduct(eye(3), m)
    >>> p
    [[[[x, y], [z, t]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[x, y], [z, t]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[0, 0], [0, 0]], [[x, y], [z, t]]]]

    See Also
    ========

    sympy.tensor.array.expressions.array_expressions.ArrayTensorProduct

    """
def tensorcontraction(array, *contraction_axes):
    """
    Contraction of an array-like object on the specified axes.

    The equivalent operator for array expressions is ``ArrayContraction``,
    which can be used to keep the expression unevaluated.

    Examples
    ========

    >>> from sympy import Array, tensorcontraction
    >>> from sympy import Matrix, eye
    >>> tensorcontraction(eye(3), (0, 1))
    3
    >>> A = Array(range(18), (3, 2, 3))
    >>> A
    [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]], [[12, 13, 14], [15, 16, 17]]]
    >>> tensorcontraction(A, (0, 2))
    [21, 30]

    Matrix multiplication may be emulated with a proper combination of
    ``tensorcontraction`` and ``tensorproduct``

    >>> from sympy import tensorproduct
    >>> from sympy.abc import a,b,c,d,e,f,g,h
    >>> m1 = Matrix([[a, b], [c, d]])
    >>> m2 = Matrix([[e, f], [g, h]])
    >>> p = tensorproduct(m1, m2)
    >>> p
    [[[[a*e, a*f], [a*g, a*h]], [[b*e, b*f], [b*g, b*h]]], [[[c*e, c*f], [c*g, c*h]], [[d*e, d*f], [d*g, d*h]]]]
    >>> tensorcontraction(p, (1, 2))
    [[a*e + b*g, a*f + b*h], [c*e + d*g, c*f + d*h]]
    >>> m1*m2
    Matrix([
    [a*e + b*g, a*f + b*h],
    [c*e + d*g, c*f + d*h]])

    See Also
    ========

    sympy.tensor.array.expressions.array_expressions.ArrayContraction

    """
def tensordiagonal(array, *diagonal_axes):
    """
    Diagonalization of an array-like object on the specified axes.

    This is equivalent to multiplying the expression by Kronecker deltas
    uniting the axes.

    The diagonal indices are put at the end of the axes.

    The equivalent operator for array expressions is ``ArrayDiagonal``, which
    can be used to keep the expression unevaluated.

    Examples
    ========

    ``tensordiagonal`` acting on a 2-dimensional array by axes 0 and 1 is
    equivalent to the diagonal of the matrix:

    >>> from sympy import Array, tensordiagonal
    >>> from sympy import Matrix, eye
    >>> tensordiagonal(eye(3), (0, 1))
    [1, 1, 1]

    >>> from sympy.abc import a,b,c,d
    >>> m1 = Matrix([[a, b], [c, d]])
    >>> tensordiagonal(m1, [0, 1])
    [a, d]

    In case of higher dimensional arrays, the diagonalized out dimensions
    are appended removed and appended as a single dimension at the end:

    >>> A = Array(range(18), (3, 2, 3))
    >>> A
    [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]], [[12, 13, 14], [15, 16, 17]]]
    >>> tensordiagonal(A, (0, 2))
    [[0, 7, 14], [3, 10, 17]]
    >>> from sympy import permutedims
    >>> tensordiagonal(A, (0, 2)) == permutedims(Array([A[0, :, 0], A[1, :, 1], A[2, :, 2]]), [1, 0])
    True

    See Also
    ========

    sympy.tensor.array.expressions.array_expressions.ArrayDiagonal

    """
def derive_by_array(expr, dx):
    """
    Derivative by arrays. Supports both arrays and scalars.

    The equivalent operator for array expressions is ``array_derive``.

    Explanation
    ===========

    Given the array `A_{i_1, \\ldots, i_N}` and the array `X_{j_1, \\ldots, j_M}`
    this function will return a new array `B` defined by

    `B_{j_1,\\ldots,j_M,i_1,\\ldots,i_N} := \\frac{\\partial A_{i_1,\\ldots,i_N}}{\\partial X_{j_1,\\ldots,j_M}}`

    Examples
    ========

    >>> from sympy import derive_by_array
    >>> from sympy.abc import x, y, z, t
    >>> from sympy import cos
    >>> derive_by_array(cos(x*t), x)
    -t*sin(t*x)
    >>> derive_by_array(cos(x*t), [x, y, z, t])
    [-t*sin(t*x), 0, 0, -x*sin(t*x)]
    >>> derive_by_array([x, y**2*z], [[x, y], [z, t]])
    [[[1, 0], [0, 2*y*z]], [[0, y**2], [0, 0]]]

    """
def permutedims(expr, perm: Incomplete | None = None, index_order_old: Incomplete | None = None, index_order_new: Incomplete | None = None):
    '''
    Permutes the indices of an array.

    Parameter specifies the permutation of the indices.

    The equivalent operator for array expressions is ``PermuteDims``, which can
    be used to keep the expression unevaluated.

    Examples
    ========

    >>> from sympy.abc import x, y, z, t
    >>> from sympy import sin
    >>> from sympy import Array, permutedims
    >>> a = Array([[x, y, z], [t, sin(x), 0]])
    >>> a
    [[x, y, z], [t, sin(x), 0]]
    >>> permutedims(a, (1, 0))
    [[x, t], [y, sin(x)], [z, 0]]

    If the array is of second order, ``transpose`` can be used:

    >>> from sympy import transpose
    >>> transpose(a)
    [[x, t], [y, sin(x)], [z, 0]]

    Examples on higher dimensions:

    >>> b = Array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    >>> permutedims(b, (2, 1, 0))
    [[[1, 5], [3, 7]], [[2, 6], [4, 8]]]
    >>> permutedims(b, (1, 2, 0))
    [[[1, 5], [2, 6]], [[3, 7], [4, 8]]]

    An alternative way to specify the same permutations as in the previous
    lines involves passing the *old* and *new* indices, either as a list or as
    a string:

    >>> permutedims(b, index_order_old="cba", index_order_new="abc")
    [[[1, 5], [3, 7]], [[2, 6], [4, 8]]]
    >>> permutedims(b, index_order_old="cab", index_order_new="abc")
    [[[1, 5], [2, 6]], [[3, 7], [4, 8]]]

    ``Permutation`` objects are also allowed:

    >>> from sympy.combinatorics import Permutation
    >>> permutedims(b, Permutation([1, 2, 0]))
    [[[1, 5], [2, 6]], [[3, 7], [4, 8]]]

    See Also
    ========

    sympy.tensor.array.expressions.array_expressions.PermuteDims

    '''

class Flatten(Printable):
    """
    Flatten an iterable object to a list in a lazy-evaluation way.

    Notes
    =====

    This class is an iterator with which the memory cost can be economised.
    Optimisation has been considered to ameliorate the performance for some
    specific data types like DenseNDimArray and SparseNDimArray.

    Examples
    ========

    >>> from sympy.tensor.array.arrayop import Flatten
    >>> from sympy.tensor.array import Array
    >>> A = Array(range(6)).reshape(2, 3)
    >>> Flatten(A)
    Flatten([[0, 1, 2], [3, 4, 5]])
    >>> [i for i in Flatten(A)]
    [0, 1, 2, 3, 4, 5]
    """
    def __init__(self, iterable) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def next(self): ...
