from sympy.core import S as S
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.logic import fuzzy_not as fuzzy_not, fuzzy_or as fuzzy_or
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.power import Pow as Pow
from sympy.core.symbol import Dummy as Dummy, Wild as Wild
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.complexes import Abs as Abs, im as im, polar_lift as polar_lift, re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.integers import ceiling as ceiling
from sympy.functions.elementary.miscellaneous import cbrt as cbrt, root as root, sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, cot as cot, csc as csc, sin as sin
from sympy.functions.special.gamma_functions import digamma as digamma, gamma as gamma, uppergamma as uppergamma
from sympy.functions.special.hyper import hyper as hyper
from sympy.polys.orthopolys import spherical_bessel_fn as spherical_bessel_fn

class BesselBase(Function):
    """
    Abstract base class for Bessel-type functions.

    This class is meant to reduce code duplication.
    All Bessel-type functions can 1) be differentiated, with the derivatives
    expressed in terms of similar functions, and 2) be rewritten in terms
    of other Bessel-type functions.

    Here, Bessel-type functions are assumed to have one complex parameter.

    To use this base class, define class attributes ``_a`` and ``_b`` such that
    ``2*F_n' = -_a*F_{n+1} + b*F_{n-1}``.

    """
    @property
    def order(self):
        """ The order of the Bessel-type function. """
    @property
    def argument(self):
        """ The argument of the Bessel-type function. """
    @classmethod
    def eval(cls, nu, z) -> None: ...
    def fdiff(self, argindex: int = 2): ...

class besselj(BesselBase):
    '''
    Bessel function of the first kind.

    Explanation
    ===========

    The Bessel $J$ function of order $\\nu$ is defined to be the function
    satisfying Bessel\'s differential equation

    .. math ::
        z^2 \\frac{\\mathrm{d}^2 w}{\\mathrm{d}z^2}
        + z \\frac{\\mathrm{d}w}{\\mathrm{d}z} + (z^2 - \\nu^2) w = 0,

    with Laurent expansion

    .. math ::
        J_\\nu(z) = z^\\nu \\left(\\frac{1}{\\Gamma(\\nu + 1) 2^\\nu} + O(z^2) \\right),

    if $\\nu$ is not a negative integer. If $\\nu=-n \\in \\mathbb{Z}_{<0}$
    *is* a negative integer, then the definition is

    .. math ::
        J_{-n}(z) = (-1)^n J_n(z).

    Examples
    ========

    Create a Bessel function object:

    >>> from sympy import besselj, jn
    >>> from sympy.abc import z, n
    >>> b = besselj(n, z)

    Differentiate it:

    >>> b.diff(z)
    besselj(n - 1, z)/2 - besselj(n + 1, z)/2

    Rewrite in terms of spherical Bessel functions:

    >>> b.rewrite(jn)
    sqrt(2)*sqrt(z)*jn(n - 1/2, z)/sqrt(pi)

    Access the parameter and argument:

    >>> b.order
    n
    >>> b.argument
    z

    See Also
    ========

    bessely, besseli, besselk

    References
    ==========

    .. [1] Abramowitz, Milton; Stegun, Irene A., eds. (1965), "Chapter 9",
           Handbook of Mathematical Functions with Formulas, Graphs, and
           Mathematical Tables
    .. [2] Luke, Y. L. (1969), The Special Functions and Their
           Approximations, Volume 1
    .. [3] https://en.wikipedia.org/wiki/Bessel_function
    .. [4] https://functions.wolfram.com/Bessel-TypeFunctions/BesselJ/

    '''
    @classmethod
    def eval(cls, nu, z): ...

class bessely(BesselBase):
    """
    Bessel function of the second kind.

    Explanation
    ===========

    The Bessel $Y$ function of order $\\nu$ is defined as

    .. math ::
        Y_\\nu(z) = \\lim_{\\mu \\to \\nu} \\frac{J_\\mu(z) \\cos(\\pi \\mu)
                                            - J_{-\\mu}(z)}{\\sin(\\pi \\mu)},

    where $J_\\mu(z)$ is the Bessel function of the first kind.

    It is a solution to Bessel's equation, and linearly independent from
    $J_\\nu$.

    Examples
    ========

    >>> from sympy import bessely, yn
    >>> from sympy.abc import z, n
    >>> b = bessely(n, z)
    >>> b.diff(z)
    bessely(n - 1, z)/2 - bessely(n + 1, z)/2
    >>> b.rewrite(yn)
    sqrt(2)*sqrt(z)*yn(n - 1/2, z)/sqrt(pi)

    See Also
    ========

    besselj, besseli, besselk

    References
    ==========

    .. [1] https://functions.wolfram.com/Bessel-TypeFunctions/BesselY/

    """
    @classmethod
    def eval(cls, nu, z): ...

