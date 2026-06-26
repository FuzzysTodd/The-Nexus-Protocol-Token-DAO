from _typeshed import Incomplete
from sympy.core import Pow as Pow, S as S
from sympy.core.function import AppliedUndef as AppliedUndef, Derivative as Derivative, diff as diff
from sympy.core.relational import Eq as Eq, Equality as Equality
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions import exp as exp
from sympy.logic.boolalg import BooleanAtom as BooleanAtom
from sympy.series import Order as Order
from sympy.simplify.simplify import besselsimp as besselsimp, posify as posify, simplify as simplify
from sympy.simplify.sqrtdenest import sqrtdenest as sqrtdenest
from sympy.simplify.trigsimp import trigsimp as trigsimp
from sympy.solvers import solve as solve
from sympy.solvers.deutils import ode_order as ode_order
from sympy.utilities.iterables import is_sequence as is_sequence, iterable as iterable

def sub_func_doit(eq, func, new):
    """
    When replacing the func with something else, we usually want the
    derivative evaluated, so this function helps in making that happen.

    Examples
    ========

    >>> from sympy import Derivative, symbols, Function
    >>> from sympy.solvers.ode.subscheck import sub_func_doit
    >>> x, z = symbols('x, z')
    >>> y = Function('y')

    >>> sub_func_doit(3*Derivative(y(x), x) - 1, y(x), x)
    2

    >>> sub_func_doit(x*Derivative(y(x), x) - y(x)**2 + y(x), y(x),
    ... 1/(x*(z + 1/x)))
    x*(-1/(x**2*(z + 1/x)) + 1/(x**3*(z + 1/x)**2)) + 1/(x*(z + 1/x))
    ...- 1/(x**2*(z + 1/x)**2)
    """
def checkodesol(ode, sol, func: Incomplete | None = None, order: str = 'auto', solve_for_func: bool = True):
    """
    Substitutes ``sol`` into ``ode`` and checks that the result is ``0``.

    This works when ``func`` is one function, like `f(x)` or a list of
    functions like `[f(x), g(x)]` when `ode` is a system of ODEs.  ``sol`` can
    be a single solution or a list of solutions.  Each solution may be an
    :py:class:`~sympy.core.relational.Equality` that the solution satisfies,
    e.g. ``Eq(f(x), C1), Eq(f(x) + C1, 0)``; or simply an
    :py:class:`~sympy.core.expr.Expr`, e.g. ``f(x) - C1``. In most cases it
    will not be necessary to explicitly identify the function, but if the
    function cannot be inferred from the original equation it can be supplied
    through the ``func`` argument.

    If a sequence of solutions is passed, the same sort of container will be
    used to return the result for each solution.

    It tries the following methods, in order, until it finds zero equivalence:

    1. Substitute the solution for `f` in the original equation.  This only
       works if ``ode`` is solved for `f`.  It will attempt to solve it first
       unless ``solve_for_func == False``.
    2. Take `n` derivatives of the solution, where `n` is the order of
       ``ode``, and check to see if that is equal to the solution.  This only
       works on exact ODEs.
    3. Take the 1st, 2nd, ..., `n`\\th derivatives of the solution, each time
       solving for the derivative of `f` of that order (this will always be
       possible because `f` is a linear operator). Then back substitute each
       derivative into ``ode`` in reverse order.

    This function returns a tuple.  The first item in the tuple is ``True`` if
    the substitution results in ``0``, and ``False`` otherwise. The second
    item in the tuple is what the substitution results in.  It should always
    be ``0`` if the first item is ``True``. Sometimes this function will
    return ``False`` even when an expression is identically equal to ``0``.
    This happens when :py:meth:`~sympy.simplify.simplify.simplify` does not
    reduce the expression to ``0``.  If an expression returned by this
    function vanishes identically, then ``sol`` really is a solution to
    the ``ode``.

    If this function seems to hang, it is probably because of a hard
    simplification.

    To use this function to test, test the first item of the tuple.

    Examples
    ========

    >>> from sympy import (Eq, Function, checkodesol, symbols,
    ...     Derivative, exp)
    >>> x, C1, C2 = symbols('x,C1,C2')
    >>> f, g = symbols('f g', cls=Function)
    >>> checkodesol(f(x).diff(x), Eq(f(x), C1))
    (True, 0)
    >>> assert checkodesol(f(x).diff(x), C1)[0]
    >>> assert not checkodesol(f(x).diff(x), x)[0]
    >>> checkodesol(f(x).diff(x, 2), x**2)
    (False, 2)

    >>> eqs = [Eq(Derivative(f(x), x), f(x)), Eq(Derivative(g(x), x), g(x))]
    >>> sol = [Eq(f(x), C1*exp(x)), Eq(g(x), C2*exp(x))]
    >>> checkodesol(eqs, sol)
    (True, [0, 0])

    """
