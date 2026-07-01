from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.core.cache import cacheit as cacheit
from sympy.core.function import Lambda as Lambda, PoleError as PoleError
from sympy.core.numbers import I as I, nan as nan, oo as oo
from sympy.core.relational import Eq as Eq, Ne as Ne
from sympy.core.singleton import S as S
from sympy.core.symbol import Dummy as Dummy, symbols as symbols
from sympy.core.sympify import sympify as sympify
from sympy.functions.combinatorial.factorials import factorial as factorial
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.piecewise import Piecewise as Piecewise
from sympy.functions.special.delta_functions import DiracDelta as DiracDelta
from sympy.integrals.integrals import Integral as Integral, integrate as integrate
from sympy.logic.boolalg import And as And, Or as Or
from sympy.polys.polyerrors import PolynomialError as PolynomialError
from sympy.polys.polytools import poly as poly
from sympy.series.series import series as series
from sympy.sets.sets import FiniteSet as FiniteSet, Intersection as Intersection, Interval as Interval, Union as Union
from sympy.solvers.inequalities import reduce_rational_inequalities as reduce_rational_inequalities
from sympy.solvers.solveset import solveset as solveset
from sympy.stats.rv import ConditionalDomain as ConditionalDomain, Distribution as Distribution, NamedArgsMixin as NamedArgsMixin, PSpace as PSpace, ProductDomain as ProductDomain, RandomDomain as RandomDomain, SingleDomain as SingleDomain, SinglePSpace as SinglePSpace, is_random as is_random, random_symbols as random_symbols

class ContinuousDomain(RandomDomain):
    """
    A domain with continuous support

    Represented using symbols and Intervals.
    """
    is_Continuous: bool
    def as_boolean(self) -> None: ...

class SingleContinuousDomain(ContinuousDomain, SingleDomain):
    """
    A univariate domain with continuous support

    Represented using a single symbol and interval.
    """
    def compute_expectation(self, expr, variables: Incomplete | None = None, **kwargs): ...
    def as_boolean(self): ...

class ProductContinuousDomain(ProductDomain, ContinuousDomain):
    """
    A collection of independent domains with continuous support
    """
    def compute_expectation(self, expr, variables: Incomplete | None = None, **kwargs): ...
    def as_boolean(self): ...

class ConditionalContinuousDomain(ContinuousDomain, ConditionalDomain):
    """
    A domain with continuous support that has been further restricted by a
    condition such as $x > 3$.
    """
    def compute_expectation(self, expr, variables: Incomplete | None = None, **kwargs): ...
    def as_boolean(self): ...
    @property
    def set(self): ...

class ContinuousDistribution(Distribution):
    def __call__(self, *args): ...

class SingleContinuousDistribution(ContinuousDistribution, NamedArgsMixin):
    """ Continuous distribution of a single variable.

    Explanation
    ===========

    Serves as superclass for Normal/Exponential/UniformDistribution etc....

    Represented by parameters for each of the specific classes.  E.g
    NormalDistribution is represented by a mean and standard deviation.

    Provides methods for pdf, cdf, and sampling.

    See Also
    ========

    sympy.stats.crv_types.*
    """
    set: Incomplete
    def __new__(cls, *args): ...
    @staticmethod
    def check(*args) -> None: ...
    def compute_cdf(self, **kwargs):
        """ Compute the CDF from the PDF.

        Returns a Lambda.
        """
    def cdf(self, x, **kwargs):
        """ Cumulative density function """
    def compute_characteristic_function(self, **kwargs):
        """ Compute the characteristic function from the PDF.

        Returns a Lambda.
        """
    def characteristic_function(self, t, **kwargs):
        """ Characteristic function """
    def compute_moment_generating_function(self, **kwargs):
        """ Compute the moment generating function from the PDF.

        Returns a Lambda.
        """
    def moment_generating_function(self, t, **kwargs):
        """ Moment generating function """
    def expectation(self, expr, var, evaluate: bool = True, **kwargs):
        """ Expectation of expression over distribution """
    def compute_quantile(self, **kwargs):
        """ Compute the Quantile from the PDF.

        Returns a Lambda.
        """
    def quantile(self, x, **kwargs):
        """ Cumulative density function """

class ContinuousPSpace(PSpace):
    """ Continuous Probability Space

    Represents the likelihood of an event space defined over a continuum.

    Represented with a ContinuousDomain and a PDF (Lambda-Like)
    """
    is_Continuous: bool
    is_real: bool
    @property
    def pdf(self): ...
    def compute_expectation(self, expr, rvs: Incomplete | None = None, evaluate: bool = False, **kwargs): ...
    def compute_density(self, expr, **kwargs): ...
    def compute_cdf(self, expr, **kwargs): ...
    def compute_characteristic_function(self, expr, **kwargs): ...
    def compute_moment_generating_function(self, expr, **kwargs): ...
    def compute_quantile(self, expr, **kwargs): ...
    def probability(self, condition, **kwargs): ...
    def where(self, condition): ...
    def conditional_space(self, condition, normalize: bool = True, **kwargs): ...

class SingleContinuousPSpace(ContinuousPSpace, SinglePSpace):
    """
    A continuous probability space over a single univariate variable.

    These consist of a Symbol and a SingleContinuousDistribution

    This class is normally accessed through the various random variable
    functions, Normal, Exponential, Uniform, etc....
    """
    @property
    def set(self): ...
    @property
    def domain(self): ...
    def sample(self, size=(), library: str = 'scipy', seed: Incomplete | None = None):
        """
        Internal sample method.

        Returns dictionary mapping RandomSymbol to realization value.
        """
    def compute_expectation(self, expr, rvs: Incomplete | None = None, evaluate: bool = False, **kwargs): ...
    def compute_cdf(self, expr, **kwargs): ...
    def compute_characteristic_function(self, expr, **kwargs): ...
    def compute_moment_generating_function(self, expr, **kwargs): ...
    def compute_density(self, expr, **kwargs): ...
    def compute_quantile(self, expr, **kwargs): ...

def reduce_rational_inequalities_wrap(condition, var): ...
