from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import ArgumentIndexError as ArgumentIndexError, Function as Function, expand_mul as expand_mul
from sympy.core.numbers import I as I, Integer as Integer, pi as pi
from sympy.core.relational import Eq as Eq
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.numbers import bernoulli as bernoulli, factorial as factorial, genocchi as genocchi, harmonic as harmonic
from sympy.functions.elementary.complexes import Abs as Abs, polar_lift as polar_lift, re as re, unpolarify as unpolarify
from sympy.functions.elementary.exponential import exp as exp, exp_polar as exp_polar, log as log
from sympy.functions.elementary.integers import ceiling as ceiling, floor as floor
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.polys.polytools import Poly as Poly

class lerchphi(Function):
    """
    Lerch transcendent (Lerch phi function).

    Explanation
    ===========

    For $\\operatorname{Re}(a) > 0$, $|z| < 1$ and $s \\in \\mathbb{C}$, the
    Lerch transcendent is defined as

    .. math :: \\Phi(z, s, a) = \\sum_{n=0}^\\infty \\frac{z^n}{(n + a)^s},

    where the standard branch of the argument is used for $n + a$,
    and by analytic continuation for other values of the parameters.

    A commonly used related function is the Lerch zeta function, defined by

    .. math:: L(q, s, a) = \\Phi(e^{2\\pi i q}, s, a).

    **Analytic Continuation and Branching Behavior**

    It can be shown that

    .. math:: \\Phi(z, s, a) = z\\Phi(z, s, a+1) + a^{-s}.

    This provides the analytic continuation to $\\operatorname{Re}(a) \\le 0$.

    Assume now $\\operatorname{Re}(a) > 0$. The integral representation

    .. math:: \\Phi_0(z, s, a) = \\int_0^\\infty \\frac{t^{s-1} e^{-at}}{1 - ze^{-t}}
                                \\frac{\\mathrm{d}t}{\\Gamma(s)}

    provides an analytic continuation to $\\mathbb{C} - [1, \\infty)$.
    Finally, for $x \\in (1, \\infty)$ we find

    .. math:: \\lim_{\\epsilon \\to 0^+} \\Phi_0(x + i\\epsilon, s, a)
             -\\lim_{\\epsilon \\to 0^+} \\Phi_0(x - i\\epsilon, s, a)
             = \\frac{2\\pi i \\log^{s-1}{x}}{x^a \\Gamma(s)},

    using the standard branch for both $\\log{x}$ and
    $\\log{\\log{x}}$ (a branch of $\\log{\\log{x}}$ is needed to
    evaluate $\\log{x}^{s-1}$).
    This concludes the analytic continuation. The Lerch transcendent is thus
    branched at $z \\in \\{0, 1, \\infty\\}$ and
    $a \\in \\mathbb{Z}_{\\le 0}$. For fixed $z, a$ outside these
    branch points, it is an entire function of $s$.

    Examples
    ========

    The Lerch transcendent is a fairly general function, for this reason it does
    not automatically evaluate to simpler functions. Use ``expand_func()`` to
    achieve this.

    If $z=1$, the Lerch transcendent reduces to the Hurwitz zeta function:

    >>> from sympy import lerchphi, expand_func
    >>> from sympy.abc import z, s, a
    >>> expand_func(lerchphi(1, s, a))
    zeta(s, a)

    More generally, if $z$ is a root of unity, the Lerch transcendent
    reduces to a sum of Hurwitz zeta functions:

    >>> expand_func(lerchphi(-1, s, a))
    zeta(s, a/2)/2**s - zeta(s, a/2 + 1/2)/2**s

    If $a=1$, the Lerch transcendent reduces to the polylogarithm:

    >>> expand_func(lerchphi(z, s, 1))
    polylog(s, z)/z

    More generally, if $a$ is rational, the Lerch transcendent reduces
    to a sum of polylogarithms:

    >>> from sympy import S
    >>> expand_func(lerchphi(z, s, S(1)/2))
    2**(s - 1)*(polylog(s, sqrt(z))/sqrt(z) -
                polylog(s, sqrt(z)*exp_polar(I*pi))/sqrt(z))
    >>> expand_func(lerchphi(z, s, S(3)/2))
    -2**s/z + 2**(s - 1)*(polylog(s, sqrt(z))/sqrt(z) -
                          polylog(s, sqrt(z)*exp_polar(I*pi))/sqrt(z))/z

    The derivatives with respect to $z$ and $a$ can be computed in
    closed form:

    >>> lerchphi(z, s, a).diff(z)
    (-a*lerchphi(z, s, a) + lerchphi(z, s - 1, a))/z
    >>> lerchphi(z, s, a).diff(a)
    -s*lerchphi(z, s + 1, a)

    See Also
    ========

    polylog, zeta

    References
    ==========

    .. [1] Bateman, H.; Erdelyi, A. (1953), Higher Transcendental Functions,
           Vol. I, New York: McGraw-Hill. Section 1.11.
    .. [2] https://dlmf.nist.gov/25.14
    .. [3] https://en.wikipedia.org/wiki/Lerch_transcendent

    """
    def fdiff(self, argindex: int = 1): ...

