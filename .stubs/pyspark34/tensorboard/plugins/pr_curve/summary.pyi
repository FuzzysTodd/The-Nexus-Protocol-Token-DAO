from _typeshed import Incomplete
from tensorboard.plugins.pr_curve import metadata as metadata

def op(name, labels, predictions, num_thresholds: Incomplete | None = None, weights: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None):
    """Create a PR curve summary op for a single binary classifier.

    Computes true/false positive/negative values for the given `predictions`
    against the ground truth `labels`, against a list of evenly distributed
    threshold values in `[0, 1]` of length `num_thresholds`.

    Each number in `predictions`, a float in `[0, 1]`, is compared with its
    corresponding boolean label in `labels`, and counts as a single tp/fp/tn/fn
    value at each threshold. This is then multiplied with `weights` which can be
    used to reweight certain values, or more commonly used for masking values.

    Args:
      name: A tag attached to the summary. Used by TensorBoard for organization.
      labels: The ground truth values. A Tensor of `bool` values with arbitrary
          shape.
      predictions: A float32 `Tensor` whose values are in the range `[0, 1]`.
          Dimensions must match those of `labels`.
      num_thresholds: Number of thresholds, evenly distributed in `[0, 1]`, to
          compute PR metrics for. Should be `>= 2`. This value should be a
          constant integer value, not a Tensor that stores an integer.
      weights: Optional float32 `Tensor`. Individual counts are multiplied by this
          value. This tensor must be either the same shape as or broadcastable to
          the `labels` tensor.
      display_name: Optional name for this summary in TensorBoard, as a
          constant `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
          constant `str`. Markdown is supported. Defaults to empty.
      collections: Optional list of graph collections keys. The new
          summary op is added to these collections. Defaults to
          `[Graph Keys.SUMMARIES]`.

    Returns:
      A summary operation for use in a TensorFlow graph. The float32 tensor
      produced by the summary operation is of dimension (6, num_thresholds). The
      first dimension (of length 6) is of the order: true positives,
      false positives, true negatives, false negatives, precision, recall.
    """
