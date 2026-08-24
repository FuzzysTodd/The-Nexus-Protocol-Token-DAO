from .accumulationbounds import AccumBounds as AccumBounds, AccumulationBounds as AccumulationBounds
from .singularities import singularities as singularities
from sympy.core import Pow as Pow, S as S
from sympy.core.function import diff as diff, expand_mul as expand_mul
from sympy.core.kind import NumberKind as NumberKind
from sympy.core.mod import Mod as Mod
from sympy.core.numbers import equal_valued as equal_valued
from sympy.core.relational import Relational as Relational
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.functions.elementary.complexes import Abs as Abs, im as im, re as re
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.elementary.trigonometric import TrigonometricFunction as TrigonometricFunction, cos as cos, csc as csc, sec as sec, sin as sin
from sympy.polys.polytools import degree as degree, lcm_list as lcm_list
from sympy.sets.fancysets import ImageSet as ImageSet
from sympy.sets.sets import Complement as Complement, FiniteSet as FiniteSet, Intersection as Intersection, Interval as Interval, Union as Union
from sympy.utilities import filldedent as filldedent
from sympy.utilities.iterables import iterable as iterable

def continuous_domain(f, symbol, domain):
    """
    Returns the intervals in the given domain for which the function
    is continuous.
    This method is limited by the ability to determine the various
    singularities and discontinuities of the given function.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    symbol : :py:class:`~.Symbol`
        The variable for which the intervals are to be determined.
    domain : :py:class:`~.Interval`
        The domain over which the continuity of the symbol has to be checked.

    Examples
    ========

    >>> from sympy import Interval, Symbol, S, tan, log, pi, sqrt
    >>> from sympy.calculus.util import continuous_domain
    >>> x = Symbol('x')
    >>> continuous_domain(1/x, x, S.Reals)
    Union(Interval.open(-oo, 0), Interval.open(0, oo))
    >>> continuous_domain(tan(x), x, Interval(0, pi))
    Union(Interval.Ropen(0, pi/2), Interval.Lopen(pi/2, pi))
    >>> continuous_domain(sqrt(x - 2), x, Interval(-5, 5))
    Interval(2, 5)
    >>> continuous_domain(log(2*x - 1), x, S.Reals)
    Interval.open(1/2, oo)

    Returns
    =======

    :py:class:`~.Interval`
        Union of all intervals where the function is continuous.

    Raises
    ======

    NotImplementedError
        If the method to determine continuity of such a function
        has not yet been developed.

    """
def function_range(f, symbol, domain):
    """
    Finds the range of a function in a given domain.
    This method is limited by the ability to determine the singularities and
    determine limits.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    symbol : :py:class:`~.Symbol`
        The variable for which the range of function is to be determined.
    domain : :py:class:`~.Interval`
        The domain under which the range of the function has to be found.

    Examples
    ========

    >>> from sympy import Interval, Symbol, S, exp, log, pi, sqrt, sin, tan
    >>> from sympy.calculus.util import function_range
    >>> x = Symbol('x')
    >>> function_range(sin(x), x, Interval(0, 2*pi))
    Interval(-1, 1)
    >>> function_range(tan(x), x, Interval(-pi/2, pi/2))
    Interval(-oo, oo)
    >>> function_range(1/x, x, S.Reals)
    Union(Interval.open(-oo, 0), Interval.open(0, oo))
    >>> function_range(exp(x), x, S.Reals)
    Interval.open(0, oo)
    >>> function_range(log(x), x, S.Reals)
    Interval(-oo, oo)
    >>> function_range(sqrt(x), x, Interval(-5, 9))
    Interval(0, 3)

    Returns
    =======

    :py:class:`~.Interval`
        Union of all ranges for all intervals under domain where function is
        continuous.

    Raises
    ======

    NotImplementedError
        If any of the intervals, in the given domain, for which function
        is continuous are not finite or real,
        OR if the critical points of the function on the domain cannot be found.
    """
