from sympy.core import Rational as Rational
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.functions.combinatorial.factorials import RisingFactorial as RisingFactorial, binomial as binomial, factorial as factorial
from sympy.functions.elementary.complexes import re as re
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.integers import floor as floor
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, sec as sec
from sympy.functions.special.gamma_functions import gamma as gamma
from sympy.functions.special.hyper import hyper as hyper
from sympy.polys.orthopolys import chebyshevt_poly as chebyshevt_poly, chebyshevu_poly as chebyshevu_poly, gegenbauer_poly as gegenbauer_poly, hermite_poly as hermite_poly, hermite_prob_poly as hermite_prob_poly, jacobi_poly as jacobi_poly, laguerre_poly as laguerre_poly, legendre_poly as legendre_poly

class OrthogonalPolynomial(Function):
    """Base class for orthogonal polynomials.
    """

class jacobi(OrthogonalPolynomial):
    """
    Jacobi polynomial $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    Explanation
    ===========

    ``jacobi(n, alpha, beta, x)`` gives the $n$th Jacobi polynomial
    in $x$, $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    The Jacobi polynomials are orthogonal on $[-1, 1]$ with respect
    to the weight $\\left(1-x\\right)^\\alpha \\left(1+x\\right)^\\beta$.

    Examples
    ========

    >>> from sympy import jacobi, S, conjugate, diff
    >>> from sympy.abc import a, b, n, x

    >>> jacobi(0, a, b, x)
    1
    >>> jacobi(1, a, b, x)
    a/2 - b/2 + x*(a/2 + b/2 + 1)
    >>> jacobi(2, a, b, x)
    a**2/8 - a*b/4 - a/8 + b**2/8 - b/8 + x**2*(a**2/8 + a*b/4 + 7*a/8 + b**2/8 + 7*b/8 + 3/2) + x*(a**2/4 + 3*a/4 - b**2/4 - 3*b/4) - 1/2

    >>> jacobi(n, a, b, x)
    jacobi(n, a, b, x)

    >>> jacobi(n, a, a, x)
    RisingFactorial(a + 1, n)*gegenbauer(n,
        a + 1/2, x)/RisingFactorial(2*a + 1, n)

    >>> jacobi(n, 0, 0, x)
    legendre(n, x)

    >>> jacobi(n, S(1)/2, S(1)/2, x)
    RisingFactorial(3/2, n)*chebyshevu(n, x)/factorial(n + 1)

    >>> jacobi(n, -S(1)/2, -S(1)/2, x)
    RisingFactorial(1/2, n)*chebyshevt(n, x)/factorial(n)

    >>> jacobi(n, a, b, -x)
    (-1)**n*jacobi(n, b, a, x)

    >>> jacobi(n, a, b, 0)
    gamma(a + n + 1)*hyper((-b - n, -n), (a + 1,), -1)/(2**n*factorial(n)*gamma(a + 1))
    >>> jacobi(n, a, b, 1)
    RisingFactorial(a + 1, n)/factorial(n)

    >>> conjugate(jacobi(n, a, b, x))
    jacobi(n, conjugate(a), conjugate(b), conjugate(x))

    >>> diff(jacobi(n,a,b,x), x)
    (a/2 + b/2 + n/2 + 1/2)*jacobi(n - 1, a + 1, b + 1, x)

    See Also
    ========

    gegenbauer,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly,
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Jacobi_polynomials
    .. [2] https://mathworld.wolfram.com/JacobiPolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/JacobiP/

    """
    @classmethod
    def eval(cls, n, a, b, x): ...
    def fdiff(self, argindex: int = 4): ...

