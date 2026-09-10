from _typeshed import Incomplete
from sympy.stats.crv import SingleContinuousDistribution

__all__ = ['ContinuousRV', 'Arcsin', 'Benini', 'Beta', 'BetaNoncentral', 'BetaPrime', 'BoundedPareto', 'Cauchy', 'Chi', 'ChiNoncentral', 'ChiSquared', 'Dagum', 'Erlang', 'ExGaussian', 'Exponential', 'ExponentialPower', 'FDistribution', 'FisherZ', 'Frechet', 'Gamma', 'GammaInverse', 'Gompertz', 'Gumbel', 'Kumaraswamy', 'Laplace', 'Levy', 'LogCauchy', 'Logistic', 'LogLogistic', 'LogitNormal', 'LogNormal', 'Lomax', 'Maxwell', 'Moyal', 'Nakagami', 'Normal', 'GaussianInverse', 'Pareto', 'PowerFunction', 'QuadraticU', 'RaisedCosine', 'Rayleigh', 'Reciprocal', 'StudentT', 'ShiftedGompertz', 'Trapezoidal', 'Triangular', 'Uniform', 'UniformSum', 'VonMises', 'Wald', 'Weibull', 'WignerSemicircle']

class ContinuousDistributionHandmade(SingleContinuousDistribution):
    def __new__(cls, pdf, set=...): ...
    @property
    def set(self): ...
    @staticmethod
    def check(pdf, set) -> None: ...

def ContinuousRV(symbol, density, set=..., **kwargs):
    '''
    Create a Continuous Random Variable given the following:

    Parameters
    ==========

    symbol : Symbol
        Represents name of the random variable.
    density : Expression containing symbol
        Represents probability density function.
    set : set/Interval
        Represents the region where the pdf is valid, by default is real line.
    check : bool
        If True, it will check whether the given density
        integrates to 1 over the given set. If False, it
        will not perform this check. Default is False.


    Returns
    =======

    RandomSymbol

    Many common continuous random variable types are already implemented.
    This function should be necessary only very rarely.


    Examples
    ========

    >>> from sympy import Symbol, sqrt, exp, pi
    >>> from sympy.stats import ContinuousRV, P, E

    >>> x = Symbol("x")

    >>> pdf = sqrt(2)*exp(-x**2/2)/(2*sqrt(pi)) # Normal distribution
    >>> X = ContinuousRV(x, pdf)

    >>> E(X)
    0
    >>> P(X>0)
    1/2
    '''

class ArcsinDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    def pdf(self, x): ...

def Arcsin(name, a: int = 0, b: int = 1):
    '''
    Create a Continuous Random Variable with an arcsin distribution.

    The density of the arcsin distribution is given by

    .. math::
        f(x) := \\frac{1}{\\pi\\sqrt{(x-a)(b-x)}}

    with :math:`x \\in (a,b)`. It must hold that :math:`-\\infty < a < b < \\infty`.

    Parameters
    ==========

    a : Real number, the left interval boundary
    b : Real number, the right interval boundary

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Arcsin, density, cdf
    >>> from sympy import Symbol

    >>> a = Symbol("a", real=True)
    >>> b = Symbol("b", real=True)
    >>> z = Symbol("z")

    >>> X = Arcsin("x", a, b)

    >>> density(X)(z)
    1/(pi*sqrt((-a + z)*(b - z)))

    >>> cdf(X)(z)
    Piecewise((0, a > z),
            (2*asin(sqrt((-a + z)/(-a + b)))/pi, b >= z),
            (1, True))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Arcsine_distribution

    '''

class BeniniDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(alpha, beta, sigma) -> None: ...
    @property
    def set(self): ...
    def pdf(self, x): ...

def Benini(name, alpha, beta, sigma):
    '''
    Create a Continuous Random Variable with a Benini distribution.

    The density of the Benini distribution is given by

    .. math::
        f(x) := e^{-\\alpha\\log{\\frac{x}{\\sigma}}
                -\\beta\\log^2\\left[{\\frac{x}{\\sigma}}\\right]}
                \\left(\\frac{\\alpha}{x}+\\frac{2\\beta\\log{\\frac{x}{\\sigma}}}{x}\\right)

    This is a heavy-tailed distribution and is also known as the log-Rayleigh
    distribution.

    Parameters
    ==========

    alpha : Real number, `\\alpha > 0`, a shape
    beta : Real number, `\\beta > 0`, a shape
    sigma : Real number, `\\sigma > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Benini, density, cdf
    >>> from sympy import Symbol, pprint

    >>> alpha = Symbol("alpha", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> sigma = Symbol("sigma", positive=True)
    >>> z = Symbol("z")

    >>> X = Benini("x", alpha, beta, sigma)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
    /                  /  z  \\\\             /  z  \\            2/  z  \\\n    |        2*beta*log|-----||  - alpha*log|-----| - beta*log  |-----|
    |alpha             \\sigma/|             \\sigma/             \\sigma/
    |----- + -----------------|*e
    \\  z             z        /

    >>> cdf(X)(z)
    Piecewise((1 - exp(-alpha*log(z/sigma) - beta*log(z/sigma)**2), sigma <= z),
            (0, True))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Benini_distribution
    .. [2] https://reference.wolfram.com/legacy/v8/ref/BeniniDistribution.html

    '''

class BetaDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(alpha, beta) -> None: ...
    def pdf(self, x): ...

def Beta(name, alpha, beta):
    '''
    Create a Continuous Random Variable with a Beta distribution.

    The density of the Beta distribution is given by

    .. math::
        f(x) := \\frac{x^{\\alpha-1}(1-x)^{\\beta-1}} {\\mathrm{B}(\\alpha,\\beta)}

    with :math:`x \\in [0,1]`.

    Parameters
    ==========

    alpha : Real number, `\\alpha > 0`, a shape
    beta : Real number, `\\beta > 0`, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Beta, density, E, variance
    >>> from sympy import Symbol, simplify, pprint, factor

    >>> alpha = Symbol("alpha", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> z = Symbol("z")

    >>> X = Beta("x", alpha, beta)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
     alpha - 1        beta - 1
    z         *(1 - z)
    --------------------------
          B(alpha, beta)

    >>> simplify(E(X))
    alpha/(alpha + beta)

    >>> factor(simplify(variance(X)))
    alpha*beta/((alpha + beta)**2*(alpha + beta + 1))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Beta_distribution
    .. [2] https://mathworld.wolfram.com/BetaDistribution.html

    '''

class BetaNoncentralDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(alpha, beta, lamda) -> None: ...
    def pdf(self, x): ...

def BetaNoncentral(name, alpha, beta, lamda):
    '''
    Create a Continuous Random Variable with a Type I Noncentral Beta distribution.

    The density of the Noncentral Beta distribution is given by

    .. math::
        f(x) := \\sum_{k=0}^\\infty e^{-\\lambda/2}\\frac{(\\lambda/2)^k}{k!}
                \\frac{x^{\\alpha+k-1}(1-x)^{\\beta-1}}{\\mathrm{B}(\\alpha+k,\\beta)}

    with :math:`x \\in [0,1]`.

    Parameters
    ==========

    alpha : Real number, `\\alpha > 0`, a shape
    beta : Real number, `\\beta > 0`, a shape
    lamda : Real number, `\\lambda \\geq 0`, noncentrality parameter

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import BetaNoncentral, density, cdf
    >>> from sympy import Symbol, pprint

    >>> alpha = Symbol("alpha", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> lamda = Symbol("lamda", nonnegative=True)
    >>> z = Symbol("z")

    >>> X = BetaNoncentral("x", alpha, beta, lamda)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
      oo
    _____
    \\    `
     \\                                              -lamda
      \\                          k                  -------
       \\    k + alpha - 1 /lamda\\         beta - 1     2
        )  z             *|-----| *(1 - z)        *e
       /                  \\  2  /
      /    ------------------------------------------------
     /                  B(k + alpha, beta)*k!
    /____,
    k = 0

    Compute cdf with specific \'x\', \'alpha\', \'beta\' and \'lamda\' values as follows:

    >>> cdf(BetaNoncentral("x", 1, 1, 1), evaluate=False)(2).doit()
    2*exp(1/2)

    The argument evaluate=False prevents an attempt at evaluation
    of the sum for general x, before the argument 2 is passed.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Noncentral_beta_distribution
    .. [2] https://reference.wolfram.com/language/ref/NoncentralBetaDistribution.html

    '''

class BetaPrimeDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(alpha, beta) -> None: ...
    set: Incomplete
    def pdf(self, x): ...

def BetaPrime(name, alpha, beta):
    '''
    Create a continuous random variable with a Beta prime distribution.

    The density of the Beta prime distribution is given by

    .. math::
        f(x) := \\frac{x^{\\alpha-1} (1+x)^{-\\alpha -\\beta}}{B(\\alpha,\\beta)}

    with :math:`x > 0`.

    Parameters
    ==========

    alpha : Real number, `\\alpha > 0`, a shape
    beta : Real number, `\\beta > 0`, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import BetaPrime, density
    >>> from sympy import Symbol, pprint

    >>> alpha = Symbol("alpha", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> z = Symbol("z")

    >>> X = BetaPrime("x", alpha, beta)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
     alpha - 1        -alpha - beta
    z         *(z + 1)
    -------------------------------
             B(alpha, beta)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Beta_prime_distribution
    .. [2] https://mathworld.wolfram.com/BetaPrimeDistribution.html

    '''

class BoundedParetoDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(alpha, left, right) -> None: ...
    def pdf(self, x): ...

def BoundedPareto(name, alpha, left, right):
    """
    Create a continuous random variable with a Bounded Pareto distribution.

    The density of the Bounded Pareto distribution is given by

    .. math::
        f(x) := \\frac{\\alpha L^{\\alpha}x^{-\\alpha-1}}{1-(\\frac{L}{H})^{\\alpha}}

    Parameters
    ==========

    alpha : Real Number, `\\alpha > 0`
        Shape parameter
    left : Real Number, `left > 0`
        Location parameter
    right : Real Number, `right > left`
        Location parameter

    Examples
    ========

    >>> from sympy.stats import BoundedPareto, density, cdf, E
    >>> from sympy import symbols
    >>> L, H = symbols('L, H', positive=True)
    >>> X = BoundedPareto('X', 2, L, H)
    >>> x = symbols('x')
    >>> density(X)(x)
    2*L**2/(x**3*(1 - L**2/H**2))
    >>> cdf(X)(x)
    Piecewise((-H**2*L**2/(x**2*(H**2 - L**2)) + H**2/(H**2 - L**2), L <= x), (0, True))
    >>> E(X).simplify()
    2*H*L/(H + L)

    Returns
    =======

    RandomSymbol

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Pareto_distribution#Bounded_Pareto_distribution

    """

class CauchyDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(x0, gamma) -> None: ...
    def pdf(self, x): ...

def Cauchy(name, x0, gamma):
    '''
    Create a continuous random variable with a Cauchy distribution.

    The density of the Cauchy distribution is given by

    .. math::
        f(x) := \\frac{1}{\\pi \\gamma [1 + {(\\frac{x-x_0}{\\gamma})}^2]}

    Parameters
    ==========

    x0 : Real number, the location
    gamma : Real number, `\\gamma > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Cauchy, density
    >>> from sympy import Symbol

    >>> x0 = Symbol("x0")
    >>> gamma = Symbol("gamma", positive=True)
    >>> z = Symbol("z")

    >>> X = Cauchy("x", x0, gamma)

    >>> density(X)(z)
    1/(pi*gamma*(1 + (-x0 + z)**2/gamma**2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Cauchy_distribution
    .. [2] https://mathworld.wolfram.com/CauchyDistribution.html

    '''

class ChiDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(k) -> None: ...
    set: Incomplete
    def pdf(self, x): ...

def Chi(name, k):
    '''
    Create a continuous random variable with a Chi distribution.

    The density of the Chi distribution is given by

    .. math::
        f(x) := \\frac{2^{1-k/2}x^{k-1}e^{-x^2/2}}{\\Gamma(k/2)}

    with :math:`x \\geq 0`.

    Parameters
    ==========

    k : Positive integer, The number of degrees of freedom

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Chi, density, E
    >>> from sympy import Symbol, simplify

    >>> k = Symbol("k", integer=True)
    >>> z = Symbol("z")

    >>> X = Chi("x", k)

    >>> density(X)(z)
    2**(1 - k/2)*z**(k - 1)*exp(-z**2/2)/gamma(k/2)

    >>> simplify(E(X))
    sqrt(2)*gamma(k/2 + 1/2)/gamma(k/2)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Chi_distribution
    .. [2] https://mathworld.wolfram.com/ChiDistribution.html

    '''

class ChiNoncentralDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(k, l) -> None: ...
    set: Incomplete
    def pdf(self, x): ...

def ChiNoncentral(name, k, l):
    '''
    Create a continuous random variable with a non-central Chi distribution.

    Explanation
    ===========

    The density of the non-central Chi distribution is given by

    .. math::
        f(x) := \\frac{e^{-(x^2+\\lambda^2)/2} x^k\\lambda}
                {(\\lambda x)^{k/2}} I_{k/2-1}(\\lambda x)

    with `x \\geq 0`. Here, `I_\\nu (x)` is the
    :ref:`modified Bessel function of the first kind <besseli>`.

    Parameters
    ==========

    k : A positive Integer, $k > 0$
        The number of degrees of freedom.
    lambda : Real number, `\\lambda > 0`
        Shift parameter.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import ChiNoncentral, density
    >>> from sympy import Symbol

    >>> k = Symbol("k", integer=True)
    >>> l = Symbol("l")
    >>> z = Symbol("z")

    >>> X = ChiNoncentral("x", k, l)

    >>> density(X)(z)
    l*z**k*exp(-l**2/2 - z**2/2)*besseli(k/2 - 1, l*z)/(l*z)**(k/2)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Noncentral_chi_distribution
    '''

class ChiSquaredDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(k) -> None: ...
    set: Incomplete
    def pdf(self, x): ...

def ChiSquared(name, k):
    '''
    Create a continuous random variable with a Chi-squared distribution.

    Explanation
    ===========

    The density of the Chi-squared distribution is given by

    .. math::
        f(x) := \\frac{1}{2^{\\frac{k}{2}}\\Gamma\\left(\\frac{k}{2}\\right)}
                x^{\\frac{k}{2}-1} e^{-\\frac{x}{2}}

    with :math:`x \\geq 0`.

    Parameters
    ==========

    k : Positive integer
        The number of degrees of freedom.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import ChiSquared, density, E, variance, moment
    >>> from sympy import Symbol

    >>> k = Symbol("k", integer=True, positive=True)
    >>> z = Symbol("z")

    >>> X = ChiSquared("x", k)

    >>> density(X)(z)
    z**(k/2 - 1)*exp(-z/2)/(2**(k/2)*gamma(k/2))

    >>> E(X)
    k

    >>> variance(X)
    2*k

    >>> moment(X, 3)
    k**3 + 6*k**2 + 8*k

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Chi_squared_distribution
    .. [2] https://mathworld.wolfram.com/Chi-SquaredDistribution.html
    '''

class DagumDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(p, a, b) -> None: ...
    def pdf(self, x): ...

def Dagum(name, p, a, b):
    '''
    Create a continuous random variable with a Dagum distribution.

    Explanation
    ===========

    The density of the Dagum distribution is given by

    .. math::
        f(x) := \\frac{a p}{x} \\left( \\frac{\\left(\\tfrac{x}{b}\\right)^{a p}}
                {\\left(\\left(\\tfrac{x}{b}\\right)^a + 1 \\right)^{p+1}} \\right)

    with :math:`x > 0`.

    Parameters
    ==========

    p : Real number
        `p > 0`, a shape.
    a : Real number
        `a > 0`, a shape.
    b : Real number
        `b > 0`, a scale.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Dagum, density, cdf
    >>> from sympy import Symbol

    >>> p = Symbol("p", positive=True)
    >>> a = Symbol("a", positive=True)
    >>> b = Symbol("b", positive=True)
    >>> z = Symbol("z")

    >>> X = Dagum("x", p, a, b)

    >>> density(X)(z)
    a*p*(z/b)**(a*p)*((z/b)**a + 1)**(-p - 1)/z

    >>> cdf(X)(z)
    Piecewise(((1 + (z/b)**(-a))**(-p), z >= 0), (0, True))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dagum_distribution

    '''
def Erlang(name, k, l):
    '''
    Create a continuous random variable with an Erlang distribution.

    Explanation
    ===========

    The density of the Erlang distribution is given by

    .. math::
        f(x) := \\frac{\\lambda^k x^{k-1} e^{-\\lambda x}}{(k-1)!}

    with :math:`x \\in [0,\\infty]`.

    Parameters
    ==========

    k : Positive integer
    l : Real number, `\\lambda > 0`, the rate

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Erlang, density, cdf, E, variance
    >>> from sympy import Symbol, simplify, pprint

    >>> k = Symbol("k", integer=True, positive=True)
    >>> l = Symbol("l", positive=True)
    >>> z = Symbol("z")

    >>> X = Erlang("x", k, l)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
     k  k - 1  -l*z
    l *z     *e
    ---------------
        Gamma(k)

    >>> C = cdf(X)(z)
    >>> pprint(C, use_unicode=False)
    /lowergamma(k, l*z)
    |------------------  for z > 0
    <     Gamma(k)
    |
    \\        0           otherwise


    >>> E(X)
    k/l

    >>> simplify(variance(X))
    k/l**2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Erlang_distribution
    .. [2] https://mathworld.wolfram.com/ErlangDistribution.html

    '''

class ExGaussianDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mean, std, rate) -> None: ...
    def pdf(self, x): ...

