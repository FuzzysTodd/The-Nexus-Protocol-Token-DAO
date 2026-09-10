from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class _SARModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        activityTimeFormat (str): Time format for events, default: yyyy/MM/dd'T'h:mm:ss
        alpha (float): alpha for implicit preference
        blockSize (int): block size for stacking input data in matrices. Data is stacked within partitions. If block size is more than remaining data in a partition then it is adjusted to the size of this data.
        checkpointInterval (int): set checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations. Note: this setting will be ignored if the checkpoint directory is not set in the SparkContext
        coldStartStrategy (str): strategy for dealing with unknown or new users/items at prediction time. This may be useful in cross-validation or production scenarios, for handling user/item ids the model has not seen in the training data. Supported values: nan,drop.
        finalStorageLevel (str): StorageLevel for ALS model factors.
        implicitPrefs (bool): whether to use implicit preference
        intermediateStorageLevel (str): StorageLevel for intermediate datasets. Cannot be 'NONE'.
        itemCol (str): column name for item ids. Ids must be within the integer value range.
        itemDataFrame (object): Time of activity
        maxIter (int): maximum number of iterations (>= 0)
        nonnegative (bool): whether to use nonnegative constraint for least squares
        numItemBlocks (int): number of item blocks
        numUserBlocks (int): number of user blocks
        predictionCol (str): prediction column name
        rank (int): rank of the factorization
        ratingCol (str): column name for ratings
        regParam (float): regularization parameter (>= 0)
        seed (long): random seed
        similarityFunction (str): Defines the similarity function to be used by the model. Lift favors serendipity, Co-occurrence favors predictability, and Jaccard is a nice compromise between the two.
        startTime (str): Set time custom now time if using historical data
        startTimeFormat (str): Format for start time
        supportThreshold (int): Minimum number of ratings per item
        timeCol (str): Time of activity
        timeDecayCoeff (int): Use to scale time decay coeff to different half life dur
        userCol (str): column name for user ids. Ids must be within the integer value range.
        userDataFrame (object): Time of activity
    """
    activityTimeFormat: Incomplete
    alpha: Incomplete
    blockSize: Incomplete
    checkpointInterval: Incomplete
    coldStartStrategy: Incomplete
    finalStorageLevel: Incomplete
    implicitPrefs: Incomplete
    intermediateStorageLevel: Incomplete
    itemCol: Incomplete
    itemDataFrame: Incomplete
    maxIter: Incomplete
    nonnegative: Incomplete
    numItemBlocks: Incomplete
    numUserBlocks: Incomplete
    predictionCol: Incomplete
    rank: Incomplete
    ratingCol: Incomplete
    regParam: Incomplete
    seed: Incomplete
    similarityFunction: Incomplete
    startTime: Incomplete
    startTimeFormat: Incomplete
    supportThreshold: Incomplete
    timeCol: Incomplete
    timeDecayCoeff: Incomplete
    userCol: Incomplete
    userDataFrame: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, activityTimeFormat: str = "yyyy/MM/dd'T'h:mm:ss", alpha: float = 1.0, blockSize: int = 4096, checkpointInterval: int = 10, coldStartStrategy: str = 'nan', finalStorageLevel: str = 'MEMORY_AND_DISK', implicitPrefs: bool = False, intermediateStorageLevel: str = 'MEMORY_AND_DISK', itemCol: str = 'item', itemDataFrame: Incomplete | None = None, maxIter: int = 10, nonnegative: bool = False, numItemBlocks: int = 10, numUserBlocks: int = 10, predictionCol: str = 'prediction', rank: int = 10, ratingCol: str = 'rating', regParam: float = 0.1, seed: int = -1453370660, similarityFunction: str = 'jaccard', startTime: Incomplete | None = None, startTimeFormat: str = 'EEE MMM dd HH:mm:ss Z yyyy', supportThreshold: int = 4, timeCol: str = 'time', timeDecayCoeff: int = 30, userCol: str = 'user', userDataFrame: Incomplete | None = None) -> None: ...
    def setParams(self, activityTimeFormat: str = "yyyy/MM/dd'T'h:mm:ss", alpha: float = 1.0, blockSize: int = 4096, checkpointInterval: int = 10, coldStartStrategy: str = 'nan', finalStorageLevel: str = 'MEMORY_AND_DISK', implicitPrefs: bool = False, intermediateStorageLevel: str = 'MEMORY_AND_DISK', itemCol: str = 'item', itemDataFrame: Incomplete | None = None, maxIter: int = 10, nonnegative: bool = False, numItemBlocks: int = 10, numUserBlocks: int = 10, predictionCol: str = 'prediction', rank: int = 10, ratingCol: str = 'rating', regParam: float = 0.1, seed: int = -1453370660, similarityFunction: str = 'jaccard', startTime: Incomplete | None = None, startTimeFormat: str = 'EEE MMM dd HH:mm:ss Z yyyy', supportThreshold: int = 4, timeCol: str = 'time', timeDecayCoeff: int = 30, userCol: str = 'user', userDataFrame: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setActivityTimeFormat(self, value):
        """
        Args:
            activityTimeFormat: Time format for events, default: yyyy/MM/dd'T'h:mm:ss
        """
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
    def setItemDataFrame(self, value):
        """
        Args:
            itemDataFrame: Time of activity
        """
    def setMaxIter(self, value):
        """
        Args:
            maxIter: maximum number of iterations (>= 0)
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
    def setSimilarityFunction(self, value):
        """
        Args:
            similarityFunction: Defines the similarity function to be used by the model. Lift favors serendipity, Co-occurrence favors predictability, and Jaccard is a nice compromise between the two.
        """
    def setStartTime(self, value):
        """
        Args:
            startTime: Set time custom now time if using historical data
        """
    def setStartTimeFormat(self, value):
        """
        Args:
            startTimeFormat: Format for start time
        """
    def setSupportThreshold(self, value):
        """
        Args:
            supportThreshold: Minimum number of ratings per item
        """
    def setTimeCol(self, value):
        """
        Args:
            timeCol: Time of activity
        """
    def setTimeDecayCoeff(self, value):
        """
        Args:
            timeDecayCoeff: Use to scale time decay coeff to different half life dur
        """
    def setUserCol(self, value):
        """
        Args:
            userCol: column name for user ids. Ids must be within the integer value range.
        """
    def setUserDataFrame(self, value):
        """
        Args:
            userDataFrame: Time of activity
        """
    def getActivityTimeFormat(self):
        """
        Returns:
            activityTimeFormat: Time format for events, default: yyyy/MM/dd'T'h:mm:ss
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
    def getItemDataFrame(self):
        """
        Returns:
            itemDataFrame: Time of activity
        """
    def getMaxIter(self):
        """
        Returns:
            maxIter: maximum number of iterations (>= 0)
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
    def getSimilarityFunction(self):
        """
        Returns:
            similarityFunction: Defines the similarity function to be used by the model. Lift favors serendipity, Co-occurrence favors predictability, and Jaccard is a nice compromise between the two.
        """
    def getStartTime(self):
        """
        Returns:
            startTime: Set time custom now time if using historical data
        """
    def getStartTimeFormat(self):
        """
        Returns:
            startTimeFormat: Format for start time
        """
    def getSupportThreshold(self):
        """
        Returns:
            supportThreshold: Minimum number of ratings per item
        """
    def getTimeCol(self):
        """
        Returns:
            timeCol: Time of activity
        """
    def getTimeDecayCoeff(self):
        """
        Returns:
            timeDecayCoeff: Use to scale time decay coeff to different half life dur
        """
    def getUserCol(self):
        """
        Returns:
            userCol: column name for user ids. Ids must be within the integer value range.
        """
    def getUserDataFrame(self):
        """
        Returns:
            userDataFrame: Time of activity
        """
