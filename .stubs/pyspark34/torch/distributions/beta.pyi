from _typeshed import Incomplete
from torch.distributions.exp_family import ExponentialFamily

__all__ = ['Beta']

class Beta(ExponentialFamily):
    '''
    Beta distribution parameterized by :attr:`concentration1` and :attr:`concentration0`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Beta(torch.tensor([0.5]), torch.tensor([0.5]))
        >>> m.sample()  # Beta distributed with concentration concentration1 and concentration0
        tensor([ 0.1046])

    Args:
        concentration1 (float or Tensor): 1st concentration parameter of the distribution
            (often referred to as alpha)
        concentration0 (float or Tensor): 2nd concentration parameter of the distribution
            (often referred to as beta)
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    def __init__(self, concentration1, concentration0, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def rsample(self, sample_shape=()): ...
    def log_prob(self, value): ...
    def entropy(self): ...
    @property
    def concentration1(self): ...
    @property
    def concentration0(self): ...
