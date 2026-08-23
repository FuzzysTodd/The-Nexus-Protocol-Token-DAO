from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from pyspark import SparkContext
from pyspark.ml import Estimator, Model, PredictionModel, Predictor
from pyspark.ml._typing import P, ParamMap
from pyspark.ml.base import _PredictorParams
from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.param.shared import HasAggregationDepth, HasBlockSize, HasElasticNetParam, HasFitIntercept, HasMaxBlockSizeInMB, HasMaxIter, HasParallelism, HasProbabilityCol, HasRawPredictionCol, HasRegParam, HasSeed, HasSolver, HasStandardization, HasStepSize, HasThreshold, HasThresholds, HasTol, HasWeightCol, Param
from pyspark.ml.regression import DecisionTreeRegressionModel, _FactorizationMachinesParams
from pyspark.ml.tree import _DecisionTreeModel, _DecisionTreeParams, _GBTParams, _HasVarianceImpurity, _RandomForestParams, _TreeClassifierParams, _TreeEnsembleModel
from pyspark.ml.util import HasTrainingSummary, JavaMLReadable, JavaMLWritable, MLReadable, MLReader, MLWritable, MLWriter
from pyspark.ml.wrapper import JavaPredictionModel, JavaPredictor, JavaWrapper
from pyspark.sql import DataFrame
from typing import Any, Dict, Generic, List, Type, TypeVar, overload

__all__ = ['LinearSVC', 'LinearSVCModel', 'LinearSVCSummary', 'LinearSVCTrainingSummary', 'LogisticRegression', 'LogisticRegressionModel', 'LogisticRegressionSummary', 'LogisticRegressionTrainingSummary', 'BinaryLogisticRegressionSummary', 'BinaryLogisticRegressionTrainingSummary', 'DecisionTreeClassifier', 'DecisionTreeClassificationModel', 'GBTClassifier', 'GBTClassificationModel', 'RandomForestClassifier', 'RandomForestClassificationModel', 'RandomForestClassificationSummary', 'RandomForestClassificationTrainingSummary', 'BinaryRandomForestClassificationSummary', 'BinaryRandomForestClassificationTrainingSummary', 'NaiveBayes', 'NaiveBayesModel', 'MultilayerPerceptronClassifier', 'MultilayerPerceptronClassificationModel', 'MultilayerPerceptronClassificationSummary', 'MultilayerPerceptronClassificationTrainingSummary', 'OneVsRest', 'OneVsRestModel', 'FMClassifier', 'FMClassificationModel', 'FMClassificationSummary', 'FMClassificationTrainingSummary']

T = TypeVar('T')
JPM = TypeVar('JPM', bound=JavaPredictionModel)
CM = TypeVar('CM', bound='ClassificationModel')

class _ClassifierParams(HasRawPredictionCol, _PredictorParams):
    """
    Classifier Params for classification tasks.

    .. versionadded:: 3.0.0
    """

class Classifier(Predictor[CM], _ClassifierParams, Generic[CM], metaclass=ABCMeta):
    """
    Classifier for classification tasks.
    Classes are indexed {0, 1, ..., numClasses - 1}.
    """
    def setRawPredictionCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """

class ClassificationModel(PredictionModel, _ClassifierParams, metaclass=ABCMeta):
    """
    Model produced by a ``Classifier``.
    Classes are indexed {0, 1, ..., numClasses - 1}.
    """
    def setRawPredictionCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """
    @property
    @abstractmethod
    def numClasses(self) -> int:
        """
        Number of classes (values which the label can take).
        """
    @abstractmethod
    def predictRaw(self, value: Vector) -> Vector:
        """
        Raw prediction for each possible label.
        """

class _ProbabilisticClassifierParams(HasProbabilityCol, HasThresholds, _ClassifierParams):
    """
    Params for :py:class:`ProbabilisticClassifier` and
    :py:class:`ProbabilisticClassificationModel`.

    .. versionadded:: 3.0.0
    """

class ProbabilisticClassifier(Classifier, _ProbabilisticClassifierParams, metaclass=ABCMeta):
    """
    Probabilistic Classifier for classification tasks.
    """
    def setProbabilityCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`probabilityCol`.
        """
    def setThresholds(self, value: List[float]) -> P:
        """
        Sets the value of :py:attr:`thresholds`.
        """

class ProbabilisticClassificationModel(ClassificationModel, _ProbabilisticClassifierParams, metaclass=ABCMeta):
    """
    Model produced by a ``ProbabilisticClassifier``.
    """
    def setProbabilityCol(self, value: str) -> CM:
        """
        Sets the value of :py:attr:`probabilityCol`.
        """
    def setThresholds(self, value: List[float]) -> CM:
        """
        Sets the value of :py:attr:`thresholds`.
        """
    @abstractmethod
    def predictProbability(self, value: Vector) -> Vector:
        """
        Predict the probability of each class given the features.
        """

class _JavaClassifier(Classifier, JavaPredictor[JPM], Generic[JPM], metaclass=ABCMeta):
    """
    Java Classifier for classification tasks.
    Classes are indexed {0, 1, ..., numClasses - 1}.
    """
    def setRawPredictionCol(self, value: str) -> P:
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """

class _JavaClassificationModel(ClassificationModel, JavaPredictionModel[T]):
    """
    Java Model produced by a ``Classifier``.
    Classes are indexed {0, 1, ..., numClasses - 1}.
    To be mixed in with :class:`pyspark.ml.JavaModel`
    """
    @property
    def numClasses(self) -> int:
        """
        Number of classes (values which the label can take).
        """
    def predictRaw(self, value: Vector) -> Vector:
        """
        Raw prediction for each possible label.
        """

class _JavaProbabilisticClassifier(ProbabilisticClassifier, _JavaClassifier[JPM], Generic[JPM], metaclass=ABCMeta):
    """
    Java Probabilistic Classifier for classification tasks.
    """

class _JavaProbabilisticClassificationModel(ProbabilisticClassificationModel, _JavaClassificationModel[T]):
    """
    Java Model produced by a ``ProbabilisticClassifier``.
    """
    def predictProbability(self, value: Vector) -> Vector:
        """
        Predict the probability of each class given the features.
        """

class _ClassificationSummary(JavaWrapper):
    """
    Abstraction for multiclass classification results for a given model.

    .. versionadded:: 3.1.0
    """
    @property
    def predictions(self) -> DataFrame:
        """
        Dataframe outputted by the model's `transform` method.
        """
    @property
    def predictionCol(self) -> str:
        '''
        Field in "predictions" which gives the prediction of each class.
        '''
    @property
    def labelCol(self) -> str:
        '''
        Field in "predictions" which gives the true label of each
        instance.
        '''
    @property
    def weightCol(self) -> str:
        '''
        Field in "predictions" which gives the weight of each instance
        as a vector.
        '''
    @property
    def labels(self) -> List[str]:
        """
        Returns the sequence of labels in ascending order. This order matches the order used
        in metrics which are specified as arrays over labels, e.g., truePositiveRateByLabel.

        .. versionadded:: 3.1.0

        Notes
        -----
        In most cases, it will be values {0.0, 1.0, ..., numClasses-1}, However, if the
        training set is missing a label, then all of the arrays over labels
        (e.g., from truePositiveRateByLabel) will be of length numClasses-1 instead of the
        expected numClasses.
        """
    @property
    def truePositiveRateByLabel(self) -> List[float]:
        """
        Returns true positive rate for each label (category).
        """
    @property
    def falsePositiveRateByLabel(self) -> List[float]:
        """
        Returns false positive rate for each label (category).
        """
    @property
    def precisionByLabel(self) -> List[float]:
        """
        Returns precision for each label (category).
        """
    @property
    def recallByLabel(self) -> List[float]:
        """
        Returns recall for each label (category).
        """
    def fMeasureByLabel(self, beta: float = 1.0) -> List[float]:
        """
        Returns f-measure for each label (category).
        """
    @property
    def accuracy(self) -> float:
        """
        Returns accuracy.
        (equals to the total number of correctly classified instances
        out of the total number of instances.)
        """
    @property
    def weightedTruePositiveRate(self) -> float:
        """
        Returns weighted true positive rate.
        (equals to precision, recall and f-measure)
        """
    @property
    def weightedFalsePositiveRate(self) -> float:
        """
        Returns weighted false positive rate.
        """
    @property
    def weightedRecall(self) -> float:
        """
        Returns weighted averaged recall.
        (equals to precision, recall and f-measure)
        """
    @property
    def weightedPrecision(self) -> float:
        """
        Returns weighted averaged precision.
        """
    def weightedFMeasure(self, beta: float = 1.0) -> float:
        """
        Returns weighted averaged f-measure.
        """

class _TrainingSummary(JavaWrapper):
    """
    Abstraction for Training results.

    .. versionadded:: 3.1.0
    """
    @property
    def objectiveHistory(self) -> List[float]:
        """
        Objective function (scaled loss + regularization) at each
        iteration. It contains one more element, the initial state,
        than number of iterations.
        """
    @property
    def totalIterations(self) -> int:
        """
        Number of training iterations until termination.
        """

