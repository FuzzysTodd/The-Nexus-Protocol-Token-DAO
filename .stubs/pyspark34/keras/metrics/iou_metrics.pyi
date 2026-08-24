import abc
import tensorflow.compat.v2 as tf
from _typeshed import Incomplete
from keras import backend as backend
from keras.metrics import base_metric as base_metric
from typing import List, Tuple

class _IoUBase(base_metric.Metric, metaclass=abc.ABCMeta):
    '''Computes the confusion matrix for Intersection-Over-Union metrics.

    Intersection-Over-Union is a common evaluation metric for semantic image
    segmentation.

    For an individual class, the IoU metric is defined as follows:

    ```
    iou = true_positives / (true_positives + false_positives + false_negatives)
    ```

    From IoUs of individual classes, the MeanIoU can be computed as the mean of
    the individual IoUs.

    To compute IoUs, the predictions are accumulated in a confusion matrix,
    weighted by `sample_weight` and the metric is then calculated from it.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    Args:
      num_classes: The possible number of labels the prediction task can have.
        This value must be provided, since a confusion matrix of size
        `(num_classes, num_classes)` will be allocated.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      ignore_class: Optional integer. The ID of a class to be ignored during
        metric computation. This is useful, for example, in segmentation
        problems featuring a "void" class (commonly -1 or 255) in segmentation
        maps. By default (`ignore_class=None`), all classes are considered.
      sparse_y_true: Whether labels are encoded using integers or
        dense floating point vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      sparse_y_pred: Whether predictions are encoded using integers or
        dense floating point vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      axis: (Optional) Defaults to -1. The dimension containing the logits.
    '''
    num_classes: Incomplete
    ignore_class: Incomplete
    sparse_y_true: Incomplete
    sparse_y_pred: Incomplete
    axis: Incomplete
    total_cm: Incomplete
    def __init__(self, num_classes: int, name: str | None = None, dtype: str | tf.dtypes.DType | None = None, ignore_class: int | None = None, sparse_y_true: bool = True, sparse_y_pred: bool = True, axis: int = -1) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates the confusion matrix statistics.

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

class IoU(_IoUBase):
    '''Computes the Intersection-Over-Union metric for specific target classes.

    General definition and computation:

    Intersection-Over-Union is a common evaluation metric for semantic image
    segmentation.

    For an individual class, the IoU metric is defined as follows:

    ```
    iou = true_positives / (true_positives + false_positives + false_negatives)
    ```

    To compute IoUs, the predictions are accumulated in a confusion matrix,
    weighted by `sample_weight` and the metric is then calculated from it.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    Note, this class first computes IoUs for all individual classes, then
    returns the mean of IoUs for the classes that are specified by
    `target_class_ids`. If `target_class_ids` has only one id value, the IoU of
    that specific class is returned.

    Args:
      num_classes: The possible number of labels the prediction task can have.
        A confusion matrix of dimension = [num_classes, num_classes] will be
        allocated to accumulate predictions from which the metric is calculated.
      target_class_ids: A tuple or list of target class ids for which the metric
        is returned. To compute IoU for a specific class, a list (or tuple) of a
        single id value should be provided.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      ignore_class: Optional integer. The ID of a class to be ignored during
        metric computation. This is useful, for example, in segmentation
        problems featuring a "void" class (commonly -1 or 255) in segmentation
        maps. By default (`ignore_class=None`), all classes are considered.
      sparse_y_true: Whether labels are encoded using integers or
        dense floating point vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      sparse_y_pred: Whether predictions are encoded using integers or
        dense floating point vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      axis: (Optional) Defaults to -1. The dimension containing the logits.

    Standalone usage:

    >>> # cm = [[1, 1],
    >>> #        [1, 1]]
    >>> # sum_row = [2, 2], sum_col = [2, 2], true_positives = [1, 1]
    >>> # iou = true_positives / (sum_row + sum_col - true_positives))
    >>> # iou = [0.33, 0.33]
    >>> m = tf.keras.metrics.IoU(num_classes=2, target_class_ids=[0])
    >>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1])
    >>> m.result().numpy()
    0.33333334

    >>> m.reset_state()
    >>> m.update_state([0, 0, 1, 1], [0, 1, 0, 1],
    ...                sample_weight=[0.3, 0.3, 0.3, 0.1])
    >>> # cm = [[0.3, 0.3],
    >>> #        [0.3, 0.1]]
    >>> # sum_row = [0.6, 0.4], sum_col = [0.6, 0.4],
    >>> # true_positives = [0.3, 0.1]
    >>> # iou = [0.33, 0.14]
    >>> m.result().numpy()
    0.33333334

    Usage with `compile()` API:

    ```python
    model.compile(
      optimizer=\'sgd\',
      loss=\'mse\',
      metrics=[tf.keras.metrics.IoU(num_classes=2, target_class_ids=[0])])
    ```
    '''
    target_class_ids: Incomplete
    def __init__(self, num_classes: int, target_class_ids: List[int] | Tuple[int, ...], name: str | None = None, dtype: str | tf.dtypes.DType | None = None, ignore_class: int | None = None, sparse_y_true: bool = True, sparse_y_pred: bool = True, axis: int = -1) -> None: ...
    def result(self):
        """Compute the intersection-over-union via the confusion matrix."""
    def get_config(self): ...

