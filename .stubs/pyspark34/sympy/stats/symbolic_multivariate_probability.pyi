from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.expr import Expr as Expr
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.matrices.common import ShapeError as ShapeError
from sympy.matrices.expressions.matexpr import MatrixExpr as MatrixExpr
from sympy.matrices.expressions.matmul import MatMul as MatMul
from sympy.matrices.expressions.special import ZeroMatrix as ZeroMatrix
from sympy.stats.rv import RandomSymbol as RandomSymbol, is_random as is_random
from sympy.stats.symbolic_probability import Covariance as Covariance, Expectation as Expectation, Variance as Variance

class ExpectationMatrix(Expectation, MatrixExpr):
    '''
    Expectation of a random matrix expression.

    Examples
    ========

    >>> from sympy.stats import ExpectationMatrix, Normal
    >>> from sympy.stats.rv import RandomMatrixSymbol
    >>> from sympy import symbols, MatrixSymbol, Matrix
    >>> k = symbols("k")
    >>> A, B = MatrixSymbol("A", k, k), MatrixSymbol("B", k, k)
    >>> X, Y = RandomMatrixSymbol("X", k, 1), RandomMatrixSymbol("Y", k, 1)
    >>> ExpectationMatrix(X)
    ExpectationMatrix(X)
    >>> ExpectationMatrix(A*X).shape
    (k, 1)

    To expand the expectation in its expression, use ``expand()``:

    >>> ExpectationMatrix(A*X + B*Y).expand()
    A*ExpectationMatrix(X) + B*ExpectationMatrix(Y)
    >>> ExpectationMatrix((X + Y)*(X - Y).T).expand()
    ExpectationMatrix(X*X.T) - ExpectationMatrix(X*Y.T) + ExpectationMatrix(Y*X.T) - ExpectationMatrix(Y*Y.T)

    To evaluate the ``ExpectationMatrix``, use ``doit()``:

    >>> N11, N12 = Normal(\'N11\', 11, 1), Normal(\'N12\', 12, 1)
    >>> N21, N22 = Normal(\'N21\', 21, 1), Normal(\'N22\', 22, 1)
    >>> M11, M12 = Normal(\'M11\', 1, 1), Normal(\'M12\', 2, 1)
    >>> M21, M22 = Normal(\'M21\', 3, 1), Normal(\'M22\', 4, 1)
    >>> x1 = Matrix([[N11, N12], [N21, N22]])
    >>> x2 = Matrix([[M11, M12], [M21, M22]])
    >>> ExpectationMatrix(x1 + x2).doit()
    Matrix([
    [12, 14],
    [24, 26]])

    '''
    def __new__(cls, expr, condition: Incomplete | None = None): ...
    @property
    def shape(self): ...
    def expand(self, **hints): ...

class VarianceMatrix(Variance, MatrixExpr):
    '''
    Variance of a random matrix probability expression. Also known as
    Covariance matrix, auto-covariance matrix, dispersion matrix,
    or variance-covariance matrix.

    Examples
    ========

    >>> from sympy.stats import VarianceMatrix
    >>> from sympy.stats.rv import RandomMatrixSymbol
    >>> from sympy import symbols, MatrixSymbol
    >>> k = symbols("k")
    >>> A, B = MatrixSymbol("A", k, k), MatrixSymbol("B", k, k)
    >>> X, Y = RandomMatrixSymbol("X", k, 1), RandomMatrixSymbol("Y", k, 1)
    >>> VarianceMatrix(X)
    VarianceMatrix(X)
    >>> VarianceMatrix(X).shape
    (k, k)

    To expand the variance in its expression, use ``expand()``:

    >>> VarianceMatrix(A*X).expand()
    A*VarianceMatrix(X)*A.T
    >>> VarianceMatrix(A*X + B*Y).expand()
    2*A*CrossCovarianceMatrix(X, Y)*B.T + A*VarianceMatrix(X)*A.T + B*VarianceMatrix(Y)*B.T
    '''
    def __new__(cls, arg, condition: Incomplete | None = None): ...
    @property
    def shape(self): ...
    def expand(self, **hints): ...

class CrossCovarianceMatrix(Covariance, MatrixExpr):
    '''
    Covariance of a random matrix probability expression.

    Examples
    ========

    >>> from sympy.stats import CrossCovarianceMatrix
    >>> from sympy.stats.rv import RandomMatrixSymbol
    >>> from sympy import symbols, MatrixSymbol
    >>> k = symbols("k")
    >>> A, B = MatrixSymbol("A", k, k), MatrixSymbol("B", k, k)
    >>> C, D = MatrixSymbol("C", k, k), MatrixSymbol("D", k, k)
    >>> X, Y = RandomMatrixSymbol("X", k, 1), RandomMatrixSymbol("Y", k, 1)
    >>> Z, W = RandomMatrixSymbol("Z", k, 1), RandomMatrixSymbol("W", k, 1)
    >>> CrossCovarianceMatrix(X, Y)
    CrossCovarianceMatrix(X, Y)
    >>> CrossCovarianceMatrix(X, Y).shape
    (k, k)

    To expand the covariance in its expression, use ``expand()``:

    >>> CrossCovarianceMatrix(X + Y, Z).expand()
    CrossCovarianceMatrix(X, Z) + CrossCovarianceMatrix(Y, Z)
    >>> CrossCovarianceMatrix(A*X, Y).expand()
    A*CrossCovarianceMatrix(X, Y)
    >>> CrossCovarianceMatrix(A*X, B.T*Y).expand()
    A*CrossCovarianceMatrix(X, Y)*B
    >>> CrossCovarianceMatrix(A*X + B*Y, C.T*Z + D.T*W).expand()
    A*CrossCovarianceMatrix(X, W)*D + A*CrossCovarianceMatrix(X, Z)*C + B*CrossCovarianceMatrix(Y, W)*D + B*CrossCovarianceMatrix(Y, Z)*C

    '''
    def __new__(cls, arg1, arg2, condition: Incomplete | None = None): ...
    @property
    def shape(self): ...
    def expand(self, **hints): ...
