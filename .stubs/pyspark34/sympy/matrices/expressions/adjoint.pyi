from sympy.core import Basic as Basic
from sympy.functions import adjoint as adjoint, conjugate as conjugate
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr
from sympy.matrices.expressions.transpose import transpose as transpose

class Adjoint(MatrixExpr):
    """
    The Hermitian adjoint of a matrix expression.

    This is a symbolic object that simply stores its argument without
    evaluating it. To actually compute the adjoint, use the ``adjoint()``
    function.

    Examples
    ========

    >>> from sympy import MatrixSymbol, Adjoint, adjoint
    >>> A = MatrixSymbol('A', 3, 5)
    >>> B = MatrixSymbol('B', 5, 3)
    >>> Adjoint(A*B)
    Adjoint(A*B)
    >>> adjoint(A*B)
    Adjoint(B)*Adjoint(A)
    >>> adjoint(A*B) == Adjoint(A*B)
    False
    >>> adjoint(A*B) == Adjoint(A*B).doit()
    True
    """
    is_Adjoint: bool
    def doit(self, **hints): ...
    @property
    def arg(self): ...
    @property
    def shape(self): ...
