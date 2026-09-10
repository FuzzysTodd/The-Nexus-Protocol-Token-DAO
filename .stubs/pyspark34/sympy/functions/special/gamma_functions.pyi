from sympy.core import Add as Add, Dummy as Dummy, S as S, expand_func as expand_func
from sympy.core.expr import Expr as Expr
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, PoleError as PoleError
from sympy.core.logic import fuzzy_and as fuzzy_and, fuzzy_not as fuzzy_not
from sympy.core.numbers import I as I, Rational as Rational, oo as oo, pi as pi
from sympy.core.power import Pow as Pow
from sympy.functions.combinatorial.factorials import RisingFactorial as RisingFactorial, factorial as factorial, rf as rf
from sympy.functions.combinatorial.numbers import bernoulli as bernoulli, harmonic as harmonic
from sympy.functions.elementary.complexes import re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, log as log
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, cot as cot, sin as sin
from sympy.functions.special.error_functions import Ei as Ei, erf as erf, erfc as erfc
from sympy.functions.special.zeta_functions import zeta as zeta
from sympy.utilities.misc import as_int as as_int

def intlike(n): ...

class gamma(Function):
    """
    The gamma function

    .. math::
        \\Gamma(x) := \\int^{\\infty}_{0} t^{x-1} e^{-t} \\mathrm{d}t.

    Explanation
    ===========

    The ``gamma`` function implements the function which passes through the
    values of the factorial function (i.e., $\\Gamma(n) = (n - 1)!$ when n is
    an integer). More generally, $\\Gamma(z)$ is defined in the whole complex
    plane except at the negative integers where there are simple poles.

    Examples
    ========

    >>> from sympy import S, I, pi, gamma
    >>> from sympy.abc import x

    Several special values are known:

    >>> gamma(1)
    1
    >>> gamma(4)
    6
    >>> gamma(S(3)/2)
    sqrt(pi)/2

    The ``gamma`` function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(gamma(x))
    gamma(conjugate(x))

    Differentiation with respect to $x$ is supported:

    >>> from sympy import diff
    >>> diff(gamma(x), x)
    gamma(x)*polygamma(0, x)

    Series expansion is also supported:

    >>> from sympy import series
    >>> series(gamma(x), x, 0, 3)
    1/x - EulerGamma + x*(EulerGamma**2/2 + pi**2/12) + x**2*(-EulerGamma*pi**2/12 - zeta(3)/3 - EulerGamma**3/6) + O(x**3)

    We can numerically evaluate the ``gamma`` function to arbitrary precision
    on the whole complex plane:

    >>> gamma(pi).evalf(40)
    2.288037795340032417959588909060233922890
    >>> gamma(1+I).evalf(20)
    0.49801566811835604271 - 0.15494982830181068512*I

    See Also
    ========

    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gamma_function
    .. [2] https://dlmf.nist.gov/5
    .. [3] https://mathworld.wolfram.com/GammaFunction.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/Gamma/

    """
    unbranched: bool
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, arg): ...

class lowergamma(Function):
    """
    The lower incomplete gamma function.

    Explanation
    ===========

    It can be defined as the meromorphic continuation of

    .. math::
        \\gamma(s, x) := \\int_0^x t^{s-1} e^{-t} \\mathrm{d}t = \\Gamma(s) - \\Gamma(s, x).

    This can be shown to be the same as

    .. math::
        \\gamma(s, x) = \\frac{x^s}{s} {}_1F_1\\left({s \\atop s+1} \\middle| -x\\right),

    where ${}_1F_1$ is the (confluent) hypergeometric function.

    Examples
    ========

    >>> from sympy import lowergamma, S
    >>> from sympy.abc import s, x
    >>> lowergamma(s, x)
    lowergamma(s, x)
    >>> lowergamma(3, x)
    -2*(x**2/2 + x + 1)*exp(-x) + 2
    >>> lowergamma(-S(1)/2, x)
    -2*sqrt(pi)*erf(sqrt(x)) - 2*exp(-x)/sqrt(x)

    See Also
    ========

    gamma: Gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Incomplete_gamma_function#Lower_incomplete_gamma_function
    .. [2] Abramowitz, Milton; Stegun, Irene A., eds. (1965), Chapter 6,
           Section 5, Handbook of Mathematical Functions with Formulas, Graphs,
           and Mathematical Tables
    .. [3] https://dlmf.nist.gov/8
    .. [4] https://functions.wolfram.com/GammaBetaErf/Gamma2/
    .. [5] https://functions.wolfram.com/GammaBetaErf/Gamma3/

    """
    def fdiff(self, argindex: int = 2): ...
    @classmethod
    def eval(cls, a, x): ...

