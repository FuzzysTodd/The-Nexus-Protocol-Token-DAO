from _typeshed import Incomplete
from abc import ABCMeta
from pyspark.ml import PredictionModel, Predictor
from pyspark.ml.base import Transformer, _PredictorParams
from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.param.shared import HasAggregationDepth, HasElasticNetParam, HasFeaturesCol, HasFitIntercept, HasLabelCol, HasLoss, HasMaxBlockSizeInMB, HasMaxIter, HasPredictionCol, HasRegParam, HasSeed, HasSolver, HasStandardization, HasStepSize, HasTol, HasVarianceCol, HasWeightCol, Param
from pyspark.ml.tree import _DecisionTreeModel, _DecisionTreeParams, _GBTParams, _RandomForestParams, _TreeEnsembleModel, _TreeRegressorParams
from pyspark.ml.util import GeneralJavaMLWritable, HasTrainingSummary, JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaPredictionModel, JavaPredictor, JavaTransformer, JavaWrapper
from pyspark.sql import DataFrame
from typing import Any, Generic, List, TypeVar

__all__ = ['AFTSurvivalRegression', 'AFTSurvivalRegressionModel', 'DecisionTreeRegressor', 'DecisionTreeRegressionModel', 'GBTRegressor', 'GBTRegressionModel', 'GeneralizedLinearRegression', 'GeneralizedLinearRegressionModel', 'GeneralizedLinearRegressionSummary', 'GeneralizedLinearRegressionTrainingSummary', 'IsotonicRegression', 'IsotonicRegressionModel', 'LinearRegression', 'LinearRegressionModel', 'LinearRegressionSummary', 'LinearRegressionTrainingSummary', 'RandomForestRegressor', 'RandomForestRegressionModel', 'FMRegressor', 'FMRegressionModel']

T = TypeVar('T')
M = TypeVar('M', bound=Transformer)
JM = TypeVar('JM', bound=JavaTransformer)

class Regressor(Predictor[M], _PredictorParams, Generic[M], metaclass=ABCMeta):
    """
    Regressor for regression tasks.

    .. versionadded:: 3.0.0
    """
class RegressionModel(PredictionModel[T], _PredictorParams, metaclass=ABCMeta):
    """
    Model produced by a ``Regressor``.

    .. versionadded:: 3.0.0
    """
class _JavaRegressor(Regressor, JavaPredictor[JM], Generic[JM], metaclass=ABCMeta):
    """
    Java Regressor for regression tasks.

    .. versionadded:: 3.0.0
    """
class _JavaRegressionModel(RegressionModel, JavaPredictionModel[T], metaclass=ABCMeta):
    """
    Java Model produced by a ``_JavaRegressor``.
    To be mixed in with :class:`pyspark.ml.JavaModel`

    .. versionadded:: 3.0.0
    """

class _LinearRegressionParams(_PredictorParams, HasRegParam, HasElasticNetParam, HasMaxIter, HasTol, HasFitIntercept, HasStandardization, HasWeightCol, HasSolver, HasAggregationDepth, HasLoss, HasMaxBlockSizeInMB):
    """
    Params for :py:class:`LinearRegression` and :py:class:`LinearRegressionModel`.

    .. versionadded:: 3.0.0
    """
    solver: Param[str]
    loss: Param[str]
    epsilon: Param[float]
    def __init__(self, *args: Any) -> None: ...
    def getEpsilon(self) -> float:
        """
        Gets the value of epsilon or its default value.
        """

class LinearRegression(_JavaRegressor['LinearRegressionModel'], _LinearRegressionParams, JavaMLWritable, JavaMLReadable['LinearRegression']):
    '''
    Linear regression.

    The learning objective is to minimize the specified loss function, with regularization.
    This supports two kinds of loss:

    * squaredError (a.k.a squared loss)
    * huber (a hybrid of squared error for relatively small errors and absolute error for     relatively large ones, and we estimate the scale parameter from training data)

    This supports multiple types of regularization:

    * none (a.k.a. ordinary least squares)
    * L2 (ridge regression)
    * L1 (Lasso)
    * L2 + L1 (elastic net)

    .. versionadded:: 1.4.0

    Notes
    -----
    Fitting with huber loss only supports none and L2 regularization.

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, 2.0, Vectors.dense(1.0)),
    ...     (0.0, 2.0, Vectors.sparse(1, [], []))], ["label", "weight", "features"])
    >>> lr = LinearRegression(regParam=0.0, solver="normal", weightCol="weight")
    >>> lr.setMaxIter(5)
    LinearRegression...
    >>> lr.getMaxIter()
    5
    >>> lr.setRegParam(0.1)
    LinearRegression...
    >>> lr.getRegParam()
    0.1
    >>> lr.setRegParam(0.0)
    LinearRegression...
    >>> model = lr.fit(df)
    >>> model.setFeaturesCol("features")
    LinearRegressionModel...
    >>> model.setPredictionCol("newPrediction")
    LinearRegressionModel...
    >>> model.getMaxIter()
    5
    >>> model.getMaxBlockSizeInMB()
    0.0
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> abs(model.predict(test0.head().features) - (-1.0)) < 0.001
    True
    >>> abs(model.transform(test0).head().newPrediction - (-1.0)) < 0.001
    True
    >>> abs(model.coefficients[0] - 1.0) < 0.001
    True
    >>> abs(model.intercept - 0.0) < 0.001
    True
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> abs(model.transform(test1).head().newPrediction - 1.0) < 0.001
    True
    >>> lr.setParams(featuresCol="vector")
    LinearRegression...
    >>> lr_path = temp_path + "/lr"
    >>> lr.save(lr_path)
    >>> lr2 = LinearRegression.load(lr_path)
    >>> lr2.getMaxIter()
    5
    >>> model_path = temp_path + "/lr_model"
    >>> model.save(model_path)
    >>> model2 = LinearRegressionModel.load(model_path)
    >>> model.coefficients[0] == model2.coefficients[0]
    True
    >>> model.intercept == model2.intercept
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> model.numFeatures
    1
    >>> model.write().format("pmml").save(model_path + "_2")
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxIter: int = 100, regParam: float = 0.0, elasticNetParam: float = 0.0, tol: float = 1e-06, fitIntercept: bool = True, standardization: bool = True, solver: str = 'auto', weightCol: str | None = None, aggregationDepth: int = 2, loss: str = 'squaredError', epsilon: float = 1.35, maxBlockSizeInMB: float = 0.0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxIter=100, regParam=0.0, elasticNetParam=0.0, tol=1e-6, fitIntercept=True,                  standardization=True, solver="auto", weightCol=None, aggregationDepth=2,                  loss="squaredError", epsilon=1.35, maxBlockSizeInMB=0.0)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxIter: int = 100, regParam: float = 0.0, elasticNetParam: float = 0.0, tol: float = 1e-06, fitIntercept: bool = True, standardization: bool = True, solver: str = 'auto', weightCol: str | None = None, aggregationDepth: int = 2, loss: str = 'squaredError', epsilon: float = 1.35, maxBlockSizeInMB: float = 0.0) -> LinearRegression:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxIter=100, regParam=0.0, elasticNetParam=0.0, tol=1e-6, fitIntercept=True,                   standardization=True, solver="auto", weightCol=None, aggregationDepth=2,                   loss="squaredError", epsilon=1.35, maxBlockSizeInMB=0.0)
        Sets params for linear regression.
        '''
    def setEpsilon(self, value: float) -> LinearRegression:
        """
        Sets the value of :py:attr:`epsilon`.
        """
    def setMaxIter(self, value: int) -> LinearRegression:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setRegParam(self, value: float) -> LinearRegression:
        """
        Sets the value of :py:attr:`regParam`.
        """
    def setTol(self, value: float) -> LinearRegression:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setElasticNetParam(self, value: float) -> LinearRegression:
        """
        Sets the value of :py:attr:`elasticNetParam`.
        """
    def setFitIntercept(self, value: bool) -> LinearRegression:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setStandardization(self, value: bool) -> LinearRegression:
        """
        Sets the value of :py:attr:`standardization`.
        """
    def setWeightCol(self, value: str) -> LinearRegression:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setSolver(self, value: str) -> LinearRegression:
        """
        Sets the value of :py:attr:`solver`.
        """
    def setAggregationDepth(self, value: int) -> LinearRegression:
        """
        Sets the value of :py:attr:`aggregationDepth`.
        """
    def setLoss(self, value: str) -> LinearRegression:
        """
        Sets the value of :py:attr:`loss`.
        """
    def setMaxBlockSizeInMB(self, value: float) -> LinearRegression:
        """
        Sets the value of :py:attr:`maxBlockSizeInMB`.
        """

