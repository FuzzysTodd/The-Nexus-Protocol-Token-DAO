from _typeshed import Incomplete
from scipy.sparse.linalg._interface import LinearOperator

__all__ = ['eigs', 'eigsh', 'ArpackError', 'ArpackNoConvergence']

SNAUPD_ERRORS = DNAUPD_ERRORS
CNAUPD_ERRORS = ZNAUPD_ERRORS
SSAUPD_ERRORS = DSAUPD_ERRORS

class ArpackError(RuntimeError):
    """
    ARPACK error
    """
    def __init__(self, info, infodict=...) -> None: ...

class ArpackNoConvergence(ArpackError):
    """
    ARPACK iteration did not converge

    Attributes
    ----------
    eigenvalues : ndarray
        Partial result. Converged eigenvalues.
    eigenvectors : ndarray
        Partial result. Converged eigenvectors.

    """
    eigenvalues: Incomplete
    eigenvectors: Incomplete
    def __init__(self, msg, eigenvalues, eigenvectors) -> None: ...

class _ArpackParams:
    resid: Incomplete
    sigma: int
    v: Incomplete
    iparam: Incomplete
    mode: Incomplete
    n: Incomplete
    tol: Incomplete
    k: Incomplete
    maxiter: Incomplete
    ncv: Incomplete
    which: Incomplete
    tp: Incomplete
    info: Incomplete
    converged: bool
    ido: int
    def __init__(self, n, k, tp, mode: int = 1, sigma: Incomplete | None = None, ncv: Incomplete | None = None, v0: Incomplete | None = None, maxiter: Incomplete | None = None, which: str = 'LM', tol: int = 0) -> None: ...

class _SymmetricArpackParams(_ArpackParams):
    OP: Incomplete
    B: Incomplete
    bmat: str
    OPa: Incomplete
    OPb: Incomplete
    A_matvec: Incomplete
    workd: Incomplete
    workl: Incomplete
    iterate_infodict: Incomplete
    extract_infodict: Incomplete
    ipntr: Incomplete
    def __init__(self, n, k, tp, matvec, mode: int = 1, M_matvec: Incomplete | None = None, Minv_matvec: Incomplete | None = None, sigma: Incomplete | None = None, ncv: Incomplete | None = None, v0: Incomplete | None = None, maxiter: Incomplete | None = None, which: str = 'LM', tol: int = 0) -> None: ...
    converged: bool
    def iterate(self) -> None: ...
    def extract(self, return_eigenvectors): ...

class _UnsymmetricArpackParams(_ArpackParams):
    OP: Incomplete
    B: Incomplete
    bmat: str
    OPa: Incomplete
    OPb: Incomplete
    matvec: Incomplete
    workd: Incomplete
    workl: Incomplete
    iterate_infodict: Incomplete
    extract_infodict: Incomplete
    ipntr: Incomplete
    rwork: Incomplete
    def __init__(self, n, k, tp, matvec, mode: int = 1, M_matvec: Incomplete | None = None, Minv_matvec: Incomplete | None = None, sigma: Incomplete | None = None, ncv: Incomplete | None = None, v0: Incomplete | None = None, maxiter: Incomplete | None = None, which: str = 'LM', tol: int = 0) -> None: ...
    converged: bool
    def iterate(self) -> None: ...
    def extract(self, return_eigenvectors): ...

class SpLuInv(LinearOperator):
    """
    SpLuInv:
       helper class to repeatedly solve M*x=b
       using a sparse LU-decomposition of M
    """
    M_lu: Incomplete
    shape: Incomplete
    dtype: Incomplete
    isreal: Incomplete
    def __init__(self, M) -> None: ...

class LuInv(LinearOperator):
    """
    LuInv:
       helper class to repeatedly solve M*x=b
       using an LU-decomposition of M
    """
    M_lu: Incomplete
    shape: Incomplete
    dtype: Incomplete
    def __init__(self, M) -> None: ...