class uppergamma(Function):
    """
    The upper incomplete gamma function.

    Explanation
    ===========

    It can be defined as the meromorphic continuation of

    .. math::
        \\Gamma(s, x) := \\int_x^\\infty t^{s-1} e^{-t} \\mathrm{d}t = \\Gamma(s) - \\gamma(s, x).

    where $\\gamma(s, x)$ is the lower incomplete gamma function,
    :class:`lowergamma`. This can be shown to be the same as

    .. math::
        \\Gamma(s, x) = \\Gamma(s) - \\frac{x^s}{s} {}_1F_1\\left({s \\atop s+1} \\middle| -x\\right),

    where ${}_1F_1$ is the (confluent) hypergeometric function.

    The upper incomplete gamma function is also essentially equivalent to the
    generalized exponential integral:

    .. math::
        \\operatorname{E}_{n}(x) = \\int_{1}^{\\infty}{\\frac{e^{-xt}}{t^n} \\, dt} = x^{n-1}\\Gamma(1-n,x).

    Examples
    ========

    >>> from sympy import uppergamma, S
    >>> from sympy.abc import s, x
    >>> uppergamma(s, x)
    uppergamma(s, x)
    >>> uppergamma(3, x)
    2*(x**2/2 + x + 1)*exp(-x)
    >>> uppergamma(-S(1)/2, x)
    -2*sqrt(pi)*erfc(sqrt(x)) + 2*exp(-x)/sqrt(x)
    >>> uppergamma(-2, x)
    expint(3, x)/x**2

    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Incomplete_gamma_function#Upper_incomplete_gamma_function
    .. [2] Abramowitz, Milton; Stegun, Irene A., eds. (1965), Chapter 6,
           Section 5, Handbook of Mathematical Functions with Formulas, Graphs,
           and Mathematical Tables
    .. [3] https://dlmf.nist.gov/8
    .. [4] https://functions.wolfram.com/GammaBetaErf/Gamma2/
    .. [5] https://functions.wolfram.com/GammaBetaErf/Gamma3/
    .. [6] https://en.wikipedia.org/wiki/Exponential_integral#Relation_with_other_functions

    """
    def fdiff(self, argindex: int = 2): ...
    @classmethod
    def eval(cls, a, z): ...

