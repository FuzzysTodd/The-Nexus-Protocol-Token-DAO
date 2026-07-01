from sympy.core import EulerGamma as EulerGamma
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, expand_mul as expand_mul
from sympy.core.numbers import I as I, Rational as Rational, pi as pi
from sympy.core.power import Pow as Pow
from sympy.core.relational import is_eq as is_eq
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import RisingFactorial as RisingFactorial, factorial as factorial, factorial2 as factorial2
from sympy.functions.elementary.complexes import polar_lift as polar_lift, re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, exp_polar as exp_polar, log as log
from sympy.functions.elementary.hyperbolic import cosh as cosh, sinh as sinh
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.miscellaneous import root as root, sqrt as sqrt
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin, sinc as sinc
from sympy.functions.special.hyper import hyper as hyper, meijerg as meijerg

def real_to_real_as_real_imag(self, deep: bool = True, **hints): ...

class erf(Function):
    """
    The Gauss error function.

    Explanation
    ===========

    This function is defined as:

    .. math ::
        \\mathrm{erf}(x) = \\frac{2}{\\sqrt{\\pi}} \\int_0^x e^{-t^2} \\mathrm{d}t.

    Examples
    ========

    >>> from sympy import I, oo, erf
    >>> from sympy.abc import z

    Several special values are known:

    >>> erf(0)
    0
    >>> erf(oo)
    1
    >>> erf(-oo)
    -1
    >>> erf(I*oo)
    oo*I
    >>> erf(-I*oo)
    -oo*I

    In general one can pull out factors of -1 and $I$ from the argument:

    >>> erf(-z)
    -erf(z)

    The error function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(erf(z))
    erf(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(erf(z), z)
    2*exp(-z**2)/sqrt(pi)

    We can numerically evaluate the error function to arbitrary precision
    on the whole complex plane:

    >>> erf(4).evalf(30)
    0.999999984582742099719981147840

    >>> erf(-4*I).evalf(30)
    -1296959.73071763923152794095062*I

    See Also
    ========

    erfc: Complementary error function.
    erfi: Imaginary error function.
    erf2: Two-argument error function.
    erfinv: Inverse error function.
    erfcinv: Inverse Complementary error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Error_function
    .. [2] https://dlmf.nist.gov/7
    .. [3] https://mathworld.wolfram.com/Erf.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/Erf

    """
    unbranched: bool
    def fdiff(self, argindex: int = 1): ...
    def inverse(self, argindex: int = 1):
        """
        Returns the inverse of this function.

        """
    @classmethod
    def eval(cls, arg): ...
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...
    as_real_imag = real_to_real_as_real_imag

class erfc(Function):
    """
    Complementary Error Function.

    Explanation
    ===========

    The function is defined as:

    .. math ::
        \\mathrm{erfc}(x) = \\frac{2}{\\sqrt{\\pi}} \\int_x^\\infty e^{-t^2} \\mathrm{d}t

    Examples
    ========

    >>> from sympy import I, oo, erfc
    >>> from sympy.abc import z

    Several special values are known:

    >>> erfc(0)
    1
    >>> erfc(oo)
    0
    >>> erfc(-oo)
    2
    >>> erfc(I*oo)
    -oo*I
    >>> erfc(-I*oo)
    oo*I

    The error function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(erfc(z))
    erfc(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(erfc(z), z)
    -2*exp(-z**2)/sqrt(pi)

    It also follows

    >>> erfc(-z)
    2 - erfc(z)

    We can numerically evaluate the complementary error function to arbitrary
    precision on the whole complex plane:

    >>> erfc(4).evalf(30)
    0.0000000154172579002800188521596734869

    >>> erfc(4*I).evalf(30)
    1.0 - 1296959.73071763923152794095062*I

    See Also
    ========

    erf: Gaussian error function.
    erfi: Imaginary error function.
    erf2: Two-argument error function.
    erfinv: Inverse error function.
    erfcinv: Inverse Complementary error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Error_function
    .. [2] https://dlmf.nist.gov/7
    .. [3] https://mathworld.wolfram.com/Erfc.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/Erfc

    """
    unbranched: bool
    def fdiff(self, argindex: int = 1): ...
    def inverse(self, argindex: int = 1):
        """
        Returns the inverse of this function.

        """
    @classmethod
    def eval(cls, arg): ...
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...
    as_real_imag = real_to_real_as_real_imag

