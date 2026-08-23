import typing
from _typeshed import Incomplete
from sympy.combinatorics import Permutation as Permutation
from sympy.core.basic import Basic as Basic
from sympy.core.containers import Tuple as Tuple
from sympy.core.expr import Expr as Expr
from sympy.core.function import Function as Function, Lambda as Lambda
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import Integer as Integer
from sympy.core.relational import Equality as Equality
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.matrices.common import MatrixCommon as MatrixCommon
from sympy.matrices.expressions.diagonal import diagonalize_vector as diagonalize_vector
from sympy.matrices.expressions.matexpr import MatrixElement as MatrixElement, MatrixExpr as MatrixExpr
from sympy.matrices.expressions.special import ZeroMatrix as ZeroMatrix
from sympy.tensor.array.arrayop import permutedims as permutedims, tensorcontraction as tensorcontraction, tensordiagonal as tensordiagonal, tensorproduct as tensorproduct
from sympy.tensor.array.dense_ndim_array import ImmutableDenseNDimArray as ImmutableDenseNDimArray
from sympy.tensor.array.ndim_array import NDimArray as NDimArray
from sympy.tensor.indexed import Indexed as Indexed, IndexedBase as IndexedBase
from typing import List, Tuple as tTuple

class _ArrayExpr(Expr):
    shape: tTuple[Expr, ...]
    def __getitem__(self, item): ...

class ArraySymbol(_ArrayExpr):
    """
    Symbol representing an array expression
    """
    def __new__(cls, symbol, shape: typing.Iterable) -> ArraySymbol: ...
    @property
    def name(self): ...
    @property
    def shape(self): ...
    def as_explicit(self): ...

class ArrayElement(Expr):
    """
    An element of an array.
    """
    is_symbol: bool
    is_commutative: bool
    def __new__(cls, name, indices): ...
    @property
    def name(self): ...
    @property
    def indices(self): ...

class ZeroArray(_ArrayExpr):
    """
    Symbolic array of zeros. Equivalent to ``ZeroMatrix`` for matrices.
    """
    def __new__(cls, *shape): ...
    @property
    def shape(self): ...
    def as_explicit(self): ...

class OneArray(_ArrayExpr):
    """
    Symbolic array of ones.
    """
    def __new__(cls, *shape): ...
    @property
    def shape(self): ...
    def as_explicit(self): ...

class _CodegenArrayAbstract(Basic):
    @property
    def subranks(self):
        '''
        Returns the ranks of the objects in the uppermost tensor product inside
        the current object.  In case no tensor products are contained, return
        the atomic ranks.

        Examples
        ========

        >>> from sympy.tensor.array import tensorproduct, tensorcontraction
        >>> from sympy import MatrixSymbol
        >>> M = MatrixSymbol("M", 3, 3)
        >>> N = MatrixSymbol("N", 3, 3)
        >>> P = MatrixSymbol("P", 3, 3)

        Important: do not confuse the rank of the matrix with the rank of an array.

        >>> tp = tensorproduct(M, N, P)
        >>> tp.subranks
        [2, 2, 2]

        >>> co = tensorcontraction(tp, (1, 2), (3, 4))
        >>> co.subranks
        [2, 2, 2]
        '''
    def subrank(self):
        """
        The sum of ``subranks``.
        """
    @property
    def shape(self): ...
    def doit(self, **hints): ...

class ArrayTensorProduct(_CodegenArrayAbstract):
    """
    Class to represent the tensor product of array-like objects.
    """
    def __new__(cls, *args, **kwargs): ...
    def as_explicit(self): ...

class ArrayAdd(_CodegenArrayAbstract):
    """
    Class for elementwise array additions.
    """
    def __new__(cls, *args, **kwargs): ...
    def as_explicit(self): ...

