from _typeshed import Incomplete
from keras import backend as backend
from keras.losses import logcosh as logcosh, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_squared_error as mean_squared_error, mean_squared_logarithmic_error as mean_squared_logarithmic_error
from keras.metrics import base_metric as base_metric
from keras.utils import losses_utils as losses_utils, metrics_utils as metrics_utils
from keras.utils.tf_utils import is_tensor_or_variable as is_tensor_or_variable

class MeanRelativeError(base_metric.Mean):
    """Computes the mean relative error by normalizing with the given values.

    This metric creates two local variables, `total` and `count` that are used
    to compute the mean relative error. This is weighted by `sample_weight`, and
    it is ultimately returned as `mean_relative_error`: an idempotent operation
    that simply divides `total` by `count`.

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
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

        Returns:
          Update op.
        """
    def get_config(self): ...

class CosineSimilarity(base_metric.MeanMetricWrapper):
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

class MeanAbsoluteError(base_metric.MeanMetricWrapper):
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

class MeanAbsolutePercentageError(base_metric.MeanMetricWrapper):
    """Computes the mean absolute percentage error between `y_true` and
    `y_pred`.

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

class MeanSquaredError(base_metric.MeanMetricWrapper):
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

class MeanSquaredLogarithmicError(base_metric.MeanMetricWrapper):
    """Computes the mean squared logarithmic error between `y_true` and
    `y_pred`.

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

class RootMeanSquaredError(base_metric.Mean):
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
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

        Returns:
          Update op.
        """
    def result(self): ...

class LogCoshError(base_metric.MeanMetricWrapper):
    """Computes the logarithm of the hyperbolic cosine of the prediction error.

    `logcosh = log((exp(x) + exp(-x))/2)`, where x is the error (y_pred -
    y_true)

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

def cosine_similarity(y_true, y_pred, axis: int = -1):
    """Computes the cosine similarity between labels and predictions.

    Args:
      y_true: The ground truth values.
      y_pred: The prediction values.
      axis: (Optional) Defaults to -1. The dimension along which the cosine
        similarity is computed.

    Returns:
      Cosine similarity value.
    """
