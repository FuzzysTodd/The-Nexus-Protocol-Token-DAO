from sympy.core.expr import Expr as Expr
from sympy.core.mul import Mul as Mul
from sympy.core.parameters import global_parameters as global_parameters
from sympy.core.singleton import S as S
from sympy.core.sympify import sympify as sympify

class TensorProduct(Expr):
    """
    Generic class for tensor products.
    """
    is_number: bool
    def __new__(cls, *args, **kwargs): ...
    def rank(self): ...
    @property
    def shape(self): ...
    def __getitem__(self, index): ...

def shape(expr):
    """
    Return the shape of the *expr* as a tuple. *expr* should represent
    suitable object such as matrix or array.

    Parameters
    ==========

    expr : SymPy object having ``MatrixKind`` or ``ArrayKind``.

    Raises
    ======

    NoShapeError : Raised when object with wrong kind is passed.

    Examples
    ========

    This function returns the shape of any object representing matrix or array.

    >>> from sympy import shape, Array, ImmutableDenseMatrix, Integral
    >>> from sympy.abc import x
    >>> A = Array([1, 2])
    >>> shape(A)
    (2,)
    >>> shape(Integral(A, x))
    (2,)
    >>> M = ImmutableDenseMatrix([1, 2])
    >>> shape(M)
    (2, 1)
    >>> shape(Integral(M, x))
    (2, 1)

    You can support new type by dispatching.

    >>> from sympy import Expr
    >>> class NewExpr(Expr):
    ...     pass
    >>> @shape.register(NewExpr)
    ... def _(expr):
    ...     return shape(expr.args[0])
    >>> shape(NewExpr(M))
    (2, 1)

    If unsuitable expression is passed, ``NoShapeError()`` will be raised.

    >>> shape(Integral(x, x))
    Traceback (most recent call last):
      ...
    sympy.tensor.functions.NoShapeError: shape() called on non-array object: Integral(x, x)

    Notes
    =====

    Array-like classes (such as ``Matrix`` or ``NDimArray``) has ``shape``
    property which returns its shape, but it cannot be used for non-array
    classes containing array. This function returns the shape of any
    registered object representing array.

    """

class NoShapeError(Exception):
    """
    Raised when ``shape()`` is called on non-array object.

    This error can be imported from ``sympy.tensor.functions``.

    Examples
    ========

    >>> from sympy import shape
    >>> from sympy.abc import x
    >>> shape(x)
    Traceback (most recent call last):
      ...
    sympy.tensor.functions.NoShapeError: shape() called on non-array object: x
    """
