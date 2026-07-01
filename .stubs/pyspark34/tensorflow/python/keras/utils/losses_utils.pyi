from _typeshed import Incomplete
from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.framework import ops as ops
from tensorflow.python.keras import backend as backend
from tensorflow.python.keras.engine import keras_tensor as keras_tensor
from tensorflow.python.ops import array_ops as array_ops, control_flow_ops as control_flow_ops, math_ops as math_ops
from tensorflow.python.ops.ragged import ragged_tensor as ragged_tensor
from tensorflow.python.util.tf_export import keras_export as keras_export

class ReductionV2:
    """Types of loss reduction.

  Contains the following values:

  * `AUTO`: Indicates that the reduction option will be determined by the usage
     context. For almost all cases this defaults to `SUM_OVER_BATCH_SIZE`. When
     used with `tf.distribute.Strategy`, outside of built-in training loops such
     as `tf.keras` `compile` and `fit`, we expect reduction value to be
     `SUM` or `NONE`. Using `AUTO` in that case will raise an error.
  * `NONE`: No **additional** reduction is applied to the output of the wrapped
     loss function. When non-scalar losses are returned to Keras functions like
     `fit`/`evaluate`, the unreduced vector loss is passed to the optimizer
     but the reported loss will be a scalar value.

     Caution: **Verify the shape of the outputs when using** `Reduction.NONE`.
     The builtin loss functions wrapped by the loss classes reduce
     one dimension (`axis=-1`, or `axis` if specified by loss function).
     `Reduction.NONE` just means that no **additional** reduction is applied by
     the class wrapper. For categorical losses with an example input shape of
     `[batch, W, H, n_classes]` the `n_classes` dimension is reduced. For
     pointwise losses your must include a dummy axis so that `[batch, W, H, 1]`
     is reduced to `[batch, W, H]`. Without the dummy axis `[batch, W, H]`
     will be incorrectly reduced to `[batch, W]`.

  * `SUM`: Scalar sum of weighted losses.
  * `SUM_OVER_BATCH_SIZE`: Scalar `SUM` divided by number of elements in losses.
     This reduction type is not supported when used with
     `tf.distribute.Strategy` outside of built-in training loops like `tf.keras`
     `compile`/`fit`.

     You can implement 'SUM_OVER_BATCH_SIZE' using global batch size like:
     ```
     with strategy.scope():
       loss_obj = tf.keras.losses.CategoricalCrossentropy(
           reduction=tf.keras.losses.Reduction.NONE)
       ....
       loss = tf.reduce_sum(loss_obj(labels, predictions)) *
           (1. / global_batch_size)
     ```

  Please see the [custom training guide](
  https://www.tensorflow.org/tutorials/distribute/custom_training) for more
  details on this.
  """
    AUTO: str
    NONE: str
    SUM: str
    SUM_OVER_BATCH_SIZE: str
    @classmethod
    def all(cls): ...
    @classmethod
    def validate(cls, key) -> None: ...

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
def squeeze_or_expand_dimensions(y_pred, y_true: Incomplete | None = None, sample_weight: Incomplete | None = None):
    """Squeeze or expand last dimension if needed.

  1. Squeezes last dim of `y_pred` or `y_true` if their rank differs by 1
  (using `remove_squeezable_dimensions`).
  2. Squeezes or expands last dim of `sample_weight` if its rank differs by 1
  from the new rank of `y_pred`.
  If `sample_weight` is scalar, it is kept scalar.

  This will use static shape if available. Otherwise, it will add graph
  operations, which could result in a performance hit.

  Args:
    y_pred: Predicted values, a `Tensor` of arbitrary dimensions.
    y_true: Optional label `Tensor` whose dimensions match `y_pred`.
    sample_weight: Optional weight scalar or `Tensor` whose dimensions match
      `y_pred`.

  Returns:
    Tuple of `y_pred`, `y_true` and `sample_weight`. Each of them possibly has
    the last dimension squeezed,
    `sample_weight` could be extended by one dimension.
    If `sample_weight` is None, (y_pred, y_true) is returned.
  """
def reduce_weighted_loss(weighted_losses, reduction=...):
    """Reduces the individual weighted loss measurements."""
def compute_weighted_loss(losses, sample_weight: Incomplete | None = None, reduction=..., name: Incomplete | None = None):
    """Computes the weighted loss.

  Args:
    losses: `Tensor` of shape `[batch_size, d1, ... dN]`.
    sample_weight: Optional `Tensor` whose rank is either 0, or the same rank as
      `losses`, or be broadcastable to `losses`.
    reduction: (Optional) Type of `tf.keras.losses.Reduction` to apply to loss.
      Default value is `SUM_OVER_BATCH_SIZE`.
    name: Optional name for the op.

  Raises:
    ValueError: If the shape of `sample_weight` is not compatible with `losses`.

  Returns:
    Weighted loss `Tensor` of the same type as `losses`. If `reduction` is
    `NONE`, this has the same shape as `losses`; otherwise, it is scalar.
  """
def scale_loss_for_distribution(loss_value):
    """Scales and returns the given loss value by the number of replicas."""
def cast_losses_to_common_dtype(losses):
    """Cast a list of losses to a common dtype.

  If any loss is floating-point, they will all be casted to the most-precise
  floating-point loss. Otherwise the losses are not casted. We also skip casting
  losses if there are any complex losses.

  Args:
    losses: A list of losses.

  Returns:
    `losses`, but they have been casted to a common dtype.
  """
