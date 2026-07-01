from _typeshed import Incomplete

__all__ = ['broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden', 'excitingmixing', 'newton_krylov', 'BroydenFirst', 'KrylovJacobian', 'InverseJacobian']

class NoConvergence(Exception): ...

class TerminationCondition:
    """
    Termination condition for an iteration. It is terminated if

    - |F| < f_rtol*|F_0|, AND
    - |F| < f_tol

    AND

    - |dx| < x_rtol*|x|, AND
    - |dx| < x_tol

    """
    x_tol: Incomplete
    x_rtol: Incomplete
    f_tol: Incomplete
    f_rtol: Incomplete
    norm: Incomplete
    iter: Incomplete
    f0_norm: Incomplete
    iteration: int
    def __init__(self, f_tol: Incomplete | None = None, f_rtol: Incomplete | None = None, x_tol: Incomplete | None = None, x_rtol: Incomplete | None = None, iter: Incomplete | None = None, norm=...) -> None: ...
    def check(self, f, x, dx): ...

class Jacobian:
    """
    Common interface for Jacobians or Jacobian approximations.

    The optional methods come useful when implementing trust region
    etc., algorithms that often require evaluating transposes of the
    Jacobian.

    Methods
    -------
    solve
        Returns J^-1 * v
    update
        Updates Jacobian to point `x` (where the function has residual `Fx`)

    matvec : optional
        Returns J * v
    rmatvec : optional
        Returns A^H * v
    rsolve : optional
        Returns A^-H * v
    matmat : optional
        Returns A * V, where V is a dense matrix with dimensions (N,K).
    todense : optional
        Form the dense Jacobian matrix. Necessary for dense trust region
        algorithms, and useful for testing.

    Attributes
    ----------
    shape
        Matrix dimensions (M, N)
    dtype
        Data type of the matrix.
    func : callable, optional
        Function the Jacobian corresponds to

    """
    __array__: Incomplete
    def __init__(self, **kw) -> None: ...
    def aspreconditioner(self): ...
    def solve(self, v, tol: int = 0) -> None: ...
    def update(self, x, F) -> None: ...
    func: Incomplete
    shape: Incomplete
    dtype: Incomplete
    def setup(self, x, F, func) -> None: ...

class InverseJacobian:
    jacobian: Incomplete
    matvec: Incomplete
    update: Incomplete
    setup: Incomplete
    rmatvec: Incomplete
    def __init__(self, jacobian) -> None: ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...

class GenericBroyden(Jacobian):
    last_f: Incomplete
    last_x: Incomplete
    alpha: Incomplete
    def setup(self, x0, f0, func) -> None: ...
    def update(self, x, f) -> None: ...

class LowRankMatrix:
    """
    A matrix represented as

    .. math:: \\alpha I + \\sum_{n=0}^{n=M} c_n d_n^\\dagger

    However, if the rank of the matrix reaches the dimension of the vectors,
    full matrix representation will be used thereon.

    """
    alpha: Incomplete
    cs: Incomplete
    ds: Incomplete
    n: Incomplete
    dtype: Incomplete
    collapsed: Incomplete
    def __init__(self, alpha, n, dtype) -> None: ...
    def matvec(self, v):
        """Evaluate w = M v"""
    def rmatvec(self, v):
        """Evaluate w = M^H v"""
    def solve(self, v, tol: int = 0):
        """Evaluate w = M^-1 v"""
    def rsolve(self, v, tol: int = 0):
        """Evaluate w = M^-H v"""
    def append(self, c, d) -> None: ...
    def __array__(self): ...
    def collapse(self) -> None:
        """Collapse the low-rank matrix to a full-rank one."""
    def restart_reduce(self, rank) -> None:
        """
        Reduce the rank of the matrix by dropping all vectors.
        """
    def simple_reduce(self, rank) -> None:
        """
        Reduce the rank of the matrix by dropping oldest vectors.
        """
    def svd_reduce(self, max_rank, to_retain: Incomplete | None = None) -> None:
        '''
        Reduce the rank of the matrix by retaining some SVD components.

        This corresponds to the "Broyden Rank Reduction Inverse"
        algorithm described in [1]_.

        Note that the SVD decomposition can be done by solving only a
        problem whose size is the effective rank of this matrix, which
        is viable even for large problems.

        Parameters
        ----------
        max_rank : int
            Maximum rank of this matrix after reduction.
        to_retain : int, optional
            Number of SVD components to retain when reduction is done
            (ie. rank > max_rank). Default is ``max_rank - 2``.

        References
        ----------
        .. [1] B.A. van der Rotten, PhD thesis,
           "A limited memory Broyden method to solve high-dimensional
           systems of nonlinear equations". Mathematisch Instituut,
           Universiteit Leiden, The Netherlands (2003).

           https://web.archive.org/web/20161022015821/http://www.math.leidenuniv.nl/scripties/Rotten.pdf

        '''

