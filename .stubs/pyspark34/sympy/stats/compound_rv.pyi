from _typeshed import Incomplete
from sympy.concrete.summations import Sum as Sum
from sympy.core.basic import Basic as Basic
from sympy.core.function import Lambda as Lambda
from sympy.core.symbol import Dummy as Dummy
from sympy.integrals.integrals import Integral as Integral
from sympy.stats.crv import ContinuousDistribution as ContinuousDistribution, SingleContinuousPSpace as SingleContinuousPSpace
from sympy.stats.crv_types import ContinuousDistributionHandmade as ContinuousDistributionHandmade
from sympy.stats.drv import DiscreteDistribution as DiscreteDistribution, SingleDiscretePSpace as SingleDiscretePSpace
from sympy.stats.drv_types import DiscreteDistributionHandmade as DiscreteDistributionHandmade
from sympy.stats.frv import SingleFiniteDistribution as SingleFiniteDistribution, SingleFinitePSpace as SingleFinitePSpace
from sympy.stats.frv_types import FiniteDistributionHandmade as FiniteDistributionHandmade
from sympy.stats.rv import Distribution as Distribution, NamedArgsMixin as NamedArgsMixin, PSpace as PSpace, RandomSymbol as RandomSymbol, is_random as is_random, random_symbols as random_symbols

class CompoundPSpace(PSpace):
    """
    A temporary Probability Space for the Compound Distribution. After
    Marginalization, this returns the corresponding Probability Space of the
    parent distribution.
    """
    def __new__(cls, s, distribution): ...
    @property
    def value(self): ...
    @property
    def symbol(self): ...
    @property
    def is_Continuous(self): ...
    @property
    def is_Finite(self): ...
    @property
    def is_Discrete(self): ...
    @property
    def distribution(self): ...
    @property
    def pdf(self): ...
    @property
    def set(self): ...
    @property
    def domain(self): ...
    def compute_density(self, expr, *, compound_evaluate: bool = True, **kwargs): ...
    def compute_cdf(self, expr, *, compound_evaluate: bool = True, **kwargs): ...
    def compute_expectation(self, expr, rvs: Incomplete | None = None, evaluate: bool = False, **kwargs): ...
    def probability(self, condition, *, compound_evaluate: bool = True, **kwargs): ...
    def conditional_space(self, condition, *, compound_evaluate: bool = True, **kwargs): ...

class CompoundDistribution(Distribution, NamedArgsMixin):
    """
    Class for Compound Distributions.

    Parameters
    ==========

    dist : Distribution
        Distribution must contain a random parameter

    Examples
    ========

    >>> from sympy.stats.compound_rv import CompoundDistribution
    >>> from sympy.stats.crv_types import NormalDistribution
    >>> from sympy.stats import Normal
    >>> from sympy.abc import x
    >>> X = Normal('X', 2, 4)
    >>> N = NormalDistribution(X, 4)
    >>> C = CompoundDistribution(N)
    >>> C.set
    Interval(-oo, oo)
    >>> C.pdf(x, evaluate=True).simplify()
    exp(-x**2/64 + x/16 - 1/16)/(8*sqrt(pi))

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Compound_probability_distribution

    """
    def __new__(cls, dist): ...
    @property
    def set(self): ...
    @property
    def is_Continuous(self): ...
    @property
    def is_Finite(self): ...
    @property
    def is_Discrete(self): ...
    def pdf(self, x, evaluate: bool = False): ...