class besseli(BesselBase):
    """
    Modified Bessel function of the first kind.

    Explanation
    ===========

    The Bessel $I$ function is a solution to the modified Bessel equation

    .. math ::
        z^2 \\frac{\\mathrm{d}^2 w}{\\mathrm{d}z^2}
        + z \\frac{\\mathrm{d}w}{\\mathrm{d}z} + (z^2 + \\nu^2)^2 w = 0.

    It can be defined as

    .. math ::
        I_\\nu(z) = i^{-\\nu} J_\\nu(iz),

    where $J_\\nu(z)$ is the Bessel function of the first kind.

    Examples
    ========

    >>> from sympy import besseli
    >>> from sympy.abc import z, n
    >>> besseli(n, z).diff(z)
    besseli(n - 1, z)/2 + besseli(n + 1, z)/2

    See Also
    ========

    besselj, bessely, besselk

    References
    ==========

    .. [1] https://functions.wolfram.com/Bessel-TypeFunctions/BesselI/

    """
    @classmethod
    def eval(cls, nu, z): ...

class besselk(BesselBase):
    """
    Modified Bessel function of the second kind.

    Explanation
    ===========

    The Bessel $K$ function of order $\\nu$ is defined as

    .. math ::
        K_\\nu(z) = \\lim_{\\mu \\to \\nu} \\frac{\\pi}{2}
                   \\frac{I_{-\\mu}(z) -I_\\mu(z)}{\\sin(\\pi \\mu)},

    where $I_\\mu(z)$ is the modified Bessel function of the first kind.

    It is a solution of the modified Bessel equation, and linearly independent
    from $Y_\\nu$.

    Examples
    ========

    >>> from sympy import besselk
    >>> from sympy.abc import z, n
    >>> besselk(n, z).diff(z)
    -besselk(n - 1, z)/2 - besselk(n + 1, z)/2

    See Also
    ========

    besselj, besseli, bessely

    References
    ==========

    .. [1] https://functions.wolfram.com/Bessel-TypeFunctions/BesselK/

    """
    @classmethod
    def eval(cls, nu, z): ...

class hankel1(BesselBase):
    """
    Hankel function of the first kind.

    Explanation
    ===========

    This function is defined as

    .. math ::
        H_\\nu^{(1)} = J_\\nu(z) + iY_\\nu(z),

    where $J_\\nu(z)$ is the Bessel function of the first kind, and
    $Y_\\nu(z)$ is the Bessel function of the second kind.

    It is a solution to Bessel's equation.

    Examples
    ========

    >>> from sympy import hankel1
    >>> from sympy.abc import z, n
    >>> hankel1(n, z).diff(z)
    hankel1(n - 1, z)/2 - hankel1(n + 1, z)/2

    See Also
    ========

    hankel2, besselj, bessely

    References
    ==========

    .. [1] https://functions.wolfram.com/Bessel-TypeFunctions/HankelH1/

    """
class hankel2(BesselBase):
    """
    Hankel function of the second kind.

    Explanation
    ===========

    This function is defined as

    .. math ::
        H_\\nu^{(2)} = J_\\nu(z) - iY_\\nu(z),

    where $J_\\nu(z)$ is the Bessel function of the first kind, and
    $Y_\\nu(z)$ is the Bessel function of the second kind.

    It is a solution to Bessel's equation, and linearly independent from
    $H_\\nu^{(1)}$.

    Examples
    ========

    >>> from sympy import hankel2
    >>> from sympy.abc import z, n
    >>> hankel2(n, z).diff(z)
    hankel2(n - 1, z)/2 - hankel2(n + 1, z)/2

    See Also
    ========

    hankel1, besselj, bessely

    References
    ==========

    .. [1] https://functions.wolfram.com/Bessel-TypeFunctions/HankelH2/

    """

