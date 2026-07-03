from _typeshed import Incomplete
from jax import device_put as device_put, lax as lax
from jax._src import dtypes as dtypes
from jax.tree_util import Partial as Partial, tree_leaves as tree_leaves, tree_map as tree_map, tree_reduce as tree_reduce, tree_structure as tree_structure

def cg(A, b, x0: Incomplete | None = None, *, tol: float = 1e-05, atol: float = 0.0, maxiter: Incomplete | None = None, M: Incomplete | None = None):
    '''Use Conjugate Gradient iteration to solve ``Ax = b``.

  The numerics of JAX\'s ``cg`` should exact match SciPy\'s ``cg`` (up to
  numerical precision), but note that the interface is slightly different: you
  need to supply the linear operator ``A`` as a function instead of a sparse
  matrix or ``LinearOperator``.

  Derivatives of ``cg`` are implemented via implicit differentiation with
  another ``cg`` solve, rather than by differentiating *through* the solver.
  They will be accurate only if both solves converge.

  Parameters
  ----------
  A: ndarray, function, or matmul-compatible object
      2D array or function that calculates the linear map (matrix-vector
      product) ``Ax`` when called like ``A(x)`` or ``A @ x``. ``A`` must represent
      a hermitian, positive definite matrix, and must return array(s) with the
      same structure and shape as its argument.
  b : array or tree of arrays
      Right hand side of the linear system representing a single vector. Can be
      stored as an array or Python container of array(s) with any shape.

  Returns
  -------
  x : array or tree of arrays
      The converged solution. Has the same structure as ``b``.
  info : None
      Placeholder for convergence information. In the future, JAX will report
      the number of iterations when convergence is not achieved, like SciPy.

  Other Parameters
  ----------------
  x0 : array or tree of arrays
      Starting guess for the solution. Must have the same structure as ``b``.
  tol, atol : float, optional
      Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
      We do not implement SciPy\'s "legacy" behavior, so JAX\'s tolerance will
      differ from SciPy unless you explicitly pass ``atol`` to SciPy\'s ``cg``.
  maxiter : integer
      Maximum number of iterations.  Iteration will stop after maxiter
      steps even if the specified tolerance has not been achieved.
  M : ndarray, function, or matmul-compatible object
      Preconditioner for A.  The preconditioner should approximate the
      inverse of A.  Effective preconditioning dramatically improves the
      rate of convergence, which implies that fewer iterations are needed
      to reach a given error tolerance.

  See also
  --------
  scipy.sparse.linalg.cg
  jax.lax.custom_linear_solve
  '''
