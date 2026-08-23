from .sets import Set as Set
from sympy.core import S as S
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.logic.boolalg import BooleanFunction as BooleanFunction
from sympy.utilities.misc import func_name as func_name

class Contains(BooleanFunction):
    """
    Asserts that x is an element of the set S.

    Examples
    ========

    >>> from sympy import Symbol, Integer, S, Contains
    >>> Contains(Integer(2), S.Integers)
    True
    >>> Contains(Integer(-2), S.Naturals)
    False
    >>> i = Symbol('i', integer=True)
    >>> Contains(i, S.Naturals)
    Contains(i, Naturals)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Element_%28mathematics%29
    """
    @classmethod
    def eval(cls, x, s): ...
    @property
    def binary_symbols(self): ...
    def as_set(self): ...