def assume_integer_order(fn): ...

class SphericalBesselBase(BesselBase):
    """
    Base class for spherical Bessel functions.

    These are thin wrappers around ordinary Bessel functions,
    since spherical Bessel functions differ from the ordinary
    ones just by a slight change in order.

    To use this class, define the ``_eval_evalf()`` and ``_expand()`` methods.

    """
    def fdiff(self, argindex: int = 2): ...

class jn(SphericalBesselBase):
    '''
    Spherical Bessel function of the first kind.

    Explanation
    ===========

    This function is a solution to the spherical Bessel equation

    .. math ::
        z^2 \\frac{\\mathrm{d}^2 w}{\\mathrm{d}z^2}
          + 2z \\frac{\\mathrm{d}w}{\\mathrm{d}z} + (z^2 - \\nu(\\nu + 1)) w = 0.

    It can be defined as

    .. math ::
        j_\\nu(z) = \\sqrt{\\frac{\\pi}{2z}} J_{\\nu + \\frac{1}{2}}(z),

    where $J_\\nu(z)$ is the Bessel function of the first kind.

    The spherical Bessel functions of integral order are
    calculated using the formula:

    .. math:: j_n(z) = f_n(z) \\sin{z} + (-1)^{n+1} f_{-n-1}(z) \\cos{z},

    where the coefficients $f_n(z)$ are available as
    :func:`sympy.polys.orthopolys.spherical_bessel_fn`.

    Examples
    ========

    >>> from sympy import Symbol, jn, sin, cos, expand_func, besselj, bessely
    >>> z = Symbol("z")
    >>> nu = Symbol("nu", integer=True)
    >>> print(expand_func(jn(0, z)))
    sin(z)/z
    >>> expand_func(jn(1, z)) == sin(z)/z**2 - cos(z)/z
    True
    >>> expand_func(jn(3, z))
    (-6/z**2 + 15/z**4)*sin(z) + (1/z - 15/z**3)*cos(z)
    >>> jn(nu, z).rewrite(besselj)
    sqrt(2)*sqrt(pi)*sqrt(1/z)*besselj(nu + 1/2, z)/2
    >>> jn(nu, z).rewrite(bessely)
    (-1)**nu*sqrt(2)*sqrt(pi)*sqrt(1/z)*bessely(-nu - 1/2, z)/2
    >>> jn(2, 5.2+0.3j).evalf(20)
    0.099419756723640344491 - 0.054525080242173562897*I

    See Also
    ========

    besselj, bessely, besselk, yn

    References
    ==========

    .. [1] https://dlmf.nist.gov/10.47

    '''
    @classmethod
    def eval(cls, nu, z): ...

class yn(SphericalBesselBase):
    '''
    Spherical Bessel function of the second kind.

    Explanation
    ===========

    This function is another solution to the spherical Bessel equation, and
    linearly independent from $j_n$. It can be defined as

    .. math ::
        y_\\nu(z) = \\sqrt{\\frac{\\pi}{2z}} Y_{\\nu + \\frac{1}{2}}(z),

    where $Y_\\nu(z)$ is the Bessel function of the second kind.

    For integral orders $n$, $y_n$ is calculated using the formula:

    .. math:: y_n(z) = (-1)^{n+1} j_{-n-1}(z)

    Examples
    ========

    >>> from sympy import Symbol, yn, sin, cos, expand_func, besselj, bessely
    >>> z = Symbol("z")
    >>> nu = Symbol("nu", integer=True)
    >>> print(expand_func(yn(0, z)))
    -cos(z)/z
    >>> expand_func(yn(1, z)) == -cos(z)/z**2-sin(z)/z
    True
    >>> yn(nu, z).rewrite(besselj)
    (-1)**(nu + 1)*sqrt(2)*sqrt(pi)*sqrt(1/z)*besselj(-nu - 1/2, z)/2
    >>> yn(nu, z).rewrite(bessely)
    sqrt(2)*sqrt(pi)*sqrt(1/z)*bessely(nu + 1/2, z)/2
    >>> yn(2, 5.2+0.3j).evalf(20)
    0.18525034196069722536 + 0.014895573969924817587*I

    See Also
    ========

    besselj, bessely, besselk, jn

    References
    ==========

    .. [1] https://dlmf.nist.gov/10.47

    '''
