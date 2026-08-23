from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_output as export_output
from tensorflow_estimator.python.estimator.head import base_head as base_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class BinaryClassHead(base_head.Head):
    '''Creates a `Head` for single label binary classification.

  Uses `sigmoid_cross_entropy_with_logits` loss.

  The head expects `logits` with shape `[D0, D1, ... DN, 1]`.
  In many applications, the shape is `[batch_size, 1]`.

  `labels` must be a dense `Tensor` with shape matching `logits`, namely
  `[D0, D1, ... DN, 1]`. If `label_vocabulary` given, `labels` must be a string
  `Tensor` with values from the vocabulary. If `label_vocabulary` is not given,
  `labels` must be float `Tensor` with values in the interval `[0, 1]`.

  If `weight_column` is specified, weights must be of shape
  `[D0, D1, ... DN]`, or `[D0, D1, ... DN, 1]`.

  The loss is the weighted sum over the input dimensions. Namely, if the input
  labels have shape `[batch_size, 1]`, the loss is the weighted sum over
  `batch_size`.

  Also supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
  `(labels, logits, features, loss_reduction)` as arguments and returns loss
  with shape `[D0, D1, ... DN, 1]`. `loss_fn` must support float `labels` with
  shape `[D0, D1, ... DN, 1]`. Namely, the head applies `label_vocabulary` to
  the input labels before passing them to `loss_fn`.

  Usage:

  >>> head = tf.estimator.BinaryClassHead()
  >>> logits = np.array(((45,), (-41,),), dtype=np.float32)
  >>> labels = np.array(((1,), (1,),), dtype=np.int32)
  >>> features = {\'x\': np.array(((42,),), dtype=np.float32)}
  >>> # expected_loss = sum(cross_entropy(labels, logits)) / batch_size
  >>> #               = sum(0, 41) / 2 = 41 / 2 = 20.50
  >>> loss = head.loss(labels, logits, features=features)
  >>> print(\'{:.2f}\'.format(loss.numpy()))
  20.50
  >>> eval_metrics = head.metrics()
  >>> updated_metrics = head.update_metrics(
  ...   eval_metrics, features, logits, labels)
  >>> for k in sorted(updated_metrics):
  ...  print(\'{} : {:.2f}\'.format(k, updated_metrics[k].result().numpy()))
    accuracy : 0.50
    accuracy_baseline : 1.00
    auc : 0.00
    auc_precision_recall : 1.00
    average_loss : 20.50
    label/mean : 1.00
    precision : 1.00
    prediction/mean : 0.50
    recall : 0.50
  >>> preds = head.predictions(logits)
  >>> print(preds[\'logits\'])
  tf.Tensor(
    [[ 45.]
     [-41.]], shape=(2, 1), dtype=float32)

  Usage with a canned estimator:

  ```python
  my_head = tf.estimator.BinaryClassHead()
  my_estimator = tf.estimator.DNNEstimator(
      head=my_head,
      hidden_units=...,
      feature_columns=...)
  ```

  It can also be used with a custom `model_fn`. Example:

  ```python
  def _my_model_fn(features, labels, mode):
    my_head = tf.estimator.BinaryClassHead()
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
    weight_column: A string or a `NumericColumn` created by
      `tf.feature_column.numeric_column` defining feature column representing
      weights. It is used to down weight or boost examples during training. It
      will be multiplied by the loss of the example.
    thresholds: Iterable of floats in the range `(0, 1)`. For binary
      classification metrics such as precision and recall, an eval metric is
      generated for each threshold value. This threshold is applied to the
      logistic values to determine the binary classification (i.e., above the
      threshold is `true`, below is `false`.
    label_vocabulary: A list or tuple of strings representing possible label
      values. If it is not given, that means labels are already encoded within
      [0, 1]. If given, labels must be string type and have any value in
      `label_vocabulary`. Note that errors will be raised if `label_vocabulary`
      is not provided but labels are strings.
    loss_reduction: One of `tf.losses.Reduction` except `NONE`. Decides how to
      reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`, namely
      weighted sum of losses divided by `batch size * label_dimension`.
    loss_fn: Optional loss function.
    name: Name of the head. If provided, summary and metrics keys will be
      suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
  '''
    def __init__(self, weight_column: Incomplete | None = None, thresholds: Incomplete | None = None, label_vocabulary: Incomplete | None = None, loss_reduction=..., loss_fn: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
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
      keys: a list or tuple of prediction keys. Each key can be either the class
        variable of prediction_keys.PredictionKeys or its string value, such as:
          prediction_keys.PredictionKeys.CLASSES or 'classes'. If not specified,
          it will return the predictions for all valid keys.

    Returns:
      A dict of predictions.
    """
    def metrics(self, regularization_losses: Incomplete | None = None):
        """Creates metrics. See `base_head.Head` for details."""
    def update_metrics(self, eval_metrics, features, logits, labels, regularization_losses: Incomplete | None = None):
        """Updates eval metrics. See `base_head.Head` for details."""
