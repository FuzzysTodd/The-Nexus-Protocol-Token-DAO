from sympy.core import Expr as Expr, Function as Function, PoleError as PoleError
from sympy.core.numbers import Rational as Rational, igcd as igcd
from sympy.functions import atan as atan, atanh as atanh, ceiling as ceiling, cos as cos, exp as exp, log as log, sin as sin, tan as tan, tanh as tanh
from sympy.polys.domains import EX as EX, QQ as QQ
from sympy.polys.monomials import monomial_div as monomial_div, monomial_ldiv as monomial_ldiv, monomial_min as monomial_min, monomial_mul as monomial_mul
from sympy.polys.polyerrors import DomainError as DomainError
from sympy.polys.rings import PolyElement as PolyElement, ring as ring, sring as sring
from sympy.utilities.misc import as_int as as_int

def rs_trunc(p1, x, prec):
    """
    Truncate the series in the ``x`` variable with precision ``prec``,
    that is, modulo ``O(x**prec)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_trunc
    >>> R, x = ring('x', QQ)
    >>> p = x**10 + x**5 + x + 1
    >>> rs_trunc(p, x, 12)
    x**10 + x**5 + x + 1
    >>> rs_trunc(p, x, 10)
    x**5 + x + 1
    """
def rs_is_puiseux(p, x):
    """
    Test if ``p`` is Puiseux series in ``x``.

    Raise an exception if it has a negative power in ``x``.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_is_puiseux
    >>> R, x = ring('x', QQ)
    >>> p = x**QQ(2,5) + x**QQ(2,3) + x
    >>> rs_is_puiseux(p, x)
    True
    """
def rs_puiseux(f, p, x, prec):
    """
    Return the puiseux series for `f(p, x, prec)`.

    To be used when function ``f`` is implemented only for regular series.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_puiseux, rs_exp
    >>> R, x = ring('x', QQ)
    >>> p = x**QQ(2,5) + x**QQ(2,3) + x
    >>> rs_puiseux(rs_exp,p, x, 1)
    1/2*x**(4/5) + x**(2/3) + x**(2/5) + 1
    """
def rs_puiseux2(f, p, q, x, prec):
    """
    Return the puiseux series for `f(p, q, x, prec)`.

    To be used when function ``f`` is implemented only for regular series.
    """
def rs_mul(p1, p2, x, prec):
    """
    Return the product of the given two series, modulo ``O(x**prec)``.

    ``x`` is the series variable or its position in the generators.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_mul
    >>> R, x = ring('x', QQ)
    >>> p1 = x**2 + 2*x + 1
    >>> p2 = x + 1
    >>> rs_mul(p1, p2, x, 3)
    3*x**2 + 3*x + 1
    """
def rs_square(p1, x, prec):
    """
    Square the series modulo ``O(x**prec)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_square
    >>> R, x = ring('x', QQ)
    >>> p = x**2 + 2*x + 1
    >>> rs_square(p, x, 3)
    6*x**2 + 4*x + 1
    """
def rs_pow(p1, n, x, prec):
    """
    Return ``p1**n`` modulo ``O(x**prec)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_pow
    >>> R, x = ring('x', QQ)
    >>> p = x + 1
    >>> rs_pow(p, 4, x, 3)
    6*x**2 + 4*x + 1
    """
def rs_subs(p, rules, x, prec):
    """
    Substitution with truncation according to the mapping in ``rules``.

    Return a series with precision ``prec`` in the generator ``x``

    Note that substitutions are not done one after the other

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_subs
    >>> R, x, y = ring('x, y', QQ)
    >>> p = x**2 + y**2
    >>> rs_subs(p, {x: x+ y, y: x+ 2*y}, x, 3)
    2*x**2 + 6*x*y + 5*y**2
    >>> (x + y)**2 + (x + 2*y)**2
    2*x**2 + 6*x*y + 5*y**2

    which differs from

    >>> rs_subs(rs_subs(p, {x: x+ y}, x, 3), {y: x+ 2*y}, x, 3)
    5*x**2 + 12*x*y + 8*y**2

    Parameters
    ----------
    p : :class:`~.PolyElement` Input series.
    rules : ``dict`` with substitution mappings.
    x : :class:`~.PolyElement` in which the series truncation is to be done.
    prec : :class:`~.Integer` order of the series after truncation.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_subs
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_subs(x**2+y**2, {y: (x+y)**2}, x, 3)
     6*x**2*y**2 + x**2 + 4*x*y**3 + y**4
    """
def rs_series_inversion(p, x, prec):
    """
    Multivariate series inversion ``1/p`` modulo ``O(x**prec)``.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_series_inversion
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_series_inversion(1 + x*y**2, x, 4)
    -x**3*y**6 + x**2*y**4 - x*y**2 + 1
    >>> rs_series_inversion(1 + x*y**2, y, 4)
    -x*y**2 + 1
    >>> rs_series_inversion(x + x**2, x, 4)
    x**3 - x**2 + x - 1 + x**(-1)
    """