def jacobi_normalized(n, a, b, x):
    """
    Jacobi polynomial $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    Explanation
    ===========

    ``jacobi_normalized(n, alpha, beta, x)`` gives the $n$th
    Jacobi polynomial in $x$, $P_n^{\\left(\\alpha, \\beta\\right)}(x)$.

    The Jacobi polynomials are orthogonal on $[-1, 1]$ with respect
    to the weight $\\left(1-x\\right)^\\alpha \\left(1+x\\right)^\\beta$.

    This functions returns the polynomials normilzed:

    .. math::

        \\int_{-1}^{1}
          P_m^{\\left(\\alpha, \\beta\\right)}(x)
          P_n^{\\left(\\alpha, \\beta\\right)}(x)
          (1-x)^{\\alpha} (1+x)^{\\beta} \\mathrm{d}x
        = \\delta_{m,n}

    Examples
    ========

    >>> from sympy import jacobi_normalized
    >>> from sympy.abc import n,a,b,x

    >>> jacobi_normalized(n, a, b, x)
    jacobi(n, a, b, x)/sqrt(2**(a + b + 1)*gamma(a + n + 1)*gamma(b + n + 1)/((a + b + 2*n + 1)*factorial(n)*gamma(a + b + n + 1)))

    Parameters
    ==========

    n : integer degree of polynomial

    a : alpha value

    b : beta value

    x : symbol

    See Also
    ========

    gegenbauer,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly,
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Jacobi_polynomials
    .. [2] https://mathworld.wolfram.com/JacobiPolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/JacobiP/

    """

class gegenbauer(OrthogonalPolynomial):
    """
    Gegenbauer polynomial $C_n^{\\left(\\alpha\\right)}(x)$.

    Explanation
    ===========

    ``gegenbauer(n, alpha, x)`` gives the $n$th Gegenbauer polynomial
    in $x$, $C_n^{\\left(\\alpha\\right)}(x)$.

    The Gegenbauer polynomials are orthogonal on $[-1, 1]$ with
    respect to the weight $\\left(1-x^2\\right)^{\\alpha-\\frac{1}{2}}$.

    Examples
    ========

    >>> from sympy import gegenbauer, conjugate, diff
    >>> from sympy.abc import n,a,x
    >>> gegenbauer(0, a, x)
    1
    >>> gegenbauer(1, a, x)
    2*a*x
    >>> gegenbauer(2, a, x)
    -a + x**2*(2*a**2 + 2*a)
    >>> gegenbauer(3, a, x)
    x**3*(4*a**3/3 + 4*a**2 + 8*a/3) + x*(-2*a**2 - 2*a)

    >>> gegenbauer(n, a, x)
    gegenbauer(n, a, x)
    >>> gegenbauer(n, a, -x)
    (-1)**n*gegenbauer(n, a, x)

    >>> gegenbauer(n, a, 0)
    2**n*sqrt(pi)*gamma(a + n/2)/(gamma(a)*gamma(1/2 - n/2)*gamma(n + 1))
    >>> gegenbauer(n, a, 1)
    gamma(2*a + n)/(gamma(2*a)*gamma(n + 1))

    >>> conjugate(gegenbauer(n, a, x))
    gegenbauer(n, conjugate(a), conjugate(x))

    >>> diff(gegenbauer(n, a, x), x)
    2*a*gegenbauer(n - 1, a + 1, x)

    See Also
    ========

    jacobi,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gegenbauer_polynomials
    .. [2] https://mathworld.wolfram.com/GegenbauerPolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/GegenbauerC3/

    """
    @classmethod
    def eval(cls, n, a, x): ...
    def fdiff(self, argindex: int = 3): ...

class chebyshevt(OrthogonalPolynomial):
    """
    Chebyshev polynomial of the first kind, $T_n(x)$.

    Explanation
    ===========

    ``chebyshevt(n, x)`` gives the $n$th Chebyshev polynomial (of the first
    kind) in $x$, $T_n(x)$.

    The Chebyshev polynomials of the first kind are orthogonal on
    $[-1, 1]$ with respect to the weight $\\frac{1}{\\sqrt{1-x^2}}$.

    Examples
    ========

    >>> from sympy import chebyshevt, diff
    >>> from sympy.abc import n,x
    >>> chebyshevt(0, x)
    1
    >>> chebyshevt(1, x)
    x
    >>> chebyshevt(2, x)
    2*x**2 - 1

    >>> chebyshevt(n, x)
    chebyshevt(n, x)
    >>> chebyshevt(n, -x)
    (-1)**n*chebyshevt(n, x)
    >>> chebyshevt(-n, x)
    chebyshevt(n, x)

    >>> chebyshevt(n, 0)
    cos(pi*n/2)
    >>> chebyshevt(n, -1)
    (-1)**n

    >>> diff(chebyshevt(n, x), x)
    n*chebyshevu(n - 1, x)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Chebyshev_polynomial
    .. [2] https://mathworld.wolfram.com/ChebyshevPolynomialoftheFirstKind.html
    .. [3] https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html
    .. [4] https://functions.wolfram.com/Polynomials/ChebyshevT/
    .. [5] https://functions.wolfram.com/Polynomials/ChebyshevU/

    """
    @classmethod
    def eval(cls, n, x): ...
    def fdiff(self, argindex: int = 2): ...

