from _typeshed import Incomplete
from sympy.core.basic import Basic as Basic
from sympy.stats.joint_rv import ProductPSpace as ProductPSpace
from sympy.stats.rv import Distribution as Distribution, ProductDomain as ProductDomain

class StochasticPSpace(ProductPSpace):
    """
    Represents probability space of stochastic processes
    and their random variables. Contains mechanics to do
    computations for queries of stochastic processes.

    Explanation
    ===========

    Initialized by symbol, the specific process and
    distribution(optional) if the random indexed symbols
    of the process follows any specific distribution, like,
    in Bernoulli Process, each random indexed symbol follows
    Bernoulli distribution. For processes with memory, this
    parameter should not be passed.
    """
    def __new__(cls, sym, process, distribution: Incomplete | None = None): ...
    @property
    def process(self):
        """
        The associated stochastic process.
        """
    @property
    def domain(self): ...
    @property
    def symbol(self): ...
    @property
    def distribution(self): ...
    def probability(self, condition, given_condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Transfers the task of handling queries to the specific stochastic
        process because every process has their own logic of handling such
        queries.
        """
    def compute_expectation(self, expr, condition: Incomplete | None = None, evaluate: bool = True, **kwargs):
        """
        Transfers the task of handling queries to the specific stochastic
        process because every process has their own logic of handling such
        queries.
        """
