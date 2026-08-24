from tensorflow.python.ops.distributions import gamma

__all__ = ['Exponential', 'ExponentialWithSoftplusRate']

class Exponential(gamma.Gamma):
    '''Exponential distribution.

  The Exponential distribution is parameterized by an event `rate` parameter.

  #### Mathematical Details

  The probability density function (pdf) is,

  ```none
  pdf(x; lambda, x > 0) = exp(-lambda x) / Z
  Z = 1 / lambda
  ```

  where `rate = lambda` and `Z` is the normalizaing constant.

  The Exponential distribution is a special case of the Gamma distribution,
  i.e.,

  ```python
  Exponential(rate) = Gamma(concentration=1., rate)
  ```

  The Exponential distribution uses a `rate` parameter, or "inverse scale",
  which can be intuited as,

  ```none
  X ~ Exponential(rate=1)
  Y = X / rate
  ```

  '''
    def __init__(self, rate, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'Exponential') -> None:
        '''Construct Exponential distribution with parameter `rate`.

    Args:
      rate: Floating point tensor, equivalent to `1 / mean`. Must contain only
        positive values.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic\'s batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.
    '''
    @property
    def rate(self): ...

class ExponentialWithSoftplusRate(Exponential):
    """Exponential with softplus transform on `rate`."""
    def __init__(self, rate, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'ExponentialWithSoftplusRate') -> None: ...
