from _typeshed import Incomplete
from py4j.java_collections import JavaArray
from pyspark import SparkContext
from pyspark.ml import Estimator, Model
from pyspark.ml._typing import ParamMap
from pyspark.ml.evaluation import Evaluator
from pyspark.ml.param import Param
from pyspark.ml.param.shared import HasCollectSubModels, HasParallelism, HasSeed
from pyspark.ml.util import MLReadable, MLReader, MLWritable, MLWriter
from typing import Any, Dict, List, Sequence, Tuple, Type, overload

__all__ = ['ParamGridBuilder', 'CrossValidator', 'CrossValidatorModel', 'TrainValidationSplit', 'TrainValidationSplitModel']

class ParamGridBuilder:
    """
    Builder for a param grid used in grid search-based model selection.


    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from pyspark.ml.classification import LogisticRegression
    >>> lr = LogisticRegression()
    >>> output = ParamGridBuilder() \\\n    ...     .baseOn({lr.labelCol: 'l'}) \\\n    ...     .baseOn([lr.predictionCol, 'p']) \\\n    ...     .addGrid(lr.regParam, [1.0, 2.0]) \\\n    ...     .addGrid(lr.maxIter, [1, 5]) \\\n    ...     .build()
    >>> expected = [
    ...     {lr.regParam: 1.0, lr.maxIter: 1, lr.labelCol: 'l', lr.predictionCol: 'p'},
    ...     {lr.regParam: 2.0, lr.maxIter: 1, lr.labelCol: 'l', lr.predictionCol: 'p'},
    ...     {lr.regParam: 1.0, lr.maxIter: 5, lr.labelCol: 'l', lr.predictionCol: 'p'},
    ...     {lr.regParam: 2.0, lr.maxIter: 5, lr.labelCol: 'l', lr.predictionCol: 'p'}]
    >>> len(output) == len(expected)
    True
    >>> all([m in expected for m in output])
    True
    """
    def __init__(self) -> None: ...
    def addGrid(self, param: Param[Any], values: List[Any]) -> ParamGridBuilder:
        """
        Sets the given parameters in this grid to fixed values.

        param must be an instance of Param associated with an instance of Params
        (such as Estimator or Transformer).
        """
    @overload
    def baseOn(self, __args: ParamMap) -> ParamGridBuilder: ...
    @overload
    def baseOn(self, *args: Tuple[Param, Any]) -> ParamGridBuilder: ...
    def build(self) -> List['ParamMap']:
        """
        Builds and returns all combinations of parameters specified
        by the param grid.
        """

class _ValidatorParams(HasSeed):
    """
    Common params for TrainValidationSplit and CrossValidator.
    """
    estimator: Param[Estimator]
    estimatorParamMaps: Param[List['ParamMap']]
    evaluator: Param[Evaluator]
    def getEstimator(self) -> Estimator:
        """
        Gets the value of estimator or its default value.
        """
    def getEstimatorParamMaps(self) -> List['ParamMap']:
        """
        Gets the value of estimatorParamMaps or its default value.
        """
    def getEvaluator(self) -> Evaluator:
        """
        Gets the value of evaluator or its default value.
        """

class _ValidatorSharedReadWrite:
    @staticmethod
    def meta_estimator_transfer_param_maps_to_java(pyEstimator: Estimator, pyParamMaps: Sequence['ParamMap']) -> JavaArray: ...
    @staticmethod
    def meta_estimator_transfer_param_maps_from_java(pyEstimator: Estimator, javaParamMaps: JavaArray) -> List['ParamMap']: ...
    @staticmethod
    def is_java_convertible(instance: _ValidatorParams) -> bool: ...
    @staticmethod
    def saveImpl(path: str, instance: _ValidatorParams, sc: SparkContext, extraMetadata: Dict[str, Any] | None = None) -> None: ...
    @staticmethod
    def load(path: str, sc: SparkContext, metadata: Dict[str, Any]) -> Tuple[Dict[str, Any], Estimator, Evaluator, List['ParamMap']]: ...
    @staticmethod
    def validateParams(instance: _ValidatorParams) -> None: ...
    @staticmethod
    def getValidatorModelWriterPersistSubModelsParam(writer: MLWriter) -> bool: ...

class CrossValidatorReader(MLReader['CrossValidator']):
    cls: Incomplete
    def __init__(self, cls: Type['CrossValidator']) -> None: ...
    def load(self, path: str) -> CrossValidator: ...