class chebyshevu(OrthogonalPolynomial):
    """
    Chebyshev polynomial of the second kind, $U_n(x)$.

    Explanation
    ===========

    ``chebyshevu(n, x)`` gives the $n$th Chebyshev polynomial of the second
    kind in x, $U_n(x)$.

    The Chebyshev polynomials of the second kind are orthogonal on
    $[-1, 1]$ with respect to the weight $\\sqrt{1-x^2}$.

    Examples
    ========

    >>> from sympy import chebyshevu, diff
    >>> from sympy.abc import n,x
    >>> chebyshevu(0, x)
    1
    >>> chebyshevu(1, x)
    2*x
    >>> chebyshevu(2, x)
    4*x**2 - 1

    >>> chebyshevu(n, x)
    chebyshevu(n, x)
    >>> chebyshevu(n, -x)
    (-1)**n*chebyshevu(n, x)
    >>> chebyshevu(-n, x)
    -chebyshevu(n - 2, x)

    >>> chebyshevu(n, 0)
    cos(pi*n/2)
    >>> chebyshevu(n, 1)
    n + 1

    >>> diff(chebyshevu(n, x), x)
    (-x*chebyshevu(n, x) + (n + 1)*chebyshevt(n + 1, x))/(x**2 - 1)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Chebyshev_polynomial
    .. [2] https://mathworld.wolfram.com/ChebyshevPolynomialoftheFirstKind.html
    .. [3] https://mathworld.wolfram.com/ChebyshevPolynomialoftheSecondKind.html
    .. [4] https://functions.wolfram.com/Polynomials/ChebyshevT/
    .. [5] https://functions.wolfram.com/Polynomials/ChebyshevU/

    """
    @classmethod
    def eval(cls, n, x): ...
    def fdiff(self, argindex: int = 2): ...

class chebyshevt_root(Function):
    """
    ``chebyshev_root(n, k)`` returns the $k$th root (indexed from zero) of
    the $n$th Chebyshev polynomial of the first kind; that is, if
    $0 \\le k < n$, ``chebyshevt(n, chebyshevt_root(n, k)) == 0``.

    Examples
    ========

    >>> from sympy import chebyshevt, chebyshevt_root
    >>> chebyshevt_root(3, 2)
    -sqrt(3)/2
    >>> chebyshevt(3, chebyshevt_root(3, 2))
    0

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly
    """
    @classmethod
    def eval(cls, n, k): ...

class chebyshevu_root(Function):
    """
    ``chebyshevu_root(n, k)`` returns the $k$th root (indexed from zero) of the
    $n$th Chebyshev polynomial of the second kind; that is, if $0 \\le k < n$,
    ``chebyshevu(n, chebyshevu_root(n, k)) == 0``.

    Examples
    ========

    >>> from sympy import chebyshevu, chebyshevu_root
    >>> chebyshevu_root(3, 2)
    -sqrt(2)/2
    >>> chebyshevu(3, chebyshevu_root(3, 2))
    0

    See Also
    ========

    chebyshevt, chebyshevt_root, chebyshevu,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly
    """
    @classmethod
    def eval(cls, n, k): ...

class legendre(OrthogonalPolynomial):
    """
    ``legendre(n, x)`` gives the $n$th Legendre polynomial of $x$, $P_n(x)$

    Explanation
    ===========

    The Legendre polynomials are orthogonal on $[-1, 1]$ with respect to
    the constant weight 1. They satisfy $P_n(1) = 1$ for all $n$; further,
    $P_n$ is odd for odd $n$ and even for even $n$.

    Examples
    ========

    >>> from sympy import legendre, diff
    >>> from sympy.abc import x, n
    >>> legendre(0, x)
    1
    >>> legendre(1, x)
    x
    >>> legendre(2, x)
    3*x**2/2 - 1/2
    >>> legendre(n, x)
    legendre(n, x)
    >>> diff(legendre(n,x), x)
    n*(x*legendre(n, x) - legendre(n - 1, x))/(x**2 - 1)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
    assoc_legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Legendre_polynomial
    .. [2] https://mathworld.wolfram.com/LegendrePolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/LegendreP/
    .. [4] https://functions.wolfram.com/Polynomials/LegendreP2/

    """
    @classmethod
    def eval(cls, n, x): ...
    def fdiff(self, argindex: int = 2): ...

