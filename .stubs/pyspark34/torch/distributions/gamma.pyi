from _typeshed import Incomplete
from torch.distributions.exp_family import ExponentialFamily

__all__ = ['Gamma']

class Gamma(ExponentialFamily):
    '''
    Creates a Gamma distribution parameterized by shape :attr:`concentration` and :attr:`rate`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Gamma(torch.tensor([1.0]), torch.tensor([1.0]))
        >>> m.sample()  # Gamma distributed with concentration=1 and rate=1
        tensor([ 0.1046])

    Args:
        concentration (float or Tensor): shape parameter of the distribution
            (often referred to as alpha)
        rate (float or Tensor): rate = 1 / scale of the distribution
            (often referred to as beta)
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def __init__(self, concentration, rate, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
    def cdf(self, value): ...