class BroydenFirst(GenericBroyden):
    '''
    Find a root of a function, using Broyden\'s first Jacobian approximation.

    This method is also known as \\"Broyden\'s good method\\".

    Parameters
    ----------
    %(params_basic)s
    %(broyden_params)s
    %(params_extra)s

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method=\'broyden1\'`` in particular.

    Notes
    -----
    This algorithm implements the inverse Jacobian Quasi-Newton update

    .. math:: H_+ = H + (dx - H df) dx^\\dagger H / ( dx^\\dagger H df)

    which corresponds to Broyden\'s first Jacobian update

    .. math:: J_+ = J + (df - J dx) dx^\\dagger / dx^\\dagger dx


    References
    ----------
    .. [1] B.A. van der Rotten, PhD thesis,
       \\"A limited memory Broyden method to solve high-dimensional
       systems of nonlinear equations\\". Mathematisch Instituut,
       Universiteit Leiden, The Netherlands (2003).

       https://web.archive.org/web/20161022015821/http://www.math.leidenuniv.nl/scripties/Rotten.pdf

    Examples
    --------
    The following functions define a system of nonlinear equations

    >>> def fun(x):
    ...     return [x[0]  + 0.5 * (x[0] - x[1])**3 - 1.0,
    ...             0.5 * (x[1] - x[0])**3 + x[1]]

    A solution can be obtained as follows.

    >>> from scipy import optimize
    >>> sol = optimize.broyden1(fun, [0, 0])
    >>> sol
    array([0.84116396, 0.15883641])

    '''
    alpha: Incomplete
    Gm: Incomplete
    max_rank: Incomplete
    def __init__(self, alpha: Incomplete | None = None, reduction_method: str = 'restart', max_rank: Incomplete | None = None) -> None: ...
    def setup(self, x, F, func) -> None: ...
    def todense(self): ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...

class BroydenSecond(BroydenFirst):
    '''
    Find a root of a function, using Broyden\'s second Jacobian approximation.

    This method is also known as "Broyden\'s bad method".

    Parameters
    ----------
    %(params_basic)s
    %(broyden_params)s
    %(params_extra)s

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method=\'broyden2\'`` in particular.

    Notes
    -----
    This algorithm implements the inverse Jacobian Quasi-Newton update

    .. math:: H_+ = H + (dx - H df) df^\\dagger / ( df^\\dagger df)

    corresponding to Broyden\'s second method.

    References
    ----------
    .. [1] B.A. van der Rotten, PhD thesis,
       "A limited memory Broyden method to solve high-dimensional
       systems of nonlinear equations". Mathematisch Instituut,
       Universiteit Leiden, The Netherlands (2003).

       https://web.archive.org/web/20161022015821/http://www.math.leidenuniv.nl/scripties/Rotten.pdf

    Examples
    --------
    The following functions define a system of nonlinear equations

    >>> def fun(x):
    ...     return [x[0]  + 0.5 * (x[0] - x[1])**3 - 1.0,
    ...             0.5 * (x[1] - x[0])**3 + x[1]]

    A solution can be obtained as follows.

    >>> from scipy import optimize
    >>> sol = optimize.broyden2(fun, [0, 0])
    >>> sol
    array([0.84116365, 0.15883529])

    '''