def not_empty_in(finset_intersection, *syms):
    """
    Finds the domain of the functions in ``finset_intersection`` in which the
    ``finite_set`` is not-empty.

    Parameters
    ==========

    finset_intersection : Intersection of FiniteSet
        The unevaluated intersection of FiniteSet containing
        real-valued functions with Union of Sets
    syms : Tuple of symbols
        Symbol for which domain is to be found

    Raises
    ======

    NotImplementedError
        The algorithms to find the non-emptiness of the given FiniteSet are
        not yet implemented.
    ValueError
        The input is not valid.
    RuntimeError
        It is a bug, please report it to the github issue tracker
        (https://github.com/sympy/sympy/issues).

    Examples
    ========

    >>> from sympy import FiniteSet, Interval, not_empty_in, oo
    >>> from sympy.abc import x
    >>> not_empty_in(FiniteSet(x/2).intersect(Interval(0, 1)), x)
    Interval(0, 2)
    >>> not_empty_in(FiniteSet(x, x**2).intersect(Interval(1, 2)), x)
    Union(Interval(1, 2), Interval(-sqrt(2), -1))
    >>> not_empty_in(FiniteSet(x**2/(x + 2)).intersect(Interval(1, oo)), x)
    Union(Interval.Lopen(-2, -1), Interval(2, oo))
    """
def periodicity(f, symbol, check: bool = False):
    '''
    Tests the given function for periodicity in the given symbol.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    symbol : :py:class:`~.Symbol`
        The variable for which the period is to be determined.
    check : bool, optional
        The flag to verify whether the value being returned is a period or not.

    Returns
    =======

    period
        The period of the function is returned.
        ``None`` is returned when the function is aperiodic or has a complex period.
        The value of $0$ is returned as the period of a constant function.

    Raises
    ======

    NotImplementedError
        The value of the period computed cannot be verified.


    Notes
    =====

    Currently, we do not support functions with a complex period.
    The period of functions having complex periodic values such
    as ``exp``, ``sinh`` is evaluated to ``None``.

    The value returned might not be the "fundamental" period of the given
    function i.e. it may not be the smallest periodic value of the function.

    The verification of the period through the ``check`` flag is not reliable
    due to internal simplification of the given expression. Hence, it is set
    to ``False`` by default.

    Examples
    ========
    >>> from sympy import periodicity, Symbol, sin, cos, tan, exp
    >>> x = Symbol(\'x\')
    >>> f = sin(x) + sin(2*x) + sin(3*x)
    >>> periodicity(f, x)
    2*pi
    >>> periodicity(sin(x)*cos(x), x)
    pi
    >>> periodicity(exp(tan(2*x) - 1), x)
    pi/2
    >>> periodicity(sin(4*x)**cos(2*x), x)
    pi
    >>> periodicity(exp(x), x)
    '''
def lcim(numbers):
    """Returns the least common integral multiple of a list of numbers.

    The numbers can be rational or irrational or a mixture of both.
    `None` is returned for incommensurable numbers.

    Parameters
    ==========

    numbers : list
        Numbers (rational and/or irrational) for which lcim is to be found.

    Returns
    =======

    number
        lcim if it exists, otherwise ``None`` for incommensurable numbers.

    Examples
    ========

    >>> from sympy.calculus.util import lcim
    >>> from sympy import S, pi
    >>> lcim([S(1)/2, S(3)/4, S(5)/6])
    15/2
    >>> lcim([2*pi, 3*pi, pi, pi/2])
    6*pi
    >>> lcim([S(1), 2*pi])
    """
