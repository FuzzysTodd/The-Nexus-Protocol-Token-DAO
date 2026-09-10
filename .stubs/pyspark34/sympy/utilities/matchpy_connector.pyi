from _typeshed import Incomplete
from matchpy import Wildcard
from sympy.core.add import Add as Add
from sympy.core.basic import Basic as Basic
from sympy.core.expr import Expr as Expr
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.relational import Equality as Equality, Unequality as Unequality
from sympy.core.symbol import Symbol as Symbol
from sympy.external import import_module as import_module
from sympy.functions import cos as cos, cot as cot, csc as csc, erf as erf, gamma as gamma, log as log, sec as sec, sin as sin, tan as tan, uppergamma as uppergamma
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.hyperbolic import acosh as acosh, acoth as acoth, acsch as acsch, asech as asech, asinh as asinh, atanh as atanh, cosh as cosh, coth as coth, csch as csch, sech as sech, sinh as sinh, tanh as tanh
from sympy.functions.elementary.trigonometric import acos as acos, acot as acot, acsc as acsc, asec as asec, asin as asin, atan as atan
from sympy.functions.special.error_functions import Ei as Ei, erfc as erfc, erfi as erfi, fresnelc as fresnelc, fresnels as fresnels
from sympy.integrals.integrals import Integral as Integral
from sympy.printing.repr import srepr as srepr
from sympy.utilities.decorator import doctest_depends_on as doctest_depends_on
from typing import List

matchpy: Incomplete

def _(operation): ...
def sympy_op_factory(old_operation, new_operands, variable_name: bool = True): ...

class Wildcard:
    min_count: Incomplete
    fixed_size: Incomplete
    variable_name: Incomplete
    optional: Incomplete
    def __init__(self, min_length, fixed_size, variable_name, optional) -> None: ...

class _WildAbstract(Wildcard, Symbol):
    min_length: int
    fixed_size: bool
    def __init__(self, variable_name: Incomplete | None = None, optional: Incomplete | None = None, **assumptions) -> None: ...
    def __new__(cls, variable_name: Incomplete | None = None, optional: Incomplete | None = None, **assumptions): ...
    def __getnewargs__(self): ...
    @staticmethod
    def __xnew__(cls, variable_name: Incomplete | None = None, optional: Incomplete | None = None, **assumptions): ...
    def __copy__(self) -> _WildAbstract: ...

class WildDot(_WildAbstract):
    min_length: int
    fixed_size: bool

class WildPlus(_WildAbstract):
    min_length: int
    fixed_size: bool

class WildStar(_WildAbstract):
    min_length: int
    fixed_size: bool

class Replacer:
    '''
    Replacer object to perform multiple pattern matching and subexpression
    replacements in SymPy expressions.

    Examples
    ========

    Example to construct a simple first degree equation solver:

    >>> from sympy.utilities.matchpy_connector import WildDot, Replacer
    >>> from sympy import Equality, Symbol
    >>> x = Symbol("x")
    >>> a_ = WildDot("a_", optional=1)
    >>> b_ = WildDot("b_", optional=0)

    The lines above have defined two wildcards, ``a_`` and ``b_``, the
    coefficients of the equation `a x + b = 0`. The optional values specified
    indicate which expression to return in case no match is found, they are
    necessary in equations like `a x = 0` and `x + b = 0`.

    Create two constraints to make sure that ``a_`` and ``b_`` will not match
    any expression containing ``x``:

    >>> from matchpy import CustomConstraint
    >>> free_x_a = CustomConstraint(lambda a_: not a_.has(x))
    >>> free_x_b = CustomConstraint(lambda b_: not b_.has(x))

    Now create the rule replacer with the constraints:

    >>> replacer = Replacer(common_constraints=[free_x_a, free_x_b])

    Add the matching rule:

    >>> replacer.add(Equality(a_*x + b_, 0), -b_/a_)

    Let\'s try it:

    >>> replacer.replace(Equality(3*x + 4, 0))
    -4/3

    Notice that it will not match equations expressed with other patterns:

    >>> eq = Equality(3*x, 4)
    >>> replacer.replace(eq)
    Eq(3*x, 4)

    In order to extend the matching patterns, define another one (we also need
    to clear the cache, because the previous result has already been memorized
    and the pattern matcher will not iterate again if given the same expression)

    >>> replacer.add(Equality(a_*x, b_), b_/a_)
    >>> replacer._replacer.matcher.clear()
    >>> replacer.replace(eq)
    4/3
    '''
    def __init__(self, common_constraints: list = []) -> None: ...
    def add(self, expr: Expr, result: Expr, conditions_true: List[Expr] = [], conditions_nonfalse: List[Expr] = []) -> None: ...
    def replace(self, expr: Expr) -> Expr: ...
