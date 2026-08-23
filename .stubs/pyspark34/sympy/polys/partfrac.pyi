from _typeshed import Incomplete
from sympy.core import Add as Add, Dummy as Dummy, Function as Function, Lambda as Lambda, S as S, sympify as sympify
from sympy.core.traversal import preorder_traversal as preorder_traversal
from sympy.polys import Poly as Poly, RootSum as RootSum, cancel as cancel, factor as factor
from sympy.polys.polyerrors import PolynomialError as PolynomialError
from sympy.polys.polyoptions import allowed_flags as allowed_flags, set_defaults as set_defaults
from sympy.polys.polytools import parallel_poly_from_expr as parallel_poly_from_expr
from sympy.utilities import numbered_symbols as numbered_symbols, public as public, take as take, xthreaded as xthreaded

def apart(f, x: Incomplete | None = None, full: bool = False, **options):
    """
    Compute partial fraction decomposition of a rational function.

    Given a rational function ``f``, computes the partial fraction
    decomposition of ``f``. Two algorithms are available: One is based on the
    undertermined coefficients method, the other is Bronstein's full partial
    fraction decomposition algorithm.

    The undetermined coefficients method (selected by ``full=False``) uses
    polynomial factorization (and therefore accepts the same options as
    factor) for the denominator. Per default it works over the rational
    numbers, therefore decomposition of denominators with non-rational roots
    (e.g. irrational, complex roots) is not supported by default (see options
    of factor).

    Bronstein's algorithm can be selected by using ``full=True`` and allows a
    decomposition of denominators with non-rational roots. A human-readable
    result can be obtained via ``doit()`` (see examples below).

    Examples
    ========

    >>> from sympy.polys.partfrac import apart
    >>> from sympy.abc import x, y

    By default, using the undetermined coefficients method:

    >>> apart(y/(x + 2)/(x + 1), x)
    -y/(x + 2) + y/(x + 1)

    The undetermined coefficients method does not provide a result when the
    denominators roots are not rational:

    >>> apart(y/(x**2 + x + 1), x)
    y/(x**2 + x + 1)

    You can choose Bronstein's algorithm by setting ``full=True``:

    >>> apart(y/(x**2 + x + 1), x, full=True)
    RootSum(_w**2 + _w + 1, Lambda(_a, (-2*_a*y/3 - y/3)/(-_a + x)))

    Calling ``doit()`` yields a human-readable result:

    >>> apart(y/(x**2 + x + 1), x, full=True).doit()
    (-y/3 - 2*y*(-1/2 - sqrt(3)*I/2)/3)/(x + 1/2 + sqrt(3)*I/2) + (-y/3 -
        2*y*(-1/2 + sqrt(3)*I/2)/3)/(x + 1/2 - sqrt(3)*I/2)


    See Also
    ========

    apart_list, assemble_partfrac_list
    """
def apart_undetermined_coeffs(P, Q):
    """Partial fractions via method of undetermined coefficients. """
def apart_full_decomposition(P, Q):
    """
    Bronstein's full partial fraction decomposition algorithm.

    Given a univariate rational function ``f``, performing only GCD
    operations over the algebraic closure of the initial ground domain
    of definition, compute full partial fraction decomposition with
    fractions having linear denominators.

    Note that no factorization of the initial denominator of ``f`` is
    performed. The final decomposition is formed in terms of a sum of
    :class:`RootSum` instances.

    References
    ==========

    .. [1] [Bronstein93]_

    """