def pb(name, labels, predictions, num_thresholds: Incomplete | None = None, weights: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Create a PR curves summary protobuf.

    Arguments:
      name: A name for the generated node. Will also serve as a series name in
          TensorBoard.
      labels: The ground truth values. A bool numpy array.
      predictions: A float32 numpy array whose values are in the range `[0, 1]`.
          Dimensions must match those of `labels`.
      num_thresholds: Optional number of thresholds, evenly distributed in
          `[0, 1]`, to compute PR metrics for. When provided, should be an int of
          value at least 2. Defaults to 201.
      weights: Optional float or float32 numpy array. Individual counts are
          multiplied by this value. This tensor must be either the same shape as
          or broadcastable to the `labels` numpy array.
      display_name: Optional name for this summary in TensorBoard, as a `str`.
          Defaults to `name`.
      description: Optional long-form description for this summary, as a `str`.
          Markdown is supported. Defaults to empty.
    """
def streaming_op(name, labels, predictions, num_thresholds: Incomplete | None = None, weights: Incomplete | None = None, metrics_collections: Incomplete | None = None, updates_collections: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Computes a precision-recall curve summary across batches of data.

    This function is similar to op() above, but can be used to compute the PR
    curve across multiple batches of labels and predictions, in the same style
    as the metrics found in tf.metrics.

    This function creates multiple local variables for storing true positives,
    true negative, etc. accumulated over each batch of data, and uses these local
    variables for computing the final PR curve summary. These variables can be
    updated with the returned update_op.

    Args:
      name: A tag attached to the summary. Used by TensorBoard for organization.
      labels: The ground truth values, a `Tensor` whose dimensions must match
        `predictions`. Will be cast to `bool`.
      predictions: A floating point `Tensor` of arbitrary shape and whose values
        are in the range `[0, 1]`.
      num_thresholds: The number of evenly spaced thresholds to generate for
        computing the PR curve. Defaults to 201.
      weights: Optional `Tensor` whose rank is either 0, or the same rank as
        `labels`, and must be broadcastable to `labels` (i.e., all dimensions must
        be either `1`, or the same as the corresponding `labels` dimension).
      metrics_collections: An optional list of collections that `auc` should be
        added to.
      updates_collections: An optional list of collections that `update_op` should
        be added to.
      display_name: Optional name for this summary in TensorBoard, as a
          constant `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
          constant `str`. Markdown is supported. Defaults to empty.

    Returns:
      pr_curve: A string `Tensor` containing a single value: the
        serialized PR curve Tensor summary. The summary contains a
        float32 `Tensor` of dimension (6, num_thresholds). The first
        dimension (of length 6) is of the order: true positives, false
        positives, true negatives, false negatives, precision, recall.
      update_op: An operation that updates the summary with the latest data.
    """
def raw_data_op(name, true_positive_counts, false_positive_counts, true_negative_counts, false_negative_counts, precision, recall, num_thresholds: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None, collections: Incomplete | None = None):
    """Create an op that collects data for visualizing PR curves.

    Unlike the op above, this one avoids computing precision, recall, and the
    intermediate counts. Instead, it accepts those tensors as arguments and
    relies on the caller to ensure that the calculations are correct (and the
    counts yield the provided precision and recall values).

    This op is useful when a caller seeks to compute precision and recall
    differently but still use the PR curves plugin.

    Args:
      name: A tag attached to the summary. Used by TensorBoard for organization.
      true_positive_counts: A rank-1 tensor of true positive counts. Must contain
          `num_thresholds` elements and be castable to float32. Values correspond
          to thresholds that increase from left to right (from 0 to 1).
      false_positive_counts: A rank-1 tensor of false positive counts. Must
          contain `num_thresholds` elements and be castable to float32. Values
          correspond to thresholds that increase from left to right (from 0 to 1).
      true_negative_counts: A rank-1 tensor of true negative counts. Must contain
          `num_thresholds` elements and be castable to float32. Values
          correspond to thresholds that increase from left to right (from 0 to 1).
      false_negative_counts: A rank-1 tensor of false negative counts. Must
          contain `num_thresholds` elements and be castable to float32. Values
          correspond to thresholds that increase from left to right (from 0 to 1).
      precision: A rank-1 tensor of precision values. Must contain
          `num_thresholds` elements and be castable to float32. Values correspond
          to thresholds that increase from left to right (from 0 to 1).
      recall: A rank-1 tensor of recall values. Must contain `num_thresholds`
          elements and be castable to float32. Values correspond to thresholds
          that increase from left to right (from 0 to 1).
      num_thresholds: Number of thresholds, evenly distributed in `[0, 1]`, to
          compute PR metrics for. Should be `>= 2`. This value should be a
          constant integer value, not a Tensor that stores an integer.
      display_name: Optional name for this summary in TensorBoard, as a
          constant `str`. Defaults to `name`.
      description: Optional long-form description for this summary, as a
          constant `str`. Markdown is supported. Defaults to empty.
      collections: Optional list of graph collections keys. The new
          summary op is added to these collections. Defaults to
          `[Graph Keys.SUMMARIES]`.

    Returns:
      A summary operation for use in a TensorFlow graph. See docs for the `op`
      method for details on the float32 tensor produced by this summary.
    """
def raw_data_pb(name, true_positive_counts, false_positive_counts, true_negative_counts, false_negative_counts, precision, recall, num_thresholds: Incomplete | None = None, display_name: Incomplete | None = None, description: Incomplete | None = None):
    """Create a PR curves summary protobuf from raw data values.

    Args:
      name: A tag attached to the summary. Used by TensorBoard for organization.
      true_positive_counts: A rank-1 numpy array of true positive counts. Must
          contain `num_thresholds` elements and be castable to float32.
      false_positive_counts: A rank-1 numpy array of false positive counts. Must
          contain `num_thresholds` elements and be castable to float32.
      true_negative_counts: A rank-1 numpy array of true negative counts. Must
          contain `num_thresholds` elements and be castable to float32.
      false_negative_counts: A rank-1 numpy array of false negative counts. Must
          contain `num_thresholds` elements and be castable to float32.
      precision: A rank-1 numpy array of precision values. Must contain
          `num_thresholds` elements and be castable to float32.
      recall: A rank-1 numpy array of recall values. Must contain `num_thresholds`
          elements and be castable to float32.
      num_thresholds: Number of thresholds, evenly distributed in `[0, 1]`, to
          compute PR metrics for. Should be an int `>= 2`.
      display_name: Optional name for this summary in TensorBoard, as a `str`.
          Defaults to `name`.
      description: Optional long-form description for this summary, as a `str`.
          Markdown is supported. Defaults to empty.

    Returns:
      A summary operation for use in a TensorFlow graph. See docs for the `op`
      method for details on the float32 tensor produced by this summary.
    """