def checksysodesol(eqs, sols, func: Incomplete | None = None):
    """
    Substitutes corresponding ``sols`` for each functions into each ``eqs`` and
    checks that the result of substitutions for each equation is ``0``. The
    equations and solutions passed can be any iterable.

    This only works when each ``sols`` have one function only, like `x(t)` or `y(t)`.
    For each function, ``sols`` can have a single solution or a list of solutions.
    In most cases it will not be necessary to explicitly identify the function,
    but if the function cannot be inferred from the original equation it
    can be supplied through the ``func`` argument.

    When a sequence of equations is passed, the same sequence is used to return
    the result for each equation with each function substituted with corresponding
    solutions.

    It tries the following method to find zero equivalence for each equation:

    Substitute the solutions for functions, like `x(t)` and `y(t)` into the
    original equations containing those functions.
    This function returns a tuple.  The first item in the tuple is ``True`` if
    the substitution results for each equation is ``0``, and ``False`` otherwise.
    The second item in the tuple is what the substitution results in.  Each element
    of the ``list`` should always be ``0`` corresponding to each equation if the
    first item is ``True``. Note that sometimes this function may return ``False``,
    but with an expression that is identically equal to ``0``, instead of returning
    ``True``.  This is because :py:meth:`~sympy.simplify.simplify.simplify` cannot
    reduce the expression to ``0``.  If an expression returned by each function
    vanishes identically, then ``sols`` really is a solution to ``eqs``.

    If this function seems to hang, it is probably because of a difficult simplification.

    Examples
    ========

    >>> from sympy import Eq, diff, symbols, sin, cos, exp, sqrt, S, Function
    >>> from sympy.solvers.ode.subscheck import checksysodesol
    >>> C1, C2 = symbols('C1:3')
    >>> t = symbols('t')
    >>> x, y = symbols('x, y', cls=Function)
    >>> eq = (Eq(diff(x(t),t), x(t) + y(t) + 17), Eq(diff(y(t),t), -2*x(t) + y(t) + 12))
    >>> sol = [Eq(x(t), (C1*sin(sqrt(2)*t) + C2*cos(sqrt(2)*t))*exp(t) - S(5)/3),
    ... Eq(y(t), (sqrt(2)*C1*cos(sqrt(2)*t) - sqrt(2)*C2*sin(sqrt(2)*t))*exp(t) - S(46)/3)]
    >>> checksysodesol(eq, sol)
    (True, [0, 0])
    >>> eq = (Eq(diff(x(t),t),x(t)*y(t)**4), Eq(diff(y(t),t),y(t)**3))
    >>> sol = [Eq(x(t), C1*exp(-1/(4*(C2 + t)))), Eq(y(t), -sqrt(2)*sqrt(-1/(C2 + t))/2),
    ... Eq(x(t), C1*exp(-1/(4*(C2 + t)))), Eq(y(t), sqrt(2)*sqrt(-1/(C2 + t))/2)]
    >>> checksysodesol(eq, sol)
    (True, [0, 0])

    """