class PermuteDims(_CodegenArrayAbstract):
    '''
    Class to represent permutation of axes of arrays.

    Examples
    ========

    >>> from sympy.tensor.array import permutedims
    >>> from sympy import MatrixSymbol
    >>> M = MatrixSymbol("M", 3, 3)
    >>> cg = permutedims(M, [1, 0])

    The object ``cg`` represents the transposition of ``M``, as the permutation
    ``[1, 0]`` will act on its indices by switching them:

    `M_{ij} \\Rightarrow M_{ji}`

    This is evident when transforming back to matrix form:

    >>> from sympy.tensor.array.expressions.from_array_to_matrix import convert_array_to_matrix
    >>> convert_array_to_matrix(cg)
    M.T

    >>> N = MatrixSymbol("N", 3, 2)
    >>> cg = permutedims(N, [1, 0])
    >>> cg.shape
    (2, 3)

    There are optional parameters that can be used as alternative to the permutation:

    >>> from sympy.tensor.array.expressions import ArraySymbol, PermuteDims
    >>> M = ArraySymbol("M", (1, 2, 3, 4, 5))
    >>> expr = PermuteDims(M, index_order_old="ijklm", index_order_new="kijml")
    >>> expr
    PermuteDims(M, (0 2 1)(3 4))
    >>> expr.shape
    (3, 1, 2, 5, 4)

    Permutations of tensor products are simplified in order to achieve a
    standard form:

    >>> from sympy.tensor.array import tensorproduct
    >>> M = MatrixSymbol("M", 4, 5)
    >>> tp = tensorproduct(M, N)
    >>> tp.shape
    (4, 5, 3, 2)
    >>> perm1 = permutedims(tp, [2, 3, 1, 0])

    The args ``(M, N)`` have been sorted and the permutation has been
    simplified, the expression is equivalent:

    >>> perm1.expr.args
    (N, M)
    >>> perm1.shape
    (3, 2, 5, 4)
    >>> perm1.permutation
    (2 3)

    The permutation in its array form has been simplified from
    ``[2, 3, 1, 0]`` to ``[0, 1, 3, 2]``, as the arguments of the tensor
    product `M` and `N` have been switched:

    >>> perm1.permutation.array_form
    [0, 1, 3, 2]

    We can nest a second permutation:

    >>> perm2 = permutedims(perm1, [1, 0, 2, 3])
    >>> perm2.shape
    (2, 3, 5, 4)
    >>> perm2.permutation.array_form
    [1, 0, 3, 2]
    '''
    def __new__(cls, expr, permutation: Incomplete | None = None, index_order_old: Incomplete | None = None, index_order_new: Incomplete | None = None, **kwargs): ...
    @property
    def expr(self): ...
    @property
    def permutation(self): ...
    def nest_permutation(self):
        """
        DEPRECATED.
        """
    def as_explicit(self): ...

class ArrayDiagonal(_CodegenArrayAbstract):
    """
    Class to represent the diagonal operator.

    Explanation
    ===========

    In a 2-dimensional array it returns the diagonal, this looks like the
    operation:

    `A_{ij} \\rightarrow A_{ii}`

    The diagonal over axes 1 and 2 (the second and third) of the tensor product
    of two 2-dimensional arrays `A \\otimes B` is

    `\\Big[ A_{ab} B_{cd} \\Big]_{abcd} \\rightarrow \\Big[ A_{ai} B_{id} \\Big]_{adi}`

    In this last example the array expression has been reduced from
    4-dimensional to 3-dimensional. Notice that no contraction has occurred,
    rather there is a new index `i` for the diagonal, contraction would have
    reduced the array to 2 dimensions.

    Notice that the diagonalized out dimensions are added as new dimensions at
    the end of the indices.
    """
    def __new__(cls, expr, *diagonal_indices, **kwargs): ...
    @property
    def expr(self): ...
    @property
    def diagonal_indices(self): ...
    def as_explicit(self): ...

class ArrayElementwiseApplyFunc(_CodegenArrayAbstract):
    def __new__(cls, function, element): ...
    @property
    def function(self): ...
    @property
    def expr(self): ...
    @property
    def shape(self): ...
    def as_explicit(self): ...

class ArrayContraction(_CodegenArrayAbstract):
    """
    This class is meant to represent contractions of arrays in a form easily
    processable by the code printers.
    """
    def __new__(cls, expr, *contraction_indices, **kwargs): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def split_multiple_contractions(self):
        """
        Recognize multiple contractions and attempt at rewriting them as paired-contractions.

        This allows some contractions involving more than two indices to be
        rewritten as multiple contractions involving two indices, thus allowing
        the expression to be rewritten as a matrix multiplication line.

        Examples:

        * `A_ij b_j0 C_jk` ===> `A*DiagMatrix(b)*C`

        Care for:
        - matrix being diagonalized (i.e. `A_ii`)
        - vectors being diagonalized (i.e. `a_i0`)

        Multiple contractions can be split into matrix multiplications if
        not more than two arguments are non-diagonals or non-vectors.
        Vectors get diagonalized while diagonal matrices remain diagonal.
        The non-diagonal matrices can be at the beginning or at the end
        of the final matrix multiplication line.
        """
    def flatten_contraction_of_diagonal(self): ...
    @property
    def free_indices(self): ...
    @property
    def free_indices_to_position(self): ...
    @property
    def expr(self): ...
    @property
    def contraction_indices(self): ...
    def sort_args_by_name(self):
        '''
        Sort arguments in the tensor product so that their order is lexicographical.

        Examples
        ========

        >>> from sympy.tensor.array.expressions.from_matrix_to_array import convert_matrix_to_array
        >>> from sympy import MatrixSymbol
        >>> from sympy.abc import N
        >>> A = MatrixSymbol("A", N, N)
        >>> B = MatrixSymbol("B", N, N)
        >>> C = MatrixSymbol("C", N, N)
        >>> D = MatrixSymbol("D", N, N)

        >>> cg = convert_matrix_to_array(C*D*A*B)
        >>> cg
        ArrayContraction(ArrayTensorProduct(A, D, C, B), (0, 3), (1, 6), (2, 5))
        >>> cg.sort_args_by_name()
        ArrayContraction(ArrayTensorProduct(A, D, B, C), (0, 3), (1, 4), (2, 7))
        '''
    def as_explicit(self): ...

