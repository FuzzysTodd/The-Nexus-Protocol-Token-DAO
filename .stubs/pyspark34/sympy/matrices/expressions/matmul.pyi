from .inverse import Inverse as Inverse
from .matexpr import MatrixExpr as MatrixExpr
from .matpow import MatPow as MatPow
from .permutation import PermutationMatrix as PermutationMatrix
from .special import GenericIdentity as GenericIdentity, Identity as Identity, OneMatrix as OneMatrix, ZeroMatrix as ZeroMatrix
from .transpose import transpose as transpose
from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.assumptions.refine import handlers_dict as handlers_dict
from sympy.core import Basic as Basic, S as S, sympify as sympify
from sympy.core.mul import Mul as Mul, mul as mul
from sympy.core.numbers import Integer as Integer, Number as Number
from sympy.core.symbol import Dummy as Dummy
from sympy.functions import adjoint as adjoint
from sympy.matrices.common import NonInvertibleMatrixError as NonInvertibleMatrixError
from sympy.matrices.matrices import MatrixBase as MatrixBase
from sympy.strategies import do_one as do_one, exhaust as exhaust, flatten as flatten, new as new, rm_id as rm_id, typed as typed, unpack as unpack
from sympy.utilities.exceptions import sympy_deprecation_warning as sympy_deprecation_warning

class MatMul(MatrixExpr, Mul):
    """
    A product of matrix expressions

    Examples
    ========

    >>> from sympy import MatMul, MatrixSymbol
    >>> A = MatrixSymbol('A', 5, 4)
    >>> B = MatrixSymbol('B', 4, 3)
    >>> C = MatrixSymbol('C', 3, 6)
    >>> MatMul(A, B, C)
    A*B*C
    """
    is_MatMul: bool
    identity: Incomplete
    def __new__(cls, *args, evaluate: bool = False, check: Incomplete | None = None, _sympify: bool = True): ...
    @property
    def shape(self): ...
    def as_coeff_matrices(self): ...
    def as_coeff_mmul(self): ...
    def expand(self, **kwargs): ...
    def doit(self, **hints): ...
    def args_cnc(self, cset: bool = False, warn: bool = True, **kwargs): ...

def newmul(*args): ...
def any_zeros(mul): ...
def merge_explicit(matmul):
    """ Merge explicit MatrixBase arguments

    >>> from sympy import MatrixSymbol, Matrix, MatMul, pprint
    >>> from sympy.matrices.expressions.matmul import merge_explicit
    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = Matrix([[1, 1], [1, 1]])
    >>> C = Matrix([[1, 2], [3, 4]])
    >>> X = MatMul(A, B, C)
    >>> pprint(X)
      [1  1] [1  2]
    A*[    ]*[    ]
      [1  1] [3  4]
    >>> pprint(merge_explicit(X))
      [4  6]
    A*[    ]
      [4  6]

    >>> X = MatMul(B, A, C)
    >>> pprint(X)
    [1  1]   [1  2]
    [    ]*A*[    ]
    [1  1]   [3  4]
    >>> pprint(merge_explicit(X))
    [1  1]   [1  2]
    [    ]*A*[    ]
    [1  1]   [3  4]
    """
def remove_ids(mul):
    """ Remove Identities from a MatMul

    This is a modified version of sympy.strategies.rm_id.
    This is necesssary because MatMul may contain both MatrixExprs and Exprs
    as args.

    See Also
    ========

    sympy.strategies.rm_id
    """
def factor_in_front(mul): ...
def combine_powers(mul):
    """Combine consecutive powers with the same base into one, e.g.
    $$A \\times A^2 \\Rightarrow A^3$$

    This also cancels out the possible matrix inverses using the
    knowledgebase of :class:`~.Inverse`, e.g.,
    $$ Y \\times X \\times X^{-1} \\Rightarrow Y $$
    """
def combine_permutations(mul):
    """Refine products of permutation matrices as the products of cycles.
    """
def combine_one_matrices(mul):
    """
    Combine products of OneMatrix

    e.g. OneMatrix(2, 3) * OneMatrix(3, 4) -> 3 * OneMatrix(2, 4)
    """
def distribute_monom(mul):
    """
    Simplify MatMul expressions but distributing
    rational term to MatMul.

    e.g. 2*(A+B) -> 2*A + 2*B
    """

rules: Incomplete
canonicalize: Incomplete

def only_squares(*matrices):
    """factor matrices only if they are square"""
def refine_MatMul(expr, assumptions):
    """
    >>> from sympy import MatrixSymbol, Q, assuming, refine
    >>> X = MatrixSymbol('X', 2, 2)
    >>> expr = X * X.T
    >>> print(expr)
    X*X.T
    >>> with assuming(Q.orthogonal(X)):
    ...     print(refine(expr))
    I
    """
