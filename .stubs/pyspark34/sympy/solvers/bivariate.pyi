from sympy.core.add import Add as Add
from sympy.core.exprtools import factor_terms as factor_terms
from sympy.core.function import expand_log as expand_log
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.sorting import ordered as ordered
from sympy.core.symbol import Dummy as Dummy
from sympy.functions.elementary.exponential import LambertW as LambertW, exp as exp, log as log
from sympy.functions.elementary.miscellaneous import root as root
from sympy.polys.polyroots import roots as roots
from sympy.polys.polytools import Poly as Poly, factor as factor
from sympy.simplify.radsimp import collect as collect
from sympy.simplify.simplify import powsimp as powsimp, separatevars as separatevars
from sympy.solvers.solvers import solve as solve
from sympy.utilities.iterables import uniq as uniq

def bivariate_type(f, x, y, *, first: bool = True):
    """Given an expression, f, 3 tests will be done to see what type
    of composite bivariate it might be, options for u(x, y) are::

        x*y
        x+y
        x*y+x
        x*y+y

    If it matches one of these types, ``u(x, y)``, ``P(u)`` and dummy
    variable ``u`` will be returned. Solving ``P(u)`` for ``u`` and
    equating the solutions to ``u(x, y)`` and then solving for ``x`` or
    ``y`` is equivalent to solving the original expression for ``x`` or
    ``y``. If ``x`` and ``y`` represent two functions in the same
    variable, e.g. ``x = g(t)`` and ``y = h(t)``, then if ``u(x, y) - p``
    can be solved for ``t`` then these represent the solutions to
    ``P(u) = 0`` when ``p`` are the solutions of ``P(u) = 0``.

    Only positive values of ``u`` are considered.

    Examples
    ========

    >>> from sympy import solve
    >>> from sympy.solvers.bivariate import bivariate_type
    >>> from sympy.abc import x, y
    >>> eq = (x**2 - 3).subs(x, x + y)
    >>> bivariate_type(eq, x, y)
    (x + y, _u**2 - 3, _u)
    >>> uxy, pu, u = _
    >>> usol = solve(pu, u); usol
    [sqrt(3)]
    >>> [solve(uxy - s) for s in solve(pu, u)]
    [[{x: -y + sqrt(3)}]]
    >>> all(eq.subs(s).equals(0) for sol in _ for s in sol)
    True

    """