class assoc_legendre(Function):
    """
    ``assoc_legendre(n, m, x)`` gives $P_n^m(x)$, where $n$ and $m$ are
    the degree and order or an expression which is related to the nth
    order Legendre polynomial, $P_n(x)$ in the following manner:

    .. math::
        P_n^m(x) = (-1)^m (1 - x^2)^{\\frac{m}{2}}
                   \\frac{\\mathrm{d}^m P_n(x)}{\\mathrm{d} x^m}

    Explanation
    ===========

    Associated Legendre polynomials are orthogonal on $[-1, 1]$ with:

    - weight $= 1$            for the same $m$ and different $n$.
    - weight $= \\frac{1}{1-x^2}$   for the same $n$ and different $m$.

    Examples
    ========

    >>> from sympy import assoc_legendre
    >>> from sympy.abc import x, m, n
    >>> assoc_legendre(0,0, x)
    1
    >>> assoc_legendre(1,0, x)
    x
    >>> assoc_legendre(1,1, x)
    -sqrt(1 - x**2)
    >>> assoc_legendre(n,m,x)
    assoc_legendre(n, m, x)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre,
    hermite, hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Associated_Legendre_polynomials
    .. [2] https://mathworld.wolfram.com/LegendrePolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/LegendreP/
    .. [4] https://functions.wolfram.com/Polynomials/LegendreP2/

    """
    @classmethod
    def eval(cls, n, m, x): ...
    def fdiff(self, argindex: int = 3): ...

class hermite(OrthogonalPolynomial):
    """
    ``hermite(n, x)`` gives the $n$th Hermite polynomial in $x$, $H_n(x)$.

    Explanation
    ===========

    The Hermite polynomials are orthogonal on $(-\\infty, \\infty)$
    with respect to the weight $\\exp\\left(-x^2\\right)$.

    Examples
    ========

    >>> from sympy import hermite, diff
    >>> from sympy.abc import x, n
    >>> hermite(0, x)
    1
    >>> hermite(1, x)
    2*x
    >>> hermite(2, x)
    4*x**2 - 2
    >>> hermite(n, x)
    hermite(n, x)
    >>> diff(hermite(n,x), x)
    2*n*hermite(n - 1, x)
    >>> hermite(n, -x)
    (-1)**n*hermite(n, x)

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite_prob,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hermite_polynomial
    .. [2] https://mathworld.wolfram.com/HermitePolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/HermiteH/

    """
    @classmethod
    def eval(cls, n, x): ...
    def fdiff(self, argindex: int = 2): ...

class hermite_prob(OrthogonalPolynomial):
    """
    ``hermite_prob(n, x)`` gives the $n$th probabilist's Hermite polynomial
    in $x$, $He_n(x)$.

    Explanation
    ===========

    The probabilist's Hermite polynomials are orthogonal on $(-\\infty, \\infty)$
    with respect to the weight $\\exp\\left(-\\frac{x^2}{2}\\right)$. They are monic
    polynomials, related to the plain Hermite polynomials (:py:class:`~.hermite`) by

    .. math :: He_n(x) = 2^{-n/2} H_n(x/\\sqrt{2})

    Examples
    ========

    >>> from sympy import hermite_prob, diff, I
    >>> from sympy.abc import x, n
    >>> hermite_prob(1, x)
    x
    >>> hermite_prob(5, x)
    x**5 - 10*x**3 + 15*x
    >>> diff(hermite_prob(n,x), x)
    n*hermite_prob(n - 1, x)
    >>> hermite_prob(n, -x)
    (-1)**n*hermite_prob(n, x)

    The sum of absolute values of coefficients of $He_n(x)$ is the number of
    matchings in the complete graph $K_n$ or telephone number, A000085 in the OEIS:

    >>> [hermite_prob(n,I) / I**n for n in range(11)]
    [1, 1, 2, 4, 10, 26, 76, 232, 764, 2620, 9496]

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite,
    laguerre, assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hermite_polynomial
    .. [2] https://mathworld.wolfram.com/HermitePolynomial.html
    """
    @classmethod
    def eval(cls, n, x): ...
    def fdiff(self, argindex: int = 2): ...

