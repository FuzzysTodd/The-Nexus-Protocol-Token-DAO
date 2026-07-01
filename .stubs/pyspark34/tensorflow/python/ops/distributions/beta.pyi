from _typeshed import Incomplete
from tensorflow.python.ops.distributions import distribution

__all__ = ['Beta', 'BetaWithSoftplusConcentration']

class Beta(distribution.Distribution):
    '''Beta distribution.

  The Beta distribution is defined over the `(0, 1)` interval using parameters
  `concentration1` (aka "alpha") and `concentration0` (aka "beta").

  #### Mathematical Details

  The probability density function (pdf) is,

  ```none
  pdf(x; alpha, beta) = x**(alpha - 1) (1 - x)**(beta - 1) / Z
  Z = Gamma(alpha) Gamma(beta) / Gamma(alpha + beta)
  ```

  where:

  * `concentration1 = alpha`,
  * `concentration0 = beta`,
  * `Z` is the normalization constant, and,
  * `Gamma` is the [gamma function](
    https://en.wikipedia.org/wiki/Gamma_function).

  The concentration parameters represent mean total counts of a `1` or a `0`,
  i.e.,

  ```none
  concentration1 = alpha = mean * total_concentration
  concentration0 = beta  = (1. - mean) * total_concentration
  ```

  where `mean` in `(0, 1)` and `total_concentration` is a positive real number
  representing a mean `total_count = concentration1 + concentration0`.

  Distribution parameters are automatically broadcast in all functions; see
  examples for details.

  Warning: The samples can be zero due to finite precision.
  This happens more often when some of the concentrations are very small.
  Make sure to round the samples to `np.finfo(dtype).tiny` before computing the
  density.

  Samples of this distribution are reparameterized (pathwise differentiable).
  The derivatives are computed using the approach described in
  (Figurnov et al., 2018).

  #### Examples

  ```python
  import tensorflow_probability as tfp
  tfd = tfp.distributions

  # Create a batch of three Beta distributions.
  alpha = [1, 2, 3]
  beta = [1, 2, 3]
  dist = tfd.Beta(alpha, beta)

  dist.sample([4, 5])  # Shape [4, 5, 3]

  # `x` has three batch entries, each with two samples.
  x = [[.1, .4, .5],
       [.2, .3, .5]]
  # Calculate the probability of each pair of samples under the corresponding
  # distribution in `dist`.
  dist.prob(x)         # Shape [2, 3]
  ```

  ```python
  # Create batch_shape=[2, 3] via parameter broadcast:
  alpha = [[1.], [2]]      # Shape [2, 1]
  beta = [3., 4, 5]        # Shape [3]
  dist = tfd.Beta(alpha, beta)

  # alpha broadcast as: [[1., 1, 1,],
  #                      [2, 2, 2]]
  # beta broadcast as:  [[3., 4, 5],
  #                      [3, 4, 5]]
  # batch_Shape [2, 3]
  dist.sample([4, 5])  # Shape [4, 5, 2, 3]

  x = [.2, .3, .5]
  # x will be broadcast as [[.2, .3, .5],
  #                         [.2, .3, .5]],
  # thus matching batch_shape [2, 3].
  dist.prob(x)         # Shape [2, 3]
  ```

  Compute the gradients of samples w.r.t. the parameters:

  ```python
  alpha = tf.constant(1.0)
  beta = tf.constant(2.0)
  dist = tfd.Beta(alpha, beta)
  samples = dist.sample(5)  # Shape [5]
  loss = tf.reduce_mean(tf.square(samples))  # Arbitrary loss function
  # Unbiased stochastic gradients of the loss function
  grads = tf.gradients(loss, [alpha, beta])
  ```

  References:
    Implicit Reparameterization Gradients:
      [Figurnov et al., 2018]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)
      ([pdf]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf))
  '''
    def __init__(self, concentration1: Incomplete | None = None, concentration0: Incomplete | None = None, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'Beta') -> None:
        '''Initialize a batch of Beta distributions.

    Args:
      concentration1: Positive floating-point `Tensor` indicating mean
        number of successes; aka "alpha". Implies `self.dtype` and
        `self.batch_shape`, i.e.,
        `concentration1.shape = [N1, N2, ..., Nm] = self.batch_shape`.
      concentration0: Positive floating-point `Tensor` indicating mean
        number of failures; aka "beta". Otherwise has same semantics as
        `concentration1`.
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
    def concentration1(self):
        """Concentration parameter associated with a `1` outcome."""
    @property
    def concentration0(self):
        """Concentration parameter associated with a `0` outcome."""
    @property
    def total_concentration(self):
        """Sum of concentration parameters."""

class BetaWithSoftplusConcentration(Beta):
    """Beta with softplus transform of `concentration1` and `concentration0`."""
    def __init__(self, concentration1, concentration0, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'BetaWithSoftplusConcentration') -> None: ...
