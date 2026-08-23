from _typeshed import Incomplete
from typing import NamedTuple

class RuntimeCounter(NamedTuple):
    runtime_secs: Incomplete
    steps: Incomplete
    step_time_secs: Incomplete

class IterationCountEstimator:
    """Estimates iterations count using past iterations runtime.

  The estimator collects iterations elapsed time (in seconds) and store it into
  a circular buffer. As it learns enough samples, it computes the mean value of
  the past observed iterations elapsed time to estimate the number of iterations
  count to run within the alloted time budget in seconds.

  To keep the buffer from growing indefinitely, we limit the size by the virtue
  of using circular buffer. As it uses the mean of iterations runtime to compute
  the iterations count estimate, setting a larger buffer size will smooth out
  the estimation. Once the buffer is getting filled up, older values will be
  dequeued in FIFO order. Setting larger buffer size will make the estimator
  less sensitive to runtime fluctuations but will result in slower convergence.
  For faster convergence buffer size can be set smaller but more prone to
  runtime fluctuations.

  As a safety feature, the estimator will return default iterations value,
  when:
  1. The circular buffer is empty (initially).
  2. The user input is invalid.
  """
    def __init__(self, capacity: int = 20) -> None:
        """Constructs a new `IterationsEstimator` instance.

    Args:
      capacity: Size of circular buffer to hold timer values. Each timer value
        represents the time spent on the last iterations.

    Raises:
      ValueError: If one or more parameters specified is invalid.
    """
    def update(self, runtime_secs, count) -> None:
        """Updates the unit time spent per iteration.

    Args:
      runtime_secs: The total elapsed time in seconds.
      count: The number of iterations.
    """
    def get(self, total_secs):
        """Gets the iterations count estimate.

    If recent predicted iterations are stable, re-use the previous value.
    Otherwise, update the prediction value based on the delta between the
    current prediction and the expected number of iterations as determined by
    the per-step runtime.

    Args:
      total_secs: The target runtime in seconds.

    Returns:
      The number of iterations as estimate.

    Raise:
      ValueError: If `total_secs` value is not positive.
    """