class erfi(Function):
    """
    Imaginary error function.

    Explanation
    ===========

    The function erfi is defined as:

    .. math ::
        \\mathrm{erfi}(x) = \\frac{2}{\\sqrt{\\pi}} \\int_0^x e^{t^2} \\mathrm{d}t

    Examples
    ========

    >>> from sympy import I, oo, erfi
    >>> from sympy.abc import z

    Several special values are known:

    >>> erfi(0)
    0
    >>> erfi(oo)
    oo
    >>> erfi(-oo)
    -oo
    >>> erfi(I*oo)
    I
    >>> erfi(-I*oo)
    -I

    In general one can pull out factors of -1 and $I$ from the argument:

    >>> erfi(-z)
    -erfi(z)

    >>> from sympy import conjugate
    >>> conjugate(erfi(z))
    erfi(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(erfi(z), z)
    2*exp(z**2)/sqrt(pi)

    We can numerically evaluate the imaginary error function to arbitrary
    precision on the whole complex plane:

    >>> erfi(2).evalf(30)
    18.5648024145755525987042919132

    >>> erfi(-2*I).evalf(30)
    -0.995322265018952734162069256367*I

    See Also
    ========

    erf: Gaussian error function.
    erfc: Complementary error function.
    erf2: Two-argument error function.
    erfinv: Inverse error function.
    erfcinv: Inverse Complementary error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Error_function
    .. [2] https://mathworld.wolfram.com/Erfi.html
    .. [3] https://functions.wolfram.com/GammaBetaErf/Erfi

    """
    unbranched: bool
    def fdiff(self, argindex: int = 1): ...
    @classmethod
    def eval(cls, z): ...
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...
    as_real_imag = real_to_real_as_real_imag

class erf2(Function):
    """
    Two-argument error function.

    Explanation
    ===========

    This function is defined as:

    .. math ::
        \\mathrm{erf2}(x, y) = \\frac{2}{\\sqrt{\\pi}} \\int_x^y e^{-t^2} \\mathrm{d}t

    Examples
    ========

    >>> from sympy import oo, erf2
    >>> from sympy.abc import x, y

    Several special values are known:

    >>> erf2(0, 0)
    0
    >>> erf2(x, x)
    0
    >>> erf2(x, oo)
    1 - erf(x)
    >>> erf2(x, -oo)
    -erf(x) - 1
    >>> erf2(oo, y)
    erf(y) - 1
    >>> erf2(-oo, y)
    erf(y) + 1

    In general one can pull out factors of -1:

    >>> erf2(-x, -y)
    -erf2(x, y)

    The error function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(erf2(x, y))
    erf2(conjugate(x), conjugate(y))

    Differentiation with respect to $x$, $y$ is supported:

    >>> from sympy import diff
    >>> diff(erf2(x, y), x)
    -2*exp(-x**2)/sqrt(pi)
    >>> diff(erf2(x, y), y)
    2*exp(-y**2)/sqrt(pi)

    See Also
    ========

    erf: Gaussian error function.
    erfc: Complementary error function.
    erfi: Imaginary error function.
    erfinv: Inverse error function.
    erfcinv: Inverse Complementary error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://functions.wolfram.com/GammaBetaErf/Erf2/

    """
    def fdiff(self, argindex): ...
    @classmethod
    def eval(cls, x, y): ...

class erfinv(Function):
    """
    Inverse Error Function. The erfinv function is defined as:

    .. math ::
        \\mathrm{erf}(x) = y \\quad \\Rightarrow \\quad \\mathrm{erfinv}(y) = x

    Examples
    ========

    >>> from sympy import erfinv
    >>> from sympy.abc import x

    Several special values are known:

    >>> erfinv(0)
    0
    >>> erfinv(1)
    oo

    Differentiation with respect to $x$ is supported:

    >>> from sympy import diff
    >>> diff(erfinv(x), x)
    sqrt(pi)*exp(erfinv(x)**2)/2

    We can numerically evaluate the inverse error function to arbitrary
    precision on [-1, 1]:

    >>> erfinv(0.2).evalf(30)
    0.179143454621291692285822705344

    See Also
    ========

    erf: Gaussian error function.
    erfc: Complementary error function.
    erfi: Imaginary error function.
    erf2: Two-argument error function.
    erfcinv: Inverse Complementary error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Error_function#Inverse_functions
    .. [2] https://functions.wolfram.com/GammaBetaErf/InverseErf/

    """
    def fdiff(self, argindex: int = 1): ...
    def inverse(self, argindex: int = 1):
        """
        Returns the inverse of this function.

        """
    @classmethod
    def eval(cls, z): ...

