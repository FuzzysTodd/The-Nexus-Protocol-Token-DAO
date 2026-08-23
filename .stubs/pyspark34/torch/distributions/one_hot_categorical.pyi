from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['OneHotCategorical', 'OneHotCategoricalStraightThrough']

class OneHotCategorical(Distribution):
    '''
    Creates a one-hot categorical distribution parameterized by :attr:`probs` or
    :attr:`logits`.

    Samples are one-hot coded vectors of size ``probs.size(-1)``.

    .. note:: The `probs` argument must be non-negative, finite and have a non-zero sum,
              and it will be normalized to sum to 1 along the last dimension. :attr:`probs`
              will return this normalized value.
              The `logits` argument will be interpreted as unnormalized log probabilities
              and can therefore be any real number. It will likewise be normalized so that
              the resulting probabilities sum to 1 along the last dimension. :attr:`logits`
              will return this normalized value.

    See also: :func:`torch.distributions.Categorical` for specifications of
    :attr:`probs` and :attr:`logits`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = OneHotCategorical(torch.tensor([ 0.25, 0.25, 0.25, 0.25 ]))
        >>> m.sample()  # equal probability of 0, 1, 2, 3
        tensor([ 0.,  0.,  0.,  1.])

    Args:
        probs (Tensor): event probabilities
        logits (Tensor): event log probabilities (unnormalized)
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_enumerate_support: bool
    def __init__(self, probs: Incomplete | None = None, logits: Incomplete | None = None, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def probs(self): ...
    @property
    def logits(self): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    @property
    def param_shape(self): ...
    def sample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
    def enumerate_support(self, expand: bool = True): ...

class OneHotCategoricalStraightThrough(OneHotCategorical):
    """
    Creates a reparameterizable :class:`OneHotCategorical` distribution based on the straight-
    through gradient estimator from [1].

    [1] Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation
    (Bengio et al, 2013)
    """
    has_rsample: bool
    def rsample(self, sample_shape=...): ...
