from sympy.core import Add as Add, Mul as Mul, Pow as Pow, S as S
from sympy.core.basic import Basic as Basic
from sympy.core.expr import Expr as Expr
from sympy.core.numbers import oo as oo, zoo as zoo
from sympy.core.relational import is_ge as is_ge, is_gt as is_gt, is_le as is_le, is_lt as is_lt
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.logic.boolalg import And as And
from sympy.multipledispatch import dispatch as dispatch
from sympy.series.order import Order as Order
from sympy.sets.sets import FiniteSet as FiniteSet

class AccumulationBounds(Expr):
    """An accumulation bounds.

    # Note AccumulationBounds has an alias: AccumBounds

    AccumulationBounds represent an interval `[a, b]`, which is always closed
    at the ends. Here `a` and `b` can be any value from extended real numbers.

    The intended meaning of AccummulationBounds is to give an approximate
    location of the accumulation points of a real function at a limit point.

    Let `a` and `b` be reals such that `a \\le b`.

    `\\left\\langle a, b\\right\\rangle = \\{x \\in \\mathbb{R} \\mid a \\le x \\le b\\}`

    `\\left\\langle -\\infty, b\\right\\rangle = \\{x \\in \\mathbb{R} \\mid x \\le b\\} \\cup \\{-\\infty, \\infty\\}`

    `\\left\\langle a, \\infty \\right\\rangle = \\{x \\in \\mathbb{R} \\mid a \\le x\\} \\cup \\{-\\infty, \\infty\\}`

    `\\left\\langle -\\infty, \\infty \\right\\rangle = \\mathbb{R} \\cup \\{-\\infty, \\infty\\}`

    ``oo`` and ``-oo`` are added to the second and third definition respectively,
    since if either ``-oo`` or ``oo`` is an argument, then the other one should
    be included (though not as an end point). This is forced, since we have,
    for example, ``1/AccumBounds(0, 1) = AccumBounds(1, oo)``, and the limit at
    `0` is not one-sided. As `x` tends to `0-`, then `1/x \\rightarrow -\\infty`, so `-\\infty`
    should be interpreted as belonging to ``AccumBounds(1, oo)`` though it need
    not appear explicitly.

    In many cases it suffices to know that the limit set is bounded.
    However, in some other cases more exact information could be useful.
    For example, all accumulation values of `\\cos(x) + 1` are non-negative.
    (``AccumBounds(-1, 1) + 1 = AccumBounds(0, 2)``)

    A AccumulationBounds object is defined to be real AccumulationBounds,
    if its end points are finite reals.

    Let `X`, `Y` be real AccumulationBounds, then their sum, difference,
    product are defined to be the following sets:

    `X + Y = \\{ x+y \\mid x \\in X \\cap y \\in Y\\}`

    `X - Y = \\{ x-y \\mid x \\in X \\cap y \\in Y\\}`

    `X \\times Y = \\{ x \\times y \\mid x \\in X \\cap y \\in Y\\}`

    When an AccumBounds is raised to a negative power, if 0 is contained
    between the bounds then an infinite range is returned, otherwise if an
    endpoint is 0 then a semi-infinite range with consistent sign will be returned.

    AccumBounds in expressions behave a lot like Intervals but the
    semantics are not necessarily the same. Division (or exponentiation
    to a negative integer power) could be handled with *intervals* by
    returning a union of the results obtained after splitting the
    bounds between negatives and positives, but that is not done with
    AccumBounds. In addition, bounds are assumed to be independent of
    each other; if the same bound is used in more than one place in an
    expression, the result may not be the supremum or infimum of the
    expression (see below). Finally, when a boundary is ``1``,
    exponentiation to the power of ``oo`` yields ``oo``, neither
    ``1`` nor ``nan``.

    Examples
    ========

    >>> from sympy import AccumBounds, sin, exp, log, pi, E, S, oo
    >>> from sympy.abc import x

    >>> AccumBounds(0, 1) + AccumBounds(1, 2)
    AccumBounds(1, 3)

    >>> AccumBounds(0, 1) - AccumBounds(0, 2)
    AccumBounds(-2, 1)

    >>> AccumBounds(-2, 3)*AccumBounds(-1, 1)
    AccumBounds(-3, 3)

    >>> AccumBounds(1, 2)*AccumBounds(3, 5)
    AccumBounds(3, 10)

    The exponentiation of AccumulationBounds is defined
    as follows:

    If 0 does not belong to `X` or `n > 0` then

    `X^n = \\{ x^n \\mid x \\in X\\}`

    >>> AccumBounds(1, 4)**(S(1)/2)
    AccumBounds(1, 2)

    otherwise, an infinite or semi-infinite result is obtained:

    >>> 1/AccumBounds(-1, 1)
    AccumBounds(-oo, oo)
    >>> 1/AccumBounds(0, 2)
    AccumBounds(1/2, oo)
    >>> 1/AccumBounds(-oo, 0)
    AccumBounds(-oo, 0)

    A boundary of 1 will always generate all nonnegatives:

    >>> AccumBounds(1, 2)**oo
    AccumBounds(0, oo)
    >>> AccumBounds(0, 1)**oo
    AccumBounds(0, oo)

    If the exponent is itself an AccumulationBounds or is not an
    integer then unevaluated results will be returned unless the base
    values are positive:

    >>> AccumBounds(2, 3)**AccumBounds(-1, 2)
    AccumBounds(1/3, 9)
    >>> AccumBounds(-2, 3)**AccumBounds(-1, 2)
    AccumBounds(-2, 3)**AccumBounds(-1, 2)

    >>> AccumBounds(-2, -1)**(S(1)/2)
    sqrt(AccumBounds(-2, -1))

    Note: `\\left\\langle a, b\\right\\rangle^2` is not same as `\\left\\langle a, b\\right\\rangle \\times \\left\\langle a, b\\right\\rangle`

    >>> AccumBounds(-1, 1)**2
    AccumBounds(0, 1)

    >>> AccumBounds(1, 3) < 4
    True

    >>> AccumBounds(1, 3) < -1
    False

    Some elementary functions can also take AccumulationBounds as input.
    A function `f` evaluated for some real AccumulationBounds `\\left\\langle a, b \\right\\rangle`
    is defined as `f(\\left\\langle a, b\\right\\rangle) = \\{ f(x) \\mid a \\le x \\le b \\}`

    >>> sin(AccumBounds(pi/6, pi/3))
    AccumBounds(1/2, sqrt(3)/2)

    >>> exp(AccumBounds(0, 1))
    AccumBounds(1, E)

    >>> log(AccumBounds(1, E))
    AccumBounds(0, 1)

    Some symbol in an expression can be substituted for a AccumulationBounds
    object. But it does not necessarily evaluate the AccumulationBounds for
    that expression.

    The same expression can be evaluated to different values depending upon
    the form it is used for substitution since each instance of an
    AccumulationBounds is considered independent. For example:

    >>> (x**2 + 2*x + 1).subs(x, AccumBounds(-1, 1))
    AccumBounds(-1, 4)

    >>> ((x + 1)**2).subs(x, AccumBounds(-1, 1))
    AccumBounds(0, 4)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Interval_arithmetic

    .. [2] https://fab.cba.mit.edu/classes/S62.12/docs/Hickey_interval.pdf

    Notes
    =====

    Do not use ``AccumulationBounds`` for floating point interval arithmetic
    calculations, use ``mpmath.iv`` instead.
    """
    is_extended_real: bool
    is_number: bool
    def __new__(cls, min, max): ...
    @property
    def min(self):
        """
        Returns the minimum possible value attained by AccumulationBounds
        object.

        Examples
        ========

        >>> from sympy import AccumBounds
        >>> AccumBounds(1, 3).min
        1

        """
    @property
    def max(self):
        """
        Returns the maximum possible value attained by AccumulationBounds
        object.

        Examples
        ========

        >>> from sympy import AccumBounds
        >>> AccumBounds(1, 3).max
        3

        """
    @property
    def delta(self):
        """
        Returns the difference of maximum possible value attained by
        AccumulationBounds object and minimum possible value attained
        by AccumulationBounds object.

        Examples
        ========

        >>> from sympy import AccumBounds
        >>> AccumBounds(1, 3).delta
        2

        """
    @property
    def mid(self):
        """
        Returns the mean of maximum possible value attained by
        AccumulationBounds object and minimum possible value
        attained by AccumulationBounds object.

        Examples
        ========

        >>> from sympy import AccumBounds
        >>> AccumBounds(1, 3).mid
        2

        """
    def __add__(self, other): ...
    __radd__ = __add__
    def __neg__(self): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __pow__(self, other): ...
    def __rpow__(self, other): ...
    def __abs__(self): ...
    def __contains__(self, other) -> bool:
        """
        Returns ``True`` if other is contained in self, where other
        belongs to extended real numbers, ``False`` if not contained,
        otherwise TypeError is raised.

        Examples
        ========

        >>> from sympy import AccumBounds, oo
        >>> 1 in AccumBounds(-1, 3)
        True

        -oo and oo go together as limits (in AccumulationBounds).

        >>> -oo in AccumBounds(1, oo)
        True

        >>> oo in AccumBounds(-oo, 0)
        True

        """
    def intersection(self, other):
        """
        Returns the intersection of 'self' and 'other'.
        Here other can be an instance of :py:class:`~.FiniteSet` or AccumulationBounds.

        Parameters
        ==========

        other : AccumulationBounds
            Another AccumulationBounds object with which the intersection
            has to be computed.

        Returns
        =======

        AccumulationBounds
            Intersection of ``self`` and ``other``.

        Examples
        ========

        >>> from sympy import AccumBounds, FiniteSet
        >>> AccumBounds(1, 3).intersection(AccumBounds(2, 4))
        AccumBounds(2, 3)

        >>> AccumBounds(1, 3).intersection(AccumBounds(4, 6))
        EmptySet

        >>> AccumBounds(1, 4).intersection(FiniteSet(1, 2, 5))
        {1, 2}

        """
    def union(self, other): ...
AccumBounds = AccumulationBounds
