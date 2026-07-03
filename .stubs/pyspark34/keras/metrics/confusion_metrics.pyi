import abc
from _typeshed import Incomplete
from keras import activations as activations, backend as backend
from keras.metrics import base_metric as base_metric
from keras.utils import metrics_utils as metrics_utils
from keras.utils.generic_utils import to_list as to_list
from keras.utils.tf_utils import is_tensor_or_variable as is_tensor_or_variable

class _ConfusionMatrixConditionCount(base_metric.Metric):
    """Calculates the number of the given confusion matrix condition.

    Args:
      confusion_matrix_cond: One of `metrics_utils.ConfusionMatrix` conditions.
      thresholds: (Optional) Defaults to 0.5. A float value or a python
        list/tuple of float threshold values in [0, 1]. A threshold is compared
        with prediction values to determine the truth value of predictions
        (i.e., above the threshold is `true`, below is `false`). One metric
        value is generated for each threshold value.
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
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

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
      thresholds: (Optional) Defaults to 0.5. A float value, or a Python
        list/tuple of float threshold values in [0, 1]. A threshold is compared
        with prediction values to determine the truth value of predictions
        (i.e., above the threshold is `true`, below is `false`). If used with a
        loss function that sets `from_logits=True` (i.e. no sigmoid applied to
        predictions), `thresholds` should be set to 0. One metric value is
        generated for each threshold value.
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

    Usage with a loss with `from_logits=True`:

    ```python
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.FalsePositives(thresholds=0)])
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
      thresholds: (Optional) Defaults to 0.5. A float value, or a Python
        list/tuple of float threshold values in [0, 1]. A threshold is compared
        with prediction values to determine the truth value of predictions
        (i.e., above the threshold is `true`, below is `false`). If used with a
        loss function that sets `from_logits=True` (i.e. no sigmoid applied to
        predictions), `thresholds` should be set to 0. One metric value is
        generated for each threshold value.
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

    Usage with a loss with `from_logits=True`:

    ```python
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.FalseNegatives(thresholds=0)])
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
      thresholds: (Optional) Defaults to 0.5. A float value, or a Python
        list/tuple of float threshold values in [0, 1]. A threshold is compared
        with prediction values to determine the truth value of predictions
        (i.e., above the threshold is `true`, below is `false`). If used with a
        loss function that sets `from_logits=True` (i.e. no sigmoid applied to
        predictions), `thresholds` should be set to 0. One metric value is
        generated for each threshold value.
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

    Usage with a loss with `from_logits=True`:

    ```python
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.TrueNegatives(thresholds=0)])
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
      thresholds: (Optional) Defaults to 0.5. A float value, or a Python
        list/tuple of float threshold values in [0, 1]. A threshold is compared
        with prediction values to determine the truth value of predictions
        (i.e., above the threshold is `true`, below is `false`). If used with a
        loss function that sets `from_logits=True` (i.e. no sigmoid applied to
        predictions), `thresholds` should be set to 0. One metric value is
        generated for each threshold value.
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

    Usage with a loss with `from_logits=True`:

    ```python
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.TruePositives(thresholds=0)])
    ```
    """
    def __init__(self, thresholds: Incomplete | None = None, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...

class Precision(base_metric.Metric):
    """Computes the precision of the predictions with respect to the labels.

    The metric creates two local variables, `true_positives` and
    `false_positives` that are used to compute the precision. This value is
    ultimately returned as `precision`, an idempotent operation that simply
    divides `true_positives` by the sum of `true_positives` and
    `false_positives`.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    If `top_k` is set, we'll calculate precision as how often on average a class
    among the top-k classes with the highest predicted values of a batch entry
    is correct and can be found in the label for that entry.

    If `class_id` is specified, we calculate precision by considering only the
    entries in the batch for which `class_id` is above the threshold and/or in
    the top-k highest predictions, and computing the fraction of them for which
    `class_id` is indeed a correct label.

    Args:
      thresholds: (Optional) A float value, or a Python list/tuple of float
        threshold values in [0, 1]. A threshold is compared with prediction
        values to determine the truth value of predictions (i.e., above the
        threshold is `true`, below is `false`). If used with a loss function
        that sets `from_logits=True` (i.e. no sigmoid applied to predictions),
        `thresholds` should be set to 0. One metric value is generated for each
        threshold value. If neither thresholds nor top_k are set, the default is
        to calculate precision with `thresholds=0.5`.
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

    >>> # With top_k=2, it will calculate precision over y_true[:2]
    >>> # and y_pred[:2]
    >>> m = tf.keras.metrics.Precision(top_k=2)
    >>> m.update_state([0, 0, 1, 1], [1, 1, 1, 1])
    >>> m.result().numpy()
    0.0

    >>> # With top_k=4, it will calculate precision over y_true[:4]
    >>> # and y_pred[:4]
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

    Usage with a loss with `from_logits=True`:

    ```python
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.Precision(thresholds=0)])
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
          y_pred: The predicted values. Each element must be in the range
            `[0, 1]`.
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

        Returns:
          Update op.
        """
    def result(self): ...
    def reset_state(self) -> None: ...
    def get_config(self): ...

class Recall(base_metric.Metric):
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
      thresholds: (Optional) A float value, or a Python list/tuple of float
        threshold values in [0, 1]. A threshold is compared with prediction
        values to determine the truth value of predictions (i.e., above the
        threshold is `true`, below is `false`). If used with a loss function
        that sets `from_logits=True` (i.e. no sigmoid applied to predictions),
        `thresholds` should be set to 0. One metric value is generated for each
        threshold value. If neither thresholds nor top_k are set, the default is
        to calculate recall with `thresholds=0.5`.
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

    Usage with a loss with `from_logits=True`:

    ```python
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.Recall(thresholds=0)])
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
          y_pred: The predicted values. Each element must be in the range
            `[0, 1]`.
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

        Returns:
          Update op.
        """
    def result(self): ...
    def reset_state(self) -> None: ...
    def get_config(self): ...

class SensitivitySpecificityBase(base_metric.Metric, metaclass=abc.ABCMeta):
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
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

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

    This metric creates four local variables, `true_positives`,
    `true_negatives`, `false_positives` and `false_negatives` that are used to
    compute the sensitivity at the given specificity. The threshold for the
    given specificity value is computed and used to evaluate the corresponding
    sensitivity.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    If `class_id` is specified, we calculate precision by considering only the
    entries in the batch for which `class_id` is above the threshold
    predictions, and computing the fraction of them for which `class_id` is
    indeed a correct label.

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

    This metric creates four local variables, `true_positives`,
    `true_negatives`, `false_positives` and `false_negatives` that are used to
    compute the specificity at the given sensitivity. The threshold for the
    given sensitivity value is computed and used to evaluate the corresponding
    specificity.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    If `class_id` is specified, we calculate precision by considering only the
    entries in the batch for which `class_id` is above the threshold
    predictions, and computing the fraction of them for which `class_id` is
    indeed a correct label.

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

    This metric creates four local variables, `true_positives`,
    `true_negatives`, `false_positives` and `false_negatives` that are used to
    compute the precision at the given recall. The threshold for the given
    recall value is computed and used to evaluate the corresponding precision.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    If `class_id` is specified, we calculate precision by considering only the
    entries in the batch for which `class_id` is above the threshold
    predictions, and computing the fraction of them for which `class_id` is
    indeed a correct label.

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

    This metric creates four local variables, `true_positives`,
    `true_negatives`, `false_positives` and `false_negatives` that are used to
    compute the recall at the given precision. The threshold for the given
    precision value is computed and used to evaluate the corresponding recall.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    If `class_id` is specified, we calculate precision by considering only the
    entries in the batch for which `class_id` is above the threshold
    predictions, and computing the fraction of them for which `class_id` is
    indeed a correct label.

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

class AUC(base_metric.Metric):
    """Approximates the AUC (Area under the curve) of the ROC or PR curves.

    The AUC (Area under the curve) of the ROC (Receiver operating
    characteristic; default) or PR (Precision Recall) curves are quality
    measures of binary classifiers. Unlike the accuracy, and like cross-entropy
    losses, ROC-AUC and PR-AUC evaluate all the operational points of a model.

    This class approximates AUCs using a Riemann sum. During the metric
    accumulation phrase, predictions are accumulated within predefined buckets
    by value. The AUC is then computed by interpolating per-bucket averages.
    These buckets define the evaluated operational points.

    This metric creates four local variables, `true_positives`,
    `true_negatives`, `false_positives` and `false_negatives` that are used to
    compute the AUC.  To discretize the AUC curve, a linearly spaced set of
    thresholds is used to compute pairs of recall and precision values. The area
    under the ROC-curve is therefore computed using the height of the recall
    values by the false positive rate, while the area under the PR-curve is the
    computed using the height of the precision values by the recall.

    This value is ultimately returned as `auc`, an idempotent operation that
    computes the area under a discretized curve of precision versus recall
    values (computed using the aforementioned variables). The `num_thresholds`
    variable controls the degree of discretization with larger numbers of
    thresholds more closely approximating the true AUC. The quality of the
    approximation may vary dramatically depending on `num_thresholds`. The
    `thresholds` parameter can be used to manually specify thresholds which
    split the predictions more evenly.

    For a best approximation of the real AUC, `predictions` should be
    distributed approximately uniformly in the range [0, 1] (if
    `from_logits=False`). The quality of the AUC approximation may be poor if
    this is not the case. Setting `summation_method` to 'minoring' or 'majoring'
    can help quantify the error in the approximation by providing lower or upper
    bound estimate of the AUC.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    Args:
      num_thresholds: (Optional) Defaults to 200. The number of thresholds to
        use when discretizing the roc curve. Values must be > 1.
      curve: (Optional) Specifies the name of the curve to be computed, 'ROC'
        [default] or 'PR' for the Precision-Recall-curve.
      summation_method: (Optional) Specifies the [Riemann summation method](
          https://en.wikipedia.org/wiki/Riemann_sum) used.
          'interpolation' (default) applies mid-point summation scheme for
          `ROC`.  For PR-AUC, interpolates (true/false) positives but not the
          ratio that is precision (see Davis & Goadrich 2006 for details);
          'minoring' applies left summation for increasing intervals and right
          summation for decreasing intervals; 'majoring' does the opposite.
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
    # Reports the AUC of a model outputting a probability.
    model.compile(optimizer='sgd',
                  loss=tf.keras.losses.BinaryCrossentropy(),
                  metrics=[tf.keras.metrics.AUC()])

    # Reports the AUC of a model outputting a logit.
    model.compile(optimizer='sgd',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=[tf.keras.metrics.AUC(from_logits=True)])
    ```
    """
    num_thresholds: Incomplete
    curve: Incomplete
    summation_method: Incomplete
    multi_label: Incomplete
    num_labels: Incomplete
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
          sample_weight: Optional weighting of each example. Defaults to 1. Can
            be a `Tensor` whose rank is either 0, or the same rank as `y_true`,
            and must be broadcastable to `y_true`.

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
        P = TP + FP (predicted positive) as varying linearly within each
        interval [A, B] between successive thresholds, we get

          Precision slope = dTP / dP
                          = (TP_B - TP_A) / (P_B - P_A)
                          = (TP - TP_A) / (P - P_A)
          Precision = (TP_A + slope * (P - P_A)) / P

        The area within the interval is (slope / total_pos_weight) times

          int_A^B{Precision.dP} = int_A^B{(TP_A + slope * (P - P_A)) * dP / P}
          int_A^B{Precision.dP} = int_A^B{slope * dP + intercept * dP / P}

        where intercept = TP_A - slope * P_A = TP_B - slope * P_B, resulting in

          int_A^B{Precision.dP} = TP_B - TP_A + intercept * log(P_B / P_A)

        Bringing back the factor (slope / total_pos_weight) we'd put aside, we
        get

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
