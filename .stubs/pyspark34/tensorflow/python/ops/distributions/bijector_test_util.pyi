from _typeshed import Incomplete
from tensorflow.python.framework import ops as ops
from tensorflow.python.ops import math_ops as math_ops

def assert_finite(array) -> None: ...
def assert_strictly_increasing(array) -> None: ...
def assert_strictly_decreasing(array) -> None: ...
def assert_strictly_monotonic(array) -> None: ...
def assert_scalar_congruency(bijector, lower_x, upper_x, n=..., rtol: float = 0.01, sess: Incomplete | None = None) -> None:
    """Assert `bijector`'s forward/inverse/inverse_log_det_jacobian are congruent.

  We draw samples `X ~ U(lower_x, upper_x)`, then feed these through the
  `bijector` in order to check that:

  1. the forward is strictly monotonic.
  2. the forward/inverse methods are inverses of each other.
  3. the jacobian is the correct change of measure.

  This can only be used for a Bijector mapping open subsets of the real line
  to themselves.  This is due to the fact that this test compares the `prob`
  before/after transformation with the Lebesgue measure on the line.

  Args:
    bijector:  Instance of Bijector
    lower_x:  Python scalar.
    upper_x:  Python scalar.  Must have `lower_x < upper_x`, and both must be in
      the domain of the `bijector`.  The `bijector` should probably not produce
      huge variation in values in the interval `(lower_x, upper_x)`, or else
      the variance based check of the Jacobian will require small `rtol` or
      huge `n`.
    n:  Number of samples to draw for the checks.
    rtol:  Positive number.  Used for the Jacobian check.
    sess:  `tf.compat.v1.Session`.  Defaults to the default session.

  Raises:
    AssertionError:  If tests fail.
  """
def assert_bijective_and_finite(bijector, x, y, event_ndims, atol: int = 0, rtol: float = 1e-05, sess: Incomplete | None = None) -> None:
    """Assert that forward/inverse (along with jacobians) are inverses and finite.

  It is recommended to use x and y values that are very very close to the edge
  of the Bijector's domain.

  Args:
    bijector:  A Bijector instance.
    x:  np.array of values in the domain of bijector.forward.
    y:  np.array of values in the domain of bijector.inverse.
    event_ndims: Integer describing the number of event dimensions this bijector
      operates on.
    atol:  Absolute tolerance.
    rtol:  Relative tolerance.
    sess:  TensorFlow session.  Defaults to the default session.

  Raises:
    AssertionError:  If tests fail.
  """