class Reshape(_CodegenArrayAbstract):
    '''
    Reshape the dimensions of an array expression.

    Examples
    ========

    >>> from sympy.tensor.array.expressions import ArraySymbol, Reshape
    >>> A = ArraySymbol("A", (6,))
    >>> A.shape
    (6,)
    >>> Reshape(A, (3, 2)).shape
    (3, 2)

    Check the component-explicit forms:

    >>> A.as_explicit()
    [A[0], A[1], A[2], A[3], A[4], A[5]]
    >>> Reshape(A, (3, 2)).as_explicit()
    [[A[0], A[1]], [A[2], A[3]], [A[4], A[5]]]

    '''
    def __new__(cls, expr, shape): ...
    @property
    def shape(self): ...
    @property
    def expr(self): ...
    def doit(self, *args, **kwargs): ...
    def as_explicit(self): ...

class _ArgE:
    """
    The ``_ArgE`` object contains references to the array expression
    (``.element``) and a list containing the information about index
    contractions (``.indices``).

    Index contractions are numbered and contracted indices show the number of
    the contraction. Uncontracted indices have ``None`` value.

    For example:
    ``_ArgE(M, [None, 3])``
    This object means that expression ``M`` is part of an array contraction
    and has two indices, the first is not contracted (value ``None``),
    the second index is contracted to the 4th (i.e. number ``3``) group of the
    array contraction object.
    """
    indices: List[int | None]
    element: Incomplete
    def __init__(self, element, indices: List[int | None] | None = None) -> None: ...

class _IndPos:
    """
    Index position, requiring two integers in the constructor:

    - arg: the position of the argument in the tensor product,
    - rel: the relative position of the index inside the argument.
    """
    arg: Incomplete
    rel: Incomplete
    def __init__(self, arg: int, rel: int) -> None: ...
    def __iter__(self): ...

class _EditArrayContraction:
    """
    Utility class to help manipulate array contraction objects.

    This class takes as input an ``ArrayContraction`` object and turns it into
    an editable object.

    The field ``args_with_ind`` of this class is a list of ``_ArgE`` objects
    which can be used to easily edit the contraction structure of the
    expression.

    Once editing is finished, the ``ArrayContraction`` object may be recreated
    by calling the ``.to_array_contraction()`` method.
    """
    args_with_ind: Incomplete
    number_of_contraction_indices: Incomplete
    def __init__(self, base_array: ArrayContraction | ArrayDiagonal | ArrayTensorProduct) -> None: ...
    def insert_after(self, arg: _ArgE, new_arg: _ArgE): ...
    def get_new_contraction_index(self): ...
    def refresh_indices(self) -> None: ...
    def merge_scalars(self) -> None: ...
    def to_array_contraction(self): ...
    def get_contraction_indices(self) -> List[List[int]]: ...
    def get_mapping_for_index(self, ind) -> List[_IndPos]: ...
    def get_contraction_indices_to_ind_rel_pos(self) -> List[List[_IndPos]]: ...
    def count_args_with_index(self, index: int) -> int:
        """
        Count the number of arguments that have the given index.
        """
    def get_args_with_index(self, index: int) -> List[_ArgE]:
        """
        Get a list of arguments having the given index.
        """
    @property
    def number_of_diagonal_indices(self): ...
    def track_permutation_start(self) -> None: ...
    def track_permutation_merge(self, destination: _ArgE, from_element: _ArgE): ...
    def get_absolute_free_range(self, arg: _ArgE) -> typing.Tuple[int, int]:
        """
        Return the range of the free indices of the arg as absolute positions
        among all free indices.
        """
    def get_absolute_range(self, arg: _ArgE) -> typing.Tuple[int, int]:
        """
        Return the absolute range of indices for arg, disregarding dummy
        indices.
        """

def get_rank(expr): ...
def get_shape(expr): ...
def nest_permutation(expr): ...
