from _typeshed import Incomplete
from torch.distributions.transformed_distribution import TransformedDistribution

__all__ = ['Weibull']

class Weibull(TransformedDistribution):
    '''
    Samples from a two-parameter Weibull distribution.

    Example:

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Weibull(torch.tensor([1.0]), torch.tensor([1.0]))
        >>> m.sample()  # sample from a Weibull distribution with scale=1, concentration=1
        tensor([ 0.4784])

    Args:
        scale (float or Tensor): Scale parameter of distribution (lambda).
        concentration (float or Tensor): Concentration parameter of distribution (k/shape).
    '''
    arg_constraints: Incomplete
    support: Incomplete
    concentration_reciprocal: Incomplete
    def __init__(self, scale, concentration, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def entropy(self): ...
