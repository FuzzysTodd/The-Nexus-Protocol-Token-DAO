import abc
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.export import export_output as export_output

DEFAULT_SERVING_KEY: Incomplete
CLASSIFY_SERVING_KEY: str
REGRESS_SERVING_KEY: str
PREDICT_SERVING_KEY: str

class Head(metaclass=abc.ABCMeta):
    '''Interface for the head/top of a model.

  Head sits on top of the model network and handles computing the outputs of
  the network. Given logits (or output of a hidden layer), a Head knows how to
  compute predictions, loss, train_op, metrics and export outputs. It is meant
  to:

  1. Simplify writing model_fn and to make model_fn more configurable for
     Estimator.
  2. Simpilfy creating loss and metrics for the train and test loop in Eager
     execution.
  3. Support wide range of machine learning models. Since most heads can work
     with logits, they can support DNN, RNN, Wide, Wide&Deep,
     Global objectives, Gradient boosted trees and many other types
     of machine learning models.

  Common usage:
  Here is simplified model_fn to build a DNN regression model.
    ```python
    def _my_dnn_model_fn(features, labels, mode, params, config=None):
      # Optionally your callers can pass head to model_fn as a param.
      head = tf.estimator.RegressionHead(...)

      feature_columns = tf.feature_column.numeric_column(...)
      feature_layer = tf.keras.layers.DenseFeatures(feature_columns)
      inputs = feature_layer(features)

      # Compute logits with tf.keras.layers API
      hidden_layer0 = tf.keras.layers.Dense(
          units=1000, activation="relu")(inputs)
      hidden_layer1 = tf.keras.layers.Dense(
          units=500, activation="relu")(hidden_layer0)
      logits = tf.keras.layers.Dense(
          units=head.logits_dimension, activation=None)(hidden_layer1)

      # Or use Keras model for logits computation
      model = tf.keras.Sequential()
      model.add(tf.keras.layers.Dense(units=1000, activation="relu"))
      model.add(tf.keras.layers.Dense(units=500, activation="relu"))
      model.add(tf.keras.layers.Dense(
         units=head.logits_dimension, activation=None))
      logits = model(inputs)

      return head.create_estimator_spec(
          features=features,
          labels=labels,
          mode=mode,
          logits=logits,
          optimizer=optimizer)
    ```
  '''
    @property
    @abc.abstractmethod
    def name(self):
        """The name of this head.

    Returns:
      A string.
    """
    @property
    @abc.abstractmethod
    def logits_dimension(self):
        """Size of the last dimension of the logits `Tensor`.

    Often is the number of classes, labels, or real values to be predicted.
    Typically, logits is of shape `[batch_size, logits_dimension]`.

    Returns:
      The expected size of the `logits` tensor.
    """
    @property
    @abc.abstractmethod
    def loss_reduction(self):
        """One of `tf.losses.Reduction`.

    Describes how to reduce training loss over batch, such as mean or sum.

    Returns:
      The type of loss reduction used in the head.
    """
    @abc.abstractmethod
    def loss(self, labels, logits, features: Incomplete | None = None, mode: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns a loss `Tensor` from provided arguments.

    Note that, the args of `features` and `mode` are most likely not used, but
    some Head implementations may require them.

    Args:
      labels: Labels `Tensor`, or `dict` mapping string label names to `Tensor`
        objects of the label values.
      logits: Logits `Tensor` to be used for loss construction.
      features: Input `dict` mapping string feature names to `Tensor` or
        `SparseTensor` objects containing the values for that feature in a
        minibatch. Often to be used to fetch example-weight tensor.
      mode: Estimator's `ModeKeys`. To be used in case loss calculation is
        different in Train and Eval mode.
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses.

    Returns:
      A scalar `Tensor` representing regularized training loss used in train and
      eval.
    """
    @abc.abstractmethod
    def predictions(self, logits, keys: Incomplete | None = None):
        """Returns a `dict` of predictions from provided logits.

    Args:
      logits: Logits `Tensor` to be used for prediction construction.
      keys: A list of `string` for prediction keys. Defaults to `None`, meaning
        if not specified, predictions will be created for all the pre-defined
        valid keys in the head.

    Returns:
      A `dict` of predicted `Tensor` keyed by prediction name.
    """
    @abc.abstractmethod
    def metrics(self, regularization_losses: Incomplete | None = None):
        """Returns a `dict` of metric objects.

    Args:
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses.

    Returns:
       A `dict` of metrics keyed by string name. The value is an instance of
       `Metric` class.
    """
    @abc.abstractmethod
    def update_metrics(self, eval_metrics, features, logits, labels, mode: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Updates metric objects and returns a `dict` of the updated metrics.

    Args:
      eval_metrics: A `dict` of metrics to be updated.
      features: Input `dict` mapping string feature names to `Tensor` or
        `SparseTensor` objects containing the values for that feature in a
        minibatch. Often to be used to fetch example-weight tensor.
      logits: logits `Tensor` to be used for metrics update.
      labels: Labels `Tensor`, or `dict` mapping string label names to `Tensor`
        objects of the label values.
      mode: Estimator's `ModeKeys`. In most cases, this arg is not used and can
        be removed in the method implementation.
      regularization_losses: A list of additional scalar losses to be added to
        the training and evaluation loss, such as regularization losses.  Note
        that, the `mode` arg is not used in the `tf.estimator.*Head`. If the
        update of the metrics doesn't rely on `mode`, it can be safely ignored
        in the method signature.

    Returns:
       A `dict` of updated metrics keyed by name. The value is an instance of
       `Metric` class.
    """
    def create_estimator_spec(self, features, mode, logits, labels: Incomplete | None = None, optimizer: Incomplete | None = None, trainable_variables: Incomplete | None = None, train_op_fn: Incomplete | None = None, update_ops: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns `EstimatorSpec` that a model_fn can return.

    It is recommended to pass all args via name.

    Args:
      features: Input `dict` mapping string feature names to `Tensor` or
        `SparseTensor` objects containing the values for that feature in a
        minibatch. Often to be used to fetch example-weight tensor.
      mode: Estimator's `ModeKeys`.
      logits: Logits `Tensor` to be used by the head.
      labels: Labels `Tensor`, or `dict` mapping string label names to `Tensor`
        objects of the label values.
      optimizer: An `tf.keras.optimizers.Optimizer` instance to optimize the
        loss in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
        trainable_variables)`, which updates variables to minimize `loss`.
      trainable_variables: A list or tuple of `Variable` objects to update to
        minimize `loss`. In Tensorflow 1.x, by default these are the list of
        variables collected in the graph under the key
        `GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
        collections and GraphKeys, trainable_variables need to be passed
        explicitly here.
      train_op_fn: Function that takes a scalar loss `Tensor` and returns an op
        to optimize the model with the loss in TRAIN mode. Used if `optimizer`
        is `None`. Exactly one of `train_op_fn` and `optimizer` must be set in
        TRAIN mode. By default, it is `None` in other modes. If you want to
        optimize loss yourself, you can pass `lambda _: tf.no_op()` and then use
          `EstimatorSpec.loss` to compute and apply gradients.
      update_ops: A list or tuple of update ops to be run at training time. For
        example, layers such as BatchNormalization create mean and variance
        update ops that need to be run at training time. In Tensorflow 1.x,
        these are thrown into an UPDATE_OPS collection. As Tensorflow 2.x
        doesn't have collections, update_ops need to be passed explicitly here.
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses.

    Returns:
      `EstimatorSpec`.
    """

def check_dense_labels_match_logits_and_reshape(labels, logits, expected_labels_dimension):
    """Checks labels shape matches logits, and reshapes if needed.

  Consider logits of shape [D0, D1, ... DN, logits_dimension]. Then labels
  shape must be [D0, D1, ... DN, expected_labels_dimension].
  If expected_labels_dimension=1, labels could be [D0, D1, ... DN] and this
  method reshapes them to [D0, D1, ... DN, 1].

  Args:
    labels: labels Tensor.
    logits: logits Tensor.
    expected_labels_dimension: Integer.

  Returns:
    Validated and reshaped labels Tensor.

  Raises:
    ValueError: If labels is a SparseTensor.
    ValueError: If labels shape is statically defined and fails validation.
    OpError: If labels shape is not statically defined and fails validation.
  """
def get_weights_and_check_match_logits(features, weight_column, logits, allow_per_logit_weights: bool = False):
    """Fetches weights from features and checks that the shape matches logits.

  Consider logits of shape [D0, D1, ... DN, logits_dimension]. Weights shape
  can be either:
  * [D0, D1, ... DN, logits_dimension] if `allow_per_logit_weights=True`.
  * [D0, D1, ... DN, 1]
  * [D0, D1, ... DN]: In this case, weights is reshaped into
    [D0, D1, ... DN, 1] to work with weight broadcasting rules.

  Args:
    features: The features dict that contains weights.
    weight_column: The weight column. If not given, this method returns 1.
    logits: logits Tensor.
    allow_per_logit_weights: Boolean. Whether we allow weights along the logits
      dimension, namely shape `[D0, D1, ... DN, logits_dimension]`.

  Returns:
    Validated and reshaped weights Tensor.

  Raises:
    ValueError: If the weights `Tensor` cannot be cast into float.
  """
def check_logits_final_dim(logits, expected_logits_dimension):
    """Checks that logits shape is [D0, D1, ... DN, logits_dimension]."""
def validate_loss_fn_args(loss_fn) -> None:
    """Validates loss_fn arguments.

  Required arguments: labels, logits.
  Optional arguments: features, loss_reduction.

  Args:
    loss_fn: The loss function.

  Raises:
    ValueError: If the signature is unexpected.
  """
def validate_loss_reduction(loss_reduction) -> None: ...
def validate_update_ops(update_ops: Incomplete | None = None) -> None: ...
def validate_v2_optimizer(optimizer) -> None: ...
def validate_trainable_variables(trainable_variables: Incomplete | None = None) -> None: ...
def validate_n_classes(n_classes):
    """Validates n_classes argument.

  Required arguments: n_classes.

  Args:
    n_classes: The number of classes.

  Raises:
    ValueError: If n_classes is <= 2 and n_classes is a Python integer.
  Returns:
    n_classes in its original type.
  """
def call_loss_fn(loss_fn, labels, logits, features, expected_loss_dim: int = 1):
    """Calls loss_fn and checks the returned shape.

  For shape checking, eager uses the static dimension to improve performance.

  Args:
    loss_fn: The loss function.
    labels: Processed labels Tensor.
    logits: Logits Tensor of shape [D0, D1, ... DN, logits_dimension].
    features: Features dict.
    expected_loss_dim: The expected last dimension of loss Tensor.

  Returns:
    Loss Tensor with shape [D0, D1, ... DN, expected_loss_dim].

  Raises:
    ValueError: If the loss tensor shape is unexpected.
  """
def check_prediction_keys(pred_keys, valid_keys) -> None: ...
def all_class_ids(logits, n_classes): ...
def all_classes(logits, n_classes, label_vocabulary: Incomplete | None = None): ...
def classification_output(scores, n_classes, label_vocabulary: Incomplete | None = None): ...
def check_label_range(labels, n_classes, message: Incomplete | None = None):
    """Check if labels are in the range of [0, n_classes)."""
def update_metric_with_broadcast_weights(eval_metric, values, weights) -> None: ...
def create_eval_metrics_tuple(fn, kwargs):
    """Creates TPU eval metrics tuple.

  Helper function to make eval_metric tuple (eval_metric_fn, fn_kwargs) used
  by `TPUEstimator`. TPUEstimator requires that `eval_metric_fn` take
  exclusively Tensor arguments. This helper can help create such a function from
  a more generic function that can take both Tensor and non-Tensor arguments.

  Args:
    fn: A eval_metric_fn that takes both Tensor and non-Tensor arguments. This
      function must return a dict of form
        {'metric name': (metric_tensor, eval_op)}
    kwargs: Dict of arguments for `fn`.

  Returns:
    `eval_metric` tuple that can be passed to a `model_fn._TPUEstimatorSpec`.
  """
def create_estimator_spec_train_op(head_name, optimizer: Incomplete | None = None, trainable_variables: Incomplete | None = None, train_op_fn: Incomplete | None = None, update_ops: Incomplete | None = None, regularized_training_loss: Incomplete | None = None, loss_reduction=...):
    """Create train_op for estimator_spec.

  Args:
    head_name: The name of the head.
    optimizer: An `tf.keras.optimizers.Optimizer` instance to optimize the loss
      in TRAIN mode. Namely, sets `train_op = optimizer.get_updates(loss,
      trainable_variables)`, which updates variables to minimize `loss`.
    trainable_variables: A list or tuple of `Variable` objects to update to
      minimize `loss`. In Tensorflow 1.x, by default these are the list of
      variables collected in the graph under the key
      `GraphKeys.TRAINABLE_VARIABLES`. As Tensorflow 2.x doesn't have
      collections and GraphKeys, trainable_variables need to be passed
      explicitly here.
    train_op_fn: Function that takes a scalar loss `Tensor` and returns
      `train_op`. Used if `optimizer` is `None`.
    update_ops: A list or tuple of update ops to be run at training time. For
      example, layers such as BatchNormalization create mean and variance update
      ops that need to be run at training time. In Tensorflow 1.x, these are
      thrown into an UPDATE_OPS collection. As Tensorflow 2.x doesn't have
      collections, update_ops need to be passed explicitly here.
    regularized_training_loss: A scalar for total training loss that includes
      all regularization losses. If you're not using optimizer to generate train
      op, make sure to scale the loss correctly before passing it in. The loss
      typically needs to be scaled down by the number of workers.
    loss_reduction: One of `tf.keras.losses.Reduction` except `NONE`. Describes
      how to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.

  Returns:
    A train op for EstimatorSpec.
  """
def create_estimator_spec_summary(regularized_training_loss, regularization_losses: Incomplete | None = None, summary_key_fn: Incomplete | None = None) -> None:
    """Create summary for estimator_spec."""