class LinearRegressionModel(_JavaRegressionModel, _LinearRegressionParams, GeneralJavaMLWritable, JavaMLReadable['LinearRegressionModel'], HasTrainingSummary['LinearRegressionSummary']):
    """
    Model fitted by :class:`LinearRegression`.

    .. versionadded:: 1.4.0
    """
    @property
    def coefficients(self) -> Vector:
        """
        Model coefficients.
        """
    @property
    def intercept(self) -> float:
        """
        Model intercept.
        """
    @property
    def scale(self) -> float:
        '''
        The value by which :math:`\\|y - X\'w\\|` is scaled down when loss is "huber", otherwise 1.0.
        '''
    @property
    def summary(self) -> LinearRegressionTrainingSummary:
        """
        Gets summary (residuals, MSE, r-squared ) of model on
        training set. An exception is thrown if
        `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> LinearRegressionSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on, where dataset is an
            instance of :py:class:`pyspark.sql.DataFrame`
        """

class LinearRegressionSummary(JavaWrapper):
    """
    Linear regression results evaluated on a dataset.

    .. versionadded:: 2.0.0
    """
    @property
    def predictions(self) -> DataFrame:
        """
        Dataframe outputted by the model's `transform` method.
        """
    @property
    def predictionCol(self) -> str:
        '''
        Field in "predictions" which gives the predicted value of
        the label at each instance.
        '''
    @property
    def labelCol(self) -> str:
        '''
        Field in "predictions" which gives the true label of each
        instance.
        '''
    @property
    def featuresCol(self) -> str:
        '''
        Field in "predictions" which gives the features of each instance
        as a vector.
        '''
    @property
    def explainedVariance(self) -> float:
        """
        Returns the explained variance regression score.
        explainedVariance = :math:`1 - \\frac{variance(y - \\hat{y})}{variance(y)}`

        Notes
        -----
        This ignores instance weights (setting all to 1.0) from
        `LinearRegression.weightCol`. This will change in later Spark
        versions.

        For additional information see
        `Explained variation on Wikipedia \\\n        <http://en.wikipedia.org/wiki/Explained_variation>`_
        """
    @property
    def meanAbsoluteError(self) -> float:
        """
        Returns the mean absolute error, which is a risk function
        corresponding to the expected value of the absolute error
        loss or l1-norm loss.

        Notes
        -----
        This ignores instance weights (setting all to 1.0) from
        `LinearRegression.weightCol`. This will change in later Spark
        versions.
        """
    @property
    def meanSquaredError(self) -> float:
        """
        Returns the mean squared error, which is a risk function
        corresponding to the expected value of the squared error
        loss or quadratic loss.

        Notes
        -----
        This ignores instance weights (setting all to 1.0) from
        `LinearRegression.weightCol`. This will change in later Spark
        versions.
        """
    @property
    def rootMeanSquaredError(self) -> float:
        """
        Returns the root mean squared error, which is defined as the
        square root of the mean squared error.

        Notes
        -----
        This ignores instance weights (setting all to 1.0) from
        `LinearRegression.weightCol`. This will change in later Spark
        versions.
        """
    @property
    def r2(self) -> float:
        """
        Returns R^2, the coefficient of determination.

        Notes
        -----
        This ignores instance weights (setting all to 1.0) from
        `LinearRegression.weightCol`. This will change in later Spark
        versions.

        See also `Wikipedia coefficient of determination         <http://en.wikipedia.org/wiki/Coefficient_of_determination>`_
        """
    @property
    def r2adj(self) -> float:
        """
        Returns Adjusted R^2, the adjusted coefficient of determination.

        Notes
        -----
        This ignores instance weights (setting all to 1.0) from
        `LinearRegression.weightCol`. This will change in later Spark versions.

        `Wikipedia coefficient of determination, Adjusted R^2         <https://en.wikipedia.org/wiki/Coefficient_of_determination#Adjusted_R2>`_
        """
    @property
    def residuals(self) -> DataFrame:
        """
        Residuals (label - predicted value)
        """
    @property
    def numInstances(self) -> int:
        """
        Number of instances in DataFrame predictions
        """
    @property
    def degreesOfFreedom(self) -> int:
        """
        Degrees of freedom.
        """
    @property
    def devianceResiduals(self) -> List[float]:
        """
        The weighted residuals, the usual residuals rescaled by the
        square root of the instance weights.
        """
    @property
    def coefficientStandardErrors(self) -> List[float]:
        '''
        Standard error of estimated coefficients and intercept.
        This value is only available when using the "normal" solver.

        If :py:attr:`LinearRegression.fitIntercept` is set to True,
        then the last element returned corresponds to the intercept.

        .. versionadded:: 2.0.0

        See Also
        --------
        LinearRegression.solver
        '''
    @property
    def tValues(self) -> List[float]:
        '''
        T-statistic of estimated coefficients and intercept.
        This value is only available when using the "normal" solver.

        If :py:attr:`LinearRegression.fitIntercept` is set to True,
        then the last element returned corresponds to the intercept.

        .. versionadded:: 2.0.0

        See Also
        --------
        LinearRegression.solver
        '''
    @property
    def pValues(self) -> List[float]:
        '''
        Two-sided p-value of estimated coefficients and intercept.
        This value is only available when using the "normal" solver.

        If :py:attr:`LinearRegression.fitIntercept` is set to True,
        then the last element returned corresponds to the intercept.

        .. versionadded:: 2.0.0

        See Also
        --------
        LinearRegression.solver
        '''

class LinearRegressionTrainingSummary(LinearRegressionSummary):
    """
    Linear regression training results. Currently, the training summary ignores the
    training weights except for the objective trace.

    .. versionadded:: 2.0.0
    """
    @property
    def objectiveHistory(self) -> List[float]:
        '''
        Objective function (scaled loss + regularization) at each
        iteration.
        This value is only available when using the "l-bfgs" solver.

        .. versionadded:: 2.0.0

        See Also
        --------
        LinearRegression.solver
        '''
    @property
    def totalIterations(self) -> int:
        '''
        Number of training iterations until termination.
        This value is only available when using the "l-bfgs" solver.

        .. versionadded:: 2.0.0

        See Also
        --------
        LinearRegression.solver
        '''

