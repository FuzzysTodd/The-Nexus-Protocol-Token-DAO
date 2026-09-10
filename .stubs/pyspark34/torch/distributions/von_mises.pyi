from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['VonMises']

class VonMises(Distribution):
    '''
    A circular von Mises distribution.

    This implementation uses polar coordinates. The ``loc`` and ``value`` args
    can be any real number (to facilitate unconstrained optimization), but are
    interpreted as angles modulo 2 pi.

    Example::
        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = VonMises(torch.tensor([1.0]), torch.tensor([1.0]))
        >>> m.sample()  # von Mises distributed with loc=1 and concentration=1
        tensor([1.9777])

    :param torch.Tensor loc: an angle in radians.
    :param torch.Tensor concentration: concentration parameter
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    def __init__(self, loc, concentration, validate_args: Incomplete | None = None) -> None: ...
    def log_prob(self, value): ...
    def sample(self, sample_shape=...):
        '''
        The sampling algorithm for the von Mises distribution is based on the following paper:
        Best, D. J., and Nicholas I. Fisher.
        "Efficient simulation of the von Mises distribution." Applied Statistics (1979): 152-157.
        '''
    def expand(self, batch_shape): ...
    @property
    def mean(self):
        """
        The provided mean is the circular one.
        """
    @property
    def mode(self): ...
    def variance(self):
        """
        The provided variance is the circular one.
        """