class erfcinv(Function):
    """
    Inverse Complementary Error Function. The erfcinv function is defined as:

    .. math ::
        \\mathrm{erfc}(x) = y \\quad \\Rightarrow \\quad \\mathrm{erfcinv}(y) = x

    Examples
    ========

    >>> from sympy import erfcinv
    >>> from sympy.abc import x

    Several special values are known:

    >>> erfcinv(1)
    0
    >>> erfcinv(0)
    oo

    Differentiation with respect to $x$ is supported:

    >>> from sympy import diff
    >>> diff(erfcinv(x), x)
    -sqrt(pi)*exp(erfcinv(x)**2)/2

    See Also
    ========

    erf: Gaussian error function.
    erfc: Complementary error function.
    erfi: Imaginary error function.
    erf2: Two-argument error function.
    erfinv: Inverse error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Error_function#Inverse_functions
    .. [2] https://functions.wolfram.com/GammaBetaErf/InverseErfc/

    """
    def fdiff(self, argindex: int = 1): ...
    def inverse(self, argindex: int = 1):
        """
        Returns the inverse of this function.

        """
    @classmethod
    def eval(cls, z): ...

class erf2inv(Function):
    """
    Two-argument Inverse error function. The erf2inv function is defined as:

    .. math ::
        \\mathrm{erf2}(x, w) = y \\quad \\Rightarrow \\quad \\mathrm{erf2inv}(x, y) = w

    Examples
    ========

    >>> from sympy import erf2inv, oo
    >>> from sympy.abc import x, y

    Several special values are known:

    >>> erf2inv(0, 0)
    0
    >>> erf2inv(1, 0)
    1
    >>> erf2inv(0, 1)
    oo
    >>> erf2inv(0, y)
    erfinv(y)
    >>> erf2inv(oo, y)
    erfcinv(-y)

    Differentiation with respect to $x$ and $y$ is supported:

    >>> from sympy import diff
    >>> diff(erf2inv(x, y), x)
    exp(-x**2 + erf2inv(x, y)**2)
    >>> diff(erf2inv(x, y), y)
    sqrt(pi)*exp(erf2inv(x, y)**2)/2

    See Also
    ========

    erf: Gaussian error function.
    erfc: Complementary error function.
    erfi: Imaginary error function.
    erf2: Two-argument error function.
    erfinv: Inverse error function.
    erfcinv: Inverse complementary error function.

    References
    ==========

    .. [1] https://functions.wolfram.com/GammaBetaErf/InverseErf2/

    """
    def fdiff(self, argindex): ...
    @classmethod
    def eval(cls, x, y): ...

class Ei(Function):
    """
    The classical exponential integral.

    Explanation
    ===========

    For use in SymPy, this function is defined as

    .. math:: \\operatorname{Ei}(x) = \\sum_{n=1}^\\infty \\frac{x^n}{n\\, n!}
                                     + \\log(x) + \\gamma,

    where $\\gamma$ is the Euler-Mascheroni constant.

    If $x$ is a polar number, this defines an analytic function on the
    Riemann surface of the logarithm. Otherwise this defines an analytic
    function in the cut plane $\\mathbb{C} \\setminus (-\\infty, 0]$.

    **Background**

    The name exponential integral comes from the following statement:

    .. math:: \\operatorname{Ei}(x) = \\int_{-\\infty}^x \\frac{e^t}{t} \\mathrm{d}t

    If the integral is interpreted as a Cauchy principal value, this statement
    holds for $x > 0$ and $\\operatorname{Ei}(x)$ as defined above.

    Examples
    ========

    >>> from sympy import Ei, polar_lift, exp_polar, I, pi
    >>> from sympy.abc import x

    >>> Ei(-1)
    Ei(-1)

    This yields a real value:

    >>> Ei(-1).n(chop=True)
    -0.219383934395520

    On the other hand the analytic continuation is not real:

    >>> Ei(polar_lift(-1)).n(chop=True)
    -0.21938393439552 + 3.14159265358979*I

    The exponential integral has a logarithmic branch point at the origin:

    >>> Ei(x*exp_polar(2*I*pi))
    Ei(x) + 2*I*pi

    Differentiation is supported:

    >>> Ei(x).diff(x)
    exp(x)/x

    The exponential integral is related to many other special functions.
    For example:

    >>> from sympy import expint, Shi
    >>> Ei(x).rewrite(expint)
    -expint(1, x*exp_polar(I*pi)) - I*pi
    >>> Ei(x).rewrite(Shi)
    Chi(x) + Shi(x)

    See Also
    ========

    expint: Generalised exponential integral.
    E1: Special case of the generalised exponential integral.
    li: Logarithmic integral.
    Li: Offset logarithmic integral.
    Si: Sine integral.
    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.
    uppergamma: Upper incomplete gamma function.

    References
    ==========

    .. [1] https://dlmf.nist.gov/6.6
    .. [2] https://en.wikipedia.org/wiki/Exponential_integral
    .. [3] Abramowitz & Stegun, section 5: https://web.archive.org/web/20201128173312/http://people.math.sfu.ca/~cbm/aands/page_228.htm

    """
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...

