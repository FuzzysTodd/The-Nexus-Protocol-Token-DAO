import jax
from _typeshed import Incomplete
from jax import lax as lax
from jax._src.numpy.util import promote_dtypes_inexact as promote_dtypes_inexact
from typing import NamedTuple

class _ZoomState(NamedTuple):
    done: bool | jax.Array
    failed: bool | jax.Array
    j: int | jax.Array
    a_lo: float | jax.Array
    phi_lo: float | jax.Array
    dphi_lo: float | jax.Array
    a_hi: float | jax.Array
    phi_hi: float | jax.Array
    dphi_hi: float | jax.Array
    a_rec: float | jax.Array
    phi_rec: float | jax.Array
    a_star: float | jax.Array
    phi_star: float | jax.Array
    dphi_star: float | jax.Array
    g_star: float | jax.Array
    nfev: int | jax.Array
    ngev: int | jax.Array

class _LineSearchState(NamedTuple):
    done: bool | jax.Array
    failed: bool | jax.Array
    i: int | jax.Array
    a_i1: float | jax.Array
    phi_i1: float | jax.Array
    dphi_i1: float | jax.Array
    nfev: int | jax.Array
    ngev: int | jax.Array
    a_star: float | jax.Array
    phi_star: float | jax.Array
    dphi_star: float | jax.Array
    g_star: jax.Array

class _LineSearchResults(NamedTuple):
    """Results of line search.

  Parameters:
    failed: True if the strong Wolfe criteria were satisfied
    nit: integer number of iterations
    nfev: integer number of functions evaluations
    ngev: integer number of gradients evaluations
    k: integer number of iterations
    a_k: integer step size
    f_k: final function value
    g_k: final gradient value
    status: integer end status
  """
    failed: bool | jax.Array
    nit: int | jax.Array
    nfev: int | jax.Array
    ngev: int | jax.Array
    k: int | jax.Array
    a_k: int | jax.Array
    f_k: jax.Array
    g_k: jax.Array
    status: bool | jax.Array

def line_search(f, xk, pk, old_fval: Incomplete | None = None, old_old_fval: Incomplete | None = None, gfk: Incomplete | None = None, c1: float = 0.0001, c2: float = 0.9, maxiter: int = 20):
    """Inexact line search that satisfies strong Wolfe conditions.

  Algorithm 3.5 from Wright and Nocedal, 'Numerical Optimization', 1999, pg. 59-61

  Args:
    fun: function of the form f(x) where x is a flat ndarray and returns a real
      scalar. The function should be composed of operations with vjp defined.
    x0: initial guess.
    pk: direction to search in. Assumes the direction is a descent direction.
    old_fval, gfk: initial value of value_and_gradient as position.
    old_old_fval: unused argument, only for scipy API compliance.
    maxiter: maximum number of iterations to search
    c1, c2: Wolfe criteria constant, see ref.

  Returns: LineSearchResults
  """
