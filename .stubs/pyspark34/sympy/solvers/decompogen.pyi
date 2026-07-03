from sympy.core import Expr as Expr, Function as Function, Pow as Pow, sympify as sympify
from sympy.core.relational import Relational as Relational
from sympy.core.singleton import S as S
from sympy.functions.elementary.miscellaneous import Max as Max, Min as Min
from sympy.polys import Poly as Poly, decompose as decompose
from sympy.utilities.misc import func_name as func_name

def decompogen(f, symbol):
    """
    Computes General functional decomposition of ``f``.
    Given an expression ``f``, returns a list ``[f_1, f_2, ..., f_n]``,
    where::
              f = f_1 o f_2 o ... f_n = f_1(f_2(... f_n))

    Note: This is a General decomposition function. It also decomposes
    Polynomials. For only Polynomial decomposition see ``decompose`` in polys.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy import decompogen, sqrt, sin, cos
    >>> decompogen(sin(cos(x)), x)
    [sin(x), cos(x)]
    >>> decompogen(sin(x)**2 + sin(x) + 1, x)
    [x**2 + x + 1, sin(x)]
    >>> decompogen(sqrt(6*x**2 - 5), x)
    [sqrt(x), 6*x**2 - 5]
    >>> decompogen(sin(sqrt(cos(x**2 + 1))), x)
    [sin(x), sqrt(x), cos(x), x**2 + 1]
    >>> decompogen(x**4 + 2*x**3 - x - 1, x)
    [x**2 - x - 1, x**2 + x]

    """
def compogen(g_s, symbol):
    """
    Returns the composition of functions.
    Given a list of functions ``g_s``, returns their composition ``f``,
    where:
        f = g_1 o g_2 o .. o g_n

    Note: This is a General composition function. It also composes Polynomials.
    For only Polynomial composition see ``compose`` in polys.

    Examples
    ========

    >>> from sympy.solvers.decompogen import compogen
    >>> from sympy.abc import x
    >>> from sympy import sqrt, sin, cos
    >>> compogen([sin(x), cos(x)], x)
    sin(cos(x))
    >>> compogen([x**2 + x + 1, sin(x)], x)
    sin(x)**2 + sin(x) + 1
    >>> compogen([sqrt(x), 6*x**2 - 5], x)
    sqrt(6*x**2 - 5)
    >>> compogen([sin(x), sqrt(x), cos(x), x**2 + 1], x)
    sin(sqrt(cos(x**2 + 1)))
    >>> compogen([x**2 - x - 1, x**2 + x], x)
    -x**2 - x + (x**2 + x)**2 - 1
    """
