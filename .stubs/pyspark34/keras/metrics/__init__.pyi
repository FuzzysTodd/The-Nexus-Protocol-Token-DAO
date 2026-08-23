from _typeshed import Incomplete
from keras.metrics.accuracy_metrics import Accuracy as Accuracy, BinaryAccuracy as BinaryAccuracy, CategoricalAccuracy as CategoricalAccuracy, SparseCategoricalAccuracy as SparseCategoricalAccuracy, SparseTopKCategoricalAccuracy as SparseTopKCategoricalAccuracy, TopKCategoricalAccuracy as TopKCategoricalAccuracy, accuracy as accuracy, binary_accuracy as binary_accuracy, categorical_accuracy as categorical_accuracy, sparse_categorical_accuracy as sparse_categorical_accuracy, sparse_top_k_categorical_accuracy as sparse_top_k_categorical_accuracy, top_k_categorical_accuracy as top_k_categorical_accuracy
from keras.metrics.base_metric import Mean as Mean, MeanMetricWrapper as MeanMetricWrapper, MeanTensor as MeanTensor, Metric as Metric, Reduce as Reduce, Sum as Sum, SumOverBatchSize as SumOverBatchSize, SumOverBatchSizeMetricWrapper as SumOverBatchSizeMetricWrapper, clone_metric as clone_metric, clone_metrics as clone_metrics
from keras.metrics.confusion_metrics import AUC as AUC, FalseNegatives as FalseNegatives, FalsePositives as FalsePositives, Precision as Precision, PrecisionAtRecall as PrecisionAtRecall, Recall as Recall, RecallAtPrecision as RecallAtPrecision, SensitivityAtSpecificity as SensitivityAtSpecificity, SensitivitySpecificityBase as SensitivitySpecificityBase, SpecificityAtSensitivity as SpecificityAtSensitivity, TrueNegatives as TrueNegatives, TruePositives as TruePositives
from keras.metrics.hinge_metrics import CategoricalHinge as CategoricalHinge, Hinge as Hinge, SquaredHinge as SquaredHinge, categorical_hinge as categorical_hinge, hinge as hinge, squared_hinge as squared_hinge
from keras.metrics.iou_metrics import BinaryIoU as BinaryIoU, IoU as IoU, MeanIoU as MeanIoU, OneHotIoU as OneHotIoU, OneHotMeanIoU as OneHotMeanIoU
from keras.metrics.probabilistic_metrics import BinaryCrossentropy as BinaryCrossentropy, CategoricalCrossentropy as CategoricalCrossentropy, KLDivergence as KLDivergence, Poisson as Poisson, SparseCategoricalCrossentropy as SparseCategoricalCrossentropy, binary_crossentropy as binary_crossentropy, categorical_crossentropy as categorical_crossentropy, kullback_leibler_divergence as kullback_leibler_divergence, poisson as poisson, sparse_categorical_crossentropy as sparse_categorical_crossentropy
from keras.metrics.regression_metrics import CosineSimilarity as CosineSimilarity, LogCoshError as LogCoshError, MeanAbsoluteError as MeanAbsoluteError, MeanAbsolutePercentageError as MeanAbsolutePercentageError, MeanRelativeError as MeanRelativeError, MeanSquaredError as MeanSquaredError, MeanSquaredLogarithmicError as MeanSquaredLogarithmicError, RootMeanSquaredError as RootMeanSquaredError, cosine_similarity as cosine_similarity, logcosh as logcosh, mean_absolute_error as mean_absolute_error, mean_absolute_percentage_error as mean_absolute_percentage_error, mean_squared_error as mean_squared_error, mean_squared_logarithmic_error as mean_squared_logarithmic_error
from keras.saving.legacy.serialization import deserialize_keras_object as deserialize_keras_object, serialize_keras_object as serialize_keras_object

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
log_cosh = logcosh
cosine_proximity = cosine_similarity

def serialize(metric, use_legacy_format: bool = False):
    """Serializes metric function or `Metric` instance.

    Args:
      metric: A Keras `Metric` instance or a metric function.

    Returns:
      Metric configuration dictionary.
    """
def deserialize(config, custom_objects: Incomplete | None = None, use_legacy_format: bool = False):
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
    <class \'...metrics.CategoricalCrossentropy\'>

    You can also specify `config` of the metric to this function by passing dict
    containing `class_name` and `config` as an identifier. Also note that the
    `class_name` must map to a `Metric` class

    >>> identifier = {"class_name": "CategoricalCrossentropy",
    ...               "config": {"from_logits": True}}
    >>> metric = tf.keras.metrics.get(identifier)
    >>> type(metric)
    <class \'...metrics.CategoricalCrossentropy\'>

    Args:
      identifier: A metric identifier. One of None or string name of a metric
        function/class or metric configuration dictionary or a metric function
        or a metric class instance

    Returns:
      A Keras metric as a `function`/ `Metric` class instance.

    Raises:
      ValueError: If `identifier` cannot be interpreted.
    '''
