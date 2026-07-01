from _typeshed import Incomplete
from torch.distributions.exp_family import ExponentialFamily

__all__ = ['Poisson']

class Poisson(ExponentialFamily):
    '''
    Creates a Poisson distribution parameterized by :attr:`rate`, the rate parameter.

    Samples are nonnegative integers, with a pmf given by

    .. math::
      \\mathrm{rate}^k \\frac{e^{-\\mathrm{rate}}}{k!}

    Example::

        >>> # xdoctest: +SKIP("poisson_cpu not implemented for \'Long\'")
        >>> m = Poisson(torch.tensor([4]))
        >>> m.sample()
        tensor([ 3.])

    Args:
        rate (Number, Tensor): the rate parameter
    '''
    arg_constraints: Incomplete
    support: Incomplete
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def __init__(self, rate, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def sample(self, sample_shape=...): ...
    def log_prob(self, value): ...
