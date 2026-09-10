from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['Geometric']

class Geometric(Distribution):
    '''
    Creates a Geometric distribution parameterized by :attr:`probs`,
    where :attr:`probs` is the probability of success of Bernoulli trials.
    It represents the probability that in :math:`k + 1` Bernoulli trials, the
    first :math:`k` trials failed, before seeing a success.

    Samples are non-negative integers [0, :math:`\\inf`).

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Geometric(torch.tensor([0.3]))
        >>> m.sample()  # underlying Bernoulli has 30% chance 1; 70% chance 0
        tensor([ 2.])

    Args:
        probs (Number, Tensor): the probability of sampling `1`. Must be in range (0, 1]
        logits (Number, Tensor): the log-odds of sampling `1`.
    '''
    arg_constraints: Incomplete
    support: Incomplete
    def __init__(self, probs: Incomplete | None = None, logits: Incomplete | None = None, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def logits(self): ...
    def probs(self): ...
    def sample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