class _BinaryClassificationSummary(_ClassificationSummary):
    """
    Binary classification results for a given model.

    .. versionadded:: 3.1.0
    """
    @property
    def scoreCol(self) -> str:
        '''
        Field in "predictions" which gives the probability or raw prediction
        of each class as a vector.
        '''
    @property
    def roc(self) -> DataFrame:
        """
        Returns the receiver operating characteristic (ROC) curve,
        which is a Dataframe having two fields (FPR, TPR) with
        (0.0, 0.0) prepended and (1.0, 1.0) appended to it.

        .. versionadded:: 3.1.0

        Notes
        -----
        `Wikipedia reference <http://en.wikipedia.org/wiki/Receiver_operating_characteristic>`_
        """
    @property
    def areaUnderROC(self) -> float:
        """
        Computes the area under the receiver operating characteristic
        (ROC) curve.
        """
    @property
    def pr(self) -> DataFrame:
        """
        Returns the precision-recall curve, which is a Dataframe
        containing two fields recall, precision with (0.0, 1.0) prepended
        to it.
        """
    @property
    def fMeasureByThreshold(self) -> DataFrame:
        """
        Returns a dataframe with two fields (threshold, F-Measure) curve
        with beta = 1.0.
        """
    @property
    def precisionByThreshold(self) -> DataFrame:
        """
        Returns a dataframe with two fields (threshold, precision) curve.
        Every possible probability obtained in transforming the dataset
        are used as thresholds used in calculating the precision.
        """
    @property
    def recallByThreshold(self) -> DataFrame:
        """
        Returns a dataframe with two fields (threshold, recall) curve.
        Every possible probability obtained in transforming the dataset
        are used as thresholds used in calculating the recall.
        """

class _LinearSVCParams(_ClassifierParams, HasRegParam, HasMaxIter, HasFitIntercept, HasTol, HasStandardization, HasWeightCol, HasAggregationDepth, HasThreshold, HasMaxBlockSizeInMB):
    """
    Params for :py:class:`LinearSVC` and :py:class:`LinearSVCModel`.

    .. versionadded:: 3.0.0
    """
    threshold: Param[float]
    def __init__(self, *args: Any) -> None: ...

class LinearSVC(_JavaClassifier['LinearSVCModel'], _LinearSVCParams, JavaMLWritable, JavaMLReadable['LinearSVC']):
    '''
    This binary classifier optimizes the Hinge Loss using the OWLQN optimizer.
    Only supports L2 regularization currently.

    .. versionadded:: 2.2.0

    Notes
    -----
    `Linear SVM Classifier <https://en.wikipedia.org/wiki/Support_vector_machine#Linear_SVM>`_

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> from pyspark.ml.linalg import Vectors
    >>> df = sc.parallelize([
    ...     Row(label=1.0, features=Vectors.dense(1.0, 1.0, 1.0)),
    ...     Row(label=0.0, features=Vectors.dense(1.0, 2.0, 3.0))]).toDF()
    >>> svm = LinearSVC()
    >>> svm.getMaxIter()
    100
    >>> svm.setMaxIter(5)
    LinearSVC...
    >>> svm.getMaxIter()
    5
    >>> svm.getRegParam()
    0.0
    >>> svm.setRegParam(0.01)
    LinearSVC...
    >>> svm.getRegParam()
    0.01
    >>> model = svm.fit(df)
    >>> model.setPredictionCol("newPrediction")
    LinearSVCModel...
    >>> model.getPredictionCol()
    \'newPrediction\'
    >>> model.setThreshold(0.5)
    LinearSVCModel...
    >>> model.getThreshold()
    0.5
    >>> model.getMaxBlockSizeInMB()
    0.0
    >>> model.coefficients
    DenseVector([0.0, -1.0319, -0.5159])
    >>> model.intercept
    2.579645978780695
    >>> model.numClasses
    2
    >>> model.numFeatures
    3
    >>> test0 = sc.parallelize([Row(features=Vectors.dense(-1.0, -1.0, -1.0))]).toDF()
    >>> model.predict(test0.head().features)
    1.0
    >>> model.predictRaw(test0.head().features)
    DenseVector([-4.1274, 4.1274])
    >>> result = model.transform(test0).head()
    >>> result.newPrediction
    1.0
    >>> result.rawPrediction
    DenseVector([-4.1274, 4.1274])
    >>> svm_path = temp_path + "/svm"
    >>> svm.save(svm_path)
    >>> svm2 = LinearSVC.load(svm_path)
    >>> svm2.getMaxIter()
    5
    >>> model_path = temp_path + "/svm_model"
    >>> model.save(model_path)
    >>> model2 = LinearSVCModel.load(model_path)
    >>> model.coefficients[0] == model2.coefficients[0]
    True
    >>> model.intercept == model2.intercept
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxIter: int = 100, regParam: float = 0.0, tol: float = 1e-06, rawPredictionCol: str = 'rawPrediction', fitIntercept: bool = True, standardization: bool = True, threshold: float = 0.0, weightCol: str | None = None, aggregationDepth: int = 2, maxBlockSizeInMB: float = 0.0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxIter=100, regParam=0.0, tol=1e-6, rawPredictionCol="rawPrediction",                  fitIntercept=True, standardization=True, threshold=0.0, weightCol=None,                  aggregationDepth=2, maxBlockSizeInMB=0.0):
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxIter: int = 100, regParam: float = 0.0, tol: float = 1e-06, rawPredictionCol: str = 'rawPrediction', fitIntercept: bool = True, standardization: bool = True, threshold: float = 0.0, weightCol: str | None = None, aggregationDepth: int = 2, maxBlockSizeInMB: float = 0.0) -> LinearSVC:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxIter=100, regParam=0.0, tol=1e-6, rawPredictionCol="rawPrediction",                   fitIntercept=True, standardization=True, threshold=0.0, weightCol=None,                   aggregationDepth=2, maxBlockSizeInMB=0.0):
        Sets params for Linear SVM Classifier.
        '''
    def setMaxIter(self, value: int) -> LinearSVC:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setRegParam(self, value: float) -> LinearSVC:
        """
        Sets the value of :py:attr:`regParam`.
        """
    def setTol(self, value: float) -> LinearSVC:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setFitIntercept(self, value: bool) -> LinearSVC:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setStandardization(self, value: bool) -> LinearSVC:
        """
        Sets the value of :py:attr:`standardization`.
        """
    def setThreshold(self, value: float) -> LinearSVC:
        """
        Sets the value of :py:attr:`threshold`.
        """
    def setWeightCol(self, value: str) -> LinearSVC:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setAggregationDepth(self, value: int) -> LinearSVC:
        """
        Sets the value of :py:attr:`aggregationDepth`.
        """
    def setMaxBlockSizeInMB(self, value: float) -> LinearSVC:
        """
        Sets the value of :py:attr:`maxBlockSizeInMB`.
        """

class LinearSVCModel(_JavaClassificationModel[Vector], _LinearSVCParams, JavaMLWritable, JavaMLReadable['LinearSVCModel'], HasTrainingSummary['LinearSVCTrainingSummary']):
    """
    Model fitted by LinearSVC.

    .. versionadded:: 2.2.0
    """
    def setThreshold(self, value: float) -> LinearSVCModel:
        """
        Sets the value of :py:attr:`threshold`.
        """
    @property
    def coefficients(self) -> Vector:
        """
        Model coefficients of Linear SVM Classifier.
        """
    @property
    def intercept(self) -> float:
        """
        Model intercept of Linear SVM Classifier.
        """
    def summary(self) -> LinearSVCTrainingSummary:
        """
        Gets summary (accuracy/precision/recall, objective history, total iterations) of model
        trained on the training set. An exception is thrown if `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> LinearSVCSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 3.1.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on.
        """

class LinearSVCSummary(_BinaryClassificationSummary):
    """
    Abstraction for LinearSVC Results for a given model.

    .. versionadded:: 3.1.0
    """
class LinearSVCTrainingSummary(LinearSVCSummary, _TrainingSummary):
    """
    Abstraction for LinearSVC Training results.

    .. versionadded:: 3.1.0
    """

class _LogisticRegressionParams(_ProbabilisticClassifierParams, HasRegParam, HasElasticNetParam, HasMaxIter, HasFitIntercept, HasTol, HasStandardization, HasWeightCol, HasAggregationDepth, HasThreshold, HasMaxBlockSizeInMB):
    """
    Params for :py:class:`LogisticRegression` and :py:class:`LogisticRegressionModel`.

    .. versionadded:: 3.0.0
    """
    threshold: Param[float]
    family: Param[str]
    lowerBoundsOnCoefficients: Param[Matrix]
    upperBoundsOnCoefficients: Param[Matrix]
    lowerBoundsOnIntercepts: Param[Vector]
    upperBoundsOnIntercepts: Param[Vector]
    def __init__(self, *args: Any) -> None: ...
    def setThreshold(self, value: float) -> P:
        """
        Sets the value of :py:attr:`threshold`.
        Clears value of :py:attr:`thresholds` if it has been set.
        """
    def getThreshold(self) -> float:
        """
        Get threshold for binary classification.

        If :py:attr:`thresholds` is set with length 2 (i.e., binary classification),
        this returns the equivalent threshold:
        :math:`\\frac{1}{1 + \\frac{thresholds(0)}{thresholds(1)}}`.
        Otherwise, returns :py:attr:`threshold` if set or its default value if unset.
        """
    def setThresholds(self, value: List[float]) -> P:
        """
        Sets the value of :py:attr:`thresholds`.
        Clears value of :py:attr:`threshold` if it has been set.
        """
    def getThresholds(self) -> List[float]:
        """
        If :py:attr:`thresholds` is set, return its value.
        Otherwise, if :py:attr:`threshold` is set, return the equivalent thresholds for binary
        classification: (1-threshold, threshold).
        If neither are set, throw an error.
        """
    def getFamily(self) -> str:
        """
        Gets the value of :py:attr:`family` or its default value.
        """
    def getLowerBoundsOnCoefficients(self) -> Matrix:
        """
        Gets the value of :py:attr:`lowerBoundsOnCoefficients`
        """
    def getUpperBoundsOnCoefficients(self) -> Matrix:
        """
        Gets the value of :py:attr:`upperBoundsOnCoefficients`
        """
    def getLowerBoundsOnIntercepts(self) -> Vector:
        """
        Gets the value of :py:attr:`lowerBoundsOnIntercepts`
        """
    def getUpperBoundsOnIntercepts(self) -> Vector:
        """
        Gets the value of :py:attr:`upperBoundsOnIntercepts`
        """

