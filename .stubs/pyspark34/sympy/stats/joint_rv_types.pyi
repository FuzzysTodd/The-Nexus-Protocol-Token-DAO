from _typeshed import Incomplete
from sympy.stats.joint_rv import JointDistribution

__all__ = ['JointRV', 'MultivariateNormal', 'MultivariateLaplace', 'Dirichlet', 'GeneralizedMultivariateLogGamma', 'GeneralizedMultivariateLogGammaOmega', 'Multinomial', 'MultivariateBeta', 'MultivariateEwens', 'MultivariateT', 'NegativeMultinomial', 'NormalGamma']

class JointDistributionHandmade(JointDistribution):
    is_Continuous: bool
    @property
    def set(self): ...

def JointRV(symbol, pdf, _set: Incomplete | None = None):
    """
    Create a Joint Random Variable where each of its component is continuous,
    given the following:

    Parameters
    ==========

    symbol : Symbol
        Represents name of the random variable.
    pdf : A PDF in terms of indexed symbols of the symbol given
        as the first argument

    NOTE
    ====

    As of now, the set for each component for a ``JointRV`` is
    equal to the set of all integers, which cannot be changed.

    Examples
    ========

    >>> from sympy import exp, pi, Indexed, S
    >>> from sympy.stats import density, JointRV
    >>> x1, x2 = (Indexed('x', i) for i in (1, 2))
    >>> pdf = exp(-x1**2/2 + x1 - x2**2/2 - S(1)/2)/(2*pi)
    >>> N1 = JointRV('x', pdf) #Multivariate Normal distribution
    >>> density(N1)(1, 2)
    exp(-2)/(2*pi)

    Returns
    =======

    RandomSymbol

    """

class MultivariateNormalDistribution(JointDistribution):
    is_Continuous: bool
    @property
    def set(self): ...
    @staticmethod
    def check(mu, sigma) -> None: ...
    def pdf(self, *args): ...

def MultivariateNormal(name, mu, sigma):
    """
    Creates a continuous random variable with Multivariate Normal
    Distribution.

    The density of the multivariate normal distribution can be found at [1].

    Parameters
    ==========

    mu : List representing the mean or the mean vector
    sigma : Positive semidefinite square matrix
        Represents covariance Matrix.
        If `\\sigma` is noninvertible then only sampling is supported currently

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import MultivariateNormal, density, marginal_distribution
    >>> from sympy import symbols, MatrixSymbol
    >>> X = MultivariateNormal('X', [3, 4], [[2, 1], [1, 2]])
    >>> y, z = symbols('y z')
    >>> density(X)(y, z)
    sqrt(3)*exp(-y**2/3 + y*z/3 + 2*y/3 - z**2/3 + 5*z/3 - 13/3)/(6*pi)
    >>> density(X)(1, 2)
    sqrt(3)*exp(-4/3)/(6*pi)
    >>> marginal_distribution(X, X[1])(y)
    exp(-(y - 4)**2/4)/(2*sqrt(pi))
    >>> marginal_distribution(X, X[0])(y)
    exp(-(y - 3)**2/4)/(2*sqrt(pi))

    The example below shows that it is also possible to use
    symbolic parameters to define the MultivariateNormal class.

    >>> n = symbols('n', integer=True, positive=True)
    >>> Sg = MatrixSymbol('Sg', n, n)
    >>> mu = MatrixSymbol('mu', n, 1)
    >>> obs = MatrixSymbol('obs', n, 1)
    >>> X = MultivariateNormal('X', mu, Sg)

    The density of a multivariate normal can be
    calculated using a matrix argument, as shown below.

    >>> density(X)(obs)
    (exp(((1/2)*mu.T - (1/2)*obs.T)*Sg**(-1)*(-mu + obs))/sqrt((2*pi)**n*Determinant(Sg)))[0, 0]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Multivariate_normal_distribution

    """

class MultivariateLaplaceDistribution(JointDistribution):
    is_Continuous: bool
    @property
    def set(self): ...
    @staticmethod
    def check(mu, sigma) -> None: ...
    def pdf(self, *args): ...

