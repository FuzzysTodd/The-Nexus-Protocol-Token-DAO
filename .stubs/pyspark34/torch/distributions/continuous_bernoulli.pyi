from _typeshed import Incomplete
from torch.distributions.exp_family import ExponentialFamily

__all__ = ['ContinuousBernoulli']

class ContinuousBernoulli(ExponentialFamily):
    '''
    Creates a continuous Bernoulli distribution parameterized by :attr:`probs`
    or :attr:`logits` (but not both).

    The distribution is supported in [0, 1] and parameterized by \'probs\' (in
    (0,1)) or \'logits\' (real-valued). Note that, unlike the Bernoulli, \'probs\'
    does not correspond to a probability and \'logits\' does not correspond to
    log-odds, but the same names are used due to the similarity with the
    Bernoulli. See [1] for more details.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = ContinuousBernoulli(torch.tensor([0.3]))
        >>> m.sample()
        tensor([ 0.2538])

    Args:
        probs (Number, Tensor): (0,1) valued parameters
        logits (Number, Tensor): real valued parameters whose sigmoid matches \'probs\'

    [1] The continuous Bernoulli: fixing a pervasive error in variational
    autoencoders, Loaiza-Ganem G and Cunningham JP, NeurIPS 2019.
    https://arxiv.org/abs/1907.06845
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    def __init__(self, probs: Incomplete | None = None, logits: Incomplete | None = None, lims=(0.499, 0.501), validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    @property
    def mean(self): ...
    @property
    def stddev(self): ...
    @property
    def variance(self): ...
    def logits(self): ...
    def probs(self): ...
    @property
    def param_shape(self): ...
    def sample(self, sample_shape=...): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def cdf(self, value): ...
    def icdf(self, value): ...
    def entropy(self): ...
