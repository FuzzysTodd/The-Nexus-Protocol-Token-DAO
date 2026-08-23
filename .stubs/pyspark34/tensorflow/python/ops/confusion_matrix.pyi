from _typeshed import Incomplete
from tensorflow.python.framework import dtypes as dtypes, ops as ops
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export

def remove_squeezable_dimensions(labels, predictions, expected_rank_diff: int = 0, name: Incomplete | None = None):
    """Squeeze last dim if ranks differ from expected by exactly 1.

  In the common case where we expect shapes to match, `expected_rank_diff`
  defaults to 0, and we squeeze the last dimension of the larger rank if they
  differ by 1.

  But, for example, if `labels` contains class IDs and `predictions` contains 1
  probability per class, we expect `predictions` to have 1 more dimension than
  `labels`, so `expected_rank_diff` would be 1. In this case, we'd squeeze
  `labels` if `rank(predictions) - rank(labels) == 0`, and
  `predictions` if `rank(predictions) - rank(labels) == 2`.

  This will use static shape if available. Otherwise, it will add graph
  operations, which could result in a performance hit.

  Args:
    labels: Label values, a `Tensor` whose dimensions match `predictions`.
    predictions: Predicted values, a `Tensor` of arbitrary dimensions.
    expected_rank_diff: Expected result of `rank(predictions) - rank(labels)`.
    name: Name of the op.

  Returns:
    Tuple of `labels` and `predictions`, possibly with last dim squeezed.
  """
def confusion_matrix(labels, predictions, num_classes: Incomplete | None = None, weights: Incomplete | None = None, dtype=..., name: Incomplete | None = None):
    """Computes the confusion matrix from predictions and labels.

  The matrix columns represent the prediction labels and the rows represent the
  real labels. The confusion matrix is always a 2-D array of shape `[n, n]`,
  where `n` is the number of valid labels for a given classification task. Both
  prediction and labels must be 1-D arrays of the same shape in order for this
  function to work.

  If `num_classes` is `None`, then `num_classes` will be set to one plus the
  maximum value in either predictions or labels. Class labels are expected to
  start at 0. For example, if `num_classes` is 3, then the possible labels
  would be `[0, 1, 2]`.

  If `weights` is not `None`, then each prediction contributes its
  corresponding weight to the total value of the confusion matrix cell.

  For example:

  ```python
    tf.math.confusion_matrix([1, 2, 4], [2, 2, 4]) ==>
        [[0 0 0 0 0]
         [0 0 1 0 0]
         [0 0 1 0 0]
         [0 0 0 0 0]
         [0 0 0 0 1]]
  ```

  Note that the possible labels are assumed to be `[0, 1, 2, 3, 4]`,
  resulting in a 5x5 confusion matrix.

  Args:
    labels: 1-D `Tensor` of real labels for the classification task.
    predictions: 1-D `Tensor` of predictions for a given classification.
    num_classes: The possible number of labels the classification task can
                 have. If this value is not provided, it will be calculated
                 using both predictions and labels array.
    weights: An optional `Tensor` whose shape matches `predictions`.
    dtype: Data type of the confusion matrix.
    name: Scope name.

  Returns:
    A `Tensor` of type `dtype` with shape `[n, n]` representing the confusion
    matrix, where `n` is the number of possible labels in the classification
    task.

  Raises:
    ValueError: If both predictions and labels are not 1-D vectors and have
      mismatched shapes, or if `weights` is not `None` and its shape doesn't
      match `predictions`.
  """
def confusion_matrix_v1(labels, predictions, num_classes: Incomplete | None = None, dtype=..., name: Incomplete | None = None, weights: Incomplete | None = None):
    """Computes the confusion matrix from predictions and labels.

  The matrix columns represent the prediction labels and the rows represent the
  real labels. The confusion matrix is always a 2-D array of shape `[n, n]`,
  where `n` is the number of valid labels for a given classification task. Both
  prediction and labels must be 1-D arrays of the same shape in order for this
  function to work.

  If `num_classes` is `None`, then `num_classes` will be set to one plus the
  maximum value in either predictions or labels. Class labels are expected to
  start at 0. For example, if `num_classes` is 3, then the possible labels
  would be `[0, 1, 2]`.

  If `weights` is not `None`, then each prediction contributes its
  corresponding weight to the total value of the confusion matrix cell.

  For example:

  ```python
    tf.math.confusion_matrix([1, 2, 4], [2, 2, 4]) ==>
        [[0 0 0 0 0]
         [0 0 1 0 0]
         [0 0 1 0 0]
         [0 0 0 0 0]
         [0 0 0 0 1]]
  ```

  Note that the possible labels are assumed to be `[0, 1, 2, 3, 4]`,
  resulting in a 5x5 confusion matrix.

  Args:
    labels: 1-D `Tensor` of real labels for the classification task.
    predictions: 1-D `Tensor` of predictions for a given classification.
    num_classes: The possible number of labels the classification task can have.
      If this value is not provided, it will be calculated using both
      predictions and labels array.
    dtype: Data type of the confusion matrix.
    name: Scope name.
    weights: An optional `Tensor` whose shape matches `predictions`.

  Returns:
    A `Tensor` of type `dtype` with shape `[n, n]` representing the confusion
    matrix, where `n` is the number of possible labels in the classification
    task.

  Raises:
    ValueError: If both predictions and labels are not 1-D vectors and have
      mismatched shapes, or if `weights` is not `None` and its shape doesn't
      match `predictions`.
  """
