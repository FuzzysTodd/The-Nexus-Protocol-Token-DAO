from _typeshed import Incomplete
from keras import backend as backend
from keras.metrics import base_metric as base_metric
from keras.utils import metrics_utils as metrics_utils

class Accuracy(base_metric.MeanMetricWrapper):
    """Calculates how often predictions equal labels.

    This metric creates two local variables, `total` and `count` that are used
    to compute the frequency with which `y_pred` matches `y_true`. This
    frequency is ultimately returned as `binary accuracy`: an idempotent
    operation that simply divides `total` by `count`.

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

class BinaryAccuracy(base_metric.MeanMetricWrapper):
    """Calculates how often predictions match binary labels.

    This metric creates two local variables, `total` and `count` that are used
    to compute the frequency with which `y_pred` matches `y_true`. This
    frequency is ultimately returned as `binary accuracy`: an idempotent
    operation that simply divides `total` by `count`.

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

class CategoricalAccuracy(base_metric.MeanMetricWrapper):
    """Calculates how often predictions match one-hot labels.

    You can provide logits of classes as `y_pred`, since argmax of
    logits and probabilities are same.

    This metric creates two local variables, `total` and `count` that are used
    to compute the frequency with which `y_pred` matches `y_true`. This
    frequency is ultimately returned as `categorical accuracy`: an idempotent
    operation that simply divides `total` by `count`.

    `y_pred` and `y_true` should be passed in as vectors of probabilities,
    rather than as labels. If necessary, use `tf.one_hot` to expand `y_true` as
    a vector.

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

class SparseCategoricalAccuracy(base_metric.MeanMetricWrapper):
    """Calculates how often predictions match integer labels.

    ```python
    acc = np.dot(sample_weight, np.equal(y_true, np.argmax(y_pred, axis=1))
    ```

    You can provide logits of classes as `y_pred`, since argmax of
    logits and probabilities are same.

    This metric creates two local variables, `total` and `count` that are used
    to compute the frequency with which `y_pred` matches `y_true`. This
    frequency is ultimately returned as `sparse categorical accuracy`: an
    idempotent operation that simply divides `total` by `count`.

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

class TopKCategoricalAccuracy(base_metric.MeanMetricWrapper):
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

class SparseTopKCategoricalAccuracy(base_metric.MeanMetricWrapper):
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
      threshold: (Optional) Float representing the threshold for deciding
        whether prediction values are 1 or 0.

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
