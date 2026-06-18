from tensorflow.python.ops.gen_clustering_ops import *
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_clustering_ops as gen_clustering_ops, math_ops as math_ops, nn_impl as nn_impl, random_ops as random_ops, state_ops as state_ops, variable_scope as variable_scope
from tensorflow.python.ops.embedding_ops import embedding_lookup as embedding_lookup

SQUARED_EUCLIDEAN_DISTANCE: str
COSINE_DISTANCE: str
RANDOM_INIT: str
KMEANS_PLUS_PLUS_INIT: str
KMC2_INIT: str
CLUSTERS_VAR_NAME: str

class KMeans:
    """Creates the graph for k-means clustering."""
    def __init__(self, inputs, num_clusters, initial_clusters=..., distance_metric=..., use_mini_batch: bool = False, mini_batch_steps_per_iteration: int = 1, random_seed: int = 0, kmeans_plus_plus_num_retries: int = 2, kmc2_chain_length: int = 200) -> None:
        '''Creates an object for generating KMeans clustering graph.

    This class implements the following variants of K-means algorithm:

    If use_mini_batch is False, it runs standard full batch K-means. Each step
    runs a single iteration of K-Means. This step can be run sharded across
    multiple workers by passing a list of sharded inputs to this class. Note
    however that a single step needs to process the full input at once.

    If use_mini_batch is True, it runs a generalization of the mini-batch
    K-means algorithm. It runs multiple iterations, where each iteration is
    composed of mini_batch_steps_per_iteration steps. Two copies of cluster
    centers are maintained: one that is updated at the end of each iteration,
    and one that is updated every step. The first copy is used to compute
    cluster allocations for each step, and for inference, while the second copy
    is the one updated each step using the mini-batch update rule. After each
    iteration is complete, this second copy is copied back the first copy.

    Note that for use_mini_batch=True, when mini_batch_steps_per_iteration=1,
    the algorithm reduces to the standard mini-batch algorithm. Also by setting
    mini_batch_steps_per_iteration = num_inputs / batch_size, the algorithm
    becomes an asynchronous version of the full-batch algorithm. Note however
    that there is no guarantee by this implementation that each input is seen
    exactly once per iteration. Also, different updates are applied
    asynchronously without locking. So this asynchronous version may not behave
    exactly like a full-batch version.

    Args:
      inputs: An input tensor or list of input tensors. It is assumed that the
        data points have been previously randomly permuted.
      num_clusters: An integer tensor specifying the number of clusters. This
        argument is ignored if initial_clusters is a tensor or numpy array.
      initial_clusters: Specifies the clusters used during initialization. One
        of the following: - a tensor or numpy array with the initial cluster
          centers. - a function f(inputs, k) that returns up to k centers from
          `inputs`.
        - "random": Choose centers randomly from `inputs`.
        - "kmeans_plus_plus": Use kmeans++ to choose centers from `inputs`.
        - "kmc2": Use the fast k-MC2 algorithm to choose centers from `inputs`.
          In the last three cases, one batch of `inputs` may not yield
          `num_clusters` centers, in which case initialization will require
          multiple batches until enough centers are chosen. In the case of
          "random" or "kmeans_plus_plus", if the input size is <= `num_clusters`
          then the entire batch is chosen to be cluster centers.
      distance_metric: Distance metric used for clustering. Supported options:
        "squared_euclidean", "cosine".
      use_mini_batch: If true, use the mini-batch k-means algorithm. Else assume
        full batch.
      mini_batch_steps_per_iteration: Number of steps after which the updated
        cluster centers are synced back to a master copy.
      random_seed: Seed for PRNG used to initialize seeds.
      kmeans_plus_plus_num_retries: For each point that is sampled during
        kmeans++ initialization, this parameter specifies the number of
        additional points to draw from the current distribution before selecting
        the best. If a negative value is specified, a heuristic is used to
        sample O(log(num_to_sample)) additional points.
      kmc2_chain_length: Determines how many candidate points are used by the
        k-MC2 algorithm to produce one new cluster centers. If a (mini-)batch
        contains less points, one new cluster center is generated from the
        (mini-)batch.

    Raises:
      ValueError: An invalid argument was passed to initial_clusters or
        distance_metric.
    '''
    def training_graph(self):
        """Generate a training graph for kmeans algorithm.

    This returns, among other things, an op that chooses initial centers
    (init_op), a boolean variable that is set to True when the initial centers
    are chosen (cluster_centers_initialized), and an op to perform either an
    entire Lloyd iteration or a mini-batch of a Lloyd iteration (training_op).
    The caller should use these components as follows. A single worker should
    execute init_op multiple times until cluster_centers_initialized becomes
    True. Then multiple workers may execute training_op any number of times.

    Returns:
      A tuple consisting of:
      all_scores: A matrix (or list of matrices) of dimensions (num_input,
        num_clusters) where the value is the distance of an input vector and a
        cluster center.
      cluster_idx: A vector (or list of vectors). Each element in the vector
        corresponds to an input row in 'inp' and specifies the cluster id
        corresponding to the input.
      scores: Similar to cluster_idx but specifies the distance to the
        assigned cluster instead.
      cluster_centers_initialized: scalar indicating whether clusters have been
        initialized.
      init_op: an op to initialize the clusters.
      training_op: an op that runs an iteration of training.
    """

class _InitializeClustersOpFactory:
    """Internal class to create the op to initialize the clusters.

    The op performs this algorithm (see constructor args):

    num_remaining = num_clusters - length(cluster_centers)
    if num_remaining == 0:
      assert that cluster_centers_initialized is true
    else:
      assert that num_remaining > 0
      new_centers = choose up to num_remaining initial centers
      l2-normalize new_centers if using cosine distance
      all_centers = concat(cluster_centers, new_centers)
      cluster_centers := all_centers
      if there is a cluster_centers_updated variable:
        cluster_centers_updated := cluster_centers
      num_now_remaining = num_clusters - length(cluster_centers)
      if num_now_remaining == 0:
        cluster_centers_initialized := true
  """
    def __init__(self, inputs, num_clusters, initial_clusters, distance_metric, random_seed, kmeans_plus_plus_num_retries, kmc2_chain_length, cluster_centers, cluster_centers_updated, cluster_centers_initialized) -> None:
        """Creates an op factory.

    Args:
      inputs: See KMeans constructor.
      num_clusters: An integer Tensor providing the number of clusters.
      initial_clusters: See KMeans constructor.
      distance_metric: See KMeans constructor.
      random_seed: See KMeans constructor.
      kmeans_plus_plus_num_retries: See KMeans constructor.
      kmc2_chain_length: See KMeans constructor.
      cluster_centers: The TF variable holding the initial centers. It may
        already contain some centers when the op is executed.
      cluster_centers_updated: A second TF variable to hold a copy of the
        initial centers, used for full-batch mode. In mini-batch mode,
        cluster_centers_updated is the same variable as cluster_centers.
      cluster_centers_initialized: A boolean TF variable that will be set to
        true when all the initial centers have been chosen.
    """
    def op(self):
        """Returns the cluster initializer op."""
