from _typeshed import Incomplete
from dataclasses import dataclass
from jax import jit as jit, lax as lax, random as random, vmap as vmap
from jax._src.numpy.util import check_arraylike as check_arraylike, promote_dtypes_inexact as promote_dtypes_inexact
from jax._src.tree_util import register_pytree_node_class as register_pytree_node_class
from jax.scipy import linalg as linalg, special as special
from typing import Any

@dataclass(frozen=True, init=False)
class gaussian_kde:
    neff: Any
    dataset: Any
    weights: Any
    covariance: Any
    inv_cov: Any
    def __init__(self, dataset, bw_method: Incomplete | None = None, weights: Incomplete | None = None) -> None: ...
    def tree_flatten(self): ...
    @classmethod
    def tree_unflatten(cls, aux_data, children): ...
    @property
    def d(self): ...
    @property
    def n(self): ...
    def evaluate(self, points): ...
    def __call__(self, points): ...
    def integrate_gaussian(self, mean, cov): ...
    def integrate_box_1d(self, low, high): ...
    def integrate_kde(self, other): ...
    def resample(self, key, shape=()):
        """Randomly sample a dataset from the estimated pdf

    Args:
      key: a PRNG key used as the random key.
      shape: optional, a tuple of nonnegative integers specifying the result
        batch shape; that is, the prefix of the result shape excluding the last
        axis.

    Returns:
      The resampled dataset as an array with shape `(d,) + shape`.
    """
    def pdf(self, x): ...
    def logpdf(self, x): ...
    def integrate_box(self, low_bounds, high_bounds, maxpts: Incomplete | None = None) -> None:
        """This method is not implemented in the JAX interface."""
    def set_bandwidth(self, bw_method: Incomplete | None = None) -> None:
        """This method is not implemented in the JAX interface."""
