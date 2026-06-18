from _typeshed import Incomplete
from tensorflow.python.ops.distributions import distribution as distribution_lib

__all__ = ['TransformedDistribution']

class TransformedDistribution(distribution_lib.Distribution):
    '''A Transformed Distribution.

  A `TransformedDistribution` models `p(y)` given a base distribution `p(x)`,
  and a deterministic, invertible, differentiable transform, `Y = g(X)`. The
  transform is typically an instance of the `Bijector` class and the base
  distribution is typically an instance of the `Distribution` class.

  A `Bijector` is expected to implement the following functions:
  - `forward`,
  - `inverse`,
  - `inverse_log_det_jacobian`.
  The semantics of these functions are outlined in the `Bijector` documentation.

  We now describe how a `TransformedDistribution` alters the input/outputs of a
  `Distribution` associated with a random variable (rv) `X`.

  Write `cdf(Y=y)` for an absolutely continuous cumulative distribution function
  of random variable `Y`; write the probability density function `pdf(Y=y) :=
  d^k / (dy_1,...,dy_k) cdf(Y=y)` for its derivative wrt to `Y` evaluated at
  `y`. Assume that `Y = g(X)` where `g` is a deterministic diffeomorphism,
  i.e., a non-random, continuous, differentiable, and invertible function.
  Write the inverse of `g` as `X = g^{-1}(Y)` and `(J o g)(x)` for the Jacobian
  of `g` evaluated at `x`.

  A `TransformedDistribution` implements the following operations:

    * `sample`
      Mathematically:   `Y = g(X)`
      Programmatically: `bijector.forward(distribution.sample(...))`

    * `log_prob`
      Mathematically:   `(log o pdf)(Y=y) = (log o pdf o g^{-1})(y)
                         + (log o abs o det o J o g^{-1})(y)`
      Programmatically: `(distribution.log_prob(bijector.inverse(y))
                         + bijector.inverse_log_det_jacobian(y))`

    * `log_cdf`
      Mathematically:   `(log o cdf)(Y=y) = (log o cdf o g^{-1})(y)`
      Programmatically: `distribution.log_cdf(bijector.inverse(x))`

    * and similarly for: `cdf`, `prob`, `log_survival_function`,
     `survival_function`.

  A simple example constructing a Log-Normal distribution from a Normal
  distribution:

  ```python
  ds = tfp.distributions
  log_normal = ds.TransformedDistribution(
    distribution=ds.Normal(loc=0., scale=1.),
    bijector=ds.bijectors.Exp(),
    name="LogNormalTransformedDistribution")
  ```

  A `LogNormal` made from callables:

  ```python
  ds = tfp.distributions
  log_normal = ds.TransformedDistribution(
    distribution=ds.Normal(loc=0., scale=1.),
    bijector=ds.bijectors.Inline(
      forward_fn=tf.exp,
      inverse_fn=tf.math.log,
      inverse_log_det_jacobian_fn=(
        lambda y: -tf.reduce_sum(tf.math.log(y), axis=-1)),
    name="LogNormalTransformedDistribution")
  ```

  Another example constructing a Normal from a StandardNormal:

  ```python
  ds = tfp.distributions
  normal = ds.TransformedDistribution(
    distribution=ds.Normal(loc=0., scale=1.),
    bijector=ds.bijectors.Affine(
      shift=-1.,
      scale_identity_multiplier=2.)
    name="NormalTransformedDistribution")
  ```

  A `TransformedDistribution`\'s batch- and event-shape are implied by the base
  distribution unless explicitly overridden by `batch_shape` or `event_shape`
  arguments. Specifying an overriding `batch_shape` (`event_shape`) is
  permitted only if the base distribution has scalar batch-shape (event-shape).
  The bijector is applied to the distribution as if the distribution possessed
  the overridden shape(s). The following example demonstrates how to construct a
  multivariate Normal as a `TransformedDistribution`.

  ```python
  ds = tfp.distributions
  # We will create two MVNs with batch_shape = event_shape = 2.
  mean = [[-1., 0],      # batch:0
          [0., 1]]       # batch:1
  chol_cov = [[[1., 0],
               [0, 1]],  # batch:0
              [[1, 0],
               [2, 2]]]  # batch:1
  mvn1 = ds.TransformedDistribution(
      distribution=ds.Normal(loc=0., scale=1.),
      bijector=ds.bijectors.Affine(shift=mean, scale_tril=chol_cov),
      batch_shape=[2],  # Valid because base_distribution.batch_shape == [].
      event_shape=[2])  # Valid because base_distribution.event_shape == [].
  mvn2 = ds.MultivariateNormalTriL(loc=mean, scale_tril=chol_cov)
  # mvn1.log_prob(x) == mvn2.log_prob(x)
  ```

  '''
    def __init__(self, distribution, bijector: Incomplete | None = None, batch_shape: Incomplete | None = None, event_shape: Incomplete | None = None, validate_args: bool = False, name: Incomplete | None = None) -> None:
        """Construct a Transformed Distribution.

    Args:
      distribution: The base distribution instance to transform. Typically an
        instance of `Distribution`.
      bijector: The object responsible for calculating the transformation.
        Typically an instance of `Bijector`. `None` means `Identity()`.
      batch_shape: `integer` vector `Tensor` which overrides `distribution`
        `batch_shape`; valid only if `distribution.is_scalar_batch()`.
      event_shape: `integer` vector `Tensor` which overrides `distribution`
        `event_shape`; valid only if `distribution.is_scalar_event()`.
      validate_args: Python `bool`, default `False`. When `True` distribution
        parameters are checked for validity despite possibly degrading runtime
        performance. When `False` invalid inputs may silently render incorrect
        outputs.
      name: Python `str` name prefixed to Ops created by this class. Default:
        `bijector.name + distribution.name`.
    """
    @property
    def distribution(self):
        """Base distribution, p(x)."""
    @property
    def bijector(self):
        """Function transforming x => y."""
