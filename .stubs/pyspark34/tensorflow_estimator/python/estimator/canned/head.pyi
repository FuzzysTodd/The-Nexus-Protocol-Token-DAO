import abc
from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import model_fn as model_fn
from tensorflow_estimator.python.estimator.canned import metric_keys as metric_keys, prediction_keys as prediction_keys
from tensorflow_estimator.python.estimator.export import export_output as export_output
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys
from typing import NamedTuple

class LossSpec(NamedTuple):
    training_loss: Incomplete
    unreduced_loss: Incomplete
    weights: Incomplete
    processed_labels: Incomplete

class _Head(metaclass=abc.ABCMeta):
    """Interface for the head/top of a model.

  Given logits (or output of a hidden layer), a Head knows how to compute
  predictions, loss, train_op, metrics and export outputs. It is meant to:

  1. Simplify writing model_fn and to make model_fn more configurable
  2. Support wide range of machine learning models. Since most heads can work
     with logits, they can support DNN, RNN, Wide, Wide&Deep,
     Global objectives, Gradient boosted trees and many other types
     of machine learning models.

  Common usage:
  Here is simplified model_fn to build a DNN regression model.
    ```python
    def _my_dnn_model_fn(features, labels, mode, params, config=None):
      # Optionally your callers can pass head to model_fn as a param.
      head = tf.contrib.estimator.regression_head(...)
      inputs = tf.feature_column.input_layer(features, ...)
      hidden_layer0 = tf.layers.dense(
          inputs, units=1000, activation=tf.nn.relu)
      hidden_layer1 = tf.layers.dense(
          hidden_layer0, units=500, activation=tf.nn.relu)
      logits = tf.layers.dense(
          hidden_layer1, units=head.logits_dimension, activation=None)

      return head.create_estimator_spec(
          features=features,
          labels=labels,
          mode=mode,
          logits=logits,
          optimizer=optimizer)
    ```

  There are cases where computing and applying gradients can not be meaningfully
  captured with optimizer or train_op_fn we support (for example, with sync
  optimizer). In such case, you can take the responsibility on your own. Here is
  a common use case,
    ```python
    estimator_spec = head.create_estimator_spec(
        features=features,
        labels=labels,
        mode=mode,
        logits=logits,
        train_op_fn=lambda _: tf.no_op())
    if mode == ModeKeys.TRAIN:
      optimizer = ...
      sync = tf.train.SyncReplicasOptimizer(opt=optimizer, ...)
      update_op = sync.minimize(
          estimator_spec.loss, global_step=tf.get_global_step())
      hooks = [sync.make_session_run_hook(is_chief)]
      ... update train_op and hooks in EstimatorSpec and return
    ```
  """
    __metaclass__ = abc.ABCMeta
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

    Typically, logits is of shape `[batch_size, logits_dimension]`.

    Returns:
      The expected size of the `logits` tensor.
    """
    @abc.abstractmethod
    def create_loss(self, features, mode, logits, labels):
        """Returns a loss Tensor from provided logits.

    This function is designed to be used by framework developers.  Almost all
    users should use create_estimator_spec(), which calls this internally.
    `mode` and `features` are most likely not used, but some Head
    implementations may require them.

    Args:
      features: Input `dict` of `Tensor` objects.
      mode: Estimator's `ModeKeys`.
      logits: logits `Tensor` to be used for loss construction.
      labels: Labels `Tensor`, or `dict` of same.

    Returns:
      A LossSpec that contains
      * the scalar `Tensor` representing reduced weighted training loss
      * the `Tensor` representing the unreduced unweighted loss
      * the `Tensor` representing the example weights
      * possibly processed labels (e.g. vocabulary lookup, shape manipulation,
        etc.)

      To be extendable in the future.
    """
    def create_estimator_spec(self, features, mode, logits, labels: Incomplete | None = None, optimizer: Incomplete | None = None, train_op_fn: Incomplete | None = None, regularization_losses: Incomplete | None = None):
        """Returns `EstimatorSpec` that a model_fn can return.

    Please note that,
    + All args must be passed via name.

    Args:
      features: Input `dict` of `Tensor` or `SparseTensor` objects.
      mode: Estimator's `ModeKeys`.
      logits: logits `Tensor` to be used by the head.
      labels: Labels `Tensor`, or `dict` of same.
      optimizer: `Optimizer` instance to optimize the loss in TRAIN mode.
        Namely, sets `train_op = optimizer.minimize(loss, global_step)`, which
        updates variables and increments `global_step`.
      train_op_fn: Function that takes a scalar loss `Tensor` and returns an op
        to optimize the model with the loss in TRAIN mode. Used if `optimizer`
        is `None`. Exactly one of `train_op_fn` and `optimizer` must be set in
        TRAIN mode. None is allowed in other modes. If you want to optimize loss
        yourself you can pass `lambda _: tf.no_op()` and then use
          EstimatorSpec.loss to compute and apply gradients.
      regularization_losses: A list of additional scalar losses to be added to
        the training loss, such as regularization losses.

    Returns:
      `EstimatorSpec`.
    """

class _MultiClassHeadWithSoftmaxCrossEntropyLoss(_Head):
    """See `_multi_class_head_with_softmax_cross_entropy_loss`."""
    def __init__(self, n_classes, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, loss_reduction=..., loss_fn: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features, mode, logits, labels):
        """See `Head`."""

class _BinaryLogisticHeadWithSigmoidCrossEntropyLoss(_Head):
    """See `_binary_logistic_head_with_sigmoid_cross_entropy_loss`."""
    def __init__(self, weight_column: Incomplete | None = None, thresholds: Incomplete | None = None, label_vocabulary: Incomplete | None = None, loss_reduction=..., loss_fn: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features, mode, logits, labels):
        """See `Head`."""

class _RegressionHeadWithMeanSquaredErrorLoss(_Head):
    """`Head` for regression using the mean squared loss."""
    def __init__(self, label_dimension, weight_column: Incomplete | None = None, loss_reduction=..., loss_fn: Incomplete | None = None, inverse_link_fn: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """`Head` for regression."""
    @property
    def name(self): ...
    @property
    def logits_dimension(self): ...
    def create_loss(self, features, mode, logits, labels):
        """See `Head`."""