class polylog(Function):
    """
    Polylogarithm function.

    Explanation
    ===========

    For $|z| < 1$ and $s \\in \\mathbb{C}$, the polylogarithm is
    defined by

    .. math:: \\operatorname{Li}_s(z) = \\sum_{n=1}^\\infty \\frac{z^n}{n^s},

    where the standard branch of the argument is used for $n$. It admits
    an analytic continuation which is branched at $z=1$ (notably not on the
    sheet of initial definition), $z=0$ and $z=\\infty$.

    The name polylogarithm comes from the fact that for $s=1$, the
    polylogarithm is related to the ordinary logarithm (see examples), and that

    .. math:: \\operatorname{Li}_{s+1}(z) =
                    \\int_0^z \\frac{\\operatorname{Li}_s(t)}{t} \\mathrm{d}t.

    The polylogarithm is a special case of the Lerch transcendent:

    .. math:: \\operatorname{Li}_{s}(z) = z \\Phi(z, s, 1).

    Examples
    ========

    For $z \\in \\{0, 1, -1\\}$, the polylogarithm is automatically expressed
    using other functions:

    >>> from sympy import polylog
    >>> from sympy.abc import s
    >>> polylog(s, 0)
    0
    >>> polylog(s, 1)
    zeta(s)
    >>> polylog(s, -1)
    -dirichlet_eta(s)

    If $s$ is a negative integer, $0$ or $1$, the polylogarithm can be
    expressed using elementary functions. This can be done using
    ``expand_func()``:

    >>> from sympy import expand_func
    >>> from sympy.abc import z
    >>> expand_func(polylog(1, z))
    -log(1 - z)
    >>> expand_func(polylog(0, z))
    z/(1 - z)

    The derivative with respect to $z$ can be computed in closed form:

    >>> polylog(s, z).diff(z)
    polylog(s - 1, z)/z

    The polylogarithm can be expressed in terms of the lerch transcendent:

    >>> from sympy import lerchphi
    >>> polylog(s, z).rewrite(lerchphi)
    z*lerchphi(z, s, 1)

    See Also
    ========

    zeta, lerchphi

    """
    @classmethod
    def eval(cls, s, z): ...
    def fdiff(self, argindex: int = 1): ...

class zeta(Function):
    """
    Hurwitz zeta function (or Riemann zeta function).

    Explanation
    ===========

    For $\\operatorname{Re}(a) > 0$ and $\\operatorname{Re}(s) > 1$, this
    function is defined as

    .. math:: \\zeta(s, a) = \\sum_{n=0}^\\infty \\frac{1}{(n + a)^s},

    where the standard choice of argument for $n + a$ is used. For fixed
    $a$ not a nonpositive integer the Hurwitz zeta function admits a
    meromorphic continuation to all of $\\mathbb{C}$; it is an unbranched
    function with a simple pole at $s = 1$.

    The Hurwitz zeta function is a special case of the Lerch transcendent:

    .. math:: \\zeta(s, a) = \\Phi(1, s, a).

    This formula defines an analytic continuation for all possible values of
    $s$ and $a$ (also $\\operatorname{Re}(a) < 0$), see the documentation of
    :class:`lerchphi` for a description of the branching behavior.

    If no value is passed for $a$ a default value of $a = 1$ is assumed,
    yielding the Riemann zeta function.

    Examples
    ========

    For $a = 1$ the Hurwitz zeta function reduces to the famous Riemann
    zeta function:

    .. math:: \\zeta(s, 1) = \\zeta(s) = \\sum_{n=1}^\\infty \\frac{1}{n^s}.

    >>> from sympy import zeta
    >>> from sympy.abc import s
    >>> zeta(s, 1)
    zeta(s)
    >>> zeta(s)
    zeta(s)

    The Riemann zeta function can also be expressed using the Dirichlet eta
    function:

    >>> from sympy import dirichlet_eta
    >>> zeta(s).rewrite(dirichlet_eta)
    dirichlet_eta(s)/(1 - 2**(1 - s))

    The Riemann zeta function at nonnegative even and negative integer
    values is related to the Bernoulli numbers and polynomials:

    >>> zeta(2)
    pi**2/6
    >>> zeta(4)
    pi**4/90
    >>> zeta(0)
    -1/2
    >>> zeta(-1)
    -1/12
    >>> zeta(-4)
    0

    The specific formulae are:

    .. math:: \\zeta(2n) = -\\frac{(2\\pi i)^{2n} B_{2n}}{2(2n)!}
    .. math:: \\zeta(-n,a) = -\\frac{B_{n+1}(a)}{n+1}

    No closed-form expressions are known at positive odd integers, but
    numerical evaluation is possible:

    >>> zeta(3).n()
    1.20205690315959

    The derivative of $\\zeta(s, a)$ with respect to $a$ can be computed:

    >>> from sympy.abc import a
    >>> zeta(s, a).diff(a)
    -s*zeta(s + 1, a)

    However the derivative with respect to $s$ has no useful closed form
    expression:

    >>> zeta(s, a).diff(s)
    Derivative(zeta(s, a), s)

    The Hurwitz zeta function can be expressed in terms of the Lerch
    transcendent, :class:`~.lerchphi`:

    >>> from sympy import lerchphi
    >>> zeta(s, a).rewrite(lerchphi)
    lerchphi(1, s, a)

    See Also
    ========

    dirichlet_eta, lerchphi, polylog

    References
    ==========

    .. [1] https://dlmf.nist.gov/25.11
    .. [2] https://en.wikipedia.org/wiki/Hurwitz_zeta_function

    """
    @classmethod
    def eval(cls, s, a: Incomplete | None = None): ...
    def fdiff(self, argindex: int = 1): ...

