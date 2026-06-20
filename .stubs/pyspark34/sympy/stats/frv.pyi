from _typeshed import Incomplete
from sympy.concrete.summations import Sum as Sum
from sympy.core.basic import Basic as Basic
from sympy.core.cache import cacheit as cacheit
from sympy.core.containers import Dict as Dict
from sympy.core.function import Lambda as Lambda
from sympy.core.logic import Logic as Logic
from sympy.core.mul import Mul as Mul
from sympy.core.numbers import I as I, nan as nan
from sympy.core.relational import Eq as Eq, Relational as Relational
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.logic.boolalg import And as And, Or as Or
from sympy.sets.sets import FiniteSet as FiniteSet, Intersection as Intersection
from sympy.stats.rv import ConditionalDomain as ConditionalDomain, Density as Density, Distribution as Distribution, IndependentProductPSpace as IndependentProductPSpace, NamedArgsMixin as NamedArgsMixin, PSpace as PSpace, ProductDomain as ProductDomain, RandomDomain as RandomDomain, SinglePSpace as SinglePSpace, random_symbols as random_symbols, rv_subs as rv_subs, sumsets as sumsets

class FiniteDensity(dict):
    """
    A domain with Finite Density.
    """
    def __call__(self, item):
        """
        Make instance of a class callable.

        If item belongs to current instance of a class, return it.

        Otherwise, return 0.
        """
    @property
    def dict(self):
        """
        Return item as dictionary.
        """

class FiniteDomain(RandomDomain):
    """
    A domain with discrete finite support

    Represented using a FiniteSet.
    """
    is_Finite: bool
    @property
    def symbols(self): ...
    @property
    def elements(self): ...
    @property
    def dict(self): ...
    def __contains__(self, other) -> bool: ...
    def __iter__(self): ...
    def as_boolean(self): ...

class SingleFiniteDomain(FiniteDomain):
    """
    A FiniteDomain over a single symbol/set

    Example: The possibilities of a *single* die roll.
    """
    def __new__(cls, symbol, set): ...
    @property
    def symbol(self): ...
    @property
    def symbols(self): ...
    @property
    def set(self): ...
    @property
    def elements(self): ...
    def __iter__(self): ...
    def __contains__(self, other) -> bool: ...

class ProductFiniteDomain(ProductDomain, FiniteDomain):
    """
    A Finite domain consisting of several other FiniteDomains

    Example: The possibilities of the rolls of three independent dice
    """
    def __iter__(self): ...
    @property
    def elements(self): ...

class ConditionalFiniteDomain(ConditionalDomain, ProductFiniteDomain):
    """
    A FiniteDomain that has been restricted by a condition

    Example: The possibilities of a die roll under the condition that the
    roll is even.
    """
    def __new__(cls, domain, condition):
        """
        Create a new instance of ConditionalFiniteDomain class
        """
    def __contains__(self, other) -> bool: ...
    def __iter__(self): ...
    @property
    def set(self): ...
    def as_boolean(self): ...

class SingleFiniteDistribution(Distribution, NamedArgsMixin):
    def __new__(cls, *args): ...
    @staticmethod
    def check(*args) -> None: ...
    @property
    def dict(self): ...
    def pmf(self, *args) -> None: ...
    @property
    def set(self) -> None: ...
    values: Incomplete
    items: Incomplete
    is_symbolic: Incomplete
    __iter__: Incomplete
    __getitem__: Incomplete
    def __call__(self, *args): ...
    def __contains__(self, other) -> bool: ...

class FinitePSpace(PSpace):
    """
    A Finite Probability Space

    Represents the probabilities of a finite number of events.
    """
    is_Finite: bool
    def __new__(cls, domain, density): ...
    def prob_of(self, elem): ...
    def where(self, condition): ...
    def compute_density(self, expr): ...
    def compute_cdf(self, expr): ...
    def sorted_cdf(self, expr, python_float: bool = False): ...
    def compute_characteristic_function(self, expr): ...
    def compute_moment_generating_function(self, expr): ...
    def compute_expectation(self, expr, rvs: Incomplete | None = None, **kwargs): ...
    def compute_quantile(self, expr): ...
    def probability(self, condition): ...
    def conditional_space(self, condition): ...
    def sample(self, size=(), library: str = 'scipy', seed: Incomplete | None = None):
        """
        Internal sample method

        Returns dictionary mapping RandomSymbol to realization value.
        """

class SingleFinitePSpace(SinglePSpace, FinitePSpace):
    """
    A single finite probability space

    Represents the probabilities of a set of random events that can be
    attributed to a single variable/symbol.

    This class is implemented by many of the standard FiniteRV types such as
    Die, Bernoulli, Coin, etc....
    """
    @property
    def domain(self): ...
    @property
    def distribution(self): ...
    def pmf(self, expr): ...
    def compute_characteristic_function(self, expr): ...
    def compute_moment_generating_function(self, expr): ...
    def compute_quantile(self, expr): ...
    def compute_density(self, expr): ...
    def compute_cdf(self, expr): ...
    def compute_expectation(self, expr, rvs: Incomplete | None = None, **kwargs): ...
    def probability(self, condition): ...
    def conditional_space(self, condition):
        """
        This method is used for transferring the
        computation to probability method because
        conditional space of random variables with
        symbolic dimensions is currently not possible.
        """

class ProductFinitePSpace(IndependentProductPSpace, FinitePSpace):
    """
    A collection of several independent finite probability spaces
    """
    @property
    def domain(self): ...
    @property
    def density(self): ...
    def probability(self, condition): ...
    def compute_density(self, expr): ...