class expint(Function):
    """
    Generalized exponential integral.

    Explanation
    ===========

    This function is defined as

    .. math:: \\operatorname{E}_\\nu(z) = z^{\\nu - 1} \\Gamma(1 - \\nu, z),

    where $\\Gamma(1 - \\nu, z)$ is the upper incomplete gamma function
    (``uppergamma``).

    Hence for $z$ with positive real part we have

    .. math:: \\operatorname{E}_\\nu(z)
              =   \\int_1^\\infty \\frac{e^{-zt}}{t^\\nu} \\mathrm{d}t,

    which explains the name.

    The representation as an incomplete gamma function provides an analytic
    continuation for $\\operatorname{E}_\\nu(z)$. If $\\nu$ is a
    non-positive integer, the exponential integral is thus an unbranched
    function of $z$, otherwise there is a branch point at the origin.
    Refer to the incomplete gamma function documentation for details of the
    branching behavior.

    Examples
    ========

    >>> from sympy import expint, S
    >>> from sympy.abc import nu, z

    Differentiation is supported. Differentiation with respect to $z$ further
    explains the name: for integral orders, the exponential integral is an
    iterated integral of the exponential function.

    >>> expint(nu, z).diff(z)
    -expint(nu - 1, z)

    Differentiation with respect to $\\nu$ has no classical expression:

    >>> expint(nu, z).diff(nu)
    -z**(nu - 1)*meijerg(((), (1, 1)), ((0, 0, 1 - nu), ()), z)

    At non-postive integer orders, the exponential integral reduces to the
    exponential function:

    >>> expint(0, z)
    exp(-z)/z
    >>> expint(-1, z)
    exp(-z)/z + exp(-z)/z**2

    At half-integers it reduces to error functions:

    >>> expint(S(1)/2, z)
    sqrt(pi)*erfc(sqrt(z))/sqrt(z)

    At positive integer orders it can be rewritten in terms of exponentials
    and ``expint(1, z)``. Use ``expand_func()`` to do this:

    >>> from sympy import expand_func
    >>> expand_func(expint(5, z))
    z**4*expint(1, z)/24 + (-z**3 + z**2 - 2*z + 6)*exp(-z)/24

    The generalised exponential integral is essentially equivalent to the
    incomplete gamma function:

    >>> from sympy import uppergamma
    >>> expint(nu, z).rewrite(uppergamma)
    z**(nu - 1)*uppergamma(1 - nu, z)

    As such it is branched at the origin:

    >>> from sympy import exp_polar, pi, I
    >>> expint(4, z*exp_polar(2*pi*I))
    I*pi*z**3/3 + expint(4, z)
    >>> expint(nu, z*exp_polar(2*pi*I))
    z**(nu - 1)*(exp(2*I*pi*nu) - 1)*gamma(1 - nu) + expint(nu, z)

    See Also
    ========

    Ei: Another related function called exponential integral.
    E1: The classical case, returns expint(1, z).
    li: Logarithmic integral.
    Li: Offset logarithmic integral.
    Si: Sine integral.
    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.
    uppergamma

    References
    ==========

    .. [1] https://dlmf.nist.gov/8.19
    .. [2] https://functions.wolfram.com/GammaBetaErf/ExpIntegralE/
    .. [3] https://en.wikipedia.org/wiki/Exponential_integral

    """
    @classmethod
    def eval(cls, nu, z): ...
    def fdiff(self, argindex): ...

