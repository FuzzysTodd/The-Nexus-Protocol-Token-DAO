import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from pyspark import since as since
from pyspark.ml._typing import ParamMap as ParamMap
from pyspark.ml.common import inherit_doc as inherit_doc
from pyspark.ml.param import P as P
from pyspark.ml.param.shared import HasFeaturesCol as HasFeaturesCol, HasInputCol as HasInputCol, HasLabelCol as HasLabelCol, HasOutputCol as HasOutputCol, HasPredictionCol as HasPredictionCol, Params as Params
from pyspark.sql.dataframe import DataFrame as DataFrame
from pyspark.sql.functions import udf as udf
from pyspark.sql.types import DataType as DataType, StructField as StructField, StructType as StructType
from typing import Any, Callable, Generic, Iterator, List, Sequence, Tuple, TypeVar, overload

T = TypeVar('T')
M = TypeVar('M', bound='Transformer')

class _FitMultipleIterator(Generic[M]):
    """
    Used by default implementation of Estimator.fitMultiple to produce models in a thread safe
    iterator. This class handles the simple case of fitMultiple where each param map should be
    fit independently.

    Parameters
    ----------
    fitSingleModel : function
        Callable[[int], Transformer] which fits an estimator to a dataset.
        `fitSingleModel` may be called up to `numModels` times, with a unique index each time.
        Each call to `fitSingleModel` with an index should return the Model associated with
        that index.
    numModel : int
        Number of models this iterator should produce.

    Notes
    -----
    See :py:meth:`Estimator.fitMultiple` for more info.
    """
    fitSingleModel: Incomplete
    numModel: Incomplete
    counter: int
    lock: Incomplete
    def __init__(self, fitSingleModel: Callable[[int], M], numModels: int) -> None:
        """ """
    def __iter__(self) -> Iterator[Tuple[int, M]]: ...
    def __next__(self) -> Tuple[int, M]: ...
    def next(self) -> Tuple[int, M]:
        """For python2 compatibility."""

class Estimator(Params, Generic[M], metaclass=ABCMeta):
    """
    Abstract class for estimators that fit models to data.

    .. versionadded:: 1.3.0
    """
    def fitMultiple(self, dataset: DataFrame, paramMaps: Sequence['ParamMap']) -> Iterator[Tuple[int, M]]:
        """
        Fits a model to the input dataset for each param map in `paramMaps`.

        .. versionadded:: 2.3.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            input dataset.
        paramMaps : :py:class:`collections.abc.Sequence`
            A Sequence of param maps.

        Returns
        -------
        :py:class:`_FitMultipleIterator`
            A thread safe iterable which contains one model for each param map. Each
            call to `next(modelIterator)` will return `(index, model)` where model was fit
            using `paramMaps[index]`. `index` values may not be sequential.
        """
    @overload
    def fit(self, dataset: DataFrame, params: ParamMap | None = ...) -> M: ...
    @overload
    def fit(self, dataset: DataFrame, params: List['ParamMap'] | Tuple['ParamMap']) -> List[M]: ...

class Transformer(Params, metaclass=ABCMeta):
    """
    Abstract class for transformers that transform one dataset into another.

    .. versionadded:: 1.3.0
    """
    def transform(self, dataset: DataFrame, params: ParamMap | None = None) -> DataFrame:
        """
        Transforms the input dataset with optional parameters.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            input dataset
        params : dict, optional
            an optional param map that overrides embedded params.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            transformed dataset
        """

class Model(Transformer, metaclass=ABCMeta):
    """
    Abstract class for models that are fitted by estimators.

    .. versionadded:: 1.4.0
    """

class UnaryTransformer(HasInputCol, HasOutputCol, Transformer, metaclass=abc.ABCMeta):
    """
    Abstract class for transformers that take one input column, apply transformation,
    and output the result as a new column.

    .. versionadded:: 2.3.0
    """
    def setInputCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`inputCol`.
        """
    def setOutputCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`outputCol`.
        """
    @abstractmethod
    def createTransformFunc(self) -> Callable[..., Any]:
        """
        Creates the transform function using the given param map. The input param map already takes
        account of the embedded param map. So the param values should be determined
        solely by the input param map.
        """
    @abstractmethod
    def outputDataType(self) -> DataType:
        """
        Returns the data type of the output column.
        """
    @abstractmethod
    def validateInputType(self, inputType: DataType) -> None:
        """
        Validates the input type. Throw an exception if it is invalid.
        """
    def transformSchema(self, schema: StructType) -> StructType: ...

class _PredictorParams(HasLabelCol, HasFeaturesCol, HasPredictionCol):
    """
    Params for :py:class:`Predictor` and :py:class:`PredictorModel`.

    .. versionadded:: 3.0.0
    """

class Predictor(Estimator[M], _PredictorParams, metaclass=ABCMeta):
    """
    Estimator for prediction tasks (regression and classification).
    """
    def setLabelCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setFeaturesCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`predictionCol`.
        """

class PredictionModel(Model, _PredictorParams, Generic[T], metaclass=ABCMeta):
    """
    Model for prediction tasks (regression and classification).
    """
    def setFeaturesCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    @property
    @abstractmethod
    def numFeatures(self) -> int:
        """
        Returns the number of features the model was trained on. If unknown, returns -1
        """
    @abstractmethod
    def predict(self, value: T) -> float:
        """
        Predict label for the given features.
        """