class polygamma(Function):
    '''
    The function ``polygamma(n, z)`` returns ``log(gamma(z)).diff(n + 1)``.

    Explanation
    ===========

    It is a meromorphic function on $\\mathbb{C}$ and defined as the $(n+1)$-th
    derivative of the logarithm of the gamma function:

    .. math::
        \\psi^{(n)} (z) := \\frac{\\mathrm{d}^{n+1}}{\\mathrm{d} z^{n+1}} \\log\\Gamma(z).

    For `n` not a nonnegative integer the generalization by Espinosa and Moll [5]_
    is used:

    .. math:: \\psi(s,z) = \\frac{\\zeta\'(s+1, z) + (\\gamma + \\psi(-s)) \\zeta(s+1, z)}
        {\\Gamma(-s)}

    Examples
    ========

    Several special values are known:

    >>> from sympy import S, polygamma
    >>> polygamma(0, 1)
    -EulerGamma
    >>> polygamma(0, 1/S(2))
    -2*log(2) - EulerGamma
    >>> polygamma(0, 1/S(3))
    -log(3) - sqrt(3)*pi/6 - EulerGamma - log(sqrt(3))
    >>> polygamma(0, 1/S(4))
    -pi/2 - log(4) - log(2) - EulerGamma
    >>> polygamma(0, 2)
    1 - EulerGamma
    >>> polygamma(0, 23)
    19093197/5173168 - EulerGamma

    >>> from sympy import oo, I
    >>> polygamma(0, oo)
    oo
    >>> polygamma(0, -oo)
    oo
    >>> polygamma(0, I*oo)
    oo
    >>> polygamma(0, -I*oo)
    oo

    Differentiation with respect to $x$ is supported:

    >>> from sympy import Symbol, diff
    >>> x = Symbol("x")
    >>> diff(polygamma(0, x), x)
    polygamma(1, x)
    >>> diff(polygamma(0, x), x, 2)
    polygamma(2, x)
    >>> diff(polygamma(0, x), x, 3)
    polygamma(3, x)
    >>> diff(polygamma(1, x), x)
    polygamma(2, x)
    >>> diff(polygamma(1, x), x, 2)
    polygamma(3, x)
    >>> diff(polygamma(2, x), x)
    polygamma(3, x)
    >>> diff(polygamma(2, x), x, 2)
    polygamma(4, x)

    >>> n = Symbol("n")
    >>> diff(polygamma(n, x), x)
    polygamma(n + 1, x)
    >>> diff(polygamma(n, x), x, 2)
    polygamma(n + 2, x)

    We can rewrite ``polygamma`` functions in terms of harmonic numbers:

    >>> from sympy import harmonic
    >>> polygamma(0, x).rewrite(harmonic)
    harmonic(x - 1) - EulerGamma
    >>> polygamma(2, x).rewrite(harmonic)
    2*harmonic(x - 1, 3) - 2*zeta(3)
    >>> ni = Symbol("n", integer=True)
    >>> polygamma(ni, x).rewrite(harmonic)
    (-1)**(n + 1)*(-harmonic(x - 1, n + 1) + zeta(n + 1))*factorial(n)

    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Polygamma_function
    .. [2] https://mathworld.wolfram.com/PolygammaFunction.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/PolyGamma/
    .. [4] https://functions.wolfram.com/GammaBetaErf/PolyGamma2/
    .. [5] O. Espinosa and V. Moll, "A generalized polygamma function",
           *Integral Transforms and Special Functions* (2004), 101-115.

    '''
    @classmethod
    def eval(cls, n, z): ...
    def fdiff(self, argindex: int = 2): ...

class loggamma(Function):
    '''
    The ``loggamma`` function implements the logarithm of the
    gamma function (i.e., $\\log\\Gamma(x)$).

    Examples
    ========

    Several special values are known. For numerical integral
    arguments we have:

    >>> from sympy import loggamma
    >>> loggamma(-2)
    oo
    >>> loggamma(0)
    oo
    >>> loggamma(1)
    0
    >>> loggamma(2)
    0
    >>> loggamma(3)
    log(2)

    And for symbolic values:

    >>> from sympy import Symbol
    >>> n = Symbol("n", integer=True, positive=True)
    >>> loggamma(n)
    log(gamma(n))
    >>> loggamma(-n)
    oo

    For half-integral values:

    >>> from sympy import S
    >>> loggamma(S(5)/2)
    log(3*sqrt(pi)/4)
    >>> loggamma(n/2)
    log(2**(1 - n)*sqrt(pi)*gamma(n)/gamma(n/2 + 1/2))

    And general rational arguments:

    >>> from sympy import expand_func
    >>> L = loggamma(S(16)/3)
    >>> expand_func(L).doit()
    -5*log(3) + loggamma(1/3) + log(4) + log(7) + log(10) + log(13)
    >>> L = loggamma(S(19)/4)
    >>> expand_func(L).doit()
    -4*log(4) + loggamma(3/4) + log(3) + log(7) + log(11) + log(15)
    >>> L = loggamma(S(23)/7)
    >>> expand_func(L).doit()
    -3*log(7) + log(2) + loggamma(2/7) + log(9) + log(16)

    The ``loggamma`` function has the following limits towards infinity:

    >>> from sympy import oo
    >>> loggamma(oo)
    oo
    >>> loggamma(-oo)
    zoo

    The ``loggamma`` function obeys the mirror symmetry
    if $x \\in \\mathbb{C} \\setminus \\{-\\infty, 0\\}$:

    >>> from sympy.abc import x
    >>> from sympy import conjugate
    >>> conjugate(loggamma(x))
    loggamma(conjugate(x))

    Differentiation with respect to $x$ is supported:

    >>> from sympy import diff
    >>> diff(loggamma(x), x)
    polygamma(0, x)

    Series expansion is also supported:

    >>> from sympy import series
    >>> series(loggamma(x), x, 0, 4).cancel()
    -log(x) - EulerGamma*x + pi**2*x**2/12 - x**3*zeta(3)/3 + O(x**4)

    We can numerically evaluate the ``loggamma`` function
    to arbitrary precision on the whole complex plane:

    >>> from sympy import I
    >>> loggamma(5).evalf(30)
    3.17805383034794561964694160130
    >>> loggamma(I).evalf(20)
    -0.65092319930185633889 - 1.8724366472624298171*I

    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    digamma: Digamma function.
    trigamma: Trigamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gamma_function
    .. [2] https://dlmf.nist.gov/5
    .. [3] https://mathworld.wolfram.com/LogGammaFunction.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/LogGamma/

    '''
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...

