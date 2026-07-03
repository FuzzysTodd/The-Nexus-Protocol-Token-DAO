from _typeshed import Incomplete
from jax import lax as lax
from jax._src import core as core

def qdwh(x, *, is_hermitian: bool = False, max_iterations: Incomplete | None = None, eps: Incomplete | None = None, dynamic_shape: tuple[int, int] | None = None):
    """QR-based dynamically weighted Halley iteration for polar decomposition.

  Args:
    x: A full-rank matrix, with shape `M x N`. The matrix may be
      padded up to that size from a smaller true shape (``dynamic_shape``).
    is_hermitian: True if `x` is Hermitian. Default to `False`.
    eps: The final result will satisfy
      ``|x_k - x_k-1| < |x_k| * (4*eps)**(1/3)`` where `x_k` is the iterate.
    max_iterations: Iterations will terminate after this many steps even if the
      above is unsatisfied.
    dynamic_shape: the unpadded shape as an ``(m, n)`` tuple; optional.

  Returns:
    A four-tuple of (u, h, num_iters, is_converged) containing the
    polar decomposition of `x = u * h`, the number of iterations to compute `u`,
    and `is_converged`, whose value is `True` when the convergence is achieved
    within the maximum number of iterations.
  """
