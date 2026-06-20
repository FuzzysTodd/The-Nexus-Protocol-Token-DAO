from .utils import get_class_name as get_class_name, get_logger as get_logger
from _typeshed import Incomplete
from pyspark.ml.util import MLReader, MLWriter
from xgboost.core import Booster as Booster

def deserialize_xgb_model(model_string, xgb_model_creator):
    """
    Deserialize an xgboost.XGBModel instance from the input model_string.
    """
def serialize_booster(booster):
    """
    Serialize the input booster to a string.

    Parameters
    ----------
    booster:
        an xgboost.core.Booster instance
    """
def deserialize_booster(ser_model_string):
    """
    Deserialize an xgboost.core.Booster from the input ser_model_string.
    """

class _SparkXGBSharedReadWrite:
    @staticmethod
    def saveMetadata(instance, path, sc, logger, extraMetadata: Incomplete | None = None) -> None:
        """
        Save the metadata of an xgboost.spark._SparkXGBEstimator or
        xgboost.spark._SparkXGBModel.
        """
    @staticmethod
    def loadMetadataAndInstance(pyspark_xgb_cls, path, sc, logger):
        """
        Load the metadata and the instance of an xgboost.spark._SparkXGBEstimator or
        xgboost.spark._SparkXGBModel.

        :return: a tuple of (metadata, instance)
        """

class SparkXGBWriter(MLWriter):
    """
    Spark Xgboost estimator writer.
    """
    instance: Incomplete
    logger: Incomplete
    def __init__(self, instance) -> None: ...
    def saveImpl(self, path) -> None:
        """
        save model.
        """

class SparkXGBReader(MLReader):
    """
    Spark Xgboost estimator reader.
    """
    cls: Incomplete
    logger: Incomplete
    def __init__(self, cls) -> None: ...
    def load(self, path):
        """
        load model.
        """

class SparkXGBModelWriter(MLWriter):
    """
    Spark Xgboost model writer.
    """
    instance: Incomplete
    logger: Incomplete
    def __init__(self, instance) -> None: ...
    def saveImpl(self, path) -> None:
        """
        Save metadata and model for a :py:class:`_SparkXGBModel`
        - save metadata to path/metadata
        - save model to path/model.json
        """

class SparkXGBModelReader(MLReader):
    """
    Spark Xgboost model reader.
    """
    cls: Incomplete
    logger: Incomplete
    def __init__(self, cls) -> None: ...
    def load(self, path):
        """
        Load metadata and model for a :py:class:`_SparkXGBModel`

        :return: SparkXGBRegressorModel or SparkXGBClassifierModel instance
        """