class Anderson(GenericBroyden):
    """
    Find a root of a function, using (extended) Anderson mixing.

    The Jacobian is formed by for a 'best' solution in the space
    spanned by last `M` vectors. As a result, only a MxM matrix
    inversions and MxN multiplications are required. [Ey]_

    Parameters
    ----------
    %(params_basic)s
    alpha : float, optional
        Initial guess for the Jacobian is (-1/alpha).
    M : float, optional
        Number of previous vectors to retain. Defaults to 5.
    w0 : float, optional
        Regularization parameter for numerical stability.
        Compared to unity, good values of the order of 0.01.
    %(params_extra)s

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method='anderson'`` in particular.

    References
    ----------
    .. [Ey] V. Eyert, J. Comp. Phys., 124, 271 (1996).

    Examples
    --------
    The following functions define a system of nonlinear equations

    >>> def fun(x):
    ...     return [x[0]  + 0.5 * (x[0] - x[1])**3 - 1.0,
    ...             0.5 * (x[1] - x[0])**3 + x[1]]

    A solution can be obtained as follows.

    >>> from scipy import optimize
    >>> sol = optimize.anderson(fun, [0, 0])
    >>> sol
    array([0.84116588, 0.15883789])

    """
    alpha: Incomplete
    M: Incomplete
    dx: Incomplete
    df: Incomplete
    gamma: Incomplete
    w0: Incomplete
    def __init__(self, alpha: Incomplete | None = None, w0: float = 0.01, M: int = 5) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...

class DiagBroyden(GenericBroyden):
    """
    Find a root of a function, using diagonal Broyden Jacobian approximation.

    The Jacobian approximation is derived from previous iterations, by
    retaining only the diagonal of Broyden matrices.

    .. warning::

       This algorithm may be useful for specific problems, but whether
       it will work may depend strongly on the problem.

    Parameters
    ----------
    %(params_basic)s
    alpha : float, optional
        Initial guess for the Jacobian is (-1/alpha).
    %(params_extra)s

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method='diagbroyden'`` in particular.

    Examples
    --------
    The following functions define a system of nonlinear equations

    >>> def fun(x):
    ...     return [x[0]  + 0.5 * (x[0] - x[1])**3 - 1.0,
    ...             0.5 * (x[1] - x[0])**3 + x[1]]

    A solution can be obtained as follows.

    >>> from scipy import optimize
    >>> sol = optimize.diagbroyden(fun, [0, 0])
    >>> sol
    array([0.84116403, 0.15883384])

    """
    alpha: Incomplete
    def __init__(self, alpha: Incomplete | None = None) -> None: ...
    d: Incomplete
    def setup(self, x, F, func) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...
    def todense(self): ...

class LinearMixing(GenericBroyden):
    """
    Find a root of a function, using a scalar Jacobian approximation.

    .. warning::

       This algorithm may be useful for specific problems, but whether
       it will work may depend strongly on the problem.

    Parameters
    ----------
    %(params_basic)s
    alpha : float, optional
        The Jacobian approximation is (-1/alpha).
    %(params_extra)s

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method='linearmixing'`` in particular.

    """
    alpha: Incomplete
    def __init__(self, alpha: Incomplete | None = None) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...
    def todense(self): ...

class ExcitingMixing(GenericBroyden):
    """
    Find a root of a function, using a tuned diagonal Jacobian approximation.

    The Jacobian matrix is diagonal and is tuned on each iteration.

    .. warning::

       This algorithm may be useful for specific problems, but whether
       it will work may depend strongly on the problem.

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method='excitingmixing'`` in particular.

    Parameters
    ----------
    %(params_basic)s
    alpha : float, optional
        Initial Jacobian approximation is (-1/alpha).
    alphamax : float, optional
        The entries of the diagonal Jacobian are kept in the range
        ``[alpha, alphamax]``.
    %(params_extra)s
    """
    alpha: Incomplete
    alphamax: Incomplete
    beta: Incomplete
    def __init__(self, alpha: Incomplete | None = None, alphamax: float = 1.0) -> None: ...
    def setup(self, x, F, func) -> None: ...
    def solve(self, f, tol: int = 0): ...
    def matvec(self, f): ...
    def rsolve(self, f, tol: int = 0): ...
    def rmatvec(self, f): ...
    def todense(self): ...

