from pyspark.mllib.common import JavaModelWrapper
from pyspark.mllib.linalg import Matrix
from pyspark.rdd import RDD
from typing import Generic, List, Tuple, TypeVar

__all__ = ['BinaryClassificationMetrics', 'RegressionMetrics', 'MulticlassMetrics', 'RankingMetrics']

T = TypeVar('T')

class BinaryClassificationMetrics(JavaModelWrapper):
    """
    Evaluator for binary classification.

    .. versionadded:: 1.4.0

    Parameters
    ----------
    scoreAndLabels : :py:class:`pyspark.RDD`
        an RDD of score, label and optional weight.

    Examples
    --------
    >>> scoreAndLabels = sc.parallelize([
    ...     (0.1, 0.0), (0.1, 1.0), (0.4, 0.0), (0.6, 0.0), (0.6, 1.0), (0.6, 1.0), (0.8, 1.0)], 2)
    >>> metrics = BinaryClassificationMetrics(scoreAndLabels)
    >>> metrics.areaUnderROC
    0.70...
    >>> metrics.areaUnderPR
    0.83...
    >>> metrics.unpersist()
    >>> scoreAndLabelsWithOptWeight = sc.parallelize([
    ...     (0.1, 0.0, 1.0), (0.1, 1.0, 0.4), (0.4, 0.0, 0.2), (0.6, 0.0, 0.6), (0.6, 1.0, 0.9),
    ...     (0.6, 1.0, 0.5), (0.8, 1.0, 0.7)], 2)
    >>> metrics = BinaryClassificationMetrics(scoreAndLabelsWithOptWeight)
    >>> metrics.areaUnderROC
    0.79...
    >>> metrics.areaUnderPR
    0.88...
    """
    def __init__(self, scoreAndLabels: RDD[Tuple[float, float]]) -> None: ...
    @property
    def areaUnderROC(self) -> float:
        """
        Computes the area under the receiver operating characteristic
        (ROC) curve.
        """
    @property
    def areaUnderPR(self) -> float:
        """
        Computes the area under the precision-recall curve.
        """
    def unpersist(self) -> None:
        """
        Unpersists intermediate RDDs used in the computation.
        """

class RegressionMetrics(JavaModelWrapper):
    """
    Evaluator for regression.

    .. versionadded:: 1.4.0

    Parameters
    ----------
    predictionAndObservations : :py:class:`pyspark.RDD`
        an RDD of prediction, observation and optional weight.

    Examples
    --------
    >>> predictionAndObservations = sc.parallelize([
    ...     (2.5, 3.0), (0.0, -0.5), (2.0, 2.0), (8.0, 7.0)])
    >>> metrics = RegressionMetrics(predictionAndObservations)
    >>> metrics.explainedVariance
    8.859...
    >>> metrics.meanAbsoluteError
    0.5...
    >>> metrics.meanSquaredError
    0.37...
    >>> metrics.rootMeanSquaredError
    0.61...
    >>> metrics.r2
    0.94...
    >>> predictionAndObservationsWithOptWeight = sc.parallelize([
    ...     (2.5, 3.0, 0.5), (0.0, -0.5, 1.0), (2.0, 2.0, 0.3), (8.0, 7.0, 0.9)])
    >>> metrics = RegressionMetrics(predictionAndObservationsWithOptWeight)
    >>> metrics.rootMeanSquaredError
    0.68...
    """
    def __init__(self, predictionAndObservations: RDD[Tuple[float, float]]) -> None: ...
    @property
    def explainedVariance(self) -> float:
        """
        Returns the explained variance regression score.
        explainedVariance = :math:`1 - \\frac{variance(y - \\hat{y})}{variance(y)}`
        """
    @property
    def meanAbsoluteError(self) -> float:
        """
        Returns the mean absolute error, which is a risk function corresponding to the
        expected value of the absolute error loss or l1-norm loss.
        """
    @property
    def meanSquaredError(self) -> float:
        """
        Returns the mean squared error, which is a risk function corresponding to the
        expected value of the squared error loss or quadratic loss.
        """
    @property
    def rootMeanSquaredError(self) -> float:
        """
        Returns the root mean squared error, which is defined as the square root of
        the mean squared error.
        """
    @property
    def r2(self) -> float:
        """
        Returns R^2^, the coefficient of determination.
        """