def ExGaussian(name, mean, std, rate):
    '''
    Create a continuous random variable with an Exponentially modified
    Gaussian (EMG) distribution.

    Explanation
    ===========

    The density of the exponentially modified Gaussian distribution is given by

    .. math::
        f(x) := \\frac{\\lambda}{2}e^{\\frac{\\lambda}{2}(2\\mu+\\lambda\\sigma^2-2x)}
            \\text{erfc}(\\frac{\\mu + \\lambda\\sigma^2 - x}{\\sqrt{2}\\sigma})

    with $x > 0$. Note that the expected value is `1/\\lambda`.

    Parameters
    ==========

    name : A string giving a name for this distribution
    mean : A Real number, the mean of Gaussian component
    std : A positive Real number,
        :math: `\\sigma^2 > 0` the variance of Gaussian component
    rate : A positive Real number,
        :math: `\\lambda > 0` the rate of Exponential component

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import ExGaussian, density, cdf, E
    >>> from sympy.stats import variance, skewness
    >>> from sympy import Symbol, pprint, simplify

    >>> mean = Symbol("mu")
    >>> std = Symbol("sigma", positive=True)
    >>> rate = Symbol("lamda", positive=True)
    >>> z = Symbol("z")
    >>> X = ExGaussian("x", mean, std, rate)

    >>> pprint(density(X)(z), use_unicode=False)
                 /           2             \\\n           lamda*\\lamda*sigma  + 2*mu - 2*z/
           ---------------------------------     /  ___ /           2         \\\\\n                           2                     |\\/ 2 *\\lamda*sigma  + mu - z/|
    lamda*e                                 *erfc|-----------------------------|
                                                 \\           2*sigma           /
    ----------------------------------------------------------------------------
                                         2

    >>> cdf(X)(z)
    -(erf(sqrt(2)*(-lamda**2*sigma**2 + lamda*(-mu + z))/(2*lamda*sigma))/2 + 1/2)*exp(lamda**2*sigma**2/2 - lamda*(-mu + z)) + erf(sqrt(2)*(-mu + z)/(2*sigma))/2 + 1/2

    >>> E(X)
    (lamda*mu + 1)/lamda

    >>> simplify(variance(X))
    sigma**2 + lamda**(-2)

    >>> simplify(skewness(X))
    2/(lamda**2*sigma**2 + 1)**(3/2)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Exponentially_modified_Gaussian_distribution
    '''

class ExponentialDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(rate) -> None: ...
    def pdf(self, x): ...

def Exponential(name, rate):
    '''
    Create a continuous random variable with an Exponential distribution.

    Explanation
    ===========

    The density of the exponential distribution is given by

    .. math::
        f(x) := \\lambda \\exp(-\\lambda x)

    with $x > 0$. Note that the expected value is `1/\\lambda`.

    Parameters
    ==========

    rate : A positive Real number, `\\lambda > 0`, the rate (or inverse scale/inverse mean)

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Exponential, density, cdf, E
    >>> from sympy.stats import variance, std, skewness, quantile
    >>> from sympy import Symbol

    >>> l = Symbol("lambda", positive=True)
    >>> z = Symbol("z")
    >>> p = Symbol("p")
    >>> X = Exponential("x", l)

    >>> density(X)(z)
    lambda*exp(-lambda*z)

    >>> cdf(X)(z)
    Piecewise((1 - exp(-lambda*z), z >= 0), (0, True))

    >>> quantile(X)(p)
    -log(1 - p)/lambda

    >>> E(X)
    1/lambda

    >>> variance(X)
    lambda**(-2)

    >>> skewness(X)
    2

    >>> X = Exponential(\'x\', 10)

    >>> density(X)(z)
    10*exp(-10*z)

    >>> E(X)
    1/10

    >>> std(X)
    1/10

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Exponential_distribution
    .. [2] https://mathworld.wolfram.com/ExponentialDistribution.html

    '''

class ExponentialPowerDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, alpha, beta) -> None: ...
    def pdf(self, x): ...

def ExponentialPower(name, mu, alpha, beta):
    '''
    Create a Continuous Random Variable with Exponential Power distribution.
    This distribution is known also as Generalized Normal
    distribution version 1.

    Explanation
    ===========

    The density of the Exponential Power distribution is given by

    .. math::
        f(x) := \\frac{\\beta}{2\\alpha\\Gamma(\\frac{1}{\\beta})}
            e^{{-(\\frac{|x - \\mu|}{\\alpha})^{\\beta}}}

    with :math:`x \\in [ - \\infty, \\infty ]`.

    Parameters
    ==========

    mu : Real number
        A location.
    alpha : Real number,`\\alpha > 0`
        A  scale.
    beta : Real number, `\\beta > 0`
        A shape.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import ExponentialPower, density, cdf
    >>> from sympy import Symbol, pprint
    >>> z = Symbol("z")
    >>> mu = Symbol("mu")
    >>> alpha = Symbol("alpha", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> X = ExponentialPower("x", mu, alpha, beta)
    >>> pprint(density(X)(z), use_unicode=False)
                     beta
           /|mu - z|\\\n          -|--------|
           \\ alpha  /
    beta*e
    ---------------------
                  / 1  \\\n     2*alpha*Gamma|----|
                  \\beta/
    >>> cdf(X)(z)
    1/2 + lowergamma(1/beta, (Abs(mu - z)/alpha)**beta)*sign(-mu + z)/(2*gamma(1/beta))

    References
    ==========

    .. [1] https://reference.wolfram.com/language/ref/ExponentialPowerDistribution.html
    .. [2] https://en.wikipedia.org/wiki/Generalized_normal_distribution#Version_1

    '''

class FDistributionDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(d1, d2) -> None: ...
    def pdf(self, x): ...

def FDistribution(name, d1, d2):
    '''
    Create a continuous random variable with a F distribution.

    Explanation
    ===========

    The density of the F distribution is given by

    .. math::
        f(x) := \\frac{\\sqrt{\\frac{(d_1 x)^{d_1} d_2^{d_2}}
                {(d_1 x + d_2)^{d_1 + d_2}}}}
                {x \\mathrm{B} \\left(\\frac{d_1}{2}, \\frac{d_2}{2}\\right)}

    with :math:`x > 0`.

    Parameters
    ==========

    d1 : `d_1 > 0`, where `d_1` is the degrees of freedom (`n_1 - 1`)
    d2 : `d_2 > 0`, where `d_2` is the degrees of freedom (`n_2 - 1`)

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import FDistribution, density
    >>> from sympy import Symbol, pprint

    >>> d1 = Symbol("d1", positive=True)
    >>> d2 = Symbol("d2", positive=True)
    >>> z = Symbol("z")

    >>> X = FDistribution("x", d1, d2)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
      d2
      --    ______________________________
      2    /       d1            -d1 - d2
    d2  *\\/  (d1*z)  *(d1*z + d2)
    --------------------------------------
                    /d1  d2\\\n                 z*B|--, --|
                    \\2   2 /

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/F-distribution
    .. [2] https://mathworld.wolfram.com/F-Distribution.html

    '''

class FisherZDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(d1, d2) -> None: ...
    def pdf(self, x): ...

def FisherZ(name, d1, d2):
    '''
    Create a Continuous Random Variable with an Fisher\'s Z distribution.

    Explanation
    ===========

    The density of the Fisher\'s Z distribution is given by

    .. math::
        f(x) := \\frac{2d_1^{d_1/2} d_2^{d_2/2}} {\\mathrm{B}(d_1/2, d_2/2)}
                \\frac{e^{d_1z}}{\\left(d_1e^{2z}+d_2\\right)^{\\left(d_1+d_2\\right)/2}}


    .. TODO - What is the difference between these degrees of freedom?

    Parameters
    ==========

    d1 : `d_1 > 0`
        Degree of freedom.
    d2 : `d_2 > 0`
        Degree of freedom.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import FisherZ, density
    >>> from sympy import Symbol, pprint

    >>> d1 = Symbol("d1", positive=True)
    >>> d2 = Symbol("d2", positive=True)
    >>> z = Symbol("z")

    >>> X = FisherZ("x", d1, d2)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                                d1   d2
        d1   d2               - -- - --
        --   --                 2    2
        2    2  /    2*z     \\           d1*z
    2*d1  *d2  *\\d1*e    + d2/         *e
    -----------------------------------------
                     /d1  d2\\\n                    B|--, --|
                     \\2   2 /

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fisher%27s_z-distribution
    .. [2] https://mathworld.wolfram.com/Fishersz-Distribution.html

    '''

class FrechetDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(a, s, m) -> None: ...
    def __new__(cls, a, s: int = 1, m: int = 0): ...
    def pdf(self, x): ...

def Frechet(name, a, s: int = 1, m: int = 0):
    '''
    Create a continuous random variable with a Frechet distribution.

    Explanation
    ===========

    The density of the Frechet distribution is given by

    .. math::
        f(x) := \\frac{\\alpha}{s} \\left(\\frac{x-m}{s}\\right)^{-1-\\alpha}
                 e^{-(\\frac{x-m}{s})^{-\\alpha}}

    with :math:`x \\geq m`.

    Parameters
    ==========

    a : Real number, :math:`a \\in \\left(0, \\infty\\right)` the shape
    s : Real number, :math:`s \\in \\left(0, \\infty\\right)` the scale
    m : Real number, :math:`m \\in \\left(-\\infty, \\infty\\right)` the minimum

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Frechet, density, cdf
    >>> from sympy import Symbol

    >>> a = Symbol("a", positive=True)
    >>> s = Symbol("s", positive=True)
    >>> m = Symbol("m", real=True)
    >>> z = Symbol("z")

    >>> X = Frechet("x", a, s, m)

    >>> density(X)(z)
    a*((-m + z)/s)**(-a - 1)*exp(-1/((-m + z)/s)**a)/s

    >>> cdf(X)(z)
    Piecewise((exp(-1/((-m + z)/s)**a), m <= z), (0, True))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fr%C3%A9chet_distribution

    '''

class GammaDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(k, theta) -> None: ...
    def pdf(self, x): ...

def Gamma(name, k, theta):
    '''
    Create a continuous random variable with a Gamma distribution.

    Explanation
    ===========

    The density of the Gamma distribution is given by

    .. math::
        f(x) := \\frac{1}{\\Gamma(k) \\theta^k} x^{k - 1} e^{-\\frac{x}{\\theta}}

    with :math:`x \\in [0,1]`.

    Parameters
    ==========

    k : Real number, `k > 0`, a shape
    theta : Real number, `\\theta > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Gamma, density, cdf, E, variance
    >>> from sympy import Symbol, pprint, simplify

    >>> k = Symbol("k", positive=True)
    >>> theta = Symbol("theta", positive=True)
    >>> z = Symbol("z")

    >>> X = Gamma("x", k, theta)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                      -z
                    -----
         -k  k - 1  theta
    theta  *z     *e
    ---------------------
           Gamma(k)

    >>> C = cdf(X, meijerg=True)(z)
    >>> pprint(C, use_unicode=False)
    /            /     z  \\\n    |k*lowergamma|k, -----|
    |            \\   theta/
    <----------------------  for z >= 0
    |     Gamma(k + 1)
    |
    \\          0             otherwise

    >>> E(X)
    k*theta

    >>> V = simplify(variance(X))
    >>> pprint(V, use_unicode=False)
           2
    k*theta


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gamma_distribution
    .. [2] https://mathworld.wolfram.com/GammaDistribution.html

    '''

class GammaInverseDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def GammaInverse(name, a, b):
    '''
    Create a continuous random variable with an inverse Gamma distribution.

    Explanation
    ===========

    The density of the inverse Gamma distribution is given by

    .. math::
        f(x) := \\frac{\\beta^\\alpha}{\\Gamma(\\alpha)} x^{-\\alpha - 1}
                \\exp\\left(\\frac{-\\beta}{x}\\right)

    with :math:`x > 0`.

    Parameters
    ==========

    a : Real number, `a > 0`, a shape
    b : Real number, `b > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import GammaInverse, density, cdf
    >>> from sympy import Symbol, pprint

    >>> a = Symbol("a", positive=True)
    >>> b = Symbol("b", positive=True)
    >>> z = Symbol("z")

    >>> X = GammaInverse("x", a, b)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                -b
                ---
     a  -a - 1   z
    b *z      *e
    ---------------
       Gamma(a)

    >>> cdf(X)(z)
    Piecewise((uppergamma(a, b/z)/gamma(a), z > 0), (0, True))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Inverse-gamma_distribution

    '''

class GumbelDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(beta, mu, minimum) -> None: ...
    def pdf(self, x): ...

def Gumbel(name, beta, mu, minimum: bool = False):
    '''
    Create a Continuous Random Variable with Gumbel distribution.

    Explanation
    ===========

    The density of the Gumbel distribution is given by

    For Maximum

    .. math::
        f(x) := \\dfrac{1}{\\beta} \\exp \\left( -\\dfrac{x-\\mu}{\\beta}
                - \\exp \\left( -\\dfrac{x - \\mu}{\\beta} \\right) \\right)

    with :math:`x \\in [ - \\infty, \\infty ]`.

    For Minimum

    .. math::
        f(x) := \\frac{e^{- e^{\\frac{- \\mu + x}{\\beta}} + \\frac{- \\mu + x}{\\beta}}}{\\beta}

    with :math:`x \\in [ - \\infty, \\infty ]`.

    Parameters
    ==========

    mu : Real number, `\\mu`, a location
    beta : Real number, `\\beta > 0`, a scale
    minimum : Boolean, by default ``False``, set to ``True`` for enabling minimum distribution

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Gumbel, density, cdf
    >>> from sympy import Symbol
    >>> x = Symbol("x")
    >>> mu = Symbol("mu")
    >>> beta = Symbol("beta", positive=True)
    >>> X = Gumbel("x", beta, mu)
    >>> density(X)(x)
    exp(-exp(-(-mu + x)/beta) - (-mu + x)/beta)/beta
    >>> cdf(X)(x)
    exp(-exp(-(-mu + x)/beta))

    References
    ==========

    .. [1] https://mathworld.wolfram.com/GumbelDistribution.html
    .. [2] https://en.wikipedia.org/wiki/Gumbel_distribution
    .. [3] https://web.archive.org/web/20200628222206/http://www.mathwave.com/help/easyfit/html/analyses/distributions/gumbel_max.html
    .. [4] https://web.archive.org/web/20200628222212/http://www.mathwave.com/help/easyfit/html/analyses/distributions/gumbel_min.html

    '''

class GompertzDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(b, eta) -> None: ...
    def pdf(self, x): ...

def Gompertz(name, b, eta):
    '''
    Create a Continuous Random Variable with Gompertz distribution.

    Explanation
    ===========

    The density of the Gompertz distribution is given by

    .. math::
        f(x) := b \\eta e^{b x} e^{\\eta} \\exp \\left(-\\eta e^{bx} \\right)

    with :math:`x \\in [0, \\infty)`.

    Parameters
    ==========

    b : Real number, `b > 0`, a scale
    eta : Real number, `\\eta > 0`, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Gompertz, density
    >>> from sympy import Symbol

    >>> b = Symbol("b", positive=True)
    >>> eta = Symbol("eta", positive=True)
    >>> z = Symbol("z")

    >>> X = Gompertz("x", b, eta)

    >>> density(X)(z)
    b*eta*exp(eta)*exp(b*z)*exp(-eta*exp(b*z))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gompertz_distribution

    '''

class KumaraswamyDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def Kumaraswamy(name, a, b):
    '''
    Create a Continuous Random Variable with a Kumaraswamy distribution.

    Explanation
    ===========

    The density of the Kumaraswamy distribution is given by

    .. math::
        f(x) := a b x^{a-1} (1-x^a)^{b-1}

    with :math:`x \\in [0,1]`.

    Parameters
    ==========

    a : Real number, `a > 0`, a shape
    b : Real number, `b > 0`, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Kumaraswamy, density, cdf
    >>> from sympy import Symbol, pprint

    >>> a = Symbol("a", positive=True)
    >>> b = Symbol("b", positive=True)
    >>> z = Symbol("z")

    >>> X = Kumaraswamy("x", a, b)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                       b - 1
         a - 1 /     a\\\n    a*b*z     *\\1 - z /

    >>> cdf(X)(z)
    Piecewise((0, z < 0), (1 - (1 - z**a)**b, z <= 1), (1, True))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Kumaraswamy_distribution

    '''

class LaplaceDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, b) -> None: ...
    def pdf(self, x): ...

def Laplace(name, mu, b):
    '''
    Create a continuous random variable with a Laplace distribution.

    Explanation
    ===========

    The density of the Laplace distribution is given by

    .. math::
        f(x) := \\frac{1}{2 b} \\exp \\left(-\\frac{|x-\\mu|}b \\right)

    Parameters
    ==========

    mu : Real number or a list/matrix, the location (mean) or the
        location vector
    b : Real number or a positive definite matrix, representing a scale
        or the covariance matrix.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Laplace, density, cdf
    >>> from sympy import Symbol, pprint

    >>> mu = Symbol("mu")
    >>> b = Symbol("b", positive=True)
    >>> z = Symbol("z")

    >>> X = Laplace("x", mu, b)

    >>> density(X)(z)
    exp(-Abs(mu - z)/b)/(2*b)

    >>> cdf(X)(z)
    Piecewise((exp((-mu + z)/b)/2, mu > z), (1 - exp((mu - z)/b)/2, True))

    >>> L = Laplace(\'L\', [1, 2], [[1, 0], [0, 1]])
    >>> pprint(density(L)(1, 2), use_unicode=False)
     5        /     ____\\\n    e *besselk\\0, \\/ 35 /
    ---------------------
              pi

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Laplace_distribution
    .. [2] https://mathworld.wolfram.com/LaplaceDistribution.html

    '''

class LevyDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(mu, c) -> None: ...
    def pdf(self, x): ...

