from sympy.core import Basic as Basic, Expr as Expr
from sympy.matrices.expressions.transpose import transpose as transpose

class DotProduct(Expr):
    """
    Dot product of vector matrices

    The input should be two 1 x n or n x 1 matrices. The output represents the
    scalar dotproduct.

    This is similar to using MatrixElement and MatMul, except DotProduct does
    not require that one vector to be a row vector and the other vector to be
    a column vector.

    >>> from sympy import MatrixSymbol, DotProduct
    >>> A = MatrixSymbol('A', 1, 3)
    >>> B = MatrixSymbol('B', 1, 3)
    >>> DotProduct(A, B)
    DotProduct(A, B)
    >>> DotProduct(A, B).doit()
    A[0, 0]*B[0, 0] + A[0, 1]*B[0, 1] + A[0, 2]*B[0, 2]
    """
    def __new__(cls, arg1, arg2): ...
    def doit(self, expand: bool = False, **hints): ...