class MulticlassMetrics(JavaModelWrapper):
    """
    Evaluator for multiclass classification.

    .. versionadded:: 1.4.0

    Parameters
    ----------
    predictionAndLabels : :py:class:`pyspark.RDD`
        an RDD of prediction, label, optional weight and optional probability.

    Examples
    --------
    >>> predictionAndLabels = sc.parallelize([(0.0, 0.0), (0.0, 1.0), (0.0, 0.0),
    ...     (1.0, 0.0), (1.0, 1.0), (1.0, 1.0), (1.0, 1.0), (2.0, 2.0), (2.0, 0.0)])
    >>> metrics = MulticlassMetrics(predictionAndLabels)
    >>> metrics.confusionMatrix().toArray()
    array([[ 2.,  1.,  1.],
           [ 1.,  3.,  0.],
           [ 0.,  0.,  1.]])
    >>> metrics.falsePositiveRate(0.0)
    0.2...
    >>> metrics.precision(1.0)
    0.75...
    >>> metrics.recall(2.0)
    1.0...
    >>> metrics.fMeasure(0.0, 2.0)
    0.52...
    >>> metrics.accuracy
    0.66...
    >>> metrics.weightedFalsePositiveRate
    0.19...
    >>> metrics.weightedPrecision
    0.68...
    >>> metrics.weightedRecall
    0.66...
    >>> metrics.weightedFMeasure()
    0.66...
    >>> metrics.weightedFMeasure(2.0)
    0.65...
    >>> predAndLabelsWithOptWeight = sc.parallelize([(0.0, 0.0, 1.0), (0.0, 1.0, 1.0),
    ...      (0.0, 0.0, 1.0), (1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 1.0), (1.0, 1.0, 1.0),
    ...      (2.0, 2.0, 1.0), (2.0, 0.0, 1.0)])
    >>> metrics = MulticlassMetrics(predAndLabelsWithOptWeight)
    >>> metrics.confusionMatrix().toArray()
    array([[ 2.,  1.,  1.],
           [ 1.,  3.,  0.],
           [ 0.,  0.,  1.]])
    >>> metrics.falsePositiveRate(0.0)
    0.2...
    >>> metrics.precision(1.0)
    0.75...
    >>> metrics.recall(2.0)
    1.0...
    >>> metrics.fMeasure(0.0, 2.0)
    0.52...
    >>> metrics.accuracy
    0.66...
    >>> metrics.weightedFalsePositiveRate
    0.19...
    >>> metrics.weightedPrecision
    0.68...
    >>> metrics.weightedRecall
    0.66...
    >>> metrics.weightedFMeasure()
    0.66...
    >>> metrics.weightedFMeasure(2.0)
    0.65...
    >>> predictionAndLabelsWithProbabilities = sc.parallelize([
    ...      (1.0, 1.0, 1.0, [0.1, 0.8, 0.1]), (0.0, 2.0, 1.0, [0.9, 0.05, 0.05]),
    ...      (0.0, 0.0, 1.0, [0.8, 0.2, 0.0]), (1.0, 1.0, 1.0, [0.3, 0.65, 0.05])])
    >>> metrics = MulticlassMetrics(predictionAndLabelsWithProbabilities)
    >>> metrics.logLoss()
    0.9682...
    """
    def __init__(self, predictionAndLabels: RDD[Tuple[float, float]]) -> None: ...
    def confusionMatrix(self) -> Matrix:
        '''
        Returns confusion matrix: predicted classes are in columns,
        they are ordered by class label ascending, as in "labels".
        '''
    def truePositiveRate(self, label: float) -> float:
        """
        Returns true positive rate for a given label (category).
        """
    def falsePositiveRate(self, label: float) -> float:
        """
        Returns false positive rate for a given label (category).
        """
    def precision(self, label: float) -> float:
        """
        Returns precision.
        """
    def recall(self, label: float) -> float:
        """
        Returns recall.
        """
    def fMeasure(self, label: float, beta: float | None = None) -> float:
        """
        Returns f-measure.
        """
    @property
    def accuracy(self) -> float:
        """
        Returns accuracy (equals to the total number of correctly classified instances
        out of the total number of instances).
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
    def weightedFMeasure(self, beta: float | None = None) -> float:
        """
        Returns weighted averaged f-measure.
        """
    def logLoss(self, eps: float = 1e-15) -> float:
        """
        Returns weighted logLoss.
        """

class RankingMetrics(JavaModelWrapper, Generic[T]):
    """
    Evaluator for ranking algorithms.

    .. versionadded:: 1.4.0

    Parameters
    ----------
    predictionAndLabels : :py:class:`pyspark.RDD`
        an RDD of (predicted ranking, ground truth set) pairs
        or (predicted ranking, ground truth set,
        relevance value of ground truth set).
        Since 3.4.0, it supports ndcg evaluation with relevance value.

    Examples
    --------
    >>> predictionAndLabels = sc.parallelize([
    ...     ([1, 6, 2, 7, 8, 3, 9, 10, 4, 5], [1, 2, 3, 4, 5]),
    ...     ([4, 1, 5, 6, 2, 7, 3, 8, 9, 10], [1, 2, 3]),
    ...     ([1, 2, 3, 4, 5], [])])
    >>> metrics = RankingMetrics(predictionAndLabels)
    >>> metrics.precisionAt(1)
    0.33...
    >>> metrics.precisionAt(5)
    0.26...
    >>> metrics.precisionAt(15)
    0.17...
    >>> metrics.meanAveragePrecision
    0.35...
    >>> metrics.meanAveragePrecisionAt(1)
    0.3333333333333333...
    >>> metrics.meanAveragePrecisionAt(2)
    0.25...
    >>> metrics.ndcgAt(3)
    0.33...
    >>> metrics.ndcgAt(10)
    0.48...
    >>> metrics.recallAt(1)
    0.06...
    >>> metrics.recallAt(5)
    0.35...
    >>> metrics.recallAt(15)
    0.66...
    """
    def __init__(self, predictionAndLabels: RDD[Tuple[List[T], List[T]]] | RDD[Tuple[List[T], List[T], List[float]]]) -> None: ...
    def precisionAt(self, k: int) -> float:
        """
        Compute the average precision of all the queries, truncated at ranking position k.

        If for a query, the ranking algorithm returns n (n < k) results, the precision value
        will be computed as #(relevant items retrieved) / k. This formula also applies when
        the size of the ground truth set is less than k.

        If a query has an empty ground truth set, zero will be used as precision together
        with a log warning.
        """
    @property
    def meanAveragePrecision(self) -> float:
        """
        Returns the mean average precision (MAP) of all the queries.
        If a query has an empty ground truth set, the average precision will be zero and
        a log warning is generated.
        """
    def meanAveragePrecisionAt(self, k: int) -> float:
        """
        Returns the mean average precision (MAP) at first k ranking of all the queries.
        If a query has an empty ground truth set, the average precision will be zero and
        a log warning is generated.
        """
    def ndcgAt(self, k: int) -> float:
        """
        Compute the average NDCG value of all the queries, truncated at ranking position k.
        The discounted cumulative gain at position k is computed as:
        sum,,i=1,,^k^ (2^{relevance of ''i''th item}^ - 1) / log(i + 1),
        and the NDCG is obtained by dividing the DCG value on the ground truth set.
        In the current implementation, the relevance value is binary.
        If a query has an empty ground truth set, zero will be used as NDCG together with
        a log warning.
        """
    def recallAt(self, k: int) -> float:
        """
        Compute the average recall of all the queries, truncated at ranking position k.

        If for a query, the ranking algorithm returns n results, the recall value
        will be computed as #(relevant items retrieved) / #(ground truth set).
        This formula also applies when the size of the ground truth set is less than k.

        If a query has an empty ground truth set, zero will be used as recall together
        with a log warning.
        """

class MultilabelMetrics(JavaModelWrapper):
    """
    Evaluator for multilabel classification.

    .. versionadded:: 1.4.0

    Parameters
    ----------
    predictionAndLabels : :py:class:`pyspark.RDD`
        an RDD of (predictions, labels) pairs,
        both are non-null Arrays, each with unique elements.

    Examples
    --------
    >>> predictionAndLabels = sc.parallelize([([0.0, 1.0], [0.0, 2.0]), ([0.0, 2.0], [0.0, 1.0]),
    ...     ([], [0.0]), ([2.0], [2.0]), ([2.0, 0.0], [2.0, 0.0]),
    ...     ([0.0, 1.0, 2.0], [0.0, 1.0]), ([1.0], [1.0, 2.0])])
    >>> metrics = MultilabelMetrics(predictionAndLabels)
    >>> metrics.precision(0.0)
    1.0
    >>> metrics.recall(1.0)
    0.66...
    >>> metrics.f1Measure(2.0)
    0.5
    >>> metrics.precision()
    0.66...
    >>> metrics.recall()
    0.64...
    >>> metrics.f1Measure()
    0.63...
    >>> metrics.microPrecision
    0.72...
    >>> metrics.microRecall
    0.66...
    >>> metrics.microF1Measure
    0.69...
    >>> metrics.hammingLoss
    0.33...
    >>> metrics.subsetAccuracy
    0.28...
    >>> metrics.accuracy
    0.54...
    """
    def __init__(self, predictionAndLabels: RDD[Tuple[List[float], List[float]]]) -> None: ...
    def precision(self, label: float | None = None) -> float:
        """
        Returns precision or precision for a given label (category) if specified.
        """
    def recall(self, label: float | None = None) -> float:
        """
        Returns recall or recall for a given label (category) if specified.
        """
    def f1Measure(self, label: float | None = None) -> float:
        """
        Returns f1Measure or f1Measure for a given label (category) if specified.
        """
    @property
    def microPrecision(self) -> float:
        """
        Returns micro-averaged label-based precision.
        (equals to micro-averaged document-based precision)
        """
    @property
    def microRecall(self) -> float:
        """
        Returns micro-averaged label-based recall.
        (equals to micro-averaged document-based recall)
        """
    @property
    def microF1Measure(self) -> float:
        """
        Returns micro-averaged label-based f1-measure.
        (equals to micro-averaged document-based f1-measure)
        """
    @property
    def hammingLoss(self) -> float:
        """
        Returns Hamming-loss.
        """
    @property
    def subsetAccuracy(self) -> float:
        """
        Returns subset accuracy.
        (for equal sets of labels)
        """
    @property
    def accuracy(self) -> float:
        """
        Returns accuracy.
        """
