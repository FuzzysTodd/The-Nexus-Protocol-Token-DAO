from _typeshed import Incomplete
from torch.distributions.exp_family import ExponentialFamily

__all__ = ['Bernoulli']

class Bernoulli(ExponentialFamily):
    '''
    Creates a Bernoulli distribution parameterized by :attr:`probs`
    or :attr:`logits` (but not both).

    Samples are binary (0 or 1). They take the value `1` with probability `p`
    and `0` with probability `1 - p`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Bernoulli(torch.tensor([0.3]))
        >>> m.sample()  # 30% chance 1; 70% chance 0
        tensor([ 0.])

    Args:
        probs (Number, Tensor): the probability of sampling `1`
        logits (Number, Tensor): the log-odds of sampling `1`
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_enumerate_support: bool
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
    @property
    def param_shape(self): ...
    def sample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
    def enumerate_support(self, expand: bool = True): ...