class SphericalHankelBase(SphericalBesselBase): ...
class hn1(SphericalHankelBase):
    '''
    Spherical Hankel function of the first kind.

    Explanation
    ===========

    This function is defined as

    .. math:: h_\\nu^(1)(z) = j_\\nu(z) + i y_\\nu(z),

    where $j_\\nu(z)$ and $y_\\nu(z)$ are the spherical
    Bessel function of the first and second kinds.

    For integral orders $n$, $h_n^(1)$ is calculated using the formula:

    .. math:: h_n^(1)(z) = j_{n}(z) + i (-1)^{n+1} j_{-n-1}(z)

    Examples
    ========

    >>> from sympy import Symbol, hn1, hankel1, expand_func, yn, jn
    >>> z = Symbol("z")
    >>> nu = Symbol("nu", integer=True)
    >>> print(expand_func(hn1(nu, z)))
    jn(nu, z) + I*yn(nu, z)
    >>> print(expand_func(hn1(0, z)))
    sin(z)/z - I*cos(z)/z
    >>> print(expand_func(hn1(1, z)))
    -I*sin(z)/z - cos(z)/z + sin(z)/z**2 - I*cos(z)/z**2
    >>> hn1(nu, z).rewrite(jn)
    (-1)**(nu + 1)*I*jn(-nu - 1, z) + jn(nu, z)
    >>> hn1(nu, z).rewrite(yn)
    (-1)**nu*yn(-nu - 1, z) + I*yn(nu, z)
    >>> hn1(nu, z).rewrite(hankel1)
    sqrt(2)*sqrt(pi)*sqrt(1/z)*hankel1(nu, z)/2

    See Also
    ========

    hn2, jn, yn, hankel1, hankel2

    References
    ==========

    .. [1] https://dlmf.nist.gov/10.47

    '''
class hn2(SphericalHankelBase):
    '''
    Spherical Hankel function of the second kind.

    Explanation
    ===========

    This function is defined as

    .. math:: h_\\nu^(2)(z) = j_\\nu(z) - i y_\\nu(z),

    where $j_\\nu(z)$ and $y_\\nu(z)$ are the spherical
    Bessel function of the first and second kinds.

    For integral orders $n$, $h_n^(2)$ is calculated using the formula:

    .. math:: h_n^(2)(z) = j_{n} - i (-1)^{n+1} j_{-n-1}(z)

    Examples
    ========

    >>> from sympy import Symbol, hn2, hankel2, expand_func, jn, yn
    >>> z = Symbol("z")
    >>> nu = Symbol("nu", integer=True)
    >>> print(expand_func(hn2(nu, z)))
    jn(nu, z) - I*yn(nu, z)
    >>> print(expand_func(hn2(0, z)))
    sin(z)/z + I*cos(z)/z
    >>> print(expand_func(hn2(1, z)))
    I*sin(z)/z - cos(z)/z + sin(z)/z**2 + I*cos(z)/z**2
    >>> hn2(nu, z).rewrite(hankel2)
    sqrt(2)*sqrt(pi)*sqrt(1/z)*hankel2(nu, z)/2
    >>> hn2(nu, z).rewrite(jn)
    -(-1)**(nu + 1)*I*jn(-nu - 1, z) + jn(nu, z)
    >>> hn2(nu, z).rewrite(yn)
    (-1)**nu*yn(-nu - 1, z) - I*yn(nu, z)

    See Also
    ========

    hn1, jn, yn, hankel1, hankel2

    References
    ==========

    .. [1] https://dlmf.nist.gov/10.47

    '''

