from _typeshed import Incomplete

__all__ = ['check_grads', 'check_jvp', 'check_vjp']

def check_jvp(f, f_jvp, args, atol: Incomplete | None = None, rtol: Incomplete | None = None, eps=..., err_msg: str = '') -> None: ...
def check_vjp(f, f_vjp, args, atol: Incomplete | None = None, rtol: Incomplete | None = None, eps=..., err_msg: str = '') -> None: ...
def check_grads(f, args, order, modes=('fwd', 'rev'), atol: Incomplete | None = None, rtol: Incomplete | None = None, eps: Incomplete | None = None):
    """Check gradients from automatic differentiation against finite differences.

  Gradients are only checked in a single randomly chosen direction, which
  ensures that the finite difference calculation does not become prohibitively
  expensive even for large input/output spaces.

  Args:
    f: function to check at ``f(*args)``.
    args: tuple of argument values.
    order: forward and backwards gradients up to this order are checked.
    modes: lists of gradient modes to check ('fwd' and/or 'rev').
    atol: absolute tolerance for gradient equality.
    rtol: relative tolerance for gradient equality.
    eps: step size used for finite differences.

  Raises:
    AssertionError: if gradients do not match.
  """
