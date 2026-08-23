from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel as JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class _RankingTrainValidationSplit(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        alpha (float): alpha for implicit preference
        blockSize (int): block size for stacking input data in matrices. Data is stacked within partitions. If block size is more than remaining data in a partition then it is adjusted to the size of this data.
        checkpointInterval (int): set checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations. Note: this setting will be ignored if the checkpoint directory is not set in the SparkContext
        coldStartStrategy (str): strategy for dealing with unknown or new users/items at prediction time. This may be useful in cross-validation or production scenarios, for handling user/item ids the model has not seen in the training data. Supported values: nan,drop.
        estimator (object): estimator for selection
        estimatorParamMaps (object): param maps for the estimator
        evaluator (object): evaluator used to select hyper-parameters that maximize the validated metric
        finalStorageLevel (str): StorageLevel for ALS model factors.
        implicitPrefs (bool): whether to use implicit preference
        intermediateStorageLevel (str): StorageLevel for intermediate datasets. Cannot be 'NONE'.
        itemCol (str): column name for item ids. Ids must be within the integer value range.
        maxIter (int): maximum number of iterations (>= 0)
        minRatingsI (int): min ratings for items > 0
        minRatingsU (int): min ratings for users > 0
        nonnegative (bool): whether to use nonnegative constraint for least squares
        numItemBlocks (int): number of item blocks
        numUserBlocks (int): number of user blocks
        parallelism (int): the number of threads to use when running parallel algorithms
        predictionCol (str): prediction column name
        rank (int): rank of the factorization
        ratingCol (str): column name for ratings
        regParam (float): regularization parameter (>= 0)
        seed (long): random seed
        trainRatio (float): ratio between training set and validation set (>= 0 and <= 1)
        userCol (str): column name for user ids. Ids must be within the integer value range.
    """
    alpha: Incomplete
    blockSize: Incomplete
    checkpointInterval: Incomplete
    coldStartStrategy: Incomplete
    estimator: Incomplete
    estimatorParamMaps: Incomplete
    evaluator: Incomplete
    finalStorageLevel: Incomplete
    implicitPrefs: Incomplete
    intermediateStorageLevel: Incomplete
    itemCol: Incomplete
    maxIter: Incomplete
    minRatingsI: Incomplete
    minRatingsU: Incomplete
    nonnegative: Incomplete
    numItemBlocks: Incomplete
    numUserBlocks: Incomplete
    parallelism: Incomplete
    predictionCol: Incomplete
    rank: Incomplete
    ratingCol: Incomplete
    regParam: Incomplete
    seed: Incomplete
    trainRatio: Incomplete
    userCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, alpha: float = 1.0, blockSize: int = 4096, checkpointInterval: int = 10, coldStartStrategy: str = 'nan', estimator: Incomplete | None = None, estimatorParamMaps: Incomplete | None = None, evaluator: Incomplete | None = None, finalStorageLevel: str = 'MEMORY_AND_DISK', implicitPrefs: bool = False, intermediateStorageLevel: str = 'MEMORY_AND_DISK', itemCol: str = 'item', maxIter: int = 10, minRatingsI: int = 1, minRatingsU: int = 1, nonnegative: bool = False, numItemBlocks: int = 10, numUserBlocks: int = 10, parallelism: int = 1, predictionCol: str = 'prediction', rank: int = 10, ratingCol: str = 'rating', regParam: float = 0.1, seed: int = -492944968, trainRatio: float = 0.75, userCol: str = 'user') -> None: ...
    def setParams(self, alpha: float = 1.0, blockSize: int = 4096, checkpointInterval: int = 10, coldStartStrategy: str = 'nan', estimator: Incomplete | None = None, estimatorParamMaps: Incomplete | None = None, evaluator: Incomplete | None = None, finalStorageLevel: str = 'MEMORY_AND_DISK', implicitPrefs: bool = False, intermediateStorageLevel: str = 'MEMORY_AND_DISK', itemCol: str = 'item', maxIter: int = 10, minRatingsI: int = 1, minRatingsU: int = 1, nonnegative: bool = False, numItemBlocks: int = 10, numUserBlocks: int = 10, parallelism: int = 1, predictionCol: str = 'prediction', rank: int = 10, ratingCol: str = 'rating', regParam: float = 0.1, seed: int = -492944968, trainRatio: float = 0.75, userCol: str = 'user'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAlpha(self, value):
        """
        Args:
            alpha: alpha for implicit preference
        """
    def setBlockSize(self, value):
        """
        Args:
            blockSize: block size for stacking input data in matrices. Data is stacked within partitions. If block size is more than remaining data in a partition then it is adjusted to the size of this data.
        """
    def setCheckpointInterval(self, value):
        """
        Args:
            checkpointInterval: set checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations. Note: this setting will be ignored if the checkpoint directory is not set in the SparkContext
        """
    def setColdStartStrategy(self, value):
        """
        Args:
            coldStartStrategy: strategy for dealing with unknown or new users/items at prediction time. This may be useful in cross-validation or production scenarios, for handling user/item ids the model has not seen in the training data. Supported values: nan,drop.
        """
    def setEstimator(self, value):
        """
        Args:
            estimator: estimator for selection
        """
    def setEstimatorParamMaps(self, value):
        """
        Args:
            estimatorParamMaps: param maps for the estimator
        """
    def setEvaluator(self, value):
        """
        Args:
            evaluator: evaluator used to select hyper-parameters that maximize the validated metric
        """
    def setFinalStorageLevel(self, value):
        """
        Args:
            finalStorageLevel: StorageLevel for ALS model factors.
        """
    def setImplicitPrefs(self, value):
        """
        Args:
            implicitPrefs: whether to use implicit preference
        """
    def setIntermediateStorageLevel(self, value):
        """
        Args:
            intermediateStorageLevel: StorageLevel for intermediate datasets. Cannot be 'NONE'.
        """
    def setItemCol(self, value):
        """
        Args:
            itemCol: column name for item ids. Ids must be within the integer value range.
        """
    def setMaxIter(self, value):
        """
        Args:
            maxIter: maximum number of iterations (>= 0)
        """
    def setMinRatingsI(self, value):
        """
        Args:
            minRatingsI: min ratings for items > 0
        """
    def setMinRatingsU(self, value):
        """
        Args:
            minRatingsU: min ratings for users > 0
        """
    def setNonnegative(self, value):
        """
        Args:
            nonnegative: whether to use nonnegative constraint for least squares
        """
    def setNumItemBlocks(self, value):
        """
        Args:
            numItemBlocks: number of item blocks
        """
    def setNumUserBlocks(self, value):
        """
        Args:
            numUserBlocks: number of user blocks
        """
    def setParallelism(self, value):
        """
        Args:
            parallelism: the number of threads to use when running parallel algorithms
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
    def setRank(self, value):
        """
        Args:
            rank: rank of the factorization
        """
    def setRatingCol(self, value):
        """
        Args:
            ratingCol: column name for ratings
        """
    def setRegParam(self, value):
        """
        Args:
            regParam: regularization parameter (>= 0)
        """
    def setSeed(self, value):
        """
        Args:
            seed: random seed
        """
    def setTrainRatio(self, value):
        """
        Args:
            trainRatio: ratio between training set and validation set (>= 0 and <= 1)
        """
    def setUserCol(self, value):
        """
        Args:
            userCol: column name for user ids. Ids must be within the integer value range.
        """
    def getAlpha(self):
        """
        Returns:
            alpha: alpha for implicit preference
        """
    def getBlockSize(self):
        """
        Returns:
            blockSize: block size for stacking input data in matrices. Data is stacked within partitions. If block size is more than remaining data in a partition then it is adjusted to the size of this data.
        """
    def getCheckpointInterval(self):
        """
        Returns:
            checkpointInterval: set checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations. Note: this setting will be ignored if the checkpoint directory is not set in the SparkContext
        """
    def getColdStartStrategy(self):
        """
        Returns:
            coldStartStrategy: strategy for dealing with unknown or new users/items at prediction time. This may be useful in cross-validation or production scenarios, for handling user/item ids the model has not seen in the training data. Supported values: nan,drop.
        """
    def getEstimator(self):
        """
        Returns:
            estimator: estimator for selection
        """
    def getEstimatorParamMaps(self):
        """
        Returns:
            estimatorParamMaps: param maps for the estimator
        """
    def getEvaluator(self):
        """
        Returns:
            evaluator: evaluator used to select hyper-parameters that maximize the validated metric
        """
    def getFinalStorageLevel(self):
        """
        Returns:
            finalStorageLevel: StorageLevel for ALS model factors.
        """
    def getImplicitPrefs(self):
        """
        Returns:
            implicitPrefs: whether to use implicit preference
        """
    def getIntermediateStorageLevel(self):
        """
        Returns:
            intermediateStorageLevel: StorageLevel for intermediate datasets. Cannot be 'NONE'.
        """
    def getItemCol(self):
        """
        Returns:
            itemCol: column name for item ids. Ids must be within the integer value range.
        """
    def getMaxIter(self):
        """
        Returns:
            maxIter: maximum number of iterations (>= 0)
        """
    def getMinRatingsI(self):
        """
        Returns:
            minRatingsI: min ratings for items > 0
        """
    def getMinRatingsU(self):
        """
        Returns:
            minRatingsU: min ratings for users > 0
        """
    def getNonnegative(self):
        """
        Returns:
            nonnegative: whether to use nonnegative constraint for least squares
        """
    def getNumItemBlocks(self):
        """
        Returns:
            numItemBlocks: number of item blocks
        """
    def getNumUserBlocks(self):
        """
        Returns:
            numUserBlocks: number of user blocks
        """
    def getParallelism(self):
        """
        Returns:
            parallelism: the number of threads to use when running parallel algorithms
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
    def getRank(self):
        """
        Returns:
            rank: rank of the factorization
        """
    def getRatingCol(self):
        """
        Returns:
            ratingCol: column name for ratings
        """
    def getRegParam(self):
        """
        Returns:
            regParam: regularization parameter (>= 0)
        """
    def getSeed(self):
        """
        Returns:
            seed: random seed
        """
    def getTrainRatio(self):
        """
        Returns:
            trainRatio: ratio between training set and validation set (>= 0 and <= 1)
        """
    def getUserCol(self):
        """
        Returns:
            userCol: column name for user ids. Ids must be within the integer value range.
        """