def E1(z):
    """
    Classical case of the generalized exponential integral.

    Explanation
    ===========

    This is equivalent to ``expint(1, z)``.

    Examples
    ========

    >>> from sympy import E1
    >>> E1(0)
    expint(1, 0)

    >>> E1(5)
    expint(1, 5)

    See Also
    ========

    Ei: Exponential integral.
    expint: Generalised exponential integral.
    li: Logarithmic integral.
    Li: Offset logarithmic integral.
    Si: Sine integral.
    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.

    """

class li(Function):
    """
    The classical logarithmic integral.

    Explanation
    ===========

    For use in SymPy, this function is defined as

    .. math:: \\operatorname{li}(x) = \\int_0^x \\frac{1}{\\log(t)} \\mathrm{d}t \\,.

    Examples
    ========

    >>> from sympy import I, oo, li
    >>> from sympy.abc import z

    Several special values are known:

    >>> li(0)
    0
    >>> li(1)
    -oo
    >>> li(oo)
    oo

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(li(z), z)
    1/log(z)

    Defining the ``li`` function via an integral:
    >>> from sympy import integrate
    >>> integrate(li(z))
    z*li(z) - Ei(2*log(z))

    >>> integrate(li(z),z)
    z*li(z) - Ei(2*log(z))


    The logarithmic integral can also be defined in terms of ``Ei``:

    >>> from sympy import Ei
    >>> li(z).rewrite(Ei)
    Ei(log(z))
    >>> diff(li(z).rewrite(Ei), z)
    1/log(z)

    We can numerically evaluate the logarithmic integral to arbitrary precision
    on the whole complex plane (except the singular points):

    >>> li(2).evalf(30)
    1.04516378011749278484458888919

    >>> li(2*I).evalf(30)
    1.0652795784357498247001125598 + 3.08346052231061726610939702133*I

    We can even compute Soldner's constant by the help of mpmath:

    >>> from mpmath import findroot
    >>> findroot(li, 2)
    1.45136923488338

    Further transformations include rewriting ``li`` in terms of
    the trigonometric integrals ``Si``, ``Ci``, ``Shi`` and ``Chi``:

    >>> from sympy import Si, Ci, Shi, Chi
    >>> li(z).rewrite(Si)
    -log(I*log(z)) - log(1/log(z))/2 + log(log(z))/2 + Ci(I*log(z)) + Shi(log(z))
    >>> li(z).rewrite(Ci)
    -log(I*log(z)) - log(1/log(z))/2 + log(log(z))/2 + Ci(I*log(z)) + Shi(log(z))
    >>> li(z).rewrite(Shi)
    -log(1/log(z))/2 + log(log(z))/2 + Chi(log(z)) - Shi(log(z))
    >>> li(z).rewrite(Chi)
    -log(1/log(z))/2 + log(log(z))/2 + Chi(log(z)) - Shi(log(z))

    See Also
    ========

    Li: Offset logarithmic integral.
    Ei: Exponential integral.
    expint: Generalised exponential integral.
    E1: Special case of the generalised exponential integral.
    Si: Sine integral.
    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Logarithmic_integral
    .. [2] https://mathworld.wolfram.com/LogarithmicIntegral.html
    .. [3] https://dlmf.nist.gov/6
    .. [4] https://mathworld.wolfram.com/SoldnersConstant.html

    """
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...

class Li(Function):
    """
    The offset logarithmic integral.

    Explanation
    ===========

    For use in SymPy, this function is defined as

    .. math:: \\operatorname{Li}(x) = \\operatorname{li}(x) - \\operatorname{li}(2)

    Examples
    ========

    >>> from sympy import Li
    >>> from sympy.abc import z

    The following special value is known:

    >>> Li(2)
    0

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(Li(z), z)
    1/log(z)

    The shifted logarithmic integral can be written in terms of $li(z)$:

    >>> from sympy import li
    >>> Li(z).rewrite(li)
    li(z) - li(2)

    We can numerically evaluate the logarithmic integral to arbitrary precision
    on the whole complex plane (except the singular points):

    >>> Li(2).evalf(30)
    0

    >>> Li(4).evalf(30)
    1.92242131492155809316615998938

    See Also
    ========

    li: Logarithmic integral.
    Ei: Exponential integral.
    expint: Generalised exponential integral.
    E1: Special case of the generalised exponential integral.
    Si: Sine integral.
    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Logarithmic_integral
    .. [2] https://mathworld.wolfram.com/LogarithmicIntegral.html
    .. [3] https://dlmf.nist.gov/6

    """
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...

