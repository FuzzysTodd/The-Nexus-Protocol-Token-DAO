import numpy as np
from pyspark.ml._typing import M
from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.param.shared import HasAggregationDepth, HasCheckpointInterval, HasDistanceMeasure, HasFeaturesCol, HasMaxBlockSizeInMB, HasMaxIter, HasPredictionCol, HasProbabilityCol, HasSeed, HasSolver, HasTol, HasWeightCol, Param
from pyspark.ml.stat import MultivariateGaussian
from pyspark.ml.util import GeneralJavaMLWritable, HasTrainingSummary, JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaParams, JavaWrapper
from pyspark.sql import DataFrame
from typing import Any, List

__all__ = ['BisectingKMeans', 'BisectingKMeansModel', 'BisectingKMeansSummary', 'KMeans', 'KMeansModel', 'KMeansSummary', 'GaussianMixture', 'GaussianMixtureModel', 'GaussianMixtureSummary', 'LDA', 'LDAModel', 'LocalLDAModel', 'DistributedLDAModel', 'PowerIterationClustering']

class ClusteringSummary(JavaWrapper):
    """
    Clustering results for a given model.

    .. versionadded:: 2.1.0
    """
    @property
    def predictionCol(self) -> str:
        """
        Name for column of predicted clusters in `predictions`.
        """
    @property
    def predictions(self) -> DataFrame:
        """
        DataFrame produced by the model's `transform` method.
        """
    @property
    def featuresCol(self) -> str:
        """
        Name for column of features in `predictions`.
        """
    @property
    def k(self) -> int:
        """
        The number of clusters the model was trained with.
        """
    @property
    def cluster(self) -> DataFrame:
        """
        DataFrame of predicted cluster centers for each training data point.
        """
    @property
    def clusterSizes(self) -> List[int]:
        """
        Size of (number of data points in) each cluster.
        """
    @property
    def numIter(self) -> int:
        """
        Number of iterations.
        """

class _GaussianMixtureParams(HasMaxIter, HasFeaturesCol, HasSeed, HasPredictionCol, HasProbabilityCol, HasTol, HasAggregationDepth, HasWeightCol):
    """
    Params for :py:class:`GaussianMixture` and :py:class:`GaussianMixtureModel`.

    .. versionadded:: 3.0.0
    """
    k: Param[int]
    def __init__(self, *args: Any) -> None: ...
    def getK(self) -> int:
        """
        Gets the value of `k`
        """

class GaussianMixtureModel(JavaModel, _GaussianMixtureParams, JavaMLWritable, JavaMLReadable['GaussianMixtureModel'], HasTrainingSummary['GaussianMixtureSummary']):
    """
    Model fitted by GaussianMixture.

    .. versionadded:: 2.0.0
    """
    def setFeaturesCol(self, value: str) -> GaussianMixtureModel:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> GaussianMixtureModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setProbabilityCol(self, value: str) -> GaussianMixtureModel:
        """
        Sets the value of :py:attr:`probabilityCol`.
        """
    @property
    def weights(self) -> List[float]:
        """
        Weight for each Gaussian distribution in the mixture.
        This is a multinomial probability distribution over the k Gaussians,
        where weights[i] is the weight for Gaussian i, and weights sum to 1.
        """
    @property
    def gaussians(self) -> List[MultivariateGaussian]:
        """
        Array of :py:class:`MultivariateGaussian` where gaussians[i] represents
        the Multivariate Gaussian (Normal) Distribution for Gaussian i
        """
    @property
    def gaussiansDF(self) -> DataFrame:
        """
        Retrieve Gaussian distributions as a DataFrame.
        Each row represents a Gaussian Distribution.
        The DataFrame has two columns: mean (Vector) and cov (Matrix).
        """
    @property
    def summary(self) -> GaussianMixtureSummary:
        """
        Gets summary (cluster assignments, cluster sizes) of the model trained on the
        training set. An exception is thrown if no summary exists.
        """
    def predict(self, value: Vector) -> int:
        """
        Predict label for the given features.
        """
    def predictProbability(self, value: Vector) -> Vector:
        """
        Predict probability for the given features.
        """

