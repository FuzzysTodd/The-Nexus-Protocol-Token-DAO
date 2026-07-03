from _typeshed import Incomplete
from sympy.stats.drv import SingleDiscreteDistribution

__all__ = ['FlorySchulz', 'Geometric', 'Hermite', 'Logarithmic', 'NegativeBinomial', 'Poisson', 'Skellam', 'YuleSimon', 'Zeta']

class DiscreteDistributionHandmade(SingleDiscreteDistribution):
    def __new__(cls, pdf, set=...): ...
    @property
    def set(self): ...
    @staticmethod
    def check(pdf, set) -> None: ...

class FlorySchulzDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(a) -> None: ...
    def pdf(self, k): ...

def FlorySchulz(name, a):
    '''
    Create a discrete random variable with a FlorySchulz distribution.

    The density of the FlorySchulz distribution is given by

    .. math::
        f(k) := (a^2) k (1 - a)^{k-1}

    Parameters
    ==========

    a : A real number between 0 and 1

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, E, variance, FlorySchulz
    >>> from sympy import Symbol, S

    >>> a = S.One / 5
    >>> z = Symbol("z")

    >>> X = FlorySchulz("x", a)

    >>> density(X)(z)
    (5/4)**(1 - z)*z/25

    >>> E(X)
    9

    >>> variance(X)
    40

    References
    ==========

    https://en.wikipedia.org/wiki/Flory%E2%80%93Schulz_distribution
    '''

class GeometricDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(p) -> None: ...
    def pdf(self, k): ...

def Geometric(name, p):
    '''
    Create a discrete random variable with a Geometric distribution.

    Explanation
    ===========

    The density of the Geometric distribution is given by

    .. math::
        f(k) := p (1 - p)^{k - 1}

    Parameters
    ==========

    p : A probability between 0 and 1

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Geometric, density, E, variance
    >>> from sympy import Symbol, S

    >>> p = S.One / 5
    >>> z = Symbol("z")

    >>> X = Geometric("x", p)

    >>> density(X)(z)
    (5/4)**(1 - z)/5

    >>> E(X)
    5

    >>> variance(X)
    20

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Geometric_distribution
    .. [2] https://mathworld.wolfram.com/GeometricDistribution.html

    '''

class HermiteDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(a1, a2) -> None: ...
    def pdf(self, k): ...

def Hermite(name, a1, a2):
    '''
    Create a discrete random variable with a Hermite distribution.

    Explanation
    ===========

    The density of the Hermite distribution is given by

    .. math::
        f(x):= e^{-a_1 -a_2}\\sum_{j=0}^{\\left \\lfloor x/2 \\right \\rfloor}
                    \\frac{a_{1}^{x-2j}a_{2}^{j}}{(x-2j)!j!}

    Parameters
    ==========

    a1 : A Positive number greater than equal to 0.
    a2 : A Positive number greater than equal to 0.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Hermite, density, E, variance
    >>> from sympy import Symbol

    >>> a1 = Symbol("a1", positive=True)
    >>> a2 = Symbol("a2", positive=True)
    >>> x = Symbol("x")

    >>> H = Hermite("H", a1=5, a2=4)

    >>> density(H)(2)
    33*exp(-9)/2

    >>> E(H)
    13

    >>> variance(H)
    21

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hermite_distribution

    '''

class LogarithmicDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(p) -> None: ...
    def pdf(self, k): ...

def Logarithmic(name, p):
    '''
    Create a discrete random variable with a Logarithmic distribution.

    Explanation
    ===========

    The density of the Logarithmic distribution is given by

    .. math::
        f(k) := \\frac{-p^k}{k \\ln{(1 - p)}}

    Parameters
    ==========

    p : A value between 0 and 1

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Logarithmic, density, E, variance
    >>> from sympy import Symbol, S

    >>> p = S.One / 5
    >>> z = Symbol("z")

    >>> X = Logarithmic("x", p)

    >>> density(X)(z)
    -1/(5**z*z*log(4/5))

    >>> E(X)
    -1/(-4*log(5) + 8*log(2))

    >>> variance(X)
    -1/((-4*log(5) + 8*log(2))*(-2*log(5) + 4*log(2))) + 1/(-64*log(2)*log(5) + 64*log(2)**2 + 16*log(5)**2) - 10/(-32*log(5) + 64*log(2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Logarithmic_distribution
    .. [2] https://mathworld.wolfram.com/LogarithmicDistribution.html

    '''

class NegativeBinomialDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(r, p) -> None: ...
    def pdf(self, k): ...

