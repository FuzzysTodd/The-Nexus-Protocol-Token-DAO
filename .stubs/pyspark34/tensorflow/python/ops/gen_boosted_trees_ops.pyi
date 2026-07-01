from _typeshed import Incomplete
from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import NamedTuple

def boosted_trees_aggregate_stats(node_ids, gradients, hessians, feature, max_splits, num_buckets, name: Incomplete | None = None):
    """Aggregates the summary of accumulated stats for the batch.

  The summary stats contains gradients and hessians accumulated for each node, feature dimension id and bucket.

  Args:
    node_ids: A `Tensor` of type `int32`.
      int32; Rank 1 Tensor containing node ids for each example, shape [batch_size].
    gradients: A `Tensor` of type `float32`.
      float32; Rank 2 Tensor (shape=[batch_size, logits_dimension]) with gradients for each example.
    hessians: A `Tensor` of type `float32`.
      float32; Rank 2 Tensor (shape=[batch_size, hessian_dimension]) with hessians for each example.
    feature: A `Tensor` of type `int32`.
      int32; Rank 2 feature Tensors (shape=[batch_size, feature_dimension]).
    max_splits: An `int` that is `>= 1`.
      int; the maximum number of splits possible in the whole tree.
    num_buckets: An `int` that is `>= 1`.
      int; equals to the maximum possible value of bucketized feature.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

BoostedTreesAggregateStats: Incomplete

def boosted_trees_aggregate_stats_eager_fallback(node_ids, gradients, hessians, feature, max_splits, num_buckets, name, ctx): ...
def boosted_trees_bucketize(float_values, bucket_boundaries, name: Incomplete | None = None):
    """Bucketize each feature based on bucket boundaries.

  An op that returns a list of float tensors, where each tensor represents the
  bucketized values for a single feature.

  Args:
    float_values: A list of `Tensor` objects with type `float32`.
      float; List of Rank 1 Tensor each containing float values for a single feature.
    bucket_boundaries: A list with the same length as `float_values` of `Tensor` objects with type `float32`.
      float; List of Rank 1 Tensors each containing the bucket boundaries for a single
      feature.
    name: A name for the operation (optional).

  Returns:
    A list with the same length as `float_values` of `Tensor` objects with type `int32`.
  """

BoostedTreesBucketize: Incomplete

def boosted_trees_bucketize_eager_fallback(float_values, bucket_boundaries, name, ctx): ...

class _BoostedTreesCalculateBestFeatureSplitOutput(NamedTuple):
    node_ids: Incomplete
    gains: Incomplete
    feature_dimensions: Incomplete
    thresholds: Incomplete
    left_node_contribs: Incomplete
    right_node_contribs: Incomplete
    split_with_default_directions: Incomplete

def boosted_trees_calculate_best_feature_split(node_id_range, stats_summary, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type: str = 'inequality', name: Incomplete | None = None):
    '''Calculates gains for each feature and returns the best possible split information for the feature.

  The split information is the best threshold (bucket id), gains and left/right node contributions per node for each feature.

  It is possible that not all nodes can be split on each feature. Hence, the list of possible nodes can differ between the features. Therefore, we return `node_ids_list` for each feature, containing the list of nodes that this feature can be used to split.

  In this manner, the output is the best split per features and per node, so that it needs to be combined later to produce the best split for each node (among all possible features).

  The output shapes are compatible in a way that the first dimension of all tensors are the same and equal to the number of possible split nodes for each feature.

  Args:
    node_id_range: A `Tensor` of type `int32`.
      A Rank 1 tensor (shape=[2]) to specify the range [first, last) of node ids to process within `stats_summary_list`. The nodes are iterated between the two nodes specified by the tensor, as like `for node_id in range(node_id_range[0], node_id_range[1])` (Note that the last index node_id_range[1] is exclusive).
    stats_summary: A `Tensor` of type `float32`.
      A Rank 4 tensor (#shape=[max_splits, feature_dims, bucket, stats_dims]) for accumulated stats summary (gradient/hessian) per node, per dimension, per buckets for each feature.
      The first dimension of the tensor is the maximum number of splits, and thus not all elements of it will be used, but only the indexes specified by node_ids will be used.
    l1: A `Tensor` of type `float32`.
      l1 regularization factor on leaf weights, per instance based.
    l2: A `Tensor` of type `float32`.
      l2 regularization factor on leaf weights, per instance based.
    tree_complexity: A `Tensor` of type `float32`.
      adjustment to the gain, per leaf based.
    min_node_weight: A `Tensor` of type `float32`.
      minimum avg of hessians in a node before required for the node to be considered for splitting.
    logits_dimension: An `int` that is `>= 1`.
      The dimension of logit, i.e., number of classes.
    split_type: An optional `string` from: `"inequality", "equality"`. Defaults to `"inequality"`.
      A string indicating if this Op should perform inequality split or equality split.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (node_ids, gains, feature_dimensions, thresholds, left_node_contribs, right_node_contribs, split_with_default_directions).

    node_ids: A `Tensor` of type `int32`.
    gains: A `Tensor` of type `float32`.
    feature_dimensions: A `Tensor` of type `int32`.
    thresholds: A `Tensor` of type `int32`.
    left_node_contribs: A `Tensor` of type `float32`.
    right_node_contribs: A `Tensor` of type `float32`.
    split_with_default_directions: A `Tensor` of type `string`.
  '''

BoostedTreesCalculateBestFeatureSplit: Incomplete

def boosted_trees_calculate_best_feature_split_eager_fallback(node_id_range, stats_summary, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type, name, ctx): ...

class _BoostedTreesCalculateBestFeatureSplitV2Output(NamedTuple):
    node_ids: Incomplete
    gains: Incomplete
    feature_ids: Incomplete
    feature_dimensions: Incomplete
    thresholds: Incomplete
    left_node_contribs: Incomplete
    right_node_contribs: Incomplete
    split_with_default_directions: Incomplete

def boosted_trees_calculate_best_feature_split_v2(node_id_range, stats_summaries_list, split_types, candidate_feature_ids, l1, l2, tree_complexity, min_node_weight, logits_dimension, name: Incomplete | None = None):
    """Calculates gains for each feature and returns the best possible split information for each node. However, if no split is found, then no split information is returned for that node.

  The split information is the best threshold (bucket id), gains and left/right node contributions per node for each feature.

  It is possible that not all nodes can be split on each feature. Hence, the list of possible nodes can differ between the features. Therefore, we return `node_ids_list` for each feature, containing the list of nodes that this feature can be used to split.

  In this manner, the output is the best split per features and per node, so that it needs to be combined later to produce the best split for each node (among all possible features).

  The output shapes are compatible in a way that the first dimension of all tensors are the same and equal to the number of possible split nodes for each feature.

  Args:
    node_id_range: A `Tensor` of type `int32`.
      A Rank 1 tensor (shape=[2]) to specify the range [first, last) of node ids to process within `stats_summary_list`. The nodes are iterated between the two nodes specified by the tensor, as like `for node_id in range(node_id_range[0], node_id_range[1])` (Note that the last index node_id_range[1] is exclusive).
    stats_summaries_list: A list of at least 1 `Tensor` objects with type `float32`.
      A list of Rank 4 tensor (#shape=[max_splits, feature_dims, bucket, stats_dims]) for accumulated stats summary (gradient/hessian) per node, per dimension, per buckets for each feature.
      The first dimension of the tensor is the maximum number of splits, and thus not all elements of it will be used, but only the indexes specified by node_ids will be used.
    split_types: A `Tensor` of type `string`.
      A Rank 1 tensor indicating if this Op should perform inequality split or equality split per feature.
    candidate_feature_ids: A `Tensor` of type `int32`.
      Rank 1 tensor with ids for each feature. This is the real id of the feature.
    l1: A `Tensor` of type `float32`.
      l1 regularization factor on leaf weights, per instance based.
    l2: A `Tensor` of type `float32`.
      l2 regularization factor on leaf weights, per instance based.
    tree_complexity: A `Tensor` of type `float32`.
      adjustment to the gain, per leaf based.
    min_node_weight: A `Tensor` of type `float32`.
      minimum avg of hessians in a node before required for the node to be considered for splitting.
    logits_dimension: An `int` that is `>= 1`.
      The dimension of logit, i.e., number of classes.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (node_ids, gains, feature_ids, feature_dimensions, thresholds, left_node_contribs, right_node_contribs, split_with_default_directions).

    node_ids: A `Tensor` of type `int32`.
    gains: A `Tensor` of type `float32`.
    feature_ids: A `Tensor` of type `int32`.
    feature_dimensions: A `Tensor` of type `int32`.
    thresholds: A `Tensor` of type `int32`.
    left_node_contribs: A `Tensor` of type `float32`.
    right_node_contribs: A `Tensor` of type `float32`.
    split_with_default_directions: A `Tensor` of type `string`.
  """

BoostedTreesCalculateBestFeatureSplitV2: Incomplete

def boosted_trees_calculate_best_feature_split_v2_eager_fallback(node_id_range, stats_summaries_list, split_types, candidate_feature_ids, l1, l2, tree_complexity, min_node_weight, logits_dimension, name, ctx): ...

class _BoostedTreesCalculateBestGainsPerFeatureOutput(NamedTuple):
    node_ids_list: Incomplete
    gains_list: Incomplete
    thresholds_list: Incomplete
    left_node_contribs_list: Incomplete
    right_node_contribs_list: Incomplete

def boosted_trees_calculate_best_gains_per_feature(node_id_range, stats_summary_list, l1, l2, tree_complexity, min_node_weight, max_splits, name: Incomplete | None = None):
    """Calculates gains for each feature and returns the best possible split information for the feature.

  The split information is the best threshold (bucket id), gains and left/right node contributions per node for each feature.

  It is possible that not all nodes can be split on each feature. Hence, the list of possible nodes can differ between the features. Therefore, we return `node_ids_list` for each feature, containing the list of nodes that this feature can be used to split.

  In this manner, the output is the best split per features and per node, so that it needs to be combined later to produce the best split for each node (among all possible features).

  The length of output lists are all of the same length, `num_features`.
  The output shapes are compatible in a way that the first dimension of all tensors of all lists are the same and equal to the number of possible split nodes for each feature.

  Args:
    node_id_range: A `Tensor` of type `int32`.
      A Rank 1 tensor (shape=[2]) to specify the range [first, last) of node ids to process within `stats_summary_list`. The nodes are iterated between the two nodes specified by the tensor, as like `for node_id in range(node_id_range[0], node_id_range[1])` (Note that the last index node_id_range[1] is exclusive).
    stats_summary_list: A list of at least 1 `Tensor` objects with type `float32`.
      A list of Rank 3 tensor (#shape=[max_splits, bucket, 2]) for accumulated stats summary (gradient/hessian) per node per buckets for each feature. The first dimension of the tensor is the maximum number of splits, and thus not all elements of it will be used, but only the indexes specified by node_ids will be used.
    l1: A `Tensor` of type `float32`.
      l1 regularization factor on leaf weights, per instance based.
    l2: A `Tensor` of type `float32`.
      l2 regularization factor on leaf weights, per instance based.
    tree_complexity: A `Tensor` of type `float32`.
      adjustment to the gain, per leaf based.
    min_node_weight: A `Tensor` of type `float32`.
      minimum avg of hessians in a node before required for the node to be considered for splitting.
    max_splits: An `int` that is `>= 1`.
      the number of nodes that can be split in the whole tree. Used as a dimension of output tensors.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (node_ids_list, gains_list, thresholds_list, left_node_contribs_list, right_node_contribs_list).

    node_ids_list: A list with the same length as `stats_summary_list` of `Tensor` objects with type `int32`.
    gains_list: A list with the same length as `stats_summary_list` of `Tensor` objects with type `float32`.
    thresholds_list: A list with the same length as `stats_summary_list` of `Tensor` objects with type `int32`.
    left_node_contribs_list: A list with the same length as `stats_summary_list` of `Tensor` objects with type `float32`.
    right_node_contribs_list: A list with the same length as `stats_summary_list` of `Tensor` objects with type `float32`.
  """

BoostedTreesCalculateBestGainsPerFeature: Incomplete

def boosted_trees_calculate_best_gains_per_feature_eager_fallback(node_id_range, stats_summary_list, l1, l2, tree_complexity, min_node_weight, max_splits, name, ctx): ...
def boosted_trees_center_bias(tree_ensemble_handle, mean_gradients, mean_hessians, l1, l2, name: Incomplete | None = None):
    """Calculates the prior from the training data (the bias) and fills in the first node with the logits' prior. Returns a boolean indicating whether to continue centering.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the tree ensemble.
    mean_gradients: A `Tensor` of type `float32`.
      A tensor with shape=[logits_dimension] with mean of gradients for a first node.
    mean_hessians: A `Tensor` of type `float32`.
      A tensor with shape=[logits_dimension] mean of hessians for a first node.
    l1: A `Tensor` of type `float32`.
      l1 regularization factor on leaf weights, per instance based.
    l2: A `Tensor` of type `float32`.
      l2 regularization factor on leaf weights, per instance based.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

BoostedTreesCenterBias: Incomplete

def boosted_trees_center_bias_eager_fallback(tree_ensemble_handle, mean_gradients, mean_hessians, l1, l2, name, ctx): ...
def boosted_trees_create_ensemble(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name: Incomplete | None = None):
    """Creates a tree ensemble model and returns a handle to it.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the tree ensemble resource to be created.
    stamp_token: A `Tensor` of type `int64`.
      Token to use as the initial value of the resource stamp.
    tree_ensemble_serialized: A `Tensor` of type `string`.
      Serialized proto of the tree ensemble.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesCreateEnsemble: Incomplete

def boosted_trees_create_ensemble_eager_fallback(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name, ctx): ...
def boosted_trees_create_quantile_stream_resource(quantile_stream_resource_handle, epsilon, num_streams, max_elements: int = 1099511627776, name: Incomplete | None = None):
    """Create the Resource for Quantile Streams.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource; Handle to quantile stream resource.
    epsilon: A `Tensor` of type `float32`.
      float; The required approximation error of the stream resource.
    num_streams: A `Tensor` of type `int64`.
      int; The number of streams managed by the resource that shares the same epsilon.
    max_elements: An optional `int`. Defaults to `1099511627776`.
      int; The maximum number of data points that can be fed to the stream.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesCreateQuantileStreamResource: Incomplete

def boosted_trees_create_quantile_stream_resource_eager_fallback(quantile_stream_resource_handle, epsilon, num_streams, max_elements, name, ctx): ...
def boosted_trees_deserialize_ensemble(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name: Incomplete | None = None):
    """Deserializes a serialized tree ensemble config and replaces current tree

  ensemble.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the tree ensemble.
    stamp_token: A `Tensor` of type `int64`.
      Token to use as the new value of the resource stamp.
    tree_ensemble_serialized: A `Tensor` of type `string`.
      Serialized proto of the ensemble.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesDeserializeEnsemble: Incomplete

def boosted_trees_deserialize_ensemble_eager_fallback(tree_ensemble_handle, stamp_token, tree_ensemble_serialized, name, ctx): ...
def boosted_trees_ensemble_resource_handle_op(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a handle to a BoostedTreesEnsembleResource

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

BoostedTreesEnsembleResourceHandleOp: Incomplete

def boosted_trees_ensemble_resource_handle_op_eager_fallback(container, shared_name, name, ctx): ...
def boosted_trees_example_debug_outputs(tree_ensemble_handle, bucketized_features, logits_dimension, name: Incomplete | None = None):
    """Debugging/model interpretability outputs for each example.

  It traverses all the trees and computes debug metrics for individual examples,
  such as getting split feature ids and logits after each split along the decision
  path used to compute directional feature contributions.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
    bucketized_features: A list of at least 1 `Tensor` objects with type `int32`.
      A list of rank 1 Tensors containing bucket id for each
      feature.
    logits_dimension: An `int`.
      scalar, dimension of the logits, to be used for constructing the protos in
      examples_debug_outputs_serialized.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
  """

BoostedTreesExampleDebugOutputs: Incomplete

def boosted_trees_example_debug_outputs_eager_fallback(tree_ensemble_handle, bucketized_features, logits_dimension, name, ctx): ...
def boosted_trees_flush_quantile_summaries(quantile_stream_resource_handle, num_features, name: Incomplete | None = None):
    """Flush the quantile summaries from each quantile stream resource.

  An op that outputs a list of quantile summaries of a quantile stream resource.
  Each summary Tensor is rank 2, containing summaries (value, weight, min_rank,
  max_rank) for a single feature.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource handle referring to a QuantileStreamResource.
    num_features: An `int` that is `>= 0`.
    name: A name for the operation (optional).

  Returns:
    A list of `num_features` `Tensor` objects with type `float32`.
  """

BoostedTreesFlushQuantileSummaries: Incomplete

def boosted_trees_flush_quantile_summaries_eager_fallback(quantile_stream_resource_handle, num_features, name, ctx): ...

class _BoostedTreesGetEnsembleStatesOutput(NamedTuple):
    stamp_token: Incomplete
    num_trees: Incomplete
    num_finalized_trees: Incomplete
    num_attempted_layers: Incomplete
    last_layer_nodes_range: Incomplete

def boosted_trees_get_ensemble_states(tree_ensemble_handle, name: Incomplete | None = None):
    """Retrieves the tree ensemble resource stamp token, number of trees and growing statistics.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the tree ensemble.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (stamp_token, num_trees, num_finalized_trees, num_attempted_layers, last_layer_nodes_range).

    stamp_token: A `Tensor` of type `int64`.
    num_trees: A `Tensor` of type `int32`.
    num_finalized_trees: A `Tensor` of type `int32`.
    num_attempted_layers: A `Tensor` of type `int32`.
    last_layer_nodes_range: A `Tensor` of type `int32`.
  """

BoostedTreesGetEnsembleStates: Incomplete

def boosted_trees_get_ensemble_states_eager_fallback(tree_ensemble_handle, name, ctx): ...
def boosted_trees_make_quantile_summaries(float_values, example_weights, epsilon, name: Incomplete | None = None):
    """Makes the summary of quantiles for the batch.

  An op that takes a list of tensors (one tensor per feature) and outputs the
  quantile summaries for each tensor.

  Args:
    float_values: A list of `Tensor` objects with type `float32`.
      float; List of Rank 1 Tensors each containing values for a single feature.
    example_weights: A `Tensor` of type `float32`.
      float; Rank 1 Tensor with weights per instance.
    epsilon: A `Tensor` of type `float32`.
      float; The required maximum approximation error.
    name: A name for the operation (optional).

  Returns:
    A list with the same length as `float_values` of `Tensor` objects with type `float32`.
  """

BoostedTreesMakeQuantileSummaries: Incomplete

def boosted_trees_make_quantile_summaries_eager_fallback(float_values, example_weights, epsilon, name, ctx): ...
def boosted_trees_make_stats_summary(node_ids, gradients, hessians, bucketized_features_list, max_splits, num_buckets, name: Incomplete | None = None):
    """Makes the summary of accumulated stats for the batch.

  The summary stats contains gradients and hessians accumulated into the corresponding node and bucket for each example.

  Args:
    node_ids: A `Tensor` of type `int32`.
      int32 Rank 1 Tensor containing node ids, which each example falls into for the requested layer.
    gradients: A `Tensor` of type `float32`.
      float32; Rank 2 Tensor (shape=[#examples, 1]) for gradients.
    hessians: A `Tensor` of type `float32`.
      float32; Rank 2 Tensor (shape=[#examples, 1]) for hessians.
    bucketized_features_list: A list of at least 1 `Tensor` objects with type `int32`.
      int32 list of Rank 1 Tensors, each containing the bucketized feature (for each feature column).
    max_splits: An `int` that is `>= 1`.
      int; the maximum number of splits possible in the whole tree.
    num_buckets: An `int` that is `>= 1`.
      int; equals to the maximum possible value of bucketized feature.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

BoostedTreesMakeStatsSummary: Incomplete

def boosted_trees_make_stats_summary_eager_fallback(node_ids, gradients, hessians, bucketized_features_list, max_splits, num_buckets, name, ctx): ...
def boosted_trees_predict(tree_ensemble_handle, bucketized_features, logits_dimension, name: Incomplete | None = None):
    """Runs multiple additive regression ensemble predictors on input instances and

  computes the logits. It is designed to be used during prediction.
  It traverses all the trees and calculates the final score for each instance.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
    bucketized_features: A list of at least 1 `Tensor` objects with type `int32`.
      A list of rank 1 Tensors containing bucket id for each
      feature.
    logits_dimension: An `int`.
      scalar, dimension of the logits, to be used for partial logits
      shape.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
  """

BoostedTreesPredict: Incomplete

def boosted_trees_predict_eager_fallback(tree_ensemble_handle, bucketized_features, logits_dimension, name, ctx): ...
def boosted_trees_quantile_stream_resource_add_summaries(quantile_stream_resource_handle, summaries, name: Incomplete | None = None):
    """Add the quantile summaries to each quantile stream resource.

  An op that adds a list of quantile summaries to a quantile stream resource. Each
  summary Tensor is rank 2, containing summaries (value, weight, min_rank, max_rank)
  for a single feature.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource handle referring to a QuantileStreamResource.
    summaries: A list of `Tensor` objects with type `float32`.
      string; List of Rank 2 Tensor each containing the summaries for a single feature.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesQuantileStreamResourceAddSummaries: Incomplete

def boosted_trees_quantile_stream_resource_add_summaries_eager_fallback(quantile_stream_resource_handle, summaries, name, ctx): ...
def boosted_trees_quantile_stream_resource_deserialize(quantile_stream_resource_handle, bucket_boundaries, name: Incomplete | None = None):
    """Deserialize bucket boundaries and ready flag into current QuantileAccumulator.

  An op that deserializes bucket boundaries and are boundaries ready flag into current QuantileAccumulator.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource handle referring to a QuantileStreamResource.
    bucket_boundaries: A list of at least 1 `Tensor` objects with type `float32`.
      float; List of Rank 1 Tensors each containing the bucket boundaries for a feature.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesQuantileStreamResourceDeserialize: Incomplete

def boosted_trees_quantile_stream_resource_deserialize_eager_fallback(quantile_stream_resource_handle, bucket_boundaries, name, ctx): ...
def boosted_trees_quantile_stream_resource_flush(quantile_stream_resource_handle, num_buckets, generate_quantiles: bool = False, name: Incomplete | None = None):
    """Flush the summaries for a quantile stream resource.

  An op that flushes the summaries for a quantile stream resource.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource handle referring to a QuantileStreamResource.
    num_buckets: A `Tensor` of type `int64`.
      int; approximate number of buckets unless using generate_quantiles.
    generate_quantiles: An optional `bool`. Defaults to `False`.
      bool; If True, the output will be the num_quantiles for each stream where the ith
      entry is the ith quantile of the input with an approximation error of epsilon.
      Duplicate values may be present.
      If False, the output will be the points in the histogram that we got which roughly
      translates to 1/epsilon boundaries and without any duplicates.
      Default to False.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesQuantileStreamResourceFlush: Incomplete

def boosted_trees_quantile_stream_resource_flush_eager_fallback(quantile_stream_resource_handle, num_buckets, generate_quantiles, name, ctx): ...
def boosted_trees_quantile_stream_resource_get_bucket_boundaries(quantile_stream_resource_handle, num_features, name: Incomplete | None = None):
    """Generate the bucket boundaries for each feature based on accumulated summaries.

  An op that returns a list of float tensors for a quantile stream resource. Each
  tensor is Rank 1 containing bucket boundaries for a single feature.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource handle referring to a QuantileStreamResource.
    num_features: An `int` that is `>= 0`.
      inferred int; number of features to get bucket boundaries for.
    name: A name for the operation (optional).

  Returns:
    A list of `num_features` `Tensor` objects with type `float32`.
  """

BoostedTreesQuantileStreamResourceGetBucketBoundaries: Incomplete

def boosted_trees_quantile_stream_resource_get_bucket_boundaries_eager_fallback(quantile_stream_resource_handle, num_features, name, ctx): ...
def boosted_trees_quantile_stream_resource_handle_op(container: str = '', shared_name: str = '', name: Incomplete | None = None):
    '''Creates a handle to a BoostedTreesQuantileStreamResource.

  Args:
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `resource`.
  '''

BoostedTreesQuantileStreamResourceHandleOp: Incomplete

def boosted_trees_quantile_stream_resource_handle_op_eager_fallback(container, shared_name, name, ctx): ...

class _BoostedTreesSerializeEnsembleOutput(NamedTuple):
    stamp_token: Incomplete
    tree_ensemble_serialized: Incomplete

def boosted_trees_serialize_ensemble(tree_ensemble_handle, name: Incomplete | None = None):
    """Serializes the tree ensemble to a proto.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the tree ensemble.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (stamp_token, tree_ensemble_serialized).

    stamp_token: A `Tensor` of type `int64`.
    tree_ensemble_serialized: A `Tensor` of type `string`.
  """

BoostedTreesSerializeEnsemble: Incomplete

def boosted_trees_serialize_ensemble_eager_fallback(tree_ensemble_handle, name, ctx): ...

class _BoostedTreesSparseAggregateStatsOutput(NamedTuple):
    stats_summary_indices: Incomplete
    stats_summary_values: Incomplete
    stats_summary_shape: Incomplete

def boosted_trees_sparse_aggregate_stats(node_ids, gradients, hessians, feature_indices, feature_values, feature_shape, max_splits, num_buckets, name: Incomplete | None = None):
    """Aggregates the summary of accumulated stats for the batch.

  The summary stats contains gradients and hessians accumulated for each node, bucket and dimension id.

  Args:
    node_ids: A `Tensor` of type `int32`.
      int32; Rank 1 Tensor containing node ids for each example, shape [batch_size].
    gradients: A `Tensor` of type `float32`.
      float32; Rank 2 Tensor (shape=[batch_size, logits_dimension]) with gradients for each example.
    hessians: A `Tensor` of type `float32`.
      float32; Rank 2 Tensor (shape=[batch_size, hessian_dimension]) with hessians for each example.
    feature_indices: A `Tensor` of type `int32`.
      int32; Rank 2 indices of feature sparse Tensors (shape=[number of sparse entries, 2]).
      Number of sparse entries across all instances from the batch. The first value is
      the index of the instance, the second is dimension of the feature. The second axis
      can only have 2 values, i.e., the input dense version of Tensor can only be matrix.
    feature_values: A `Tensor` of type `int32`.
      int32; Rank 1 values of feature sparse Tensors (shape=[number of sparse entries]).
      Number of sparse entries across all instances from the batch. The first value is
      the index of the instance, the second is dimension of the feature.
    feature_shape: A `Tensor` of type `int32`.
      int32; Rank 1 dense shape of feature sparse Tensors (shape=[2]).
      The first axis can only have 2 values, [batch_size, feature_dimension].
    max_splits: An `int` that is `>= 1`.
      int; the maximum number of splits possible in the whole tree.
    num_buckets: An `int` that is `>= 1`.
      int; equals to the maximum possible value of bucketized feature + 1.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (stats_summary_indices, stats_summary_values, stats_summary_shape).

    stats_summary_indices: A `Tensor` of type `int32`.
    stats_summary_values: A `Tensor` of type `float32`.
    stats_summary_shape: A `Tensor` of type `int32`.
  """

BoostedTreesSparseAggregateStats: Incomplete

def boosted_trees_sparse_aggregate_stats_eager_fallback(node_ids, gradients, hessians, feature_indices, feature_values, feature_shape, max_splits, num_buckets, name, ctx): ...

class _BoostedTreesSparseCalculateBestFeatureSplitOutput(NamedTuple):
    node_ids: Incomplete
    gains: Incomplete
    feature_dimensions: Incomplete
    thresholds: Incomplete
    left_node_contribs: Incomplete
    right_node_contribs: Incomplete
    split_with_default_directions: Incomplete

def boosted_trees_sparse_calculate_best_feature_split(node_id_range, stats_summary_indices, stats_summary_values, stats_summary_shape, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type: str = 'inequality', name: Incomplete | None = None):
    '''Calculates gains for each feature and returns the best possible split information for the feature.

  The split information is the best threshold (bucket id), gains and left/right node contributions per node for each feature.

  It is possible that not all nodes can be split on each feature. Hence, the list of possible nodes can differ between the features. Therefore, we return `node_ids_list` for each feature, containing the list of nodes that this feature can be used to split.

  In this manner, the output is the best split per features and per node, so that it needs to be combined later to produce the best split for each node (among all possible features).

  The output shapes are compatible in a way that the first dimension of all tensors are the same and equal to the number of possible split nodes for each feature.

  Args:
    node_id_range: A `Tensor` of type `int32`.
      A Rank 1 tensor (shape=[2]) to specify the range [first, last) of node ids to process within `stats_summary_list`. The nodes are iterated between the two nodes specified by the tensor, as like `for node_id in range(node_id_range[0], node_id_range[1])` (Note that the last index node_id_range[1] is exclusive).
    stats_summary_indices: A `Tensor` of type `int32`.
      A Rank 2 int64 tensor of dense shape [N, 4] (N specifies the number of non-zero values) for accumulated stats summary (gradient/hessian) per node per bucket for each feature. The second dimension contains node id, feature dimension, bucket id, and stats dim.
      stats dim is the sum of logits dimension and hessian dimension, hessian dimension can either be logits dimension if diagonal hessian is used, or logits dimension^2 if full hessian is used.
    stats_summary_values: A `Tensor` of type `float32`.
      A Rank 1 float tensor of dense shape [N] (N specifies the number of non-zero values), which supplies the values for each element in summary_indices.
    stats_summary_shape: A `Tensor` of type `int32`.
      A Rank 1 float tensor of dense shape [4], which specifies the dense shape of the sparse tensor, which is [num tree nodes, feature dimensions, num buckets, stats dim].
    l1: A `Tensor` of type `float32`.
      l1 regularization factor on leaf weights, per instance based.
    l2: A `Tensor` of type `float32`.
      l2 regularization factor on leaf weights, per instance based.
    tree_complexity: A `Tensor` of type `float32`.
      adjustment to the gain, per leaf based.
    min_node_weight: A `Tensor` of type `float32`.
      minimum avg of hessians in a node before required for the node to be considered for splitting.
    logits_dimension: An `int` that is `>= 1`.
      The dimension of logit, i.e., number of classes.
    split_type: An optional `string` from: `"inequality"`. Defaults to `"inequality"`.
      A string indicating if this Op should perform inequality split or equality split.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (node_ids, gains, feature_dimensions, thresholds, left_node_contribs, right_node_contribs, split_with_default_directions).

    node_ids: A `Tensor` of type `int32`.
    gains: A `Tensor` of type `float32`.
    feature_dimensions: A `Tensor` of type `int32`.
    thresholds: A `Tensor` of type `int32`.
    left_node_contribs: A `Tensor` of type `float32`.
    right_node_contribs: A `Tensor` of type `float32`.
    split_with_default_directions: A `Tensor` of type `string`.
  '''

BoostedTreesSparseCalculateBestFeatureSplit: Incomplete

def boosted_trees_sparse_calculate_best_feature_split_eager_fallback(node_id_range, stats_summary_indices, stats_summary_values, stats_summary_shape, l1, l2, tree_complexity, min_node_weight, logits_dimension, split_type, name, ctx): ...

class _BoostedTreesTrainingPredictOutput(NamedTuple):
    partial_logits: Incomplete
    tree_ids: Incomplete
    node_ids: Incomplete

def boosted_trees_training_predict(tree_ensemble_handle, cached_tree_ids, cached_node_ids, bucketized_features, logits_dimension, name: Incomplete | None = None):
    """Runs multiple additive regression ensemble predictors on input instances and

  computes the update to cached logits. It is designed to be used during training.
  It traverses the trees starting from cached tree id and cached node id and
  calculates the updates to be pushed to the cache.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
    cached_tree_ids: A `Tensor` of type `int32`.
      Rank 1 Tensor containing cached tree ids which is the starting
      tree of prediction.
    cached_node_ids: A `Tensor` of type `int32`.
      Rank 1 Tensor containing cached node id which is the starting
      node of prediction.
    bucketized_features: A list of at least 1 `Tensor` objects with type `int32`.
      A list of rank 1 Tensors containing bucket id for each
      feature.
    logits_dimension: An `int`.
      scalar, dimension of the logits, to be used for partial logits
      shape.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (partial_logits, tree_ids, node_ids).

    partial_logits: A `Tensor` of type `float32`.
    tree_ids: A `Tensor` of type `int32`.
    node_ids: A `Tensor` of type `int32`.
  """

BoostedTreesTrainingPredict: Incomplete

def boosted_trees_training_predict_eager_fallback(tree_ensemble_handle, cached_tree_ids, cached_node_ids, bucketized_features, logits_dimension, name, ctx): ...
def boosted_trees_update_ensemble(tree_ensemble_handle, feature_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, max_depth, learning_rate, pruning_mode, name: Incomplete | None = None):
    """Updates the tree ensemble by either adding a layer to the last tree being grown

  or by starting a new tree.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the ensemble variable.
    feature_ids: A `Tensor` of type `int32`.
      Rank 1 tensor with ids for each feature. This is the real id of
      the feature that will be used in the split.
    node_ids: A list of `Tensor` objects with type `int32`.
      List of rank 1 tensors representing the nodes for which this feature
      has a split.
    gains: A list with the same length as `node_ids` of `Tensor` objects with type `float32`.
      List of rank 1 tensors representing the gains for each of the feature's
      split.
    thresholds: A list with the same length as `node_ids` of `Tensor` objects with type `int32`.
      List of rank 1 tensors representing the thesholds for each of the
      feature's split.
    left_node_contribs: A list with the same length as `node_ids` of `Tensor` objects with type `float32`.
      List of rank 2 tensors with left leaf contribs for each of
      the feature's splits. Will be added to the previous node values to constitute
      the values of the left nodes.
    right_node_contribs: A list with the same length as `node_ids` of `Tensor` objects with type `float32`.
      List of rank 2 tensors with right leaf contribs for each
      of the feature's splits. Will be added to the previous node values to constitute
      the values of the right nodes.
    max_depth: A `Tensor` of type `int32`. Max depth of the tree to build.
    learning_rate: A `Tensor` of type `float32`.
      shrinkage const for each new tree.
    pruning_mode: An `int` that is `>= 0`.
      0-No pruning, 1-Pre-pruning, 2-Post-pruning.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesUpdateEnsemble: Incomplete

def boosted_trees_update_ensemble_eager_fallback(tree_ensemble_handle, feature_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, max_depth, learning_rate, pruning_mode, name, ctx): ...
def boosted_trees_update_ensemble_v2(tree_ensemble_handle, feature_ids, dimension_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, split_types, max_depth, learning_rate, pruning_mode, logits_dimension: int = 1, name: Incomplete | None = None):
    """Updates the tree ensemble by adding a layer to the last tree being grown

  or by starting a new tree.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the ensemble variable.
    feature_ids: A list of at least 1 `Tensor` objects with type `int32`.
      Rank 1 tensor with ids for each feature. This is the real id of
      the feature that will be used in the split.
    dimension_ids: A list of `Tensor` objects with type `int32`.
      List of rank 1 tensors representing the dimension in each feature.
    node_ids: A list with the same length as `dimension_ids` of `Tensor` objects with type `int32`.
      List of rank 1 tensors representing the nodes for which this feature
      has a split.
    gains: A list with the same length as `dimension_ids` of `Tensor` objects with type `float32`.
      List of rank 1 tensors representing the gains for each of the feature's
      split.
    thresholds: A list with the same length as `dimension_ids` of `Tensor` objects with type `int32`.
      List of rank 1 tensors representing the thesholds for each of the
      feature's split.
    left_node_contribs: A list with the same length as `dimension_ids` of `Tensor` objects with type `float32`.
      List of rank 2 tensors with left leaf contribs for each of
      the feature's splits. Will be added to the previous node values to constitute
      the values of the left nodes.
    right_node_contribs: A list with the same length as `dimension_ids` of `Tensor` objects with type `float32`.
      List of rank 2 tensors with right leaf contribs for each
      of the feature's splits. Will be added to the previous node values to constitute
      the values of the right nodes.
    split_types: A list with the same length as `dimension_ids` of `Tensor` objects with type `string`.
      List of rank 1 tensors representing the split type for each feature.
    max_depth: A `Tensor` of type `int32`. Max depth of the tree to build.
    learning_rate: A `Tensor` of type `float32`.
      shrinkage const for each new tree.
    pruning_mode: A `Tensor` of type `int32`.
      0-No pruning, 1-Pre-pruning, 2-Post-pruning.
    logits_dimension: An optional `int`. Defaults to `1`.
      scalar, dimension of the logits
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """

BoostedTreesUpdateEnsembleV2: Incomplete

def boosted_trees_update_ensemble_v2_eager_fallback(tree_ensemble_handle, feature_ids, dimension_ids, node_ids, gains, thresholds, left_node_contribs, right_node_contribs, split_types, max_depth, learning_rate, pruning_mode, logits_dimension, name, ctx): ...
def is_boosted_trees_ensemble_initialized(tree_ensemble_handle, name: Incomplete | None = None):
    """Checks whether a tree ensemble has been initialized.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the tree ensemble resource.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsBoostedTreesEnsembleInitialized: Incomplete

def is_boosted_trees_ensemble_initialized_eager_fallback(tree_ensemble_handle, name, ctx): ...
def is_boosted_trees_quantile_stream_resource_initialized(quantile_stream_resource_handle, name: Incomplete | None = None):
    """Checks whether a quantile stream has been initialized.

  An Op that checks if quantile stream resource is initialized.

  Args:
    quantile_stream_resource_handle: A `Tensor` of type `resource`.
      resource; The reference to quantile stream resource handle.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """

IsBoostedTreesQuantileStreamResourceInitialized: Incomplete

def is_boosted_trees_quantile_stream_resource_initialized_eager_fallback(quantile_stream_resource_handle, name, ctx): ...