class GaussianMixture(JavaEstimator[GaussianMixtureModel], _GaussianMixtureParams, JavaMLWritable, JavaMLReadable['GaussianMixture']):
    '''
    GaussianMixture clustering.
    This class performs expectation maximization for multivariate Gaussian
    Mixture Models (GMMs).  A GMM represents a composite distribution of
    independent Gaussian distributions with associated "mixing" weights
    specifying each\'s contribution to the composite.

    Given a set of sample points, this class will maximize the log-likelihood
    for a mixture of k Gaussians, iterating until the log-likelihood changes by
    less than convergenceTol, or until it has reached the max number of iterations.
    While this process is generally guaranteed to converge, it is not guaranteed
    to find a global optimum.

    .. versionadded:: 2.0.0

    Notes
    -----
    For high-dimensional data (with many features), this algorithm may perform poorly.
    This is due to high-dimensional data (a) making it difficult to cluster at all
    (based on statistical/theoretical arguments) and (b) numerical issues with
    Gaussian distributions.

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors

    >>> data = [(Vectors.dense([-0.1, -0.05 ]),),
    ...         (Vectors.dense([-0.01, -0.1]),),
    ...         (Vectors.dense([0.9, 0.8]),),
    ...         (Vectors.dense([0.75, 0.935]),),
    ...         (Vectors.dense([-0.83, -0.68]),),
    ...         (Vectors.dense([-0.91, -0.76]),)]
    >>> df = spark.createDataFrame(data, ["features"])
    >>> gm = GaussianMixture(k=3, tol=0.0001, seed=10)
    >>> gm.getMaxIter()
    100
    >>> gm.setMaxIter(30)
    GaussianMixture...
    >>> gm.getMaxIter()
    30
    >>> model = gm.fit(df)
    >>> model.getAggregationDepth()
    2
    >>> model.getFeaturesCol()
    \'features\'
    >>> model.setPredictionCol("newPrediction")
    GaussianMixtureModel...
    >>> model.predict(df.head().features)
    2
    >>> model.predictProbability(df.head().features)
    DenseVector([0.0, 0.0, 1.0])
    >>> model.hasSummary
    True
    >>> summary = model.summary
    >>> summary.k
    3
    >>> summary.clusterSizes
    [2, 2, 2]
    >>> weights = model.weights
    >>> len(weights)
    3
    >>> gaussians = model.gaussians
    >>> len(gaussians)
    3
    >>> gaussians[0].mean
    DenseVector([0.825, 0.8675])
    >>> gaussians[0].cov
    DenseMatrix(2, 2, [0.0056, -0.0051, -0.0051, 0.0046], 0)
    >>> gaussians[1].mean
    DenseVector([-0.87, -0.72])
    >>> gaussians[1].cov
    DenseMatrix(2, 2, [0.0016, 0.0016, 0.0016, 0.0016], 0)
    >>> gaussians[2].mean
    DenseVector([-0.055, -0.075])
    >>> gaussians[2].cov
    DenseMatrix(2, 2, [0.002, -0.0011, -0.0011, 0.0006], 0)
    >>> model.gaussiansDF.select("mean").head()
    Row(mean=DenseVector([0.825, 0.8675]))
    >>> model.gaussiansDF.select("cov").head()
    Row(cov=DenseMatrix(2, 2, [0.0056, -0.0051, -0.0051, 0.0046], False))
    >>> transformed = model.transform(df).select("features", "newPrediction")
    >>> rows = transformed.collect()
    >>> rows[4].newPrediction == rows[5].newPrediction
    True
    >>> rows[2].newPrediction == rows[3].newPrediction
    True
    >>> gmm_path = temp_path + "/gmm"
    >>> gm.save(gmm_path)
    >>> gm2 = GaussianMixture.load(gmm_path)
    >>> gm2.getK()
    3
    >>> model_path = temp_path + "/gmm_model"
    >>> model.save(model_path)
    >>> model2 = GaussianMixtureModel.load(model_path)
    >>> model2.hasSummary
    False
    >>> model2.weights == model.weights
    True
    >>> model2.gaussians[0].mean == model.gaussians[0].mean
    True
    >>> model2.gaussians[0].cov == model.gaussians[0].cov
    True
    >>> model2.gaussians[1].mean == model.gaussians[1].mean
    True
    >>> model2.gaussians[1].cov == model.gaussians[1].cov
    True
    >>> model2.gaussians[2].mean == model.gaussians[2].mean
    True
    >>> model2.gaussians[2].cov == model.gaussians[2].cov
    True
    >>> model2.gaussiansDF.select("mean").head()
    Row(mean=DenseVector([0.825, 0.8675]))
    >>> model2.gaussiansDF.select("cov").head()
    Row(cov=DenseMatrix(2, 2, [0.0056, -0.0051, -0.0051, 0.0046], False))
    >>> model.transform(df).take(1) == model2.transform(df).take(1)
    True
    >>> gm2.setWeightCol("weight")
    GaussianMixture...
    '''
    def __init__(self, *, featuresCol: str = 'features', predictionCol: str = 'prediction', k: int = 2, probabilityCol: str = 'probability', tol: float = 0.01, maxIter: int = 100, seed: int | None = None, aggregationDepth: int = 2, weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", predictionCol="prediction", k=2,                  probabilityCol="probability", tol=0.01, maxIter=100, seed=None,                  aggregationDepth=2, weightCol=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', predictionCol: str = 'prediction', k: int = 2, probabilityCol: str = 'probability', tol: float = 0.01, maxIter: int = 100, seed: int | None = None, aggregationDepth: int = 2, weightCol: str | None = None) -> GaussianMixture:
        '''
        setParams(self, \\*, featuresCol="features", predictionCol="prediction", k=2,                   probabilityCol="probability", tol=0.01, maxIter=100, seed=None,                   aggregationDepth=2, weightCol=None)

        Sets params for GaussianMixture.
        '''
    def setK(self, value: int) -> GaussianMixture:
        """
        Sets the value of :py:attr:`k`.
        """
    def setMaxIter(self, value: int) -> GaussianMixture:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setFeaturesCol(self, value: str) -> GaussianMixture:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> GaussianMixture:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setProbabilityCol(self, value: str) -> GaussianMixture:
        """
        Sets the value of :py:attr:`probabilityCol`.
        """
    def setWeightCol(self, value: str) -> GaussianMixture:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setSeed(self, value: int) -> GaussianMixture:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setTol(self, value: float) -> GaussianMixture:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setAggregationDepth(self, value: int) -> GaussianMixture:
        """
        Sets the value of :py:attr:`aggregationDepth`.
        """

class GaussianMixtureSummary(ClusteringSummary):
    """
    Gaussian mixture clustering results for a given model.

    .. versionadded:: 2.1.0
    """
    @property
    def probabilityCol(self) -> str:
        """
        Name for column of predicted probability of each cluster in `predictions`.
        """
    @property
    def probability(self) -> DataFrame:
        """
        DataFrame of probabilities of each cluster for each training data point.
        """
    @property
    def logLikelihood(self) -> float:
        """
        Total log-likelihood for this model on the given data.
        """

class KMeansSummary(ClusteringSummary):
    """
    Summary of KMeans.

    .. versionadded:: 2.1.0
    """
    @property
    def trainingCost(self) -> float:
        """
        K-means cost (sum of squared distances to the nearest centroid for all points in the
        training dataset). This is equivalent to sklearn's inertia.
        """

class _KMeansParams(HasMaxIter, HasFeaturesCol, HasSeed, HasPredictionCol, HasTol, HasDistanceMeasure, HasWeightCol, HasSolver, HasMaxBlockSizeInMB):
    """
    Params for :py:class:`KMeans` and :py:class:`KMeansModel`.

    .. versionadded:: 3.0.0
    """
    k: Param[int]
    initMode: Param[str]
    initSteps: Param[int]
    solver: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getK(self) -> int:
        """
        Gets the value of `k`
        """
    def getInitMode(self) -> str:
        """
        Gets the value of `initMode`
        """
    def getInitSteps(self) -> int:
        """
        Gets the value of `initSteps`
        """

class KMeansModel(JavaModel, _KMeansParams, GeneralJavaMLWritable, JavaMLReadable['KMeansModel'], HasTrainingSummary['KMeansSummary']):
    """
    Model fitted by KMeans.

    .. versionadded:: 1.5.0
    """
    def setFeaturesCol(self, value: str) -> KMeansModel:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> KMeansModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def clusterCenters(self) -> List[np.ndarray]:
        """Get the cluster centers, represented as a list of NumPy arrays."""
    @property
    def summary(self) -> KMeansSummary:
        """
        Gets summary (cluster assignments, cluster sizes) of the model trained on the
        training set. An exception is thrown if no summary exists.
        """
    def predict(self, value: Vector) -> int:
        """
        Predict label for the given features.
        """

class KMeans(JavaEstimator[KMeansModel], _KMeansParams, JavaMLWritable, JavaMLReadable['KMeans']):
    '''
    K-means clustering with a k-means++ like initialization mode
    (the k-means|| algorithm by Bahmani et al).

    .. versionadded:: 1.5.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> data = [(Vectors.dense([0.0, 0.0]), 2.0), (Vectors.dense([1.0, 1.0]), 2.0),
    ...         (Vectors.dense([9.0, 8.0]), 2.0), (Vectors.dense([8.0, 9.0]), 2.0)]
    >>> df = spark.createDataFrame(data, ["features", "weighCol"])
    >>> kmeans = KMeans(k=2)
    >>> kmeans.setSeed(1)
    KMeans...
    >>> kmeans.setWeightCol("weighCol")
    KMeans...
    >>> kmeans.setMaxIter(10)
    KMeans...
    >>> kmeans.getMaxIter()
    10
    >>> kmeans.clear(kmeans.maxIter)
    >>> kmeans.getSolver()
    \'auto\'
    >>> model = kmeans.fit(df)
    >>> model.getMaxBlockSizeInMB()
    0.0
    >>> model.getDistanceMeasure()
    \'euclidean\'
    >>> model.setPredictionCol("newPrediction")
    KMeansModel...
    >>> model.predict(df.head().features)
    0
    >>> centers = model.clusterCenters()
    >>> len(centers)
    2
    >>> transformed = model.transform(df).select("features", "newPrediction")
    >>> rows = transformed.collect()
    >>> rows[0].newPrediction == rows[1].newPrediction
    True
    >>> rows[2].newPrediction == rows[3].newPrediction
    True
    >>> model.hasSummary
    True
    >>> summary = model.summary
    >>> summary.k
    2
    >>> summary.clusterSizes
    [2, 2]
    >>> summary.trainingCost
    4.0
    >>> kmeans_path = temp_path + "/kmeans"
    >>> kmeans.save(kmeans_path)
    >>> kmeans2 = KMeans.load(kmeans_path)
    >>> kmeans2.getK()
    2
    >>> model_path = temp_path + "/kmeans_model"
    >>> model.save(model_path)
    >>> model2 = KMeansModel.load(model_path)
    >>> model2.hasSummary
    False
    >>> model.clusterCenters()[0] == model2.clusterCenters()[0]
    array([ True,  True], dtype=bool)
    >>> model.clusterCenters()[1] == model2.clusterCenters()[1]
    array([ True,  True], dtype=bool)
    >>> model.transform(df).take(1) == model2.transform(df).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', predictionCol: str = 'prediction', k: int = 2, initMode: str = 'k-means||', initSteps: int = 2, tol: float = 0.0001, maxIter: int = 20, seed: int | None = None, distanceMeasure: str = 'euclidean', weightCol: str | None = None, solver: str = 'auto', maxBlockSizeInMB: float = 0.0) -> None:
        '''
        __init__(self, \\*, featuresCol="features", predictionCol="prediction", k=2,                  initMode="k-means||", initSteps=2, tol=1e-4, maxIter=20, seed=None,                  distanceMeasure="euclidean", weightCol=None, solver="auto",                  maxBlockSizeInMB=0.0)
        '''
    def setParams(self, *, featuresCol: str = 'features', predictionCol: str = 'prediction', k: int = 2, initMode: str = 'k-means||', initSteps: int = 2, tol: float = 0.0001, maxIter: int = 20, seed: int | None = None, distanceMeasure: str = 'euclidean', weightCol: str | None = None, solver: str = 'auto', maxBlockSizeInMB: float = 0.0) -> KMeans:
        '''
        setParams(self, \\*, featuresCol="features", predictionCol="prediction", k=2,                   initMode="k-means||", initSteps=2, tol=1e-4, maxIter=20, seed=None,                   distanceMeasure="euclidean", weightCol=None, solver="auto",                   maxBlockSizeInMB=0.0)

        Sets params for KMeans.
        '''
    def setK(self, value: int) -> KMeans:
        """
        Sets the value of :py:attr:`k`.
        """
    def setInitMode(self, value: str) -> KMeans:
        """
        Sets the value of :py:attr:`initMode`.
        """
    def setInitSteps(self, value: int) -> KMeans:
        """
        Sets the value of :py:attr:`initSteps`.
        """
    def setDistanceMeasure(self, value: str) -> KMeans:
        """
        Sets the value of :py:attr:`distanceMeasure`.
        """
    def setMaxIter(self, value: int) -> KMeans:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setFeaturesCol(self, value: str) -> KMeans:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> KMeans:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setSeed(self, value: int) -> KMeans:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setTol(self, value: float) -> KMeans:
        """
        Sets the value of :py:attr:`tol`.
        """
    def setWeightCol(self, value: str) -> KMeans:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def setSolver(self, value: str) -> KMeans:
        """
        Sets the value of :py:attr:`solver`.
        """
    def setMaxBlockSizeInMB(self, value: float) -> KMeans:
        """
        Sets the value of :py:attr:`maxBlockSizeInMB`.
        """

class _BisectingKMeansParams(HasMaxIter, HasFeaturesCol, HasSeed, HasPredictionCol, HasDistanceMeasure, HasWeightCol):
    """
    Params for :py:class:`BisectingKMeans` and :py:class:`BisectingKMeansModel`.

    .. versionadded:: 3.0.0
    """
    k: Param[int]
    minDivisibleClusterSize: Param[float]
    def __init__(self, *args: Any) -> None: ...
    def getK(self) -> int:
        """
        Gets the value of `k` or its default value.
        """
    def getMinDivisibleClusterSize(self) -> float:
        """
        Gets the value of `minDivisibleClusterSize` or its default value.
        """

class BisectingKMeansModel(JavaModel, _BisectingKMeansParams, JavaMLWritable, JavaMLReadable['BisectingKMeansModel'], HasTrainingSummary['BisectingKMeansSummary']):
    """
    Model fitted by BisectingKMeans.

    .. versionadded:: 2.0.0
    """
    def setFeaturesCol(self, value: str) -> BisectingKMeansModel:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> BisectingKMeansModel:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def clusterCenters(self) -> List[np.ndarray]:
        """Get the cluster centers, represented as a list of NumPy arrays."""
    def computeCost(self, dataset: DataFrame) -> float:
        """
        Computes the sum of squared distances between the input points
        and their corresponding cluster centers.

        .. deprecated:: 3.0.0
            It will be removed in future versions. Use :py:class:`ClusteringEvaluator` instead.
            You can also get the cost on the training dataset in the summary.
        """
    @property
    def summary(self) -> BisectingKMeansSummary:
        """
        Gets summary (cluster assignments, cluster sizes) of the model trained on the
        training set. An exception is thrown if no summary exists.
        """
    def predict(self, value: Vector) -> int:
        """
        Predict label for the given features.
        """

class BisectingKMeans(JavaEstimator[BisectingKMeansModel], _BisectingKMeansParams, JavaMLWritable, JavaMLReadable['BisectingKMeans']):
    '''
    A bisecting k-means algorithm based on the paper "A comparison of document clustering
    techniques" by Steinbach, Karypis, and Kumar, with modification to fit Spark.
    The algorithm starts from a single cluster that contains all points.
    Iteratively it finds divisible clusters on the bottom level and bisects each of them using
    k-means, until there are `k` leaf clusters in total or no leaf clusters are divisible.
    The bisecting steps of clusters on the same level are grouped together to increase parallelism.
    If bisecting all divisible clusters on the bottom level would result more than `k` leaf
    clusters, larger clusters get higher priority.

    .. versionadded:: 2.0.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors
    >>> data = [(Vectors.dense([0.0, 0.0]), 2.0), (Vectors.dense([1.0, 1.0]), 2.0),
    ...         (Vectors.dense([9.0, 8.0]), 2.0), (Vectors.dense([8.0, 9.0]), 2.0)]
    >>> df = spark.createDataFrame(data, ["features", "weighCol"])
    >>> bkm = BisectingKMeans(k=2, minDivisibleClusterSize=1.0)
    >>> bkm.setMaxIter(10)
    BisectingKMeans...
    >>> bkm.getMaxIter()
    10
    >>> bkm.clear(bkm.maxIter)
    >>> bkm.setSeed(1)
    BisectingKMeans...
    >>> bkm.setWeightCol("weighCol")
    BisectingKMeans...
    >>> bkm.getSeed()
    1
    >>> bkm.clear(bkm.seed)
    >>> model = bkm.fit(df)
    >>> model.getMaxIter()
    20
    >>> model.setPredictionCol("newPrediction")
    BisectingKMeansModel...
    >>> model.predict(df.head().features)
    0
    >>> centers = model.clusterCenters()
    >>> len(centers)
    2
    >>> model.computeCost(df)
    2.0
    >>> model.hasSummary
    True
    >>> summary = model.summary
    >>> summary.k
    2
    >>> summary.clusterSizes
    [2, 2]
    >>> summary.trainingCost
    4.000...
    >>> transformed = model.transform(df).select("features", "newPrediction")
    >>> rows = transformed.collect()
    >>> rows[0].newPrediction == rows[1].newPrediction
    True
    >>> rows[2].newPrediction == rows[3].newPrediction
    True
    >>> bkm_path = temp_path + "/bkm"
    >>> bkm.save(bkm_path)
    >>> bkm2 = BisectingKMeans.load(bkm_path)
    >>> bkm2.getK()
    2
    >>> bkm2.getDistanceMeasure()
    \'euclidean\'
    >>> model_path = temp_path + "/bkm_model"
    >>> model.save(model_path)
    >>> model2 = BisectingKMeansModel.load(model_path)
    >>> model2.hasSummary
    False
    >>> model.clusterCenters()[0] == model2.clusterCenters()[0]
    array([ True,  True], dtype=bool)
    >>> model.clusterCenters()[1] == model2.clusterCenters()[1]
    array([ True,  True], dtype=bool)
    >>> model.transform(df).take(1) == model2.transform(df).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', predictionCol: str = 'prediction', maxIter: int = 20, seed: int | None = None, k: int = 4, minDivisibleClusterSize: float = 1.0, distanceMeasure: str = 'euclidean', weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, featuresCol="features", predictionCol="prediction", maxIter=20,                  seed=None, k=4, minDivisibleClusterSize=1.0, distanceMeasure="euclidean",                  weightCol=None)
        '''
    def setParams(self, *, featuresCol: str = 'features', predictionCol: str = 'prediction', maxIter: int = 20, seed: int | None = None, k: int = 4, minDivisibleClusterSize: float = 1.0, distanceMeasure: str = 'euclidean', weightCol: str | None = None) -> BisectingKMeans:
        '''
        setParams(self, \\*, featuresCol="features", predictionCol="prediction", maxIter=20,                   seed=None, k=4, minDivisibleClusterSize=1.0, distanceMeasure="euclidean",                   weightCol=None)
        Sets params for BisectingKMeans.
        '''
    def setK(self, value: int) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`k`.
        """
    def setMinDivisibleClusterSize(self, value: float) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`minDivisibleClusterSize`.
        """
    def setDistanceMeasure(self, value: str) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`distanceMeasure`.
        """
    def setMaxIter(self, value: int) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setFeaturesCol(self, value: str) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setPredictionCol(self, value: str) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`predictionCol`.
        """
    def setSeed(self, value: int) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setWeightCol(self, value: str) -> BisectingKMeans:
        """
        Sets the value of :py:attr:`weightCol`.
        """

class BisectingKMeansSummary(ClusteringSummary):
    """
    Bisecting KMeans clustering results for a given model.

    .. versionadded:: 2.1.0
    """
    @property
    def trainingCost(self) -> float:
        """
        Sum of squared distances to the nearest centroid for all points in the training dataset.
        This is equivalent to sklearn's inertia.
        """

class _LDAParams(HasMaxIter, HasFeaturesCol, HasSeed, HasCheckpointInterval):
    """
    Params for :py:class:`LDA` and :py:class:`LDAModel`.

    .. versionadded:: 3.0.0
    """
    k: Param[int]
    optimizer: Param[str]
    learningOffset: Param[float]
    learningDecay: Param[float]
    subsamplingRate: Param[float]
    optimizeDocConcentration: Param[bool]
    docConcentration: Param[List[float]]
    topicConcentration: Param[float]
    topicDistributionCol: Param[str]
    keepLastCheckpoint: Param[bool]
    def __init__(self, *args: Any) -> None: ...
    def getK(self) -> int:
        """
        Gets the value of :py:attr:`k` or its default value.
        """
    def getOptimizer(self) -> str:
        """
        Gets the value of :py:attr:`optimizer` or its default value.
        """
    def getLearningOffset(self) -> float:
        """
        Gets the value of :py:attr:`learningOffset` or its default value.
        """
    def getLearningDecay(self) -> float:
        """
        Gets the value of :py:attr:`learningDecay` or its default value.
        """
    def getSubsamplingRate(self) -> float:
        """
        Gets the value of :py:attr:`subsamplingRate` or its default value.
        """
    def getOptimizeDocConcentration(self) -> bool:
        """
        Gets the value of :py:attr:`optimizeDocConcentration` or its default value.
        """
    def getDocConcentration(self) -> List[float]:
        """
        Gets the value of :py:attr:`docConcentration` or its default value.
        """
    def getTopicConcentration(self) -> float:
        """
        Gets the value of :py:attr:`topicConcentration` or its default value.
        """
    def getTopicDistributionCol(self) -> str:
        """
        Gets the value of :py:attr:`topicDistributionCol` or its default value.
        """
    def getKeepLastCheckpoint(self) -> bool:
        """
        Gets the value of :py:attr:`keepLastCheckpoint` or its default value.
        """

class LDAModel(JavaModel, _LDAParams):
    """
    Latent Dirichlet Allocation (LDA) model.
    This abstraction permits for different underlying representations,
    including local and distributed data structures.

    .. versionadded:: 2.0.0
    """
    def setFeaturesCol(self, value: str) -> M:
        """
        Sets the value of :py:attr:`featuresCol`.
        """
    def setSeed(self, value: int) -> M:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setTopicDistributionCol(self, value: str) -> M:
        """
        Sets the value of :py:attr:`topicDistributionCol`.
        """
    def isDistributed(self) -> bool:
        """
        Indicates whether this instance is of type DistributedLDAModel
        """
    def vocabSize(self) -> int:
        """Vocabulary size (number of terms or words in the vocabulary)"""
    def topicsMatrix(self) -> Matrix:
        '''
        Inferred topics, where each topic is represented by a distribution over terms.
        This is a matrix of size vocabSize x k, where each column is a topic.
        No guarantees are given about the ordering of the topics.

        .. warning:: If this model is actually a :py:class:`DistributedLDAModel`
            instance produced by the Expectation-Maximization ("em") `optimizer`,
            then this method could involve collecting a large amount of data
            to the driver (on the order of vocabSize x k).
        '''
    def logLikelihood(self, dataset: DataFrame) -> float:
        '''
        Calculates a lower bound on the log likelihood of the entire corpus.
        See Equation (16) in the Online LDA paper (Hoffman et al., 2010).

        .. warning:: If this model is an instance of :py:class:`DistributedLDAModel` (produced when
            :py:attr:`optimizer` is set to "em"), this involves collecting a large
            :py:func:`topicsMatrix` to the driver. This implementation may be changed in the future.
        '''
    def logPerplexity(self, dataset: DataFrame) -> float:
        '''
        Calculate an upper bound on perplexity.  (Lower is better.)
        See Equation (16) in the Online LDA paper (Hoffman et al., 2010).

        .. warning:: If this model is an instance of :py:class:`DistributedLDAModel` (produced when
            :py:attr:`optimizer` is set to "em"), this involves collecting a large
            :py:func:`topicsMatrix` to the driver. This implementation may be changed in the future.
        '''
    def describeTopics(self, maxTermsPerTopic: int = 10) -> DataFrame:
        """
        Return the topics described by their top-weighted terms.
        """
    def estimatedDocConcentration(self) -> Vector:
        """
        Value for :py:attr:`LDA.docConcentration` estimated from data.
        If Online LDA was used and :py:attr:`LDA.optimizeDocConcentration` was set to false,
        then this returns the fixed (given) value for the :py:attr:`LDA.docConcentration` parameter.
        """

class DistributedLDAModel(LDAModel, JavaMLReadable['DistributedLDAModel'], JavaMLWritable):
    """
    Distributed model fitted by :py:class:`LDA`.
    This type of model is currently only produced by Expectation-Maximization (EM).

    This model stores the inferred topics, the full training dataset, and the topic distribution
    for each training document.

    .. versionadded:: 2.0.0
    """
    def toLocal(self) -> LocalLDAModel:
        """
        Convert this distributed model to a local representation.  This discards info about the
        training dataset.

        .. warning:: This involves collecting a large :py:func:`topicsMatrix` to the driver.
        """
    def trainingLogLikelihood(self) -> float:
        """
        Log likelihood of the observed tokens in the training set,
        given the current parameter estimates:
        log P(docs | topics, topic distributions for docs, Dirichlet hyperparameters)

        Notes
        -----
        - This excludes the prior; for that, use :py:func:`logPrior`.
        - Even with :py:func:`logPrior`, this is NOT the same as the data log likelihood given
            the hyperparameters.
        - This is computed from the topic distributions computed during training. If you call
            :py:func:`logLikelihood` on the same training dataset, the topic distributions
            will be computed again, possibly giving different results.
        """
    def logPrior(self) -> float:
        """
        Log probability of the current parameter estimate:
        log P(topics, topic distributions for docs | alpha, eta)
        """
    def getCheckpointFiles(self) -> List[str]:
        """
        If using checkpointing and :py:attr:`LDA.keepLastCheckpoint` is set to true, then there may
        be saved checkpoint files.  This method is provided so that users can manage those files.

        .. versionadded:: 2.0.0

        Returns
        -------
        list
            List of checkpoint files from training

        Notes
        -----
        Removing the checkpoints can cause failures if a partition is lost and is needed
        by certain :py:class:`DistributedLDAModel` methods.  Reference counting will clean up
        the checkpoints when this model and derivative data go out of scope.
        """

class LocalLDAModel(LDAModel, JavaMLReadable['LocalLDAModel'], JavaMLWritable):
    """
    Local (non-distributed) model fitted by :py:class:`LDA`.
    This model stores the inferred topics only; it does not store info about the training dataset.

    .. versionadded:: 2.0.0
    """

class LDA(JavaEstimator[LDAModel], _LDAParams, JavaMLReadable['LDA'], JavaMLWritable):
    '''
    Latent Dirichlet Allocation (LDA), a topic model designed for text documents.

    Terminology:

     - "term" = "word": an element of the vocabulary
     - "token": instance of a term appearing in a document
     - "topic": multinomial distribution over terms representing some concept
     - "document": one piece of text, corresponding to one row in the input data

    Original LDA paper (journal version):
      Blei, Ng, and Jordan.  "Latent Dirichlet Allocation."  JMLR, 2003.

    Input data (featuresCol):
    LDA is given a collection of documents as input data, via the featuresCol parameter.
    Each document is specified as a :py:class:`Vector` of length vocabSize, where each entry is the
    count for the corresponding term (word) in the document.  Feature transformers such as
    :py:class:`pyspark.ml.feature.Tokenizer` and :py:class:`pyspark.ml.feature.CountVectorizer`
    can be useful for converting text to word count vectors.

    .. versionadded:: 2.0.0

    Examples
    --------
    >>> from pyspark.ml.linalg import Vectors, SparseVector
    >>> from pyspark.ml.clustering import LDA
    >>> df = spark.createDataFrame([[1, Vectors.dense([0.0, 1.0])],
    ...      [2, SparseVector(2, {0: 1.0})],], ["id", "features"])
    >>> lda = LDA(k=2, seed=1, optimizer="em")
    >>> lda.setMaxIter(10)
    LDA...
    >>> lda.getMaxIter()
    10
    >>> lda.clear(lda.maxIter)
    >>> model = lda.fit(df)
    >>> model.setSeed(1)
    DistributedLDAModel...
    >>> model.getTopicDistributionCol()
    \'topicDistribution\'
    >>> model.isDistributed()
    True
    >>> localModel = model.toLocal()
    >>> localModel.isDistributed()
    False
    >>> model.vocabSize()
    2
    >>> model.describeTopics().show()
    +-----+-----------+--------------------+
    |topic|termIndices|         termWeights|
    +-----+-----------+--------------------+
    |    0|     [1, 0]|[0.50401530077160...|
    |    1|     [0, 1]|[0.50401530077160...|
    +-----+-----------+--------------------+
    ...
    >>> model.topicsMatrix()
    DenseMatrix(2, 2, [0.496, 0.504, 0.504, 0.496], 0)
    >>> lda_path = temp_path + "/lda"
    >>> lda.save(lda_path)
    >>> sameLDA = LDA.load(lda_path)
    >>> distributed_model_path = temp_path + "/lda_distributed_model"
    >>> model.save(distributed_model_path)
    >>> sameModel = DistributedLDAModel.load(distributed_model_path)
    >>> local_model_path = temp_path + "/lda_local_model"
    >>> localModel.save(local_model_path)
    >>> sameLocalModel = LocalLDAModel.load(local_model_path)
    >>> model.transform(df).take(1) == sameLocalModel.transform(df).take(1)
    True
    '''
    def __init__(self, *, featuresCol: str = 'features', maxIter: int = 20, seed: int | None = None, checkpointInterval: int = 10, k: int = 10, optimizer: str = 'online', learningOffset: float = 1024.0, learningDecay: float = 0.51, subsamplingRate: float = 0.05, optimizeDocConcentration: bool = True, docConcentration: List[float] | None = None, topicConcentration: float | None = None, topicDistributionCol: str = 'topicDistribution', keepLastCheckpoint: bool = True) -> None:
        '''
        __init__(self, \\*, featuresCol="features", maxIter=20, seed=None, checkpointInterval=10,                  k=10, optimizer="online", learningOffset=1024.0, learningDecay=0.51,                  subsamplingRate=0.05, optimizeDocConcentration=True,                  docConcentration=None, topicConcentration=None,                  topicDistributionCol="topicDistribution", keepLastCheckpoint=True)
        '''
    def setParams(self, *, featuresCol: str = 'features', maxIter: int = 20, seed: int | None = None, checkpointInterval: int = 10, k: int = 10, optimizer: str = 'online', learningOffset: float = 1024.0, learningDecay: float = 0.51, subsamplingRate: float = 0.05, optimizeDocConcentration: bool = True, docConcentration: List[float] | None = None, topicConcentration: float | None = None, topicDistributionCol: str = 'topicDistribution', keepLastCheckpoint: bool = True) -> LDA:
        '''
        setParams(self, \\*, featuresCol="features", maxIter=20, seed=None, checkpointInterval=10,                  k=10, optimizer="online", learningOffset=1024.0, learningDecay=0.51,                  subsamplingRate=0.05, optimizeDocConcentration=True,                  docConcentration=None, topicConcentration=None,                  topicDistributionCol="topicDistribution", keepLastCheckpoint=True)

        Sets params for LDA.
        '''
    def setCheckpointInterval(self, value: int) -> LDA:
        """
        Sets the value of :py:attr:`checkpointInterval`.
        """
    def setSeed(self, value: int) -> LDA:
        """
        Sets the value of :py:attr:`seed`.
        """
    def setK(self, value: int) -> LDA:
        """
        Sets the value of :py:attr:`k`.

        >>> algo = LDA().setK(10)
        >>> algo.getK()
        10
        """
    def setOptimizer(self, value: str) -> LDA:
        '''
        Sets the value of :py:attr:`optimizer`.
        Currently only support \'em\' and \'online\'.

        Examples
        --------
        >>> algo = LDA().setOptimizer("em")
        >>> algo.getOptimizer()
        \'em\'
        '''
    def setLearningOffset(self, value: float) -> LDA:
        """
        Sets the value of :py:attr:`learningOffset`.

        Examples
        --------
        >>> algo = LDA().setLearningOffset(100)
        >>> algo.getLearningOffset()
        100.0
        """
    def setLearningDecay(self, value: float) -> LDA:
        """
        Sets the value of :py:attr:`learningDecay`.

        Examples
        --------
        >>> algo = LDA().setLearningDecay(0.1)
        >>> algo.getLearningDecay()
        0.1...
        """
    def setSubsamplingRate(self, value: float) -> LDA:
        """
        Sets the value of :py:attr:`subsamplingRate`.

        Examples
        --------
        >>> algo = LDA().setSubsamplingRate(0.1)
        >>> algo.getSubsamplingRate()
        0.1...
        """
    def setOptimizeDocConcentration(self, value: bool) -> LDA:
        """
        Sets the value of :py:attr:`optimizeDocConcentration`.

        Examples
        --------
        >>> algo = LDA().setOptimizeDocConcentration(True)
        >>> algo.getOptimizeDocConcentration()
        True
        """
    def setDocConcentration(self, value: List[float]) -> LDA:
        """
        Sets the value of :py:attr:`docConcentration`.

        Examples
        --------
        >>> algo = LDA().setDocConcentration([0.1, 0.2])
        >>> algo.getDocConcentration()
        [0.1..., 0.2...]
        """
    def setTopicConcentration(self, value: float) -> LDA:
        """
        Sets the value of :py:attr:`topicConcentration`.

        Examples
        --------
        >>> algo = LDA().setTopicConcentration(0.5)
        >>> algo.getTopicConcentration()
        0.5...
        """
    def setTopicDistributionCol(self, value: str) -> LDA:
        '''
        Sets the value of :py:attr:`topicDistributionCol`.

        Examples
        --------
        >>> algo = LDA().setTopicDistributionCol("topicDistributionCol")
        >>> algo.getTopicDistributionCol()
        \'topicDistributionCol\'
        '''
    def setKeepLastCheckpoint(self, value: bool) -> LDA:
        """
        Sets the value of :py:attr:`keepLastCheckpoint`.

        Examples
        --------
        >>> algo = LDA().setKeepLastCheckpoint(False)
        >>> algo.getKeepLastCheckpoint()
        False
        """
    def setMaxIter(self, value: int) -> LDA:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setFeaturesCol(self, value: str) -> LDA:
        """
        Sets the value of :py:attr:`featuresCol`.
        """

class _PowerIterationClusteringParams(HasMaxIter, HasWeightCol):
    """
    Params for :py:class:`PowerIterationClustering`.

    .. versionadded:: 3.0.0
    """
    k: Param[int]
    initMode: Param[str]
    srcCol: Param[str]
    dstCol: Param[str]
    def __init__(self, *args: Any) -> None: ...
    def getK(self) -> int:
        """
        Gets the value of :py:attr:`k` or its default value.
        """
    def getInitMode(self) -> str:
        """
        Gets the value of :py:attr:`initMode` or its default value.
        """
    def getSrcCol(self) -> str:
        """
        Gets the value of :py:attr:`srcCol` or its default value.
        """
    def getDstCol(self) -> str:
        """
        Gets the value of :py:attr:`dstCol` or its default value.
        """

class PowerIterationClustering(_PowerIterationClusteringParams, JavaParams, JavaMLReadable['PowerIterationClustering'], JavaMLWritable):
    '''
    Power Iteration Clustering (PIC), a scalable graph clustering algorithm developed by
    `Lin and Cohen <http://www.cs.cmu.edu/~frank/papers/icml2010-pic-final.pdf>`_. From the
    abstract: PIC finds a very low-dimensional embedding of a dataset using truncated power
    iteration on a normalized pair-wise similarity matrix of the data.

    This class is not yet an Estimator/Transformer, use :py:func:`assignClusters` method
    to run the PowerIterationClustering algorithm.

    .. versionadded:: 2.4.0

    Notes
    -----
    See `Wikipedia on Spectral clustering <http://en.wikipedia.org/wiki/Spectral_clustering>`_

    Examples
    --------
    >>> data = [(1, 0, 0.5),
    ...         (2, 0, 0.5), (2, 1, 0.7),
    ...         (3, 0, 0.5), (3, 1, 0.7), (3, 2, 0.9),
    ...         (4, 0, 0.5), (4, 1, 0.7), (4, 2, 0.9), (4, 3, 1.1),
    ...         (5, 0, 0.5), (5, 1, 0.7), (5, 2, 0.9), (5, 3, 1.1), (5, 4, 1.3)]
    >>> df = spark.createDataFrame(data).toDF("src", "dst", "weight").repartition(1)
    >>> pic = PowerIterationClustering(k=2, weightCol="weight")
    >>> pic.setMaxIter(40)
    PowerIterationClustering...
    >>> assignments = pic.assignClusters(df)
    >>> assignments.sort(assignments.id).show(truncate=False)
    +---+-------+
    |id |cluster|
    +---+-------+
    |0  |0      |
    |1  |0      |
    |2  |0      |
    |3  |0      |
    |4  |0      |
    |5  |1      |
    +---+-------+
    ...
    >>> pic_path = temp_path + "/pic"
    >>> pic.save(pic_path)
    >>> pic2 = PowerIterationClustering.load(pic_path)
    >>> pic2.getK()
    2
    >>> pic2.getMaxIter()
    40
    >>> pic2.assignClusters(df).take(6) == assignments.take(6)
    True
    '''
    def __init__(self, *, k: int = 2, maxIter: int = 20, initMode: str = 'random', srcCol: str = 'src', dstCol: str = 'dst', weightCol: str | None = None) -> None:
        '''
        __init__(self, \\*, k=2, maxIter=20, initMode="random", srcCol="src", dstCol="dst",                 weightCol=None)
        '''
    def setParams(self, *, k: int = 2, maxIter: int = 20, initMode: str = 'random', srcCol: str = 'src', dstCol: str = 'dst', weightCol: str | None = None) -> PowerIterationClustering:
        '''
        setParams(self, \\*, k=2, maxIter=20, initMode="random", srcCol="src", dstCol="dst",                  weightCol=None)
        Sets params for PowerIterationClustering.
        '''
    def setK(self, value: int) -> PowerIterationClustering:
        """
        Sets the value of :py:attr:`k`.
        """
    def setInitMode(self, value: str) -> PowerIterationClustering:
        """
        Sets the value of :py:attr:`initMode`.
        """
    def setSrcCol(self, value: str) -> PowerIterationClustering:
        """
        Sets the value of :py:attr:`srcCol`.
        """
    def setDstCol(self, value: str) -> PowerIterationClustering:
        """
        Sets the value of :py:attr:`dstCol`.
        """
    def setMaxIter(self, value: int) -> PowerIterationClustering:
        """
        Sets the value of :py:attr:`maxIter`.
        """
    def setWeightCol(self, value: str) -> PowerIterationClustering:
        """
        Sets the value of :py:attr:`weightCol`.
        """
    def assignClusters(self, dataset: DataFrame) -> DataFrame:
        """
        Run the PIC algorithm and returns a cluster assignment for each input vertex.

        Parameters
        ----------
        dataset : :py:class:`pyspark.sql.DataFrame`
          A dataset with columns src, dst, weight representing the affinity matrix,
          which is the matrix A in the PIC paper. Suppose the src column value is i,
          the dst column value is j, the weight column value is similarity s,,ij,,
          which must be nonnegative. This is a symmetric matrix and hence
          s,,ij,, = s,,ji,,. For any (i, j) with nonzero similarity, there should be
          either (i, j, s,,ij,,) or (j, i, s,,ji,,) in the input. Rows with i = j are
          ignored, because we assume s,,ij,, = 0.0.

        Returns
        -------
        :py:class:`pyspark.sql.DataFrame`
            A dataset that contains columns of vertex id and the corresponding cluster for
            the id. The schema of it will be:
            - id: Long
            - cluster: Int
        """
