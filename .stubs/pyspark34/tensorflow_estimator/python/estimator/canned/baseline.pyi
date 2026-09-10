from _typeshed import Incomplete
from tensorflow_estimator.python.estimator import estimator as estimator
from tensorflow_estimator.python.estimator.canned import optimizers as optimizers
from tensorflow_estimator.python.estimator.estimator_export import estimator_export as estimator_export
from tensorflow_estimator.python.estimator.head import head_utils as head_utils, regression_head as regression_head
from tensorflow_estimator.python.estimator.mode_keys import ModeKeys as ModeKeys

class BaselineClassifierV2(estimator.EstimatorV2):
    '''A classifier that can establish a simple baseline.

  This classifier ignores feature values and will learn to predict the average
  value of each label. For single-label problems, this will predict the
  probability distribution of the classes as seen in the labels. For multi-label
  problems, this will predict the fraction of examples that are positive for
  each class.

  Example:

  ```python

  # Build BaselineClassifier
  classifier = tf.estimator.BaselineClassifier(n_classes=3)

  # Input builders
  def input_fn_train:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass

  def input_fn_eval:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass

  # Fit model.
  classifier.train(input_fn=input_fn_train)

  # Evaluate cross entropy between the test and train labels.
  loss = classifier.evaluate(input_fn=input_fn_eval)["loss"]

  # predict outputs the probability distribution of the classes as seen in
  # training.
  predictions = classifier.predict(new_samples)

  ```

  Input of `train` and `evaluate` should have following features,
    otherwise there will be a `KeyError`:

  * if `weight_column` is not `None`, a feature with
     `key=weight_column` whose value is a `Tensor`.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, loss_reduction=...) -> None:
        """Initializes a BaselineClassifier instance.

    Args:
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      n_classes: number of label classes. Default is binary classification.
        It must be greater than 1. Note: Class labels are integers representing
          the class index (i.e. values from 0 to n_classes-1). For arbitrary
          label values (e.g. string labels), convert to class indices first.
      weight_column: A string or a `NumericColumn` created by
        `tf.feature_column.numeric_column` defining feature column representing
        weights. It will be multiplied by the loss of the example.
      label_vocabulary: Optional list of strings with size `[n_classes]`
        defining the label vocabulary. Only supported for `n_classes` > 2.
      optimizer: String, `tf.keras.optimizers.*` object, or callable that
        creates the optimizer to use for training. If not specified, will use
        `Ftrl` as the default optimizer.
      config: `RunConfig` object to configure the runtime settings.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.

    Returns:
      A `BaselineClassifier` estimator.

    Raises:
      ValueError: If `n_classes` < 2.
    """

class BaselineClassifier(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, model_dir: Incomplete | None = None, n_classes: int = 2, weight_column: Incomplete | None = None, label_vocabulary: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, loss_reduction=...) -> None: ...

class BaselineEstimatorV2(estimator.EstimatorV2):
    '''An estimator that can establish a simple baseline.

  The estimator uses a user-specified head.

  This estimator ignores feature values and will learn to predict the average
  value of each label. E.g. for single-label classification problems, this will
  predict the probability distribution of the classes as seen in the labels.
  For multi-label classification problems, it will predict the ratio of examples
  that contain each class.

  Example:

  ```python

  # Build baseline multi-label classifier.
  estimator = tf.estimator.BaselineEstimator(
      head=tf.estimator.MultiLabelHead(n_classes=3))

  # Input builders
  def input_fn_train:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass

  def input_fn_eval:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass

  # Fit model.
  estimator.train(input_fn=input_fn_train)

  # Evaluates cross entropy between the test and train labels.
  loss = estimator.evaluate(input_fn=input_fn_eval)["loss"]

  # For each class, predicts the ratio of training examples that contain the
  # class.
  predictions = estimator.predict(new_samples)

  ```

  Input of `train` and `evaluate` should have following features,
    otherwise there will be a `KeyError`:

  * if `weight_column` is specified in the `head` constructor (and not None) for
    the head passed to BaselineEstimator\'s constructor, a feature with
    `key=weight_column` whose value is a `Tensor`.
  '''
    def __init__(self, head, model_dir: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None) -> None:
        """Initializes a BaselineEstimator instance.

    Args:
      head: A `Head` instance constructed with a method such as
        `tf.estimator.MultiLabelHead`.
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      optimizer: String, `tf.keras.optimizers.*` object, or callable that
        creates the optimizer to use for training. If not specified, will use
        `Ftrl` as the default optimizer.
      config: `RunConfig` object to configure the runtime settings.
    """

class BaselineEstimator(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, head, model_dir: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None) -> None: ...

class BaselineRegressorV2(estimator.EstimatorV2):
    '''A regressor that can establish a simple baseline.

  This regressor ignores feature values and will learn to predict the average
  value of each label.

  Example:

  ```python

  # Build BaselineRegressor
  regressor = tf.estimator.BaselineRegressor()

  # Input builders
  def input_fn_train:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass

  def input_fn_eval:
    # Returns tf.data.Dataset of (x, y) tuple where y represents label\'s class
    # index.
    pass

  # Fit model.
  regressor.train(input_fn=input_fn_train)

  # Evaluate squared-loss between the test and train targets.
  loss = regressor.evaluate(input_fn=input_fn_eval)["loss"]

  # predict outputs the mean value seen during training.
  predictions = regressor.predict(new_samples)
  ```

  Input of `train` and `evaluate` should have following features,
    otherwise there will be a `KeyError`:

  * if `weight_column` is not `None`, a feature with
     `key=weight_column` whose value is a `Tensor`.

  @compatibility(eager)
  Estimators can be used while eager execution is enabled. Note that `input_fn`
  and all hooks are executed inside a graph context, so they have to be written
  to be compatible with graph mode. Note that `input_fn` code using `tf.data`
  generally works in both graph and eager modes.
  @end_compatibility
  '''
    def __init__(self, model_dir: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, loss_reduction=...) -> None:
        """Initializes a BaselineRegressor instance.

    Args:
      model_dir: Directory to save model parameters, graph and etc. This can
        also be used to load checkpoints from the directory into a estimator to
        continue training a previously saved model.
      label_dimension: Number of regression targets per example. This is the
        size of the last dimension of the labels and logits `Tensor` objects
        (typically, these have shape `[batch_size, label_dimension]`).
      weight_column: A string or a `_NumericColumn` created by
        `tf.feature_column.numeric_column` defining feature column representing
        weights. It will be multiplied by the loss of the example.
      optimizer: String, `tf.keras.optimizers.*` object, or callable that
        creates the optimizer to use for training. If not specified, will use
        `Ftrl` as the default optimizer.
      config: `RunConfig` object to configure the runtime settings.
      loss_reduction: One of `tf.losses.Reduction` except `NONE`. Describes how
        to reduce training loss over batch. Defaults to `SUM_OVER_BATCH_SIZE`.

    Returns:
      A `BaselineRegressor` estimator.
    """

class BaselineRegressor(estimator.Estimator):
    __doc__: Incomplete
    def __init__(self, model_dir: Incomplete | None = None, label_dimension: int = 1, weight_column: Incomplete | None = None, optimizer: str = 'Ftrl', config: Incomplete | None = None, loss_reduction=...) -> None: ...
