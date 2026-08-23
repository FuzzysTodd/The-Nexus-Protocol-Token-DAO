import jax
from jax import lax as lax
from jax._src.scipy.optimize.line_search import line_search as line_search
from typing import Callable, NamedTuple

class _BFGSResults(NamedTuple):
    """Results from BFGS optimization.

  Parameters:
    converged: True if minimization converged.
    failed: True if line search failed.
    k: integer the number of iterations of the BFGS update.
    nfev: integer total number of objective evaluations performed.
    ngev: integer total number of jacobian evaluations
    nhev: integer total number of hessian evaluations
    x_k: array containing the last argument value found during the search. If
      the search converged, then this value is the argmin of the objective
      function.
    f_k: array containing the value of the objective function at `x_k`. If the
      search converged, then this is the (local) minimum of the objective
      function.
    g_k: array containing the gradient of the objective function at `x_k`. If
      the search converged the l2-norm of this tensor should be below the
      tolerance.
    H_k: array containing the inverse of the estimated Hessian.
    status: int describing end state.
    line_search_status: int describing line search end state (only means
      something if line search fails).
  """
    converged: bool | jax.Array
    failed: bool | jax.Array
    k: int | jax.Array
    nfev: int | jax.Array
    ngev: int | jax.Array
    nhev: int | jax.Array
    x_k: jax.Array
    f_k: jax.Array
    g_k: jax.Array
    H_k: jax.Array
    old_old_fval: jax.Array
    status: int | jax.Array
    line_search_status: int | jax.Array

def minimize_bfgs(fun: Callable, x0: jax.Array, maxiter: int | None = None, norm=..., gtol: float = 1e-05, line_search_maxiter: int = 10) -> _BFGSResults:
    """Minimize a function using BFGS.

  Implements the BFGS algorithm from
    Algorithm 6.1 from Wright and Nocedal, 'Numerical Optimization', 1999, pg.
    136-143.

  Args:
    fun: function of the form f(x) where x is a flat ndarray and returns a real
      scalar. The function should be composed of operations with vjp defined.
    x0: initial guess.
    maxiter: maximum number of iterations.
    norm: order of norm for convergence check. Default inf.
    gtol: terminates minimization when |grad|_norm < g_tol.
    line_search_maxiter: maximum number of linesearch iterations.

  Returns:
    Optimization result.
  """
