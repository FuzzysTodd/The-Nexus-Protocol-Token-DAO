from sympy.core.basic import Basic as Basic
from sympy.core.expr import Expr as Expr, ExprBuilder as ExprBuilder
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.core.symbol import uniquely_named_symbol as uniquely_named_symbol
from sympy.core.sympify import sympify as sympify
from sympy.matrices.common import NonSquareMatrixError as NonSquareMatrixError
from sympy.matrices.matrices import MatrixBase as MatrixBase

class Trace(Expr):
    """Matrix Trace

    Represents the trace of a matrix expression.

    Examples
    ========

    >>> from sympy import MatrixSymbol, Trace, eye
    >>> A = MatrixSymbol('A', 3, 3)
    >>> Trace(A)
    Trace(A)
    >>> Trace(eye(3))
    Trace(Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]]))
    >>> Trace(eye(3)).simplify()
    3
    """
    is_Trace: bool
    is_commutative: bool
    def __new__(cls, mat): ...
    @property
    def arg(self): ...
    def doit(self, **hints): ...
    def as_explicit(self): ...

def trace(expr):
    """Trace of a Matrix.  Sum of the diagonal elements.

    Examples
    ========

    >>> from sympy import trace, Symbol, MatrixSymbol, eye
    >>> n = Symbol('n')
    >>> X = MatrixSymbol('X', n, n)  # A square matrix
    >>> trace(2*X)
    2*Trace(X)
    >>> trace(eye(3))
    3
    """
