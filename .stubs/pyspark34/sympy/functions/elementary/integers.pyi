from sympy.core import Add as Add, S as S
from sympy.core.basic import Basic as Basic
from sympy.core.evalf import PrecisionExhausted as PrecisionExhausted, get_integer_part as get_integer_part
from sympy.core.expr import Expr as Expr
from sympy.core.function import Function as Function
from sympy.core.logic import fuzzy_or as fuzzy_or
from sympy.core.numbers import Integer as Integer
from sympy.core.relational import Ge as Ge, Gt as Gt, Le as Le, Lt as Lt, Relational as Relational, is_eq as is_eq
from sympy.core.symbol import Symbol as Symbol
from sympy.functions.elementary.complexes import im as im, re as re
from sympy.multipledispatch import dispatch as dispatch
from typing import Tuple as tTuple

class RoundFunction(Function):
    """Abstract base class for rounding functions."""
    args: tTuple[Expr]
    @classmethod
    def eval(cls, arg): ...

class floor(RoundFunction):
    '''
    Floor is a univariate function which returns the largest integer
    value not greater than its argument. This implementation
    generalizes floor to complex numbers by taking the floor of the
    real and imaginary parts separately.

    Examples
    ========

    >>> from sympy import floor, E, I, S, Float, Rational
    >>> floor(17)
    17
    >>> floor(Rational(23, 10))
    2
    >>> floor(2*E)
    5
    >>> floor(-Float(0.567))
    -1
    >>> floor(-I/2)
    -I
    >>> floor(S(5)/2 + 5*I/2)
    2 + 2*I

    See Also
    ========

    sympy.functions.elementary.integers.ceiling

    References
    ==========

    .. [1] "Concrete mathematics" by Graham, pp. 87
    .. [2] https://mathworld.wolfram.com/FloorFunction.html

    '''
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...

class ceiling(RoundFunction):
    '''
    Ceiling is a univariate function which returns the smallest integer
    value not less than its argument. This implementation
    generalizes ceiling to complex numbers by taking the ceiling of the
    real and imaginary parts separately.

    Examples
    ========

    >>> from sympy import ceiling, E, I, S, Float, Rational
    >>> ceiling(17)
    17
    >>> ceiling(Rational(23, 10))
    3
    >>> ceiling(2*E)
    6
    >>> ceiling(-Float(0.567))
    0
    >>> ceiling(I/2)
    I
    >>> ceiling(S(5)/2 + 5*I/2)
    3 + 3*I

    See Also
    ========

    sympy.functions.elementary.integers.floor

    References
    ==========

    .. [1] "Concrete mathematics" by Graham, pp. 87
    .. [2] https://mathworld.wolfram.com/CeilingFunction.html

    '''
    def __lt__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __le__(self, other): ...

class frac(Function):
    """Represents the fractional part of x

    For real numbers it is defined [1]_ as

    .. math::
        x - \\left\\lfloor{x}\\right\\rfloor

    Examples
    ========

    >>> from sympy import Symbol, frac, Rational, floor, I
    >>> frac(Rational(4, 3))
    1/3
    >>> frac(-Rational(4, 3))
    2/3

    returns zero for integer arguments

    >>> n = Symbol('n', integer=True)
    >>> frac(n)
    0

    rewrite as floor

    >>> x = Symbol('x')
    >>> frac(x).rewrite(floor)
    x - floor(x)

    for complex arguments

    >>> r = Symbol('r', real=True)
    >>> t = Symbol('t', real=True)
    >>> frac(t + I*r)
    I*frac(r) + frac(t)

    See Also
    ========

    sympy.functions.elementary.integers.floor
    sympy.functions.elementary.integers.ceiling

    References
    ===========

    .. [1] https://en.wikipedia.org/wiki/Fractional_part
    .. [2] https://mathworld.wolfram.com/FractionalPart.html

    """
    @classmethod
    def eval(cls, arg): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