def rs_series_reversion(p, x, n, y):
    """
    Reversion of a series.

    ``p`` is a series with ``O(x**n)`` of the form $p = ax + f(x)$
    where $a$ is a number different from 0.

    $f(x) = \\sum_{k=2}^{n-1} a_kx_k$

    Parameters
    ==========

      a_k : Can depend polynomially on other variables, not indicated.
      x : Variable with name x.
      y : Variable with name y.

    Returns
    =======

    Solve $p = y$, that is, given $ax + f(x) - y = 0$,
    find the solution $x = r(y)$ up to $O(y^n)$.

    Algorithm
    =========

    If $r_i$ is the solution at order $i$, then:
    $ar_i + f(r_i) - y = O\\left(y^{i + 1}\\right)$

    and if $r_{i + 1}$ is the solution at order $i + 1$, then:
    $ar_{i + 1} + f(r_{i + 1}) - y = O\\left(y^{i + 2}\\right)$

    We have, $r_{i + 1} = r_i + e$, such that,
    $ae + f(r_i) = O\\left(y^{i + 2}\\right)$
    or $e = -f(r_i)/a$

    So we use the recursion relation:
    $r_{i + 1} = r_i - f(r_i)/a$
    with the boundary condition: $r_1 = y$

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_series_reversion, rs_trunc
    >>> R, x, y, a, b = ring('x, y, a, b', QQ)
    >>> p = x - x**2 - 2*b*x**2 + 2*a*b*x**2
    >>> p1 = rs_series_reversion(p, x, 3, y); p1
    -2*y**2*a*b + 2*y**2*b + y**2 + y
    >>> rs_trunc(p.compose(x, p1), y, 3)
    y
    """
def rs_series_from_list(p, c, x, prec, concur: int = 1):
    """
    Return a series `sum c[n]*p**n` modulo `O(x**prec)`.

    It reduces the number of multiplications by summing concurrently.

    `ax = [1, p, p**2, .., p**(J - 1)]`
    `s = sum(c[i]*ax[i]` for i in `range(r, (r + 1)*J))*p**((K - 1)*J)`
    with `K >= (n + 1)/J`

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_series_from_list, rs_trunc
    >>> R, x = ring('x', QQ)
    >>> p = x**2 + x + 1
    >>> c = [1, 2, 3]
    >>> rs_series_from_list(p, c, x, 4)
    6*x**3 + 11*x**2 + 8*x + 6
    >>> rs_trunc(1 + 2*p + 3*p**2, x, 4)
    6*x**3 + 11*x**2 + 8*x + 6
    >>> pc = R.from_list(list(reversed(c)))
    >>> rs_trunc(pc.compose(x, p), x, 4)
    6*x**3 + 11*x**2 + 8*x + 6

    """
def rs_diff(p, x):
    """
    Return partial derivative of ``p`` with respect to ``x``.

    Parameters
    ==========

    x : :class:`~.PolyElement` with respect to which ``p`` is differentiated.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_diff
    >>> R, x, y = ring('x, y', QQ)
    >>> p = x + x**2*y**3
    >>> rs_diff(p, x)
    2*x*y**3 + 1
    """
def rs_integrate(p, x):
    """
    Integrate ``p`` with respect to ``x``.

    Parameters
    ==========

    x : :class:`~.PolyElement` with respect to which ``p`` is integrated.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_integrate
    >>> R, x, y = ring('x, y', QQ)
    >>> p = x + x**2*y**3
    >>> rs_integrate(p, x)
    1/3*x**3*y**3 + 1/2*x**2
    """
def rs_fun(p, f, *args):
    """
    Function of a multivariate series computed by substitution.

    The case with f method name is used to compute `rs\\_tan` and `rs\\_nth\\_root`
    of a multivariate series:

        `rs\\_fun(p, tan, iv, prec)`

        tan series is first computed for a dummy variable _x,
        i.e, `rs\\_tan(\\_x, iv, prec)`. Then we substitute _x with p to get the
        desired series

    Parameters
    ==========

    p : :class:`~.PolyElement` The multivariate series to be expanded.
    f : `ring\\_series` function to be applied on `p`.
    args[-2] : :class:`~.PolyElement` with respect to which, the series is to be expanded.
    args[-1] : Required order of the expanded series.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_fun, _tan1
    >>> R, x, y = ring('x, y', QQ)
    >>> p = x + x*y + x**2*y + x**3*y**2
    >>> rs_fun(p, _tan1, x, 4)
    1/3*x**3*y**3 + 2*x**3*y**2 + x**3*y + 1/3*x**3 + x**2*y + x*y + x
    """
