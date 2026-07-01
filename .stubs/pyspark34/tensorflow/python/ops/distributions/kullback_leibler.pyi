from _typeshed import Incomplete

__all__ = ['RegisterKL', 'kl_divergence']

def kl_divergence(distribution_a, distribution_b, allow_nan_stats: bool = True, name: Incomplete | None = None):
    '''Get the KL-divergence KL(distribution_a || distribution_b).

  If there is no KL method registered specifically for `type(distribution_a)`
  and `type(distribution_b)`, then the class hierarchies of these types are
  searched.

  If one KL method is registered between any pairs of classes in these two
  parent hierarchies, it is used.

  If more than one such registered method exists, the method whose registered
  classes have the shortest sum MRO paths to the input types is used.

  If more than one such shortest path exists, the first method
  identified in the search is used (favoring a shorter MRO distance to
  `type(distribution_a)`).

  Args:
    distribution_a: The first distribution.
    distribution_b: The second distribution.
    allow_nan_stats: Python `bool`, default `True`. When `True`,
      statistics (e.g., mean, mode, variance) use the value "`NaN`" to
      indicate the result is undefined. When `False`, an exception is raised
      if one or more of the statistic\'s batch members are undefined.
    name: Python `str` name prefixed to Ops created by this class.

  Returns:
    A Tensor with the batchwise KL-divergence between `distribution_a`
    and `distribution_b`.

  Raises:
    NotImplementedError: If no KL method is defined for distribution types
      of `distribution_a` and `distribution_b`.
  '''

class RegisterKL:
    """Decorator to register a KL divergence implementation function.

  Usage:

  @distributions.RegisterKL(distributions.Normal, distributions.Normal)
  def _kl_normal_mvn(norm_a, norm_b):
    # Return KL(norm_a || norm_b)
  """
    def __init__(self, dist_cls_a, dist_cls_b) -> None:
        """Initialize the KL registrar.

    Args:
      dist_cls_a: the class of the first argument of the KL divergence.
      dist_cls_b: the class of the second argument of the KL divergence.
    """
    def __call__(self, kl_fn):
        """Perform the KL registration.

    Args:
      kl_fn: The function to use for the KL divergence.

    Returns:
      kl_fn

    Raises:
      TypeError: if kl_fn is not a callable.
      ValueError: if a KL divergence function has already been registered for
        the given argument classes.
    """
