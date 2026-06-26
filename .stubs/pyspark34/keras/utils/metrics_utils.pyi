from _typeshed import Incomplete
from enum import Enum
from keras import backend as backend
from keras.utils import losses_utils as losses_utils, tf_utils as tf_utils
from keras.utils.generic_utils import to_list as to_list

NEG_INF: float

class Reduction(Enum):
    """Types of metrics reduction.

    Contains the following values:

    * `SUM`: Scalar sum of weighted values.
    * `SUM_OVER_BATCH_SIZE`: Scalar sum of weighted values divided by
          number of elements.
    * `WEIGHTED_MEAN`: Scalar sum of weighted values divided by sum of weights.
    """
    SUM: str
    SUM_OVER_BATCH_SIZE: str
    WEIGHTED_MEAN: str

def update_state_wrapper(update_state_fn):
    """Decorator to wrap metric `update_state()` with `add_update()`.

    Args:
      update_state_fn: function that accumulates metric statistics.

    Returns:
      Decorated function that wraps `update_state_fn()` with `add_update()`.
    """
def result_wrapper(result_fn):
    """Decorator to wrap metric `result()` function in `merge_call()`.

    Result computation is an idempotent operation that simply calculates the
    metric value using the state variables.

    If metric state variables are distributed across replicas/devices and
    `result()` is requested from the context of one device - This function wraps
    `result()` in a distribution strategy `merge_call()`. With this,
    the metric state variables will be aggregated across devices.

    Args:
      result_fn: function that computes the metric result.

    Returns:
      Decorated function that wraps `result_fn()` in distribution strategy
      `merge_call()`.
    """
def weakmethod(method):
    """Creates a weak reference to the bound method."""
def assert_thresholds_range(thresholds) -> None: ...
def parse_init_thresholds(thresholds, default_threshold: float = 0.5): ...

class ConfusionMatrix(Enum):
    TRUE_POSITIVES: str
    FALSE_POSITIVES: str
    TRUE_NEGATIVES: str
    FALSE_NEGATIVES: str

class AUCCurve(Enum):
    """Type of AUC Curve (ROC or PR)."""
    ROC: str
    PR: str
    @staticmethod
    def from_str(key): ...

class AUCSummationMethod(Enum):
    """Type of AUC summation method.

    https://en.wikipedia.org/wiki/Riemann_sum)

    Contains the following values:
    * 'interpolation': Applies mid-point summation scheme for `ROC` curve. For
      `PR` curve, interpolates (true/false) positives but not the ratio that is
      precision (see Davis & Goadrich 2006 for details).
    * 'minoring': Applies left summation for increasing intervals and right
      summation for decreasing intervals.
    * 'majoring': Applies right summation for increasing intervals and left
      summation for decreasing intervals.
    """
    INTERPOLATION: str
    MAJORING: str
    MINORING: str
    @staticmethod
    def from_str(key): ...

def is_evenly_distributed_thresholds(thresholds):
    """Check if the thresholds list is evenly distributed.

    We could leverage evenly distributed thresholds to use less memory when
    calculate metrcis like AUC where each individual threshold need to be
    evaluated.

    Args:
      thresholds: A python list or tuple, or 1D numpy array whose value is
        ranged in [0, 1].

    Returns:
      boolean, whether the values in the inputs are evenly distributed.
    """