def apart_list(f, x: Incomplete | None = None, dummies: Incomplete | None = None, **options):
    """
    Compute partial fraction decomposition of a rational function
    and return the result in structured form.

    Given a rational function ``f`` compute the partial fraction decomposition
    of ``f``. Only Bronstein's full partial fraction decomposition algorithm
    is supported by this method. The return value is highly structured and
    perfectly suited for further algorithmic treatment rather than being
    human-readable. The function returns a tuple holding three elements:

    * The first item is the common coefficient, free of the variable `x` used
      for decomposition. (It is an element of the base field `K`.)

    * The second item is the polynomial part of the decomposition. This can be
      the zero polynomial. (It is an element of `K[x]`.)

    * The third part itself is a list of quadruples. Each quadruple
      has the following elements in this order:

      - The (not necessarily irreducible) polynomial `D` whose roots `w_i` appear
        in the linear denominator of a bunch of related fraction terms. (This item
        can also be a list of explicit roots. However, at the moment ``apart_list``
        never returns a result this way, but the related ``assemble_partfrac_list``
        function accepts this format as input.)

      - The numerator of the fraction, written as a function of the root `w`

      - The linear denominator of the fraction *excluding its power exponent*,
        written as a function of the root `w`.

      - The power to which the denominator has to be raised.

    On can always rebuild a plain expression by using the function ``assemble_partfrac_list``.

    Examples
    ========

    A first example:

    >>> from sympy.polys.partfrac import apart_list, assemble_partfrac_list
    >>> from sympy.abc import x, t

    >>> f = (2*x**3 - 2*x) / (x**2 - 2*x + 1)
    >>> pfd = apart_list(f)
    >>> pfd
    (1,
    Poly(2*x + 4, x, domain='ZZ'),
    [(Poly(_w - 1, _w, domain='ZZ'), Lambda(_a, 4), Lambda(_a, -_a + x), 1)])

    >>> assemble_partfrac_list(pfd)
    2*x + 4 + 4/(x - 1)

    Second example:

    >>> f = (-2*x - 2*x**2) / (3*x**2 - 6*x)
    >>> pfd = apart_list(f)
    >>> pfd
    (-1,
    Poly(2/3, x, domain='QQ'),
    [(Poly(_w - 2, _w, domain='ZZ'), Lambda(_a, 2), Lambda(_a, -_a + x), 1)])

    >>> assemble_partfrac_list(pfd)
    -2/3 - 2/(x - 2)

    Another example, showing symbolic parameters:

    >>> pfd = apart_list(t/(x**2 + x + t), x)
    >>> pfd
    (1,
    Poly(0, x, domain='ZZ[t]'),
    [(Poly(_w**2 + _w + t, _w, domain='ZZ[t]'),
    Lambda(_a, -2*_a*t/(4*t - 1) - t/(4*t - 1)),
    Lambda(_a, -_a + x),
    1)])

    >>> assemble_partfrac_list(pfd)
    RootSum(_w**2 + _w + t, Lambda(_a, (-2*_a*t/(4*t - 1) - t/(4*t - 1))/(-_a + x)))

    This example is taken from Bronstein's original paper:

    >>> f = 36 / (x**5 - 2*x**4 - 2*x**3 + 4*x**2 + x - 2)
    >>> pfd = apart_list(f)
    >>> pfd
    (1,
    Poly(0, x, domain='ZZ'),
    [(Poly(_w - 2, _w, domain='ZZ'), Lambda(_a, 4), Lambda(_a, -_a + x), 1),
    (Poly(_w**2 - 1, _w, domain='ZZ'), Lambda(_a, -3*_a - 6), Lambda(_a, -_a + x), 2),
    (Poly(_w + 1, _w, domain='ZZ'), Lambda(_a, -4), Lambda(_a, -_a + x), 1)])

    >>> assemble_partfrac_list(pfd)
    -4/(x + 1) - 3/(x + 1)**2 - 9/(x - 1)**2 + 4/(x - 2)

    See also
    ========

    apart, assemble_partfrac_list

    References
    ==========

    .. [1] [Bronstein93]_

    """
def apart_list_full_decomposition(P, Q, dummygen):
    """
    Bronstein's full partial fraction decomposition algorithm.

    Given a univariate rational function ``f``, performing only GCD
    operations over the algebraic closure of the initial ground domain
    of definition, compute full partial fraction decomposition with
    fractions having linear denominators.

    Note that no factorization of the initial denominator of ``f`` is
    performed. The final decomposition is formed in terms of a sum of
    :class:`RootSum` instances.

    References
    ==========

    .. [1] [Bronstein93]_

    """
def assemble_partfrac_list(partial_list):
    '''Reassemble a full partial fraction decomposition
    from a structured result obtained by the function ``apart_list``.

    Examples
    ========

    This example is taken from Bronstein\'s original paper:

    >>> from sympy.polys.partfrac import apart_list, assemble_partfrac_list
    >>> from sympy.abc import x

    >>> f = 36 / (x**5 - 2*x**4 - 2*x**3 + 4*x**2 + x - 2)
    >>> pfd = apart_list(f)
    >>> pfd
    (1,
    Poly(0, x, domain=\'ZZ\'),
    [(Poly(_w - 2, _w, domain=\'ZZ\'), Lambda(_a, 4), Lambda(_a, -_a + x), 1),
    (Poly(_w**2 - 1, _w, domain=\'ZZ\'), Lambda(_a, -3*_a - 6), Lambda(_a, -_a + x), 2),
    (Poly(_w + 1, _w, domain=\'ZZ\'), Lambda(_a, -4), Lambda(_a, -_a + x), 1)])

    >>> assemble_partfrac_list(pfd)
    -4/(x + 1) - 3/(x + 1)**2 - 9/(x - 1)**2 + 4/(x - 2)

    If we happen to know some roots we can provide them easily inside the structure:

    >>> pfd = apart_list(2/(x**2-2))
    >>> pfd
    (1,
    Poly(0, x, domain=\'ZZ\'),
    [(Poly(_w**2 - 2, _w, domain=\'ZZ\'),
    Lambda(_a, _a/2),
    Lambda(_a, -_a + x),
    1)])

    >>> pfda = assemble_partfrac_list(pfd)
    >>> pfda
    RootSum(_w**2 - 2, Lambda(_a, _a/(-_a + x)))/2

    >>> pfda.doit()
    -sqrt(2)/(2*(x + sqrt(2))) + sqrt(2)/(2*(x - sqrt(2)))

    >>> from sympy import Dummy, Poly, Lambda, sqrt
    >>> a = Dummy("a")
    >>> pfd = (1, Poly(0, x, domain=\'ZZ\'), [([sqrt(2),-sqrt(2)], Lambda(a, a/2), Lambda(a, -a + x), 1)])

    >>> assemble_partfrac_list(pfd)
    -sqrt(2)/(2*(x + sqrt(2))) + sqrt(2)/(2*(x - sqrt(2)))

    See Also
    ========

    apart, apart_list
    '''