class TrigonometricIntegral(Function):
    """ Base class for trigonometric integrals. """
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...

class Si(TrigonometricIntegral):
    """
    Sine integral.

    Explanation
    ===========

    This function is defined by

    .. math:: \\operatorname{Si}(z) = \\int_0^z \\frac{\\sin{t}}{t} \\mathrm{d}t.

    It is an entire function.

    Examples
    ========

    >>> from sympy import Si
    >>> from sympy.abc import z

    The sine integral is an antiderivative of $sin(z)/z$:

    >>> Si(z).diff(z)
    sin(z)/z

    It is unbranched:

    >>> from sympy import exp_polar, I, pi
    >>> Si(z*exp_polar(2*I*pi))
    Si(z)

    Sine integral behaves much like ordinary sine under multiplication by ``I``:

    >>> Si(I*z)
    I*Shi(z)
    >>> Si(-z)
    -Si(z)

    It can also be expressed in terms of exponential integrals, but beware
    that the latter is branched:

    >>> from sympy import expint
    >>> Si(z).rewrite(expint)
    -I*(-expint(1, z*exp_polar(-I*pi/2))/2 +
         expint(1, z*exp_polar(I*pi/2))/2) + pi/2

    It can be rewritten in the form of sinc function (by definition):

    >>> from sympy import sinc
    >>> Si(z).rewrite(sinc)
    Integral(sinc(t), (t, 0, z))

    See Also
    ========

    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.
    Ei: Exponential integral.
    expint: Generalised exponential integral.
    sinc: unnormalized sinc function
    E1: Special case of the generalised exponential integral.
    li: Logarithmic integral.
    Li: Offset logarithmic integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigonometric_integral

    """
class Ci(TrigonometricIntegral):
    """
    Cosine integral.

    Explanation
    ===========

    This function is defined for positive $x$ by

    .. math:: \\operatorname{Ci}(x) = \\gamma + \\log{x}
                         + \\int_0^x \\frac{\\cos{t} - 1}{t} \\mathrm{d}t
           = -\\int_x^\\infty \\frac{\\cos{t}}{t} \\mathrm{d}t,

    where $\\gamma$ is the Euler-Mascheroni constant.

    We have

    .. math:: \\operatorname{Ci}(z) =
        -\\frac{\\operatorname{E}_1\\left(e^{i\\pi/2} z\\right)
               + \\operatorname{E}_1\\left(e^{-i \\pi/2} z\\right)}{2}

    which holds for all polar $z$ and thus provides an analytic
    continuation to the Riemann surface of the logarithm.

    The formula also holds as stated
    for $z \\in \\mathbb{C}$ with $\\Re(z) > 0$.
    By lifting to the principal branch, we obtain an analytic function on the
    cut complex plane.

    Examples
    ========

    >>> from sympy import Ci
    >>> from sympy.abc import z

    The cosine integral is a primitive of $\\cos(z)/z$:

    >>> Ci(z).diff(z)
    cos(z)/z

    It has a logarithmic branch point at the origin:

    >>> from sympy import exp_polar, I, pi
    >>> Ci(z*exp_polar(2*I*pi))
    Ci(z) + 2*I*pi

    The cosine integral behaves somewhat like ordinary $\\cos$ under
    multiplication by $i$:

    >>> from sympy import polar_lift
    >>> Ci(polar_lift(I)*z)
    Chi(z) + I*pi/2
    >>> Ci(polar_lift(-1)*z)
    Ci(z) + I*pi

    It can also be expressed in terms of exponential integrals:

    >>> from sympy import expint
    >>> Ci(z).rewrite(expint)
    -expint(1, z*exp_polar(-I*pi/2))/2 - expint(1, z*exp_polar(I*pi/2))/2

    See Also
    ========

    Si: Sine integral.
    Shi: Hyperbolic sine integral.
    Chi: Hyperbolic cosine integral.
    Ei: Exponential integral.
    expint: Generalised exponential integral.
    E1: Special case of the generalised exponential integral.
    li: Logarithmic integral.
    Li: Offset logarithmic integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigonometric_integral

    """
