from _typeshed import Incomplete
from sympy.core import Add as Add, Eq as Eq, Expr as Expr, Mul as Mul, Pow as Pow, S as S, expand_mul as expand_mul, expand_multinomial as expand_multinomial
from sympy.core.exprtools import decompose_power as decompose_power, decompose_power_rat as decompose_power_rat
from sympy.polys.polyerrors import GeneratorsError as GeneratorsError, PolynomialError as PolynomialError
from sympy.polys.polyoptions import build_options as build_options

illegal_types: Incomplete
finf: Incomplete

def parallel_dict_from_expr(exprs, **args):
    """Transform expressions into a multinomial form. """
def dict_from_expr(expr, **args):
    """Transform an expression into a multinomial form. """
def expr_from_dict(rep, *gens):
    """Convert a multinomial form into an expression. """
parallel_dict_from_basic = parallel_dict_from_expr
dict_from_basic = dict_from_expr
basic_from_dict = expr_from_dict

class PicklableWithSlots:
    """
    Mixin class that allows to pickle objects with ``__slots__``.

    Examples
    ========

    First define a class that mixes :class:`PicklableWithSlots` in::

        >>> from sympy.polys.polyutils import PicklableWithSlots
        >>> class Some(PicklableWithSlots):
        ...     __slots__ = ('foo', 'bar')
        ...
        ...     def __init__(self, foo, bar):
        ...         self.foo = foo
        ...         self.bar = bar

    To make :mod:`pickle` happy in doctest we have to use these hacks::

        >>> import builtins
        >>> builtins.Some = Some
        >>> from sympy.polys import polyutils
        >>> polyutils.Some = Some

    Next lets see if we can create an instance, pickle it and unpickle::

        >>> some = Some('abc', 10)
        >>> some.foo, some.bar
        ('abc', 10)

        >>> from pickle import dumps, loads
        >>> some2 = loads(dumps(some))

        >>> some2.foo, some2.bar
        ('abc', 10)

    """

class IntegerPowerable:
    """
    Mixin class for classes that define a `__mul__` method, and want to be
    raised to integer powers in the natural way that follows. Implements
    powering via binary expansion, for efficiency.

    By default, only integer powers $\\geq 2$ are supported. To support the
    first, zeroth, or negative powers, override the corresponding methods,
    `_first_power`, `_zeroth_power`, `_negative_power`, below.
    """
    def __pow__(self, e, modulo: Incomplete | None = None): ...
