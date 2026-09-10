from _typeshed import Incomplete
from torch.distributions import constraints
from torch.distributions.distribution import Distribution
from typing import Dict

__all__ = ['Independent']

class Independent(Distribution):
    """
    Reinterprets some of the batch dims of a distribution as event dims.

    This is mainly useful for changing the shape of the result of
    :meth:`log_prob`. For example to create a diagonal Normal distribution with
    the same shape as a Multivariate Normal distribution (so they are
    interchangeable), you can::

        >>> from torch.distributions.multivariate_normal import MultivariateNormal
        >>> from torch.distributions.normal import Normal
        >>> loc = torch.zeros(3)
        >>> scale = torch.ones(3)
        >>> mvn = MultivariateNormal(loc, scale_tril=torch.diag(scale))
        >>> [mvn.batch_shape, mvn.event_shape]
        [torch.Size([]), torch.Size([3])]
        >>> normal = Normal(loc, scale)
        >>> [normal.batch_shape, normal.event_shape]
        [torch.Size([3]), torch.Size([])]
        >>> diagn = Independent(normal, 1)
        >>> [diagn.batch_shape, diagn.event_shape]
        [torch.Size([]), torch.Size([3])]

    Args:
        base_distribution (torch.distributions.distribution.Distribution): a
            base distribution
        reinterpreted_batch_ndims (int): the number of batch dims to
            reinterpret as event dims
    """
    arg_constraints: Dict[str, constraints.Constraint]
    base_dist: Incomplete
    reinterpreted_batch_ndims: Incomplete
    def __init__(self, base_distribution, reinterpreted_batch_ndims, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def has_rsample(self): ...
    @property
    def has_enumerate_support(self): ...
    def support(self): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def sample(self, sample_shape=...): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
    def enumerate_support(self, expand: bool = True): ...
