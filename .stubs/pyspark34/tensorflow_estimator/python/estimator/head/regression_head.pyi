from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_output as export_output
from tensorflow_estimator.python.estimator.head import base_head as base_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class RegressionHead(base_head.Head):
    '''Creates a `Head` for regression using the `mean_squared_error` loss.

  The loss is the weighted sum over all input dimensions. Namely, if the input
  labels have shape `[batch_size, label_dimension]`, the loss is the weighted
  sum over both `batch_size` and `label_dimension`.

  The head expects `logits` with shape `[D0, D1, ... DN, label_dimension]`.
  In many applications, the shape is `[batch_size, label_dimension]`.

  The `labels` shape must match `logits`, namely
  `[D0, D1, ... DN, label_dimension]`. If `label_dimension=1`, shape
  `[D0, D1, ... DN]` is also supported.

  If `weight_column` is specified, weights must be of shape
  `[D0, D1, ... DN]`, `[D0, D1, ... DN, 1]` or
  `[D0, D1, ... DN, label_dimension]`.

  Supports custom `loss_fn`. `loss_fn` takes `(labels, logits)` or
  `(labels, logits, features, loss_reduction)` as arguments and returns
  unreduced loss with shape `[D0, D1, ... DN, label_dimension]`.

  Also supports custom `inverse_link_fn`, also known as \'mean function\'.
  `inverse_link_fn` is only used in `PREDICT` mode. It takes `logits` as
  argument and returns predicted values. This function is the inverse of the
  link function defined in
  https://en.wikipedia.org/wiki/Generalized_linear_model#Link_function
  Namely, for poisson regression, set `inverse_link_fn=tf.exp`.

  Usage:

  >>> head = tf.estimator.RegressionHead()
  >>> logits = np.array(((45,), (41,),), dtype=np.float32)
  >>> labels = np.array(((43,), (44,),), dtype=np.int32)
  >>> features = {\'x\': np.array(((42,),), dtype=np.float32)}
  >>> # expected_loss = weighted_loss / batch_size
  >>> #               = (43-45)^2 + (44-41)^2 / 2 = 6.50
  >>> loss = head.loss(labels, logits, features=features)
  >>> print(\'{:.2f}\'.format(loss.numpy()))
  6.50
  >>> eval_metrics = head.metrics()
  >>> updated_metrics = head.update_metrics(
  ...   eval_metrics, features, logits, labels)
  >>> for k in sorted(updated_metrics):
  ...  print(\'{} : {:.2f}\'.format(k, updated_metrics[k].result().numpy()))
    average_loss : 6.50
    label/mean : 43.50
    prediction/mean : 43.00
  >>> preds = head.predictions(logits)
  >>> print(preds[\'predictions\'])
  tf.Tensor(
    [[45.]
     [41.]], shape=(2, 1), dtype=float32)

  Usage with a canned estimator:

  ```python
  my_head = tf.estimator.RegressionHead()
  my_estimator = tf.estimator.DNNEstimator(
      head=my_head,
      hidden_units=...,
      feature_columns=...)
  ```

  It can also be used with a custom `model_fn`. Example:

  ```python
  def _my_model_fn(features, labels, mode):
    my_head = tf.estimator.RegressionHead()
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
    label_dimension: Number of regression labels per example. This is the size
      of the last dimension of the labels `Tensor` (typically, this has shape
      `[batch_size, label_dimension]`).
    loss_reduction: One of `tf.losses.Reduction` except `NONE`. Decides how to
      reduce training loss over batch and label dimension. Defaults to
      `SUM_OVER_BATCH_SIZE`, namely weighted sum of losses divided by
      `batch_size * label_dimension`.
    loss_fn: Optional loss function. Defaults to `mean_squared_error`.
    inverse_link_fn: Optional inverse link function, also known as \'mean
      function\'. Defaults to identity.
    name: name of the head. If provided, summary and metrics keys will be
      suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
  '''
    def __init__(self, label_dimension: int = 1, weight_column: Incomplete | None = None, loss_reduction=..., loss_fn: Incomplete | None = None, inverse_link_fn: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
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
        """Return predictions based on keys. See `base_head.Head` for details."""
    def predictions(self, logits):
        """Return predictions based on keys.

    See `base_head.Head` for details.

    Args:
      logits: logits `Tensor` with shape `[D0, D1, ... DN, logits_dimension]`.
        For many applications, the shape is `[batch_size, logits_dimension]`.

    Returns:
      A dict of predictions.
    """
    def metrics(self, regularization_losses: Incomplete | None = None):
        """Creates metrics. See `base_head.Head` for details."""
    def update_metrics(self, eval_metrics, features, logits, labels, regularization_losses: Incomplete | None = None):
        """Updates eval metrics. See `base_head.Head` for details."""

class PoissonRegressionHead(RegressionHead):
    '''Creates a `Head` for poisson regression using `tf.nn.log_poisson_loss`.

  The loss is the weighted sum over all input dimensions. Namely, if the input
  labels have shape `[batch_size, label_dimension]`, the loss is the weighted
  sum over both `batch_size` and `label_dimension`.

  The head expects `logits` with shape `[D0, D1, ... DN, label_dimension]`.
  In many applications, the shape is `[batch_size, label_dimension]`.

  The `labels` shape must match `logits`, namely
  `[D0, D1, ... DN, label_dimension]`. If `label_dimension=1`, shape
  `[D0, D1, ... DN]` is also supported.

  If `weight_column` is specified, weights must be of shape
  `[D0, D1, ... DN]`, `[D0, D1, ... DN, 1]` or
  `[D0, D1, ... DN, label_dimension]`.

  This is implemented as a generalized linear model, see
  https://en.wikipedia.org/wiki/Generalized_linear_model.

  The head can be used with a canned estimator. Example:

  ```python
  my_head = tf.estimator.PoissonRegressionHead()
  my_estimator = tf.estimator.DNNEstimator(
      head=my_head,
      hidden_units=...,
      feature_columns=...)
  ```

  It can also be used with a custom `model_fn`. Example:

  ```python
  def _my_model_fn(features, labels, mode):
    my_head = tf.estimator.PoissonRegressionHead()
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
    label_dimension: Number of regression labels per example. This is the size
      of the last dimension of the labels `Tensor` (typically, this has shape
      `[batch_size, label_dimension]`).
    loss_reduction: One of `tf.losses.Reduction` except `NONE`. Decides how to
      reduce training loss over batch and label dimension. Defaults to
      `SUM_OVER_BATCH_SIZE`, namely weighted sum of losses divided by `batch
      size * label_dimension`.
    compute_full_loss: Whether to include the constant `log(z!)` term in
      computing the poisson loss. See `tf.nn.log_poisson_loss` for the full
      documentation.
    name: name of the head. If provided, summary and metrics keys will be
      suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
  '''
    def __init__(self, label_dimension: int = 1, weight_column: Incomplete | None = None, loss_reduction=..., compute_full_loss: bool = True, name: Incomplete | None = None) -> None: ...

class LogisticRegressionHead(RegressionHead):
    '''Creates a `Head` for logistic regression.

  Uses `sigmoid_cross_entropy_with_logits` loss, which is the same as
  `BinaryClassHead`. The differences compared to `BinaryClassHead` are:

  * Does not support `label_vocabulary`. Instead, labels must be float in the
    range [0, 1].
  * Does not calculate some metrics that do not make sense, such as AUC.
  * In `PREDICT` mode, only returns logits and predictions
    (`=tf.sigmoid(logits)`), whereas `BinaryClassHead` also returns
    probabilities, classes, and class_ids.
  * Export output defaults to `RegressionOutput`, whereas `BinaryClassHead`
    defaults to `PredictOutput`.

  The head expects `logits` with shape `[D0, D1, ... DN, 1]`.
  In many applications, the shape is `[batch_size, 1]`.

  The `labels` shape must match `logits`, namely
  `[D0, D1, ... DN]` or `[D0, D1, ... DN, 1]`.

  If `weight_column` is specified, weights must be of shape
  `[D0, D1, ... DN]` or `[D0, D1, ... DN, 1]`.

  This is implemented as a generalized linear model, see
  https://en.wikipedia.org/wiki/Generalized_linear_model.

  The head can be used with a canned estimator. Example:

  ```python
  my_head = tf.estimator.LogisticRegressionHead()
  my_estimator = tf.estimator.DNNEstimator(
      head=my_head,
      hidden_units=...,
      feature_columns=...)
  ```

  It can also be used with a custom `model_fn`. Example:

  ```python
  def _my_model_fn(features, labels, mode):
    my_head = tf.estimator.LogisticRegressionHead()
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
    loss_reduction: One of `tf.losses.Reduction` except `NONE`. Decides how to
      reduce training loss over batch and label dimension. Defaults to
      `SUM_OVER_BATCH_SIZE`, namely weighted sum of losses divided by `batch
      size * label_dimension`.
    name: name of the head. If provided, summary and metrics keys will be
      suffixed by `"/" + name`. Also used as `name_scope` when creating ops.
  '''
    def __init__(self, weight_column: Incomplete | None = None, loss_reduction=..., name: Incomplete | None = None) -> None: ...