class CrossValidatorWriter(MLWriter):
    instance: Incomplete
    def __init__(self, instance: CrossValidator) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class CrossValidatorModelReader(MLReader['CrossValidatorModel']):
    cls: Incomplete
    def __init__(self, cls: Type['CrossValidatorModel']) -> None: ...
    def load(self, path: str) -> CrossValidatorModel: ...

class CrossValidatorModelWriter(MLWriter):
    instance: Incomplete
    def __init__(self, instance: CrossValidatorModel) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class _CrossValidatorParams(_ValidatorParams):
    """
    Params for :py:class:`CrossValidator` and :py:class:`CrossValidatorModel`.

    .. versionadded:: 3.0.0
    """
    numFolds: Param[int]
    foldCol: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getNumFolds(self) -> int:
        """
        Gets the value of numFolds or its default value.
        """
    def getFoldCol(self) -> str:
        """
        Gets the value of foldCol or its default value.
        """

class CrossValidator(Estimator['CrossValidatorModel'], _CrossValidatorParams, HasParallelism, HasCollectSubModels, MLReadable['CrossValidator'], MLWritable):
    '''

    K-fold cross validation performs model selection by splitting the dataset into a set of
    non-overlapping randomly partitioned folds which are used as separate training and test datasets
    e.g., with k=3 folds, K-fold cross validation will generate 3 (training, test) dataset pairs,
    each of which uses 2/3 of the data for training and 1/3 for testing. Each fold is used as the
    test set exactly once.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from pyspark.ml.classification import LogisticRegression
    >>> from pyspark.ml.evaluation import BinaryClassificationEvaluator
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.tuning import CrossValidator, ParamGridBuilder, CrossValidatorModel
    >>> import tempfile
    >>> dataset = spark.createDataFrame(
    ...     [(Vectors.dense([0.0]), 0.0),
    ...      (Vectors.dense([0.4]), 1.0),
    ...      (Vectors.dense([0.5]), 0.0),
    ...      (Vectors.dense([0.6]), 1.0),
    ...      (Vectors.dense([1.0]), 1.0)] * 10,
    ...     ["features", "label"])
    >>> lr = LogisticRegression()
    >>> grid = ParamGridBuilder().addGrid(lr.maxIter, [0, 1]).build()
    >>> evaluator = BinaryClassificationEvaluator()
    >>> cv = CrossValidator(estimator=lr, estimatorParamMaps=grid, evaluator=evaluator,
    ...     parallelism=2)
    >>> cvModel = cv.fit(dataset)
    >>> cvModel.getNumFolds()
    3
    >>> cvModel.avgMetrics[0]
    0.5
    >>> path = tempfile.mkdtemp()
    >>> model_path = path + "/model"
    >>> cvModel.write().save(model_path)
    >>> cvModelRead = CrossValidatorModel.read().load(model_path)
    >>> cvModelRead.avgMetrics
    [0.5, ...
    >>> evaluator.evaluate(cvModel.transform(dataset))
    0.8333...
    >>> evaluator.evaluate(cvModelRead.transform(dataset))
    0.8333...
    '''
    def __init__(self, *, estimator: Estimator | None = None, estimatorParamMaps: List['ParamMap'] | None = None, evaluator: Evaluator | None = None, numFolds: int = 3, seed: int | None = None, parallelism: int = 1, collectSubModels: bool = False, foldCol: str = '') -> None:
        '''
        __init__(self, \\*, estimator=None, estimatorParamMaps=None, evaluator=None, numFolds=3,                 seed=None, parallelism=1, collectSubModels=False, foldCol="")
        '''
    def setParams(self, *, estimator: Estimator | None = None, estimatorParamMaps: List['ParamMap'] | None = None, evaluator: Evaluator | None = None, numFolds: int = 3, seed: int | None = None, parallelism: int = 1, collectSubModels: bool = False, foldCol: str = '') -> CrossValidator:
        '''
        setParams(self, \\*, estimator=None, estimatorParamMaps=None, evaluator=None, numFolds=3,                  seed=None, parallelism=1, collectSubModels=False, foldCol=""):
        Sets params for cross validator.
        '''
    def setEstimator(self, value: Estimator) -> CrossValidator:
        """
        Sets the value of :py:attr:`estimator`.
        """
    def setEstimatorParamMaps(self, value: List['ParamMap']) -> CrossValidator:
        """
        Sets the value of :py:attr:`estimatorParamMaps`.
        """
    def setEvaluator(self, value: Evaluator) -> CrossValidator:
        """
        Sets the value of :py:attr:`evaluator`.
        """
    def setNumFolds(self, value: int) -> CrossValidator:
        """
        Sets the value of :py:attr:`numFolds`.
        """
    def setFoldCol(self, value: str) -> CrossValidator:
        """
        Sets the value of :py:attr:`foldCol`.
        """
    def setSeed(self, value: int) -> CrossValidator:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setParallelism(self, value: int) -> CrossValidator:
        """
        Sets the value of :py:attr:`parallelism`.
        """
    def setCollectSubModels(self, value: bool) -> CrossValidator:
        """
        Sets the value of :py:attr:`collectSubModels`.
        """
    def copy(self, extra: ParamMap | None = None) -> CrossValidator:
        """
        Creates a copy of this instance with a randomly generated uid
        and some extra params. This copies creates a deep copy of
        the embedded paramMap, and copies the embedded and extra parameters over.


        .. versionadded:: 1.4.0

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`CrossValidator`
            Copy of this instance
        """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    @classmethod
    def read(cls) -> CrossValidatorReader:
        """Returns an MLReader instance for this class."""