class dirichlet_eta(Function):
    '''
    Dirichlet eta function.

    Explanation
    ===========

    For $\\operatorname{Re}(s) > 0$ and $0 < x \\le 1$, this function is defined as

    .. math:: \\eta(s, a) = \\sum_{n=0}^\\infty \\frac{(-1)^n}{(n+a)^s}.

    It admits a unique analytic continuation to all of $\\mathbb{C}$ for any
    fixed $a$ not a nonpositive integer. It is an entire, unbranched function.

    It can be expressed using the Hurwitz zeta function as

    .. math:: \\eta(s, a) = \\zeta(s,a) - 2^{1-s} \\zeta\\left(s, \\frac{a+1}{2}\\right)

    and using the generalized Genocchi function as

    .. math:: \\eta(s, a) = \\frac{G(1-s, a)}{2(s-1)}.

    In both cases the limiting value of $\\log2 - \\psi(a) + \\psi\\left(\\frac{a+1}{2}\\right)$
    is used when $s = 1$.

    Examples
    ========

    >>> from sympy import dirichlet_eta, zeta
    >>> from sympy.abc import s
    >>> dirichlet_eta(s).rewrite(zeta)
    Piecewise((log(2), Eq(s, 1)), ((1 - 2**(1 - s))*zeta(s), True))

    See Also
    ========

    zeta

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dirichlet_eta_function
    .. [2] Peter Luschny, "An introduction to the Bernoulli function",
           https://arxiv.org/abs/2009.06743

    '''
    @classmethod
    def eval(cls, s, a: Incomplete | None = None): ...

class riemann_xi(Function):
    """
    Riemann Xi function.

    Examples
    ========

    The Riemann Xi function is closely related to the Riemann zeta function.
    The zeros of Riemann Xi function are precisely the non-trivial zeros
    of the zeta function.

    >>> from sympy import riemann_xi, zeta
    >>> from sympy.abc import s
    >>> riemann_xi(s).rewrite(zeta)
    s*(s - 1)*gamma(s/2)*zeta(s)/(2*pi**(s/2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Riemann_Xi_function

    """
    @classmethod
    def eval(cls, s): ...

class stieltjes(Function):
    """
    Represents Stieltjes constants, $\\gamma_{k}$ that occur in
    Laurent Series expansion of the Riemann zeta function.

    Examples
    ========

    >>> from sympy import stieltjes
    >>> from sympy.abc import n, m
    >>> stieltjes(n)
    stieltjes(n)

    The zero'th stieltjes constant:

    >>> stieltjes(0)
    EulerGamma
    >>> stieltjes(0, 1)
    EulerGamma

    For generalized stieltjes constants:

    >>> stieltjes(n, m)
    stieltjes(n, m)

    Constants are only defined for integers >= 0:

    >>> stieltjes(-1)
    zoo

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Stieltjes_constants

    """
    @classmethod
    def eval(cls, n, a: Incomplete | None = None): ...