def MultivariateLaplace(name, mu, sigma):
    """
    Creates a continuous random variable with Multivariate Laplace
    Distribution.

    The density of the multivariate Laplace distribution can be found at [1].

    Parameters
    ==========

    mu : List representing the mean or the mean vector
    sigma : Positive definite square matrix
        Represents covariance Matrix

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import MultivariateLaplace, density
    >>> from sympy import symbols
    >>> y, z = symbols('y z')
    >>> X = MultivariateLaplace('X', [2, 4], [[3, 1], [1, 3]])
    >>> density(X)(y, z)
    sqrt(2)*exp(y/4 + 5*z/4)*besselk(0, sqrt(15*y*(3*y/8 - z/8)/2 + 15*z*(-y/8 + 3*z/8)/2))/(4*pi)
    >>> density(X)(1, 2)
    sqrt(2)*exp(11/4)*besselk(0, sqrt(165)/4)/(4*pi)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Multivariate_Laplace_distribution

    """

class MultivariateTDistribution(JointDistribution):
    is_Continuous: bool
    @property
    def set(self): ...
    @staticmethod
    def check(mu, sigma, v) -> None: ...
    def pdf(self, *args): ...

def MultivariateT(syms, mu, sigma, v):
    '''
    Creates a joint random variable with multivariate T-distribution.

    Parameters
    ==========

    syms : A symbol/str
        For identifying the random variable.
    mu : A list/matrix
        Representing the location vector
    sigma : The shape matrix for the distribution

    Examples
    ========

    >>> from sympy.stats import density, MultivariateT
    >>> from sympy import Symbol

    >>> x = Symbol("x")
    >>> X = MultivariateT("x", [1, 1], [[1, 0], [0, 1]], 2)

    >>> density(X)(1, 2)
    2/(9*pi)

    Returns
    =======

    RandomSymbol

    '''

class NormalGammaDistribution(JointDistribution):
    is_Continuous: bool
    @staticmethod
    def check(mu, lamda, alpha, beta) -> None: ...
    @property
    def set(self): ...
    def pdf(self, x, tau): ...

def NormalGamma(sym, mu, lamda, alpha, beta):
    """
    Creates a bivariate joint random variable with multivariate Normal gamma
    distribution.

    Parameters
    ==========

    sym : A symbol/str
        For identifying the random variable.
    mu : A real number
        The mean of the normal distribution
    lamda : A positive integer
        Parameter of joint distribution
    alpha : A positive integer
        Parameter of joint distribution
    beta : A positive integer
        Parameter of joint distribution

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, NormalGamma
    >>> from sympy import symbols

    >>> X = NormalGamma('x', 0, 1, 2, 3)
    >>> y, z = symbols('y z')

    >>> density(X)(y, z)
    9*sqrt(2)*z**(3/2)*exp(-3*z)*exp(-y**2*z/2)/(2*sqrt(pi))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Normal-gamma_distribution

    """

class MultivariateBetaDistribution(JointDistribution):
    is_Continuous: bool
    @staticmethod
    def check(alpha) -> None: ...
    @property
    def set(self): ...
    def pdf(self, *syms): ...

def MultivariateBeta(syms, *alpha):
    """
    Creates a continuous random variable with Dirichlet/Multivariate Beta
    Distribution.

    The density of the Dirichlet distribution can be found at [1].

    Parameters
    ==========

    alpha : Positive real numbers
        Signifies concentration numbers.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, MultivariateBeta, marginal_distribution
    >>> from sympy import Symbol
    >>> a1 = Symbol('a1', positive=True)
    >>> a2 = Symbol('a2', positive=True)
    >>> B = MultivariateBeta('B', [a1, a2])
    >>> C = MultivariateBeta('C', a1, a2)
    >>> x = Symbol('x')
    >>> y = Symbol('y')
    >>> density(B)(x, y)
    x**(a1 - 1)*y**(a2 - 1)*gamma(a1 + a2)/(gamma(a1)*gamma(a2))
    >>> marginal_distribution(C, C[0])(x)
    x**(a1 - 1)*gamma(a1 + a2)/(a2*gamma(a1)*gamma(a2))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dirichlet_distribution
    .. [2] https://mathworld.wolfram.com/DirichletDistribution.html

    """