class IterInv(LinearOperator):
    """
    IterInv:
       helper class to repeatedly solve M*x=b
       using an iterative method.
    """
    M: Incomplete
    dtype: Incomplete
    shape: Incomplete
    ifunc: Incomplete
    tol: Incomplete
    def __init__(self, M, ifunc=..., tol: int = 0) -> None: ...

class IterOpInv(LinearOperator):
    """
    IterOpInv:
       helper class to repeatedly solve [A-sigma*M]*x = b
       using an iterative method
    """
    A: Incomplete
    M: Incomplete
    sigma: Incomplete
    OP: Incomplete
    shape: Incomplete
    ifunc: Incomplete
    tol: Incomplete
    def __init__(self, A, M, sigma, ifunc=..., tol: int = 0) -> None: ...
    @property
    def dtype(self): ...

def eigs(A, k: int = 6, M: Incomplete | None = None, sigma: Incomplete | None = None, which: str = 'LM', v0: Incomplete | None = None, ncv: Incomplete | None = None, maxiter: Incomplete | None = None, tol: int = 0, return_eigenvectors: bool = True, Minv: Incomplete | None = None, OPinv: Incomplete | None = None, OPpart: Incomplete | None = None):
    """
    Find k eigenvalues and eigenvectors of the square matrix A.

    Solves ``A @ x[i] = w[i] * x[i]``, the standard eigenvalue problem
    for w[i] eigenvalues with corresponding eigenvectors x[i].

    If M is specified, solves ``A @ x[i] = w[i] * M @ x[i]``, the
    generalized eigenvalue problem for w[i] eigenvalues
    with corresponding eigenvectors x[i]

    Parameters
    ----------
    A : ndarray, sparse matrix or LinearOperator
        An array, sparse matrix, or LinearOperator representing
        the operation ``A @ x``, where A is a real or complex square matrix.
    k : int, optional
        The number of eigenvalues and eigenvectors desired.
        `k` must be smaller than N-1. It is not possible to compute all
        eigenvectors of a matrix.
    M : ndarray, sparse matrix or LinearOperator, optional
        An array, sparse matrix, or LinearOperator representing
        the operation M@x for the generalized eigenvalue problem

            A @ x = w * M @ x.

        M must represent a real symmetric matrix if A is real, and must
        represent a complex Hermitian matrix if A is complex. For best
        results, the data type of M should be the same as that of A.
        Additionally:

            If `sigma` is None, M is positive definite

            If sigma is specified, M is positive semi-definite

        If sigma is None, eigs requires an operator to compute the solution
        of the linear equation ``M @ x = b``.  This is done internally via a
        (sparse) LU decomposition for an explicit matrix M, or via an
        iterative solver for a general linear operator.  Alternatively,
        the user can supply the matrix or operator Minv, which gives
        ``x = Minv @ b = M^-1 @ b``.
    sigma : real or complex, optional
        Find eigenvalues near sigma using shift-invert mode.  This requires
        an operator to compute the solution of the linear system
        ``[A - sigma * M] @ x = b``, where M is the identity matrix if
        unspecified. This is computed internally via a (sparse) LU
        decomposition for explicit matrices A & M, or via an iterative
        solver if either A or M is a general linear operator.
        Alternatively, the user can supply the matrix or operator OPinv,
        which gives ``x = OPinv @ b = [A - sigma * M]^-1 @ b``.
        For a real matrix A, shift-invert can either be done in imaginary
        mode or real mode, specified by the parameter OPpart ('r' or 'i').
        Note that when sigma is specified, the keyword 'which' (below)
        refers to the shifted eigenvalues ``w'[i]`` where:

            If A is real and OPpart == 'r' (default),
              ``w'[i] = 1/2 * [1/(w[i]-sigma) + 1/(w[i]-conj(sigma))]``.

            If A is real and OPpart == 'i',
              ``w'[i] = 1/2i * [1/(w[i]-sigma) - 1/(w[i]-conj(sigma))]``.

            If A is complex, ``w'[i] = 1/(w[i]-sigma)``.

    v0 : ndarray, optional
        Starting vector for iteration.
        Default: random
    ncv : int, optional
        The number of Lanczos vectors generated
        `ncv` must be greater than `k`; it is recommended that ``ncv > 2*k``.
        Default: ``min(n, max(2*k + 1, 20))``
    which : str, ['LM' | 'SM' | 'LR' | 'SR' | 'LI' | 'SI'], optional
        Which `k` eigenvectors and eigenvalues to find:

            'LM' : largest magnitude

            'SM' : smallest magnitude

            'LR' : largest real part

            'SR' : smallest real part

            'LI' : largest imaginary part

            'SI' : smallest imaginary part

        When sigma != None, 'which' refers to the shifted eigenvalues w'[i]
        (see discussion in 'sigma', above).  ARPACK is generally better
        at finding large values than small values.  If small eigenvalues are
        desired, consider using shift-invert mode for better performance.
    maxiter : int, optional
        Maximum number of Arnoldi update iterations allowed
        Default: ``n*10``
    tol : float, optional
        Relative accuracy for eigenvalues (stopping criterion)
        The default value of 0 implies machine precision.
    return_eigenvectors : bool, optional
        Return eigenvectors (True) in addition to eigenvalues
    Minv : ndarray, sparse matrix or LinearOperator, optional
        See notes in M, above.
    OPinv : ndarray, sparse matrix or LinearOperator, optional
        See notes in sigma, above.
    OPpart : {'r' or 'i'}, optional
        See notes in sigma, above

    Returns
    -------
    w : ndarray
        Array of k eigenvalues.
    v : ndarray
        An array of `k` eigenvectors.
        ``v[:, i]`` is the eigenvector corresponding to the eigenvalue w[i].

    Raises
    ------
    ArpackNoConvergence
        When the requested convergence is not obtained.
        The currently converged eigenvalues and eigenvectors can be found
        as ``eigenvalues`` and ``eigenvectors`` attributes of the exception
        object.

    See Also
    --------
    eigsh : eigenvalues and eigenvectors for symmetric matrix A
    svds : singular value decomposition for a matrix A

    Notes
    -----
    This function is a wrapper to the ARPACK [1]_ SNEUPD, DNEUPD, CNEUPD,
    ZNEUPD, functions which use the Implicitly Restarted Arnoldi Method to
    find the eigenvalues and eigenvectors [2]_.

    References
    ----------
    .. [1] ARPACK Software, http://www.caam.rice.edu/software/ARPACK/
    .. [2] R. B. Lehoucq, D. C. Sorensen, and C. Yang,  ARPACK USERS GUIDE:
       Solution of Large Scale Eigenvalue Problems by Implicitly Restarted
       Arnoldi Methods. SIAM, Philadelphia, PA, 1998.

    Examples
    --------
    Find 6 eigenvectors of the identity matrix:

    >>> import numpy as np
    >>> from scipy.sparse.linalg import eigs
    >>> id = np.eye(13)
    >>> vals, vecs = eigs(id, k=6)
    >>> vals
    array([ 1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j])
    >>> vecs.shape
    (13, 6)

    """