def mul_xin(p, i, n):
    """
    Return `p*x_i**n`.

    `x\\_i` is the ith variable in ``p``.
    """
def pow_xin(p, i, n):
    """
    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import pow_xin
    >>> R, x, y = ring('x, y', QQ)
    >>> p = x**QQ(2,5) + x + x**QQ(2,3)
    >>> index = p.ring.gens.index(x)
    >>> pow_xin(p, index, 15)
    x**15 + x**10 + x**6
    """
def rs_nth_root(p, n, x, prec):
    """
    Multivariate series expansion of the nth root of ``p``.

    Parameters
    ==========

    p : Expr
        The polynomial to computer the root of.
    n : integer
        The order of the root to be computed.
    x : :class:`~.PolyElement`
    prec : integer
        Order of the expanded series.

    Notes
    =====

    The result of this function is dependent on the ring over which the
    polynomial has been defined. If the answer involves a root of a constant,
    make sure that the polynomial is over a real field. It cannot yet handle
    roots of symbols.

    Examples
    ========

    >>> from sympy.polys.domains import QQ, RR
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_nth_root
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_nth_root(1 + x + x*y, -3, x, 3)
    2/9*x**2*y**2 + 4/9*x**2*y + 2/9*x**2 - 1/3*x*y - 1/3*x + 1
    >>> R, x, y = ring('x, y', RR)
    >>> rs_nth_root(3 + x + x*y, 3, x, 2)
    0.160249952256379*x*y + 0.160249952256379*x + 1.44224957030741
    """
def rs_log(p, x, prec):
    """
    The Logarithm of ``p`` modulo ``O(x**prec)``.

    Notes
    =====

    Truncation of ``integral dx p**-1*d p/dx`` is used.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_log
    >>> R, x = ring('x', QQ)
    >>> rs_log(1 + x, x, 8)
    1/7*x**7 - 1/6*x**6 + 1/5*x**5 - 1/4*x**4 + 1/3*x**3 - 1/2*x**2 + x
    >>> rs_log(x**QQ(3, 2) + 1, x, 5)
    1/3*x**(9/2) - 1/2*x**3 + x**(3/2)
    """
def rs_LambertW(p, x, prec):
    """
    Calculate the series expansion of the principal branch of the Lambert W
    function.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_LambertW
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_LambertW(x + x*y, x, 3)
    -x**2*y**2 - 2*x**2*y - x**2 + x*y + x

    See Also
    ========

    LambertW
    """
def rs_exp(p, x, prec):
    """
    Exponentiation of a series modulo ``O(x**prec)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_exp
    >>> R, x = ring('x', QQ)
    >>> rs_exp(x**2, x, 7)
    1/6*x**6 + 1/2*x**4 + x**2 + 1
    """
def rs_atan(p, x, prec):
    """
    The arctangent of a series

    Return the series expansion of the atan of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_atan
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_atan(x + x*y, x, 4)
    -1/3*x**3*y**3 - x**3*y**2 - x**3*y - 1/3*x**3 + x*y + x

    See Also
    ========

    atan
    """
def rs_asin(p, x, prec):
    """
    Arcsine of a series

    Return the series expansion of the asin of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_asin
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_asin(x, x, 8)
    5/112*x**7 + 3/40*x**5 + 1/6*x**3 + x

    See Also
    ========

    asin
    """
def rs_tan(p, x, prec):
    """
    Tangent of a series.

    Return the series expansion of the tan of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_tan
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_tan(x + x*y, x, 4)
    1/3*x**3*y**3 + x**3*y**2 + x**3*y + 1/3*x**3 + x*y + x

   See Also
   ========

   _tan1, tan
   """
def rs_cot(p, x, prec):
    """
    Cotangent of a series

    Return the series expansion of the cot of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_cot
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_cot(x, x, 6)
    -2/945*x**5 - 1/45*x**3 - 1/3*x + x**(-1)

    See Also
    ========

    cot
    """
def rs_sin(p, x, prec):
    """
    Sine of a series

    Return the series expansion of the sin of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_sin
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_sin(x + x*y, x, 4)
    -1/6*x**3*y**3 - 1/2*x**3*y**2 - 1/2*x**3*y - 1/6*x**3 + x*y + x
    >>> rs_sin(x**QQ(3, 2) + x*y**QQ(7, 5), x, 4)
    -1/2*x**(7/2)*y**(14/5) - 1/6*x**3*y**(21/5) + x**(3/2) + x*y**(7/5)

    See Also
    ========

    sin
    """
