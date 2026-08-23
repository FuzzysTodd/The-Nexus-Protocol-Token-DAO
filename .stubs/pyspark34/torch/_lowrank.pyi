from torch import Tensor
from typing import Tuple

__all__ = ['svd_lowrank', 'pca_lowrank']

def svd_lowrank(A: Tensor, q: int | None = 6, niter: int | None = 2, M: Tensor | None = None) -> Tuple[Tensor, Tensor, Tensor]:
    """Return the singular value decomposition ``(U, S, V)`` of a matrix,
    batches of matrices, or a sparse matrix :math:`A` such that
    :math:`A \\approx U diag(S) V^T`. In case :math:`M` is given, then
    SVD is computed for the matrix :math:`A - M`.

    .. note:: The implementation is based on the Algorithm 5.1 from
              Halko et al, 2009.

    .. note:: To obtain repeatable results, reset the seed for the
              pseudorandom number generator

    .. note:: The input is assumed to be a low-rank matrix.

    .. note:: In general, use the full-rank SVD implementation
              :func:`torch.linalg.svd` for dense matrices due to its 10-fold
              higher performance characteristics. The low-rank SVD
              will be useful for huge sparse matrices that
              :func:`torch.linalg.svd` cannot handle.

    Args::
        A (Tensor): the input tensor of size :math:`(*, m, n)`

        q (int, optional): a slightly overestimated rank of A.

        niter (int, optional): the number of subspace iterations to
                               conduct; niter must be a nonnegative
                               integer, and defaults to 2

        M (Tensor, optional): the input tensor's mean of size
                              :math:`(*, 1, n)`.

    References::
        - Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
          structure with randomness: probabilistic algorithms for
          constructing approximate matrix decompositions,
          arXiv:0909.4061 [math.NA; math.PR], 2009 (available at
          `arXiv <https://arxiv.org/abs/0909.4061>`_).

    """
def pca_lowrank(A: Tensor, q: int | None = None, center: bool = True, niter: int = 2) -> Tuple[Tensor, Tensor, Tensor]:
    """Performs linear Principal Component Analysis (PCA) on a low-rank
    matrix, batches of such matrices, or sparse matrix.

    This function returns a namedtuple ``(U, S, V)`` which is the
    nearly optimal approximation of a singular value decomposition of
    a centered matrix :math:`A` such that :math:`A = U diag(S) V^T`.

    .. note:: The relation of ``(U, S, V)`` to PCA is as follows:

                - :math:`A` is a data matrix with ``m`` samples and
                  ``n`` features

                - the :math:`V` columns represent the principal directions

                - :math:`S ** 2 / (m - 1)` contains the eigenvalues of
                  :math:`A^T A / (m - 1)` which is the covariance of
                  ``A`` when ``center=True`` is provided.

                - ``matmul(A, V[:, :k])`` projects data to the first k
                  principal components

    .. note:: Different from the standard SVD, the size of returned
              matrices depend on the specified rank and q
              values as follows:

                - :math:`U` is m x q matrix

                - :math:`S` is q-vector

                - :math:`V` is n x q matrix

    .. note:: To obtain repeatable results, reset the seed for the
              pseudorandom number generator

    Args:

        A (Tensor): the input tensor of size :math:`(*, m, n)`

        q (int, optional): a slightly overestimated rank of
                           :math:`A`. By default, ``q = min(6, m,
                           n)``.

        center (bool, optional): if True, center the input tensor,
                                 otherwise, assume that the input is
                                 centered.

        niter (int, optional): the number of subspace iterations to
                               conduct; niter must be a nonnegative
                               integer, and defaults to 2.

    References::

        - Nathan Halko, Per-Gunnar Martinsson, and Joel Tropp, Finding
          structure with randomness: probabilistic algorithms for
          constructing approximate matrix decompositions,
          arXiv:0909.4061 [math.NA; math.PR], 2009 (available at
          `arXiv <http://arxiv.org/abs/0909.4061>`_).

    """