class Shi(TrigonometricIntegral):
    """
    Sinh integral.

    Explanation
    ===========

    This function is defined by

    .. math:: \\operatorname{Shi}(z) = \\int_0^z \\frac{\\sinh{t}}{t} \\mathrm{d}t.

    It is an entire function.

    Examples
    ========

    >>> from sympy import Shi
    >>> from sympy.abc import z

    The Sinh integral is a primitive of $\\sinh(z)/z$:

    >>> Shi(z).diff(z)
    sinh(z)/z

    It is unbranched:

    >>> from sympy import exp_polar, I, pi
    >>> Shi(z*exp_polar(2*I*pi))
    Shi(z)

    The $\\sinh$ integral behaves much like ordinary $\\sinh$ under
    multiplication by $i$:

    >>> Shi(I*z)
    I*Si(z)
    >>> Shi(-z)
    -Shi(z)

    It can also be expressed in terms of exponential integrals, but beware
    that the latter is branched:

    >>> from sympy import expint
    >>> Shi(z).rewrite(expint)
    expint(1, z)/2 - expint(1, z*exp_polar(I*pi))/2 - I*pi/2

    See Also
    ========

    Si: Sine integral.
    Ci: Cosine integral.
    Chi: Hyperbolic cosine integral.
    Ei: Exponential integral.
    expint: Generalised exponential integral.
    E1: Special case of the generalised exponential integral.
    li: Logarithmic integral.
    Li: Offset logarithmic integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigonometric_integral

    """
class Chi(TrigonometricIntegral):
    """
    Cosh integral.

    Explanation
    ===========

    This function is defined for positive $x$ by

    .. math:: \\operatorname{Chi}(x) = \\gamma + \\log{x}
                         + \\int_0^x \\frac{\\cosh{t} - 1}{t} \\mathrm{d}t,

    where $\\gamma$ is the Euler-Mascheroni constant.

    We have

    .. math:: \\operatorname{Chi}(z) = \\operatorname{Ci}\\left(e^{i \\pi/2}z\\right)
                         - i\\frac{\\pi}{2},

    which holds for all polar $z$ and thus provides an analytic
    continuation to the Riemann surface of the logarithm.
    By lifting to the principal branch we obtain an analytic function on the
    cut complex plane.

    Examples
    ========

    >>> from sympy import Chi
    >>> from sympy.abc import z

    The $\\cosh$ integral is a primitive of $\\cosh(z)/z$:

    >>> Chi(z).diff(z)
    cosh(z)/z

    It has a logarithmic branch point at the origin:

    >>> from sympy import exp_polar, I, pi
    >>> Chi(z*exp_polar(2*I*pi))
    Chi(z) + 2*I*pi

    The $\\cosh$ integral behaves somewhat like ordinary $\\cosh$ under
    multiplication by $i$:

    >>> from sympy import polar_lift
    >>> Chi(polar_lift(I)*z)
    Ci(z) + I*pi/2
    >>> Chi(polar_lift(-1)*z)
    Chi(z) + I*pi

    It can also be expressed in terms of exponential integrals:

    >>> from sympy import expint
    >>> Chi(z).rewrite(expint)
    -expint(1, z)/2 - expint(1, z*exp_polar(I*pi))/2 - I*pi/2

    See Also
    ========

    Si: Sine integral.
    Ci: Cosine integral.
    Shi: Hyperbolic sine integral.
    Ei: Exponential integral.
    expint: Generalised exponential integral.
    E1: Special case of the generalised exponential integral.
    li: Logarithmic integral.
    Li: Offset logarithmic integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigonometric_integral

    """

class FresnelIntegral(Function):
    """ Base class for the Fresnel integrals."""
    unbranched: bool
    @classmethod
    def eval(cls, z): ...
    def fdiff(self, argindex: int = 1): ...
    as_real_imag = real_to_real_as_real_imag