def update_confusion_matrix_variables(variables_to_update, y_true, y_pred, thresholds, top_k: Incomplete | None = None, class_id: Incomplete | None = None, sample_weight: Incomplete | None = None, multi_label: bool = False, label_weights: Incomplete | None = None, thresholds_distributed_evenly: bool = False):
    """Returns op to update the given confusion matrix variables.

    For every pair of values in y_true and y_pred:

    true_positive: y_true == True and y_pred > thresholds
    false_negatives: y_true == True and y_pred <= thresholds
    true_negatives: y_true == False and y_pred <= thresholds
    false_positive: y_true == False and y_pred > thresholds

    The results will be weighted and added together. When multiple thresholds
    are provided, we will repeat the same for every threshold.

    For estimation of these metrics over a stream of data, the function creates
    an `update_op` operation that updates the given variables.

    If `sample_weight` is `None`, weights default to 1.
    Use weights of 0 to mask values.

    Args:
      variables_to_update: Dictionary with 'tp', 'fn', 'tn', 'fp' as valid keys
        and corresponding variables to update as values.
      y_true: A `Tensor` whose shape matches `y_pred`. Will be cast to `bool`.
      y_pred: A floating point `Tensor` of arbitrary shape and whose values are
        in the range `[0, 1]`.
      thresholds: A float value, float tensor, python list, or tuple of float
        thresholds in `[0, 1]`, or NEG_INF (used when top_k is set).
      top_k: Optional int, indicates that the positive labels should be limited
        to the top k predictions.
      class_id: Optional int, limits the prediction and labels to the class
        specified by this argument.
      sample_weight: Optional `Tensor` whose rank is either 0, or the same rank
        as `y_true`, and must be broadcastable to `y_true` (i.e., all dimensions
        must be either `1`, or the same as the corresponding `y_true`
        dimension).
      multi_label: Optional boolean indicating whether multidimensional
        prediction/labels should be treated as multilabel responses, or
        flattened into a single label. When True, the valus of
        `variables_to_update` must have a second dimension equal to the number
        of labels in y_true and y_pred, and those tensors must not be
        RaggedTensors.
      label_weights: (optional) tensor of non-negative weights for multilabel
        data. The weights are applied when calculating TP, FP, FN, and TN
        without explicit multilabel handling (i.e. when the data is to be
        flattened).
      thresholds_distributed_evenly: Boolean, whether the thresholds are evenly
        distributed within the list. An optimized method will be used if this is
        the case. See _update_confusion_matrix_variables_optimized() for more
        details.

    Returns:
      Update op.

    Raises:
      ValueError: If `y_pred` and `y_true` have mismatched shapes, or if
        `sample_weight` is not `None` and its shape doesn't match `y_pred`, or
        if `variables_to_update` contains invalid keys.
    """
def ragged_assert_compatible_and_get_flat_values(values, mask: Incomplete | None = None):
    """If ragged, it checks the compatibility and then returns the flat_values.

       Note: If two tensors are dense, it does not check their compatibility.
       Note: Although two ragged tensors with different ragged ranks could have
             identical overall rank and dimension sizes and hence be compatible,
             we do not support those cases.
    Args:
       values: A list of potentially ragged tensor of the same ragged_rank.
       mask: A potentially ragged tensor of the same ragged_rank as elements in
         Values.

    Returns:
       A tuple in which the first element is the list of tensors and the second
       is the mask tensor. ([Values], mask). Mask and the element in Values
       are equal to the flat_values of the input arguments (if they were
       ragged).
    """
def binary_matches(y_true, y_pred, threshold: float = 0.5):
    """Creates int Tensor, 1 for label-prediction match, 0 for mismatch.

    Args:
      y_true: Ground truth values, of shape (batch_size, d0, .. dN).
      y_pred: The predicted values, of shape (batch_size, d0, .. dN).
      threshold: (Optional) Float representing the threshold for deciding
        whether prediction values are 1 or 0.

    Returns:
      Binary matches, of shape (batch_size, d0, .. dN).
    """
def sparse_categorical_matches(y_true, y_pred):
    """Creates float Tensor, 1.0 for label-prediction match, 0.0 for mismatch.

    You can provide logits of classes as `y_pred`, since argmax of
    logits and probabilities are same.

    Args:
      y_true: Integer ground truth values.
      y_pred: The prediction values.

    Returns:
      Match tensor: 1.0 for label-prediction match, 0.0 for mismatch.
    """
def sparse_top_k_categorical_matches(y_true, y_pred, k: int = 5):
    """Creates float Tensor, 1.0 for label-TopK_prediction match, 0.0 for
    mismatch.

    Args:
      y_true: tensor of true targets.
      y_pred: tensor of predicted targets.
      k: (Optional) Number of top elements to look at for computing accuracy.
        Defaults to 5.

    Returns:
      Match tensor: 1.0 for label-prediction match, 0.0 for mismatch.
    """
