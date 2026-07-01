from jax import lax as lax
from jax._src.scipy.optimize.line_search import line_search as line_search
from jax._src.typing import Array as Array
from typing import NamedTuple

class LBFGSResults(NamedTuple):
    """Results from L-BFGS optimization

  Parameters:
    converged: True if minimization converged
    failed: True if non-zero status and not converged
    k: integer number of iterations of the main loop (optimisation steps)
    nfev: integer total number of objective evaluations performed.
    ngev: integer total number of jacobian evaluations
    x_k: array containing the last argument value found during the search. If
      the search converged, then this value is the argmin of the objective
      function.
    f_k: array containing the value of the objective function at `x_k`. If the
      search converged, then this is the (local) minimum of the objective
      function.
    g_k: array containing the gradient of the objective function at `x_k`. If
      the search converged the l2-norm of this tensor should be below the
      tolerance.
    status: integer describing the status:
      0 = nominal  ,  1 = max iters reached  ,  2 = max fun evals reached
      3 = max grad evals reached  ,  4 = insufficient progress (ftol)
      5 = line search failed
    ls_status: integer describing the end status of the last line search
  """
    converged: bool | Array
    failed: bool | Array
    k: int | Array
    nfev: int | Array
    ngev: int | Array
    x_k: Array
    f_k: Array
    g_k: Array
    s_history: Array
    y_history: Array
    rho_history: Array
    gamma: float | Array
    status: int | Array
    ls_status: int | Array
