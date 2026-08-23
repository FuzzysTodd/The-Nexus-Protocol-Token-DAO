from _typeshed import Incomplete
from tensorflow.python.ops.distributions import special_math as special_math

def test_moment_matching(samples, number_moments, dist, stride: int = 0):
    """Return z-test scores for sample moments to match analytic moments.

  Given `samples`, check that the first sample `number_moments` match
  the given  `dist` moments by doing a z-test.

  Args:
    samples: Samples from target distribution.
    number_moments: Python `int` describing how many sample moments to check.
    dist: SciPy distribution object that provides analytic moments.
    stride: Distance between samples to check for statistical properties.
      A stride of 0 means to use all samples, while other strides test for
      spatial correlation.
  Returns:
    Array of z_test scores.
  """
def chi_squared(x, bins):
    """Pearson's Chi-squared test."""
def normal_cdf(x):
    """Cumulative distribution function for a standard normal distribution."""
def anderson_darling(x):
    """Anderson-Darling test for a standard normal distribution."""
def test_truncated_normal(assert_equal, assert_all_close, n, y, means: Incomplete | None = None, stddevs: Incomplete | None = None, minvals: Incomplete | None = None, maxvals: Incomplete | None = None, mean_atol: float = 0.0005, median_atol: float = 0.0008, variance_rtol: float = 0.001):
    """Tests truncated normal distribution's statistics."""
