from tensorflow.python.ops.distributions import distribution

__all__ = ['Gamma', 'GammaWithSoftplusConcentrationRate']

class Gamma(distribution.Distribution):
    '''Gamma distribution.

  The Gamma distribution is defined over positive real numbers using
  parameters `concentration` (aka "alpha") and `rate` (aka "beta").

  #### Mathematical Details

  The probability density function (pdf) is,

  ```none
  pdf(x; alpha, beta, x > 0) = x**(alpha - 1) exp(-x beta) / Z
  Z = Gamma(alpha) beta**(-alpha)
  ```

  where:

  * `concentration = alpha`, `alpha > 0`,
  * `rate = beta`, `beta > 0`,
  * `Z` is the normalizing constant, and,
  * `Gamma` is the [gamma function](
    https://en.wikipedia.org/wiki/Gamma_function).

  The cumulative density function (cdf) is,

  ```none
  cdf(x; alpha, beta, x > 0) = GammaInc(alpha, beta x) / Gamma(alpha)
  ```

  where `GammaInc` is the [lower incomplete Gamma function](
  https://en.wikipedia.org/wiki/Incomplete_gamma_function).

  The parameters can be intuited via their relationship to mean and stddev,

  ```none
  concentration = alpha = (mean / stddev)**2
  rate = beta = mean / stddev**2 = concentration / mean
  ```

  Distribution parameters are automatically broadcast in all functions; see
  examples for details.

  Warning: The samples of this distribution are always non-negative. However,
  the samples that are smaller than `np.finfo(dtype).tiny` are rounded
  to this value, so it appears more often than it should.
  This should only be noticeable when the `concentration` is very small, or the
  `rate` is very large. See note in `tf.random.gamma` docstring.

  Samples of this distribution are reparameterized (pathwise differentiable).
  The derivatives are computed using the approach described in
  (Figurnov et al., 2018).

  #### Examples

  ```python
  import tensorflow_probability as tfp
  tfd = tfp.distributions

  dist = tfd.Gamma(concentration=3.0, rate=2.0)
  dist2 = tfd.Gamma(concentration=[3.0, 4.0], rate=[2.0, 3.0])
  ```

  Compute the gradients of samples w.r.t. the parameters:

  ```python
  concentration = tf.constant(3.0)
  rate = tf.constant(2.0)
  dist = tfd.Gamma(concentration, rate)
  samples = dist.sample(5)  # Shape [5]
  loss = tf.reduce_mean(tf.square(samples))  # Arbitrary loss function
  # Unbiased stochastic gradients of the loss function
  grads = tf.gradients(loss, [concentration, rate])
  ```

  References:
    Implicit Reparameterization Gradients:
      [Figurnov et al., 2018]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)
      ([pdf](http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf))
  '''
    def __init__(self, concentration, rate, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'Gamma') -> None:
        '''Construct Gamma with `concentration` and `rate` parameters.

    The parameters `concentration` and `rate` must be shaped in a way that
    supports broadcasting (e.g. `concentration + rate` is a valid operation).

    Args:
      concentration: Floating point tensor, the concentration params of the
        distribution(s). Must contain only positive values.
      rate: Floating point tensor, the inverse scale params of the
        distribution(s). Must contain only positive values.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      allow_nan_stats: Python `bool`, default `True`. When `True`, statistics
        (e.g., mean, mode, variance) use the value "`NaN`" to indicate the
        result is undefined. When `False`, an exception is raised if one or
        more of the statistic\'s batch members are undefined.
      name: Python `str` name prefixed to Ops created by this class.

    Raises:
      TypeError: if `concentration` and `rate` are different dtypes.
    '''
    @property
    def concentration(self):
        """Concentration parameter."""
    @property
    def rate(self):
        """Rate parameter."""

class GammaWithSoftplusConcentrationRate(Gamma):
    """`Gamma` with softplus of `concentration` and `rate`."""
    def __init__(self, concentration, rate, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'GammaWithSoftplusConcentrationRate') -> None: ...