def Levy(name, mu, c):
    '''
    Create a continuous random variable with a Levy distribution.

    The density of the Levy distribution is given by

    .. math::
        f(x) := \\sqrt(\\frac{c}{2 \\pi}) \\frac{\\exp -\\frac{c}{2 (x - \\mu)}}{(x - \\mu)^{3/2}}

    Parameters
    ==========

    mu : Real number
        The location parameter.
    c : Real number, `c > 0`
        A scale parameter.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Levy, density, cdf
    >>> from sympy import Symbol

    >>> mu = Symbol("mu", real=True)
    >>> c = Symbol("c", positive=True)
    >>> z = Symbol("z")

    >>> X = Levy("x", mu, c)

    >>> density(X)(z)
    sqrt(2)*sqrt(c)*exp(-c/(-2*mu + 2*z))/(2*sqrt(pi)*(-mu + z)**(3/2))

    >>> cdf(X)(z)
    erfc(sqrt(c)*sqrt(1/(-2*mu + 2*z)))

    References
    ==========
    .. [1] https://en.wikipedia.org/wiki/L%C3%A9vy_distribution
    .. [2] https://mathworld.wolfram.com/LevyDistribution.html
    '''

class LogCauchyDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, sigma) -> None: ...
    def pdf(self, x): ...

def LogCauchy(name, mu, sigma):
    '''
    Create a continuous random variable with a Log-Cauchy distribution.
    The density of the Log-Cauchy distribution is given by

    .. math::
        f(x) := \\frac{1}{\\pi x} \\frac{\\sigma}{(log(x)-\\mu^2) + \\sigma^2}

    Parameters
    ==========

    mu : Real number, the location

    sigma : Real number, `\\sigma > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import LogCauchy, density, cdf
    >>> from sympy import Symbol, S

    >>> mu = 2
    >>> sigma = S.One / 5
    >>> z = Symbol("z")

    >>> X = LogCauchy("x", mu, sigma)

    >>> density(X)(z)
    1/(5*pi*z*((log(z) - 2)**2 + 1/25))

    >>> cdf(X)(z)
    atan(5*log(z) - 10)/pi + 1/2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Log-Cauchy_distribution
    '''

class LogisticDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, s) -> None: ...
    def pdf(self, x): ...

def Logistic(name, mu, s):
    '''
    Create a continuous random variable with a logistic distribution.

    Explanation
    ===========

    The density of the logistic distribution is given by

    .. math::
        f(x) := \\frac{e^{-(x-\\mu)/s}} {s\\left(1+e^{-(x-\\mu)/s}\\right)^2}

    Parameters
    ==========

    mu : Real number, the location (mean)
    s : Real number, `s > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Logistic, density, cdf
    >>> from sympy import Symbol

    >>> mu = Symbol("mu", real=True)
    >>> s = Symbol("s", positive=True)
    >>> z = Symbol("z")

    >>> X = Logistic("x", mu, s)

    >>> density(X)(z)
    exp((mu - z)/s)/(s*(exp((mu - z)/s) + 1)**2)

    >>> cdf(X)(z)
    1/(exp((mu - z)/s) + 1)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Logistic_distribution
    .. [2] https://mathworld.wolfram.com/LogisticDistribution.html

    '''

class LogLogisticDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(alpha, beta) -> None: ...
    def pdf(self, x): ...
    def expectation(self, expr, var, **kwargs): ...

def LogLogistic(name, alpha, beta):
    '''
    Create a continuous random variable with a log-logistic distribution.
    The distribution is unimodal when ``beta > 1``.

    Explanation
    ===========

    The density of the log-logistic distribution is given by

    .. math::
        f(x) := \\frac{(\\frac{\\beta}{\\alpha})(\\frac{x}{\\alpha})^{\\beta - 1}}
                {(1 + (\\frac{x}{\\alpha})^{\\beta})^2}

    Parameters
    ==========

    alpha : Real number, `\\alpha > 0`, scale parameter and median of distribution
    beta : Real number, `\\beta > 0`, a shape parameter

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import LogLogistic, density, cdf, quantile
    >>> from sympy import Symbol, pprint

    >>> alpha = Symbol("alpha", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> p = Symbol("p")
    >>> z = Symbol("z", positive=True)

    >>> X = LogLogistic("x", alpha, beta)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                  beta - 1
           /  z  \\\n      beta*|-----|
           \\alpha/
    ------------------------
                           2
          /       beta    \\\n          |/  z  \\        |
    alpha*||-----|     + 1|
          \\\\alpha/        /

    >>> cdf(X)(z)
    1/(1 + (z/alpha)**(-beta))

    >>> quantile(X)(p)
    alpha*(p/(1 - p))**(1/beta)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Log-logistic_distribution

    '''

class LogitNormalDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, s) -> None: ...
    def pdf(self, x): ...

def LogitNormal(name, mu, s):
    '''
    Create a continuous random variable with a Logit-Normal distribution.

    The density of the logistic distribution is given by

    .. math::
        f(x) := \\frac{1}{s \\sqrt{2 \\pi}} \\frac{1}{x(1 - x)} e^{- \\frac{(logit(x)  - \\mu)^2}{s^2}}
        where logit(x) = \\log(\\frac{x}{1 - x})
    Parameters
    ==========

    mu : Real number, the location (mean)
    s : Real number, `s > 0`, a scale

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import LogitNormal, density, cdf
    >>> from sympy import Symbol,pprint

    >>> mu = Symbol("mu", real=True)
    >>> s = Symbol("s", positive=True)
    >>> z = Symbol("z")
    >>> X = LogitNormal("x",mu,s)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                              2
            /         /  z  \\\\\n           -|-mu + log|-----||
            \\         \\1 - z//
           ---------------------
                       2
      ___           2*s
    \\/ 2 *e
    ----------------------------
            ____
        2*\\/ pi *s*z*(1 - z)

    >>> density(X)(z)
    sqrt(2)*exp(-(-mu + log(z/(1 - z)))**2/(2*s**2))/(2*sqrt(pi)*s*z*(1 - z))

    >>> cdf(X)(z)
    erf(sqrt(2)*(-mu + log(z/(1 - z)))/(2*s))/2 + 1/2


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Logit-normal_distribution

    '''

class LogNormalDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mean, std) -> None: ...
    def pdf(self, x): ...

def LogNormal(name, mean, std):
    '''
    Create a continuous random variable with a log-normal distribution.

    Explanation
    ===========

    The density of the log-normal distribution is given by

    .. math::
        f(x) := \\frac{1}{x\\sqrt{2\\pi\\sigma^2}}
                e^{-\\frac{\\left(\\ln x-\\mu\\right)^2}{2\\sigma^2}}

    with :math:`x \\geq 0`.

    Parameters
    ==========

    mu : Real number
        The log-scale.
    sigma : Real number
        A shape. ($\\sigma^2 > 0$)

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import LogNormal, density
    >>> from sympy import Symbol, pprint

    >>> mu = Symbol("mu", real=True)
    >>> sigma = Symbol("sigma", positive=True)
    >>> z = Symbol("z")

    >>> X = LogNormal("x", mu, sigma)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                          2
           -(-mu + log(z))
           -----------------
                      2
      ___      2*sigma
    \\/ 2 *e
    ------------------------
            ____
        2*\\/ pi *sigma*z


    >>> X = LogNormal(\'x\', 0, 1) # Mean 0, standard deviation 1

    >>> density(X)(z)
    sqrt(2)*exp(-log(z)**2/2)/(2*sqrt(pi)*z)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lognormal
    .. [2] https://mathworld.wolfram.com/LogNormalDistribution.html

    '''

class LomaxDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(alpha, lamda) -> None: ...
    def pdf(self, x): ...

def Lomax(name, alpha, lamda):
    """
    Create a continuous random variable with a Lomax distribution.

    Explanation
    ===========

    The density of the Lomax distribution is given by

    .. math::
        f(x) := \\frac{\\alpha}{\\lambda}\\left[1+\\frac{x}{\\lambda}\\right]^{-(\\alpha+1)}

    Parameters
    ==========

    alpha : Real Number, `\\alpha > 0`
        Shape parameter
    lamda : Real Number, `\\lambda > 0`
        Scale parameter

    Examples
    ========

    >>> from sympy.stats import Lomax, density, cdf, E
    >>> from sympy import symbols
    >>> a, l = symbols('a, l', positive=True)
    >>> X = Lomax('X', a, l)
    >>> x = symbols('x')
    >>> density(X)(x)
    a*(1 + x/l)**(-a - 1)/l
    >>> cdf(X)(x)
    Piecewise((1 - 1/(1 + x/l)**a, x >= 0), (0, True))
    >>> a = 2
    >>> X = Lomax('X', a, l)
    >>> E(X)
    l

    Returns
    =======

    RandomSymbol

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Lomax_distribution

    """

class MaxwellDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(a) -> None: ...
    def pdf(self, x): ...

def Maxwell(name, a):
    '''
    Create a continuous random variable with a Maxwell distribution.

    Explanation
    ===========

    The density of the Maxwell distribution is given by

    .. math::
        f(x) := \\sqrt{\\frac{2}{\\pi}} \\frac{x^2 e^{-x^2/(2a^2)}}{a^3}

    with :math:`x \\geq 0`.

    .. TODO - what does the parameter mean?

    Parameters
    ==========

    a : Real number, `a > 0`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Maxwell, density, E, variance
    >>> from sympy import Symbol, simplify

    >>> a = Symbol("a", positive=True)
    >>> z = Symbol("z")

    >>> X = Maxwell("x", a)

    >>> density(X)(z)
    sqrt(2)*z**2*exp(-z**2/(2*a**2))/(sqrt(pi)*a**3)

    >>> E(X)
    2*sqrt(2)*a/sqrt(pi)

    >>> simplify(variance(X))
    a**2*(-8 + 3*pi)/pi

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Maxwell_distribution
    .. [2] https://mathworld.wolfram.com/MaxwellDistribution.html

    '''

class MoyalDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(mu, sigma) -> None: ...
    def pdf(self, x): ...

def Moyal(name, mu, sigma):
    '''
    Create a continuous random variable with a Moyal distribution.

    Explanation
    ===========

    The density of the Moyal distribution is given by

    .. math::
        f(x) := \\frac{\\exp-\\frac{1}{2}\\exp-\\frac{x-\\mu}{\\sigma}-\\frac{x-\\mu}{2\\sigma}}{\\sqrt{2\\pi}\\sigma}

    with :math:`x \\in \\mathbb{R}`.

    Parameters
    ==========

    mu : Real number
        Location parameter
    sigma : Real positive number
        Scale parameter

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Moyal, density, cdf
    >>> from sympy import Symbol, simplify
    >>> mu = Symbol("mu", real=True)
    >>> sigma = Symbol("sigma", positive=True, real=True)
    >>> z = Symbol("z")
    >>> X = Moyal("x", mu, sigma)
    >>> density(X)(z)
    sqrt(2)*exp(-exp((mu - z)/sigma)/2 - (-mu + z)/(2*sigma))/(2*sqrt(pi)*sigma)
    >>> simplify(cdf(X)(z))
    1 - erf(sqrt(2)*exp((mu - z)/(2*sigma))/2)

    References
    ==========

    .. [1] https://reference.wolfram.com/language/ref/MoyalDistribution.html
    .. [2] https://www.stat.rice.edu/~dobelman/textfiles/DistributionsHandbook.pdf

    '''

class NakagamiDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, omega) -> None: ...
    def pdf(self, x): ...

def Nakagami(name, mu, omega):
    '''
    Create a continuous random variable with a Nakagami distribution.

    Explanation
    ===========

    The density of the Nakagami distribution is given by

    .. math::
        f(x) := \\frac{2\\mu^\\mu}{\\Gamma(\\mu)\\omega^\\mu} x^{2\\mu-1}
                \\exp\\left(-\\frac{\\mu}{\\omega}x^2 \\right)

    with :math:`x > 0`.

    Parameters
    ==========

    mu : Real number, `\\mu \\geq \\frac{1}{2}`, a shape
    omega : Real number, `\\omega > 0`, the spread

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Nakagami, density, E, variance, cdf
    >>> from sympy import Symbol, simplify, pprint

    >>> mu = Symbol("mu", positive=True)
    >>> omega = Symbol("omega", positive=True)
    >>> z = Symbol("z")

    >>> X = Nakagami("x", mu, omega)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                                    2
                               -mu*z
                               -------
        mu      -mu  2*mu - 1  omega
    2*mu  *omega   *z        *e
    ----------------------------------
                Gamma(mu)

    >>> simplify(E(X))
    sqrt(mu)*sqrt(omega)*gamma(mu + 1/2)/gamma(mu + 1)

    >>> V = simplify(variance(X))
    >>> pprint(V, use_unicode=False)
                        2
             omega*Gamma (mu + 1/2)
    omega - -----------------------
            Gamma(mu)*Gamma(mu + 1)

    >>> cdf(X)(z)
    Piecewise((lowergamma(mu, mu*z**2/omega)/gamma(mu), z > 0),
            (0, True))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Nakagami_distribution

    '''

class NormalDistribution(SingleContinuousDistribution):
    @staticmethod
    def check(mean, std) -> None: ...
    def pdf(self, x): ...

def Normal(name, mean, std):
    '''
    Create a continuous random variable with a Normal distribution.

    Explanation
    ===========

    The density of the Normal distribution is given by

    .. math::
        f(x) := \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{ -\\frac{(x-\\mu)^2}{2\\sigma^2} }

    Parameters
    ==========

    mu : Real number or a list representing the mean or the mean vector
    sigma : Real number or a positive definite square matrix,
         :math:`\\sigma^2 > 0`, the variance

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Normal, density, E, std, cdf, skewness, quantile, marginal_distribution
    >>> from sympy import Symbol, simplify, pprint

    >>> mu = Symbol("mu")
    >>> sigma = Symbol("sigma", positive=True)
    >>> z = Symbol("z")
    >>> y = Symbol("y")
    >>> p = Symbol("p")
    >>> X = Normal("x", mu, sigma)

    >>> density(X)(z)
    sqrt(2)*exp(-(-mu + z)**2/(2*sigma**2))/(2*sqrt(pi)*sigma)

    >>> C = simplify(cdf(X))(z) # it needs a little more help...
    >>> pprint(C, use_unicode=False)
       /  ___          \\\n       |\\/ 2 *(-mu + z)|
    erf|---------------|
       \\    2*sigma    /   1
    -------------------- + -
             2             2

    >>> quantile(X)(p)
    mu + sqrt(2)*sigma*erfinv(2*p - 1)

    >>> simplify(skewness(X))
    0

    >>> X = Normal("x", 0, 1) # Mean 0, standard deviation 1
    >>> density(X)(z)
    sqrt(2)*exp(-z**2/2)/(2*sqrt(pi))

    >>> E(2*X + 1)
    1

    >>> simplify(std(2*X + 1))
    2

    >>> m = Normal(\'X\', [1, 2], [[2, 1], [1, 2]])
    >>> pprint(density(m)(y, z), use_unicode=False)
              2          2
             y    y*z   z
           - -- + --- - -- + z - 1
      ___    3     3    3
    \\/ 3 *e
    ------------------------------
                 6*pi

    >>> marginal_distribution(m, m[0])(1)
     1/(2*sqrt(pi))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Normal_distribution
    .. [2] https://mathworld.wolfram.com/NormalDistributionFunction.html

    '''

class GaussianInverseDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(mean, shape) -> None: ...
    def pdf(self, x): ...

def GaussianInverse(name, mean, shape):
    '''
    Create a continuous random variable with an Inverse Gaussian distribution.
    Inverse Gaussian distribution is also known as Wald distribution.

    Explanation
    ===========

    The density of the Inverse Gaussian distribution is given by

    .. math::
        f(x) := \\sqrt{\\frac{\\lambda}{2\\pi x^3}} e^{-\\frac{\\lambda(x-\\mu)^2}{2x\\mu^2}}

    Parameters
    ==========

    mu :
        Positive number representing the mean.
    lambda :
        Positive number representing the shape parameter.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import GaussianInverse, density, E, std, skewness
    >>> from sympy import Symbol, pprint

    >>> mu = Symbol("mu", positive=True)
    >>> lamda = Symbol("lambda", positive=True)
    >>> z = Symbol("z", positive=True)
    >>> X = GaussianInverse("x", mu, lamda)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
                                       2
                      -lambda*(-mu + z)
                      -------------------
                                2
      ___   ________        2*mu *z
    \\/ 2 *\\/ lambda *e
    -------------------------------------
                    ____  3/2
                2*\\/ pi *z

    >>> E(X)
    mu

    >>> std(X).expand()
    mu**(3/2)/sqrt(lambda)

    >>> skewness(X).expand()
    3*sqrt(mu)/sqrt(lambda)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution
    .. [2] https://mathworld.wolfram.com/InverseGaussianDistribution.html

    '''
Wald = GaussianInverse

class ParetoDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(xm, alpha) -> None: ...
    def pdf(self, x): ...

def Pareto(name, xm, alpha):
    '''
    Create a continuous random variable with the Pareto distribution.

    Explanation
    ===========

    The density of the Pareto distribution is given by

    .. math::
        f(x) := \\frac{\\alpha\\,x_m^\\alpha}{x^{\\alpha+1}}

    with :math:`x \\in [x_m,\\infty]`.

    Parameters
    ==========

    xm : Real number, `x_m > 0`, a scale
    alpha : Real number, `\\alpha > 0`, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Pareto, density
    >>> from sympy import Symbol

    >>> xm = Symbol("xm", positive=True)
    >>> beta = Symbol("beta", positive=True)
    >>> z = Symbol("z")

    >>> X = Pareto("x", xm, beta)

    >>> density(X)(z)
    beta*xm**beta*z**(-beta - 1)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Pareto_distribution
    .. [2] https://mathworld.wolfram.com/ParetoDistribution.html

    '''

class PowerFunctionDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(alpha, a, b) -> None: ...
    def pdf(self, x): ...

