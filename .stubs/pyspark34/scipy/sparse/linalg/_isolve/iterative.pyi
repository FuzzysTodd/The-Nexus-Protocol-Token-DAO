from _typeshed import Incomplete

__all__ = ['bicg', 'bicgstab', 'cg', 'cgs', 'gmres', 'qmr']

def bicg(A, b, x0: Incomplete | None = None, tol: float = 1e-05, maxiter: Incomplete | None = None, M: Incomplete | None = None, callback: Incomplete | None = None, atol: Incomplete | None = None): ...
def bicgstab(A, b, x0: Incomplete | None = None, tol: float = 1e-05, maxiter: Incomplete | None = None, M: Incomplete | None = None, callback: Incomplete | None = None, atol: Incomplete | None = None): ...
def cg(A, b, x0: Incomplete | None = None, tol: float = 1e-05, maxiter: Incomplete | None = None, M: Incomplete | None = None, callback: Incomplete | None = None, atol: Incomplete | None = None): ...
def cgs(A, b, x0: Incomplete | None = None, tol: float = 1e-05, maxiter: Incomplete | None = None, M: Incomplete | None = None, callback: Incomplete | None = None, atol: Incomplete | None = None): ...
def gmres(A, b, x0: Incomplete | None = None, tol: float = 1e-05, restart: Incomplete | None = None, maxiter: Incomplete | None = None, M: Incomplete | None = None, callback: Incomplete | None = None, restrt: Incomplete | None = None, atol: Incomplete | None = None, callback_type: Incomplete | None = None):
    """
    Use Generalized Minimal RESidual iteration to solve ``Ax = b``.

    Parameters
    ----------
    A : {sparse matrix, ndarray, LinearOperator}
        The real or complex N-by-N matrix of the linear system.
        Alternatively, ``A`` can be a linear operator which can
        produce ``Ax`` using, e.g.,
        ``scipy.sparse.linalg.LinearOperator``.
    b : ndarray
        Right hand side of the linear system. Has shape (N,) or (N,1).

    Returns
    -------
    x : ndarray
        The converged solution.
    info : int
        Provides convergence information:
          * 0  : successful exit
          * >0 : convergence to tolerance not achieved, number of iterations
          * <0 : illegal input or breakdown

    Other parameters
    ----------------
    x0 : ndarray
        Starting guess for the solution (a vector of zeros by default).
    tol, atol : float, optional
        Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
        The default for ``atol`` is ``'legacy'``, which emulates
        a different legacy behavior.

        .. warning::

           The default value for `atol` will be changed in a future release.
           For future compatibility, specify `atol` explicitly.
    restart : int, optional
        Number of iterations between restarts. Larger values increase
        iteration cost, but may be necessary for convergence.
        Default is 20.
    maxiter : int, optional
        Maximum number of iterations (restart cycles).  Iteration will stop
        after maxiter steps even if the specified tolerance has not been
        achieved.
    M : {sparse matrix, ndarray, LinearOperator}
        Inverse of the preconditioner of A.  M should approximate the
        inverse of A and be easy to solve for (see Notes).  Effective
        preconditioning dramatically improves the rate of convergence,
        which implies that fewer iterations are needed to reach a given
        error tolerance.  By default, no preconditioner is used.
    callback : function
        User-supplied function to call after each iteration.  It is called
        as `callback(args)`, where `args` are selected by `callback_type`.
    callback_type : {'x', 'pr_norm', 'legacy'}, optional
        Callback function argument requested:
          - ``x``: current iterate (ndarray), called on every restart
          - ``pr_norm``: relative (preconditioned) residual norm (float),
            called on every inner iteration
          - ``legacy`` (default): same as ``pr_norm``, but also changes the
            meaning of 'maxiter' to count inner iterations instead of restart
            cycles.
    restrt : int, optional, deprecated

        .. deprecated:: 0.11.0
           `gmres` keyword argument `restrt` is deprecated infavour of
           `restart` and will be removed in SciPy 1.12.0.

    See Also
    --------
    LinearOperator

    Notes
    -----
    A preconditioner, P, is chosen such that P is close to A but easy to solve
    for. The preconditioner parameter required by this routine is
    ``M = P^-1``. The inverse should preferably not be calculated
    explicitly.  Rather, use the following template to produce M::

      # Construct a linear operator that computes P^-1 @ x.
      import scipy.sparse.linalg as spla
      M_x = lambda x: spla.spsolve(P, x)
      M = spla.LinearOperator((n, n), M_x)

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_matrix
    >>> from scipy.sparse.linalg import gmres
    >>> A = csc_matrix([[3, 2, 0], [1, -1, 0], [0, 5, 1]], dtype=float)
    >>> b = np.array([2, 4, -1], dtype=float)
    >>> x, exitCode = gmres(A, b)
    >>> print(exitCode)            # 0 indicates successful convergence
    0
    >>> np.allclose(A.dot(x), b)
    True
    """
def qmr(A, b, x0: Incomplete | None = None, tol: float = 1e-05, maxiter: Incomplete | None = None, M1: Incomplete | None = None, M2: Incomplete | None = None, callback: Incomplete | None = None, atol: Incomplete | None = None):
    """Use Quasi-Minimal Residual iteration to solve ``Ax = b``.

    Parameters
    ----------
    A : {sparse matrix, ndarray, LinearOperator}
        The real-valued N-by-N matrix of the linear system.
        Alternatively, ``A`` can be a linear operator which can
        produce ``Ax`` and ``A^T x`` using, e.g.,
        ``scipy.sparse.linalg.LinearOperator``.
    b : ndarray
        Right hand side of the linear system. Has shape (N,) or (N,1).

    Returns
    -------
    x : ndarray
        The converged solution.
    info : integer
        Provides convergence information:
            0  : successful exit
            >0 : convergence to tolerance not achieved, number of iterations
            <0 : illegal input or breakdown

    Other Parameters
    ----------------
    x0 : ndarray
        Starting guess for the solution.
    tol, atol : float, optional
        Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
        The default for ``atol`` is ``'legacy'``, which emulates
        a different legacy behavior.

        .. warning::

           The default value for `atol` will be changed in a future release.
           For future compatibility, specify `atol` explicitly.
    maxiter : integer
        Maximum number of iterations.  Iteration will stop after maxiter
        steps even if the specified tolerance has not been achieved.
    M1 : {sparse matrix, ndarray, LinearOperator}
        Left preconditioner for A.
    M2 : {sparse matrix, ndarray, LinearOperator}
        Right preconditioner for A. Used together with the left
        preconditioner M1.  The matrix M1@A@M2 should have better
        conditioned than A alone.
    callback : function
        User-supplied function to call after each iteration.  It is called
        as callback(xk), where xk is the current solution vector.

    See Also
    --------
    LinearOperator

    Examples
    --------
    >>> import numpy as np
    >>> from scipy.sparse import csc_matrix
    >>> from scipy.sparse.linalg import qmr
    >>> A = csc_matrix([[3, 2, 0], [1, -1, 0], [0, 5, 1]], dtype=float)
    >>> b = np.array([2, 4, -1], dtype=float)
    >>> x, exitCode = qmr(A, b)
    >>> print(exitCode)            # 0 indicates successful convergence
    0
    >>> np.allclose(A.dot(x), b)
    True
    """
