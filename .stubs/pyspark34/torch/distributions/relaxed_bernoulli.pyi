from _typeshed import Incomplete
from torch.distributions.distribution import Distribution
from torch.distributions.transformed_distribution import TransformedDistribution

__all__ = ['LogitRelaxedBernoulli', 'RelaxedBernoulli']

class LogitRelaxedBernoulli(Distribution):
    """
    Creates a LogitRelaxedBernoulli distribution parameterized by :attr:`probs`
    or :attr:`logits` (but not both), which is the logit of a RelaxedBernoulli
    distribution.

    Samples are logits of values in (0, 1). See [1] for more details.

    Args:
        temperature (Tensor): relaxation temperature
        probs (Number, Tensor): the probability of sampling `1`
        logits (Number, Tensor): the log-odds of sampling `1`

    [1] The Concrete Distribution: A Continuous Relaxation of Discrete Random
    Variables (Maddison et al, 2017)

    [2] Categorical Reparametrization with Gumbel-Softmax
    (Jang et al, 2017)
    """
    arg_constraints: Incomplete
    support: Incomplete
    temperature: Incomplete
    def __init__(self, temperature, probs: Incomplete | None = None, logits: Incomplete | None = None, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def logits(self): ...
    def probs(self): ...
    @property
    def param_shape(self): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...

class RelaxedBernoulli(TransformedDistribution):
    '''
    Creates a RelaxedBernoulli distribution, parametrized by
    :attr:`temperature`, and either :attr:`probs` or :attr:`logits`
    (but not both). This is a relaxed version of the `Bernoulli` distribution,
    so the values are in (0, 1), and has reparametrizable samples.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = RelaxedBernoulli(torch.tensor([2.2]),
        ...                      torch.tensor([0.1, 0.2, 0.3, 0.99]))
        >>> m.sample()
        tensor([ 0.2951,  0.3442,  0.8918,  0.9021])

    Args:
        temperature (Tensor): relaxation temperature
        probs (Number, Tensor): the probability of sampling `1`
        logits (Number, Tensor): the log-odds of sampling `1`
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    def __init__(self, temperature, probs: Incomplete | None = None, logits: Incomplete | None = None, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def temperature(self): ...
    @property
    def logits(self): ...
    @property
    def probs(self): ...
