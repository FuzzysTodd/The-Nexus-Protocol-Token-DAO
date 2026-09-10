from ._trustregion import BaseQuadraticSubproblem
from _typeshed import Incomplete

__all__ = ['_minimize_trustregion_exact', 'estimate_smallest_singular_value', 'singular_leading_submatrix', 'IterativeSubproblem']

def _minimize_trustregion_exact(fun, x0, args=(), jac: Incomplete | None = None, hess: Incomplete | None = None, **trust_region_options):
    """
    Minimization of scalar function of one or more variables using
    a nearly exact trust-region algorithm.

    Options
    -------
    initial_tr_radius : float
        Initial trust-region radius.
    max_tr_radius : float
        Maximum value of the trust-region radius. No steps that are longer
        than this value will be proposed.
    eta : float
        Trust region related acceptance stringency for proposed steps.
    gtol : float
        Gradient norm must be less than ``gtol`` before successful
        termination.
    """
def estimate_smallest_singular_value(U):
    """Given upper triangular matrix ``U`` estimate the smallest singular
    value and the correspondent right singular vector in O(n**2) operations.

    Parameters
    ----------
    U : ndarray
        Square upper triangular matrix.

    Returns
    -------
    s_min : float
        Estimated smallest singular value of the provided matrix.
    z_min : ndarray
        Estimatied right singular vector.

    Notes
    -----
    The procedure is based on [1]_ and is done in two steps. First, it finds
    a vector ``e`` with components selected from {+1, -1} such that the
    solution ``w`` from the system ``U.T w = e`` is as large as possible.
    Next it estimate ``U v = w``. The smallest singular value is close
    to ``norm(w)/norm(v)`` and the right singular vector is close
    to ``v/norm(v)``.

    The estimation will be better more ill-conditioned is the matrix.

    References
    ----------
    .. [1] Cline, A. K., Moler, C. B., Stewart, G. W., Wilkinson, J. H.
           An estimate for the condition number of a matrix.  1979.
           SIAM Journal on Numerical Analysis, 16(2), 368-375.
    """
def singular_leading_submatrix(A, U, k):
    """
    Compute term that makes the leading ``k`` by ``k``
    submatrix from ``A`` singular.

    Parameters
    ----------
    A : ndarray
        Symmetric matrix that is not positive definite.
    U : ndarray
        Upper triangular matrix resulting of an incomplete
        Cholesky decomposition of matrix ``A``.
    k : int
        Positive integer such that the leading k by k submatrix from
        `A` is the first non-positive definite leading submatrix.

    Returns
    -------
    delta : float
        Amount that should be added to the element (k, k) of the
        leading k by k submatrix of ``A`` to make it singular.
    v : ndarray
        A vector such that ``v.T B v = 0``. Where B is the matrix A after
        ``delta`` is added to its element (k, k).
    """

class IterativeSubproblem(BaseQuadraticSubproblem):
    '''Quadratic subproblem solved by nearly exact iterative method.

    Notes
    -----
    This subproblem solver was based on [1]_, [2]_ and [3]_,
    which implement similar algorithms. The algorithm is basically
    that of [1]_ but ideas from [2]_ and [3]_ were also used.

    References
    ----------
    .. [1] A.R. Conn, N.I. Gould, and P.L. Toint, "Trust region methods",
           Siam, pp. 169-200, 2000.
    .. [2] J. Nocedal and  S. Wright, "Numerical optimization",
           Springer Science & Business Media. pp. 83-91, 2006.
    .. [3] J.J. More and D.C. Sorensen, "Computing a trust region step",
           SIAM Journal on Scientific and Statistical Computing, vol. 4(3),
           pp. 553-572, 1983.
    '''
    UPDATE_COEFF: float
    EPS: Incomplete
    previous_tr_radius: int
    lambda_lb: Incomplete
    niter: int
    k_easy: Incomplete
    k_hard: Incomplete
    dimension: Incomplete
    hess_inf: Incomplete
    hess_fro: Incomplete
    CLOSE_TO_ZERO: Incomplete
    def __init__(self, x, fun, jac, hess, hessp: Incomplete | None = None, k_easy: float = 0.1, k_hard: float = 0.2) -> None: ...
    lambda_current: Incomplete
    def solve(self, tr_radius):
        """Solve quadratic subproblem"""
