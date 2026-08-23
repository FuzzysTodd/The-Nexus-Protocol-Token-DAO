from _typeshed import Incomplete
from torch.autograd import Function
from torch.distributions.exp_family import ExponentialFamily

__all__ = ['Dirichlet']

class _Dirichlet(Function):
    @staticmethod
    def forward(ctx, concentration): ...
    @staticmethod
    def backward(ctx, grad_output): ...

class Dirichlet(ExponentialFamily):
    '''
    Creates a Dirichlet distribution parameterized by concentration :attr:`concentration`.

    Example::

        >>> # xdoctest: +IGNORE_WANT("non-deterinistic")
        >>> m = Dirichlet(torch.tensor([0.5, 0.5]))
        >>> m.sample()  # Dirichlet distributed with concentration [0.5, 0.5]
        tensor([ 0.1046,  0.8954])

    Args:
        concentration (Tensor): concentration parameter of the distribution
            (often referred to as alpha)
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    concentration: Incomplete
    def __init__(self, concentration, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def rsample(self, sample_shape=()): ...
    def log_prob(self, value): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def entropy(self): ...
