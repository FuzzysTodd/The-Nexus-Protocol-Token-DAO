from abc import ABCMeta
from pyspark.ml._typing import BinaryClassificationEvaluatorMetricType, ClusteringEvaluatorDistanceMeasureType, ClusteringEvaluatorMetricType, MulticlassClassificationEvaluatorMetricType, MultilabelClassificationEvaluatorMetricType, ParamMap, RankingEvaluatorMetricType, RegressionEvaluatorMetricType
from pyspark.ml.param import Param, Params
from pyspark.ml.param.shared import HasFeaturesCol, HasLabelCol, HasPredictionCol, HasProbabilityCol, HasRawPredictionCol, HasWeightCol
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaParams
from pyspark.sql.dataframe import DataFrame

__all__ = ['Evaluator', 'BinaryClassificationEvaluator', 'RegressionEvaluator', 'MulticlassClassificationEvaluator', 'MultilabelClassificationEvaluator', 'ClusteringEvaluator', 'RankingEvaluator']

class Evaluator(Params, metaclass=ABCMeta):
    """
    Base class for evaluators that compute metrics from predictions.

    .. versionadded:: 1.4.0
    """
    def evaluate(self, dataset: DataFrame, params: ParamMap | None = None) -> float:
        """
        Evaluates the output with optional parameters.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
            a dataset that contains labels/observations and predictions
        params : dict, optional
            an optional param map that overrides embedded params

        Returns
        -------
        float
            metric
        """
    def isLargerBetter(self) -> bool:
        """
        Indicates whether the metric returned by :py:meth:`evaluate` should be maximized
        (True, default) or minimized (False).
        A given evaluator may support multiple metrics which may be maximized or minimized.
        """

class JavaEvaluator(JavaParams, Evaluator, metaclass=ABCMeta):
    """
    Base class for :py:class:`Evaluator`s that wrap Java/Scala
    implementations.
    """
    def isLargerBetter(self) -> bool: ...

class BinaryClassificationEvaluator(JavaEvaluator, HasLabelCol, HasRawPredictionCol, HasWeightCol, JavaMLReadable['BinaryClassificationEvaluator'], JavaMLWritable):
    '''
    Evaluator for binary classification, which expects input columns rawPrediction, label
    and an optional weight column.
    The rawPrediction column can be of type double (binary 0/1 prediction, or probability of label
    1) or of type vector (length-2 vector of raw predictions, scores, or label probabilities).

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> scoreAndLabels = map(lambda x: (Vectors.dense([1.0 - x[0], x[0]]), x[1]),
    ...    [(0.1, 0.0), (0.1, 1.0), (0.4, 0.0), (0.6, 0.0), (0.6, 1.0), (0.6, 1.0), (0.8, 1.0)])
    >>> dataset = spark.createDataFrame(scoreAndLabels, ["raw", "label"])
    ...
    >>> evaluator = BinaryClassificationEvaluator()
    >>> evaluator.setRawPredictionCol("raw")
    BinaryClassificationEvaluator...
    >>> evaluator.evaluate(dataset)
    0.70...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "areaUnderPR"})
    0.83...
    >>> bce_path = temp_path + "/bce"
    >>> evaluator.save(bce_path)
    >>> evaluator2 = BinaryClassificationEvaluator.load(bce_path)
    >>> str(evaluator2.getRawPredictionCol())
    \'raw\'
    >>> scoreAndLabelsAndWeight = map(lambda x: (Vectors.dense([1.0 - x[0], x[0]]), x[1], x[2]),
    ...    [(0.1, 0.0, 1.0), (0.1, 1.0, 0.9), (0.4, 0.0, 0.7), (0.6, 0.0, 0.9),
    ...     (0.6, 1.0, 1.0), (0.6, 1.0, 0.3), (0.8, 1.0, 1.0)])
    >>> dataset = spark.createDataFrame(scoreAndLabelsAndWeight, ["raw", "label", "weight"])
    ...
    >>> evaluator = BinaryClassificationEvaluator(rawPredictionCol="raw", weightCol="weight")
    >>> evaluator.evaluate(dataset)
    0.70...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "areaUnderPR"})
    0.82...
    >>> evaluator.getNumBins()
    1000
    '''
    metricName: Param['BinaryClassificationEvaluatorMetricType']
    numBins: Param[int]
    def __init__(self, *, rawPredictionCol: str = 'rawPrediction', labelCol: str = 'label', metricName: BinaryClassificationEvaluatorMetricType = 'areaUnderROC', weightCol: str | None = None, numBins: int = 1000) -> None:
        '''
        __init__(self, \\*, rawPredictionCol="rawPrediction", labelCol="label",                  metricName="areaUnderROC", weightCol=None, numBins=1000)
        '''
    def setMetricName(self, value: BinaryClassificationEvaluatorMetricType) -> BinaryClassificationEvaluator:
        """
        Sets the value of :py:attr:`metricName`.
        """
    def getMetricName(self) -> str:
        """
        Gets the value of metricName or its default value.
        """
    def setNumBins(self, value: int) -> BinaryClassificationEvaluator:
        """
        Sets the value of :py:attr:`numBins`.
        """
    def getNumBins(self) -> int:
        """
        Gets the value of numBins or its default value.
        """
    def setLabelCol(self, value: str) -> BinaryClassificationEvaluator:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setRawPredictionCol(self, value: str) -> BinaryClassificationEvaluator:
        """
        Sets the value of :py:attr:`rawPredictionCol`.
        """
    def setWeightCol(self, value: str) -> BinaryClassificationEvaluator:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setParams(self, *, rawPredictionCol: str = 'rawPrediction', labelCol: str = 'label', metricName: BinaryClassificationEvaluatorMetricType = 'areaUnderROC', weightCol: str | None = None, numBins: int = 1000) -> BinaryClassificationEvaluator:
        '''
        setParams(self, \\*, rawPredictionCol="rawPrediction", labelCol="label",                   metricName="areaUnderROC", weightCol=None, numBins=1000)
        Sets params for binary classification evaluator.
        '''

class RegressionEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, HasWeightCol, JavaMLReadable['RegressionEvaluator'], JavaMLWritable):
    '''
    Evaluator for Regression, which expects input columns prediction, label
    and an optional weight column.

    .. versionadded:: 1.4.0

    Examples
    --------
    >>> scoreAndLabels = [(-28.98343821, -27.0), (20.21491975, 21.5),
    ...   (-25.98418959, -22.0), (30.69731842, 33.0), (74.69283752, 71.0)]
    >>> dataset = spark.createDataFrame(scoreAndLabels, ["raw", "label"])
    ...
    >>> evaluator = RegressionEvaluator()
    >>> evaluator.setPredictionCol("raw")
    RegressionEvaluator...
    >>> evaluator.evaluate(dataset)
    2.842...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "r2"})
    0.993...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "mae"})
    2.649...
    >>> re_path = temp_path + "/re"
    >>> evaluator.save(re_path)
    >>> evaluator2 = RegressionEvaluator.load(re_path)
    >>> str(evaluator2.getPredictionCol())
    \'raw\'
    >>> scoreAndLabelsAndWeight = [(-28.98343821, -27.0, 1.0), (20.21491975, 21.5, 0.8),
    ...   (-25.98418959, -22.0, 1.0), (30.69731842, 33.0, 0.6), (74.69283752, 71.0, 0.2)]
    >>> dataset = spark.createDataFrame(scoreAndLabelsAndWeight, ["raw", "label", "weight"])
    ...
    >>> evaluator = RegressionEvaluator(predictionCol="raw", weightCol="weight")
    >>> evaluator.evaluate(dataset)
    2.740...
    >>> evaluator.getThroughOrigin()
    False
    '''
    metricName: Param['RegressionEvaluatorMetricType']
    throughOrigin: Param[bool]
    def __init__(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: RegressionEvaluatorMetricType = 'rmse', weightCol: str | None = None, throughOrigin: bool = False) -> None:
        '''
        __init__(self, \\*, predictionCol="prediction", labelCol="label",                  metricName="rmse", weightCol=None, throughOrigin=False)
        '''
    def setMetricName(self, value: RegressionEvaluatorMetricType) -> RegressionEvaluator:
        """
        Sets the value of :py:attr:`metricName`.
        """
    def getMetricName(self) -> RegressionEvaluatorMetricType:
        """
        Gets the value of metricName or its default value.
        """
    def setThroughOrigin(self, value: bool) -> RegressionEvaluator:
        """
        Sets the value of :py:attr:`throughOrigin`.
        """
    def getThroughOrigin(self) -> bool:
        """
        Gets the value of throughOrigin or its default value.
        """
    def setLabelCol(self, value: str) -> RegressionEvaluator:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setPredictionCol(self, value: str) -> RegressionEvaluator:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setWeightCol(self, value: str) -> RegressionEvaluator:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setParams(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: RegressionEvaluatorMetricType = 'rmse', weightCol: str | None = None, throughOrigin: bool = False) -> RegressionEvaluator:
        '''
        setParams(self, \\*, predictionCol="prediction", labelCol="label",                   metricName="rmse", weightCol=None, throughOrigin=False)
        Sets params for regression evaluator.
        '''

class MulticlassClassificationEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, HasWeightCol, HasProbabilityCol, JavaMLReadable['MulticlassClassificationEvaluator'], JavaMLWritable):
    '''
    Evaluator for Multiclass Classification, which expects input
    columns: prediction, label, weight (optional) and probabilityCol (only for logLoss).

    .. versionadded:: 1.5.0

    Examples
    --------
    >>> scoreAndLabels = [(0.0, 0.0), (0.0, 1.0), (0.0, 0.0),
    ...     (1.0, 0.0), (1.0, 1.0), (1.0, 1.0), (1.0, 1.0), (2.0, 2.0), (2.0, 0.0)]
    >>> dataset = spark.createDataFrame(scoreAndLabels, ["prediction", "label"])
    >>> evaluator = MulticlassClassificationEvaluator()
    >>> evaluator.setPredictionCol("prediction")
    MulticlassClassificationEvaluator...
    >>> evaluator.evaluate(dataset)
    0.66...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "accuracy"})
    0.66...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "truePositiveRateByLabel",
    ...     evaluator.metricLabel: 1.0})
    0.75...
    >>> evaluator.setMetricName("hammingLoss")
    MulticlassClassificationEvaluator...
    >>> evaluator.evaluate(dataset)
    0.33...
    >>> mce_path = temp_path + "/mce"
    >>> evaluator.save(mce_path)
    >>> evaluator2 = MulticlassClassificationEvaluator.load(mce_path)
    >>> str(evaluator2.getPredictionCol())
    \'prediction\'
    >>> scoreAndLabelsAndWeight = [(0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (0.0, 0.0, 1.0),
    ...     (1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 1.0),
    ...     (2.0, 2.0, 1.0), (2.0, 0.0, 1.0)]
    >>> dataset = spark.createDataFrame(scoreAndLabelsAndWeight, ["prediction", "label", "weight"])
    >>> evaluator = MulticlassClassificationEvaluator(predictionCol="prediction",
    ...     weightCol="weight")
    >>> evaluator.evaluate(dataset)
    0.66...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "accuracy"})
    0.66...
    >>> predictionAndLabelsWithProbabilities = [
    ...      (1.0, 1.0, 1.0, [0.1, 0.8, 0.1]), (0.0, 2.0, 1.0, [0.9, 0.05, 0.05]),
    ...      (0.0, 0.0, 1.0, [0.8, 0.2, 0.0]), (1.0, 1.0, 1.0, [0.3, 0.65, 0.05])]
    >>> dataset = spark.createDataFrame(predictionAndLabelsWithProbabilities, ["prediction",
    ...     "label", "weight", "probability"])
    >>> evaluator = MulticlassClassificationEvaluator(predictionCol="prediction",
    ...     probabilityCol="probability")
    >>> evaluator.setMetricName("logLoss")
    MulticlassClassificationEvaluator...
    >>> evaluator.evaluate(dataset)
    0.9682...
    '''
    metricName: Param['MulticlassClassificationEvaluatorMetricType']
    metricLabel: Param[float]
    beta: Param[float]
    eps: Param[float]
    def __init__(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: MulticlassClassificationEvaluatorMetricType = 'f1', weightCol: str | None = None, metricLabel: float = 0.0, beta: float = 1.0, probabilityCol: str = 'probability', eps: float = 1e-15) -> None:
        '''
        __init__(self, \\*, predictionCol="prediction", labelCol="label",                  metricName="f1", weightCol=None, metricLabel=0.0, beta=1.0,                  probabilityCol="probability", eps=1e-15)
        '''
    def setMetricName(self, value: MulticlassClassificationEvaluatorMetricType) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`metricName`.
        """
    def getMetricName(self) -> MulticlassClassificationEvaluatorMetricType:
        """
        Gets the value of metricName or its default value.
        """
    def setMetricLabel(self, value: float) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`metricLabel`.
        """
    def getMetricLabel(self) -> float:
        """
        Gets the value of metricLabel or its default value.
        """
    def setBeta(self, value: float) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`beta`.
        """
    def getBeta(self) -> float:
        """
        Gets the value of beta or its default value.
        """
    def setEps(self, value: float) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`eps`.
        """
    def getEps(self) -> float:
        """
        Gets the value of eps or its default value.
        """
    def setLabelCol(self, value: str) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setPredictionCol(self, value: str) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setProbabilityCol(self, value: str) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`probabilityCol`.
        """
    def setWeightCol(self, value: str) -> MulticlassClassificationEvaluator:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setParams(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: MulticlassClassificationEvaluatorMetricType = 'f1', weightCol: str | None = None, metricLabel: float = 0.0, beta: float = 1.0, probabilityCol: str = 'probability', eps: float = 1e-15) -> MulticlassClassificationEvaluator:
        '''
        setParams(self, \\*, predictionCol="prediction", labelCol="label",                   metricName="f1", weightCol=None, metricLabel=0.0, beta=1.0,                   probabilityCol="probability", eps=1e-15)
        Sets params for multiclass classification evaluator.
        '''

class MultilabelClassificationEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, JavaMLReadable['MultilabelClassificationEvaluator'], JavaMLWritable):
    '''
    Evaluator for Multilabel Classification, which expects two input
    columns: prediction and label.

    .. versionadded:: 3.0.0

    Notes
    -----
    Experimental

    Examples
    --------
    >>> scoreAndLabels = [([0.0, 1.0], [0.0, 2.0]), ([0.0, 2.0], [0.0, 1.0]),
    ...     ([], [0.0]), ([2.0], [2.0]), ([2.0, 0.0], [2.0, 0.0]),
    ...     ([0.0, 1.0, 2.0], [0.0, 1.0]), ([1.0], [1.0, 2.0])]
    >>> dataset = spark.createDataFrame(scoreAndLabels, ["prediction", "label"])
    ...
    >>> evaluator = MultilabelClassificationEvaluator()
    >>> evaluator.setPredictionCol("prediction")
    MultilabelClassificationEvaluator...
    >>> evaluator.evaluate(dataset)
    0.63...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "accuracy"})
    0.54...
    >>> mlce_path = temp_path + "/mlce"
    >>> evaluator.save(mlce_path)
    >>> evaluator2 = MultilabelClassificationEvaluator.load(mlce_path)
    >>> str(evaluator2.getPredictionCol())
    \'prediction\'
    '''
    metricName: Param['MultilabelClassificationEvaluatorMetricType']
    metricLabel: Param[float]
    def __init__(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: MultilabelClassificationEvaluatorMetricType = 'f1Measure', metricLabel: float = 0.0) -> None:
        '''
        __init__(self, \\*, predictionCol="prediction", labelCol="label",                  metricName="f1Measure", metricLabel=0.0)
        '''
    def setMetricName(self, value: MultilabelClassificationEvaluatorMetricType) -> MultilabelClassificationEvaluator:
        """
        Sets the value of :py:attr:`metricName`.
        """
    def getMetricName(self) -> MultilabelClassificationEvaluatorMetricType:
        """
        Gets the value of metricName or its default value.
        """
    def setMetricLabel(self, value: float) -> MultilabelClassificationEvaluator:
        """
        Sets the value of :py:attr:`metricLabel`.
        """
    def getMetricLabel(self) -> float:
        """
        Gets the value of metricLabel or its default value.
        """
    def setLabelCol(self, value: str) -> MultilabelClassificationEvaluator:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setPredictionCol(self, value: str) -> MultilabelClassificationEvaluator:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setParams(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: MultilabelClassificationEvaluatorMetricType = 'f1Measure', metricLabel: float = 0.0) -> MultilabelClassificationEvaluator:
        '''
        setParams(self, \\*, predictionCol="prediction", labelCol="label",                   metricName="f1Measure", metricLabel=0.0)
        Sets params for multilabel classification evaluator.
        '''

class ClusteringEvaluator(JavaEvaluator, HasPredictionCol, HasFeaturesCol, HasWeightCol, JavaMLReadable['ClusteringEvaluator'], JavaMLWritable):
    '''
    Evaluator for Clustering results, which expects two input
    columns: prediction and features. The metric computes the Silhouette
    measure using the squared Euclidean distance.

    The Silhouette is a measure for the validation of the consistency
    within clusters. It ranges between 1 and -1, where a value close to
    1 means that the points in a cluster are close to the other points
    in the same cluster and far from the points of the other clusters.

    .. versionadded:: 2.3.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> featureAndPredictions = map(lambda x: (Vectors.dense(x[0]), x[1]),
    ...     [([0.0, 0.5], 0.0), ([0.5, 0.0], 0.0), ([10.0, 11.0], 1.0),
    ...     ([10.5, 11.5], 1.0), ([1.0, 1.0], 0.0), ([8.0, 6.0], 1.0)])
    >>> dataset = spark.createDataFrame(featureAndPredictions, ["features", "prediction"])
    ...
    >>> evaluator = ClusteringEvaluator()
    >>> evaluator.setPredictionCol("prediction")
    ClusteringEvaluator...
    >>> evaluator.evaluate(dataset)
    0.9079...
    >>> featureAndPredictionsWithWeight = map(lambda x: (Vectors.dense(x[0]), x[1], x[2]),
    ...     [([0.0, 0.5], 0.0, 2.5), ([0.5, 0.0], 0.0, 2.5), ([10.0, 11.0], 1.0, 2.5),
    ...     ([10.5, 11.5], 1.0, 2.5), ([1.0, 1.0], 0.0, 2.5), ([8.0, 6.0], 1.0, 2.5)])
    >>> dataset = spark.createDataFrame(
    ...     featureAndPredictionsWithWeight, ["features", "prediction", "weight"])
    >>> evaluator = ClusteringEvaluator()
    >>> evaluator.setPredictionCol("prediction")
    ClusteringEvaluator...
    >>> evaluator.setWeightCol("weight")
    ClusteringEvaluator...
    >>> evaluator.evaluate(dataset)
    0.9079...
    >>> ce_path = temp_path + "/ce"
    >>> evaluator.save(ce_path)
    >>> evaluator2 = ClusteringEvaluator.load(ce_path)
    >>> str(evaluator2.getPredictionCol())
    \'prediction\'
    '''
    metricName: Param['ClusteringEvaluatorMetricType']
    distanceMeasure: Param['ClusteringEvaluatorDistanceMeasureType']
    def __init__(self, *, predictionCol: str = 'prediction', featuresCol: str = 'features', metricName: ClusteringEvaluatorMetricType = 'silhouette', distanceMeasure: str = 'squaredEuclidean', weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, predictionCol="prediction", featuresCol="features",                  metricName="silhouette", distanceMeasure="squaredEuclidean", weightCol=None)
        '''
    def setParams(self, *, predictionCol: str = 'prediction', featuresCol: str = 'features', metricName: ClusteringEvaluatorMetricType = 'silhouette', distanceMeasure: str = 'squaredEuclidean', weightCol: str | None = None) -> ClusteringEvaluator:
        '''
        setParams(self, \\*, predictionCol="prediction", featuresCol="features",                   metricName="silhouette", distanceMeasure="squaredEuclidean", weightCol=None)
        Sets params for clustering evaluator.
        '''
    def setMetricName(self, value: ClusteringEvaluatorMetricType) -> ClusteringEvaluator:
        """
        Sets the value of :py:attr:`metricName`.
        """
    def getMetricName(self) -> ClusteringEvaluatorMetricType:
        """
        Gets the value of metricName or its default value.
        """
    def setDistanceMeasure(self, value: ClusteringEvaluatorDistanceMeasureType) -> ClusteringEvaluator:
        """
        Sets the value of :py:attr:`distanceMeasure`.
        """
    def getDistanceMeasure(self) -> ClusteringEvaluatorDistanceMeasureType:
        """
        Gets the value of `distanceMeasure`
        """
    def setFeaturesCol(self, value: str) -> ClusteringEvaluator:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> ClusteringEvaluator:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setWeightCol(self, value: str) -> ClusteringEvaluator:
        """
        Sets the value of :py:attr:`weightCol`.
        """

class RankingEvaluator(JavaEvaluator, HasLabelCol, HasPredictionCol, JavaMLReadable['RankingEvaluator'], JavaMLWritable):
    '''
    Evaluator for Ranking, which expects two input
    columns: prediction and label.

    .. versionadded:: 3.0.0

    Notes
    -----
    Experimental

    Examples
    --------
    >>> scoreAndLabels = [([1.0, 6.0, 2.0, 7.0, 8.0, 3.0, 9.0, 10.0, 4.0, 5.0],
    ...     [1.0, 2.0, 3.0, 4.0, 5.0]),
    ...     ([4.0, 1.0, 5.0, 6.0, 2.0, 7.0, 3.0, 8.0, 9.0, 10.0], [1.0, 2.0, 3.0]),
    ...     ([1.0, 2.0, 3.0, 4.0, 5.0], [])]
    >>> dataset = spark.createDataFrame(scoreAndLabels, ["prediction", "label"])
    ...
    >>> evaluator = RankingEvaluator()
    >>> evaluator.setPredictionCol("prediction")
    RankingEvaluator...
    >>> evaluator.evaluate(dataset)
    0.35...
    >>> evaluator.evaluate(dataset, {evaluator.metricName: "precisionAtK", evaluator.k: 2})
    0.33...
    >>> ranke_path = temp_path + "/ranke"
    >>> evaluator.save(ranke_path)
    >>> evaluator2 = RankingEvaluator.load(ranke_path)
    >>> str(evaluator2.getPredictionCol())
    \'prediction\'
    '''
    metricName: Param['RankingEvaluatorMetricType']
    k: Param[int]
    def __init__(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: RankingEvaluatorMetricType = 'meanAveragePrecision', k: int = 10) -> None:
        '''
        __init__(self, \\*, predictionCol="prediction", labelCol="label",                  metricName="meanAveragePrecision", k=10)
        '''
    def setMetricName(self, value: RankingEvaluatorMetricType) -> RankingEvaluator:
        """
        Sets the value of :py:attr:`metricName`.
        """
    def getMetricName(self) -> RankingEvaluatorMetricType:
        """
        Gets the value of metricName or its default value.
        """
    def setK(self, value: int) -> RankingEvaluator:
        """
        Sets the value of :py:attr:`k`.
        """
    def getK(self) -> int:
        """
        Gets the value of k or its default value.
        """
    def setLabelCol(self, value: str) -> RankingEvaluator:
        """
        Sets the value of :py:attr:`labelCol`.
        """
    def setPredictionCol(self, value: str) -> RankingEvaluator:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setParams(self, *, predictionCol: str = 'prediction', labelCol: str = 'label', metricName: RankingEvaluatorMetricType = 'meanAveragePrecision', k: int = 10) -> RankingEvaluator:
        '''
        setParams(self, \\*, predictionCol="prediction", labelCol="label",                   metricName="meanAveragePrecision", k=10)
        Sets params for ranking evaluator.
        '''