def is_convex(f, *syms, domain=...):
    """Determines the  convexity of the function passed in the argument.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    syms : Tuple of :py:class:`~.Symbol`
        The variables with respect to which the convexity is to be determined.
    domain : :py:class:`~.Interval`, optional
        The domain over which the convexity of the function has to be checked.
        If unspecified, S.Reals will be the default domain.

    Returns
    =======

    bool
        The method returns ``True`` if the function is convex otherwise it
        returns ``False``.

    Raises
    ======

    NotImplementedError
        The check for the convexity of multivariate functions is not implemented yet.

    Notes
    =====

    To determine concavity of a function pass `-f` as the concerned function.
    To determine logarithmic convexity of a function pass `\\log(f)` as
    concerned function.
    To determine logarithmic concavity of a function pass `-\\log(f)` as
    concerned function.

    Currently, convexity check of multivariate functions is not handled.

    Examples
    ========

    >>> from sympy import is_convex, symbols, exp, oo, Interval
    >>> x = symbols('x')
    >>> is_convex(exp(x), x)
    True
    >>> is_convex(x**3, x, domain = Interval(-1, oo))
    False
    >>> is_convex(1/x**2, x, domain=Interval.open(0, oo))
    True

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Convex_function
    .. [2] http://www.ifp.illinois.edu/~angelia/L3_convfunc.pdf
    .. [3] https://en.wikipedia.org/wiki/Logarithmically_convex_function
    .. [4] https://en.wikipedia.org/wiki/Logarithmically_concave_function
    .. [5] https://en.wikipedia.org/wiki/Concave_function

    """
def stationary_points(f, symbol, domain=...):
    """
    Returns the stationary points of a function (where derivative of the
    function is 0) in the given domain.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    symbol : :py:class:`~.Symbol`
        The variable for which the stationary points are to be determined.
    domain : :py:class:`~.Interval`
        The domain over which the stationary points have to be checked.
        If unspecified, ``S.Reals`` will be the default domain.

    Returns
    =======

    Set
        A set of stationary points for the function. If there are no
        stationary point, an :py:class:`~.EmptySet` is returned.

    Examples
    ========

    >>> from sympy import Interval, Symbol, S, sin, pi, pprint, stationary_points
    >>> x = Symbol('x')

    >>> stationary_points(1/x, x, S.Reals)
    EmptySet

    >>> pprint(stationary_points(sin(x), x), use_unicode=False)
              pi                              3*pi
    {2*n*pi + -- | n in Integers} U {2*n*pi + ---- | n in Integers}
              2                                2

    >>> stationary_points(sin(x),x, Interval(0, 4*pi))
    {pi/2, 3*pi/2, 5*pi/2, 7*pi/2}

    """
def maximum(f, symbol, domain=...):
    """
    Returns the maximum value of a function in the given domain.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    symbol : :py:class:`~.Symbol`
        The variable for maximum value needs to be determined.
    domain : :py:class:`~.Interval`
        The domain over which the maximum have to be checked.
        If unspecified, then the global maximum is returned.

    Returns
    =======

    number
        Maximum value of the function in given domain.

    Examples
    ========

    >>> from sympy import Interval, Symbol, S, sin, cos, pi, maximum
    >>> x = Symbol('x')

    >>> f = -x**2 + 2*x + 5
    >>> maximum(f, x, S.Reals)
    6

    >>> maximum(sin(x), x, Interval(-pi, pi/4))
    sqrt(2)/2

    >>> maximum(sin(x)*cos(x), x)
    1/2

    """
def minimum(f, symbol, domain=...):
    """
    Returns the minimum value of a function in the given domain.

    Parameters
    ==========

    f : :py:class:`~.Expr`
        The concerned function.
    symbol : :py:class:`~.Symbol`
        The variable for minimum value needs to be determined.
    domain : :py:class:`~.Interval`
        The domain over which the minimum have to be checked.
        If unspecified, then the global minimum is returned.

    Returns
    =======

    number
        Minimum value of the function in the given domain.

    Examples
    ========

    >>> from sympy import Interval, Symbol, S, sin, cos, minimum
    >>> x = Symbol('x')

    >>> f = x**2 + 2*x + 5
    >>> minimum(f, x, S.Reals)
    4

    >>> minimum(sin(x), x, Interval(2, 3))
    sin(3)

    >>> minimum(sin(x)*cos(x), x)
    -1/2

    """