def jn_zeros(n, k, method: str = 'sympy', dps: int = 15):
    '''
    Zeros of the spherical Bessel function of the first kind.

    Explanation
    ===========

    This returns an array of zeros of $jn$ up to the $k$-th zero.

    * method = "sympy": uses `mpmath.besseljzero
      <https://mpmath.org/doc/current/functions/bessel.html#mpmath.besseljzero>`_
    * method = "scipy": uses the
      `SciPy\'s sph_jn <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.jn_zeros.html>`_
      and
      `newton <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html>`_
      to find all
      roots, which is faster than computing the zeros using a general
      numerical solver, but it requires SciPy and only works with low
      precision floating point numbers. (The function used with
      method="sympy" is a recent addition to mpmath; before that a general
      solver was used.)

    Examples
    ========

    >>> from sympy import jn_zeros
    >>> jn_zeros(2, 4, dps=5)
    [5.7635, 9.095, 12.323, 15.515]

    See Also
    ========

    jn, yn, besselj, besselk, bessely

    Parameters
    ==========

    n : integer
        order of Bessel function

    k : integer
        number of zeros to return


    '''

class AiryBase(Function):
    """
    Abstract base class for Airy functions.

    This class is meant to reduce code duplication.

    """
    def as_real_imag(self, deep: bool = True, **hints): ...

class airyai(AiryBase):
    """
    The Airy function $\\operatorname{Ai}$ of the first kind.

    Explanation
    ===========

    The Airy function $\\operatorname{Ai}(z)$ is defined to be the function
    satisfying Airy's differential equation

    .. math::
        \\frac{\\mathrm{d}^2 w(z)}{\\mathrm{d}z^2} - z w(z) = 0.

    Equivalently, for real $z$

    .. math::
        \\operatorname{Ai}(z) := \\frac{1}{\\pi}
        \\int_0^\\infty \\cos\\left(\\frac{t^3}{3} + z t\\right) \\mathrm{d}t.

    Examples
    ========

    Create an Airy function object:

    >>> from sympy import airyai
    >>> from sympy.abc import z

    >>> airyai(z)
    airyai(z)

    Several special values are known:

    >>> airyai(0)
    3**(1/3)/(3*gamma(2/3))
    >>> from sympy import oo
    >>> airyai(oo)
    0
    >>> airyai(-oo)
    0

    The Airy function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(airyai(z))
    airyai(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(airyai(z), z)
    airyaiprime(z)
    >>> diff(airyai(z), z, 2)
    z*airyai(z)

    Series expansion is also supported:

    >>> from sympy import series
    >>> series(airyai(z), z, 0, 3)
    3**(5/6)*gamma(1/3)/(6*pi) - 3**(1/6)*z*gamma(2/3)/(2*pi) + O(z**3)

    We can numerically evaluate the Airy function to arbitrary precision
    on the whole complex plane:

    >>> airyai(-2).evalf(50)
    0.22740742820168557599192443603787379946077222541710

    Rewrite $\\operatorname{Ai}(z)$ in terms of hypergeometric functions:

    >>> from sympy import hyper
    >>> airyai(z).rewrite(hyper)
    -3**(2/3)*z*hyper((), (4/3,), z**3/9)/(3*gamma(1/3)) + 3**(1/3)*hyper((), (2/3,), z**3/9)/(3*gamma(2/3))

    See Also
    ========

    airybi: Airy function of the second kind.
    airyaiprime: Derivative of the Airy function of the first kind.
    airybiprime: Derivative of the Airy function of the second kind.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Airy_function
    .. [2] https://dlmf.nist.gov/9
    .. [3] https://encyclopediaofmath.org/wiki/Airy_functions
    .. [4] https://mathworld.wolfram.com/AiryFunctions.html

    """
    nargs: int
    unbranched: bool
    @classmethod
    def eval(cls, arg): ...
    def fdiff(self, argindex: int = 1): ...
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...