Dirichlet = MultivariateBeta

class MultivariateEwensDistribution(JointDistribution):
    is_Discrete: bool
    is_Continuous: bool
    @staticmethod
    def check(n, theta) -> None: ...
    @property
    def set(self): ...
    def pdf(self, *syms): ...

def MultivariateEwens(syms, n, theta):
    """
    Creates a discrete random variable with Multivariate Ewens
    Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    n : Positive integer
        Size of the sample or the integer whose partitions are considered
    theta : Positive real number
        Denotes Mutation rate

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, marginal_distribution, MultivariateEwens
    >>> from sympy import Symbol
    >>> a1 = Symbol('a1', positive=True)
    >>> a2 = Symbol('a2', positive=True)
    >>> ed = MultivariateEwens('E', 2, 1)
    >>> density(ed)(a1, a2)
    Piecewise((1/(2**a2*factorial(a1)*factorial(a2)), Eq(a1 + 2*a2, 2)), (0, True))
    >>> marginal_distribution(ed, ed[0])(a1)
    Piecewise((1/factorial(a1), Eq(a1, 2)), (0, True))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Ewens%27s_sampling_formula
    .. [2] https://www.researchgate.net/publication/280311472_The_Ubiquitous_Ewens_Sampling_Formula

    """

class GeneralizedMultivariateLogGammaDistribution(JointDistribution):
    is_Continuous: bool
    def check(self, delta, v, l, mu) -> None: ...
    @property
    def set(self): ...
    def pdf(self, *y): ...

def GeneralizedMultivariateLogGamma(syms, delta, v, lamda, mu):
    """
    Creates a joint random variable with generalized multivariate log gamma
    distribution.

    The joint pdf can be found at [1].

    Parameters
    ==========

    syms : list/tuple/set of symbols for identifying each component
    delta : A constant in range $[0, 1]$
    v : Positive real number
    lamda : List of positive real numbers
    mu : List of positive real numbers

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density
    >>> from sympy.stats.joint_rv_types import GeneralizedMultivariateLogGamma
    >>> from sympy import symbols, S
    >>> v = 1
    >>> l, mu = [1, 1, 1], [1, 1, 1]
    >>> d = S.Half
    >>> y = symbols('y_1:4', positive=True)
    >>> Gd = GeneralizedMultivariateLogGamma('G', d, v, l, mu)
    >>> density(Gd)(y[0], y[1], y[2])
    Sum(exp((n + 1)*(y_1 + y_2 + y_3) - exp(y_1) - exp(y_2) -
    exp(y_3))/(2**n*gamma(n + 1)**3), (n, 0, oo))/2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Generalized_multivariate_log-gamma_distribution
    .. [2] https://www.researchgate.net/publication/234137346_On_a_multivariate_log-gamma_distribution_and_the_use_of_the_distribution_in_the_Bayesian_analysis

    Note
    ====

    If the GeneralizedMultivariateLogGamma is too long to type use,

    >>> from sympy.stats.joint_rv_types import GeneralizedMultivariateLogGamma as GMVLG
    >>> Gd = GMVLG('G', d, v, l, mu)

    If you want to pass the matrix omega instead of the constant delta, then use
    ``GeneralizedMultivariateLogGammaOmega``.

    """
