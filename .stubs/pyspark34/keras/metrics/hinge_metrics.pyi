from _typeshed import Incomplete
from keras.losses import categorical_hinge as categorical_hinge, hinge as hinge, squared_hinge as squared_hinge
from keras.metrics import base_metric as base_metric

class Hinge(base_metric.MeanMetricWrapper):
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
    model.compile(
        optimizer='sgd', loss='mse', metrics=[tf.keras.metrics.Hinge()])
    ```
    """
    def __init__(self, name: str = 'hinge', dtype: Incomplete | None = None) -> None: ...

class SquaredHinge(base_metric.MeanMetricWrapper):
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

class CategoricalHinge(base_metric.MeanMetricWrapper):
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
