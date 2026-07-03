import abc
from _typeshed import Incomplete
from tensorflow.python.autograph.core import ag_ctx as ag_ctx
from tensorflow.python.eager import context as context, def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, tensor_shape as tensor_shape
from tensorflow.python.keras import activations as activations, backend as backend
from tensorflow.python.keras.engine import base_layer as base_layer, base_layer_utils as base_layer_utils, keras_tensor as keras_tensor
from tensorflow.python.keras.losses import binary_crossentropy as binary_crossentropy, categorical_crossentropy as categorical_crossentropy, categorical_hinge as categorical_hinge, hinge as hinge, kullback_leibler_divergence as kullback_leibler_divergence, logcosh as logcosh, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_squared_error as mean_squared_error, mean_squared_logarithmic_error as mean_squared_logarithmic_error, poisson as poisson, sparse_categorical_crossentropy as sparse_categorical_crossentropy, squared_hinge as squared_hinge
from tensorflow.python.keras.saving.saved_model import metric_serialization as metric_serialization
from tensorflow.python.keras.utils import generic_utils as generic_utils, losses_utils as losses_utils, metrics_utils as metrics_utils
from tensorflow.python.keras.utils.generic_utils import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object, to_list as to_list
from tensorflow.python.keras.utils.tf_utils import is_tensor_or_variable as is_tensor_or_variable
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, confusion_matrix as confusion_matrix, init_ops as init_ops, math_ops as math_ops, nn as nn, weights_broadcast_ops as weights_broadcast_ops
from tensorflow.python.util import dispatch as dispatch, nest as nest
from tensorflow.python.util.tf_export import keras_export as keras_export
from tensorflow.tools.docs import doc_controls as doc_controls

