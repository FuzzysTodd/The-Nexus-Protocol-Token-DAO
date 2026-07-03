from _typeshed import Incomplete
from collections.abc import Generator
from jax import custom_derivatives as custom_derivatives, lax as lax
from jax._src import core as core
from jax._src.numpy.util import promote_dtypes_inexact as promote_dtypes_inexact
from jax._src.util import safe_map as safe_map, safe_zip as safe_zip
from jax.flatten_util import ravel_pytree as ravel_pytree
from jax.tree_util import tree_leaves as tree_leaves, tree_map as tree_map

map = safe_map
zip = safe_zip

def ravel_first_arg(f, unravel): ...
def ravel_first_arg_(unravel, y_flat, *args) -> Generator[Incomplete, Incomplete, None]: ...
def interp_fit_dopri(y0, y1, k, dt): ...
def fit_4th_order_polynomial(y0, y1, y_mid, dy0, dy1, dt): ...
def initial_step_size(fun, t0, y0, order, rtol, atol, f0): ...
def runge_kutta_step(func, y0, f0, t0, dt): ...
def abs2(x): ...
def mean_error_ratio(error_estimate, rtol, atol, y0, y1): ...
def optimal_step_size(last_step, mean_error_ratio, safety: float = 0.9, ifactor: float = 10.0, dfactor: float = 0.2, order: float = 5.0):
    """Compute optimal Runge-Kutta stepsize."""
def odeint(func, y0, t, *args, rtol: float = 1.4e-08, atol: float = 1.4e-08, mxstep=..., hmax=...):
    """Adaptive stepsize (Dormand-Prince) Runge-Kutta odeint implementation.

  Args:
    func: function to evaluate the time derivative of the solution `y` at time
      `t` as `func(y, t, *args)`, producing the same shape/structure as `y0`.
    y0: array or pytree of arrays representing the initial value for the state.
    t: array of float times for evaluation, like `jnp.linspace(0., 10., 101)`,
      in which the values must be strictly increasing.
    *args: tuple of additional arguments for `func`, which must be arrays
      scalars, or (nested) standard Python containers (tuples, lists, dicts,
      namedtuples, i.e. pytrees) of those types.
    rtol: float, relative local error tolerance for solver (optional).
    atol: float, absolute local error tolerance for solver (optional).
    mxstep: int, maximum number of steps to take for each timepoint (optional).
    hmax: float, maximum step size allowed (optional).

  Returns:
    Values of the solution `y` (i.e. integrated system values) at each time
    point in `t`, represented as an array (or pytree of arrays) with the same
    shape/structure as `y0` except with a new leading axis of length `len(t)`.
  """
