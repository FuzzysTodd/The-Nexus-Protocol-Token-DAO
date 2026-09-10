from _typeshed import Incomplete
from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.assumptions.refine import handlers_dict as handlers_dict
from sympy.core import Basic as Basic, S as S
from sympy.matrices.common import NonSquareMatrixError as NonSquareMatrixError
from sympy.matrices.expressions.matpow import MatPow as MatPow

class Inverse(MatPow):
    """
    The multiplicative inverse of a matrix expression

    This is a symbolic object that simply stores its argument without
    evaluating it. To actually compute the inverse, use the ``.inverse()``
    method of matrices.

    Examples
    ========

    >>> from sympy import MatrixSymbol, Inverse
    >>> A = MatrixSymbol('A', 3, 3)
    >>> B = MatrixSymbol('B', 3, 3)
    >>> Inverse(A)
    A**(-1)
    >>> A.inverse() == Inverse(A)
    True
    >>> (A*B).inverse()
    B**(-1)*A**(-1)
    >>> Inverse(A*B)
    (A*B)**(-1)

    """
    is_Inverse: bool
    exp: Incomplete
    def __new__(cls, mat, exp=...): ...
    @property
    def arg(self): ...
    @property
    def shape(self): ...
    def doit(self, **hints): ...

def refine_Inverse(expr, assumptions):
    """
    >>> from sympy import MatrixSymbol, Q, assuming, refine
    >>> X = MatrixSymbol('X', 2, 2)
    >>> X.I
    X**(-1)
    >>> with assuming(Q.orthogonal(X)):
    ...     print(refine(X.I))
    X.T
    """
