from sympy.core.expr import ExprBuilder as ExprBuilder
from sympy.core.function import Function as Function, FunctionClass as FunctionClass, Lambda as Lambda
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.matrices.expressions import MatrixExpr as MatrixExpr
from sympy.matrices.matrices import MatrixBase as MatrixBase

class ElementwiseApplyFunction(MatrixExpr):
    '''
    Apply function to a matrix elementwise without evaluating.

    Examples
    ========

    It can be created by calling ``.applyfunc(<function>)`` on a matrix
    expression:

    >>> from sympy import MatrixSymbol
    >>> from sympy.matrices.expressions.applyfunc import ElementwiseApplyFunction
    >>> from sympy import exp
    >>> X = MatrixSymbol("X", 3, 3)
    >>> X.applyfunc(exp)
    Lambda(_d, exp(_d)).(X)

    Otherwise using the class constructor:

    >>> from sympy import eye
    >>> expr = ElementwiseApplyFunction(exp, eye(3))
    >>> expr
    Lambda(_d, exp(_d)).(Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]]))
    >>> expr.doit()
    Matrix([
    [E, 1, 1],
    [1, E, 1],
    [1, 1, E]])

    Notice the difference with the real mathematical functions:

    >>> exp(eye(3))
    Matrix([
    [E, 0, 0],
    [0, E, 0],
    [0, 0, E]])
    '''
    def __new__(cls, function, expr): ...
    @property
    def function(self): ...
    @property
    def expr(self): ...
    @property
    def shape(self): ...
    def doit(self, **hints): ...
