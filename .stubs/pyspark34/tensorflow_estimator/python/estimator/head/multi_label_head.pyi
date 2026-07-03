from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_output as export_output
from tensorflow_estimator.python.estimator.head import base_head as base_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class MultiLabelHead(base_head.Head):
    '''Creates a `Head` for multi-label classification.

  Multi-label classification handles the case where each example may have zero
  or more associated labels, from a discrete set. This is distinct from
  `MultiClassHead` which has exactly one label per example.

  Uses `sigmoid_cross_entropy` loss average over classes and weighted sum over
  the batch. Namely, if the input logits have shape `[batch_size, n_classes]`,
  the loss is the average over `n_classes` and the weighted sum over
  `batch_size`.

  The head expects `logits` with shape `[D0, D1, ... DN, n_classes]`. In many
  applications, the shape is `[batch_size, n_classes]`.

  Labels can be:

  * A multi-hot tensor of shape `[D0, D1, ... DN, n_classes]`
  * An integer `SparseTensor` of class indices. The `dense_shape` must be
    `[D0, D1, ... DN, ?]` and the values within `[0, n_classes)`.
  * If `label_vocabulary` is given, a string `SparseTensor`. The `dense_shape`
    must be `[D0, D1, ... DN, ?]` and the values within `label_vocabulary` or a
    multi-hot tensor of shape `[D0, D1, ... DN, n_classes]`.

  If `weight_column` is specified, weights must be of shape
  `[D0, D1, ... DN]`, or `[D0, D1, ... DN, 1]`.

  Also supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
  `(labels, logits, features)` as arguments and returns unreduced loss with
  shape `[D0, D1, ... DN, 1]`. `loss_fn` must support indicator `labels` with
  shape `[D0, D1, ... DN, n_classes]`. Namely, the head applies
  `label_vocabulary` to the input labels before passing them to `loss_fn`.

  Usage:

  >>> n_classes = 2
  >>> head = tf.estimator.MultiLabelHead(n_classes)
  >>> logits = np.array([[-1., 1.], [-1.5, 1.5]], dtype=np.float32)
  >>> labels = np.array([[1, 0], [1, 1]], dtype=np.int64)
  >>> features = {\'x\': np.array([[41], [42]], dtype=np.int32)}
  >>> # expected_loss = sum(_sigmoid_cross_entropy(labels, logits)) / batch_size
  >>> #               = sum(1.31326169, 0.9514133) / 2 = 1.13
  >>> loss = head.loss(labels, logits, features=features)
  >>> print(\'{:.2f}\'.format(loss.numpy()))
  1.13
  >>> eval_metrics = head.metrics()
  >>> updated_metrics = head.update_metrics(
  ...   eval_metrics, features, logits, labels)
  >>> for k in sorted(updated_metrics):
  ...  print(\'{} : {:.2f}\'.format(k, updated_metrics[k].result().numpy()))
  auc : 0.33
  auc_precision_recall : 0.77
  average_loss : 1.13
  >>> preds = head.predictions(logits)
  >>> print(preds[\'logits\'])
  tf.Tensor(
    [[-1.   1. ]
     [-1.5  1.5]], shape=(2, 2), dtype=float32)

  Usage with a canned estimator:

  ```python
  my_head = tf.estimator.MultiLabelHead(n_classes=3)
  my_estimator = tf.estimator.DNNEstimator(
      head=my_head,
      hidden_units=...,
      feature_columns=...)
  ```

  It can also be used with a custom `model_fn`. Example:

  ```python
  def _my_model_fn(features, labels, mode):
    my_head = tf.estimator.MultiLabelHead(n_classes=3)
    logits = tf.keras.Model(...)(features)

    return my_head.create_estimator_spec(
        features=features,
        mode=mode,
        labels=labels,
        optimizer=tf.keras.optimizers.Adagrad(lr=0.1),
        logits=logits)

  my_estimator = tf.estimator.Estimator(model_fn=_my_model_fn)
  ```

  Args:
    n_classes: Number of classes, must be greater than 1 (for 1 class, use
      `BinaryClassHead`).
    weight_column: A string or a `NumericColumn` created by
      `tf.feature_column.numeric_column` defining feature column representing
      weights. It is used to down weight or boost examples during training. It
      will be multiplied by the loss of the example.  Per-class weighting is not
      supported.
    thresholds: Iterable of floats in the range `(0, 1)`. Accuracy, precision
      and recall metrics are evaluated for each threshold value. The threshold
      is applied to the predicted probabilities, i.e. above the threshold is
      `true`, below is `false`.
    label_vocabulary: A list of strings represents possible label values. If it
      is not given, that means labels are already encoded as integer within [0,
      n_classes) or multi-hot Tensor. If given, labels must be SparseTensor
      `string` type and have any value in `label_vocabulary`. Also there will be
      errors if vocabulary is not provided and labels are string.
    loss_reduction: One of `tf.losses.Reduction` except `NONE`. Decides how to
      reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`, namely
      weighted sum of losses divided by batch size.
    loss_fn: Optional loss function.
    classes_for_class_based_metrics: List of integer class IDs or string class
      names for which per-class metrics are evaluated. If integers, all must be
      in the range `[0, n_classes - 1]`. If strings, all must be in
      `label_vocabulary`.
    name: Name of the head. If provided, summary and metrics keys will be
      suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
  '''
    def __init__(self, n_classes, weight_column: Incomplete | None = None, thresholds: Incomplete | None = None, label_vocabulary: Incomplete | None = None, loss_reduction=..., loss_fn: Incomplete | None = None, classes_for_class_based_metrics: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    @property
    def name(self):
        """See `base_head.Head` for details."""
    @property
    def logits_dimension(self):
        """See `base_head.Head` for details."""
    @property
    def loss_reduction(self):
        """See `base_head.Head` for details."""
    def loss(self, labels, logits, features: Incomplete | None = None, mode: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns regularized training loss. See `base_head.Head` for details."""
    def predictions(self, logits, keys: Incomplete | None = None):
        """Return predictions based on keys.

    See `base_head.Head` for details.

    Args:
      logits: logits `Tensor` with shape `[D0, D1, ... DN, logits_dimension]`.
        For many applications, the shape is `[batch_size, logits_dimension]`.
      keys: a list of prediction keys. Key can be either the class variable
        of prediction_keys.PredictionKeys or its string value, such as:
          prediction_keys.PredictionKeys.LOGITS or 'logits'.

    Returns:
      A dict of predictions.
    """
    def metrics(self, regularization_losses: Incomplete | None = None):
        """Creates metrics. See `base_head.Head` for details."""
    def update_metrics(self, eval_metrics, features, logits, labels, regularization_losses: Incomplete | None = None):
        """Updates eval metrics. See `base_head.Head` for details."""
