from .add import Add as Add
from .exprtools import gcd_terms as gcd_terms
from .function import Function as Function
from .kind import NumberKind as NumberKind
from .logic import fuzzy_and as fuzzy_and, fuzzy_not as fuzzy_not
from .mul import Mul as Mul
from .numbers import equal_valued as equal_valued
from .singleton import S as S

class Mod(Function):
    """Represents a modulo operation on symbolic expressions.

    Parameters
    ==========

    p : Expr
        Dividend.

    q : Expr
        Divisor.

    Notes
    =====

    The convention used is the same as Python's: the remainder always has the
    same sign as the divisor.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> x**2 % y
    Mod(x**2, y)
    >>> _.subs({x: 5, y: 6})
    1

    """
    kind = NumberKind
    @classmethod
    def eval(cls, p, q): ...