class _IsotonicRegressionParams(HasFeaturesCol, HasLabelCol, HasPredictionCol, HasWeightCol):
    """
    Params for :py:class:`IsotonicRegression` and :py:class:`IsotonicRegressionModel`.

    .. versionadded:: 3.0.0
    """
    isotonic: Param[bool]
    featureIndex: Param[int]
    def __init__(self, *args: Any) -> None: ...
    def getIsotonic(self) -> bool:
        """
        Gets the value of isotonic or its default value.
        """
    def getFeatureIndex(self) -> int:
        """
        Gets the value of featureIndex or its default value.
        """

class IsotonicRegression(JavaEstimator, _IsotonicRegressionParams, HasWeightCol, JavaMLWritable, JavaMLReadable):
    '''
    Currently implemented using parallelized pool adjacent violators algorithm.
    Only univariate (single feature) algorithm supported.

    .. versionadded:: 1.6.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> ir = IsotonicRegression()
    >>> model = ir.fit(df)
    >>> model.setFeaturesCol("features")
    IsotonicRegressionModel...
    >>> model.numFeatures
    1
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.transform(test0).head().prediction
    0.0
    >>> model.predict(test0.head().features[model.getFeatureIndex()])
    0.0
    >>> model.boundaries
    DenseVector([0.0, 1.0])
    >>> ir_path = temp_path + "/ir"
    >>> ir.save(ir_path)
    >>> ir2 = IsotonicRegression.load(ir_path)
    >>> ir2.getIsotonic()
    True
    >>> model_path = temp_path + "/ir_model"
    >>> model.save(model_path)
    >>> model2 = IsotonicRegressionModel.load(model_path)
    >>> model.boundaries == model2.boundaries
    True
    >>> model.predictions == model2.predictions
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', weightCol: str | None = None, isotonic: bool = True, featureIndex: int = 0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  weightCol=None, isotonic=True, featureIndex=0):
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', weightCol: str | None = None, isotonic: bool = True, featureIndex: int = 0) -> IsotonicRegression:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  weightCol=None, isotonic=True, featureIndex=0):
        Set the params for IsotonicRegression.
        '''
    def setIsotonic(self, value: bool) -> IsotonicRegression:
        """
        Sets the value of :py:attr:`isotonic`.
        """
    def setFeatureIndex(self, value: int) -> IsotonicRegression:
        """
        Sets the value of :py:attr:`featureIndex`.
        """
    def setFeaturesCol(self, value: str) -> IsotonicRegression:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> IsotonicRegression:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setLabelCol(self, value: str) -> IsotonicRegression:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setWeightCol(self, value: str) -> IsotonicRegression:
        """
        Sets the value of :py:attr:`weightCol`.
        """

class IsotonicRegressionModel(JavaModel, _IsotonicRegressionParams, JavaMLWritable, JavaMLReadable['IsotonicRegressionModel']):
    """
    Model fitted by :class:`IsotonicRegression`.

    .. versionadded:: 1.6.0
    """
    def setFeaturesCol(self, value: str) -> IsotonicRegressionModel:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> IsotonicRegressionModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setFeatureIndex(self, value: int) -> IsotonicRegressionModel:
        """
        Sets the value of :py:attr:`featureIndex`.
        """
    @property
    def boundaries(self) -> Vector:
        """
        Boundaries in increasing order for which predictions are known.
        """
    @property
    def predictions(self) -> Vector:
        """
        Predictions associated with the boundaries at the same index, monotone because of isotonic
        regression.
        """
    @property
    def numFeatures(self) -> int:
        """
        Returns the number of features the model was trained on. If unknown, returns -1
        """
    def predict(self, value: float) -> float:
        """
        Predict label for the given features.
        """

class _DecisionTreeRegressorParams(_DecisionTreeParams, _TreeRegressorParams, HasVarianceCol):
    """
    Params for :py:class:`DecisionTreeRegressor` and :py:class:`DecisionTreeRegressionModel`.

    .. versionadded:: 3.0.0
    """
    def __init__(self, *args: Any) -> None: ...

class DecisionTreeRegressor(_JavaRegressor['DecisionTreeRegressionModel'], _DecisionTreeRegressorParams, JavaMLWritable, JavaMLReadable['DecisionTreeRegressor']):
    '''
    `Decision tree <http://en.wikipedia.org/wiki/Decision_tree_learning>`_
    learning algorithm for regression.
    It supports both continuous and categorical features.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> dt = DecisionTreeRegressor(maxDepth=2)
    >>> dt.setVarianceCol("variance")
    DecisionTreeRegressor...
    >>> model = dt.fit(df)
    >>> model.getVarianceCol()
    \'variance\'
    >>> model.setLeafCol("leafId")
    DecisionTreeRegressionModel...
    >>> model.depth
    1
    >>> model.numNodes
    3
    >>> model.featureImportances
    SparseVector(1, {0: 1.0})
    >>> model.numFeatures
    1
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.predict(test0.head().features)
    0.0
    >>> result = model.transform(test0).head()
    >>> result.prediction
    0.0
    >>> model.predictLeaf(test0.head().features)
    0.0
    >>> result.leafId
    0.0
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> model.transform(test1).head().prediction
    1.0
    >>> dtr_path = temp_path + "/dtr"
    >>> dt.save(dtr_path)
    >>> dt2 = DecisionTreeRegressor.load(dtr_path)
    >>> dt2.getMaxDepth()
    2
    >>> model_path = temp_path + "/dtr_model"
    >>> model.save(model_path)
    >>> model2 = DecisionTreeRegressionModel.load(model_path)
    >>> model.numNodes == model2.numNodes
    True
    >>> model.depth == model2.depth
    True
    >>> model.transform(test1).head().variance
    0.0
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> df3 = spark.createDataFrame([
    ...     (1.0, 0.2, Vectors.dense(1.0)),
    ...     (1.0, 0.8, Vectors.dense(1.0)),
    ...     (0.0, 1.0, Vectors.sparse(1, [], []))], ["label", "weight", "features"])
    >>> dt3 = DecisionTreeRegressor(maxDepth=2, weightCol="weight", varianceCol="variance")
    >>> model3 = dt3.fit(df3)
    >>> print(model3.toDebugString)
    DecisionTreeRegressionModel...depth=1, numNodes=3...
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'variance', seed: int | None = None, varianceCol: str | None = None, weightCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                  maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10,                  impurity="variance", seed=None, varianceCol=None, weightCol=None,                  leafCol="", minWeightFractionPerNode=0.0)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'variance', seed: int | None = None, varianceCol: str | None = None, weightCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0) -> DecisionTreeRegressor:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                   maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10,                   impurity="variance", seed=None, varianceCol=None, weightCol=None,                   leafCol="", minWeightFractionPerNode=0.0)
        Sets params for the DecisionTreeRegressor.
        '''
    def setMaxDepth(self, value: int) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`maxDepth`.
        """
    def setMaxBins(self, value: int) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`maxBins`.
        """
    def setMinInstancesPerNode(self, value: int) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
    def setMinWeightFractionPerNode(self, value: float) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`minWeightFractionPerNode`.
        """
    def setMinInfoGain(self, value: float) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
    def setMaxMemoryInMB(self, value: int) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
    def setCacheNodeIds(self, value: bool) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
    def setImpurity(self, value: str) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`impurity`.
        """
    def setCheckpointInterval(self, value: int) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setWeightCol(self, value: str) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setVarianceCol(self, value: str) -> DecisionTreeRegressor:
        """
        Sets the value of :py:attr:`varianceCol`.
        """