def PowerFunction(name, alpha, a, b):
    '''
    Creates a continuous random variable with a Power Function Distribution.

    Explanation
    ===========

    The density of PowerFunction distribution is given by

    .. math::
        f(x) := \\frac{{\\alpha}(x - a)^{\\alpha - 1}}{(b - a)^{\\alpha}}

    with :math:`x \\in [a,b]`.

    Parameters
    ==========

    alpha : Positive number, `0 < \\alpha`, the shape parameter
    a : Real number, :math:`-\\infty < a`, the left boundary
    b : Real number, :math:`a < b < \\infty`, the right boundary

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import PowerFunction, density, cdf, E, variance
    >>> from sympy import Symbol
    >>> alpha = Symbol("alpha", positive=True)
    >>> a = Symbol("a", real=True)
    >>> b = Symbol("b", real=True)
    >>> z = Symbol("z")

    >>> X = PowerFunction("X", 2, a, b)

    >>> density(X)(z)
    (-2*a + 2*z)/(-a + b)**2

    >>> cdf(X)(z)
    Piecewise((a**2/(a**2 - 2*a*b + b**2) - 2*a*z/(a**2 - 2*a*b + b**2) +
    z**2/(a**2 - 2*a*b + b**2), a <= z), (0, True))

    >>> alpha = 2
    >>> a = 0
    >>> b = 1
    >>> Y = PowerFunction("Y", alpha, a, b)

    >>> E(Y)
    2/3

    >>> variance(Y)
    1/18

    References
    ==========

    .. [1] https://web.archive.org/web/20200204081320/http://www.mathwave.com/help/easyfit/html/analyses/distributions/power_func.html

    '''

class QuadraticUDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def QuadraticU(name, a, b):
    '''
    Create a Continuous Random Variable with a U-quadratic distribution.

    Explanation
    ===========

    The density of the U-quadratic distribution is given by

    .. math::
        f(x) := \\alpha (x-\\beta)^2

    with :math:`x \\in [a,b]`.

    Parameters
    ==========

    a : Real number
    b : Real number, :math:`a < b`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import QuadraticU, density
    >>> from sympy import Symbol, pprint

    >>> a = Symbol("a", real=True)
    >>> b = Symbol("b", real=True)
    >>> z = Symbol("z")

    >>> X = QuadraticU("x", a, b)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
    /                2
    |   /  a   b    \\\n    |12*|- - - - + z|
    |   \\  2   2    /
    <-----------------  for And(b >= z, a <= z)
    |            3
    |    (-a + b)
    |
    \\        0                 otherwise

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/U-quadratic_distribution

    '''

class RaisedCosineDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(mu, s) -> None: ...
    def pdf(self, x): ...

def RaisedCosine(name, mu, s):
    '''
    Create a Continuous Random Variable with a raised cosine distribution.

    Explanation
    ===========

    The density of the raised cosine distribution is given by

    .. math::
        f(x) := \\frac{1}{2s}\\left(1+\\cos\\left(\\frac{x-\\mu}{s}\\pi\\right)\\right)

    with :math:`x \\in [\\mu-s,\\mu+s]`.

    Parameters
    ==========

    mu : Real number
    s : Real number, `s > 0`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import RaisedCosine, density
    >>> from sympy import Symbol, pprint

    >>> mu = Symbol("mu", real=True)
    >>> s = Symbol("s", positive=True)
    >>> z = Symbol("z")

    >>> X = RaisedCosine("x", mu, s)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
    /   /pi*(-mu + z)\\\n    |cos|------------| + 1
    |   \\     s      /
    <---------------------  for And(z >= mu - s, z <= mu + s)
    |         2*s
    |
    \\          0                        otherwise

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Raised_cosine_distribution

    '''

class RayleighDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(sigma) -> None: ...
    def pdf(self, x): ...

def Rayleigh(name, sigma):
    '''
    Create a continuous random variable with a Rayleigh distribution.

    Explanation
    ===========

    The density of the Rayleigh distribution is given by

    .. math ::
        f(x) := \\frac{x}{\\sigma^2} e^{-x^2/2\\sigma^2}

    with :math:`x > 0`.

    Parameters
    ==========

    sigma : Real number, `\\sigma > 0`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Rayleigh, density, E, variance
    >>> from sympy import Symbol

    >>> sigma = Symbol("sigma", positive=True)
    >>> z = Symbol("z")

    >>> X = Rayleigh("x", sigma)

    >>> density(X)(z)
    z*exp(-z**2/(2*sigma**2))/sigma**2

    >>> E(X)
    sqrt(2)*sqrt(pi)*sigma/2

    >>> variance(X)
    -pi*sigma**2/2 + 2*sigma**2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Rayleigh_distribution
    .. [2] https://mathworld.wolfram.com/RayleighDistribution.html

    '''

class ReciprocalDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def Reciprocal(name, a, b):
    """Creates a continuous random variable with a reciprocal distribution.


    Parameters
    ==========

    a : Real number, :math:`0 < a`
    b : Real number, :math:`a < b`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Reciprocal, density, cdf
    >>> from sympy import symbols
    >>> a, b, x = symbols('a, b, x', positive=True)
    >>> R = Reciprocal('R', a, b)

    >>> density(R)(x)
    1/(x*(-log(a) + log(b)))
    >>> cdf(R)(x)
    Piecewise((log(a)/(log(a) - log(b)) - log(x)/(log(a) - log(b)), a <= x), (0, True))

    Reference
    =========

    .. [1] https://en.wikipedia.org/wiki/Reciprocal_distribution

    """

class ShiftedGompertzDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(b, eta) -> None: ...
    def pdf(self, x): ...

def ShiftedGompertz(name, b, eta):
    '''
    Create a continuous random variable with a Shifted Gompertz distribution.

    Explanation
    ===========

    The density of the Shifted Gompertz distribution is given by

    .. math::
        f(x) := b e^{-b x} e^{-\\eta \\exp(-b x)} \\left[1 + \\eta(1 - e^(-bx)) \\right]

    with :math:`x \\in [0, \\infty)`.

    Parameters
    ==========

    b : Real number, `b > 0`, a scale
    eta : Real number, `\\eta > 0`, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========
    >>> from sympy.stats import ShiftedGompertz, density
    >>> from sympy import Symbol

    >>> b = Symbol("b", positive=True)
    >>> eta = Symbol("eta", positive=True)
    >>> x = Symbol("x")

    >>> X = ShiftedGompertz("x", b, eta)

    >>> density(X)(x)
    b*(eta*(1 - exp(-b*x)) + 1)*exp(-b*x)*exp(-eta*exp(-b*x))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Shifted_Gompertz_distribution

    '''

class StudentTDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(nu) -> None: ...
    def pdf(self, x): ...

def StudentT(name, nu):
    '''
    Create a continuous random variable with a student\'s t distribution.

    Explanation
    ===========

    The density of the student\'s t distribution is given by

    .. math::
        f(x) := \\frac{\\Gamma \\left(\\frac{\\nu+1}{2} \\right)}
                {\\sqrt{\\nu\\pi}\\Gamma \\left(\\frac{\\nu}{2} \\right)}
                \\left(1+\\frac{x^2}{\\nu} \\right)^{-\\frac{\\nu+1}{2}}

    Parameters
    ==========

    nu : Real number, `\\nu > 0`, the degrees of freedom

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import StudentT, density, cdf
    >>> from sympy import Symbol, pprint

    >>> nu = Symbol("nu", positive=True)
    >>> z = Symbol("z")

    >>> X = StudentT("x", nu)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
               nu   1
             - -- - -
               2    2
     /     2\\\n     |    z |
     |1 + --|
     \\    nu/
    -----------------
      ____  /     nu\\\n    \\/ nu *B|1/2, --|
            \\     2 /

    >>> cdf(X)(z)
    1/2 + z*gamma(nu/2 + 1/2)*hyper((1/2, nu/2 + 1/2), (3/2,),
                                -z**2/nu)/(sqrt(pi)*sqrt(nu)*gamma(nu/2))


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Student_t-distribution
    .. [2] https://mathworld.wolfram.com/Studentst-Distribution.html

    '''

class TrapezoidalDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(a, b, c, d) -> None: ...
    def pdf(self, x): ...

def Trapezoidal(name, a, b, c, d):
    '''
    Create a continuous random variable with a trapezoidal distribution.

    Explanation
    ===========

    The density of the trapezoidal distribution is given by

    .. math::
        f(x) := \\begin{cases}
                  0 & \\mathrm{for\\ } x < a, \\\\\n                  \\frac{2(x-a)}{(b-a)(d+c-a-b)} & \\mathrm{for\\ } a \\le x < b, \\\\\n                  \\frac{2}{d+c-a-b} & \\mathrm{for\\ } b \\le x < c, \\\\\n                  \\frac{2(d-x)}{(d-c)(d+c-a-b)} & \\mathrm{for\\ } c \\le x < d, \\\\\n                  0 & \\mathrm{for\\ } d < x.
                \\end{cases}

    Parameters
    ==========

    a : Real number, :math:`a < d`
    b : Real number, :math:`a \\le b < c`
    c : Real number, :math:`b < c \\le d`
    d : Real number

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Trapezoidal, density
    >>> from sympy import Symbol, pprint

    >>> a = Symbol("a")
    >>> b = Symbol("b")
    >>> c = Symbol("c")
    >>> d = Symbol("d")
    >>> z = Symbol("z")

    >>> X = Trapezoidal("x", a,b,c,d)

    >>> pprint(density(X)(z), use_unicode=False)
    /        -2*a + 2*z
    |-------------------------  for And(a <= z, b > z)
    |(-a + b)*(-a - b + c + d)
    |
    |           2
    |     --------------        for And(b <= z, c > z)
    <     -a - b + c + d
    |
    |        2*d - 2*z
    |-------------------------  for And(d >= z, c <= z)
    |(-c + d)*(-a - b + c + d)
    |
    \\            0                     otherwise

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trapezoidal_distribution

    '''

class TriangularDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(a, b, c) -> None: ...
    def pdf(self, x): ...

def Triangular(name, a, b, c):
    '''
    Create a continuous random variable with a triangular distribution.

    Explanation
    ===========

    The density of the triangular distribution is given by

    .. math::
        f(x) := \\begin{cases}
                  0 & \\mathrm{for\\ } x < a, \\\\\n                  \\frac{2(x-a)}{(b-a)(c-a)} & \\mathrm{for\\ } a \\le x < c, \\\\\n                  \\frac{2}{b-a} & \\mathrm{for\\ } x = c, \\\\\n                  \\frac{2(b-x)}{(b-a)(b-c)} & \\mathrm{for\\ } c < x \\le b, \\\\\n                  0 & \\mathrm{for\\ } b < x.
                \\end{cases}

    Parameters
    ==========

    a : Real number, :math:`a \\in \\left(-\\infty, \\infty\\right)`
    b : Real number, :math:`a < b`
    c : Real number, :math:`a \\leq c \\leq b`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Triangular, density
    >>> from sympy import Symbol, pprint

    >>> a = Symbol("a")
    >>> b = Symbol("b")
    >>> c = Symbol("c")
    >>> z = Symbol("z")

    >>> X = Triangular("x", a,b,c)

    >>> pprint(density(X)(z), use_unicode=False)
    /    -2*a + 2*z
    |-----------------  for And(a <= z, c > z)
    |(-a + b)*(-a + c)
    |
    |       2
    |     ------              for c = z
    <     -a + b
    |
    |   2*b - 2*z
    |----------------   for And(b >= z, c < z)
    |(-a + b)*(b - c)
    |
    \\        0                otherwise

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Triangular_distribution
    .. [2] https://mathworld.wolfram.com/TriangularDistribution.html

    '''

class UniformDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(left, right) -> None: ...
    def pdf(self, x): ...
    def expectation(self, expr, var, **kwargs): ...

def Uniform(name, left, right):
    '''
    Create a continuous random variable with a uniform distribution.

    Explanation
    ===========

    The density of the uniform distribution is given by

    .. math::
        f(x) := \\begin{cases}
                  \\frac{1}{b - a} & \\text{for } x \\in [a,b]  \\\\\n                  0               & \\text{otherwise}
                \\end{cases}

    with :math:`x \\in [a,b]`.

    Parameters
    ==========

    a : Real number, :math:`-\\infty < a`, the left boundary
    b : Real number, :math:`a < b < \\infty`, the right boundary

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Uniform, density, cdf, E, variance
    >>> from sympy import Symbol, simplify

    >>> a = Symbol("a", negative=True)
    >>> b = Symbol("b", positive=True)
    >>> z = Symbol("z")

    >>> X = Uniform("x", a, b)

    >>> density(X)(z)
    Piecewise((1/(-a + b), (b >= z) & (a <= z)), (0, True))

    >>> cdf(X)(z)
    Piecewise((0, a > z), ((-a + z)/(-a + b), b >= z), (1, True))

    >>> E(X)
    a/2 + b/2

    >>> simplify(variance(X))
    a**2/12 - a*b/6 + b**2/12

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Uniform_distribution_%28continuous%29
    .. [2] https://mathworld.wolfram.com/UniformDistribution.html

    '''

class UniformSumDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(n) -> None: ...
    def pdf(self, x): ...

def UniformSum(name, n):
    '''
    Create a continuous random variable with an Irwin-Hall distribution.

    Explanation
    ===========

    The probability distribution function depends on a single parameter
    $n$ which is an integer.

    The density of the Irwin-Hall distribution is given by

    .. math ::
        f(x) := \\frac{1}{(n-1)!}\\sum_{k=0}^{\\left\\lfloor x\\right\\rfloor}(-1)^k
                \\binom{n}{k}(x-k)^{n-1}

    Parameters
    ==========

    n : A positive integer, `n > 0`

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import UniformSum, density, cdf
    >>> from sympy import Symbol, pprint

    >>> n = Symbol("n", integer=True)
    >>> z = Symbol("z")

    >>> X = UniformSum("x", n)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
    floor(z)
      ___
      \\  `
       \\         k         n - 1 /n\\\n        )    (-1) *(-k + z)     *| |
       /                         \\k/
      /__,
     k = 0
    --------------------------------
                (n - 1)!

    >>> cdf(X)(z)
    Piecewise((0, z < 0), (Sum((-1)**_k*(-_k + z)**n*binomial(n, _k),
                    (_k, 0, floor(z)))/factorial(n), n >= z), (1, True))


    Compute cdf with specific \'x\' and \'n\' values as follows :
    >>> cdf(UniformSum("x", 5), evaluate=False)(2).doit()
    9/40

    The argument evaluate=False prevents an attempt at evaluation
    of the sum for general n, before the argument 2 is passed.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Uniform_sum_distribution
    .. [2] https://mathworld.wolfram.com/UniformSumDistribution.html

    '''

class VonMisesDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(mu, k) -> None: ...
    def pdf(self, x): ...

def VonMises(name, mu, k):
    '''
    Create a Continuous Random Variable with a von Mises distribution.

    Explanation
    ===========

    The density of the von Mises distribution is given by

    .. math::
        f(x) := \\frac{e^{\\kappa\\cos(x-\\mu)}}{2\\pi I_0(\\kappa)}

    with :math:`x \\in [0,2\\pi]`.

    Parameters
    ==========

    mu : Real number
        Measure of location.
    k : Real number
        Measure of concentration.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import VonMises, density
    >>> from sympy import Symbol, pprint

    >>> mu = Symbol("mu")
    >>> k = Symbol("k", positive=True)
    >>> z = Symbol("z")

    >>> X = VonMises("x", mu, k)

    >>> D = density(X)(z)
    >>> pprint(D, use_unicode=False)
         k*cos(mu - z)
        e
    ------------------
    2*pi*besseli(0, k)


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Von_Mises_distribution
    .. [2] https://mathworld.wolfram.com/vonMisesDistribution.html

    '''

class WeibullDistribution(SingleContinuousDistribution):
    set: Incomplete
    @staticmethod
    def check(alpha, beta) -> None: ...
    def pdf(self, x): ...

def Weibull(name, alpha, beta):
    '''
    Create a continuous random variable with a Weibull distribution.

    Explanation
    ===========

    The density of the Weibull distribution is given by

    .. math::
        f(x) := \\begin{cases}
                  \\frac{k}{\\lambda}\\left(\\frac{x}{\\lambda}\\right)^{k-1}
                  e^{-(x/\\lambda)^{k}} & x\\geq0\\\\\n                  0 & x<0
                \\end{cases}

    Parameters
    ==========

    lambda : Real number, $\\lambda > 0$, a scale
    k : Real number, $k > 0$, a shape

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Weibull, density, E, variance
    >>> from sympy import Symbol, simplify

    >>> l = Symbol("lambda", positive=True)
    >>> k = Symbol("k", positive=True)
    >>> z = Symbol("z")

    >>> X = Weibull("x", l, k)

    >>> density(X)(z)
    k*(z/lambda)**(k - 1)*exp(-(z/lambda)**k)/lambda

    >>> simplify(E(X))
    lambda*gamma(1 + 1/k)

    >>> simplify(variance(X))
    lambda**2*(-gamma(1 + 1/k)**2 + gamma(1 + 2/k))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Weibull_distribution
    .. [2] https://mathworld.wolfram.com/WeibullDistribution.html

    '''

class WignerSemicircleDistribution(SingleContinuousDistribution):
    @property
    def set(self): ...
    @staticmethod
    def check(R) -> None: ...
    def pdf(self, x): ...

def WignerSemicircle(name, R):
    '''
    Create a continuous random variable with a Wigner semicircle distribution.

    Explanation
    ===========

    The density of the Wigner semicircle distribution is given by

    .. math::
        f(x) := \\frac2{\\pi R^2}\\,\\sqrt{R^2-x^2}

    with :math:`x \\in [-R,R]`.

    Parameters
    ==========

    R : Real number, `R > 0`, the radius

    Returns
    =======

    A RandomSymbol.

    Examples
    ========

    >>> from sympy.stats import WignerSemicircle, density, E
    >>> from sympy import Symbol

    >>> R = Symbol("R", positive=True)
    >>> z = Symbol("z")

    >>> X = WignerSemicircle("x", R)

    >>> density(X)(z)
    2*sqrt(R**2 - z**2)/(pi*R**2)

    >>> E(X)
    0

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Wigner_semicircle_distribution
    .. [2] https://mathworld.wolfram.com/WignersSemicircleLaw.html

    '''
