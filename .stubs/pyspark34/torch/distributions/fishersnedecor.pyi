from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['FisherSnedecor']

class FisherSnedecor(Distribution):
    '''
    Creates a Fisher-Snedecor distribution parameterized by :attr:`df1` and :attr:`df2`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = FisherSnedecor(torch.tensor([1.0]), torch.tensor([2.0]))
        >>> m.sample()  # Fisher-Snedecor-distributed with df1=1 and df2=2
        tensor([ 0.2453])

    Args:
        df1 (float or Tensor): degrees of freedom parameter 1
        df2 (float or Tensor): degrees of freedom parameter 2
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    def __init__(self, df1, df2, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
