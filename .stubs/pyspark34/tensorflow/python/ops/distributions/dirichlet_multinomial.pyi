from tensorflow.python.ops.distributions import distribution

__all__ = ['DirichletMultinomial']

class DirichletMultinomial(distribution.Distribution):
    """Dirichlet-Multinomial compound distribution.

  The Dirichlet-Multinomial distribution is parameterized by a (batch of)
  length-`K` `concentration` vectors (`K > 1`) and a `total_count` number of
  trials, i.e., the number of trials per draw from the DirichletMultinomial. It
  is defined over a (batch of) length-`K` vector `counts` such that
  `tf.reduce_sum(counts, -1) = total_count`. The Dirichlet-Multinomial is
  identically the Beta-Binomial distribution when `K = 2`.

  #### Mathematical Details

  The Dirichlet-Multinomial is a distribution over `K`-class counts, i.e., a
  length-`K` vector of non-negative integer `counts = n = [n_0, ..., n_{K-1}]`.

  The probability mass function (pmf) is,

  ```none
  pmf(n; alpha, N) = Beta(alpha + n) / (prod_j n_j!) / Z
  Z = Beta(alpha) / N!
  ```

  where:

  * `concentration = alpha = [alpha_0, ..., alpha_{K-1}]`, `alpha_j > 0`,
  * `total_count = N`, `N` a positive integer,
  * `N!` is `N` factorial, and,
  * `Beta(x) = prod_j Gamma(x_j) / Gamma(sum_j x_j)` is the
    [multivariate beta function](
    https://en.wikipedia.org/wiki/Beta_function#Multivariate_beta_function),
    and,
  * `Gamma` is the [gamma function](
    https://en.wikipedia.org/wiki/Gamma_function).

  Dirichlet-Multinomial is a [compound distribution](
  https://en.wikipedia.org/wiki/Compound_probability_distribution), i.e., its
  samples are generated as follows.

    1. Choose class probabilities:
       `probs = [p_0,...,p_{K-1}] ~ Dir(concentration)`
    2. Draw integers:
       `counts = [n_0,...,n_{K-1}] ~ Multinomial(total_count, probs)`

  The last `concentration` dimension parametrizes a single Dirichlet-Multinomial
  distribution. When calling distribution functions (e.g., `dist.prob(counts)`),
  `concentration`, `total_count` and `counts` are broadcast to the same shape.
  The last dimension of `counts` corresponds single Dirichlet-Multinomial
  distributions.

  Distribution parameters are automatically broadcast in all functions; see
  examples for details.

  #### Pitfalls

  The number of classes, `K`, must not exceed:
  - the largest integer representable by `self.dtype`, i.e.,
    `2**(mantissa_bits+1)` (IEE754),
  - the maximum `Tensor` index, i.e., `2**31-1`.

  In other words,

  ```python
  K <= min(2**31-1, {
    tf.float16: 2**11,
    tf.float32: 2**24,
    tf.float64: 2**53 }[param.dtype])
  ```

  Note: This condition is validated only when `self.validate_args = True`.

  #### Examples

  ```python
  alpha = [1., 2., 3.]
  n = 2.
  dist = DirichletMultinomial(n, alpha)
  ```

  Creates a 3-class distribution, with the 3rd class is most likely to be
  drawn.
  The distribution functions can be evaluated on counts.

  ```python
  # counts same shape as alpha.
  counts = [0., 0., 2.]
  dist.prob(counts)  # Shape []

  # alpha will be broadcast to [[1., 2., 3.], [1., 2., 3.]] to match counts.
  counts = [[1., 1., 0.], [1., 0., 1.]]
  dist.prob(counts)  # Shape [2]

  # alpha will be broadcast to shape [5, 7, 3] to match counts.
  counts = [[...]]  # Shape [5, 7, 3]
  dist.prob(counts)  # Shape [5, 7]
  ```

  Creates a 2-batch of 3-class distributions.

  ```python
  alpha = [[1., 2., 3.], [4., 5., 6.]]  # Shape [2, 3]
  n = [3., 3.]
  dist = DirichletMultinomial(n, alpha)

  # counts will be broadcast to [[2., 1., 0.], [2., 1., 0.]] to match alpha.
  counts = [2., 1., 0.]
  dist.prob(counts)  # Shape [2]
  ```

  """
    def __init__(self, total_count, concentration, validate_args: bool = False, allow_nan_stats: bool = True, name: str = 'DirichletMultinomial') -> None:
        '''Initialize a batch of DirichletMultinomial distributions.

    Args:
      total_count:  Non-negative floating point tensor, whose dtype is the same
        as `concentration`. The shape is broadcastable to `[N1,..., Nm]` with
        `m >= 0`. Defines this as a batch of `N1 x ... x Nm` different
        Dirichlet multinomial distributions. Its components should be equal to
        integer values.
      concentration: Positive floating point tensor, whose dtype is the
        same as `n` with shape broadcastable to `[N1,..., Nm, K]` `m >= 0`.
        Defines this as a batch of `N1 x ... x Nm` different `K` class Dirichlet
        multinomial distributions.
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
    def total_count(self):
        """Number of trials used to construct a sample."""
    @property
    def concentration(self):
        """Concentration parameter; expected prior counts for that coordinate."""
    @property
    def total_concentration(self):
        """Sum of last dim of concentration parameter."""