class Metric(base_layer.Layer, metaclass=abc.ABCMeta):
    """Encapsulates metric logic and state.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    **kwargs: Additional layer keywords arguments.

  Standalone usage:

  ```python
  m = SomeMetric(...)
  for input in ...:
    m.update_state(input)
  print('Final result: ', m.result().numpy())
  ```

  Usage with `compile()` API:

  ```python
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(64, activation='relu'))
  model.add(tf.keras.layers.Dense(64, activation='relu'))
  model.add(tf.keras.layers.Dense(10, activation='softmax'))

  model.compile(optimizer=tf.keras.optimizers.RMSprop(0.01),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=[tf.keras.metrics.CategoricalAccuracy()])

  data = np.random.random((1000, 32))
  labels = np.random.random((1000, 10))

  dataset = tf.data.Dataset.from_tensor_slices((data, labels))
  dataset = dataset.batch(32)

  model.fit(dataset, epochs=10)
  ```

  To be implemented by subclasses:
  * `__init__()`: All state variables should be created in this method by
    calling `self.add_weight()` like: `self.var = self.add_weight(...)`
  * `update_state()`: Has all updates to the state variables like:
    self.var.assign_add(...).
  * `result()`: Computes and returns a value for the metric
    from the state variables.

  Example subclass implementation:

  ```python
  class BinaryTruePositives(tf.keras.metrics.Metric):

    def __init__(self, name='binary_true_positives', **kwargs):
      super(BinaryTruePositives, self).__init__(name=name, **kwargs)
      self.true_positives = self.add_weight(name='tp', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
      y_true = tf.cast(y_true, tf.bool)
      y_pred = tf.cast(y_pred, tf.bool)

      values = tf.logical_and(tf.equal(y_true, True), tf.equal(y_pred, True))
      values = tf.cast(values, self.dtype)
      if sample_weight is not None:
        sample_weight = tf.cast(sample_weight, self.dtype)
        sample_weight = tf.broadcast_to(sample_weight, values.shape)
        values = tf.multiply(values, sample_weight)
      self.true_positives.assign_add(tf.reduce_sum(values))

    def result(self):
      return self.true_positives
  ```
  """
    stateful: bool
    built: bool
    def __init__(self, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    def __new__(cls, *args, **kwargs): ...
    def __call__(self, *args, **kwargs):
        """Accumulates statistics and then computes metric result value.

    Args:
      *args:
      **kwargs: A mini-batch of inputs to the Metric,
        passed on to `update_state()`.

    Returns:
      The metric value tensor.
    """
    @property
    def dtype(self): ...
    def get_config(self):
        """Returns the serializable config of the metric."""
    def reset_state(self):
        """Resets all of the metric state variables.

    This function is called between epochs/steps,
    when a metric is evaluated during training.
    """
    @abc.abstractmethod
    def update_state(self, *args, **kwargs):
        """Accumulates statistics for the metric.

    Note: This function is executed as a graph function in graph mode.
    This means:
      a) Operations on the same resource are executed in textual order.
         This should make it easier to do things like add the updated
         value of a variable to another, for example.
      b) You don't need to worry about collecting the update ops to execute.
         All update ops added to the graph by this function will be executed.
      As a result, code should generally work the same way with graph or
      eager execution.

    Args:
      *args:
      **kwargs: A mini-batch of inputs to the Metric.
    """
    @abc.abstractmethod
    def result(self):
        """Computes and returns the metric value tensor.

    Result computation is an idempotent operation that simply calculates the
    metric value using the state variables.
    """
    def add_weight(self, name, shape=(), aggregation=..., synchronization=..., initializer: Incomplete | None = None, dtype: Incomplete | None = None):
        """Adds state variable. Only for use by subclasses."""
    @property
    def trainable_weights(self): ...
    @property
    def non_trainable_weights(self): ...
    def reset_states(self): ...

class Reduce(Metric):
    """Encapsulates metrics that perform a reduce operation on the values.

  Args:
    reduction: a `tf.keras.metrics.Reduction` enum value.
    name: string name of the metric instance.
    dtype: (Optional) data type of the metric result.
  """
    reduction: Incomplete
    total: Incomplete
    count: Incomplete
    def __init__(self, reduction, name, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, values, sample_weight: Incomplete | None = None):
        """Accumulates statistics for computing the metric.

    Args:
      values: Per-example value.
      sample_weight: Optional weighting of each example. Defaults to 1.

    Returns:
      Update op.
    """
    def result(self): ...

class Sum(Reduce):
    """Computes the (weighted) sum of the given values.

  For example, if values is [1, 3, 5, 7] then the sum is 16.
  If the weights were specified as [1, 1, 0, 0] then the sum would be 4.

  This metric creates one variable, `total`, that is used to compute the sum of
  `values`. This is ultimately returned as `sum`.

  If `sample_weight` is `None`, weights default to 1.  Use `sample_weight` of 0
  to mask values.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Sum()
  >>> m.update_state([1, 3, 5, 7])
  >>> m.result().numpy()
  16.0

  Usage with `compile()` API:

  ```python
  model.add_metric(tf.keras.metrics.Sum(name='sum_1')(outputs))
  model.compile(optimizer='sgd', loss='mse')
  ```
  """
    def __init__(self, name: str = 'sum', dtype: Incomplete | None = None) -> None: ...

class Mean(Reduce):
    """Computes the (weighted) mean of the given values.

  For example, if values is [1, 3, 5, 7] then the mean is 4.
  If the weights were specified as [1, 1, 0, 0] then the mean would be 2.

  This metric creates two variables, `total` and `count` that are used to
  compute the average of `values`. This average is ultimately returned as `mean`
  which is an idempotent operation that simply divides `total` by `count`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Mean()
  >>> m.update_state([1, 3, 5, 7])
  >>> m.result().numpy()
  4.0
  >>> m.reset_state()
  >>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0])
  >>> m.result().numpy()
  2.0

  Usage with `compile()` API:

  ```python
  model.add_metric(tf.keras.metrics.Mean(name='mean_1')(outputs))
  model.compile(optimizer='sgd', loss='mse')
  ```
  """
    def __init__(self, name: str = 'mean', dtype: Incomplete | None = None) -> None: ...

class MeanRelativeError(Mean):
    """Computes the mean relative error by normalizing with the given values.

  This metric creates two local variables, `total` and `count` that are used to
  compute the mean relative error. This is weighted by `sample_weight`, and
  it is ultimately returned as `mean_relative_error`:
  an idempotent operation that simply divides `total` by `count`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    normalizer: The normalizer values with same shape as predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.MeanRelativeError(normalizer=[1, 3, 2, 3])
  >>> m.update_state([1, 3, 2, 3], [2, 4, 6, 8])

  >>> # metric = mean(|y_pred - y_true| / normalizer)
  >>> #        = mean([1, 1, 4, 5] / [1, 3, 2, 3]) = mean([1, 1/3, 2, 5/3])
  >>> #        = 5/4 = 1.25
  >>> m.result().numpy()
  1.25

  Usage with `compile()` API:

  ```python
  model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[tf.keras.metrics.MeanRelativeError(normalizer=[1, 3])])
  ```
  """
    normalizer: Incomplete
    def __init__(self, normalizer, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates metric statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def get_config(self): ...

class MeanMetricWrapper(Mean):
    """Wraps a stateless metric function with the Mean metric.

  You could use this class to quickly build a mean metric from a function. The
  function needs to have the signature `fn(y_true, y_pred)` and return a
  per-sample loss array. `MeanMetricWrapper.result()` will return
  the average metric value across all samples seen so far.

  For example:

  ```python
  def accuracy(y_true, y_pred):
    return tf.cast(tf.math.equal(y_true, y_pred), tf.float32)

  accuracy_metric = tf.keras.metrics.MeanMetricWrapper(fn=accuracy)

  keras_model.compile(..., metrics=accuracy_metric)
  ```

  Args:
    fn: The metric function to wrap, with signature `fn(y_true, y_pred,
      **kwargs)`.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    **kwargs: Keyword arguments to pass on to `fn`.
  """
    def __init__(self, fn, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates metric statistics.

    `y_true` and `y_pred` should have the same shape.

    Args:
      y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
      y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
      sample_weight: Optional `sample_weight` acts as a
        coefficient for the metric. If a scalar is provided, then the metric is
        simply scaled by the given value. If `sample_weight` is a tensor of size
        `[batch_size]`, then the metric for each sample of the batch is rescaled
        by the corresponding element in the `sample_weight` vector. If the shape
        of `sample_weight` is `[batch_size, d0, .. dN-1]` (or can be broadcasted
        to this shape), then each metric element of `y_pred` is scaled by the
        corresponding value of `sample_weight`. (Note on `dN-1`: all metric
        functions reduce by 1 dimension, usually the last axis (-1)).

    Returns:
      Update op.
    """
    def get_config(self): ...
    @classmethod
    def from_config(cls, config): ...

class Accuracy(MeanMetricWrapper):
    """Calculates how often predictions equal labels.

  This metric creates two local variables, `total` and `count` that are used to
  compute the frequency with which `y_pred` matches `y_true`. This frequency is
  ultimately returned as `binary accuracy`: an idempotent operation that simply
  divides `total` by `count`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Accuracy()
  >>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]])
  >>> m.result().numpy()
  0.75

  >>> m.reset_state()
  >>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]],
  ...                sample_weight=[1, 1, 0, 0])
  >>> m.result().numpy()
  0.5

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.Accuracy()])
  ```
  """
    def __init__(self, name: str = 'accuracy', dtype: Incomplete | None = None) -> None: ...

class BinaryAccuracy(MeanMetricWrapper):
    """Calculates how often predictions match binary labels.

  This metric creates two local variables, `total` and `count` that are used to
  compute the frequency with which `y_pred` matches `y_true`. This frequency is
  ultimately returned as `binary accuracy`: an idempotent operation that simply
  divides `total` by `count`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    threshold: (Optional) Float representing the threshold for deciding
    whether prediction values are 1 or 0.

  Standalone usage:

  >>> m = tf.keras.metrics.BinaryAccuracy()
  >>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]])
  >>> m.result().numpy()
  0.75

  >>> m.reset_state()
  >>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]],
  ...                sample_weight=[1, 0, 0, 1])
  >>> m.result().numpy()
  0.5

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.BinaryAccuracy()])
  ```
  """
    def __init__(self, name: str = 'binary_accuracy', dtype: Incomplete | None = None, threshold: float = 0.5) -> None: ...

class CategoricalAccuracy(MeanMetricWrapper):
    """Calculates how often predictions match one-hot labels.

  You can provide logits of classes as `y_pred`, since argmax of
  logits and probabilities are same.

  This metric creates two local variables, `total` and `count` that are used to
  compute the frequency with which `y_pred` matches `y_true`. This frequency is
  ultimately returned as `categorical accuracy`: an idempotent operation that
  simply divides `total` by `count`.

  `y_pred` and `y_true` should be passed in as vectors of probabilities, rather
  than as labels. If necessary, use `tf.one_hot` to expand `y_true` as a vector.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.CategoricalAccuracy()
  >>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8],
  ...                 [0.05, 0.95, 0]])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8],
  ...                 [0.05, 0.95, 0]],
  ...                sample_weight=[0.7, 0.3])
  >>> m.result().numpy()
  0.3

  Usage with `compile()` API:

  ```python
  model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[tf.keras.metrics.CategoricalAccuracy()])
  ```
  """
    def __init__(self, name: str = 'categorical_accuracy', dtype: Incomplete | None = None) -> None: ...

class SparseCategoricalAccuracy(MeanMetricWrapper):
    """Calculates how often predictions match integer labels.

  ```python
  acc = np.dot(sample_weight, np.equal(y_true, np.argmax(y_pred, axis=1))
  ```

  You can provide logits of classes as `y_pred`, since argmax of
  logits and probabilities are same.

  This metric creates two local variables, `total` and `count` that are used to
  compute the frequency with which `y_pred` matches `y_true`. This frequency is
  ultimately returned as `sparse categorical accuracy`: an idempotent operation
  that simply divides `total` by `count`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.SparseCategoricalAccuracy()
  >>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]],
  ...                sample_weight=[0.7, 0.3])
  >>> m.result().numpy()
  0.3

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
  ```
  """
    def __init__(self, name: str = 'sparse_categorical_accuracy', dtype: Incomplete | None = None) -> None: ...

class TopKCategoricalAccuracy(MeanMetricWrapper):
    """Computes how often targets are in the top `K` predictions.

  Args:
    k: (Optional) Number of top elements to look at for computing accuracy.
      Defaults to 5.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.TopKCategoricalAccuracy(k=1)
  >>> m.update_state([[0, 0, 1], [0, 1, 0]],
  ...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([[0, 0, 1], [0, 1, 0]],
  ...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]],
  ...                sample_weight=[0.7, 0.3])
  >>> m.result().numpy()
  0.3

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.TopKCategoricalAccuracy()])
  ```
  """
    def __init__(self, k: int = 5, name: str = 'top_k_categorical_accuracy', dtype: Incomplete | None = None) -> None: ...

class SparseTopKCategoricalAccuracy(MeanMetricWrapper):
    """Computes how often integer targets are in the top `K` predictions.

  Args:
    k: (Optional) Number of top elements to look at for computing accuracy.
      Defaults to 5.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.SparseTopKCategoricalAccuracy(k=1)
  >>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]],
  ...                sample_weight=[0.7, 0.3])
  >>> m.result().numpy()
  0.3

  Usage with `compile()` API:

  ```python
  model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[tf.keras.metrics.SparseTopKCategoricalAccuracy()])
  ```
  """
    def __init__(self, k: int = 5, name: str = 'sparse_top_k_categorical_accuracy', dtype: Incomplete | None = None) -> None: ...

class _ConfusionMatrixConditionCount(Metric):
    """Calculates the number of the given confusion matrix condition.

  Args:
    confusion_matrix_cond: One of `metrics_utils.ConfusionMatrix` conditions.
    thresholds: (Optional) Defaults to 0.5. A float value or a python list/tuple
      of float threshold values in [0, 1]. A threshold is compared with
      prediction values to determine the truth value of predictions (i.e., above
      the threshold is `true`, below is `false`). One metric value is generated
      for each threshold value.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
  """
    init_thresholds: Incomplete
    thresholds: Incomplete
    accumulator: Incomplete
    def __init__(self, confusion_matrix_cond, thresholds: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates the metric statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def result(self): ...
    def reset_state(self) -> None: ...
    def get_config(self): ...

class FalsePositives(_ConfusionMatrixConditionCount):
    """Calculates the number of false positives.

  If `sample_weight` is given, calculates the sum of the weights of
  false positives. This metric creates one local variable, `accumulator`
  that is used to keep track of the number of false positives.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    thresholds: (Optional) Defaults to 0.5. A float value or a python
      list/tuple of float threshold values in [0, 1]. A threshold is compared
      with prediction values to determine the truth value of predictions
      (i.e., above the threshold is `true`, below is `false`). One metric
      value is generated for each threshold value.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.FalsePositives()
  >>> m.update_state([0, 1, 0, 0], [0, 0, 1, 1])
  >>> m.result().numpy()
  2.0

  >>> m.reset_state()
  >>> m.update_state([0, 1, 0, 0], [0, 0, 1, 1], sample_weight=[0, 0, 1, 0])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.FalsePositives()])
  ```
  """
    def __init__(self, thresholds: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...

class FalseNegatives(_ConfusionMatrixConditionCount):
    """Calculates the number of false negatives.

  If `sample_weight` is given, calculates the sum of the weights of
  false negatives. This metric creates one local variable, `accumulator`
  that is used to keep track of the number of false negatives.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    thresholds: (Optional) Defaults to 0.5. A float value or a python
      list/tuple of float threshold values in [0, 1]. A threshold is compared
      with prediction values to determine the truth value of predictions
      (i.e., above the threshold is `true`, below is `false`). One metric
      value is generated for each threshold value.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.FalseNegatives()
  >>> m.update_state([0, 1, 1, 1], [0, 1, 0, 0])
  >>> m.result().numpy()
  2.0

  >>> m.reset_state()
  >>> m.update_state([0, 1, 1, 1], [0, 1, 0, 0], sample_weight=[0, 0, 1, 0])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.FalseNegatives()])
  ```
  """
    def __init__(self, thresholds: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...

class TrueNegatives(_ConfusionMatrixConditionCount):
    """Calculates the number of true negatives.

  If `sample_weight` is given, calculates the sum of the weights of
  true negatives. This metric creates one local variable, `accumulator`
  that is used to keep track of the number of true negatives.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    thresholds: (Optional) Defaults to 0.5. A float value or a python
      list/tuple of float threshold values in [0, 1]. A threshold is compared
      with prediction values to determine the truth value of predictions
      (i.e., above the threshold is `true`, below is `false`). One metric
      value is generated for each threshold value.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.TrueNegatives()
  >>> m.update_state([0, 1, 0, 0], [1, 1, 0, 0])
  >>> m.result().numpy()
  2.0

  >>> m.reset_state()
  >>> m.update_state([0, 1, 0, 0], [1, 1, 0, 0], sample_weight=[0, 0, 1, 0])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.TrueNegatives()])
  ```
  """
    def __init__(self, thresholds: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...

class TruePositives(_ConfusionMatrixConditionCount):
    """Calculates the number of true positives.

  If `sample_weight` is given, calculates the sum of the weights of
  true positives. This metric creates one local variable, `true_positives`
  that is used to keep track of the number of true positives.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    thresholds: (Optional) Defaults to 0.5. A float value or a python
      list/tuple of float threshold values in [0, 1]. A threshold is compared
      with prediction values to determine the truth value of predictions
      (i.e., above the threshold is `true`, below is `false`). One metric
      value is generated for each threshold value.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.TruePositives()
  >>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1])
  >>> m.result().numpy()
  2.0

  >>> m.reset_state()
  >>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1], sample_weight=[0, 0, 1, 0])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.TruePositives()])
  ```
  """
    def __init__(self, thresholds: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...

class Precision(Metric):
    """Computes the precision of the predictions with respect to the labels.

  The metric creates two local variables, `true_positives` and `false_positives`
  that are used to compute the precision. This value is ultimately returned as
  `precision`, an idempotent operation that simply divides `true_positives`
  by the sum of `true_positives` and `false_positives`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  If `top_k` is set, we'll calculate precision as how often on average a class
  among the top-k classes with the highest predicted values of a batch entry is
  correct and can be found in the label for that entry.

  If `class_id` is specified, we calculate precision by considering only the
  entries in the batch for which `class_id` is above the threshold and/or in the
  top-k highest predictions, and computing the fraction of them for which
  `class_id` is indeed a correct label.

  Args:
    thresholds: (Optional) A float value or a python list/tuple of float
      threshold values in [0, 1]. A threshold is compared with prediction
      values to determine the truth value of predictions (i.e., above the
      threshold is `true`, below is `false`). One metric value is generated
      for each threshold value. If neither thresholds nor top_k are set, the
      default is to calculate precision with `thresholds=0.5`.
    top_k: (Optional) Unset by default. An int value specifying the top-k
      predictions to consider when calculating precision.
    class_id: (Optional) Integer class ID for which we want binary metrics.
      This must be in the half-open interval `[0, num_classes)`, where
      `num_classes` is the last dimension of predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Precision()
  >>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1])
  >>> m.result().numpy()
  0.6666667

  >>> m.reset_state()
  >>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1], sample_weight=[0, 0, 1, 0])
  >>> m.result().numpy()
  1.0

  >>> # With top_k=2, it will calculate precision over y_true[:2] and y_pred[:2]
  >>> m = tf.keras.metrics.Precision(top_k=2)
  >>> m.update_state([0, 0, 1, 1], [1, 1, 1, 1])
  >>> m.result().numpy()
  0.0

  >>> # With top_k=4, it will calculate precision over y_true[:4] and y_pred[:4]
  >>> m = tf.keras.metrics.Precision(top_k=4)
  >>> m.update_state([0, 0, 1, 1], [1, 1, 1, 1])
  >>> m.result().numpy()
  0.5

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.Precision()])
  ```
  """
    init_thresholds: Incomplete
    top_k: Incomplete
    class_id: Incomplete
    thresholds: Incomplete
    true_positives: Incomplete
    false_positives: Incomplete
    def __init__(self, thresholds: Incomplete | None = None, top_k: Incomplete | None = None, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates true positive and false positive statistics.

    Args:
      y_true: The ground truth values, with the same dimensions as `y_pred`.
        Will be cast to `bool`.
      y_pred: The predicted values. Each element must be in the range `[0, 1]`.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def result(self): ...
    def reset_state(self) -> None: ...
    def get_config(self): ...

class Recall(Metric):
    """Computes the recall of the predictions with respect to the labels.

  This metric creates two local variables, `true_positives` and
  `false_negatives`, that are used to compute the recall. This value is
  ultimately returned as `recall`, an idempotent operation that simply divides
  `true_positives` by the sum of `true_positives` and `false_negatives`.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  If `top_k` is set, recall will be computed as how often on average a class
  among the labels of a batch entry is in the top-k predictions.

  If `class_id` is specified, we calculate recall by considering only the
  entries in the batch for which `class_id` is in the label, and computing the
  fraction of them for which `class_id` is above the threshold and/or in the
  top-k predictions.

  Args:
    thresholds: (Optional) A float value or a python list/tuple of float
      threshold values in [0, 1]. A threshold is compared with prediction
      values to determine the truth value of predictions (i.e., above the
      threshold is `true`, below is `false`). One metric value is generated
      for each threshold value. If neither thresholds nor top_k are set, the
      default is to calculate recall with `thresholds=0.5`.
    top_k: (Optional) Unset by default. An int value specifying the top-k
      predictions to consider when calculating recall.
    class_id: (Optional) Integer class ID for which we want binary metrics.
      This must be in the half-open interval `[0, num_classes)`, where
      `num_classes` is the last dimension of predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Recall()
  >>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1])
  >>> m.result().numpy()
  0.6666667

  >>> m.reset_state()
  >>> m.update_state([0, 1, 1, 1], [1, 0, 1, 1], sample_weight=[0, 0, 1, 0])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.Recall()])
  ```
  """
    init_thresholds: Incomplete
    top_k: Incomplete
    class_id: Incomplete
    thresholds: Incomplete
    true_positives: Incomplete
    false_negatives: Incomplete
    def __init__(self, thresholds: Incomplete | None = None, top_k: Incomplete | None = None, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates true positive and false negative statistics.

    Args:
      y_true: The ground truth values, with the same dimensions as `y_pred`.
        Will be cast to `bool`.
      y_pred: The predicted values. Each element must be in the range `[0, 1]`.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def result(self): ...
    def reset_state(self) -> None: ...
    def get_config(self): ...

class SensitivitySpecificityBase(Metric, metaclass=abc.ABCMeta):
    """Abstract base class for computing sensitivity and specificity.

  For additional information about specificity and sensitivity, see
  [the following](https://en.wikipedia.org/wiki/Sensitivity_and_specificity).
  """
    value: Incomplete
    class_id: Incomplete
    true_positives: Incomplete
    true_negatives: Incomplete
    false_positives: Incomplete
    false_negatives: Incomplete
    thresholds: Incomplete
    def __init__(self, value, num_thresholds: int = 200, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates confusion matrix statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def reset_state(self) -> None: ...
    def get_config(self): ...

class SensitivityAtSpecificity(SensitivitySpecificityBase):
    """Computes best sensitivity where specificity is >= specified value.

  the sensitivity at a given specificity.

  `Sensitivity` measures the proportion of actual positives that are correctly
  identified as such (tp / (tp + fn)).
  `Specificity` measures the proportion of actual negatives that are correctly
  identified as such (tn / (tn + fp)).

  This metric creates four local variables, `true_positives`, `true_negatives`,
  `false_positives` and `false_negatives` that are used to compute the
  sensitivity at the given specificity. The threshold for the given specificity
  value is computed and used to evaluate the corresponding sensitivity.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  If `class_id` is specified, we calculate precision by considering only the
  entries in the batch for which `class_id` is above the threshold predictions,
  and computing the fraction of them for which `class_id` is indeed a correct
  label.

  For additional information about specificity and sensitivity, see
  [the following](https://en.wikipedia.org/wiki/Sensitivity_and_specificity).

  Args:
    specificity: A scalar value in range `[0, 1]`.
    num_thresholds: (Optional) Defaults to 200. The number of thresholds to
      use for matching the given specificity.
    class_id: (Optional) Integer class ID for which we want binary metrics.
      This must be in the half-open interval `[0, num_classes)`, where
      `num_classes` is the last dimension of predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.SensitivityAtSpecificity(0.5)
  >>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8],
  ...                sample_weight=[1, 1, 2, 2, 1])
  >>> m.result().numpy()
  0.333333

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.SensitivityAtSpecificity()])
  ```
  """
    specificity: Incomplete
    num_thresholds: Incomplete
    def __init__(self, specificity, num_thresholds: int = 200, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def result(self): ...
    def get_config(self): ...

class SpecificityAtSensitivity(SensitivitySpecificityBase):
    """Computes best specificity where sensitivity is >= specified value.

  `Sensitivity` measures the proportion of actual positives that are correctly
  identified as such (tp / (tp + fn)).
  `Specificity` measures the proportion of actual negatives that are correctly
  identified as such (tn / (tn + fp)).

  This metric creates four local variables, `true_positives`, `true_negatives`,
  `false_positives` and `false_negatives` that are used to compute the
  specificity at the given sensitivity. The threshold for the given sensitivity
  value is computed and used to evaluate the corresponding specificity.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  If `class_id` is specified, we calculate precision by considering only the
  entries in the batch for which `class_id` is above the threshold predictions,
  and computing the fraction of them for which `class_id` is indeed a correct
  label.

  For additional information about specificity and sensitivity, see
  [the following](https://en.wikipedia.org/wiki/Sensitivity_and_specificity).

  Args:
    sensitivity: A scalar value in range `[0, 1]`.
    num_thresholds: (Optional) Defaults to 200. The number of thresholds to
      use for matching the given sensitivity.
    class_id: (Optional) Integer class ID for which we want binary metrics.
      This must be in the half-open interval `[0, num_classes)`, where
      `num_classes` is the last dimension of predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.SpecificityAtSensitivity(0.5)
  >>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8])
  >>> m.result().numpy()
  0.66666667

  >>> m.reset_state()
  >>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8],
  ...                sample_weight=[1, 1, 2, 2, 2])
  >>> m.result().numpy()
  0.5

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.SpecificityAtSensitivity()])
  ```
  """
    sensitivity: Incomplete
    num_thresholds: Incomplete
    def __init__(self, sensitivity, num_thresholds: int = 200, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def result(self): ...
    def get_config(self): ...

class PrecisionAtRecall(SensitivitySpecificityBase):
    """Computes best precision where recall is >= specified value.

  This metric creates four local variables, `true_positives`, `true_negatives`,
  `false_positives` and `false_negatives` that are used to compute the
  precision at the given recall. The threshold for the given recall
  value is computed and used to evaluate the corresponding precision.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  If `class_id` is specified, we calculate precision by considering only the
  entries in the batch for which `class_id` is above the threshold predictions,
  and computing the fraction of them for which `class_id` is indeed a correct
  label.

  Args:
    recall: A scalar value in range `[0, 1]`.
    num_thresholds: (Optional) Defaults to 200. The number of thresholds to
      use for matching the given recall.
    class_id: (Optional) Integer class ID for which we want binary metrics.
      This must be in the half-open interval `[0, num_classes)`, where
      `num_classes` is the last dimension of predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.PrecisionAtRecall(0.5)
  >>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([0, 0, 0, 1, 1], [0, 0.3, 0.8, 0.3, 0.8],
  ...                sample_weight=[2, 2, 2, 1, 1])
  >>> m.result().numpy()
  0.33333333

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.PrecisionAtRecall(recall=0.8)])
  ```
  """
    recall: Incomplete
    num_thresholds: Incomplete
    def __init__(self, recall, num_thresholds: int = 200, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def result(self): ...
    def get_config(self): ...

class RecallAtPrecision(SensitivitySpecificityBase):
    """Computes best recall where precision is >= specified value.

  For a given score-label-distribution the required precision might not
  be achievable, in this case 0.0 is returned as recall.

  This metric creates four local variables, `true_positives`, `true_negatives`,
  `false_positives` and `false_negatives` that are used to compute the
  recall at the given precision. The threshold for the given precision
  value is computed and used to evaluate the corresponding recall.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  If `class_id` is specified, we calculate precision by considering only the
  entries in the batch for which `class_id` is above the threshold predictions,
  and computing the fraction of them for which `class_id` is indeed a correct
  label.

  Args:
    precision: A scalar value in range `[0, 1]`.
    num_thresholds: (Optional) Defaults to 200. The number of thresholds to
      use for matching the given precision.
    class_id: (Optional) Integer class ID for which we want binary metrics.
      This must be in the half-open interval `[0, num_classes)`, where
      `num_classes` is the last dimension of predictions.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.RecallAtPrecision(0.8)
  >>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9],
  ...                sample_weight=[1, 0, 0, 1])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.RecallAtPrecision(precision=0.8)])
  ```
  """
    precision: Incomplete
    num_thresholds: Incomplete
    def __init__(self, precision, num_thresholds: int = 200, class_id: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def result(self): ...
    def get_config(self): ...

class AUC(Metric):
    """Approximates the AUC (Area under the curve) of the ROC or PR curves.

  The AUC (Area under the curve) of the ROC (Receiver operating
  characteristic; default) or PR (Precision Recall) curves are quality measures
  of binary classifiers. Unlike the accuracy, and like cross-entropy
  losses, ROC-AUC and PR-AUC evaluate all the operational points of a model.

  This class approximates AUCs using a Riemann sum. During the metric
  accumulation phrase, predictions are accumulated within predefined buckets
  by value. The AUC is then computed by interpolating per-bucket averages. These
  buckets define the evaluated operational points.

  This metric creates four local variables, `true_positives`, `true_negatives`,
  `false_positives` and `false_negatives` that are used to compute the AUC.
  To discretize the AUC curve, a linearly spaced set of thresholds is used to
  compute pairs of recall and precision values. The area under the ROC-curve is
  therefore computed using the height of the recall values by the false positive
  rate, while the area under the PR-curve is the computed using the height of
  the precision values by the recall.

  This value is ultimately returned as `auc`, an idempotent operation that
  computes the area under a discretized curve of precision versus recall values
  (computed using the aforementioned variables). The `num_thresholds` variable
  controls the degree of discretization with larger numbers of thresholds more
  closely approximating the true AUC. The quality of the approximation may vary
  dramatically depending on `num_thresholds`. The `thresholds` parameter can be
  used to manually specify thresholds which split the predictions more evenly.

  For a best approximation of the real AUC, `predictions` should be distributed
  approximately uniformly in the range [0, 1] (if `from_logits=False`). The
  quality of the AUC approximation may be poor if this is not the case. Setting
  `summation_method` to 'minoring' or 'majoring' can help quantify the error in
  the approximation by providing lower or upper bound estimate of the AUC.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    num_thresholds: (Optional) Defaults to 200. The number of thresholds to
      use when discretizing the roc curve. Values must be > 1.
    curve: (Optional) Specifies the name of the curve to be computed, 'ROC'
      [default] or 'PR' for the Precision-Recall-curve.
    summation_method: (Optional) Specifies the [Riemann summation method](
        https://en.wikipedia.org/wiki/Riemann_sum) used.
        'interpolation' (default) applies mid-point summation scheme for `ROC`.
        For PR-AUC, interpolates (true/false) positives but not the ratio that
        is precision (see Davis & Goadrich 2006 for details);
        'minoring' applies left summation
        for increasing intervals and right summation for decreasing intervals;
        'majoring' does the opposite.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    thresholds: (Optional) A list of floating point values to use as the
      thresholds for discretizing the curve. If set, the `num_thresholds`
      parameter is ignored. Values should be in [0, 1]. Endpoint thresholds
      equal to {-epsilon, 1+epsilon} for a small positive epsilon value will
      be automatically included with these to correctly handle predictions
      equal to exactly 0 or 1.
    multi_label: boolean indicating whether multilabel data should be
      treated as such, wherein AUC is computed separately for each label and
      then averaged across labels, or (when False) if the data should be
      flattened into a single label before AUC computation. In the latter
      case, when multilabel data is passed to AUC, each label-prediction pair
      is treated as an individual data point. Should be set to False for
      multi-class data.
    num_labels: (Optional) The number of labels, used when `multi_label` is
      True. If `num_labels` is not specified, then state variables get created
      on the first call to `update_state`.
    label_weights: (Optional) list, array, or tensor of non-negative weights
      used to compute AUCs for multilabel data. When `multi_label` is True,
      the weights are applied to the individual label AUCs when they are
      averaged to produce the multi-label AUC. When it's False, they are used
      to weight the individual label predictions in computing the confusion
      matrix on the flattened data. Note that this is unlike class_weights in
      that class_weights weights the example depending on the value of its
      label, whereas label_weights depends only on the index of that label
      before flattening; therefore `label_weights` should not be used for
      multi-class data.
    from_logits: boolean indicating whether the predictions (`y_pred` in
      `update_state`) are probabilities or sigmoid logits. As a rule of thumb,
      when using a keras loss, the `from_logits` constructor argument of the
      loss should match the AUC `from_logits` constructor argument.

  Standalone usage:

  >>> m = tf.keras.metrics.AUC(num_thresholds=3)
  >>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9])
  >>> # threshold values are [0 - 1e-7, 0.5, 1 + 1e-7]
  >>> # tp = [2, 1, 0], fp = [2, 0, 0], fn = [0, 1, 2], tn = [0, 2, 2]
  >>> # tp_rate = recall = [1, 0.5, 0], fp_rate = [1, 0, 0]
  >>> # auc = ((((1+0.5)/2)*(1-0)) + (((0.5+0)/2)*(0-0))) = 0.75
  >>> m.result().numpy()
  0.75

  >>> m.reset_state()
  >>> m.update_state([0, 0, 1, 1], [0, 0.5, 0.3, 0.9],
  ...                sample_weight=[1, 0, 0, 1])
  >>> m.result().numpy()
  1.0

  Usage with `compile()` API:

  ```python
  # Reports the AUC of a model outputing a probability.
  model.compile(optimizer='sgd',
                loss=tf.keras.losses.BinaryCrossentropy(),
                metrics=[tf.keras.metrics.AUC()])

  # Reports the AUC of a model outputing a logit.
  model.compile(optimizer='sgd',
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=[tf.keras.metrics.AUC(from_logits=True)])
  ```
  """
    num_thresholds: Incomplete
    curve: Incomplete
    summation_method: Incomplete
    multi_label: Incomplete
    label_weights: Incomplete
    def __init__(self, num_thresholds: int = 200, curve: str = 'ROC', summation_method: str = 'interpolation', name: Incomplete | None = None, dtype: Incomplete | None = None, thresholds: Incomplete | None = None, multi_label: bool = False, num_labels: Incomplete | None = None, label_weights: Incomplete | None = None, from_logits: bool = False) -> None: ...
    @property
    def thresholds(self):
        """The thresholds used for evaluating AUC."""
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates confusion matrix statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def interpolate_pr_auc(self):
        """Interpolation formula inspired by section 4 of Davis & Goadrich 2006.

    https://www.biostat.wisc.edu/~page/rocpr.pdf

    Note here we derive & use a closed formula not present in the paper
    as follows:

      Precision = TP / (TP + FP) = TP / P

    Modeling all of TP (true positive), FP (false positive) and their sum
    P = TP + FP (predicted positive) as varying linearly within each interval
    [A, B] between successive thresholds, we get

      Precision slope = dTP / dP
                      = (TP_B - TP_A) / (P_B - P_A)
                      = (TP - TP_A) / (P - P_A)
      Precision = (TP_A + slope * (P - P_A)) / P

    The area within the interval is (slope / total_pos_weight) times

      int_A^B{Precision.dP} = int_A^B{(TP_A + slope * (P - P_A)) * dP / P}
      int_A^B{Precision.dP} = int_A^B{slope * dP + intercept * dP / P}

    where intercept = TP_A - slope * P_A = TP_B - slope * P_B, resulting in

      int_A^B{Precision.dP} = TP_B - TP_A + intercept * log(P_B / P_A)

    Bringing back the factor (slope / total_pos_weight) we'd put aside, we get

      slope * [dTP + intercept *  log(P_B / P_A)] / total_pos_weight

    where dTP == TP_B - TP_A.

    Note that when P_A == 0 the above calculation simplifies into

      int_A^B{Precision.dTP} = int_A^B{slope * dTP} = slope * (TP_B - TP_A)

    which is really equivalent to imputing constant precision throughout the
    first bucket having >0 true positives.

    Returns:
      pr_auc: an approximation of the area under the P-R curve.
    """
    def result(self): ...
    def reset_state(self) -> None: ...
    def get_config(self): ...

class CosineSimilarity(MeanMetricWrapper):
    """Computes the cosine similarity between the labels and predictions.

  `cosine similarity = (a . b) / ||a|| ||b||`

  See: [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity).

  This metric keeps the average cosine similarity between `predictions` and
  `labels` over a stream of data.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    axis: (Optional) Defaults to -1. The dimension along which the cosine
      similarity is computed.

  Standalone usage:

  >>> # l2_norm(y_true) = [[0., 1.], [1./1.414, 1./1.414]]
  >>> # l2_norm(y_pred) = [[1., 0.], [1./1.414, 1./1.414]]
  >>> # l2_norm(y_true) . l2_norm(y_pred) = [[0., 0.], [0.5, 0.5]]
  >>> # result = mean(sum(l2_norm(y_true) . l2_norm(y_pred), axis=1))
  >>> #        = ((0. + 0.) +  (0.5 + 0.5)) / 2
  >>> m = tf.keras.metrics.CosineSimilarity(axis=1)
  >>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]])
  >>> m.result().numpy()
  0.49999997

  >>> m.reset_state()
  >>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]],
  ...                sample_weight=[0.3, 0.7])
  >>> m.result().numpy()
  0.6999999

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.CosineSimilarity(axis=1)])
  ```
  """
    def __init__(self, name: str = 'cosine_similarity', dtype: Incomplete | None = None, axis: int = -1) -> None: ...

class MeanAbsoluteError(MeanMetricWrapper):
    """Computes the mean absolute error between the labels and predictions.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.MeanAbsoluteError()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  0.25

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.5

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.MeanAbsoluteError()])
  ```
  """
    def __init__(self, name: str = 'mean_absolute_error', dtype: Incomplete | None = None) -> None: ...

class MeanAbsolutePercentageError(MeanMetricWrapper):
    """Computes the mean absolute percentage error between `y_true` and `y_pred`.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.MeanAbsolutePercentageError()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  250000000.0

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  500000000.0

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.MeanAbsolutePercentageError()])
  ```
  """
    def __init__(self, name: str = 'mean_absolute_percentage_error', dtype: Incomplete | None = None) -> None: ...

class MeanSquaredError(MeanMetricWrapper):
    """Computes the mean squared error between `y_true` and `y_pred`.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.MeanSquaredError()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  0.25

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.5

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.MeanSquaredError()])
  ```
  """
    def __init__(self, name: str = 'mean_squared_error', dtype: Incomplete | None = None) -> None: ...

class MeanSquaredLogarithmicError(MeanMetricWrapper):
    """Computes the mean squared logarithmic error between `y_true` and `y_pred`.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.MeanSquaredLogarithmicError()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  0.12011322

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.24022643

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.MeanSquaredLogarithmicError()])
  ```
  """
    def __init__(self, name: str = 'mean_squared_logarithmic_error', dtype: Incomplete | None = None) -> None: ...

class Hinge(MeanMetricWrapper):
    """Computes the hinge metric between `y_true` and `y_pred`.

  `y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are
  provided we will convert them to -1 or 1.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Hinge()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
  >>> m.result().numpy()
  1.3

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  1.1

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd', loss='mse', metrics=[tf.keras.metrics.Hinge()])
  ```
  """
    def __init__(self, name: str = 'hinge', dtype: Incomplete | None = None) -> None: ...

class SquaredHinge(MeanMetricWrapper):
    """Computes the squared hinge metric between `y_true` and `y_pred`.

  `y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are
  provided we will convert them to -1 or 1.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.SquaredHinge()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
  >>> m.result().numpy()
  1.86

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  1.46

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.SquaredHinge()])
  ```
  """
    def __init__(self, name: str = 'squared_hinge', dtype: Incomplete | None = None) -> None: ...

class CategoricalHinge(MeanMetricWrapper):
    """Computes the categorical hinge metric between `y_true` and `y_pred`.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.CategoricalHinge()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
  >>> m.result().numpy()
  1.4000001

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  1.2

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.CategoricalHinge()])
  ```
  """
    def __init__(self, name: str = 'categorical_hinge', dtype: Incomplete | None = None) -> None: ...

class RootMeanSquaredError(Mean):
    """Computes root mean squared error metric between `y_true` and `y_pred`.

  Standalone usage:

  >>> m = tf.keras.metrics.RootMeanSquaredError()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  0.5

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.70710677

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.RootMeanSquaredError()])
  ```
  """
    def __init__(self, name: str = 'root_mean_squared_error', dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates root mean squared error statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def result(self): ...

class LogCoshError(MeanMetricWrapper):
    """Computes the logarithm of the hyperbolic cosine of the prediction error.

  `logcosh = log((exp(x) + exp(-x))/2)`, where x is the error (y_pred - y_true)

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.LogCoshError()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  0.10844523

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.21689045

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.LogCoshError()])
  ```
  """
    def __init__(self, name: str = 'logcosh', dtype: Incomplete | None = None) -> None: ...

class Poisson(MeanMetricWrapper):
    """Computes the Poisson metric between `y_true` and `y_pred`.

  `metric = y_pred - y_true * log(y_pred)`

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.Poisson()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
  >>> m.result().numpy()
  0.49999997

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.99999994

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.Poisson()])
  ```
  """
    def __init__(self, name: str = 'poisson', dtype: Incomplete | None = None) -> None: ...

class KLDivergence(MeanMetricWrapper):
    """Computes Kullback-Leibler divergence metric between `y_true` and `y_pred`.

  `metric = y_true * log(y_true / y_pred)`

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> m = tf.keras.metrics.KLDivergence()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
  >>> m.result().numpy()
  0.45814306

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.9162892

  Usage with `compile()` API:

  ```python
  model.compile(optimizer='sgd',
                loss='mse',
                metrics=[tf.keras.metrics.KLDivergence()])
  ```
  """
    def __init__(self, name: str = 'kullback_leibler_divergence', dtype: Incomplete | None = None) -> None: ...

class MeanIoU(Metric):
    """Computes the mean Intersection-Over-Union metric.

  Mean Intersection-Over-Union is a common evaluation metric for semantic image
  segmentation, which first computes the IOU for each semantic class and then
  computes the average over classes. IOU is defined as follows:
    IOU = true_positive / (true_positive + false_positive + false_negative).
  The predictions are accumulated in a confusion matrix, weighted by
  `sample_weight` and the metric is then calculated from it.

  If `sample_weight` is `None`, weights default to 1.
  Use `sample_weight` of 0 to mask values.

  Args:
    num_classes: The possible number of labels the prediction task can have.
      This value must be provided, since a confusion matrix of dimension =
      [num_classes, num_classes] will be allocated.
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.

  Standalone usage:

  >>> # cm = [[1, 1],
  >>> #        [1, 1]]
  >>> # sum_row = [2, 2], sum_col = [2, 2], true_positives = [1, 1]
  >>> # iou = true_positives / (sum_row + sum_col - true_positives))
  >>> # result = (1 / (2 + 2 - 1) + 1 / (2 + 2 - 1)) / 2 = 0.33
  >>> m = tf.keras.metrics.MeanIoU(num_classes=2)
  >>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1])
  >>> m.result().numpy()
  0.33333334

  >>> m.reset_state()
  >>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1],
  ...                sample_weight=[0.3, 0.3, 0.3, 0.1])
  >>> m.result().numpy()
  0.23809525

  Usage with `compile()` API:

  ```python
  model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[tf.keras.metrics.MeanIoU(num_classes=2)])
  ```
  """
    num_classes: Incomplete
    total_cm: Incomplete
    def __init__(self, num_classes, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates the confusion matrix statistics.

    Args:
      y_true: The ground truth values.
      y_pred: The predicted values.
      sample_weight: Optional weighting of each example. Defaults to 1. Can be a
        `Tensor` whose rank is either 0, or the same rank as `y_true`, and must
        be broadcastable to `y_true`.

    Returns:
      Update op.
    """
    def result(self):
        """Compute the mean intersection-over-union via the confusion matrix."""
    def reset_state(self) -> None: ...
    def get_config(self): ...

class MeanTensor(Metric):
    """Computes the element-wise (weighted) mean of the given tensors.

  `MeanTensor` returns a tensor with the same shape of the input tensors. The
  mean value is updated by keeping local variables `total` and `count`. The
  `total` tracks the sum of the weighted values, and `count` stores the sum of
  the weighted counts.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    shape: (Optional) A list of integers, a tuple of integers, or a 1-D Tensor
      of type int32. If not specified, the shape is inferred from the values at
      the first call of update_state.

  Standalone usage:

  >>> m = tf.keras.metrics.MeanTensor()
  >>> m.update_state([0, 1, 2, 3])
  >>> m.update_state([4, 5, 6, 7])
  >>> m.result().numpy()
  array([2., 3., 4., 5.], dtype=float32)

  >>> m.update_state([12, 10, 8, 6], sample_weight= [0, 0.2, 0.5, 1])
  >>> m.result().numpy()
  array([2.       , 3.6363635, 4.8      , 5.3333335], dtype=float32)

  >>> m = tf.keras.metrics.MeanTensor(dtype=tf.float64, shape=(1, 4))
  >>> m.result().numpy()
  array([[0., 0., 0., 0.]])
  >>> m.update_state([[0, 1, 2, 3]])
  >>> m.update_state([[4, 5, 6, 7]])
  >>> m.result().numpy()
  array([[2., 3., 4., 5.]])
  """
    def __init__(self, name: str = 'mean_tensor', dtype: Incomplete | None = None, shape: Incomplete | None = None) -> None: ...
    @property
    def total(self): ...
    @property
    def count(self): ...
    def update_state(self, values, sample_weight: Incomplete | None = None):
        """Accumulates statistics for computing the element-wise mean.

    Args:
      values: Per-example value.
      sample_weight: Optional weighting of each example. Defaults to 1.

    Returns:
      Update op.
    """
    def result(self): ...
    def reset_state(self) -> None: ...

class BinaryCrossentropy(MeanMetricWrapper):
    '''Computes the crossentropy metric between the labels and predictions.

  This is the crossentropy metric class to be used when there are only two
  label classes (0 and 1).

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    from_logits: (Optional )Whether output is expected to be a logits tensor.
      By default, we consider that output encodes a probability distribution.
    label_smoothing: (Optional) Float in [0, 1]. When > 0, label values are
      smoothed, meaning the confidence on label values are relaxed.
      e.g. `label_smoothing=0.2` means that we will use a value of `0.1` for
      label `0` and `0.9` for label `1`".

  Standalone usage:

  >>> m = tf.keras.metrics.BinaryCrossentropy()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
  >>> m.result().numpy()
  0.81492424

  >>> m.reset_state()
  >>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
  ...                sample_weight=[1, 0])
  >>> m.result().numpy()
  0.9162905

  Usage with `compile()` API:

  ```python
  model.compile(
      optimizer=\'sgd\',
      loss=\'mse\',
      metrics=[tf.keras.metrics.BinaryCrossentropy()])
  ```
  '''
    def __init__(self, name: str = 'binary_crossentropy', dtype: Incomplete | None = None, from_logits: bool = False, label_smoothing: int = 0) -> None: ...

class CategoricalCrossentropy(MeanMetricWrapper):
    '''Computes the crossentropy metric between the labels and predictions.

  This is the crossentropy metric class to be used when there are multiple
  label classes (2 or more). Here we assume that labels are given as a `one_hot`
  representation. eg., When labels values are [2, 0, 1],
   `y_true` = [[0, 0, 1], [1, 0, 0], [0, 1, 0]].

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    from_logits: (Optional) Whether output is expected to be a logits tensor.
      By default, we consider that output encodes a probability distribution.
    label_smoothing: (Optional) Float in [0, 1]. When > 0, label values are
      smoothed, meaning the confidence on label values are relaxed. e.g.
      `label_smoothing=0.2` means that we will use a value of `0.1` for label
      `0` and `0.9` for label `1`"

  Standalone usage:

  >>> # EPSILON = 1e-7, y = y_true, y` = y_pred
  >>> # y` = clip_ops.clip_by_value(output, EPSILON, 1. - EPSILON)
  >>> # y` = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]
  >>> # xent = -sum(y * log(y\'), axis = -1)
  >>> #      = -((log 0.95), (log 0.1))
  >>> #      = [0.051, 2.302]
  >>> # Reduced xent = (0.051 + 2.302) / 2
  >>> m = tf.keras.metrics.CategoricalCrossentropy()
  >>> m.update_state([[0, 1, 0], [0, 0, 1]],
  ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
  >>> m.result().numpy()
  1.1769392

  >>> m.reset_state()
  >>> m.update_state([[0, 1, 0], [0, 0, 1]],
  ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]],
  ...                sample_weight=tf.constant([0.3, 0.7]))
  >>> m.result().numpy()
  1.6271976

  Usage with `compile()` API:

  ```python
  model.compile(
    optimizer=\'sgd\',
    loss=\'mse\',
    metrics=[tf.keras.metrics.CategoricalCrossentropy()])
  ```
  '''
    def __init__(self, name: str = 'categorical_crossentropy', dtype: Incomplete | None = None, from_logits: bool = False, label_smoothing: int = 0) -> None: ...

class SparseCategoricalCrossentropy(MeanMetricWrapper):
    """Computes the crossentropy metric between the labels and predictions.

  Use this crossentropy metric when there are two or more label classes.
  We expect labels to be provided as integers. If you want to provide labels
  using `one-hot` representation, please use `CategoricalCrossentropy` metric.
  There should be `# classes` floating point values per feature for `y_pred`
  and a single floating point value per feature for `y_true`.

  In the snippet below, there is a single floating point value per example for
  `y_true` and `# classes` floating pointing values per example for `y_pred`.
  The shape of `y_true` is `[batch_size]` and the shape of `y_pred` is
  `[batch_size, num_classes]`.

  Args:
    name: (Optional) string name of the metric instance.
    dtype: (Optional) data type of the metric result.
    from_logits: (Optional) Whether output is expected to be a logits tensor.
      By default, we consider that output encodes a probability distribution.
    axis: (Optional) Defaults to -1. The dimension along which the metric is
      computed.

  Standalone usage:

  >>> # y_true = one_hot(y_true) = [[0, 1, 0], [0, 0, 1]]
  >>> # logits = log(y_pred)
  >>> # softmax = exp(logits) / sum(exp(logits), axis=-1)
  >>> # softmax = [[0.05, 0.95, EPSILON], [0.1, 0.8, 0.1]]
  >>> # xent = -sum(y * log(softmax), 1)
  >>> # log(softmax) = [[-2.9957, -0.0513, -16.1181],
  >>> #                [-2.3026, -0.2231, -2.3026]]
  >>> # y_true * log(softmax) = [[0, -0.0513, 0], [0, 0, -2.3026]]
  >>> # xent = [0.0513, 2.3026]
  >>> # Reduced xent = (0.0513 + 2.3026) / 2
  >>> m = tf.keras.metrics.SparseCategoricalCrossentropy()
  >>> m.update_state([1, 2],
  ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]])
  >>> m.result().numpy()
  1.1769392

  >>> m.reset_state()
  >>> m.update_state([1, 2],
  ...                [[0.05, 0.95, 0], [0.1, 0.8, 0.1]],
  ...                sample_weight=tf.constant([0.3, 0.7]))
  >>> m.result().numpy()
  1.6271976

  Usage with `compile()` API:

  ```python
  model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[tf.keras.metrics.SparseCategoricalCrossentropy()])
  ```
  """
    def __init__(self, name: str = 'sparse_categorical_crossentropy', dtype: Incomplete | None = None, from_logits: bool = False, axis: int = -1) -> None: ...

class SumOverBatchSize(Reduce):
    """Computes the weighted sum over batch size of the given values.

  For example, if values is [1, 3, 5, 7] then the metric value is 4.
  If the weights were specified as [1, 1, 0, 0] then the value would be 1.

  This metric creates two variables, `total` and `count` that are used to
  compute the average of `values`. This average is ultimately returned as sum
  over batch size which is an idempotent operation that simply divides `total`
  by `count`.

  If `sample_weight` is `None`, weights default to 1.  Use `sample_weight` of 0
  to mask values.
  """
    def __init__(self, name: str = 'sum_over_batch_size', dtype: Incomplete | None = None) -> None: ...

class SumOverBatchSizeMetricWrapper(SumOverBatchSize):
    """Wraps a function with the `SumOverBatchSizeMetricWrapper` metric."""
    def __init__(self, fn, name: Incomplete | None = None, dtype: Incomplete | None = None, **kwargs) -> None:
        """Creates a `SumOverBatchSizeMetricWrapper` instance.

    Args:
      fn: The metric function to wrap, with signature `fn(y_true, y_pred,
        **kwargs)`.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      **kwargs: The keyword arguments that are passed on to `fn`.
    """
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None): ...
    def get_config(self): ...

def accuracy(y_true, y_pred): ...
def binary_accuracy(y_true, y_pred, threshold: float = 0.5):
    """Calculates how often predictions match binary labels.

  Standalone usage:
  >>> y_true = [[1], [1], [0], [0]]
  >>> y_pred = [[1], [1], [0], [0]]
  >>> m = tf.keras.metrics.binary_accuracy(y_true, y_pred)
  >>> assert m.shape == (4,)
  >>> m.numpy()
  array([1., 1., 1., 1.], dtype=float32)

  Args:
    y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
    y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
    threshold: (Optional) Float representing the threshold for deciding whether
      prediction values are 1 or 0.

  Returns:
    Binary accuracy values. shape = `[batch_size, d0, .. dN-1]`
  """
def categorical_accuracy(y_true, y_pred):
    """Calculates how often predictions match one-hot labels.

  Standalone usage:
  >>> y_true = [[0, 0, 1], [0, 1, 0]]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.categorical_accuracy(y_true, y_pred)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([0., 1.], dtype=float32)

  You can provide logits of classes as `y_pred`, since argmax of
  logits and probabilities are same.

  Args:
    y_true: One-hot ground truth values.
    y_pred: The prediction values.

  Returns:
    Categorical accuracy values.
  """
def sparse_categorical_accuracy(y_true, y_pred):
    """Calculates how often predictions match integer labels.

  Standalone usage:
  >>> y_true = [2, 1]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.sparse_categorical_accuracy(y_true, y_pred)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([0., 1.], dtype=float32)

  You can provide logits of classes as `y_pred`, since argmax of
  logits and probabilities are same.

  Args:
    y_true: Integer ground truth values.
    y_pred: The prediction values.

  Returns:
    Sparse categorical accuracy values.
  """
def top_k_categorical_accuracy(y_true, y_pred, k: int = 5):
    """Computes how often targets are in the top `K` predictions.

  Standalone usage:
  >>> y_true = [[0, 0, 1], [0, 1, 0]]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.top_k_categorical_accuracy(y_true, y_pred, k=3)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([1., 1.], dtype=float32)

  Args:
    y_true: The ground truth values.
    y_pred: The prediction values.
    k: (Optional) Number of top elements to look at for computing accuracy.
      Defaults to 5.

  Returns:
    Top K categorical accuracy value.
  """
def sparse_top_k_categorical_accuracy(y_true, y_pred, k: int = 5):
    """Computes how often integer targets are in the top `K` predictions.

  Standalone usage:
  >>> y_true = [2, 1]
  >>> y_pred = [[0.1, 0.9, 0.8], [0.05, 0.95, 0]]
  >>> m = tf.keras.metrics.sparse_top_k_categorical_accuracy(
  ...     y_true, y_pred, k=3)
  >>> assert m.shape == (2,)
  >>> m.numpy()
  array([1., 1.], dtype=float32)

  Args:
    y_true: tensor of true targets.
    y_pred: tensor of predicted targets.
    k: (Optional) Number of top elements to look at for computing accuracy.
      Defaults to 5.

  Returns:
    Sparse top K categorical accuracy value.
  """
def cosine_proximity(y_true, y_pred, axis: int = -1):
    """Computes the cosine similarity between labels and predictions.

  Args:
    y_true: The ground truth values.
    y_pred: The prediction values.
    axis: (Optional) Defaults to -1. The dimension along which the cosine
      similarity is computed.

  Returns:
    Cosine similarity value.
  """
acc = accuracy
ACC = accuracy
bce = binary_crossentropy
BCE = binary_crossentropy
mse = mean_squared_error
MSE = mean_squared_error
mae = mean_absolute_error
MAE = mean_absolute_error
mape = mean_absolute_percentage_error
MAPE = mean_absolute_percentage_error
msle = mean_squared_logarithmic_error
MSLE = mean_squared_logarithmic_error
cosine_similarity = cosine_proximity
log_cosh = logcosh

def clone_metric(metric):
    """Returns a clone of the metric if stateful, otherwise returns it as is."""
def clone_metrics(metrics):
    """Clones the given metric list/dict."""
def serialize(metric):
    """Serializes metric function or `Metric` instance.

  Args:
    metric: A Keras `Metric` instance or a metric function.

  Returns:
    Metric configuration dictionary.
  """
def deserialize(config, custom_objects: Incomplete | None = None):
    """Deserializes a serialized metric class/function instance.

  Args:
    config: Metric configuration.
    custom_objects: Optional dictionary mapping names (strings) to custom
      objects (classes and functions) to be considered during deserialization.

  Returns:
      A Keras `Metric` instance or a metric function.
  """
def get(identifier):
    '''Retrieves a Keras metric as a `function`/`Metric` class instance.

  The `identifier` may be the string name of a metric function or class.

  >>> metric = tf.keras.metrics.get("categorical_crossentropy")
  >>> type(metric)
  <class \'function\'>
  >>> metric = tf.keras.metrics.get("CategoricalCrossentropy")
  >>> type(metric)
  <class \'...keras.metrics.CategoricalCrossentropy\'>

  You can also specify `config` of the metric to this function by passing dict
  containing `class_name` and `config` as an identifier. Also note that the
  `class_name` must map to a `Metric` class

  >>> identifier = {"class_name": "CategoricalCrossentropy",
  ...               "config": {"from_logits": True}}
  >>> metric = tf.keras.metrics.get(identifier)
  >>> type(metric)
  <class \'...keras.metrics.CategoricalCrossentropy\'>

  Args:
    identifier: A metric identifier. One of None or string name of a metric
      function/class or metric configuration dictionary or a metric function or
      a metric class instance

  Returns:
    A Keras metric as a `function`/ `Metric` class instance.

  Raises:
    ValueError: If `identifier` cannot be interpreted.
  '''
def is_built_in(cls): ...