def gmres(A, b, x0: Incomplete | None = None, *, tol: float = 1e-05, atol: float = 0.0, restart: int = 20, maxiter: Incomplete | None = None, M: Incomplete | None = None, solve_method: str = 'batched'):
    '''
  GMRES solves the linear system A x = b for x, given A and b.

  A is specified as a function performing A(vi) -> vf = A @ vi, and in principle
  need not have any particular special properties, such as symmetry. However,
  convergence is often slow for nearly symmetric operators.

  Parameters
  ----------
  A: ndarray, function, or matmul-compatible object
      2D array or function that calculates the linear map (matrix-vector
      product) ``Ax`` when called like ``A(x)`` or ``A @ x``. ``A``
      must return array(s) with the same structure and shape as its argument.
  b : array or tree of arrays
      Right hand side of the linear system representing a single vector. Can be
      stored as an array or Python container of array(s) with any shape.

  Returns
  -------
  x : array or tree of arrays
      The converged solution. Has the same structure as ``b``.
  info : None
      Placeholder for convergence information. In the future, JAX will report
      the number of iterations when convergence is not achieved, like SciPy.

  Other Parameters
  ----------------
  x0 : array or tree of arrays, optional
      Starting guess for the solution. Must have the same structure as ``b``.
      If this is unspecified, zeroes are used.
  tol, atol : float, optional
      Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
      We do not implement SciPy\'s "legacy" behavior, so JAX\'s tolerance will
      differ from SciPy unless you explicitly pass ``atol`` to SciPy\'s ``gmres``.
  restart : integer, optional
      Size of the Krylov subspace ("number of iterations") built between
      restarts. GMRES works by approximating the true solution x as its
      projection into a Krylov space of this dimension - this parameter
      therefore bounds the maximum accuracy achievable from any guess
      solution. Larger values increase both number of iterations and iteration
      cost, but may be necessary for convergence. The algorithm terminates
      early if convergence is achieved before the full subspace is built.
      Default is 20.
  maxiter : integer
      Maximum number of times to rebuild the size-``restart`` Krylov space
      starting from the solution found at the last iteration. If GMRES
      halts or is very slow, decreasing this parameter may help.
      Default is infinite.
  M : ndarray, function, or matmul-compatible object
      Preconditioner for A.  The preconditioner should approximate the
      inverse of A.  Effective preconditioning dramatically improves the
      rate of convergence, which implies that fewer iterations are needed
      to reach a given error tolerance.
  solve_method : \'incremental\' or \'batched\'
      The \'incremental\' solve method builds a QR decomposition for the Krylov
      subspace incrementally during the GMRES process using Givens rotations.
      This improves numerical stability and gives a free estimate of the
      residual norm that allows for early termination within a single "restart".
      In contrast, the \'batched\' solve method solves the least squares problem
      from scratch at the end of each GMRES iteration. It does not allow for
      early termination, but has much less overhead on GPUs.

  See also
  --------
  scipy.sparse.linalg.gmres
  jax.lax.custom_linear_solve
  '''
def bicgstab(A, b, x0: Incomplete | None = None, *, tol: float = 1e-05, atol: float = 0.0, maxiter: Incomplete | None = None, M: Incomplete | None = None):
    '''Use Bi-Conjugate Gradient Stable iteration to solve ``Ax = b``.

  The numerics of JAX\'s ``bicgstab`` should exact match SciPy\'s
  ``bicgstab`` (up to numerical precision), but note that the interface
  is slightly different: you need to supply the linear operator ``A`` as
  a function instead of a sparse matrix or ``LinearOperator``.

  As with ``cg``, derivatives of ``bicgstab`` are implemented via implicit
  differentiation with another ``bicgstab`` solve, rather than by
  differentiating *through* the solver. They will be accurate only if
  both solves converge.

  Parameters
  ----------
  A: ndarray, function, or matmul-compatible object
      2D array or function that calculates the linear map (matrix-vector
      product) ``Ax`` when called like ``A(x)`` or ``A @ x``. ``A`` can represent
      any general (nonsymmetric) linear operator, and function must return array(s)
      with the same structure and shape as its argument.
  b : array or tree of arrays
      Right hand side of the linear system representing a single vector. Can be
      stored as an array or Python container of array(s) with any shape.

  Returns
  -------
  x : array or tree of arrays
      The converged solution. Has the same structure as ``b``.
  info : None
      Placeholder for convergence information. In the future, JAX will report
      the number of iterations when convergence is not achieved, like SciPy.

  Other Parameters
  ----------------
  x0 : array or tree of arrays
      Starting guess for the solution. Must have the same structure as ``b``.
  tol, atol : float, optional
      Tolerances for convergence, ``norm(residual) <= max(tol*norm(b), atol)``.
      We do not implement SciPy\'s "legacy" behavior, so JAX\'s tolerance will
      differ from SciPy unless you explicitly pass ``atol`` to SciPy\'s ``cg``.
  maxiter : integer
      Maximum number of iterations.  Iteration will stop after maxiter
      steps even if the specified tolerance has not been achieved.
  M : ndarray, function, or matmul-compatible object
      Preconditioner for A.  The preconditioner should approximate the
      inverse of A.  Effective preconditioning dramatically improves the
      rate of convergence, which implies that fewer iterations are needed
      to reach a given error tolerance.

  See also
  --------
  scipy.sparse.linalg.bicgstab
  jax.lax.custom_linear_solve
  '''
