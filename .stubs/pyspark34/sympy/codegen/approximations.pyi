from _typeshed import Incomplete
from sympy.calculus.singularities import is_decreasing as is_decreasing, is_increasing as is_increasing
from sympy.codegen.rewriting import Optimization as Optimization
from sympy.core.function import UndefinedFunction as UndefinedFunction
from sympy.sets.sets import Interval as Interval

class SumApprox(Optimization):
    """
    Approximates sum by neglecting small terms.

    Explanation
    ===========

    If terms are expressions which can be determined to be monotonic, then
    bounds for those expressions are added.

    Parameters
    ==========

    bounds : dict
        Mapping expressions to length 2 tuple of bounds (low, high).
    reltol : number
        Threshold for when to ignore a term. Taken relative to the largest
        lower bound among bounds.

    Examples
    ========

    >>> from sympy import exp
    >>> from sympy.abc import x, y, z
    >>> from sympy.codegen.rewriting import optimize
    >>> from sympy.codegen.approximations import SumApprox
    >>> bounds = {x: (-1, 1), y: (1000, 2000), z: (-10, 3)}
    >>> sum_approx3 = SumApprox(bounds, reltol=1e-3)
    >>> sum_approx2 = SumApprox(bounds, reltol=1e-2)
    >>> sum_approx1 = SumApprox(bounds, reltol=1e-1)
    >>> expr = 3*(x + y + exp(z))
    >>> optimize(expr, [sum_approx3])
    3*(x + y + exp(z))
    >>> optimize(expr, [sum_approx2])
    3*y + 3*exp(z)
    >>> optimize(expr, [sum_approx1])
    3*y

    """
    bounds: Incomplete
    reltol: Incomplete
    def __init__(self, bounds, reltol, **kwargs) -> None: ...
    def __call__(self, expr): ...
    def query(self, expr): ...
    def value(self, add): ...

class SeriesApprox(Optimization):
    """ Approximates functions by expanding them as a series.

    Parameters
    ==========

    bounds : dict
        Mapping expressions to length 2 tuple of bounds (low, high).
    reltol : number
        Threshold for when to ignore a term. Taken relative to the largest
        lower bound among bounds.
    max_order : int
        Largest order to include in series expansion
    n_point_checks : int (even)
        The validity of an expansion (with respect to reltol) is checked at
        discrete points (linearly spaced over the bounds of the variable). The
        number of points used in this numerical check is given by this number.

    Examples
    ========

    >>> from sympy import sin, pi
    >>> from sympy.abc import x, y
    >>> from sympy.codegen.rewriting import optimize
    >>> from sympy.codegen.approximations import SeriesApprox
    >>> bounds = {x: (-.1, .1), y: (pi-1, pi+1)}
    >>> series_approx2 = SeriesApprox(bounds, reltol=1e-2)
    >>> series_approx3 = SeriesApprox(bounds, reltol=1e-3)
    >>> series_approx8 = SeriesApprox(bounds, reltol=1e-8)
    >>> expr = sin(x)*sin(y)
    >>> optimize(expr, [series_approx2])
    x*(-y + (y - pi)**3/6 + pi)
    >>> optimize(expr, [series_approx3])
    (-x**3/6 + x)*sin(y)
    >>> optimize(expr, [series_approx8])
    sin(x)*sin(y)

    """
    bounds: Incomplete
    reltol: Incomplete
    max_order: Incomplete
    n_point_checks: Incomplete
    def __init__(self, bounds, reltol, max_order: int = 4, n_point_checks: int = 4, **kwargs) -> None: ...
    def __call__(self, expr): ...
    def query(self, expr): ...
    def value(self, fexpr): ...