class digamma(Function):
    """
    The ``digamma`` function is the first derivative of the ``loggamma``
    function

    .. math::
        \\psi(x) := \\frac{\\mathrm{d}}{\\mathrm{d} z} \\log\\Gamma(z)
                = \\frac{\\Gamma'(z)}{\\Gamma(z) }.

    In this case, ``digamma(z) = polygamma(0, z)``.

    Examples
    ========

    >>> from sympy import digamma
    >>> digamma(0)
    zoo
    >>> from sympy import Symbol
    >>> z = Symbol('z')
    >>> digamma(z)
    polygamma(0, z)

    To retain ``digamma`` as it is:

    >>> digamma(0, evaluate=False)
    digamma(0)
    >>> digamma(z, evaluate=False)
    digamma(z)

    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    trigamma: Trigamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Digamma_function
    .. [2] https://mathworld.wolfram.com/DigammaFunction.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/PolyGamma2/

    """
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, z): ...

class trigamma(Function):
    """
    The ``trigamma`` function is the second derivative of the ``loggamma``
    function

    .. math::
        \\psi^{(1)}(z) := \\frac{\\mathrm{d}^{2}}{\\mathrm{d} z^{2}} \\log\\Gamma(z).

    In this case, ``trigamma(z) = polygamma(1, z)``.

    Examples
    ========

    >>> from sympy import trigamma
    >>> trigamma(0)
    zoo
    >>> from sympy import Symbol
    >>> z = Symbol('z')
    >>> trigamma(z)
    polygamma(1, z)

    To retain ``trigamma`` as it is:

    >>> trigamma(0, evaluate=False)
    trigamma(0)
    >>> trigamma(z, evaluate=False)
    trigamma(z)


    See Also
    ========

    gamma: Gamma function.
    lowergamma: Lower incomplete gamma function.
    uppergamma: Upper incomplete gamma function.
    polygamma: Polygamma function.
    loggamma: Log Gamma function.
    digamma: Digamma function.
    beta: Euler Beta function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigamma_function
    .. [2] https://mathworld.wolfram.com/TrigammaFunction.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/PolyGamma2/

    """
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, z): ...

class multigamma(Function):
    """
    The multivariate gamma function is a generalization of the gamma function

    .. math::
        \\Gamma_p(z) = \\pi^{p(p-1)/4}\\prod_{k=1}^p \\Gamma[z + (1 - k)/2].

    In a special case, ``multigamma(x, 1) = gamma(x)``.

    Examples
    ========

    >>> from sympy import S, multigamma
    >>> from sympy import Symbol
    >>> x = Symbol('x')
    >>> p = Symbol('p', positive=True, integer=True)

    >>> multigamma(x, p)
    pi**(p*(p - 1)/4)*Product(gamma(-_k/2 + x + 1/2), (_k, 1, p))

    Several special values are known:

    >>> multigamma(1, 1)
    1
    >>> multigamma(4, 1)
    6
    >>> multigamma(S(3)/2, 1)
    sqrt(pi)/2

    Writing ``multigamma`` in terms of the ``gamma`` function:

    >>> multigamma(x, 1)
    gamma(x)

    >>> multigamma(x, 2)
    sqrt(pi)*gamma(x)*gamma(x - 1/2)

    >>> multigamma(x, 3)
    pi**(3/2)*gamma(x)*gamma(x - 1)*gamma(x - 1/2)

    Parameters
    ==========

    p : order or dimension of the multivariate gamma function

    See Also
    ========

    gamma, lowergamma, uppergamma, polygamma, loggamma, digamma, trigamma,
    beta

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Multivariate_gamma_function

    """
    unbranched: bool
    def fdiff(self, argindex: int = 2): ...
    @classmethod
    def eval(cls, x, p): ...
