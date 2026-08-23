from _typeshed import Incomplete
from torch.distributions.distribution import Distribution

__all__ = ['MultivariateNormal']

class MultivariateNormal(Distribution):
    '''
    Creates a multivariate normal (also called Gaussian) distribution
    parameterized by a mean vector and a covariance matrix.

    The multivariate normal distribution can be parameterized either
    in terms of a positive definite covariance matrix :math:`\\mathbf{\\Sigma}`
    or a positive definite precision matrix :math:`\\mathbf{\\Sigma}^{-1}`
    or a lower-triangular matrix :math:`\\mathbf{L}` with positive-valued
    diagonal entries, such that
    :math:`\\mathbf{\\Sigma} = \\mathbf{L}\\mathbf{L}^\\top`. This triangular matrix
    can be obtained via e.g. Cholesky decomposition of the covariance.

    Example:

        >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_LAPACK)
        >>> # xdoctest: +IGNORE_WANT("non-determenistic")
        >>> m = MultivariateNormal(torch.zeros(2), torch.eye(2))
        >>> m.sample()  # normally distributed with mean=`[0,0]` and covariance_matrix=`I`
        tensor([-0.2102, -0.5429])

    Args:
        loc (Tensor): mean of the distribution
        covariance_matrix (Tensor): positive-definite covariance matrix
        precision_matrix (Tensor): positive-definite precision matrix
        scale_tril (Tensor): lower-triangular factor of covariance, with positive-valued diagonal

    Note:
        Only one of :attr:`covariance_matrix` or :attr:`precision_matrix` or
        :attr:`scale_tril` can be specified.

        Using :attr:`scale_tril` will be more efficient: all computations internally
        are based on :attr:`scale_tril`. If :attr:`covariance_matrix` or
        :attr:`precision_matrix` is passed instead, it is only used to compute
        the corresponding lower triangular matrices using a Cholesky decomposition.
    '''
    arg_constraints: Incomplete
    support: Incomplete
    has_rsample: bool
    loc: Incomplete
    def __init__(self, loc, covariance_matrix: Incomplete | None = None, precision_matrix: Incomplete | None = None, scale_tril: Incomplete | None = None, validate_args: Incomplete | None = None) -> None: ...
    def expand(self, batch_shape, _instance: Incomplete | None = None): ...
    def scale_tril(self): ...
    def covariance_matrix(self): ...
    def precision_matrix(self): ...
    @property
    def mean(self): ...
    @property
    def mode(self): ...
    @property
    def variance(self): ...
    def rsample(self, sample_shape=...): ...
    def log_prob(self, value): ...
    def entropy(self): ...
