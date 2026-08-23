from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['StudentT']

class StudentT(Distribution):
    '''
    Creates a Student\'s t-distribution parameterized by degree of
    freedom :attr:`df`, mean :attr:`loc` and scale :attr:`scale`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = StudentT(torch.tensor([2.0]))
        >>> m.sample()  # Student\'s t-distributed with degrees of freedom=2
        tensor([ 0.1046])

    Args:
        df (float or Tensor): degrees of freedom
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
    def __init__(self, df, loc: float = 0.0, scale: float = 1.0, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