class CrossValidatorModel(Model, _CrossValidatorParams, MLReadable['CrossValidatorModel'], MLWritable):
    '''
    CrossValidatorModel contains the model with the highest average cross-validation
    metric across folds and uses this model to transform input data. CrossValidatorModel
    also tracks the metrics for each param map evaluated.

    .. versionadded:: 1.4.0

    Notes
    -----
    Since version 3.3.0, CrossValidatorModel contains a new attribute "stdMetrics",
    which represent standard deviation of metrics for each paramMap in
    CrossValidator.estimatorParamMaps.
    '''
    bestModel: Incomplete
    avgMetrics: Incomplete
    subModels: Incomplete
    stdMetrics: Incomplete
    def __init__(self, bestModel: Model, avgMetrics: List[float] | None = None, subModels: List[List[Model]] | None = None, stdMetrics: List[float] | None = None) -> None: ...
    def copy(self, extra: ParamMap | None = None) -> CrossValidatorModel:
        """
        Creates a copy of this instance with a randomly generated uid
        and some extra params. This copies the underlying bestModel,
        creates a deep copy of the embedded paramMap, and
        copies the embedded and extra parameters over.
        It does not copy the extra Params into the subModels.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`CrossValidatorModel`
            Copy of this instance
        """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    @classmethod
    def read(cls) -> CrossValidatorModelReader:
        """Returns an MLReader instance for this class."""

class TrainValidationSplitReader(MLReader['TrainValidationSplit']):
    cls: Incomplete
    def __init__(self, cls: Type['TrainValidationSplit']) -> None: ...
    def load(self, path: str) -> TrainValidationSplit: ...

class TrainValidationSplitWriter(MLWriter):
    instance: Incomplete
    def __init__(self, instance: TrainValidationSplit) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class TrainValidationSplitModelReader(MLReader['TrainValidationSplitModel']):
    cls: Incomplete
    def __init__(self, cls: Type['TrainValidationSplitModel']) -> None: ...
    def load(self, path: str) -> TrainValidationSplitModel: ...

class TrainValidationSplitModelWriter(MLWriter):
    instance: Incomplete
    def __init__(self, instance: TrainValidationSplitModel) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class _TrainValidationSplitParams(_ValidatorParams):
    """
    Params for :py:class:`TrainValidationSplit` and :py:class:`TrainValidationSplitModel`.

    .. versionadded:: 3.0.0
    """
    trainRatio: Param[float]
    def __init__(self, *args: Any) -> None: ...
    def getTrainRatio(self) -> float:
        """
        Gets the value of trainRatio or its default value.
        """

