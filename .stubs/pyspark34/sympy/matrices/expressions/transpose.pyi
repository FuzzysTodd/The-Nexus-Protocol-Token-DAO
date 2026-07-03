from sympy.assumptions.ask import Q as Q, ask as ask
from sympy.assumptions.refine import handlers_dict as handlers_dict
from sympy.core.basic import Basic as Basic
from sympy.functions import adjoint as adjoint, conjugate as conjugate
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr

class Transpose(MatrixExpr):
    """
    The transpose of a matrix expression.

    This is a symbolic object that simply stores its argument without
    evaluating it. To actually compute the transpose, use the ``transpose()``
    function, or the ``.T`` attribute of matrices.

    Examples
    ========

    >>> from sympy import MatrixSymbol, Transpose, transpose
    >>> A = MatrixSymbol('A', 3, 5)
    >>> B = MatrixSymbol('B', 5, 3)
    >>> Transpose(A)
    A.T
    >>> A.T == transpose(A) == Transpose(A)
    True
    >>> Transpose(A*B)
    (A*B).T
    >>> transpose(A*B)
    B.T*A.T

    """
    is_Transpose: bool
    def doit(self, **hints): ...
    @property
    def arg(self): ...
    @property
    def shape(self): ...

def transpose(expr):
    """Matrix transpose"""
def refine_Transpose(expr, assumptions):
    """
    >>> from sympy import MatrixSymbol, Q, assuming, refine
    >>> X = MatrixSymbol('X', 2, 2)
    >>> X.T
    X.T
    >>> with assuming(Q.symmetric(X)):
    ...     print(refine(X.T))
    X
    """