class KrylovJacobian(Jacobian):
    '''
    Find a root of a function, using Krylov approximation for inverse Jacobian.

    This method is suitable for solving large-scale problems.

    Parameters
    ----------
    %(params_basic)s
    rdiff : float, optional
        Relative step size to use in numerical differentiation.
    method : str or callable, optional
        Krylov method to use to approximate the Jacobian.  Can be a string,
        or a function implementing the same interface as the iterative
        solvers in `scipy.sparse.linalg`. If a string, needs to be one of:
        ``\'lgmres\'``, ``\'gmres\'``, ``\'bicgstab\'``, ``\'cgs\'``, ``\'minres\'``,
        ``\'tfqmr\'``.

        The default is `scipy.sparse.linalg.lgmres`.
    inner_maxiter : int, optional
        Parameter to pass to the "inner" Krylov solver: maximum number of
        iterations. Iteration will stop after maxiter steps even if the
        specified tolerance has not been achieved.
    inner_M : LinearOperator or InverseJacobian
        Preconditioner for the inner Krylov iteration.
        Note that you can use also inverse Jacobians as (adaptive)
        preconditioners. For example,

        >>> from scipy.optimize import BroydenFirst, KrylovJacobian
        >>> from scipy.optimize import InverseJacobian
        >>> jac = BroydenFirst()
        >>> kjac = KrylovJacobian(inner_M=InverseJacobian(jac))

        If the preconditioner has a method named \'update\', it will be called
        as ``update(x, f)`` after each nonlinear step, with ``x`` giving
        the current point, and ``f`` the current function value.
    outer_k : int, optional
        Size of the subspace kept across LGMRES nonlinear iterations.
        See `scipy.sparse.linalg.lgmres` for details.
    inner_kwargs : kwargs
        Keyword parameters for the "inner" Krylov solver
        (defined with `method`). Parameter names must start with
        the `inner_` prefix which will be stripped before passing on
        the inner method. See, e.g., `scipy.sparse.linalg.gmres` for details.
    %(params_extra)s

    See Also
    --------
    root : Interface to root finding algorithms for multivariate
           functions. See ``method=\'krylov\'`` in particular.
    scipy.sparse.linalg.gmres
    scipy.sparse.linalg.lgmres

    Notes
    -----
    This function implements a Newton-Krylov solver. The basic idea is
    to compute the inverse of the Jacobian with an iterative Krylov
    method. These methods require only evaluating the Jacobian-vector
    products, which are conveniently approximated by a finite difference:

    .. math:: J v \\approx (f(x + \\omega*v/|v|) - f(x)) / \\omega

    Due to the use of iterative matrix inverses, these methods can
    deal with large nonlinear problems.

    SciPy\'s `scipy.sparse.linalg` module offers a selection of Krylov
    solvers to choose from. The default here is `lgmres`, which is a
    variant of restarted GMRES iteration that reuses some of the
    information obtained in the previous Newton steps to invert
    Jacobians in subsequent steps.

    For a review on Newton-Krylov methods, see for example [1]_,
    and for the LGMRES sparse inverse method, see [2]_.

    References
    ----------
    .. [1] C. T. Kelley, Solving Nonlinear Equations with Newton\'s Method,
           SIAM, pp.57-83, 2003.
           :doi:`10.1137/1.9780898718898.ch3`
    .. [2] D.A. Knoll and D.E. Keyes, J. Comp. Phys. 193, 357 (2004).
           :doi:`10.1016/j.jcp.2003.08.010`
    .. [3] A.H. Baker and E.R. Jessup and T. Manteuffel,
           SIAM J. Matrix Anal. Appl. 26, 962 (2005).
           :doi:`10.1137/S0895479803422014`

    Examples
    --------
    The following functions define a system of nonlinear equations

    >>> def fun(x):
    ...     return [x[0] + 0.5 * x[1] - 1.0,
    ...             0.5 * (x[1] - x[0]) ** 2]

    A solution can be obtained as follows.

    >>> from scipy import optimize
    >>> sol = optimize.newton_krylov(fun, [0, 0])
    >>> sol
    array([0.66731771, 0.66536458])

    '''
    preconditioner: Incomplete
    rdiff: Incomplete
    method: Incomplete
    method_kw: Incomplete
    def __init__(self, rdiff: Incomplete | None = None, method: str = 'lgmres', inner_maxiter: int = 20, inner_M: Incomplete | None = None, outer_k: int = 10, **kw) -> None: ...
    def matvec(self, v): ...
    def solve(self, rhs, tol: int = 0): ...
    x0: Incomplete
    f0: Incomplete
    def update(self, x, f) -> None: ...
    op: Incomplete
    def setup(self, x, f, func) -> None: ...

broyden1: Incomplete
broyden2: Incomplete
anderson: Incomplete
linearmixing: Incomplete
diagbroyden: Incomplete
excitingmixing: Incomplete
newton_krylov: Incomplete