class TrainValidationSplit(Estimator['TrainValidationSplitModel'], _TrainValidationSplitParams, HasParallelism, HasCollectSubModels, MLReadable['TrainValidationSplit'], MLWritable):
    '''
    Validation for hyper-parameter tuning. Randomly splits the input dataset into train and
    validation sets, and uses evaluation metric on the validation set to select the best model.
    Similar to :class:`CrossValidator`, but only splits the set once.

    .. versionadded:: 2.0.0

    Examples
    --------
    >>> from pyspark.ml.classification import LogisticRegression
    >>> from pyspark.ml.evaluation import BinaryClassificationEvaluator
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.tuning import TrainValidationSplit, ParamGridBuilder
    >>> from pyspark.ml.tuning import TrainValidationSplitModel
    >>> import tempfile
    >>> dataset = spark.createDataFrame(
    ...     [(Vectors.dense([0.0]), 0.0),
    ...      (Vectors.dense([0.4]), 1.0),
    ...      (Vectors.dense([0.5]), 0.0),
    ...      (Vectors.dense([0.6]), 1.0),
    ...      (Vectors.dense([1.0]), 1.0)] * 10,
    ...     ["features", "label"]).repartition(1)
    >>> lr = LogisticRegression()
    >>> grid = ParamGridBuilder().addGrid(lr.maxIter, [0, 1]).build()
    >>> evaluator = BinaryClassificationEvaluator()
    >>> tvs = TrainValidationSplit(estimator=lr, estimatorParamMaps=grid, evaluator=evaluator,
    ...     parallelism=1, seed=42)
    >>> tvsModel = tvs.fit(dataset)
    >>> tvsModel.getTrainRatio()
    0.75
    >>> tvsModel.validationMetrics
    [0.5, ...
    >>> path = tempfile.mkdtemp()
    >>> model_path = path + "/model"
    >>> tvsModel.write().save(model_path)
    >>> tvsModelRead = TrainValidationSplitModel.read().load(model_path)
    >>> tvsModelRead.validationMetrics
    [0.5, ...
    >>> evaluator.evaluate(tvsModel.transform(dataset))
    0.833...
    >>> evaluator.evaluate(tvsModelRead.transform(dataset))
    0.833...
    '''
    def __init__(self, *, estimator: Estimator | None = None, estimatorParamMaps: List['ParamMap'] | None = None, evaluator: Evaluator | None = None, trainRatio: float = 0.75, parallelism: int = 1, collectSubModels: bool = False, seed: int | None = None) -> None:
        """
        __init__(self, \\*, estimator=None, estimatorParamMaps=None, evaluator=None,                  trainRatio=0.75, parallelism=1, collectSubModels=False, seed=None)
        """
    def setParams(self, *, estimator: Estimator | None = None, estimatorParamMaps: List['ParamMap'] | None = None, evaluator: Evaluator | None = None, trainRatio: float = 0.75, parallelism: int = 1, collectSubModels: bool = False, seed: int | None = None) -> TrainValidationSplit:
        """
        setParams(self, \\*, estimator=None, estimatorParamMaps=None, evaluator=None,                   trainRatio=0.75, parallelism=1, collectSubModels=False, seed=None):
        Sets params for the train validation split.
        """
    def setEstimator(self, value: Estimator) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`estimator`.
        """
    def setEstimatorParamMaps(self, value: List['ParamMap']) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`estimatorParamMaps`.
        """
    def setEvaluator(self, value: Evaluator) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`evaluator`.
        """
    def setTrainRatio(self, value: float) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`trainRatio`.
        """
    def setSeed(self, value: int) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setParallelism(self, value: int) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`parallelism`.
        """
    def setCollectSubModels(self, value: bool) -> TrainValidationSplit:
        """
        Sets the value of :py:attr:`collectSubModels`.
        """
    def copy(self, extra: ParamMap | None = None) -> TrainValidationSplit:
        """
        Creates a copy of this instance with a randomly generated uid
        and some extra params. This copies creates a deep copy of
        the embedded paramMap, and copies the embedded and extra parameters over.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`TrainValidationSplit`
            Copy of this instance
        """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    @classmethod
    def read(cls) -> TrainValidationSplitReader:
        """Returns an MLReader instance for this class."""

class TrainValidationSplitModel(Model, _TrainValidationSplitParams, MLReadable['TrainValidationSplitModel'], MLWritable):
    """
    Model from train validation split.

    .. versionadded:: 2.0.0
    """
    bestModel: Incomplete
    validationMetrics: Incomplete
    subModels: Incomplete
    def __init__(self, bestModel: Model, validationMetrics: List[float] | None = None, subModels: List[Model] | None = None) -> None: ...
    def copy(self, extra: ParamMap | None = None) -> TrainValidationSplitModel:
        """
        Creates a copy of this instance with a randomly generated uid
        and some extra params. This copies the underlying bestModel,
        creates a deep copy of the embedded paramMap, and
        copies the embedded and extra parameters over.
        And, this creates a shallow copy of the validationMetrics.
        It does not copy the extra Params into the subModels.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`TrainValidationSplitModel`
            Copy of this instance
        """
    def write(self) -> MLWriter:
        """Returns an MLWriter instance for this ML instance."""
    @classmethod
    def read(cls) -> TrainValidationSplitModelReader:
        """Returns an MLReader instance for this class."""
