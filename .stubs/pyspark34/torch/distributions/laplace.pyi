from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['Laplace']

class Laplace(Distribution):
    '''
    Creates a Laplace distribution parameterized by :attr:`loc` and :attr:`scale`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Laplace(torch.tensor([0.0]), torch.tensor([1.0]))
        >>> m.sample()  # Laplace distributed with loc=0, scale=1
        tensor([ 0.1046])

    Args:
        loc (float or Tensor): mean of the distribution
        scale (float or Tensor): scale of the distribution
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
    @property
    def stddev(self): ...
    def __init__(self, loc, scale, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def cdf(self, value): ...
    def icdf(self, value): ...
    def entropy(self): ...