class LogisticRegression(_JavaProbabilisticClassifier['LogisticRegressionModel'], _LogisticRegressionParams, JavaMLWritable, JavaMLReadable['LogisticRegression']):
    '''
    Logistic regression.
    This class supports multinomial logistic (softmax) and binomial logistic regression.

    .. versionadded:: 1.3.0

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> from pyspark.ml.linalg import Vectors
    >>> bdf = sc.parallelize([
    ...     Row(label=1.0, weight=1.0, features=Vectors.dense(0.0, 5.0)),
    ...     Row(label=0.0, weight=2.0, features=Vectors.dense(1.0, 2.0)),
    ...     Row(label=1.0, weight=3.0, features=Vectors.dense(2.0, 1.0)),
    ...     Row(label=0.0, weight=4.0, features=Vectors.dense(3.0, 3.0))]).toDF()
    >>> blor = LogisticRegression(weightCol="weight")
    >>> blor.getRegParam()
    0.0
    >>> blor.setRegParam(0.01)
    LogisticRegression...
    >>> blor.getRegParam()
    0.01
    >>> blor.setMaxIter(10)
    LogisticRegression...
    >>> blor.getMaxIter()
    10
    >>> blor.clear(blor.maxIter)
    >>> blorModel = blor.fit(bdf)
    >>> blorModel.setFeaturesCol("features")
    LogisticRegressionModel...
    >>> blorModel.setProbabilityCol("newProbability")
    LogisticRegressionModel...
    >>> blorModel.getProbabilityCol()
    \'newProbability\'
    >>> blorModel.getMaxBlockSizeInMB()
    0.0
    >>> blorModel.setThreshold(0.1)
    LogisticRegressionModel...
    >>> blorModel.getThreshold()
    0.1
    >>> blorModel.coefficients
    DenseVector([-1.080..., -0.646...])
    >>> blorModel.intercept
    3.112...
    >>> blorModel.evaluate(bdf).accuracy == blorModel.summary.accuracy
    True
    >>> data_path = "data/mllib/sample_multiclass_classification_data.txt"
    >>> mdf = spark.read.format("libsvm").load(data_path)
    >>> mlor = LogisticRegression(regParam=0.1, elasticNetParam=1.0, family="multinomial")
    >>> mlorModel = mlor.fit(mdf)
    >>> mlorModel.coefficientMatrix
    SparseMatrix(3, 4, [0, 1, 2, 3], [3, 2, 1], [1.87..., -2.75..., -0.50...], 1)
    >>> mlorModel.interceptVector
    DenseVector([0.04..., -0.42..., 0.37...])
    >>> test0 = sc.parallelize([Row(features=Vectors.dense(-1.0, 1.0))]).toDF()
    >>> blorModel.predict(test0.head().features)
    1.0
    >>> blorModel.predictRaw(test0.head().features)
    DenseVector([-3.54..., 3.54...])
    >>> blorModel.predictProbability(test0.head().features)
    DenseVector([0.028, 0.972])
    >>> result = blorModel.transform(test0).head()
    >>> result.prediction
    1.0
    >>> result.newProbability
    DenseVector([0.02..., 0.97...])
    >>> result.rawPrediction
    DenseVector([-3.54..., 3.54...])
    >>> test1 = sc.parallelize([Row(features=Vectors.sparse(2, [0], [1.0]))]).toDF()
    >>> blorModel.transform(test1).head().prediction
    1.0
    >>> blor.setParams("vector")
    Traceback (most recent call last):
        ...
    TypeError: Method setParams forces keyword arguments.
    >>> lr_path = temp_path + "/lr"
    >>> blor.save(lr_path)
    >>> lr2 = LogisticRegression.load(lr_path)
    >>> lr2.getRegParam()
    0.01
    >>> model_path = temp_path + "/lr_model"
    >>> blorModel.save(model_path)
    >>> model2 = LogisticRegressionModel.load(model_path)
    >>> blorModel.coefficients[0] == model2.coefficients[0]
    True
    >>> blorModel.intercept == model2.intercept
    True
    >>> model2
    LogisticRegressionModel: uid=..., numClasses=2, numFeatures=2
    >>> blorModel.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    @overload
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., threshold: float = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., standardization: bool = ..., weightCol: str | None = ..., aggregationDepth: int = ..., family: str = ..., lowerBoundsOnCoefficients: Matrix | None = ..., upperBoundsOnCoefficients: Matrix | None = ..., lowerBoundsOnIntercepts: Vector | None = ..., upperBoundsOnIntercepts: Vector | None = ..., maxBlockSizeInMB: float = ...) -> None: ...
    @overload
    def __init__(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., thresholds: List[float] | None = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., standardization: bool = ..., weightCol: str | None = ..., aggregationDepth: int = ..., family: str = ..., lowerBoundsOnCoefficients: Matrix | None = ..., upperBoundsOnCoefficients: Matrix | None = ..., lowerBoundsOnIntercepts: Vector | None = ..., upperBoundsOnIntercepts: Vector | None = ..., maxBlockSizeInMB: float = ...) -> None: ...
    @overload
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., threshold: float = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., standardization: bool = ..., weightCol: str | None = ..., aggregationDepth: int = ..., family: str = ..., lowerBoundsOnCoefficients: Matrix | None = ..., upperBoundsOnCoefficients: Matrix | None = ..., lowerBoundsOnIntercepts: Vector | None = ..., upperBoundsOnIntercepts: Vector | None = ..., maxBlockSizeInMB: float = ...) -> LogisticRegression: ...
    @overload
    def setParams(self, *, featuresCol: str = ..., labelCol: str = ..., predictionCol: str = ..., maxIter: int = ..., regParam: float = ..., elasticNetParam: float = ..., tol: float = ..., fitIntercept: bool = ..., thresholds: List[float] | None = ..., probabilityCol: str = ..., rawPredictionCol: str = ..., standardization: bool = ..., weightCol: str | None = ..., aggregationDepth: int = ..., family: str = ..., lowerBoundsOnCoefficients: Matrix | None = ..., upperBoundsOnCoefficients: Matrix | None = ..., lowerBoundsOnIntercepts: Vector | None = ..., upperBoundsOnIntercepts: Vector | None = ..., maxBlockSizeInMB: float = ...) -> LogisticRegression: ...
    def setFamily(self, value: str) -> LogisticRegression:
        """
        Sets the value of :py:attr:`family`.
        """
    def setLowerBoundsOnCoefficients(self, value: Matrix) -> LogisticRegression:
        """
        Sets the value of :py:attr:`lowerBoundsOnCoefficients`
        """
    def setUpperBoundsOnCoefficients(self, value: Matrix) -> LogisticRegression:
        """
        Sets the value of :py:attr:`upperBoundsOnCoefficients`
        """
    def setLowerBoundsOnIntercepts(self, value: Vector) -> LogisticRegression:
        """
        Sets the value of :py:attr:`lowerBoundsOnIntercepts`
        """
    def setUpperBoundsOnIntercepts(self, value: Vector) -> LogisticRegression:
        """
        Sets the value of :py:attr:`upperBoundsOnIntercepts`
        """
    def setMaxIter(self, value: int) -> LogisticRegression:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setRegParam(self, value: float) -> LogisticRegression:
        """
        Sets the value of :py:attr:`regParam`.
        """
    def setTol(self, value: float) -> LogisticRegression:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setElasticNetParam(self, value: float) -> LogisticRegression:
        """
        Sets the value of :py:attr:`elasticNetParam`.
        """
    def setFitIntercept(self, value: bool) -> LogisticRegression:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setStandardization(self, value: bool) -> LogisticRegression:
        """
        Sets the value of :py:attr:`standardization`.
        """
    def setWeightCol(self, value: str) -> LogisticRegression:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setAggregationDepth(self, value: int) -> LogisticRegression:
        """
        Sets the value of :py:attr:`aggregationDepth`.
        """
    def setMaxBlockSizeInMB(self, value: float) -> LogisticRegression:
        """
        Sets the value of :py:attr:`maxBlockSizeInMB`.
        """

class LogisticRegressionModel(_JavaProbabilisticClassificationModel[Vector], _LogisticRegressionParams, JavaMLWritable, JavaMLReadable['LogisticRegressionModel'], HasTrainingSummary['LogisticRegressionTrainingSummary']):
    """
    Model fitted by LogisticRegression.

    .. versionadded:: 1.3.0
    """
    @property
    def coefficients(self) -> Vector:
        """
        Model coefficients of binomial logistic regression.
        An exception is thrown in the case of multinomial logistic regression.
        """
    @property
    def intercept(self) -> float:
        """
        Model intercept of binomial logistic regression.
        An exception is thrown in the case of multinomial logistic regression.
        """
    @property
    def coefficientMatrix(self) -> Matrix:
        """
        Model coefficients.
        """
    @property
    def interceptVector(self) -> Vector:
        """
        Model intercept.
        """
    @property
    def summary(self) -> LogisticRegressionTrainingSummary:
        """
        Gets summary (accuracy/precision/recall, objective history, total iterations) of model
        trained on the training set. An exception is thrown if `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> LogisticRegressionSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on.
        """

class LogisticRegressionSummary(_ClassificationSummary):
    """
    Abstraction for Logistic Regression Results for a given model.

    .. versionadded:: 2.0.0
    """
    @property
    def probabilityCol(self) -> str:
        '''
        Field in "predictions" which gives the probability
        of each class as a vector.
        '''
    @property
    def featuresCol(self) -> str:
        '''
        Field in "predictions" which gives the features of each instance
        as a vector.
        '''

class LogisticRegressionTrainingSummary(LogisticRegressionSummary, _TrainingSummary):
    """
    Abstraction for multinomial Logistic Regression Training results.

    .. versionadded:: 2.0.0
    """
class BinaryLogisticRegressionSummary(_BinaryClassificationSummary, LogisticRegressionSummary):
    """
    Binary Logistic regression results for a given model.

    .. versionadded:: 2.0.0
    """
class BinaryLogisticRegressionTrainingSummary(BinaryLogisticRegressionSummary, LogisticRegressionTrainingSummary):
    """
    Binary Logistic regression training results for a given model.

    .. versionadded:: 2.0.0
    """

class _DecisionTreeClassifierParams(_DecisionTreeParams, _TreeClassifierParams):
    """
    Params for :py:class:`DecisionTreeClassifier` and :py:class:`DecisionTreeClassificationModel`.
    """
    def __init__(self, *args: Any) -> None: ...

class DecisionTreeClassifier(_JavaProbabilisticClassifier['DecisionTreeClassificationModel'], _DecisionTreeClassifierParams, JavaMLWritable, JavaMLReadable['DecisionTreeClassifier']):
    '''
    `Decision tree <http://en.wikipedia.org/wiki/Decision_tree_learning>`_
    learning algorithm for classification.
    It supports both binary and multiclass labels, as well as both continuous and categorical
    features.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.feature import StringIndexer
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> stringIndexer = StringIndexer(inputCol="label", outputCol="indexed")
    >>> si_model = stringIndexer.fit(df)
    >>> td = si_model.transform(df)
    >>> dt = DecisionTreeClassifier(maxDepth=2, labelCol="indexed", leafCol="leafId")
    >>> model = dt.fit(td)
    >>> model.getLabelCol()
    \'indexed\'
    >>> model.setFeaturesCol("features")
    DecisionTreeClassificationModel...
    >>> model.numNodes
    3
    >>> model.depth
    1
    >>> model.featureImportances
    SparseVector(1, {0: 1.0})
    >>> model.numFeatures
    1
    >>> model.numClasses
    2
    >>> print(model.toDebugString)
    DecisionTreeClassificationModel...depth=1, numNodes=3...
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.predict(test0.head().features)
    0.0
    >>> model.predictRaw(test0.head().features)
    DenseVector([1.0, 0.0])
    >>> model.predictProbability(test0.head().features)
    DenseVector([1.0, 0.0])
    >>> result = model.transform(test0).head()
    >>> result.prediction
    0.0
    >>> result.probability
    DenseVector([1.0, 0.0])
    >>> result.rawPrediction
    DenseVector([1.0, 0.0])
    >>> result.leafId
    0.0
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> model.transform(test1).head().prediction
    1.0
    >>> dtc_path = temp_path + "/dtc"
    >>> dt.save(dtc_path)
    >>> dt2 = DecisionTreeClassifier.load(dtc_path)
    >>> dt2.getMaxDepth()
    2
    >>> model_path = temp_path + "/dtc_model"
    >>> model.save(model_path)
    >>> model2 = DecisionTreeClassificationModel.load(model_path)
    >>> model.featureImportances == model2.featureImportances
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> df3 = spark.createDataFrame([
    ...     (1.0, 0.2, Vectors.dense(1.0)),
    ...     (1.0, 0.8, Vectors.dense(1.0)),
    ...     (0.0, 1.0, Vectors.sparse(1, [], []))], ["label", "weight", "features"])
    >>> si3 = StringIndexer(inputCol="label", outputCol="indexed")
    >>> si_model3 = si3.fit(df3)
    >>> td3 = si_model3.transform(df3)
    >>> dt3 = DecisionTreeClassifier(maxDepth=2, weightCol="weight", labelCol="indexed")
    >>> model3 = dt3.fit(td3)
    >>> print(model3.toDebugString)
    DecisionTreeClassificationModel...depth=1, numNodes=3...
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'gini', seed: int | None = None, weightCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  probabilityCol="probability", rawPredictionCol="rawPrediction",                  maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                  maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10, impurity="gini",                  seed=None, weightCol=None, leafCol="", minWeightFractionPerNode=0.0)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'gini', seed: int | None = None, weightCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0) -> DecisionTreeClassifier:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   probabilityCol="probability", rawPredictionCol="rawPrediction",                   maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                   maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10, impurity="gini",                   seed=None, weightCol=None, leafCol="", minWeightFractionPerNode=0.0)
        Sets params for the DecisionTreeClassifier.
        '''
    def setMaxDepth(self, value: int) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`maxDepth`.
        """
    def setMaxBins(self, value: int) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`maxBins`.
        """
    def setMinInstancesPerNode(self, value: int) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
    def setMinWeightFractionPerNode(self, value: float) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`minWeightFractionPerNode`.
        """
    def setMinInfoGain(self, value: float) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
    def setMaxMemoryInMB(self, value: int) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
    def setCacheNodeIds(self, value: bool) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
    def setImpurity(self, value: str) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`impurity`.
        """
    def setCheckpointInterval(self, value: int) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setWeightCol(self, value: str) -> DecisionTreeClassifier:
        """
        Sets the value of :py:attr:`weightCol`.
        """

class DecisionTreeClassificationModel(_DecisionTreeModel, _JavaProbabilisticClassificationModel[Vector], _DecisionTreeClassifierParams, JavaMLWritable, JavaMLReadable['DecisionTreeClassificationModel']):
    """
    Model fitted by DecisionTreeClassifier.

    .. versionadded:: 1.4.0
    """
    @property
    def featureImportances(self) -> Vector:
        '''
        Estimate of the importance of each feature.

        This generalizes the idea of "Gini" importance to other losses,
        following the explanation of Gini importance from "Random Forests" documentation
        by Leo Breiman and Adele Cutler, and following the implementation from scikit-learn.

        This feature importance is calculated as follows:
          - importance(feature j) = sum (over nodes which split on feature j) of the gain,
            where gain is scaled by the number of instances passing through node
          - Normalize importances for tree to sum to 1.

        .. versionadded:: 2.0.0

        Notes
        -----
        Feature importance for single decision trees can have high variance due to
        correlated predictor variables. Consider using a :py:class:`RandomForestClassifier`
        to determine feature importance instead.
        '''

class _RandomForestClassifierParams(_RandomForestParams, _TreeClassifierParams):
    """
    Params for :py:class:`RandomForestClassifier` and :py:class:`RandomForestClassificationModel`.
    """
    def __init__(self, *args: Any) -> None: ...

class RandomForestClassifier(_JavaProbabilisticClassifier['RandomForestClassificationModel'], _RandomForestClassifierParams, JavaMLWritable, JavaMLReadable['RandomForestClassifier']):
    '''
    `Random Forest <http://en.wikipedia.org/wiki/Random_forest>`_
    learning algorithm for classification.
    It supports both binary and multiclass labels, as well as both continuous and categorical
    features.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> import numpy
    >>> from numpy import allclose
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.feature import StringIndexer
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> stringIndexer = StringIndexer(inputCol="label", outputCol="indexed")
    >>> si_model = stringIndexer.fit(df)
    >>> td = si_model.transform(df)
    >>> rf = RandomForestClassifier(numTrees=3, maxDepth=2, labelCol="indexed", seed=42,
    ...     leafCol="leafId")
    >>> rf.getMinWeightFractionPerNode()
    0.0
    >>> model = rf.fit(td)
    >>> model.getLabelCol()
    \'indexed\'
    >>> model.setFeaturesCol("features")
    RandomForestClassificationModel...
    >>> model.setRawPredictionCol("newRawPrediction")
    RandomForestClassificationModel...
    >>> model.getBootstrap()
    True
    >>> model.getRawPredictionCol()
    \'newRawPrediction\'
    >>> model.featureImportances
    SparseVector(1, {0: 1.0})
    >>> allclose(model.treeWeights, [1.0, 1.0, 1.0])
    True
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.predict(test0.head().features)
    0.0
    >>> model.predictRaw(test0.head().features)
    DenseVector([2.0, 0.0])
    >>> model.predictProbability(test0.head().features)
    DenseVector([1.0, 0.0])
    >>> result = model.transform(test0).head()
    >>> result.prediction
    0.0
    >>> numpy.argmax(result.probability)
    0
    >>> numpy.argmax(result.newRawPrediction)
    0
    >>> result.leafId
    DenseVector([0.0, 0.0, 0.0])
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> model.transform(test1).head().prediction
    1.0
    >>> model.trees
    [DecisionTreeClassificationModel...depth=..., DecisionTreeClassificationModel...]
    >>> rfc_path = temp_path + "/rfc"
    >>> rf.save(rfc_path)
    >>> rf2 = RandomForestClassifier.load(rfc_path)
    >>> rf2.getNumTrees()
    3
    >>> model_path = temp_path + "/rfc_model"
    >>> model.save(model_path)
    >>> model2 = RandomForestClassificationModel.load(model_path)
    >>> model.featureImportances == model2.featureImportances
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'gini', numTrees: int = 20, featureSubsetStrategy: str = 'auto', seed: int | None = None, subsamplingRate: float = 1.0, leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None, bootstrap: bool | None = True) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  probabilityCol="probability", rawPredictionCol="rawPrediction",                  maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                  maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10, impurity="gini",                  numTrees=20, featureSubsetStrategy="auto", seed=None, subsamplingRate=1.0,                  leafCol="", minWeightFractionPerNode=0.0, weightCol=None, bootstrap=True)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'gini', numTrees: int = 20, featureSubsetStrategy: str = 'auto', seed: int | None = None, subsamplingRate: float = 1.0, leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None, bootstrap: bool | None = True) -> RandomForestClassifier:
        '''
        setParams(self, featuresCol="features", labelCol="label", predictionCol="prediction",                  probabilityCol="probability", rawPredictionCol="rawPrediction",                   maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                   maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10, seed=None,                   impurity="gini", numTrees=20, featureSubsetStrategy="auto", subsamplingRate=1.0,                   leafCol="", minWeightFractionPerNode=0.0, weightCol=None, bootstrap=True)
        Sets params for linear classification.
        '''
    def setMaxDepth(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`maxDepth`.
        """
    def setMaxBins(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`maxBins`.
        """
    def setMinInstancesPerNode(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
    def setMinInfoGain(self, value: float) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
    def setMaxMemoryInMB(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
    def setCacheNodeIds(self, value: bool) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
    def setImpurity(self, value: str) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`impurity`.
        """
    def setNumTrees(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`numTrees`.
        """
    def setBootstrap(self, value: bool) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`bootstrap`.
        """
    def setSubsamplingRate(self, value: float) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`subsamplingRate`.
        """
    def setFeatureSubsetStrategy(self, value: str) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`featureSubsetStrategy`.
        """
    def setSeed(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setCheckpointInterval(self, value: int) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setWeightCol(self, value: str) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setMinWeightFractionPerNode(self, value: float) -> RandomForestClassifier:
        """
        Sets the value of :py:attr:`minWeightFractionPerNode`.
        """

class RandomForestClassificationModel(_TreeEnsembleModel, _JavaProbabilisticClassificationModel[Vector], _RandomForestClassifierParams, JavaMLWritable, JavaMLReadable['RandomForestClassificationModel'], HasTrainingSummary['RandomForestClassificationTrainingSummary']):
    """
    Model fitted by RandomForestClassifier.

    .. versionadded:: 1.4.0
    """
    @property
    def featureImportances(self) -> Vector:
        '''
        Estimate of the importance of each feature.

        Each feature\'s importance is the average of its importance across all trees in the ensemble
        The importance vector is normalized to sum to 1. This method is suggested by Hastie et al.
        (Hastie, Tibshirani, Friedman. "The Elements of Statistical Learning, 2nd Edition." 2001.)
        and follows the implementation from scikit-learn.

        .. versionadded:: 2.0.0

        See Also
        --------
        DecisionTreeClassificationModel.featureImportances
        '''
    @property
    def trees(self) -> List[DecisionTreeClassificationModel]:
        """Trees in this ensemble. Warning: These have null parent Estimators."""
    @property
    def summary(self) -> RandomForestClassificationTrainingSummary:
        """
        Gets summary (accuracy/precision/recall, objective history, total iterations) of model
        trained on the training set. An exception is thrown if `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> BinaryRandomForestClassificationSummary | RandomForestClassificationSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 3.1.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on.
        """

class RandomForestClassificationSummary(_ClassificationSummary):
    """
    Abstraction for RandomForestClassification Results for a given model.

    .. versionadded:: 3.1.0
    """
class RandomForestClassificationTrainingSummary(RandomForestClassificationSummary, _TrainingSummary):
    """
    Abstraction for RandomForestClassificationTraining Training results.

    .. versionadded:: 3.1.0
    """
class BinaryRandomForestClassificationSummary(_BinaryClassificationSummary):
    """
    BinaryRandomForestClassification results for a given model.

    .. versionadded:: 3.1.0
    """
class BinaryRandomForestClassificationTrainingSummary(BinaryRandomForestClassificationSummary, RandomForestClassificationTrainingSummary):
    """
    BinaryRandomForestClassification training results for a given model.

    .. versionadded:: 3.1.0
    """

class _GBTClassifierParams(_GBTParams, _HasVarianceImpurity):
    """
    Params for :py:class:`GBTClassifier` and :py:class:`GBTClassifierModel`.

    .. versionadded:: 3.0.0
    """
    supportedLossTypes: List[str]
    lossType: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getLossType(self) -> str:
        """
        Gets the value of lossType or its default value.
        """

class GBTClassifier(_JavaProbabilisticClassifier['GBTClassificationModel'], _GBTClassifierParams, JavaMLWritable, JavaMLReadable['GBTClassifier']):
    '''
    `Gradient-Boosted Trees (GBTs) <http://en.wikipedia.org/wiki/Gradient_boosting>`_
    learning algorithm for classification.
    It supports binary labels, as well as both continuous and categorical features.

    .. versionadded:: 1.4.0

    Notes
    -----
    Multiclass labels are not currently supported.

    The implementation is based upon: J.H. Friedman. "Stochastic Gradient Boosting." 1999.

    Gradient Boosting vs. TreeBoost:

    - This implementation is for Stochastic Gradient Boosting, not for TreeBoost.
    - Both algorithms learn tree ensembles by minimizing loss functions.
    - TreeBoost (Friedman, 1999) additionally modifies the outputs at tree leaf nodes
      based on the loss function, whereas the original gradient boosting method does not.
    - We expect to implement TreeBoost in the future:
      `SPARK-4240 <https://issues.apache.org/jira/browse/SPARK-4240>`_

    Examples
    --------
    >>> from numpy import allclose
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.feature import StringIndexer
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> stringIndexer = StringIndexer(inputCol="label", outputCol="indexed")
    >>> si_model = stringIndexer.fit(df)
    >>> td = si_model.transform(df)
    >>> gbt = GBTClassifier(maxIter=5, maxDepth=2, labelCol="indexed", seed=42,
    ...     leafCol="leafId")
    >>> gbt.setMaxIter(5)
    GBTClassifier...
    >>> gbt.setMinWeightFractionPerNode(0.049)
    GBTClassifier...
    >>> gbt.getMaxIter()
    5
    >>> gbt.getFeatureSubsetStrategy()
    \'all\'
    >>> model = gbt.fit(td)
    >>> model.getLabelCol()
    \'indexed\'
    >>> model.setFeaturesCol("features")
    GBTClassificationModel...
    >>> model.setThresholds([0.3, 0.7])
    GBTClassificationModel...
    >>> model.getThresholds()
    [0.3, 0.7]
    >>> model.featureImportances
    SparseVector(1, {0: 1.0})
    >>> allclose(model.treeWeights, [1.0, 0.1, 0.1, 0.1, 0.1])
    True
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.predict(test0.head().features)
    0.0
    >>> model.predictRaw(test0.head().features)
    DenseVector([1.1697, -1.1697])
    >>> model.predictProbability(test0.head().features)
    DenseVector([0.9121, 0.0879])
    >>> result = model.transform(test0).head()
    >>> result.prediction
    0.0
    >>> result.leafId
    DenseVector([0.0, 0.0, 0.0, 0.0, 0.0])
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> model.transform(test1).head().prediction
    1.0
    >>> model.totalNumNodes
    15
    >>> print(model.toDebugString)
    GBTClassificationModel...numTrees=5...
    >>> gbtc_path = temp_path + "gbtc"
    >>> gbt.save(gbtc_path)
    >>> gbt2 = GBTClassifier.load(gbtc_path)
    >>> gbt2.getMaxDepth()
    2
    >>> model_path = temp_path + "gbtc_model"
    >>> model.save(model_path)
    >>> model2 = GBTClassificationModel.load(model_path)
    >>> model.featureImportances == model2.featureImportances
    True
    >>> model.treeWeights == model2.treeWeights
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> model.trees
    [DecisionTreeRegressionModel...depth=..., DecisionTreeRegressionModel...]
    >>> validation = spark.createDataFrame([(0.0, Vectors.dense(-1.0),)],
    ...              ["indexed", "features"])
    >>> model.evaluateEachIteration(validation)
    [0.25..., 0.23..., 0.21..., 0.19..., 0.18...]
    >>> model.numClasses
    2
    >>> gbt = gbt.setValidationIndicatorCol("validationIndicator")
    >>> gbt.getValidationIndicatorCol()
    \'validationIndicator\'
    >>> gbt.getValidationTol()
    0.01
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, lossType: str = 'logistic', maxIter: int = 20, stepSize: float = 0.1, seed: int | None = None, subsamplingRate: float = 1.0, impurity: str = 'variance', featureSubsetStrategy: str = 'all', validationTol: float = 0.01, validationIndicatorCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                  maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10,                  lossType="logistic", maxIter=20, stepSize=0.1, seed=None, subsamplingRate=1.0,                  impurity="variance", featureSubsetStrategy="all", validationTol=0.01,                  validationIndicatorCol=None, leafCol="", minWeightFractionPerNode=0.0,                  weightCol=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, lossType: str = 'logistic', maxIter: int = 20, stepSize: float = 0.1, seed: int | None = None, subsamplingRate: float = 1.0, impurity: str = 'variance', featureSubsetStrategy: str = 'all', validationTol: float = 0.01, validationIndicatorCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None) -> GBTClassifier:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                   maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10,                   lossType="logistic", maxIter=20, stepSize=0.1, seed=None, subsamplingRate=1.0,                   impurity="variance", featureSubsetStrategy="all", validationTol=0.01,                   validationIndicatorCol=None, leafCol="", minWeightFractionPerNode=0.0,                   weightCol=None)
        Sets params for Gradient Boosted Tree Classification.
        '''
    def setMaxDepth(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`maxDepth`.
        """
    def setMaxBins(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`maxBins`.
        """
    def setMinInstancesPerNode(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
    def setMinInfoGain(self, value: float) -> GBTClassifier:
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
    def setMaxMemoryInMB(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
    def setCacheNodeIds(self, value: bool) -> GBTClassifier:
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
    def setImpurity(self, value: str) -> GBTClassifier:
        """
        Sets the value of :py:attr:`impurity`.
        """
    def setLossType(self, value: str) -> GBTClassifier:
        """
        Sets the value of :py:attr:`lossType`.
        """
    def setSubsamplingRate(self, value: float) -> GBTClassifier:
        """
        Sets the value of :py:attr:`subsamplingRate`.
        """
    def setFeatureSubsetStrategy(self, value: str) -> GBTClassifier:
        """
        Sets the value of :py:attr:`featureSubsetStrategy`.
        """
    def setValidationIndicatorCol(self, value: str) -> GBTClassifier:
        """
        Sets the value of :py:attr:`validationIndicatorCol`.
        """
    def setMaxIter(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setCheckpointInterval(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setStepSize(self, value: int) -> GBTClassifier:
        """
        Sets the value of :py:attr:`stepSize`.
        """
    def setWeightCol(self, value: str) -> GBTClassifier:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setMinWeightFractionPerNode(self, value: float) -> GBTClassifier:
        """
        Sets the value of :py:attr:`minWeightFractionPerNode`.
        """

class GBTClassificationModel(_TreeEnsembleModel, _JavaProbabilisticClassificationModel[Vector], _GBTClassifierParams, JavaMLWritable, JavaMLReadable['GBTClassificationModel']):
    """
    Model fitted by GBTClassifier.

    .. versionadded:: 1.4.0
    """
    @property
    def featureImportances(self) -> Vector:
        '''
        Estimate of the importance of each feature.

        Each feature\'s importance is the average of its importance across all trees in the ensemble
        The importance vector is normalized to sum to 1. This method is suggested by Hastie et al.
        (Hastie, Tibshirani, Friedman. "The Elements of Statistical Learning, 2nd Edition." 2001.)
        and follows the implementation from scikit-learn.

        .. versionadded:: 2.0.0

        See Also
        --------
        DecisionTreeClassificationModel.featureImportances
        '''
    @property
    def trees(self) -> List[DecisionTreeRegressionModel]:
        """Trees in this ensemble. Warning: These have null parent Estimators."""
    def evaluateEachIteration(self, dataset: DataFrame) -> List[float]:
        """
        Method to compute error or loss for every iteration of gradient boosting.

        .. versionadded:: 2.4.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on.
        """

class _NaiveBayesParams(_PredictorParams, HasWeightCol):
    """
    Params for :py:class:`NaiveBayes` and :py:class:`NaiveBayesModel`.

    .. versionadded:: 3.0.0
    """
    smoothing: Param[float]
    modelType: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getSmoothing(self) -> float:
        """
        Gets the value of smoothing or its default value.
        """
    def getModelType(self) -> str:
        """
        Gets the value of modelType or its default value.
        """

class NaiveBayes(_JavaProbabilisticClassifier['NaiveBayesModel'], _NaiveBayesParams, HasThresholds, HasWeightCol, JavaMLWritable, JavaMLReadable['NaiveBayes']):
    '''
    Naive Bayes Classifiers.
    It supports both Multinomial and Bernoulli NB. `Multinomial NB     <http://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html>`_
    can handle finitely supported discrete data. For example, by converting documents into
    TF-IDF vectors, it can be used for document classification. By making every vector a
    binary (0/1) data, it can also be used as `Bernoulli NB     <http://nlp.stanford.edu/IR-book/html/htmledition/the-bernoulli-model-1.html>`_.

    The input feature values for Multinomial NB and Bernoulli NB must be nonnegative.
    Since 3.0.0, it supports Complement NB which is an adaptation of the Multinomial NB.
    Specifically, Complement NB uses statistics from the complement of each class to compute
    the model\'s coefficients. The inventors of Complement NB show empirically that the parameter
    estimates for CNB are more stable than those for Multinomial NB. Like Multinomial NB, the
    input feature values for Complement NB must be nonnegative.
    Since 3.0.0, it also supports `Gaussian NB     <https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gaussian_naive_Bayes>`_.
    which can handle continuous data.

    .. versionadded:: 1.5.0

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     Row(label=0.0, weight=0.1, features=Vectors.dense([0.0, 0.0])),
    ...     Row(label=0.0, weight=0.5, features=Vectors.dense([0.0, 1.0])),
    ...     Row(label=1.0, weight=1.0, features=Vectors.dense([1.0, 0.0]))])
    >>> nb = NaiveBayes(smoothing=1.0, modelType="multinomial", weightCol="weight")
    >>> model = nb.fit(df)
    >>> model.setFeaturesCol("features")
    NaiveBayesModel...
    >>> model.getSmoothing()
    1.0
    >>> model.pi
    DenseVector([-0.81..., -0.58...])
    >>> model.theta
    DenseMatrix(2, 2, [-0.91..., -0.51..., -0.40..., -1.09...], 1)
    >>> model.sigma
    DenseMatrix(0, 0, [...], ...)
    >>> test0 = sc.parallelize([Row(features=Vectors.dense([1.0, 0.0]))]).toDF()
    >>> model.predict(test0.head().features)
    1.0
    >>> model.predictRaw(test0.head().features)
    DenseVector([-1.72..., -0.99...])
    >>> model.predictProbability(test0.head().features)
    DenseVector([0.32..., 0.67...])
    >>> result = model.transform(test0).head()
    >>> result.prediction
    1.0
    >>> result.probability
    DenseVector([0.32..., 0.67...])
    >>> result.rawPrediction
    DenseVector([-1.72..., -0.99...])
    >>> test1 = sc.parallelize([Row(features=Vectors.sparse(2, [0], [1.0]))]).toDF()
    >>> model.transform(test1).head().prediction
    1.0
    >>> nb_path = temp_path + "/nb"
    >>> nb.save(nb_path)
    >>> nb2 = NaiveBayes.load(nb_path)
    >>> nb2.getSmoothing()
    1.0
    >>> model_path = temp_path + "/nb_model"
    >>> model.save(model_path)
    >>> model2 = NaiveBayesModel.load(model_path)
    >>> model.pi == model2.pi
    True
    >>> model.theta == model2.theta
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> nb = nb.setThresholds([0.01, 10.00])
    >>> model3 = nb.fit(df)
    >>> result = model3.transform(test0).head()
    >>> result.prediction
    0.0
    >>> nb3 = NaiveBayes().setModelType("gaussian")
    >>> model4 = nb3.fit(df)
    >>> model4.getModelType()
    \'gaussian\'
    >>> model4.sigma
    DenseMatrix(2, 2, [0.0, 0.25, 0.0, 0.0], 1)
    >>> nb5 = NaiveBayes(smoothing=1.0, modelType="complement", weightCol="weight")
    >>> model5 = nb5.fit(df)
    >>> model5.getModelType()
    \'complement\'
    >>> model5.theta
    DenseMatrix(2, 2, [...], 1)
    >>> model5.sigma
    DenseMatrix(0, 0, [...], ...)
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', smoothing: float = 1.0, modelType: str = 'multinomial', thresholds: List[float] | None = None, weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  probabilityCol="probability", rawPredictionCol="rawPrediction", smoothing=1.0,                  modelType="multinomial", thresholds=None, weightCol=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', smoothing: float = 1.0, modelType: str = 'multinomial', thresholds: List[float] | None = None, weightCol: str | None = None) -> NaiveBayes:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   probabilityCol="probability", rawPredictionCol="rawPrediction", smoothing=1.0,                   modelType="multinomial", thresholds=None, weightCol=None)
        Sets params for Naive Bayes.
        '''
    def setSmoothing(self, value: float) -> NaiveBayes:
        """
        Sets the value of :py:attr:`smoothing`.
        """
    def setModelType(self, value: str) -> NaiveBayes:
        """
        Sets the value of :py:attr:`modelType`.
        """
    def setWeightCol(self, value: str) -> NaiveBayes:
        """
        Sets the value of :py:attr:`weightCol`.
        """

class NaiveBayesModel(_JavaProbabilisticClassificationModel[Vector], _NaiveBayesParams, JavaMLWritable, JavaMLReadable['NaiveBayesModel']):
    """
    Model fitted by NaiveBayes.

    .. versionadded:: 1.5.0
    """
    @property
    def pi(self) -> Vector:
        """
        log of class priors.
        """
    @property
    def theta(self) -> Matrix:
        """
        log of class conditional probabilities.
        """
    @property
    def sigma(self) -> Matrix:
        """
        variance of each feature.
        """

class _MultilayerPerceptronParams(_ProbabilisticClassifierParams, HasSeed, HasMaxIter, HasTol, HasStepSize, HasSolver, HasBlockSize):
    """
    Params for :py:class:`MultilayerPerceptronClassifier`.

    .. versionadded:: 3.0.0
    """
    layers: Param[List[int]]
    solver: Param[str]
    initialWeights: Param[Vector]
    def __init__(self, *args: Any) -> None: ...
    def getLayers(self) -> List[int]:
        """
        Gets the value of layers or its default value.
        """
    def getInitialWeights(self) -> Vector:
        """
        Gets the value of initialWeights or its default value.
        """

class MultilayerPerceptronClassifier(_JavaProbabilisticClassifier['MultilayerPerceptronClassificationModel'], _MultilayerPerceptronParams, JavaMLWritable, JavaMLReadable['MultilayerPerceptronClassifier']):
    '''
    Classifier trainer based on the Multilayer Perceptron.
    Each layer has sigmoid activation function, output layer has softmax.
    Number of inputs has to be equal to the size of feature vectors.
    Number of outputs has to be equal to the total number of labels.

    .. versionadded:: 1.6.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (0.0, Vectors.dense([0.0, 0.0])),
    ...     (1.0, Vectors.dense([0.0, 1.0])),
    ...     (1.0, Vectors.dense([1.0, 0.0])),
    ...     (0.0, Vectors.dense([1.0, 1.0]))], ["label", "features"])
    >>> mlp = MultilayerPerceptronClassifier(layers=[2, 2, 2], seed=123)
    >>> mlp.setMaxIter(100)
    MultilayerPerceptronClassifier...
    >>> mlp.getMaxIter()
    100
    >>> mlp.getBlockSize()
    128
    >>> mlp.setBlockSize(1)
    MultilayerPerceptronClassifier...
    >>> mlp.getBlockSize()
    1
    >>> model = mlp.fit(df)
    >>> model.setFeaturesCol("features")
    MultilayerPerceptronClassificationModel...
    >>> model.getMaxIter()
    100
    >>> model.getLayers()
    [2, 2, 2]
    >>> model.weights.size
    12
    >>> testDF = spark.createDataFrame([
    ...     (Vectors.dense([1.0, 0.0]),),
    ...     (Vectors.dense([0.0, 0.0]),)], ["features"])
    >>> model.predict(testDF.head().features)
    1.0
    >>> model.predictRaw(testDF.head().features)
    DenseVector([-16.208, 16.344])
    >>> model.predictProbability(testDF.head().features)
    DenseVector([0.0, 1.0])
    >>> model.transform(testDF).select("features", "prediction").show()
    +---------+----------+
    | features|prediction|
    +---------+----------+
    |[1.0,0.0]|       1.0|
    |[0.0,0.0]|       0.0|
    +---------+----------+
    ...
    >>> mlp_path = temp_path + "/mlp"
    >>> mlp.save(mlp_path)
    >>> mlp2 = MultilayerPerceptronClassifier.load(mlp_path)
    >>> mlp2.getBlockSize()
    1
    >>> model_path = temp_path + "/mlp_model"
    >>> model.save(model_path)
    >>> model2 = MultilayerPerceptronClassificationModel.load(model_path)
    >>> model.getLayers() == model2.getLayers()
    True
    >>> model.weights == model2.weights
    True
    >>> model.transform(testDF).take(1) == model2.transform(testDF).take(1)
    True
    >>> mlp2 = mlp2.setInitialWeights(list(range(0, 12)))
    >>> model3 = mlp2.fit(df)
    >>> model3.weights != model2.weights
    True
    >>> model3.getLayers() == model.getLayers()
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxIter: int = 100, tol: float = 1e-06, seed: int | None = None, layers: List[int] | None = None, blockSize: int = 128, stepSize: float = 0.03, solver: str = 'l-bfgs', initialWeights: Vector | None = None, probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction') -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxIter=100, tol=1e-6, seed=None, layers=None, blockSize=128, stepSize=0.03,                  solver="l-bfgs", initialWeights=None, probabilityCol="probability",                  rawPredictionCol="rawPrediction")
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxIter: int = 100, tol: float = 1e-06, seed: int | None = None, layers: List[int] | None = None, blockSize: int = 128, stepSize: float = 0.03, solver: str = 'l-bfgs', initialWeights: Vector | None = None, probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction') -> MultilayerPerceptronClassifier:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxIter=100, tol=1e-6, seed=None, layers=None, blockSize=128, stepSize=0.03,                   solver="l-bfgs", initialWeights=None, probabilityCol="probability",                   rawPredictionCol="rawPrediction"):
        Sets params for MultilayerPerceptronClassifier.
        '''
    def setLayers(self, value: List[int]) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`layers`.
        """
    def setBlockSize(self, value: int) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`blockSize`.
        """
    def setInitialWeights(self, value: Vector) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`initialWeights`.
        """
    def setMaxIter(self, value: int) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setSeed(self, value: int) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setTol(self, value: float) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setStepSize(self, value: float) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`stepSize`.
        """
    def setSolver(self, value: str) -> MultilayerPerceptronClassifier:
        """
        Sets the value of :py:attr:`solver`.
        """

class MultilayerPerceptronClassificationModel(_JavaProbabilisticClassificationModel[Vector], _MultilayerPerceptronParams, JavaMLWritable, JavaMLReadable['MultilayerPerceptronClassificationModel'], HasTrainingSummary['MultilayerPerceptronClassificationTrainingSummary']):
    """
    Model fitted by MultilayerPerceptronClassifier.

    .. versionadded:: 1.6.0
    """
    @property
    def weights(self) -> Vector:
        """
        the weights of layers.
        """
    def summary(self) -> MultilayerPerceptronClassificationTrainingSummary:
        """
        Gets summary (accuracy/precision/recall, objective history, total iterations) of model
        trained on the training set. An exception is thrown if `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> MultilayerPerceptronClassificationSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 3.1.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on.
        """

class MultilayerPerceptronClassificationSummary(_ClassificationSummary):
    """
    Abstraction for MultilayerPerceptronClassifier Results for a given model.

    .. versionadded:: 3.1.0
    """
class MultilayerPerceptronClassificationTrainingSummary(MultilayerPerceptronClassificationSummary, _TrainingSummary):
    """
    Abstraction for MultilayerPerceptronClassifier Training results.

    .. versionadded:: 3.1.0
    """

class _OneVsRestParams(_ClassifierParams, HasWeightCol):
    """
    Params for :py:class:`OneVsRest` and :py:class:`OneVsRestModelModel`.
    """
    classifier: Param[Classifier]
    def getClassifier(self) -> Classifier:
        """
        Gets the value of classifier or its default value.
        """

class OneVsRest(Estimator['OneVsRestModel'], _OneVsRestParams, HasParallelism, MLReadable['OneVsRest'], MLWritable, Generic[CM]):
    '''
    Reduction of Multiclass Classification to Binary Classification.
    Performs reduction using one against all strategy.
    For a multiclass classification with k classes, train k models (one per class).
    Each example is scored against all k models and the model with highest score
    is picked to label the example.

    .. versionadded:: 2.0.0

    Examples
    --------
    >>> from pyspark.sql import Row
    >>> from pyspark.ml.linalg import Vectors
    >>> data_path = "data/mllib/sample_multiclass_classification_data.txt"
    >>> df = spark.read.format("libsvm").load(data_path)
    >>> lr = LogisticRegression(regParam=0.01)
    >>> ovr = OneVsRest(classifier=lr)
    >>> ovr.getRawPredictionCol()
    \'rawPrediction\'
    >>> ovr.setPredictionCol("newPrediction")
    OneVsRest...
    >>> model = ovr.fit(df)
    >>> model.models[0].coefficients
    DenseVector([0.5..., -1.0..., 3.4..., 4.2...])
    >>> model.models[1].coefficients
    DenseVector([-2.1..., 3.1..., -2.6..., -2.3...])
    >>> model.models[2].coefficients
    DenseVector([0.3..., -3.4..., 1.0..., -1.1...])
    >>> [x.intercept for x in model.models]
    [-2.7..., -2.5..., -1.3...]
    >>> test0 = sc.parallelize([Row(features=Vectors.dense(-1.0, 0.0, 1.0, 1.0))]).toDF()
    >>> model.transform(test0).head().newPrediction
    0.0
    >>> test1 = sc.parallelize([Row(features=Vectors.sparse(4, [0], [1.0]))]).toDF()
    >>> model.transform(test1).head().newPrediction
    2.0
    >>> test2 = sc.parallelize([Row(features=Vectors.dense(0.5, 0.4, 0.3, 0.2))]).toDF()
    >>> model.transform(test2).head().newPrediction
    0.0
    >>> model_path = temp_path + "/ovr_model"
    >>> model.save(model_path)
    >>> model2 = OneVsRestModel.load(model_path)
    >>> model2.transform(test0).head().newPrediction
    0.0
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> model.transform(test2).columns
    [\'features\', \'rawPrediction\', \'newPrediction\']
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', rawPredictionCol: str = 'rawPrediction', classifier: Classifier[CM] | None = None, weightCol: str | None = None, parallelism: int = 1) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  rawPredictionCol="rawPrediction", classifier=None, weightCol=None, parallelism=1):
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', rawPredictionCol: str = 'rawPrediction', classifier: Classifier[CM] | None = None, weightCol: str | None = None, parallelism: int = 1) -> OneVsRest:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   rawPredictionCol="rawPrediction", classifier=None, weightCol=None, parallelism=1):
        Sets params for OneVsRest.
        '''
    def setClassifier(self, value: Classifier[CM]) -> OneVsRest:
        """
        Sets the value of :py:attr:`classifier`.
        """
    def setLabelCol(self, value: str) -> OneVsRest:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setFeaturesCol(self, value: str) -> OneVsRest:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> OneVsRest:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setRawPredictionCol(self, value: str) -> OneVsRest:
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """
    def setWeightCol(self, value: str) -> OneVsRest:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setParallelism(self, value: int) -> OneVsRest:
        """
        Sets the value of :py:attr:`parallelism`.
        """
    def copy(self, extra: ParamMap | None = None) -> OneVsRest:
        """
        Creates a copy of this instance with a randomly generated uid
        and some extra params. This creates a deep copy of the embedded paramMap,
        and copies the embedded and extra parameters over.

        .. versionadded:: 2.0.0

        Examples
        --------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`OneVsRest`
            Copy of this instance
        """
    @classmethod
    def read(cls) -> OneVsRestReader: ...
    def write(self) -> MLWriter: ...

class _OneVsRestSharedReadWrite:
    @staticmethod
    def saveImpl(instance: OneVsRest | OneVsRestModel, sc: SparkContext, path: str, extraMetadata: Dict[str, Any] | None = None) -> None: ...
    @staticmethod
    def loadClassifier(path: str, sc: SparkContext) -> OneVsRest | OneVsRestModel: ...
    @staticmethod
    def validateParams(instance: OneVsRest | OneVsRestModel) -> None: ...

class OneVsRestReader(MLReader[OneVsRest]):
    cls: Incomplete
    def __init__(self, cls: Type[OneVsRest]) -> None: ...
    def load(self, path: str) -> OneVsRest: ...

class OneVsRestWriter(MLWriter):
    instance: Incomplete
    def __init__(self, instance: OneVsRest) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class OneVsRestModel(Model, _OneVsRestParams, MLReadable['OneVsRestModel'], MLWritable):
    """
    Model fitted by OneVsRest.
    This stores the models resulting from training k binary classifiers: one for each class.
    Each example is scored against all k models, and the model with the highest score
    is picked to label the example.

    .. versionadded:: 2.0.0
    """
    def setFeaturesCol(self, value: str) -> OneVsRestModel:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> OneVsRestModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setRawPredictionCol(self, value: str) -> OneVsRestModel:
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """
    models: Incomplete
    def __init__(self, models: List[ClassificationModel]) -> None: ...
    def copy(self, extra: ParamMap | None = None) -> OneVsRestModel:
        """
        Creates a copy of this instance with a randomly generated uid
        and some extra params. This creates a deep copy of the embedded paramMap,
        and copies the embedded and extra parameters over.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        extra : dict, optional
            Extra parameters to copy to the new instance

        Returns
        -------
        :py:class:`OneVsRestModel`
            Copy of this instance
        """
    @classmethod
    def read(cls) -> OneVsRestModelReader: ...
    def write(self) -> MLWriter: ...

class OneVsRestModelReader(MLReader[OneVsRestModel]):
    cls: Incomplete
    def __init__(self, cls: Type[OneVsRestModel]) -> None: ...
    def load(self, path: str) -> OneVsRestModel: ...

class OneVsRestModelWriter(MLWriter):
    instance: Incomplete
    def __init__(self, instance: OneVsRestModel) -> None: ...
    def saveImpl(self, path: str) -> None: ...

class FMClassifier(_JavaProbabilisticClassifier['FMClassificationModel'], _FactorizationMachinesParams, JavaMLWritable, JavaMLReadable['FMClassifier']):
    '''
    Factorization Machines learning algorithm for classification.

    Solver supports:

    * gd (normal mini-batch gradient descent)
    * adamW (default)

    .. versionadded:: 3.0.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.classification import FMClassifier
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> fm = FMClassifier(factorSize=2)
    >>> fm.setSeed(11)
    FMClassifier...
    >>> model = fm.fit(df)
    >>> model.getMaxIter()
    100
    >>> test0 = spark.createDataFrame([
    ...     (Vectors.dense(-1.0),),
    ...     (Vectors.dense(0.5),),
    ...     (Vectors.dense(1.0),),
    ...     (Vectors.dense(2.0),)], ["features"])
    >>> model.predictRaw(test0.head().features)
    DenseVector([22.13..., -22.13...])
    >>> model.predictProbability(test0.head().features)
    DenseVector([1.0, 0.0])
    >>> model.transform(test0).select("features", "probability").show(10, False)
    +--------+------------------------------------------+
    |features|probability                               |
    +--------+------------------------------------------+
    |[-1.0]  |[0.9999999997574736,2.425264676902229E-10]|
    |[0.5]   |[0.47627851732981163,0.5237214826701884]  |
    |[1.0]   |[5.491554426243495E-4,0.9994508445573757] |
    |[2.0]   |[2.005766663870645E-10,0.9999999997994233]|
    +--------+------------------------------------------+
    ...
    >>> model.intercept
    -7.316665276826291
    >>> model.linear
    DenseVector([14.8232])
    >>> model.factors
    DenseMatrix(1, 2, [0.0163, -0.0051], 1)
    >>> model_path = temp_path + "/fm_model"
    >>> model.save(model_path)
    >>> model2 = FMClassificationModel.load(model_path)
    >>> model2.intercept
    -7.316665276826291
    >>> model2.linear
    DenseVector([14.8232])
    >>> model2.factors
    DenseMatrix(1, 2, [0.0163, -0.0051], 1)
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', factorSize: int = 8, fitIntercept: bool = True, fitLinear: bool = True, regParam: float = 0.0, miniBatchFraction: float = 1.0, initStd: float = 0.01, maxIter: int = 100, stepSize: float = 1.0, tol: float = 1e-06, solver: str = 'adamW', thresholds: List[float] | None = None, seed: int | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  probabilityCol="probability", rawPredictionCol="rawPrediction",                  factorSize=8, fitIntercept=True, fitLinear=True, regParam=0.0,                  miniBatchFraction=1.0, initStd=0.01, maxIter=100, stepSize=1.0,                  tol=1e-6, solver="adamW", thresholds=None, seed=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', factorSize: int = 8, fitIntercept: bool = True, fitLinear: bool = True, regParam: float = 0.0, miniBatchFraction: float = 1.0, initStd: float = 0.01, maxIter: int = 100, stepSize: float = 1.0, tol: float = 1e-06, solver: str = 'adamW', thresholds: List[float] | None = None, seed: int | None = None) -> FMClassifier:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   probabilityCol="probability", rawPredictionCol="rawPrediction",                   factorSize=8, fitIntercept=True, fitLinear=True, regParam=0.0,                   miniBatchFraction=1.0, initStd=0.01, maxIter=100, stepSize=1.0,                   tol=1e-6, solver="adamW", thresholds=None, seed=None)
        Sets Params for FMClassifier.
        '''
    def setFactorSize(self, value: int) -> FMClassifier:
        """
        Sets the value of :py:attr:`factorSize`.
        """
    def setFitLinear(self, value: bool) -> FMClassifier:
        """
        Sets the value of :py:attr:`fitLinear`.
        """
    def setMiniBatchFraction(self, value: float) -> FMClassifier:
        """
        Sets the value of :py:attr:`miniBatchFraction`.
        """
    def setInitStd(self, value: float) -> FMClassifier:
        """
        Sets the value of :py:attr:`initStd`.
        """
    def setMaxIter(self, value: int) -> FMClassifier:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setStepSize(self, value: float) -> FMClassifier:
        """
        Sets the value of :py:attr:`stepSize`.
        """
    def setTol(self, value: float) -> FMClassifier:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setSolver(self, value: str) -> FMClassifier:
        """
        Sets the value of :py:attr:`solver`.
        """
    def setSeed(self, value: int) -> FMClassifier:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setFitIntercept(self, value: bool) -> FMClassifier:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setRegParam(self, value: float) -> FMClassifier:
        """
        Sets the value of :py:attr:`regParam`.
        """

class FMClassificationModel(_JavaProbabilisticClassificationModel[Vector], _FactorizationMachinesParams, JavaMLWritable, JavaMLReadable['FMClassificationModel'], HasTrainingSummary):
    """
    Model fitted by :class:`FMClassifier`.

    .. versionadded:: 3.0.0
    """
    @property
    def intercept(self) -> float:
        """
        Model intercept.
        """
    @property
    def linear(self) -> Vector:
        """
        Model linear term.
        """
    @property
    def factors(self) -> Matrix:
        """
        Model factor term.
        """
    def summary(self) -> FMClassificationTrainingSummary:
        """
        Gets summary (accuracy/precision/recall, objective history, total iterations) of model
        trained on the training set. An exception is thrown if `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> FMClassificationSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 3.1.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on.
        """

class FMClassificationSummary(_BinaryClassificationSummary):
    """
    Abstraction for FMClassifier Results for a given model.

    .. versionadded:: 3.1.0
    """
class FMClassificationTrainingSummary(FMClassificationSummary, _TrainingSummary):
    """
    Abstraction for FMClassifier Training results.

    .. versionadded:: 3.1.0
    """
