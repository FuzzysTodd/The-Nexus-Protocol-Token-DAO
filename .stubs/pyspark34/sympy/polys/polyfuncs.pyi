from _typeshed import Incomplete
from sympy.core import Basic as Basic, Dummy as Dummy, S as S, symbols as symbols
from sympy.polys.polyerrors import ComputationFailed as ComputationFailed, MultivariatePolynomialError as MultivariatePolynomialError, OptionError as OptionError, PolificationFailed as PolificationFailed
from sympy.polys.polyoptions import allowed_flags as allowed_flags, build_options as build_options
from sympy.polys.polytools import Poly as Poly, poly_from_expr as poly_from_expr
from sympy.polys.rings import sring as sring
from sympy.polys.specialpolys import interpolating_poly as interpolating_poly, symmetric_poly as symmetric_poly
from sympy.utilities import numbered_symbols as numbered_symbols, public as public, take as take

def symmetrize(F, *gens, **args):
    """
    Rewrite a polynomial in terms of elementary symmetric polynomials.

    A symmetric polynomial is a multivariate polynomial that remains invariant
    under any variable permutation, i.e., if `f = f(x_1, x_2, \\dots, x_n)`,
    then `f = f(x_{i_1}, x_{i_2}, \\dots, x_{i_n})`, where
    `(i_1, i_2, \\dots, i_n)` is a permutation of `(1, 2, \\dots, n)` (an
    element of the group `S_n`).

    Returns a tuple of symmetric polynomials ``(f1, f2, ..., fn)`` such that
    ``f = f1 + f2 + ... + fn``.

    Examples
    ========

    >>> from sympy.polys.polyfuncs import symmetrize
    >>> from sympy.abc import x, y

    >>> symmetrize(x**2 + y**2)
    (-2*x*y + (x + y)**2, 0)

    >>> symmetrize(x**2 + y**2, formal=True)
    (s1**2 - 2*s2, 0, [(s1, x + y), (s2, x*y)])

    >>> symmetrize(x**2 - y**2)
    (-2*x*y + (x + y)**2, -2*y**2)

    >>> symmetrize(x**2 - y**2, formal=True)
    (s1**2 - 2*s2, -2*y**2, [(s1, x + y), (s2, x*y)])

    """
def horner(f, *gens, **args):
    """
    Rewrite a polynomial in Horner form.

    Among other applications, evaluation of a polynomial at a point is optimal
    when it is applied using the Horner scheme ([1]).

    Examples
    ========

    >>> from sympy.polys.polyfuncs import horner
    >>> from sympy.abc import x, y, a, b, c, d, e

    >>> horner(9*x**4 + 8*x**3 + 7*x**2 + 6*x + 5)
    x*(x*(x*(9*x + 8) + 7) + 6) + 5

    >>> horner(a*x**4 + b*x**3 + c*x**2 + d*x + e)
    e + x*(d + x*(c + x*(a*x + b)))

    >>> f = 4*x**2*y**2 + 2*x**2*y + 2*x*y**2 + x*y

    >>> horner(f, wrt=x)
    x*(x*y*(4*y + 2) + y*(2*y + 1))

    >>> horner(f, wrt=y)
    y*(x*y*(4*x + 2) + x*(2*x + 1))

    References
    ==========
    [1] - https://en.wikipedia.org/wiki/Horner_scheme

    """
def interpolate(data, x):
    """
    Construct an interpolating polynomial for the data points
    evaluated at point x (which can be symbolic or numeric).

    Examples
    ========

    >>> from sympy.polys.polyfuncs import interpolate
    >>> from sympy.abc import a, b, x

    A list is interpreted as though it were paired with a range starting
    from 1:

    >>> interpolate([1, 4, 9, 16], x)
    x**2

    This can be made explicit by giving a list of coordinates:

    >>> interpolate([(1, 1), (2, 4), (3, 9)], x)
    x**2

    The (x, y) coordinates can also be given as keys and values of a
    dictionary (and the points need not be equispaced):

    >>> interpolate([(-1, 2), (1, 2), (2, 5)], x)
    x**2 + 1
    >>> interpolate({-1: 2, 1: 2, 2: 5}, x)
    x**2 + 1

    If the interpolation is going to be used only once then the
    value of interest can be passed instead of passing a symbol:

    >>> interpolate([1, 4, 9], 5)
    25

    Symbolic coordinates are also supported:

    >>> [(i,interpolate((a, b), i)) for i in range(1, 4)]
    [(1, a), (2, b), (3, -a + 2*b)]
    """
def rational_interpolate(data, degnum, X=...):
    '''
    Returns a rational interpolation, where the data points are element of
    any integral domain.

    The first argument  contains the data (as a list of coordinates). The
    ``degnum`` argument is the degree in the numerator of the rational
    function. Setting it too high will decrease the maximal degree in the
    denominator for the same amount of data.

    Examples
    ========

    >>> from sympy.polys.polyfuncs import rational_interpolate

    >>> data = [(1, -210), (2, -35), (3, 105), (4, 231), (5, 350), (6, 465)]
    >>> rational_interpolate(data, 2)
    (105*x**2 - 525)/(x + 1)

    Values do not need to be integers:

    >>> from sympy import sympify
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> y = sympify("[-1, 0, 2, 22/5, 7, 68/7]")
    >>> rational_interpolate(zip(x, y), 2)
    (3*x**2 - 7*x + 2)/(x + 1)

    The symbol for the variable can be changed if needed:
    >>> from sympy import symbols
    >>> z = symbols(\'z\')
    >>> rational_interpolate(data, 2, X=z)
    (105*z**2 - 525)/(z + 1)

    References
    ==========

    .. [1] Algorithm is adapted from:
           http://axiom-wiki.newsynthesis.org/RationalInterpolation

    '''
def viete(f, roots: Incomplete | None = None, *gens, **args):
    """
    Generate Viete's formulas for ``f``.

    Examples
    ========

    >>> from sympy.polys.polyfuncs import viete
    >>> from sympy import symbols

    >>> x, a, b, c, r1, r2 = symbols('x,a:c,r1:3')

    >>> viete(a*x**2 + b*x + c, [r1, r2], x)
    [(r1 + r2, -b/a), (r1*r2, c/a)]

    """