class fresnels(FresnelIntegral):
    """
    Fresnel integral S.

    Explanation
    ===========

    This function is defined by

    .. math:: \\operatorname{S}(z) = \\int_0^z \\sin{\\frac{\\pi}{2} t^2} \\mathrm{d}t.

    It is an entire function.

    Examples
    ========

    >>> from sympy import I, oo, fresnels
    >>> from sympy.abc import z

    Several special values are known:

    >>> fresnels(0)
    0
    >>> fresnels(oo)
    1/2
    >>> fresnels(-oo)
    -1/2
    >>> fresnels(I*oo)
    -I/2
    >>> fresnels(-I*oo)
    I/2

    In general one can pull out factors of -1 and $i$ from the argument:

    >>> fresnels(-z)
    -fresnels(z)
    >>> fresnels(I*z)
    -I*fresnels(z)

    The Fresnel S integral obeys the mirror symmetry
    $\\overline{S(z)} = S(\\bar{z})$:

    >>> from sympy import conjugate
    >>> conjugate(fresnels(z))
    fresnels(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(fresnels(z), z)
    sin(pi*z**2/2)

    Defining the Fresnel functions via an integral:

    >>> from sympy import integrate, pi, sin, expand_func
    >>> integrate(sin(pi*z**2/2), z)
    3*fresnels(z)*gamma(3/4)/(4*gamma(7/4))
    >>> expand_func(integrate(sin(pi*z**2/2), z))
    fresnels(z)

    We can numerically evaluate the Fresnel integral to arbitrary precision
    on the whole complex plane:

    >>> fresnels(2).evalf(30)
    0.343415678363698242195300815958

    >>> fresnels(-2*I).evalf(30)
    0.343415678363698242195300815958*I

    See Also
    ========

    fresnelc: Fresnel cosine integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fresnel_integral
    .. [2] https://dlmf.nist.gov/7
    .. [3] https://mathworld.wolfram.com/FresnelIntegrals.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/FresnelS
    .. [5] The converging factors for the fresnel integrals
            by John W. Wrench Jr. and Vicki Alley

    """
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...

class fresnelc(FresnelIntegral):
    """
    Fresnel integral C.

    Explanation
    ===========

    This function is defined by

    .. math:: \\operatorname{C}(z) = \\int_0^z \\cos{\\frac{\\pi}{2} t^2} \\mathrm{d}t.

    It is an entire function.

    Examples
    ========

    >>> from sympy import I, oo, fresnelc
    >>> from sympy.abc import z

    Several special values are known:

    >>> fresnelc(0)
    0
    >>> fresnelc(oo)
    1/2
    >>> fresnelc(-oo)
    -1/2
    >>> fresnelc(I*oo)
    I/2
    >>> fresnelc(-I*oo)
    -I/2

    In general one can pull out factors of -1 and $i$ from the argument:

    >>> fresnelc(-z)
    -fresnelc(z)
    >>> fresnelc(I*z)
    I*fresnelc(z)

    The Fresnel C integral obeys the mirror symmetry
    $\\overline{C(z)} = C(\\bar{z})$:

    >>> from sympy import conjugate
    >>> conjugate(fresnelc(z))
    fresnelc(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(fresnelc(z), z)
    cos(pi*z**2/2)

    Defining the Fresnel functions via an integral:

    >>> from sympy import integrate, pi, cos, expand_func
    >>> integrate(cos(pi*z**2/2), z)
    fresnelc(z)*gamma(1/4)/(4*gamma(5/4))
    >>> expand_func(integrate(cos(pi*z**2/2), z))
    fresnelc(z)

    We can numerically evaluate the Fresnel integral to arbitrary precision
    on the whole complex plane:

    >>> fresnelc(2).evalf(30)
    0.488253406075340754500223503357

    >>> fresnelc(-2*I).evalf(30)
    -0.488253406075340754500223503357*I

    See Also
    ========

    fresnels: Fresnel sine integral.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fresnel_integral
    .. [2] https://dlmf.nist.gov/7
    .. [3] https://mathworld.wolfram.com/FresnelIntegrals.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/FresnelC
    .. [5] The converging factors for the fresnel integrals
            by John W. Wrench Jr. and Vicki Alley

    """
    @staticmethod
    def taylor_term(n, x, *previous_terms): ...

class _erfs(Function):
    """
    Helper function to make the $\\mathrm{erf}(z)$ function
    tractable for the Gruntz algorithm.

    """
    @classmethod
    def eval(cls, arg): ...
    def fdiff(self, argindex: int = 1): ...

class _eis(Function):
    """
    Helper function to make the $\\mathrm{Ei}(z)$ and $\\mathrm{li}(z)$
    functions tractable for the Gruntz algorithm.

    """
    def fdiff(self, argindex: int = 1): ...
