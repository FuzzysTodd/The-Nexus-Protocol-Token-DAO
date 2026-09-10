from tensorflow.python.ops.distributions import distribution

__all__ = ['Laplace', 'LaplaceWithSoftplusScale']

class Laplace(distribution.Distribution):
    '''The Laplace distribution with location `loc` and `scale` parameters.

  #### Mathematical details

  The probability density function (pdf) of this distribution is,

  ```none
  pdf(x; mu, sigma) = exp(-|x - mu| / sigma) / Z
  Z = 2 sigma
  ```

  where `loc = mu`, `scale = sigma`, and `Z` is the normalization constant.

  Note that the Laplace distribution can be thought of two exponential
  distributions spliced together "back-to-back."

  The Lpalce distribution is a member of the [location-scale family](
  https://en.wikipedia.org/wiki/Location-scale_family), i.e., it can be
  constructed as,

  ```none
  X ~ Laplace(loc=0, scale=1)
  Y = loc + scale * X
  ```

  '''
    def __init__(self, loc, scale, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'Laplace') -> None:
        '''Construct Laplace distribution with parameters `loc` and `scale`.

    The parameters `loc` and `scale` must be shaped in a way that supports
    broadcasting (e.g., `loc / scale` is a valid operation).

    Args:
      loc: Floating point tensor which characterizes the location (center)
        of the distribution.
      scale: Positive floating point tensor which characterizes the spread of
        the distribution.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`,
        statistics (e.g., mean, mode, variance) use the value "`NaN`" to
        indicate the result is undefined. When `False`, an exception is raised
        if one or more of the statistic\'s batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      TypeError: if `loc` and `scale` are of different dtype.
    '''
    @property
    def loc(self):
        """Distribution parameter for the location."""
    @property
    def scale(self):
        """Distribution parameter for scale."""

class LaplaceWithSoftplusScale(Laplace):
    """Laplace with softplus applied to `scale`."""
    def __init__(self, loc, scale, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'LaplaceWithSoftplusScale') -> None: ...
