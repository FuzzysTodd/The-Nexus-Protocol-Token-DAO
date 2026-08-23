from _typeshed import Incomplete
from torch.distributions.transformed_distribution import TransformedDistribution

__all__ = ['Gumbel']

class Gumbel(TransformedDistribution):
    '''
    Samples from a Gumbel Distribution.

    Examples::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Gumbel(torch.tensor([1.0]), torch.tensor([2.0]))
        >>> m.sample()  # sample from Gumbel distribution with loc=1, scale=2
        tensor([ 1.0124])

    Args:
        loc (float or Tensor): Location parameter of the distribution
        scale (float or Tensor): Scale parameter of the distribution
    '''
    arg_constraints: Incomplete
    support: Incomplete
    def __init__(self, loc, scale, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def log_prob(self, value): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def stddev(self): ...
    @property
    def variance(self): ...
    def entropy(self): ...
