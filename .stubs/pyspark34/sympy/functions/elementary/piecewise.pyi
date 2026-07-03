from _typeshed import Incomplete
from sympy.core import Dummy as Dummy, Function as Function, Mul as Mul, S as S, Tuple as Tuple, diff as diff
from sympy.core.basic import Basic as Basic, as_Basic as as_Basic
from sympy.core.numbers import NumberSymbol as NumberSymbol, Rational as Rational
from sympy.core.parameters import global_parameters as global_parameters
from sympy.core.relational import Eq as Eq, Gt as Gt, Lt as Lt, Ne as Ne, Relational as Relational
from sympy.core.sorting import ordered as ordered
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.logic.boolalg import And as And, Boolean as Boolean, ITE as ITE, Not as Not, Or as Or, distribute_and_over_or as distribute_and_over_or, distribute_or_over_and as distribute_or_over_and, false as false, simplify_logic as simplify_logic, to_cnf as to_cnf, true as true
from sympy.utilities.iterables import common_prefix as common_prefix, sift as sift, uniq as uniq
from sympy.utilities.misc import filldedent as filldedent, func_name as func_name

Undefined: Incomplete

class ExprCondPair(Tuple):
    """Represents an expression, condition pair."""
    def __new__(cls, expr, cond): ...
    @property
    def expr(self):
        """
        Returns the expression of this pair.
        """
    @property
    def cond(self):
        """
        Returns the condition of this pair.
        """
    @property
    def is_commutative(self): ...
    def __iter__(self): ...

class Piecewise(Function):
    """
    Represents a piecewise function.

    Usage:

      Piecewise( (expr,cond), (expr,cond), ... )
        - Each argument is a 2-tuple defining an expression and condition
        - The conds are evaluated in turn returning the first that is True.
          If any of the evaluated conds are not explicitly False,
          e.g. ``x < 1``, the function is returned in symbolic form.
        - If the function is evaluated at a place where all conditions are False,
          nan will be returned.
        - Pairs where the cond is explicitly False, will be removed and no pair
          appearing after a True condition will ever be retained. If a single
          pair with a True condition remains, it will be returned, even when
          evaluation is False.

    Examples
    ========

    >>> from sympy import Piecewise, log, piecewise_fold
    >>> from sympy.abc import x, y
    >>> f = x**2
    >>> g = log(x)
    >>> p = Piecewise((0, x < -1), (f, x <= 1), (g, True))
    >>> p.subs(x,1)
    1
    >>> p.subs(x,5)
    log(5)

    Booleans can contain Piecewise elements:

    >>> cond = (x < y).subs(x, Piecewise((2, x < 0), (3, True))); cond
    Piecewise((2, x < 0), (3, True)) < y

    The folded version of this results in a Piecewise whose
    expressions are Booleans:

    >>> folded_cond = piecewise_fold(cond); folded_cond
    Piecewise((2 < y, x < 0), (3 < y, True))

    When a Boolean containing Piecewise (like cond) or a Piecewise
    with Boolean expressions (like folded_cond) is used as a condition,
    it is converted to an equivalent :class:`~.ITE` object:

    >>> Piecewise((1, folded_cond))
    Piecewise((1, ITE(x < 0, y > 2, y > 3)))

    When a condition is an ``ITE``, it will be converted to a simplified
    Boolean expression:

    >>> piecewise_fold(_)
    Piecewise((1, ((x >= 0) | (y > 2)) & ((y > 3) | (x < 0))))

    See Also
    ========

    piecewise_fold
    piecewise_exclusive
    ITE
    """
    nargs: Incomplete
    is_Piecewise: bool
    def __new__(cls, *args, **options): ...
    @classmethod
    def eval(cls, *_args):
        """Either return a modified version of the args or, if no
        modifications were made, return None.

        Modifications that are made here:

        1. relationals are made canonical
        2. any False conditions are dropped
        3. any repeat of a previous condition is ignored
        4. any args past one with a true condition are dropped

        If there are no args left, nan will be returned.
        If there is a single arg with a True condition, its
        corresponding expression will be returned.

        EXAMPLES
        ========

        >>> from sympy import Piecewise
        >>> from sympy.abc import x
        >>> cond = -x < -1
        >>> args = [(1, cond), (4, cond), (3, False), (2, True), (5, x < 1)]
        >>> Piecewise(*args, evaluate=False)
        Piecewise((1, -x < -1), (4, -x < -1), (2, True))
        >>> Piecewise(*args)
        Piecewise((1, x > 1), (2, True))
        """
    def doit(self, **hints):
        """
        Evaluate this piecewise function.
        """
    def piecewise_integrate(self, x, **kwargs):
        """Return the Piecewise with each expression being
        replaced with its antiderivative. To obtain a continuous
        antiderivative, use the :func:`~.integrate` function or method.

        Examples
        ========

        >>> from sympy import Piecewise
        >>> from sympy.abc import x
        >>> p = Piecewise((0, x < 0), (1, x < 1), (2, True))
        >>> p.piecewise_integrate(x)
        Piecewise((0, x < 0), (x, x < 1), (2*x, True))

        Note that this does not give a continuous function, e.g.
        at x = 1 the 3rd condition applies and the antiderivative
        there is 2*x so the value of the antiderivative is 2:

        >>> anti = _
        >>> anti.subs(x, 1)
        2

        The continuous derivative accounts for the integral *up to*
        the point of interest, however:

        >>> p.integrate(x)
        Piecewise((0, x < 0), (x, x < 1), (2*x - 1, True))
        >>> _.subs(x, 1)
        1

        See Also
        ========
        Piecewise._eval_integral
        """
    def as_expr_set_pairs(self, domain: Incomplete | None = None):
        """Return tuples for each argument of self that give
        the expression and the interval in which it is valid
        which is contained within the given domain.
        If a condition cannot be converted to a set, an error
        will be raised. The variable of the conditions is
        assumed to be real; sets of real values are returned.

        Examples
        ========

        >>> from sympy import Piecewise, Interval
        >>> from sympy.abc import x
        >>> p = Piecewise(
        ...     (1, x < 2),
        ...     (2,(x > 0) & (x < 4)),
        ...     (3, True))
        >>> p.as_expr_set_pairs()
        [(1, Interval.open(-oo, 2)),
         (2, Interval.Ropen(2, 4)),
         (3, Interval(4, oo))]
        >>> p.as_expr_set_pairs(Interval(0, 3))
        [(1, Interval.Ropen(0, 2)),
         (2, Interval(2, 3))]
        """