class laguerre(OrthogonalPolynomial):
    """
    Returns the $n$th Laguerre polynomial in $x$, $L_n(x)$.

    Examples
    ========

    >>> from sympy import laguerre, diff
    >>> from sympy.abc import x, n
    >>> laguerre(0, x)
    1
    >>> laguerre(1, x)
    1 - x
    >>> laguerre(2, x)
    x**2/2 - 2*x + 1
    >>> laguerre(3, x)
    -x**3/6 + 3*x**2/2 - 3*x + 1

    >>> laguerre(n, x)
    laguerre(n, x)

    >>> diff(laguerre(n, x), x)
    -assoc_laguerre(n - 1, 1, x)

    Parameters
    ==========

    n : int
        Degree of Laguerre polynomial. Must be `n \\ge 0`.

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    assoc_laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Laguerre_polynomial
    .. [2] https://mathworld.wolfram.com/LaguerrePolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/LaguerreL/
    .. [4] https://functions.wolfram.com/Polynomials/LaguerreL3/

    """
    @classmethod
    def eval(cls, n, x): ...
    def fdiff(self, argindex: int = 2): ...

class assoc_laguerre(OrthogonalPolynomial):
    """
    Returns the $n$th generalized Laguerre polynomial in $x$, $L_n(x)$.

    Examples
    ========

    >>> from sympy import assoc_laguerre, diff
    >>> from sympy.abc import x, n, a
    >>> assoc_laguerre(0, a, x)
    1
    >>> assoc_laguerre(1, a, x)
    a - x + 1
    >>> assoc_laguerre(2, a, x)
    a**2/2 + 3*a/2 + x**2/2 + x*(-a - 2) + 1
    >>> assoc_laguerre(3, a, x)
    a**3/6 + a**2 + 11*a/6 - x**3/6 + x**2*(a/2 + 3/2) +
        x*(-a**2/2 - 5*a/2 - 3) + 1

    >>> assoc_laguerre(n, a, 0)
    binomial(a + n, a)

    >>> assoc_laguerre(n, a, x)
    assoc_laguerre(n, a, x)

    >>> assoc_laguerre(n, 0, x)
    laguerre(n, x)

    >>> diff(assoc_laguerre(n, a, x), x)
    -assoc_laguerre(n - 1, a + 1, x)

    >>> diff(assoc_laguerre(n, a, x), a)
    Sum(assoc_laguerre(_k, a, x)/(-a + n), (_k, 0, n - 1))

    Parameters
    ==========

    n : int
        Degree of Laguerre polynomial. Must be `n \\ge 0`.

    alpha : Expr
        Arbitrary expression. For ``alpha=0`` regular Laguerre
        polynomials will be generated.

    See Also
    ========

    jacobi, gegenbauer,
    chebyshevt, chebyshevt_root, chebyshevu, chebyshevu_root,
    legendre, assoc_legendre,
    hermite, hermite_prob,
    laguerre,
    sympy.polys.orthopolys.jacobi_poly
    sympy.polys.orthopolys.gegenbauer_poly
    sympy.polys.orthopolys.chebyshevt_poly
    sympy.polys.orthopolys.chebyshevu_poly
    sympy.polys.orthopolys.hermite_poly
    sympy.polys.orthopolys.hermite_prob_poly
    sympy.polys.orthopolys.legendre_poly
    sympy.polys.orthopolys.laguerre_poly

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Laguerre_polynomial#Generalized_Laguerre_polynomials
    .. [2] https://mathworld.wolfram.com/AssociatedLaguerrePolynomial.html
    .. [3] https://functions.wolfram.com/Polynomials/LaguerreL/
    .. [4] https://functions.wolfram.com/Polynomials/LaguerreL3/

    """
    @classmethod
    def eval(cls, n, alpha, x): ...
    def fdiff(self, argindex: int = 3): ...