class airybi(AiryBase):
    """
    The Airy function $\\operatorname{Bi}$ of the second kind.

    Explanation
    ===========

    The Airy function $\\operatorname{Bi}(z)$ is defined to be the function
    satisfying Airy's differential equation

    .. math::
        \\frac{\\mathrm{d}^2 w(z)}{\\mathrm{d}z^2} - z w(z) = 0.

    Equivalently, for real $z$

    .. math::
        \\operatorname{Bi}(z) := \\frac{1}{\\pi}
                 \\int_0^\\infty
                   \\exp\\left(-\\frac{t^3}{3} + z t\\right)
                   + \\sin\\left(\\frac{t^3}{3} + z t\\right) \\mathrm{d}t.

    Examples
    ========

    Create an Airy function object:

    >>> from sympy import airybi
    >>> from sympy.abc import z

    >>> airybi(z)
    airybi(z)

    Several special values are known:

    >>> airybi(0)
    3**(5/6)/(3*gamma(2/3))
    >>> from sympy import oo
    >>> airybi(oo)
    oo
    >>> airybi(-oo)
    0

    The Airy function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(airybi(z))
    airybi(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(airybi(z), z)
    airybiprime(z)
    >>> diff(airybi(z), z, 2)
    z*airybi(z)

    Series expansion is also supported:

    >>> from sympy import series
    >>> series(airybi(z), z, 0, 3)
    3**(1/3)*gamma(1/3)/(2*pi) + 3**(2/3)*z*gamma(2/3)/(2*pi) + O(z**3)

    We can numerically evaluate the Airy function to arbitrary precision
    on the whole complex plane:

    >>> airybi(-2).evalf(50)
    -0.41230258795639848808323405461146104203453483447240

    Rewrite $\\operatorname{Bi}(z)$ in terms of hypergeometric functions:

    >>> from sympy import hyper
    >>> airybi(z).rewrite(hyper)
    3**(1/6)*z*hyper((), (4/3,), z**3/9)/gamma(1/3) + 3**(5/6)*hyper((), (2/3,), z**3/9)/(3*gamma(2/3))

    See Also
    ========

    airyai: Airy function of the first kind.
    airyaiprime: Derivative of the Airy function of the first kind.
    airybiprime: Derivative of the Airy function of the second kind.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Airy_function
    .. [2] https://dlmf.nist.gov/9
    .. [3] https://encyclopediaofmath.org/wiki/Airy_functions
    .. [4] https://mathworld.wolfram.com/AiryFunctions.html

    """
    nargs: int
    unbranched: bool
    @classmethod
    def eval(cls, arg): ...
    def fdiff(self, argindex: int = 1): ...
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...

class airyaiprime(AiryBase):
    """
    The derivative $\\operatorname{Ai}^\\prime$ of the Airy function of the first
    kind.

    Explanation
    ===========

    The Airy function $\\operatorname{Ai}^\\prime(z)$ is defined to be the
    function

    .. math::
        \\operatorname{Ai}^\\prime(z) := \\frac{\\mathrm{d} \\operatorname{Ai}(z)}{\\mathrm{d} z}.

    Examples
    ========

    Create an Airy function object:

    >>> from sympy import airyaiprime
    >>> from sympy.abc import z

    >>> airyaiprime(z)
    airyaiprime(z)

    Several special values are known:

    >>> airyaiprime(0)
    -3**(2/3)/(3*gamma(1/3))
    >>> from sympy import oo
    >>> airyaiprime(oo)
    0

    The Airy function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(airyaiprime(z))
    airyaiprime(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(airyaiprime(z), z)
    z*airyai(z)
    >>> diff(airyaiprime(z), z, 2)
    z*airyaiprime(z) + airyai(z)

    Series expansion is also supported:

    >>> from sympy import series
    >>> series(airyaiprime(z), z, 0, 3)
    -3**(2/3)/(3*gamma(1/3)) + 3**(1/3)*z**2/(6*gamma(2/3)) + O(z**3)

    We can numerically evaluate the Airy function to arbitrary precision
    on the whole complex plane:

    >>> airyaiprime(-2).evalf(50)
    0.61825902074169104140626429133247528291577794512415

    Rewrite $\\operatorname{Ai}^\\prime(z)$ in terms of hypergeometric functions:

    >>> from sympy import hyper
    >>> airyaiprime(z).rewrite(hyper)
    3**(1/3)*z**2*hyper((), (5/3,), z**3/9)/(6*gamma(2/3)) - 3**(2/3)*hyper((), (1/3,), z**3/9)/(3*gamma(1/3))

    See Also
    ========

    airyai: Airy function of the first kind.
    airybi: Airy function of the second kind.
    airybiprime: Derivative of the Airy function of the second kind.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Airy_function
    .. [2] https://dlmf.nist.gov/9
    .. [3] https://encyclopediaofmath.org/wiki/Airy_functions
    .. [4] https://mathworld.wolfram.com/AiryFunctions.html

    """
    nargs: int
    unbranched: bool
    @classmethod
    def eval(cls, arg): ...
    def fdiff(self, argindex: int = 1): ...