def GeneralizedMultivariateLogGammaOmega(syms, omega, v, lamda, mu):
    """
    Extends GeneralizedMultivariateLogGamma.

    Parameters
    ==========

    syms : list/tuple/set of symbols
        For identifying each component
    omega : A square matrix
           Every element of square matrix must be absolute value of
           square root of correlation coefficient
    v : Positive real number
    lamda : List of positive real numbers
    mu : List of positive real numbers

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density
    >>> from sympy.stats.joint_rv_types import GeneralizedMultivariateLogGammaOmega
    >>> from sympy import Matrix, symbols, S
    >>> omega = Matrix([[1, S.Half, S.Half], [S.Half, 1, S.Half], [S.Half, S.Half, 1]])
    >>> v = 1
    >>> l, mu = [1, 1, 1], [1, 1, 1]
    >>> G = GeneralizedMultivariateLogGammaOmega('G', omega, v, l, mu)
    >>> y = symbols('y_1:4', positive=True)
    >>> density(G)(y[0], y[1], y[2])
    sqrt(2)*Sum((1 - sqrt(2)/2)**n*exp((n + 1)*(y_1 + y_2 + y_3) - exp(y_1) -
    exp(y_2) - exp(y_3))/gamma(n + 1)**3, (n, 0, oo))/2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Generalized_multivariate_log-gamma_distribution
    .. [2] https://www.researchgate.net/publication/234137346_On_a_multivariate_log-gamma_distribution_and_the_use_of_the_distribution_in_the_Bayesian_analysis

    Notes
    =====

    If the GeneralizedMultivariateLogGammaOmega is too long to type use,

    >>> from sympy.stats.joint_rv_types import GeneralizedMultivariateLogGammaOmega as GMVLGO
    >>> G = GMVLGO('G', omega, v, l, mu)

    """

class MultinomialDistribution(JointDistribution):
    is_Continuous: bool
    is_Discrete: bool
    @staticmethod
    def check(n, p) -> None: ...
    @property
    def set(self): ...
    def pdf(self, *x): ...

def Multinomial(syms, n, *p):
    """
    Creates a discrete random variable with Multinomial Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    n : Positive integer
        Represents number of trials
    p : List of event probabilities
        Must be in the range of $[0, 1]$.

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, Multinomial, marginal_distribution
    >>> from sympy import symbols
    >>> x1, x2, x3 = symbols('x1, x2, x3', nonnegative=True, integer=True)
    >>> p1, p2, p3 = symbols('p1, p2, p3', positive=True)
    >>> M = Multinomial('M', 3, p1, p2, p3)
    >>> density(M)(x1, x2, x3)
    Piecewise((6*p1**x1*p2**x2*p3**x3/(factorial(x1)*factorial(x2)*factorial(x3)),
    Eq(x1 + x2 + x3, 3)), (0, True))
    >>> marginal_distribution(M, M[0])(x1).subs(x1, 1)
    3*p1*p2**2 + 6*p1*p2*p3 + 3*p1*p3**2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Multinomial_distribution
    .. [2] https://mathworld.wolfram.com/MultinomialDistribution.html

    """

class NegativeMultinomialDistribution(JointDistribution):
    is_Continuous: bool
    is_Discrete: bool
    @staticmethod
    def check(k0, p) -> None: ...
    @property
    def set(self): ...
    def pdf(self, *k): ...

def NegativeMultinomial(syms, k0, *p):
    """
    Creates a discrete random variable with Negative Multinomial Distribution.

    The density of the said distribution can be found at [1].

    Parameters
    ==========

    k0 : positive integer
        Represents number of failures before the experiment is stopped
    p : List of event probabilities
        Must be in the range of $[0, 1]$

    Returns
    =======

    RandomSymbol

    Examples
    ========

    >>> from sympy.stats import density, NegativeMultinomial, marginal_distribution
    >>> from sympy import symbols
    >>> x1, x2, x3 = symbols('x1, x2, x3', nonnegative=True, integer=True)
    >>> p1, p2, p3 = symbols('p1, p2, p3', positive=True)
    >>> N = NegativeMultinomial('M', 3, p1, p2, p3)
    >>> N_c = NegativeMultinomial('M', 3, 0.1, 0.1, 0.1)
    >>> density(N)(x1, x2, x3)
    p1**x1*p2**x2*p3**x3*(-p1 - p2 - p3 + 1)**3*gamma(x1 + x2 +
    x3 + 3)/(2*factorial(x1)*factorial(x2)*factorial(x3))
    >>> marginal_distribution(N_c, N_c[0])(1).evalf().round(2)
    0.25


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Negative_multinomial_distribution
    .. [2] https://mathworld.wolfram.com/NegativeBinomialDistribution.html

    """
