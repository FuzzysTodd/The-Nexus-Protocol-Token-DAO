from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def kmc2_chain_initialization(distances, seed, name: Incomplete | None = None):
    """Returns the index of a data point that should be added to the seed set.

  Entries in distances are assumed to be squared distances of candidate points to
  the already sampled centers in the seed set. The op constructs one Markov chain
  of the k-MC^2 algorithm and returns the index of one candidate point to be added
  as an additional cluster center.

  Args:
    distances: A `Tensor` of type `float32`.
      Vector with squared distances to the closest previously sampled cluster center
      for each candidate point.
    seed: A `Tensor` of type `int64`.
      Scalar. Seed for initializing the random number generator.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `int64`.
  """

KMC2ChainInitialization: Incomplete

def kmc2_chain_initialization_eager_fallback(distances, seed, name, ctx): ...
def kmeans_plus_plus_initialization(points, num_to_sample, seed, num_retries_per_sample, name: Incomplete | None = None):
    """Selects num_to_sample rows of input using the KMeans++ criterion.

  Rows of points are assumed to be input points. One row is selected at random.
  Subsequent rows are sampled with probability proportional to the squared L2
  distance from the nearest row selected thus far till num_to_sample rows have
  been sampled.

  Args:
    points: A `Tensor` of type `float32`.
      Matrix of shape (n, d). Rows are assumed to be input points.
    num_to_sample: A `Tensor` of type `int64`.
      Scalar. The number of rows to sample. This value must not be larger than n.
    seed: A `Tensor` of type `int64`.
      Scalar. Seed for initializing the random number generator.
    num_retries_per_sample: A `Tensor` of type `int64`.
      Scalar. For each row that is sampled, this parameter
      specifies the number of additional points to draw from the current
      distribution before selecting the best. If a negative value is specified, a
      heuristic is used to sample O(log(num_to_sample)) additional points.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

KmeansPlusPlusInitialization: Incomplete

def kmeans_plus_plus_initialization_eager_fallback(points, num_to_sample, seed, num_retries_per_sample, name, ctx): ...

class _NearestNeighborsOutput(NamedTuple):
    nearest_center_indices: Incomplete
    nearest_center_distances: Incomplete

def nearest_neighbors(points, centers, k, name: Incomplete | None = None):
    """Selects the k nearest centers for each point.

  Rows of points are assumed to be input points. Rows of centers are assumed to be
  the list of candidate centers. For each point, the k centers that have least L2
  distance to it are computed.

  Args:
    points: A `Tensor` of type `float32`.
      Matrix of shape (n, d). Rows are assumed to be input points.
    centers: A `Tensor` of type `float32`.
      Matrix of shape (m, d). Rows are assumed to be centers.
    k: A `Tensor` of type `int64`.
      Number of nearest centers to return for each point. If k is larger than m, then
      only m centers are returned.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (nearest_center_indices, nearest_center_distances).

    nearest_center_indices: A `Tensor` of type `int64`.
    nearest_center_distances: A `Tensor` of type `float32`.
  """

NearestNeighbors: Incomplete

def nearest_neighbors_eager_fallback(points, centers, k, name, ctx): ...