class DecisionTreeRegressionModel(_JavaRegressionModel, _DecisionTreeModel, _DecisionTreeRegressorParams, JavaMLWritable, JavaMLReadable['DecisionTreeRegressionModel']):
    """
    Model fitted by :class:`DecisionTreeRegressor`.

    .. versionadded:: 1.4.0
    """
    def setVarianceCol(self, value: str) -> DecisionTreeRegressionModel:
        """
        Sets the value of :py:attr:`varianceCol`.
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
        correlated predictor variables. Consider using a :py:class:`RandomForestRegressor`
        to determine feature importance instead.
        '''

class _RandomForestRegressorParams(_RandomForestParams, _TreeRegressorParams):
    """
    Params for :py:class:`RandomForestRegressor` and :py:class:`RandomForestRegressionModel`.

    .. versionadded:: 3.0.0
    """
    def __init__(self, *args: Any) -> None: ...

class RandomForestRegressor(_JavaRegressor['RandomForestRegressionModel'], _RandomForestRegressorParams, JavaMLWritable, JavaMLReadable['RandomForestRegressor']):
    '''
    `Random Forest <http://en.wikipedia.org/wiki/Random_forest>`_
    learning algorithm for regression.
    It supports both continuous and categorical features.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from numpy import allclose
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> rf = RandomForestRegressor(numTrees=2, maxDepth=2)
    >>> rf.getMinWeightFractionPerNode()
    0.0
    >>> rf.setSeed(42)
    RandomForestRegressor...
    >>> model = rf.fit(df)
    >>> model.getBootstrap()
    True
    >>> model.getSeed()
    42
    >>> model.setLeafCol("leafId")
    RandomForestRegressionModel...
    >>> model.featureImportances
    SparseVector(1, {0: 1.0})
    >>> allclose(model.treeWeights, [1.0, 1.0])
    True
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.predict(test0.head().features)
    0.0
    >>> model.predictLeaf(test0.head().features)
    DenseVector([0.0, 0.0])
    >>> result = model.transform(test0).head()
    >>> result.prediction
    0.0
    >>> result.leafId
    DenseVector([0.0, 0.0])
    >>> model.numFeatures
    1
    >>> model.trees
    [DecisionTreeRegressionModel...depth=..., DecisionTreeRegressionModel...]
    >>> model.getNumTrees
    2
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> model.transform(test1).head().prediction
    0.5
    >>> rfr_path = temp_path + "/rfr"
    >>> rf.save(rfr_path)
    >>> rf2 = RandomForestRegressor.load(rfr_path)
    >>> rf2.getNumTrees()
    2
    >>> model_path = temp_path + "/rfr_model"
    >>> model.save(model_path)
    >>> model2 = RandomForestRegressionModel.load(model_path)
    >>> model.featureImportances == model2.featureImportances
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'variance', subsamplingRate: float = 1.0, seed: int | None = None, numTrees: int = 20, featureSubsetStrategy: str = 'auto', leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None, bootstrap: bool | None = True) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                  maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10,                  impurity="variance", subsamplingRate=1.0, seed=None, numTrees=20,                  featureSubsetStrategy="auto", leafCol=", minWeightFractionPerNode=0.0",                  weightCol=None, bootstrap=True)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, checkpointInterval: int = 10, impurity: str = 'variance', subsamplingRate: float = 1.0, seed: int | None = None, numTrees: int = 20, featureSubsetStrategy: str = 'auto', leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None, bootstrap: bool | None = True) -> RandomForestRegressor:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                   maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10,                   impurity="variance", subsamplingRate=1.0, seed=None, numTrees=20,                   featureSubsetStrategy="auto", leafCol="", minWeightFractionPerNode=0.0,                   weightCol=None, bootstrap=True)
        Sets params for linear regression.
        '''
    def setMaxDepth(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`maxDepth`.
        """
    def setMaxBins(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`maxBins`.
        """
    def setMinInstancesPerNode(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
    def setMinInfoGain(self, value: float) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
    def setMaxMemoryInMB(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
    def setCacheNodeIds(self, value: bool) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
    def setImpurity(self, value: str) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`impurity`.
        """
    def setNumTrees(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`numTrees`.
        """
    def setBootstrap(self, value: bool) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`bootstrap`.
        """
    def setSubsamplingRate(self, value: float) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`subsamplingRate`.
        """
    def setFeatureSubsetStrategy(self, value: str) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`featureSubsetStrategy`.
        """
    def setCheckpointInterval(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setWeightCol(self, value: str) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setMinWeightFractionPerNode(self, value: float) -> RandomForestRegressor:
        """
        Sets the value of :py:attr:`minWeightFractionPerNode`.
        """

class RandomForestRegressionModel(_JavaRegressionModel[Vector], _TreeEnsembleModel, _RandomForestRegressorParams, JavaMLWritable, JavaMLReadable['RandomForestRegressionModel']):
    """
    Model fitted by :class:`RandomForestRegressor`.

    .. versionadded:: 1.4.0
    """
    @property
    def trees(self) -> List[DecisionTreeRegressionModel]:
        """Trees in this ensemble. Warning: These have null parent Estimators."""
    @property
    def featureImportances(self) -> Vector:
        '''
        Estimate of the importance of each feature.

        Each feature\'s importance is the average of its importance across all trees in the ensemble
        The importance vector is normalized to sum to 1. This method is suggested by Hastie et al.
        (Hastie, Tibshirani, Friedman. "The Elements of Statistical Learning, 2nd Edition." 2001.)
        and follows the implementation from scikit-learn.

        .. versionadded:: 2.0.0

        Examples
        --------
        DecisionTreeRegressionModel.featureImportances
        '''

class _GBTRegressorParams(_GBTParams, _TreeRegressorParams):
    """
    Params for :py:class:`GBTRegressor` and :py:class:`GBTRegressorModel`.

    .. versionadded:: 3.0.0
    """
    supportedLossTypes: List[str]
    lossType: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getLossType(self) -> str:
        """
        Gets the value of lossType or its default value.
        """

class GBTRegressor(_JavaRegressor['GBTRegressionModel'], _GBTRegressorParams, JavaMLWritable, JavaMLReadable['GBTRegressor']):
    '''
    `Gradient-Boosted Trees (GBTs) <http://en.wikipedia.org/wiki/Gradient_boosting>`_
    learning algorithm for regression.
    It supports both continuous and categorical features.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from numpy import allclose
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>> gbt = GBTRegressor(maxDepth=2, seed=42, leafCol="leafId")
    >>> gbt.setMaxIter(5)
    GBTRegressor...
    >>> gbt.setMinWeightFractionPerNode(0.049)
    GBTRegressor...
    >>> gbt.getMaxIter()
    5
    >>> print(gbt.getImpurity())
    variance
    >>> print(gbt.getFeatureSubsetStrategy())
    all
    >>> model = gbt.fit(df)
    >>> model.featureImportances
    SparseVector(1, {0: 1.0})
    >>> model.numFeatures
    1
    >>> allclose(model.treeWeights, [1.0, 0.1, 0.1, 0.1, 0.1])
    True
    >>> test0 = spark.createDataFrame([(Vectors.dense(-1.0),)], ["features"])
    >>> model.predict(test0.head().features)
    0.0
    >>> model.predictLeaf(test0.head().features)
    DenseVector([0.0, 0.0, 0.0, 0.0, 0.0])
    >>> result = model.transform(test0).head()
    >>> result.prediction
    0.0
    >>> result.leafId
    DenseVector([0.0, 0.0, 0.0, 0.0, 0.0])
    >>> test1 = spark.createDataFrame([(Vectors.sparse(1, [0], [1.0]),)], ["features"])
    >>> model.transform(test1).head().prediction
    1.0
    >>> gbtr_path = temp_path + "gbtr"
    >>> gbt.save(gbtr_path)
    >>> gbt2 = GBTRegressor.load(gbtr_path)
    >>> gbt2.getMaxDepth()
    2
    >>> model_path = temp_path + "gbtr_model"
    >>> model.save(model_path)
    >>> model2 = GBTRegressionModel.load(model_path)
    >>> model.featureImportances == model2.featureImportances
    True
    >>> model.treeWeights == model2.treeWeights
    True
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    >>> model.trees
    [DecisionTreeRegressionModel...depth=..., DecisionTreeRegressionModel...]
    >>> validation = spark.createDataFrame([(0.0, Vectors.dense(-1.0))],
    ...              ["label", "features"])
    >>> model.evaluateEachIteration(validation, "squared")
    [0.0, 0.0, 0.0, 0.0, 0.0]
    >>> gbt = gbt.setValidationIndicatorCol("validationIndicator")
    >>> gbt.getValidationIndicatorCol()
    \'validationIndicator\'
    >>> gbt.getValidationTol()
    0.01
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, subsamplingRate: float = 1.0, checkpointInterval: int = 10, lossType: str = 'squared', maxIter: int = 20, stepSize: float = 0.1, seed: int | None = None, impurity: str = 'variance', featureSubsetStrategy: str = 'all', validationTol: float = 0.1, validationIndicatorCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                  maxMemoryInMB=256, cacheNodeIds=False, subsamplingRate=1.0,                  checkpointInterval=10, lossType="squared", maxIter=20, stepSize=0.1, seed=None,                  impurity="variance", featureSubsetStrategy="all", validationTol=0.01,                  validationIndicatorCol=None, leafCol="", minWeightFractionPerNode=0.0,
                 weightCol=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', maxDepth: int = 5, maxBins: int = 32, minInstancesPerNode: int = 1, minInfoGain: float = 0.0, maxMemoryInMB: int = 256, cacheNodeIds: bool = False, subsamplingRate: float = 1.0, checkpointInterval: int = 10, lossType: str = 'squared', maxIter: int = 20, stepSize: float = 0.1, seed: int | None = None, impurity: str = 'variance', featureSubsetStrategy: str = 'all', validationTol: float = 0.1, validationIndicatorCol: str | None = None, leafCol: str = '', minWeightFractionPerNode: float = 0.0, weightCol: str | None = None) -> GBTRegressor:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,                   maxMemoryInMB=256, cacheNodeIds=False, subsamplingRate=1.0,                   checkpointInterval=10, lossType="squared", maxIter=20, stepSize=0.1, seed=None,                   impurity="variance", featureSubsetStrategy="all", validationTol=0.01,                   validationIndicatorCol=None, leafCol="", minWeightFractionPerNode=0.0,                   weightCol=None)
        Sets params for Gradient Boosted Tree Regression.
        '''
    def setMaxDepth(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`maxDepth`.
        """
    def setMaxBins(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`maxBins`.
        """
    def setMinInstancesPerNode(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`minInstancesPerNode`.
        """
    def setMinInfoGain(self, value: float) -> GBTRegressor:
        """
        Sets the value of :py:attr:`minInfoGain`.
        """
    def setMaxMemoryInMB(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`maxMemoryInMB`.
        """
    def setCacheNodeIds(self, value: bool) -> GBTRegressor:
        """
        Sets the value of :py:attr:`cacheNodeIds`.
        """
    def setImpurity(self, value: str) -> GBTRegressor:
        """
        Sets the value of :py:attr:`impurity`.
        """
    def setLossType(self, value: str) -> GBTRegressor:
        """
        Sets the value of :py:attr:`lossType`.
        """
    def setSubsamplingRate(self, value: float) -> GBTRegressor:
        """
        Sets the value of :py:attr:`subsamplingRate`.
        """
    def setFeatureSubsetStrategy(self, value: str) -> GBTRegressor:
        """
        Sets the value of :py:attr:`featureSubsetStrategy`.
        """
    def setValidationIndicatorCol(self, value: str) -> GBTRegressor:
        """
        Sets the value of :py:attr:`validationIndicatorCol`.
        """
    def setMaxIter(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setCheckpointInterval(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> GBTRegressor:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setStepSize(self, value: float) -> GBTRegressor:
        """
        Sets the value of :py:attr:`stepSize`.
        """
    def setWeightCol(self, value: str) -> GBTRegressor:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setMinWeightFractionPerNode(self, value: float) -> GBTRegressor:
        """
        Sets the value of :py:attr:`minWeightFractionPerNode`.
        """

class GBTRegressionModel(_JavaRegressionModel[Vector], _TreeEnsembleModel, _GBTRegressorParams, JavaMLWritable, JavaMLReadable['GBTRegressionModel']):
    """
    Model fitted by :class:`GBTRegressor`.

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

        Examples
        --------
        DecisionTreeRegressionModel.featureImportances
        '''
    @property
    def trees(self) -> List[DecisionTreeRegressionModel]:
        """Trees in this ensemble. Warning: These have null parent Estimators."""
    def evaluateEachIteration(self, dataset: DataFrame, loss: str) -> List[float]:
        """
        Method to compute error or loss for every iteration of gradient boosting.

        .. versionadded:: 2.4.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on, where dataset is an
            instance of :py:class:`pyspark.sql.DataFrame`
        loss : str
            The loss function used to compute error.
            Supported options: squared, absolute
        """

class _AFTSurvivalRegressionParams(_PredictorParams, HasMaxIter, HasTol, HasFitIntercept, HasAggregationDepth, HasMaxBlockSizeInMB):
    """
    Params for :py:class:`AFTSurvivalRegression` and :py:class:`AFTSurvivalRegressionModel`.

    .. versionadded:: 3.0.0
    """
    censorCol: Param[str]
    quantileProbabilities: Param[List[float]]
    quantilesCol: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getCensorCol(self) -> str:
        """
        Gets the value of censorCol or its default value.
        """
    def getQuantileProbabilities(self) -> List[float]:
        """
        Gets the value of quantileProbabilities or its default value.
        """
    def getQuantilesCol(self) -> str:
        """
        Gets the value of quantilesCol or its default value.
        """

class AFTSurvivalRegression(_JavaRegressor['AFTSurvivalRegressionModel'], _AFTSurvivalRegressionParams, JavaMLWritable, JavaMLReadable['AFTSurvivalRegression']):
    '''
    Accelerated Failure Time (AFT) Model Survival Regression

    Fit a parametric AFT survival regression model based on the Weibull distribution
    of the survival time.

    Notes
    -----
    For more information see Wikipedia page on
    `AFT Model <https://en.wikipedia.org/wiki/Accelerated_failure_time_model>`_


    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(1.0), 1.0),
    ...     (1e-40, Vectors.sparse(1, [], []), 0.0)], ["label", "features", "censor"])
    >>> aftsr = AFTSurvivalRegression()
    >>> aftsr.setMaxIter(10)
    AFTSurvivalRegression...
    >>> aftsr.getMaxIter()
    10
    >>> aftsr.clear(aftsr.maxIter)
    >>> model = aftsr.fit(df)
    >>> model.getMaxBlockSizeInMB()
    0.0
    >>> model.setFeaturesCol("features")
    AFTSurvivalRegressionModel...
    >>> model.predict(Vectors.dense(6.3))
    1.0
    >>> model.predictQuantiles(Vectors.dense(6.3))
    DenseVector([0.0101, 0.0513, 0.1054, 0.2877, 0.6931, 1.3863, 2.3026, 2.9957, 4.6052])
    >>> model.transform(df).show()
    +-------+---------+------+----------+
    |  label| features|censor|prediction|
    +-------+---------+------+----------+
    |    1.0|    [1.0]|   1.0|       1.0|
    |1.0E-40|(1,[],[])|   0.0|       1.0|
    +-------+---------+------+----------+
    ...
    >>> aftsr_path = temp_path + "/aftsr"
    >>> aftsr.save(aftsr_path)
    >>> aftsr2 = AFTSurvivalRegression.load(aftsr_path)
    >>> aftsr2.getMaxIter()
    100
    >>> model_path = temp_path + "/aftsr_model"
    >>> model.save(model_path)
    >>> model2 = AFTSurvivalRegressionModel.load(model_path)
    >>> model.coefficients == model2.coefficients
    True
    >>> model.intercept == model2.intercept
    True
    >>> model.scale == model2.scale
    True
    >>> model.transform(df).take(1) == model2.transform(df).take(1)
    True

    .. versionadded:: 1.6.0
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', fitIntercept: bool = True, maxIter: int = 100, tol: float = 1e-06, censorCol: str = 'censor', quantileProbabilities: List[float] = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99], quantilesCol: str | None = None, aggregationDepth: int = 2, maxBlockSizeInMB: float = 0.0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  fitIntercept=True, maxIter=100, tol=1E-6, censorCol="censor",                  quantileProbabilities=[0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99],                  quantilesCol=None, aggregationDepth=2, maxBlockSizeInMB=0.0)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', fitIntercept: bool = True, maxIter: int = 100, tol: float = 1e-06, censorCol: str = 'censor', quantileProbabilities: List[float] = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99], quantilesCol: str | None = None, aggregationDepth: int = 2, maxBlockSizeInMB: float = 0.0) -> AFTSurvivalRegression:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   fitIntercept=True, maxIter=100, tol=1E-6, censorCol="censor",                   quantileProbabilities=[0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99],                   quantilesCol=None, aggregationDepth=2, maxBlockSizeInMB=0.0):
        '''
    def setCensorCol(self, value: str) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`censorCol`.
        """
    def setQuantileProbabilities(self, value: List[float]) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`quantileProbabilities`.
        """
    def setQuantilesCol(self, value: str) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`quantilesCol`.
        """
    def setMaxIter(self, value: int) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setTol(self, value: float) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setFitIntercept(self, value: bool) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setAggregationDepth(self, value: int) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`aggregationDepth`.
        """
    def setMaxBlockSizeInMB(self, value: int) -> AFTSurvivalRegression:
        """
        Sets the value of :py:attr:`maxBlockSizeInMB`.
        """

class AFTSurvivalRegressionModel(_JavaRegressionModel[Vector], _AFTSurvivalRegressionParams, JavaMLWritable, JavaMLReadable['AFTSurvivalRegressionModel']):
    """
    Model fitted by :class:`AFTSurvivalRegression`.

    .. versionadded:: 1.6.0
    """
    def setQuantileProbabilities(self, value: List[float]) -> AFTSurvivalRegressionModel:
        """
        Sets the value of :py:attr:`quantileProbabilities`.
        """
    def setQuantilesCol(self, value: str) -> AFTSurvivalRegressionModel:
        """
        Sets the value of :py:attr:`quantilesCol`.
        """
    @property
    def coefficients(self) -> Vector:
        """
        Model coefficients.
        """
    @property
    def intercept(self) -> float:
        """
        Model intercept.
        """
    @property
    def scale(self) -> float:
        """
        Model scale parameter.
        """
    def predictQuantiles(self, features: Vector) -> Vector:
        """
        Predicted Quantiles
        """

class _GeneralizedLinearRegressionParams(_PredictorParams, HasFitIntercept, HasMaxIter, HasTol, HasRegParam, HasWeightCol, HasSolver, HasAggregationDepth):
    """
    Params for :py:class:`GeneralizedLinearRegression` and
    :py:class:`GeneralizedLinearRegressionModel`.

    .. versionadded:: 3.0.0
    """
    family: Param[str]
    link: Param[str]
    linkPredictionCol: Param[str]
    variancePower: Param[float]
    linkPower: Param[float]
    solver: Param[str]
    offsetCol: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getFamily(self) -> str:
        """
        Gets the value of family or its default value.
        """
    def getLinkPredictionCol(self) -> str:
        """
        Gets the value of linkPredictionCol or its default value.
        """
    def getLink(self) -> str:
        """
        Gets the value of link or its default value.
        """
    def getVariancePower(self) -> float:
        """
        Gets the value of variancePower or its default value.
        """
    def getLinkPower(self) -> float:
        """
        Gets the value of linkPower or its default value.
        """
    def getOffsetCol(self) -> str:
        """
        Gets the value of offsetCol or its default value.
        """

class GeneralizedLinearRegression(_JavaRegressor['GeneralizedLinearRegressionModel'], _GeneralizedLinearRegressionParams, JavaMLWritable, JavaMLReadable['GeneralizedLinearRegression']):
    '''
    Generalized Linear Regression.

    Fit a Generalized Linear Model specified by giving a symbolic description of the linear
    predictor (link function) and a description of the error distribution (family). It supports
    "gaussian", "binomial", "poisson", "gamma" and "tweedie" as family. Valid link functions for
    each family is listed below. The first link function of each family is the default one.

    * "gaussian" -> "identity", "log", "inverse"

    * "binomial" -> "logit", "probit", "cloglog"

    * "poisson"  -> "log", "identity", "sqrt"

    * "gamma"    -> "inverse", "identity", "log"

    * "tweedie"  -> power link function specified through "linkPower".                     The default link power in the tweedie family is 1 - variancePower.

    .. versionadded:: 2.0.0

    Notes
    -----
    For more information see Wikipedia page on
    `GLM <https://en.wikipedia.org/wiki/Generalized_linear_model>`_

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> df = spark.createDataFrame([
    ...     (1.0, Vectors.dense(0.0, 0.0)),
    ...     (1.0, Vectors.dense(1.0, 2.0)),
    ...     (2.0, Vectors.dense(0.0, 0.0)),
    ...     (2.0, Vectors.dense(1.0, 1.0)),], ["label", "features"])
    >>> glr = GeneralizedLinearRegression(family="gaussian", link="identity", linkPredictionCol="p")
    >>> glr.setRegParam(0.1)
    GeneralizedLinearRegression...
    >>> glr.getRegParam()
    0.1
    >>> glr.clear(glr.regParam)
    >>> glr.setMaxIter(10)
    GeneralizedLinearRegression...
    >>> glr.getMaxIter()
    10
    >>> glr.clear(glr.maxIter)
    >>> model = glr.fit(df)
    >>> model.setFeaturesCol("features")
    GeneralizedLinearRegressionModel...
    >>> model.getMaxIter()
    25
    >>> model.getAggregationDepth()
    2
    >>> transformed = model.transform(df)
    >>> abs(transformed.head().prediction - 1.5) < 0.001
    True
    >>> abs(transformed.head().p - 1.5) < 0.001
    True
    >>> model.coefficients
    DenseVector([1.5..., -1.0...])
    >>> model.numFeatures
    2
    >>> abs(model.intercept - 1.5) < 0.001
    True
    >>> glr_path = temp_path + "/glr"
    >>> glr.save(glr_path)
    >>> glr2 = GeneralizedLinearRegression.load(glr_path)
    >>> glr.getFamily() == glr2.getFamily()
    True
    >>> model_path = temp_path + "/glr_model"
    >>> model.save(model_path)
    >>> model2 = GeneralizedLinearRegressionModel.load(model_path)
    >>> model.intercept == model2.intercept
    True
    >>> model.coefficients[0] == model2.coefficients[0]
    True
    >>> model.transform(df).take(1) == model2.transform(df).take(1)
    True
    '''
    def __init__(self, *, labelCol: str = 'label', featuresCol: str = 'features', predictionCol: str = 'prediction', family: str = 'gaussian', link: str | None = None, fitIntercept: bool = True, maxIter: int = 25, tol: float = 1e-06, regParam: float = 0.0, weightCol: str | None = None, solver: str = 'irls', linkPredictionCol: str | None = None, variancePower: float = 0.0, linkPower: float | None = None, offsetCol: str | None = None, aggregationDepth: int = 2) -> None:
        '''
        __init__(self, \\*, labelCol="label", featuresCol="features", predictionCol="prediction",                  family="gaussian", link=None, fitIntercept=True, maxIter=25, tol=1e-6,                  regParam=0.0, weightCol=None, solver="irls", linkPredictionCol=None,                  variancePower=0.0, linkPower=None, offsetCol=None, aggregationDepth=2)
        '''
    def setParams(self, *, labelCol: str = 'label', featuresCol: str = 'features', predictionCol: str = 'prediction', family: str = 'gaussian', link: str | None = None, fitIntercept: bool = True, maxIter: int = 25, tol: float = 1e-06, regParam: float = 0.0, weightCol: str | None = None, solver: str = 'irls', linkPredictionCol: str | None = None, variancePower: float = 0.0, linkPower: float | None = None, offsetCol: str | None = None, aggregationDepth: int = 2) -> GeneralizedLinearRegression:
        '''
        setParams(self, \\*, labelCol="label", featuresCol="features", predictionCol="prediction",                   family="gaussian", link=None, fitIntercept=True, maxIter=25, tol=1e-6,                   regParam=0.0, weightCol=None, solver="irls", linkPredictionCol=None,                   variancePower=0.0, linkPower=None, offsetCol=None, aggregationDepth=2)
        Sets params for generalized linear regression.
        '''
    def setFamily(self, value: str) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`family`.
        """
    def setLinkPredictionCol(self, value: str) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`linkPredictionCol`.
        """
    def setLink(self, value: str) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`link`.
        """
    def setVariancePower(self, value: float) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`variancePower`.
        """
    def setLinkPower(self, value: float) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`linkPower`.
        """
    def setOffsetCol(self, value: str) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`offsetCol`.
        """
    def setMaxIter(self, value: int) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setRegParam(self, value: float) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`regParam`.
        """
    def setTol(self, value: float) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setFitIntercept(self, value: bool) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setWeightCol(self, value: str) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setSolver(self, value: str) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`solver`.
        """
    def setAggregationDepth(self, value: int) -> GeneralizedLinearRegression:
        """
        Sets the value of :py:attr:`aggregationDepth`.
        """

class GeneralizedLinearRegressionModel(_JavaRegressionModel[Vector], _GeneralizedLinearRegressionParams, JavaMLWritable, JavaMLReadable['GeneralizedLinearRegressionModel'], HasTrainingSummary['GeneralizedLinearRegressionTrainingSummary']):
    """
    Model fitted by :class:`GeneralizedLinearRegression`.

    .. versionadded:: 2.0.0
    """
    def setLinkPredictionCol(self, value: str) -> GeneralizedLinearRegressionModel:
        """
        Sets the value of :py:attr:`linkPredictionCol`.
        """
    @property
    def coefficients(self) -> Vector:
        """
        Model coefficients.
        """
    @property
    def intercept(self) -> float:
        """
        Model intercept.
        """
    @property
    def summary(self) -> GeneralizedLinearRegressionTrainingSummary:
        """
        Gets summary (residuals, deviance, p-values) of model on
        training set. An exception is thrown if
        `trainingSummary is None`.
        """
    def evaluate(self, dataset: DataFrame) -> GeneralizedLinearRegressionSummary:
        """
        Evaluates the model on a test dataset.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            Test dataset to evaluate model on, where dataset is an
            instance of :py:class:`pyspark.sql.DataFrame`
        """

class GeneralizedLinearRegressionSummary(JavaWrapper):
    """
    Generalized linear regression results evaluated on a dataset.

    .. versionadded:: 2.0.0
    """
    @property
    def predictions(self) -> DataFrame:
        """
        Predictions output by the model's `transform` method.
        """
    @property
    def predictionCol(self) -> str:
        """
        Field in :py:attr:`predictions` which gives the predicted value of each instance.
        This is set to a new column name if the original model's `predictionCol` is not set.
        """
    @property
    def numInstances(self) -> int:
        """
        Number of instances in DataFrame predictions.
        """
    @property
    def rank(self) -> int:
        """
        The numeric rank of the fitted linear model.
        """
    @property
    def degreesOfFreedom(self) -> int:
        """
        Degrees of freedom.
        """
    @property
    def residualDegreeOfFreedom(self) -> int:
        """
        The residual degrees of freedom.
        """
    @property
    def residualDegreeOfFreedomNull(self) -> int:
        """
        The residual degrees of freedom for the null model.
        """
    def residuals(self, residualsType: str = 'deviance') -> DataFrame:
        """
        Get the residuals of the fitted model by type.

        .. versionadded:: 2.0.0

        Parameters
        ----------
        residualsType : str, optional
            The type of residuals which should be returned.
            Supported options: deviance (default), pearson, working, and response.
        """
    @property
    def nullDeviance(self) -> float:
        """
        The deviance for the null model.
        """
    @property
    def deviance(self) -> float:
        """
        The deviance for the fitted model.
        """
    @property
    def dispersion(self) -> float:
        '''
        The dispersion of the fitted model.
        It is taken as 1.0 for the "binomial" and "poisson" families, and otherwise
        estimated by the residual Pearson\'s Chi-Squared statistic (which is defined as
        sum of the squares of the Pearson residuals) divided by the residual degrees of freedom.
        '''
    @property
    def aic(self) -> float:
        '''
        Akaike\'s "An Information Criterion"(AIC) for the fitted model.
        '''

class GeneralizedLinearRegressionTrainingSummary(GeneralizedLinearRegressionSummary):
    """
    Generalized linear regression training results.

    .. versionadded:: 2.0.0
    """
    @property
    def numIterations(self) -> int:
        """
        Number of training iterations.
        """
    @property
    def solver(self) -> str:
        """
        The numeric solver used for training.
        """
    @property
    def coefficientStandardErrors(self) -> List[float]:
        """
        Standard error of estimated coefficients and intercept.

        If :py:attr:`GeneralizedLinearRegression.fitIntercept` is set to True,
        then the last element returned corresponds to the intercept.
        """
    @property
    def tValues(self) -> List[float]:
        """
        T-statistic of estimated coefficients and intercept.

        If :py:attr:`GeneralizedLinearRegression.fitIntercept` is set to True,
        then the last element returned corresponds to the intercept.
        """
    @property
    def pValues(self) -> List[float]:
        """
        Two-sided p-value of estimated coefficients and intercept.

        If :py:attr:`GeneralizedLinearRegression.fitIntercept` is set to True,
        then the last element returned corresponds to the intercept.
        """

class _FactorizationMachinesParams(_PredictorParams, HasMaxIter, HasStepSize, HasTol, HasSolver, HasSeed, HasFitIntercept, HasRegParam, HasWeightCol):
    """
    Params for :py:class:`FMRegressor`, :py:class:`FMRegressionModel`, :py:class:`FMClassifier`
    and :py:class:`FMClassifierModel`.

    .. versionadded:: 3.0.0
    """
    factorSize: Param[int]
    fitLinear: Param[bool]
    miniBatchFraction: Param[float]
    initStd: Param[float]
    solver: Incomplete
    def __init__(self, *args: Any) -> None: ...
    def getFactorSize(self) -> int:
        """
        Gets the value of factorSize or its default value.
        """
    def getFitLinear(self) -> bool:
        """
        Gets the value of fitLinear or its default value.
        """
    def getMiniBatchFraction(self) -> float:
        """
        Gets the value of miniBatchFraction or its default value.
        """
    def getInitStd(self) -> float:
        """
        Gets the value of initStd or its default value.
        """

class FMRegressor(_JavaRegressor['FMRegressionModel'], _FactorizationMachinesParams, JavaMLWritable, JavaMLReadable['FMRegressor']):
    '''
    Factorization Machines learning algorithm for regression.

    solver Supports:

    * gd (normal mini-batch gradient descent)
    * adamW (default)

    .. versionadded:: 3.0.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> from pyspark.ml.regression import FMRegressor
    >>> df = spark.createDataFrame([
    ...     (2.0, Vectors.dense(2.0)),
    ...     (1.0, Vectors.dense(1.0)),
    ...     (0.0, Vectors.sparse(1, [], []))], ["label", "features"])
    >>>
    >>> fm = FMRegressor(factorSize=2)
    >>> fm.setSeed(16)
    FMRegressor...
    >>> model = fm.fit(df)
    >>> model.getMaxIter()
    100
    >>> test0 = spark.createDataFrame([
    ...     (Vectors.dense(-2.0),),
    ...     (Vectors.dense(0.5),),
    ...     (Vectors.dense(1.0),),
    ...     (Vectors.dense(4.0),)], ["features"])
    >>> model.transform(test0).show(10, False)
    +--------+-------------------+
    |features|prediction         |
    +--------+-------------------+
    |[-2.0]  |-1.9989237712341565|
    |[0.5]   |0.4956682219523814 |
    |[1.0]   |0.994586620589689  |
    |[4.0]   |3.9880970124135344 |
    +--------+-------------------+
    ...
    >>> model.intercept
    -0.0032501766849261557
    >>> model.linear
    DenseVector([0.9978])
    >>> model.factors
    DenseMatrix(1, 2, [0.0173, 0.0021], 1)
    >>> model_path = temp_path + "/fm_model"
    >>> model.save(model_path)
    >>> model2 = FMRegressionModel.load(model_path)
    >>> model2.intercept
    -0.0032501766849261557
    >>> model2.linear
    DenseVector([0.9978])
    >>> model2.factors
    DenseMatrix(1, 2, [0.0173, 0.0021], 1)
    >>> model.transform(test0).take(1) == model2.transform(test0).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', factorSize: int = 8, fitIntercept: bool = True, fitLinear: bool = True, regParam: float = 0.0, miniBatchFraction: float = 1.0, initStd: float = 0.01, maxIter: int = 100, stepSize: float = 1.0, tol: float = 1e-06, solver: str = 'adamW', seed: int | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                  factorSize=8, fitIntercept=True, fitLinear=True, regParam=0.0,                  miniBatchFraction=1.0, initStd=0.01, maxIter=100, stepSize=1.0,                  tol=1e-6, solver="adamW", seed=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', labelCol: str = 'label', predictionCol: str = 'prediction', factorSize: int = 8, fitIntercept: bool = True, fitLinear: bool = True, regParam: float = 0.0, miniBatchFraction: float = 1.0, initStd: float = 0.01, maxIter: int = 100, stepSize: float = 1.0, tol: float = 1e-06, solver: str = 'adamW', seed: int | None = None) -> FMRegressor:
        '''
        setParams(self, \\*, featuresCol="features", labelCol="label", predictionCol="prediction",                   factorSize=8, fitIntercept=True, fitLinear=True, regParam=0.0,                   miniBatchFraction=1.0, initStd=0.01, maxIter=100, stepSize=1.0,                   tol=1e-6, solver="adamW", seed=None)
        Sets Params for FMRegressor.
        '''
    def setFactorSize(self, value: int) -> FMRegressor:
        """
        Sets the value of :py:attr:`factorSize`.
        """
    def setFitLinear(self, value: bool) -> FMRegressor:
        """
        Sets the value of :py:attr:`fitLinear`.
        """
    def setMiniBatchFraction(self, value: float) -> FMRegressor:
        """
        Sets the value of :py:attr:`miniBatchFraction`.
        """
    def setInitStd(self, value: float) -> FMRegressor:
        """
        Sets the value of :py:attr:`initStd`.
        """
    def setMaxIter(self, value: int) -> FMRegressor:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setStepSize(self, value: float) -> FMRegressor:
        """
        Sets the value of :py:attr:`stepSize`.
        """
    def setTol(self, value: float) -> FMRegressor:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setSolver(self, value: str) -> FMRegressor:
        """
        Sets the value of :py:attr:`solver`.
        """
    def setSeed(self, value: int) -> FMRegressor:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setFitIntercept(self, value: bool) -> FMRegressor:
        """
        Sets the value of :py:attr:`fitIntercept`.
        """
    def setRegParam(self, value: float) -> FMRegressor:
        """
        Sets the value of :py:attr:`regParam`.
        """

class FMRegressionModel(_JavaRegressionModel, _FactorizationMachinesParams, JavaMLWritable, JavaMLReadable['FMRegressionModel']):
    """
    Model fitted by :class:`FMRegressor`.

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