class BinaryIoU(IoU):
    """Computes the Intersection-Over-Union metric for class 0 and/or 1.

    General definition and computation:

    Intersection-Over-Union is a common evaluation metric for semantic image
    segmentation.

    For an individual class, the IoU metric is defined as follows:

    ```
    iou = true_positives / (true_positives + false_positives + false_negatives)
    ```

    To compute IoUs, the predictions are accumulated in a confusion matrix,
    weighted by `sample_weight` and the metric is then calculated from it.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    This class can be used to compute IoUs for a binary classification task
    where the predictions are provided as logits. First a `threshold` is applied
    to the predicted values such that those that are below the `threshold` are
    converted to class 0 and those that are above the `threshold` are converted
    to class 1.

    IoUs for classes 0 and 1 are then computed, the mean of IoUs for the classes
    that are specified by `target_class_ids` is returned.

    Note: with `threshold=0`, this metric has the same behavior as `IoU`.

    Args:
      target_class_ids: A tuple or list of target class ids for which the metric
        is returned. Options are `[0]`, `[1]`, or `[0, 1]`. With `[0]` (or
        `[1]`), the IoU metric for class 0 (or class 1, respectively) is
        returned. With `[0, 1]`, the mean of IoUs for the two classes is
        returned.
      threshold: A threshold that applies to the prediction logits to convert
        them to either predicted class 0 if the logit is below `threshold` or
        predicted class 1 if the logit is above `threshold`.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.

    Standalone usage:

    >>> m = tf.keras.metrics.BinaryIoU(target_class_ids=[0, 1], threshold=0.3)
    >>> m.update_state([0, 1, 0, 1], [0.1, 0.2, 0.4, 0.7])
    >>> m.result().numpy()
    0.33333334

    >>> m.reset_state()
    >>> m.update_state([0, 1, 0, 1], [0.1, 0.2, 0.4, 0.7],
    ...                sample_weight=[0.2, 0.3, 0.4, 0.1])
    >>> # cm = [[0.2, 0.4],
    >>> #        [0.3, 0.1]]
    >>> # sum_row = [0.6, 0.4], sum_col = [0.5, 0.5],
    >>> # true_positives = [0.2, 0.1]
    >>> # iou = [0.222, 0.125]
    >>> m.result().numpy()
    0.17361112

    Usage with `compile()` API:

    ```python
    model.compile(
      optimizer='sgd',
      loss='mse',
      metrics=[tf.keras.metrics.BinaryIoU(target_class_ids=[0], threshold=0.5)])
    ```
    """
    threshold: Incomplete
    def __init__(self, target_class_ids: List[int] | Tuple[int, ...] = (0, 1), threshold: float = 0.5, name: Incomplete | None = None, dtype: Incomplete | None = None) -> None: ...
    def update_state(self, y_true, y_pred, sample_weight: Incomplete | None = None):
        """Accumulates the confusion matrix statistics.

        Before the confusion matrix is updated, the predicted values are
        thresholded to be:
          0 for values that are smaller than the `threshold`
          1 for values that are larger or equal to the `threshold`

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

class MeanIoU(IoU):
    '''Computes the mean Intersection-Over-Union metric.

    General definition and computation:

    Intersection-Over-Union is a common evaluation metric for semantic image
    segmentation.

    For an individual class, the IoU metric is defined as follows:

    ```
    iou = true_positives / (true_positives + false_positives + false_negatives)
    ```

    To compute IoUs, the predictions are accumulated in a confusion matrix,
    weighted by `sample_weight` and the metric is then calculated from it.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    Note that this class first computes IoUs for all individual classes, then
    returns the mean of these values.

    Args:
      num_classes: The possible number of labels the prediction task can have.
        This value must be provided, since a confusion matrix of dimension =
        [num_classes, num_classes] will be allocated.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      ignore_class: Optional integer. The ID of a class to be ignored during
        metric computation. This is useful, for example, in segmentation
        problems featuring a "void" class (commonly -1 or 255) in segmentation
        maps. By default (`ignore_class=None`), all classes are considered.
      sparse_y_true: Whether labels are encoded using integers or
        dense floating point vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      sparse_y_pred: Whether predictions are encoded using integers or
        dense floating point vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      axis: (Optional) Defaults to -1. The dimension containing the logits.

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
      optimizer=\'sgd\',
      loss=\'mse\',
      metrics=[tf.keras.metrics.MeanIoU(num_classes=2)])
    ```
    '''
    def __init__(self, num_classes: int, name: str | None = None, dtype: str | tf.dtypes.DType | None = None, ignore_class: int | None = None, sparse_y_true: bool = True, sparse_y_pred: bool = True, axis: int = -1) -> None: ...
    def get_config(self): ...

class OneHotIoU(IoU):
    '''Computes the Intersection-Over-Union metric for one-hot encoded labels.

    General definition and computation:

    Intersection-Over-Union is a common evaluation metric for semantic image
    segmentation.

    For an individual class, the IoU metric is defined as follows:

    ```
    iou = true_positives / (true_positives + false_positives + false_negatives)
    ```

    To compute IoUs, the predictions are accumulated in a confusion matrix,
    weighted by `sample_weight` and the metric is then calculated from it.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    This class can be used to compute IoU for multi-class classification tasks
    where the labels are one-hot encoded (the last axis should have one
    dimension per class). Note that the predictions should also have the same
    shape. To compute the IoU, first the labels and predictions are converted
    back into integer format by taking the argmax over the class axis. Then the
    same computation steps as for the base `IoU` class apply.

    Note, if there is only one channel in the labels and predictions, this class
    is the same as class `IoU`. In this case, use `IoU` instead.

    Also, make sure that `num_classes` is equal to the number of classes in the
    data, to avoid a "labels out of bound" error when the confusion matrix is
    computed.

    Args:
      num_classes: The possible number of labels the prediction task can have.
        A confusion matrix of shape `(num_classes, num_classes)` will be
        allocated to accumulate predictions from which the metric is calculated.
      target_class_ids: A tuple or list of target class ids for which the metric
        is returned. To compute IoU for a specific class, a list (or tuple) of a
        single id value should be provided.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      ignore_class: Optional integer. The ID of a class to be ignored during
        metric computation. This is useful, for example, in segmentation
        problems featuring a "void" class (commonly -1 or 255) in segmentation
        maps. By default (`ignore_class=None`), all classes are considered.
      sparse_y_pred: Whether predictions are encoded using natural numbers or
        probability distribution vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      axis: (Optional) Defaults to -1. The dimension containing the logits.

    Standalone usage:

    >>> y_true = tf.constant([[0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 0, 0]])
    >>> y_pred = tf.constant([[0.2, 0.3, 0.5], [0.1, 0.2, 0.7], [0.5, 0.3, 0.1],
    ...                       [0.1, 0.4, 0.5]])
    >>> sample_weight = [0.1, 0.2, 0.3, 0.4]
    >>> m = tf.keras.metrics.OneHotIoU(num_classes=3, target_class_ids=[0, 2])
    >>> m.update_state(
    ...     y_true=y_true, y_pred=y_pred, sample_weight=sample_weight)
    >>> # cm = [[0, 0, 0.2+0.4],
    >>> #       [0.3, 0, 0],
    >>> #       [0, 0, 0.1]]
    >>> # sum_row = [0.3, 0, 0.7], sum_col = [0.6, 0.3, 0.1]
    >>> # true_positives = [0, 0, 0.1]
    >>> # single_iou = true_positives / (sum_row + sum_col - true_positives))
    >>> # mean_iou = (0 / (0.3 + 0.6 - 0) + 0.1 / (0.7 + 0.1 - 0.1)) / 2
    >>> m.result().numpy()
    0.071

    Usage with `compile()` API:

    ```python
    model.compile(
      optimizer=\'sgd\',
      loss=\'mse\',
      metrics=[tf.keras.metrics.OneHotIoU(num_classes=3, target_class_id=[1])])
    ```
    '''
    def __init__(self, num_classes: int, target_class_ids: List[int] | Tuple[int, ...], name: Incomplete | None = None, dtype: Incomplete | None = None, ignore_class: int | None = None, sparse_y_pred: bool = False, axis: int = -1) -> None: ...
    def get_config(self): ...

class OneHotMeanIoU(MeanIoU):
    '''Computes mean Intersection-Over-Union metric for one-hot encoded labels.

    General definition and computation:

    Intersection-Over-Union is a common evaluation metric for semantic image
    segmentation.

    For an individual class, the IoU metric is defined as follows:

    ```
    iou = true_positives / (true_positives + false_positives + false_negatives)
    ```

    To compute IoUs, the predictions are accumulated in a confusion matrix,
    weighted by `sample_weight` and the metric is then calculated from it.

    If `sample_weight` is `None`, weights default to 1.
    Use `sample_weight` of 0 to mask values.

    This class can be used to compute the mean IoU for multi-class
    classification tasks where the labels are one-hot encoded (the last axis
    should have one dimension per class). Note that the predictions should also
    have the same shape. To compute the mean IoU, first the labels and
    predictions are converted back into integer format by taking the argmax over
    the class axis. Then the same computation steps as for the base `MeanIoU`
    class apply.

    Note, if there is only one channel in the labels and predictions, this class
    is the same as class `MeanIoU`. In this case, use `MeanIoU` instead.

    Also, make sure that `num_classes` is equal to the number of classes in the
    data, to avoid a "labels out of bound" error when the confusion matrix is
    computed.

    Args:
      num_classes: The possible number of labels the prediction task can have.
        A confusion matrix of shape `(num_classes, num_classes)` will be
        allocated to accumulate predictions from which the metric is calculated.
      name: (Optional) string name of the metric instance.
      dtype: (Optional) data type of the metric result.
      ignore_class: Optional integer. The ID of a class to be ignored during
        metric computation. This is useful, for example, in segmentation
        problems featuring a "void" class (commonly -1 or 255) in segmentation
        maps. By default (`ignore_class=None`), all classes are considered.
      sparse_y_pred: Whether predictions are encoded using natural numbers or
        probability distribution vectors. If `False`, the `tf.argmax` function
        will be used to determine each sample\'s most likely associated label.
      axis: (Optional) Defaults to -1. The dimension containing the logits.

    Standalone usage:

    >>> y_true = tf.constant([[0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 0, 0]])
    >>> y_pred = tf.constant([[0.2, 0.3, 0.5], [0.1, 0.2, 0.7], [0.5, 0.3, 0.1],
    ...                       [0.1, 0.4, 0.5]])
    >>> sample_weight = [0.1, 0.2, 0.3, 0.4]
    >>> m = tf.keras.metrics.OneHotMeanIoU(num_classes=3)
    >>> m.update_state(
    ...     y_true=y_true, y_pred=y_pred, sample_weight=sample_weight)
    >>> # cm = [[0, 0, 0.2+0.4],
    >>> #       [0.3, 0, 0],
    >>> #       [0, 0, 0.1]]
    >>> # sum_row = [0.3, 0, 0.7], sum_col = [0.6, 0.3, 0.1]
    >>> # true_positives = [0, 0, 0.1]
    >>> # single_iou = true_positives / (sum_row + sum_col - true_positives))
    >>> # mean_iou = (0 + 0 + 0.1 / (0.7 + 0.1 - 0.1)) / 3
    >>> m.result().numpy()
    0.048

    Usage with `compile()` API:

    ```python
    model.compile(
      optimizer=\'sgd\',
      loss=\'mse\',
      metrics=[tf.keras.metrics.OneHotMeanIoU(num_classes=3)])
    ```
    '''
    def __init__(self, num_classes: int, name: str = None, dtype: str | tf.dtypes.DType | None = None, ignore_class: int | None = None, sparse_y_pred: bool = False, axis: int = -1) -> None: ...
    def get_config(self): ...