class airybiprime(AiryBase):
    """
    The derivative $\\operatorname{Bi}^\\prime$ of the Airy function of the first
    kind.

    Explanation
    ===========

    The Airy function $\\operatorname{Bi}^\\prime(z)$ is defined to be the
    function

    .. math::
        \\operatorname{Bi}^\\prime(z) := \\frac{\\mathrm{d} \\operatorname{Bi}(z)}{\\mathrm{d} z}.

    Examples
    ========

    Create an Airy function object:

    >>> from sympy import airybiprime
    >>> from sympy.abc import z

    >>> airybiprime(z)
    airybiprime(z)

    Several special values are known:

    >>> airybiprime(0)
    3**(1/6)/gamma(1/3)
    >>> from sympy import oo
    >>> airybiprime(oo)
    oo
    >>> airybiprime(-oo)
    0

    The Airy function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(airybiprime(z))
    airybiprime(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(airybiprime(z), z)
    z*airybi(z)
    >>> diff(airybiprime(z), z, 2)
    z*airybiprime(z) + airybi(z)

    Series expansion is also supported:

    >>> from sympy import series
    >>> series(airybiprime(z), z, 0, 3)
    3**(1/6)/gamma(1/3) + 3**(5/6)*z**2/(6*gamma(2/3)) + O(z**3)

    We can numerically evaluate the Airy function to arbitrary precision
    on the whole complex plane:

    >>> airybiprime(-2).evalf(50)
    0.27879516692116952268509756941098324140300059345163

    Rewrite $\\operatorname{Bi}^\\prime(z)$ in terms of hypergeometric functions:

    >>> from sympy import hyper
    >>> airybiprime(z).rewrite(hyper)
    3**(5/6)*z**2*hyper((), (5/3,), z**3/9)/(6*gamma(2/3)) + 3**(1/6)*hyper((), (1/3,), z**3/9)/gamma(1/3)

    See Also
    ========

    airyai: Airy function of the first kind.
    airybi: Airy function of the second kind.
    airyaiprime: Derivative of the Airy function of the first kind.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Airy_function
    .. [2] https://dlmf.nist.gov/9
    .. [3] https://encyclopediaofmath.org/wiki/Airy_functions
    .. [4] https://mathworld.wolfram.com/AiryFunctions.html

    """
    nargs: int
    unbranched: bool
    @classmethod
    def eval(cls, arg): ...
    def fdiff(self, argindex: int = 1): ...

class marcumq(Function):
    """
    The Marcum Q-function.

    Explanation
    ===========

    The Marcum Q-function is defined by the meromorphic continuation of

    .. math::
        Q_m(a, b) = a^{- m + 1} \\int_{b}^{\\infty} x^{m} e^{- \\frac{a^{2}}{2} - \\frac{x^{2}}{2}} I_{m - 1}\\left(a x\\right)\\, dx

    Examples
    ========

    >>> from sympy import marcumq
    >>> from sympy.abc import m, a, b
    >>> marcumq(m, a, b)
    marcumq(m, a, b)

    Special values:

    >>> marcumq(m, 0, b)
    uppergamma(m, b**2/2)/gamma(m)
    >>> marcumq(0, 0, 0)
    0
    >>> marcumq(0, a, 0)
    1 - exp(-a**2/2)
    >>> marcumq(1, a, a)
    1/2 + exp(-a**2)*besseli(0, a**2)/2
    >>> marcumq(2, a, a)
    1/2 + exp(-a**2)*besseli(0, a**2)/2 + exp(-a**2)*besseli(1, a**2)

    Differentiation with respect to $a$ and $b$ is supported:

    >>> from sympy import diff
    >>> diff(marcumq(m, a, b), a)
    a*(-marcumq(m, a, b) + marcumq(m + 1, a, b))
    >>> diff(marcumq(m, a, b), b)
    -a**(1 - m)*b**m*exp(-a**2/2 - b**2/2)*besseli(m - 1, a*b)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Marcum_Q-function
    .. [2] https://mathworld.wolfram.com/MarcumQ-Function.html

    """
    @classmethod
    def eval(cls, m, a, b): ...
    def fdiff(self, argindex: int = 2): ...
