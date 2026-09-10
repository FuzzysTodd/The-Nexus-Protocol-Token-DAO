from abc import ABCMeta
from py4j.java_gateway import JavaClass as JavaClass, JavaObject as JavaObject
from pyspark import SparkContext as SparkContext, since as since
from pyspark.ml import Estimator as Estimator, Model as Model, PredictionModel as PredictionModel, Predictor as Predictor, Transformer as Transformer
from pyspark.ml._typing import ParamMap as ParamMap
from pyspark.ml.base import _PredictorParams
from pyspark.ml.common import inherit_doc as inherit_doc
from pyspark.ml.param import Param as Param, Params as Params
from pyspark.sql import DataFrame as DataFrame
from typing import Generic, TypeVar

T = TypeVar('T')
JW = TypeVar('JW', bound='JavaWrapper')
JM = TypeVar('JM', bound='JavaTransformer')
JP = TypeVar('JP', bound='JavaParams')

class JavaWrapper:
    """
    Wrapper class for a Java companion object
    """
    def __init__(self, java_obj: JavaObject | None = None) -> None: ...
    def __del__(self) -> None: ...

class JavaParams(JavaWrapper, Params, metaclass=ABCMeta):
    """
    Utility class to help create wrapper classes from Java/Scala
    implementations of pipeline components.
    """
    def copy(self, extra: ParamMap | None = None) -> JP:
        """
        Creates a copy of this instance with the same uid and some
        extra params. This implementation first calls Params.copy and
        then make a copy of the companion Java pipeline component with
        extra params. So both the Python wrapper and the Java pipeline
        component get copied.

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`JavaParams`
            Copy of this instance
        """
    def clear(self, param: Param) -> None:
        """
        Clears a param from the param map if it has been explicitly set.
        """

class JavaEstimator(JavaParams, Estimator[JM], metaclass=ABCMeta):
    """
    Base class for :py:class:`Estimator`s that wrap Java/Scala
    implementations.
    """
class JavaTransformer(JavaParams, Transformer, metaclass=ABCMeta):
    """
    Base class for :py:class:`Transformer`s that wrap Java/Scala
    implementations. Subclasses should ensure they have the transformer Java object
    available as _java_obj.
    """

class JavaModel(JavaTransformer, Model, metaclass=ABCMeta):
    """
    Base class for :py:class:`Model`s that wrap Java/Scala
    implementations. Subclasses should inherit this class before
    param mix-ins, because this sets the UID from the Java model.
    """
    def __init__(self, java_model: JavaObject | None = None) -> None:
        """
        Initialize this instance with a Java model object.
        Subclasses should call this constructor, initialize params,
        and then call _transfer_params_from_java.

        This instance can be instantiated without specifying java_model,
        it will be assigned after that, but this scenario only used by
        :py:class:`JavaMLReader` to load models.  This is a bit of a
        hack, but it is easiest since a proper fix would require
        MLReader (in pyspark.ml.util) to depend on these wrappers, but
        these wrappers depend on pyspark.ml.util (both directly and via
        other ML classes).
        """

class JavaPredictor(Predictor, JavaEstimator[JM], _PredictorParams, Generic[JM], metaclass=ABCMeta):
    """
    (Private) Java Estimator for prediction tasks (regression and classification).
    """

class JavaPredictionModel(PredictionModel[T], JavaModel, _PredictorParams):
    """
    (Private) Java Model for prediction tasks (regression and classification).
    """
    @property
    def numFeatures(self) -> int:
        """
        Returns the number of features the model was trained on. If unknown, returns -1
        """
    def predict(self, value: T) -> float:
        """
        Predict label for the given features.
        """
