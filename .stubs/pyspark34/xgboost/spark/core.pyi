from .data import alias as alias, create_dmatrix_from_partitions as create_dmatrix_from_partitions, stack_series as stack_series
from .model import SparkXGBModelReader as SparkXGBModelReader, SparkXGBModelWriter as SparkXGBModelWriter, SparkXGBReader as SparkXGBReader, SparkXGBWriter as SparkXGBWriter
from .params import HasArbitraryParamsDict as HasArbitraryParamsDict, HasBaseMarginCol as HasBaseMarginCol, HasEnableSparseDataOptim as HasEnableSparseDataOptim, HasFeaturesCols as HasFeaturesCols, HasQueryIdCol as HasQueryIdCol
from .utils import CommunicatorContext as CommunicatorContext, get_class_name as get_class_name, get_logger as get_logger
from _typeshed import Incomplete
from pyspark.ml import Estimator, Model
from pyspark.ml.param.shared import HasFeaturesCol, HasLabelCol, HasPredictionCol, HasProbabilityCol, HasRawPredictionCol, HasValidationIndicatorCol, HasWeightCol
from pyspark.ml.util import MLReadable, MLWritable
from xgboost import XGBClassifier as XGBClassifier, XGBRanker as XGBRanker, XGBRegressor as XGBRegressor
from xgboost.compat import is_cudf_available as is_cudf_available
from xgboost.core import Booster as Booster

class _SparkXGBParams(HasFeaturesCol, HasLabelCol, HasWeightCol, HasPredictionCol, HasValidationIndicatorCol, HasArbitraryParamsDict, HasBaseMarginCol, HasFeaturesCols, HasEnableSparseDataOptim, HasQueryIdCol):
    num_workers: Incomplete
    use_gpu: Incomplete
    force_repartition: Incomplete
    repartition_random_shuffle: Incomplete
    feature_names: Incomplete

class _SparkXGBEstimator(Estimator, _SparkXGBParams, MLReadable, MLWritable):
    def __init__(self) -> None: ...
    def setParams(self, **kwargs) -> None:
        """
        Set params for the estimator.
        """
    def write(self):
        """
        Return the writer for saving the estimator.
        """
    @classmethod
    def read(cls):
        """
        Return the reader for loading the estimator.
        """

class _SparkXGBModel(Model, _SparkXGBParams, MLReadable, MLWritable):
    def __init__(self, xgb_sklearn_model: Incomplete | None = None) -> None: ...
    def get_booster(self):
        """
        Return the `xgboost.core.Booster` instance.
        """
    def get_feature_importances(self, importance_type: str = 'weight'):
        """Get feature importance of each feature.
        Importance type can be defined as:

        * 'weight': the number of times a feature is used to split the data across all trees.
        * 'gain': the average gain across all splits the feature is used in.
        * 'cover': the average coverage across all splits the feature is used in.
        * 'total_gain': the total gain across all splits the feature is used in.
        * 'total_cover': the total coverage across all splits the feature is used in.

        Parameters
        ----------
        importance_type: str, default 'weight'
            One of the importance types defined above.
        """
    def write(self):
        """
        Return the writer for saving the model.
        """
    @classmethod
    def read(cls):
        """
        Return the reader for loading the model.
        """

class SparkXGBRegressorModel(_SparkXGBModel):
    """
    The model returned by :func:`xgboost.spark.SparkXGBRegressor.fit`

    .. Note:: This API is experimental.
    """
class SparkXGBRankerModel(_SparkXGBModel):
    """
    The model returned by :func:`xgboost.spark.SparkXGBRanker.fit`

    .. Note:: This API is experimental.
    """
class SparkXGBClassifierModel(_SparkXGBModel, HasProbabilityCol, HasRawPredictionCol):
    """
    The model returned by :func:`xgboost.spark.SparkXGBClassifier.fit`

    .. Note:: This API is experimental.
    """