def eigsh(A, k: int = 6, M: Incomplete | None = None, sigma: Incomplete | None = None, which: str = 'LM', v0: Incomplete | None = None, ncv: Incomplete | None = None, maxiter: Incomplete | None = None, tol: int = 0, return_eigenvectors: bool = True, Minv: Incomplete | None = None, OPinv: Incomplete | None = None, mode: str = 'normal'):
    """
    Find k eigenvalues and eigenvectors of the real symmetric square matrix
    or complex Hermitian matrix A.

    Solves ``A @ x[i] = w[i] * x[i]``, the standard eigenvalue problem for
    w[i] eigenvalues with corresponding eigenvectors x[i].

    If M is specified, solves ``A @ x[i] = w[i] * M @ x[i]``, the
    generalized eigenvalue problem for w[i] eigenvalues
    with corresponding eigenvectors x[i].

    Note that there is no specialized routine for the case when A is a complex
    Hermitian matrix. In this case, ``eigsh()`` will call ``eigs()`` and return the
    real parts of the eigenvalues thus obtained.

    Parameters
    ----------
    A : ndarray, sparse matrix or LinearOperator
        A square operator representing the operation ``A @ x``, where ``A`` is
        real symmetric or complex Hermitian. For buckling mode (see below)
        ``A`` must additionally be positive-definite.
    k : int, optional
        The number of eigenvalues and eigenvectors desired.
        `k` must be smaller than N. It is not possible to compute all
        eigenvectors of a matrix.

    Returns
    -------
    w : array
        Array of k eigenvalues.
    v : array
        An array representing the `k` eigenvectors.  The column ``v[:, i]`` is
        the eigenvector corresponding to the eigenvalue ``w[i]``.

    Other Parameters
    ----------------
    M : An N x N matrix, array, sparse matrix, or linear operator representing
        the operation ``M @ x`` for the generalized eigenvalue problem

            A @ x = w * M @ x.

        M must represent a real symmetric matrix if A is real, and must
        represent a complex Hermitian matrix if A is complex. For best
        results, the data type of M should be the same as that of A.
        Additionally:

            If sigma is None, M is symmetric positive definite.

            If sigma is specified, M is symmetric positive semi-definite.

            In buckling mode, M is symmetric indefinite.

        If sigma is None, eigsh requires an operator to compute the solution
        of the linear equation ``M @ x = b``. This is done internally via a
        (sparse) LU decomposition for an explicit matrix M, or via an
        iterative solver for a general linear operator.  Alternatively,
        the user can supply the matrix or operator Minv, which gives
        ``x = Minv @ b = M^-1 @ b``.
    sigma : real
        Find eigenvalues near sigma using shift-invert mode.  This requires
        an operator to compute the solution of the linear system
        ``[A - sigma * M] x = b``, where M is the identity matrix if
        unspecified.  This is computed internally via a (sparse) LU
        decomposition for explicit matrices A & M, or via an iterative
        solver if either A or M is a general linear operator.
        Alternatively, the user can supply the matrix or operator OPinv,
        which gives ``x = OPinv @ b = [A - sigma * M]^-1 @ b``.
        Note that when sigma is specified, the keyword 'which' refers to
        the shifted eigenvalues ``w'[i]`` where:

            if mode == 'normal', ``w'[i] = 1 / (w[i] - sigma)``.

            if mode == 'cayley', ``w'[i] = (w[i] + sigma) / (w[i] - sigma)``.

            if mode == 'buckling', ``w'[i] = w[i] / (w[i] - sigma)``.

        (see further discussion in 'mode' below)
    v0 : ndarray, optional
        Starting vector for iteration.
        Default: random
    ncv : int, optional
        The number of Lanczos vectors generated ncv must be greater than k and
        smaller than n; it is recommended that ``ncv > 2*k``.
        Default: ``min(n, max(2*k + 1, 20))``
    which : str ['LM' | 'SM' | 'LA' | 'SA' | 'BE']
        If A is a complex Hermitian matrix, 'BE' is invalid.
        Which `k` eigenvectors and eigenvalues to find:

            'LM' : Largest (in magnitude) eigenvalues.

            'SM' : Smallest (in magnitude) eigenvalues.

            'LA' : Largest (algebraic) eigenvalues.

            'SA' : Smallest (algebraic) eigenvalues.

            'BE' : Half (k/2) from each end of the spectrum.

        When k is odd, return one more (k/2+1) from the high end.
        When sigma != None, 'which' refers to the shifted eigenvalues ``w'[i]``
        (see discussion in 'sigma', above).  ARPACK is generally better
        at finding large values than small values.  If small eigenvalues are
        desired, consider using shift-invert mode for better performance.
    maxiter : int, optional
        Maximum number of Arnoldi update iterations allowed.
        Default: ``n*10``
    tol : float
        Relative accuracy for eigenvalues (stopping criterion).
        The default value of 0 implies machine precision.
    Minv : N x N matrix, array, sparse matrix, or LinearOperator
        See notes in M, above.
    OPinv : N x N matrix, array, sparse matrix, or LinearOperator
        See notes in sigma, above.
    return_eigenvectors : bool
        Return eigenvectors (True) in addition to eigenvalues.
        This value determines the order in which eigenvalues are sorted.
        The sort order is also dependent on the `which` variable.

            For which = 'LM' or 'SA':
                If `return_eigenvectors` is True, eigenvalues are sorted by
                algebraic value.

                If `return_eigenvectors` is False, eigenvalues are sorted by
                absolute value.

            For which = 'BE' or 'LA':
                eigenvalues are always sorted by algebraic value.

            For which = 'SM':
                If `return_eigenvectors` is True, eigenvalues are sorted by
                algebraic value.

                If `return_eigenvectors` is False, eigenvalues are sorted by
                decreasing absolute value.

    mode : string ['normal' | 'buckling' | 'cayley']
        Specify strategy to use for shift-invert mode.  This argument applies
        only for real-valued A and sigma != None.  For shift-invert mode,
        ARPACK internally solves the eigenvalue problem
        ``OP @ x'[i] = w'[i] * B @ x'[i]``
        and transforms the resulting Ritz vectors x'[i] and Ritz values w'[i]
        into the desired eigenvectors and eigenvalues of the problem
        ``A @ x[i] = w[i] * M @ x[i]``.
        The modes are as follows:

            'normal' :
                OP = [A - sigma * M]^-1 @ M,
                B = M,
                w'[i] = 1 / (w[i] - sigma)

            'buckling' :
                OP = [A - sigma * M]^-1 @ A,
                B = A,
                w'[i] = w[i] / (w[i] - sigma)

            'cayley' :
                OP = [A - sigma * M]^-1 @ [A + sigma * M],
                B = M,
                w'[i] = (w[i] + sigma) / (w[i] - sigma)

        The choice of mode will affect which eigenvalues are selected by
        the keyword 'which', and can also impact the stability of
        convergence (see [2] for a discussion).

    Raises
    ------
    ArpackNoConvergence
        When the requested convergence is not obtained.

        The currently converged eigenvalues and eigenvectors can be found
        as ``eigenvalues`` and ``eigenvectors`` attributes of the exception
        object.

    See Also
    --------
    eigs : eigenvalues and eigenvectors for a general (nonsymmetric) matrix A
    svds : singular value decomposition for a matrix A

    Notes
    -----
    This function is a wrapper to the ARPACK [1]_ SSEUPD and DSEUPD
    functions which use the Implicitly Restarted Lanczos Method to
    find the eigenvalues and eigenvectors [2]_.

    References
    ----------
    .. [1] ARPACK Software, http://www.caam.rice.edu/software/ARPACK/
    .. [2] R. B. Lehoucq, D. C. Sorensen, and C. Yang,  ARPACK USERS GUIDE:
       Solution of Large Scale Eigenvalue Problems by Implicitly Restarted
       Arnoldi Methods. SIAM, Philadelphia, PA, 1998.

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse.linalg import eigsh
    >>> identity = np.eye(13)
    >>> eigenvalues, eigenvectors = eigsh(identity, k=6)
    >>> eigenvalues
    array([1., 1., 1., 1., 1., 1.])
    >>> eigenvectors.shape
    (13, 6)

    """