def NegativeBinomial(name, r, p):
    '''
    Create a discrete random variable with a Negative Binomial distribution.

    Explanation
    ===========

    The density of the Negative Binomial distribution is given by

    .. math::
        f(k) := \\binom{k + r - 1}{k} (1 - p)^r p^k

    Parameters
    ==========

    r : A positive value
    p : A value between 0 and 1

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import NegativeBinomial, density, E, variance
    >>> from sympy import Symbol, S

    >>> r = 5
    >>> p = S.One / 5
    >>> z = Symbol("z")

    >>> X = NegativeBinomial("x", r, p)

    >>> density(X)(z)
    1024*binomial(z + 4, z)/(3125*5**z)

    >>> E(X)
    5/4

    >>> variance(X)
    25/16

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Negative_binomial_distribution
    .. [2] https://mathworld.wolfram.com/NegativeBinomialDistribution.html

    '''

class PoissonDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(lamda) -> None: ...
    def pdf(self, k): ...

def Poisson(name, lamda):
    '''
    Create a discrete random variable with a Poisson distribution.

    Explanation
    ===========

    The density of the Poisson distribution is given by

    .. math::
        f(k) := \\frac{\\lambda^{k} e^{- \\lambda}}{k!}

    Parameters
    ==========

    lamda : Positive number, a rate

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Poisson, density, E, variance
    >>> from sympy import Symbol, simplify

    >>> rate = Symbol("lambda", positive=True)
    >>> z = Symbol("z")

    >>> X = Poisson("x", rate)

    >>> density(X)(z)
    lambda**z*exp(-lambda)/factorial(z)

    >>> E(X)
    lambda

    >>> simplify(variance(X))
    lambda

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Poisson_distribution
    .. [2] https://mathworld.wolfram.com/PoissonDistribution.html

    '''

class SkellamDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(mu1, mu2) -> None: ...
    def pdf(self, k): ...

def Skellam(name, mu1, mu2):
    '''
    Create a discrete random variable with a Skellam distribution.

    Explanation
    ===========

    The Skellam is the distribution of the difference N1 - N2
    of two statistically independent random variables N1 and N2
    each Poisson-distributed with respective expected values mu1 and mu2.

    The density of the Skellam distribution is given by

    .. math::
        f(k) := e^{-(\\mu_1+\\mu_2)}(\\frac{\\mu_1}{\\mu_2})^{k/2}I_k(2\\sqrt{\\mu_1\\mu_2})

    Parameters
    ==========

    mu1 : A non-negative value
    mu2 : A non-negative value

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Skellam, density, E, variance
    >>> from sympy import Symbol, pprint

    >>> z = Symbol("z", integer=True)
    >>> mu1 = Symbol("mu1", positive=True)
    >>> mu2 = Symbol("mu2", positive=True)
    >>> X = Skellam("x", mu1, mu2)

    >>> pprint(density(X)(z), use_unicode=False)
         z
         -
         2
    /mu1\\   -mu1 - mu2        /       _____   _____\\\n    |---| *e          *besseli\\z, 2*\\/ mu1 *\\/ mu2 /
    \\mu2/
    >>> E(X)
    mu1 - mu2
    >>> variance(X).expand()
    mu1 + mu2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Skellam_distribution

    '''

class YuleSimonDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(rho) -> None: ...
    def pdf(self, k): ...

def YuleSimon(name, rho):
    '''
    Create a discrete random variable with a Yule-Simon distribution.

    Explanation
    ===========

    The density of the Yule-Simon distribution is given by

    .. math::
        f(k) := \\rho B(k, \\rho + 1)

    Parameters
    ==========

    rho : A positive value

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import YuleSimon, density, E, variance
    >>> from sympy import Symbol, simplify

    >>> p = 5
    >>> z = Symbol("z")

    >>> X = YuleSimon("x", p)

    >>> density(X)(z)
    5*beta(z, 6)

    >>> simplify(E(X))
    5/4

    >>> simplify(variance(X))
    25/48

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Yule%E2%80%93Simon_distribution

    '''

class ZetaDistribution(SingleDiscreteDistribution):
    set: Incomplete
    @staticmethod
    def check(s) -> None: ...
    def pdf(self, k): ...

def Zeta(name, s):
    '''
    Create a discrete random variable with a Zeta distribution.

    Explanation
    ===========

    The density of the Zeta distribution is given by

    .. math::
        f(k) := \\frac{1}{k^s \\zeta{(s)}}

    Parameters
    ==========

    s : A value greater than 1

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import Zeta, density, E, variance
    >>> from sympy import Symbol

    >>> s = 5
    >>> z = Symbol("z")

    >>> X = Zeta("x", s)

    >>> density(X)(z)
    1/(z**5*zeta(5))

    >>> E(X)
    pi**4/(90*zeta(5))

    >>> variance(X)
    -pi**8/(8100*zeta(5)**2) + zeta(3)/zeta(5)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Zeta_distribution

    '''