def piecewise_fold(expr, evaluate: bool = True):
    """
    Takes an expression containing a piecewise function and returns the
    expression in piecewise form. In addition, any ITE conditions are
    rewritten in negation normal form and simplified.

    The final Piecewise is evaluated (default) but if the raw form
    is desired, send ``evaluate=False``; if trivial evaluation is
    desired, send ``evaluate=None`` and duplicate conditions and
    processing of True and False will be handled.

    Examples
    ========

    >>> from sympy import Piecewise, piecewise_fold, S
    >>> from sympy.abc import x
    >>> p = Piecewise((x, x < 1), (1, S(1) <= x))
    >>> piecewise_fold(x*p)
    Piecewise((x**2, x < 1), (x, True))

    See Also
    ========

    Piecewise
    piecewise_exclusive
    """
def piecewise_simplify_arguments(expr, **kwargs): ...
def piecewise_simplify(expr, **kwargs): ...
def piecewise_exclusive(expr, *, skip_nan: bool = False, deep: bool = True):
    '''
    Rewrite :class:`Piecewise` with mutually exclusive conditions.

    Explanation
    ===========

    SymPy represents the conditions of a :class:`Piecewise` in an
    "if-elif"-fashion, allowing more than one condition to be simultaneously
    True. The interpretation is that the first condition that is True is the
    case that holds. While this is a useful representation computationally it
    is not how a piecewise formula is typically shown in a mathematical text.
    The :func:`piecewise_exclusive` function can be used to rewrite any
    :class:`Piecewise` with more typical mutually exclusive conditions.

    Note that further manipulation of the resulting :class:`Piecewise`, e.g.
    simplifying it, will most likely make it non-exclusive. Hence, this is
    primarily a function to be used in conjunction with printing the Piecewise
    or if one would like to reorder the expression-condition pairs.

    If it is not possible to determine that all possibilities are covered by
    the different cases of the :class:`Piecewise` then a final
    :class:`~sympy.core.numbers.NaN` case will be included explicitly. This
    can be prevented by passing ``skip_nan=True``.

    Examples
    ========

    >>> from sympy import piecewise_exclusive, Symbol, Piecewise, S
    >>> x = Symbol(\'x\', real=True)
    >>> p = Piecewise((0, x < 0), (S.Half, x <= 0), (1, True))
    >>> piecewise_exclusive(p)
    Piecewise((0, x < 0), (1/2, Eq(x, 0)), (1, x > 0))
    >>> piecewise_exclusive(Piecewise((2, x > 1)))
    Piecewise((2, x > 1), (nan, x <= 1))
    >>> piecewise_exclusive(Piecewise((2, x > 1)), skip_nan=True)
    Piecewise((2, x > 1))

    Parameters
    ==========

    expr: a SymPy expression.
        Any :class:`Piecewise` in the expression will be rewritten.
    skip_nan: ``bool`` (default ``False``)
        If ``skip_nan`` is set to ``True`` then a final
        :class:`~sympy.core.numbers.NaN` case will not be included.
    deep:  ``bool`` (default ``True``)
        If ``deep`` is ``True`` then :func:`piecewise_exclusive` will rewrite
        any :class:`Piecewise` subexpressions in ``expr`` rather than just
        rewriting ``expr`` itself.

    Returns
    =======

    An expression equivalent to ``expr`` but where all :class:`Piecewise` have
    been rewritten with mutually exclusive conditions.

    See Also
    ========

    Piecewise
    piecewise_fold
    '''