def rs_cos(p, x, prec):
    """
    Cosine of a series

    Return the series expansion of the cos of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_cos
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_cos(x + x*y, x, 4)
    -1/2*x**2*y**2 - x**2*y - 1/2*x**2 + 1
    >>> rs_cos(x + x*y, x, 4)/x**QQ(7, 5)
    -1/2*x**(3/5)*y**2 - x**(3/5)*y - 1/2*x**(3/5) + x**(-7/5)

    See Also
    ========

    cos
    """
def rs_cos_sin(p, x, prec):
    """
    Return the tuple ``(rs_cos(p, x, prec)`, `rs_sin(p, x, prec))``.

    Is faster than calling rs_cos and rs_sin separately
    """
def rs_atanh(p, x, prec):
    """
    Hyperbolic arctangent of a series

    Return the series expansion of the atanh of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_atanh
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_atanh(x + x*y, x, 4)
    1/3*x**3*y**3 + x**3*y**2 + x**3*y + 1/3*x**3 + x*y + x

    See Also
    ========

    atanh
    """
def rs_sinh(p, x, prec):
    """
    Hyperbolic sine of a series

    Return the series expansion of the sinh of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_sinh
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_sinh(x + x*y, x, 4)
    1/6*x**3*y**3 + 1/2*x**3*y**2 + 1/2*x**3*y + 1/6*x**3 + x*y + x

    See Also
    ========

    sinh
    """
def rs_cosh(p, x, prec):
    """
    Hyperbolic cosine of a series

    Return the series expansion of the cosh of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_cosh
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_cosh(x + x*y, x, 4)
    1/2*x**2*y**2 + x**2*y + 1/2*x**2 + 1

    See Also
    ========

    cosh
    """
def rs_tanh(p, x, prec):
    """
    Hyperbolic tangent of a series

    Return the series expansion of the tanh of ``p``, about 0.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_tanh
    >>> R, x, y = ring('x, y', QQ)
    >>> rs_tanh(x + x*y, x, 4)
    -1/3*x**3*y**3 - x**3*y**2 - x**3*y - 1/3*x**3 + x*y + x

    See Also
    ========

    tanh
    """
def rs_newton(p, x, prec):
    """
    Compute the truncated Newton sum of the polynomial ``p``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_newton
    >>> R, x = ring('x', QQ)
    >>> p = x**2 - 2
    >>> rs_newton(p, x, 5)
    8*x**4 + 4*x**2 + 2
    """
def rs_hadamard_exp(p1, inverse: bool = False):
    """
    Return ``sum f_i/i!*x**i`` from ``sum f_i*x**i``,
    where ``x`` is the first variable.

    If ``invers=True`` return ``sum f_i*i!*x**i``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_hadamard_exp
    >>> R, x = ring('x', QQ)
    >>> p = 1 + x + x**2 + x**3
    >>> rs_hadamard_exp(p)
    1/6*x**3 + 1/2*x**2 + x + 1
    """
def rs_compose_add(p1, p2):
    '''
    compute the composed sum ``prod(p2(x - beta) for beta root of p1)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_compose_add
    >>> R, x = ring(\'x\', QQ)
    >>> f = x**2 - 2
    >>> g = x**2 - 3
    >>> rs_compose_add(f, g)
    x**4 - 10*x**2 + 1

    References
    ==========

    .. [1] A. Bostan, P. Flajolet, B. Salvy and E. Schost
           "Fast Computation with Two Algebraic Numbers",
           (2002) Research Report 4579, Institut
           National de Recherche en Informatique et en Automatique
    '''
def rs_min_pow(expr, series_rs, a):
    """Find the minimum power of `a` in the series expansion of expr"""
def rs_series(expr, a, prec):
    """Return the series expansion of an expression about 0.

    Parameters
    ==========

    expr : :class:`Expr`
    a : :class:`Symbol` with respect to which expr is to be expanded
    prec : order of the series expansion

    Currently supports multivariate Taylor series expansion. This is much
    faster that SymPy's series method as it uses sparse polynomial operations.

    It automatically creates the simplest ring required to represent the series
    expansion through repeated calls to sring.

    Examples
    ========

    >>> from sympy.polys.ring_series import rs_series
    >>> from sympy import sin, cos, exp, tan, symbols, QQ
    >>> a, b, c = symbols('a, b, c')
    >>> rs_series(sin(a) + exp(a), a, 5)
    1/24*a**4 + 1/2*a**2 + 2*a + 1
    >>> series = rs_series(tan(a + b)*cos(a + c), a, 2)
    >>> series.as_expr()
    -a*sin(c)*tan(b) + a*cos(c)*tan(b)**2 + a*cos(c) + cos(c)*tan(b)
    >>> series = rs_series(exp(a**QQ(1,3) + a**QQ(2, 5)), a, 1)
    >>> series.as_expr()
    a**(11/15) + a**(4/5)/2 + a**(2/5) + a**(2/3)/2 + a**(1/3) + 1

    """
