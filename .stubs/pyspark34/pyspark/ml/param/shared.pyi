from pyspark.ml.param import Param as Param, Params as Params, TypeConverters as TypeConverters
from typing import List

class HasMaxIter(Params):
    """
    Mixin for param maxIter: max number of iterations (>= 0).
    """
    maxIter: Param[int]
    def __init__(self) -> None: ...
    def getMaxIter(self) -> int:
        """
        Gets the value of maxIter or its default value.
        """

class HasRegParam(Params):
    """
    Mixin for param regParam: regularization parameter (>= 0).
    """
    regParam: Param[float]
    def __init__(self) -> None: ...
    def getRegParam(self) -> float:
        """
        Gets the value of regParam or its default value.
        """

class HasFeaturesCol(Params):
    """
    Mixin for param featuresCol: features column name.
    """
    featuresCol: Param[str]
    def __init__(self) -> None: ...
    def getFeaturesCol(self) -> str:
        """
        Gets the value of featuresCol or its default value.
        """

class HasLabelCol(Params):
    """
    Mixin for param labelCol: label column name.
    """
    labelCol: Param[str]
    def __init__(self) -> None: ...
    def getLabelCol(self) -> str:
        """
        Gets the value of labelCol or its default value.
        """

class HasPredictionCol(Params):
    """
    Mixin for param predictionCol: prediction column name.
    """
    predictionCol: Param[str]
    def __init__(self) -> None: ...
    def getPredictionCol(self) -> str:
        """
        Gets the value of predictionCol or its default value.
        """

class HasProbabilityCol(Params):
    """
    Mixin for param probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities.
    """
    probabilityCol: Param[str]
    def __init__(self) -> None: ...
    def getProbabilityCol(self) -> str:
        """
        Gets the value of probabilityCol or its default value.
        """

class HasRawPredictionCol(Params):
    """
    Mixin for param rawPredictionCol: raw prediction (a.k.a. confidence) column name.
    """
    rawPredictionCol: Param[str]
    def __init__(self) -> None: ...
    def getRawPredictionCol(self) -> str:
        """
        Gets the value of rawPredictionCol or its default value.
        """

class HasInputCol(Params):
    """
    Mixin for param inputCol: input column name.
    """
    inputCol: Param[str]
    def __init__(self) -> None: ...
    def getInputCol(self) -> str:
        """
        Gets the value of inputCol or its default value.
        """

class HasInputCols(Params):
    """
    Mixin for param inputCols: input column names.
    """
    inputCols: Param[List[str]]
    def __init__(self) -> None: ...
    def getInputCols(self) -> List[str]:
        """
        Gets the value of inputCols or its default value.
        """

class HasOutputCol(Params):
    """
    Mixin for param outputCol: output column name.
    """
    outputCol: Param[str]
    def __init__(self) -> None: ...
    def getOutputCol(self) -> str:
        """
        Gets the value of outputCol or its default value.
        """

class HasOutputCols(Params):
    """
    Mixin for param outputCols: output column names.
    """
    outputCols: Param[List[str]]
    def __init__(self) -> None: ...
    def getOutputCols(self) -> List[str]:
        """
        Gets the value of outputCols or its default value.
        """

class HasNumFeatures(Params):
    """
    Mixin for param numFeatures: Number of features. Should be greater than 0.
    """
    numFeatures: Param[int]
    def __init__(self) -> None: ...
    def getNumFeatures(self) -> int:
        """
        Gets the value of numFeatures or its default value.
        """

class HasCheckpointInterval(Params):
    """
    Mixin for param checkpointInterval: set checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations. Note: this setting will be ignored if the checkpoint directory is not set in the SparkContext.
    """
    checkpointInterval: Param[int]
    def __init__(self) -> None: ...
    def getCheckpointInterval(self) -> int:
        """
        Gets the value of checkpointInterval or its default value.
        """

class HasSeed(Params):
    """
    Mixin for param seed: random seed.
    """
    seed: Param[int]
    def __init__(self) -> None: ...
    def getSeed(self) -> int:
        """
        Gets the value of seed or its default value.
        """

class HasTol(Params):
    """
    Mixin for param tol: the convergence tolerance for iterative algorithms (>= 0).
    """
    tol: Param[float]
    def __init__(self) -> None: ...
    def getTol(self) -> float:
        """
        Gets the value of tol or its default value.
        """

class HasRelativeError(Params):
    """
    Mixin for param relativeError: the relative target precision for the approximate quantile algorithm. Must be in the range [0, 1]
    """
    relativeError: Param[float]
    def __init__(self) -> None: ...
    def getRelativeError(self) -> float:
        """
        Gets the value of relativeError or its default value.
        """

class HasStepSize(Params):
    """
    Mixin for param stepSize: Step size to be used for each iteration of optimization (>= 0).
    """
    stepSize: Param[float]
    def __init__(self) -> None: ...
    def getStepSize(self) -> float:
        """
        Gets the value of stepSize or its default value.
        """

class HasHandleInvalid(Params):
    """
    Mixin for param handleInvalid: how to handle invalid entries. Options are skip (which will filter out rows with bad values), or error (which will throw an error). More options may be added later.
    """
    handleInvalid: Param[str]
    def __init__(self) -> None: ...
    def getHandleInvalid(self) -> str:
        """
        Gets the value of handleInvalid or its default value.
        """

class HasElasticNetParam(Params):
    """
    Mixin for param elasticNetParam: the ElasticNet mixing parameter, in range [0, 1]. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty.
    """
    elasticNetParam: Param[float]
    def __init__(self) -> None: ...
    def getElasticNetParam(self) -> float:
        """
        Gets the value of elasticNetParam or its default value.
        """

class HasFitIntercept(Params):
    """
    Mixin for param fitIntercept: whether to fit an intercept term.
    """
    fitIntercept: Param[bool]
    def __init__(self) -> None: ...
    def getFitIntercept(self) -> bool:
        """
        Gets the value of fitIntercept or its default value.
        """

class HasStandardization(Params):
    """
    Mixin for param standardization: whether to standardize the training features before fitting the model.
    """
    standardization: Param[bool]
    def __init__(self) -> None: ...
    def getStandardization(self) -> bool:
        """
        Gets the value of standardization or its default value.
        """

class HasThresholds(Params):
    """
    Mixin for param thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0, excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold.
    """
    thresholds: Param[List[float]]
    def __init__(self) -> None: ...
    def getThresholds(self) -> List[float]:
        """
        Gets the value of thresholds or its default value.
        """

class HasThreshold(Params):
    """
    Mixin for param threshold: threshold in binary classification prediction, in range [0, 1]
    """
    threshold: Param[float]
    def __init__(self) -> None: ...
    def getThreshold(self) -> float:
        """
        Gets the value of threshold or its default value.
        """

class HasWeightCol(Params):
    """
    Mixin for param weightCol: weight column name. If this is not set or empty, we treat all instance weights as 1.0.
    """
    weightCol: Param[str]
    def __init__(self) -> None: ...
    def getWeightCol(self) -> str:
        """
        Gets the value of weightCol or its default value.
        """

class HasSolver(Params):
    """
    Mixin for param solver: the solver algorithm for optimization. If this is not set or empty, default value is 'auto'.
    """
    solver: Param[str]
    def __init__(self) -> None: ...
    def getSolver(self) -> str:
        """
        Gets the value of solver or its default value.
        """

class HasVarianceCol(Params):
    """
    Mixin for param varianceCol: column name for the biased sample variance of prediction.
    """
    varianceCol: Param[str]
    def __init__(self) -> None: ...
    def getVarianceCol(self) -> str:
        """
        Gets the value of varianceCol or its default value.
        """

class HasAggregationDepth(Params):
    """
    Mixin for param aggregationDepth: suggested depth for treeAggregate (>= 2).
    """
    aggregationDepth: Param[int]
    def __init__(self) -> None: ...
    def getAggregationDepth(self) -> int:
        """
        Gets the value of aggregationDepth or its default value.
        """

class HasParallelism(Params):
    """
    Mixin for param parallelism: the number of threads to use when running parallel algorithms (>= 1).
    """
    parallelism: Param[int]
    def __init__(self) -> None: ...
    def getParallelism(self) -> int:
        """
        Gets the value of parallelism or its default value.
        """

class HasCollectSubModels(Params):
    """
    Mixin for param collectSubModels: Param for whether to collect a list of sub-models trained during tuning. If set to false, then only the single best sub-model will be available after fitting. If set to true, then all sub-models will be available. Warning: For large models, collecting all sub-models can cause OOMs on the Spark driver.
    """
    collectSubModels: Param[bool]
    def __init__(self) -> None: ...
    def getCollectSubModels(self) -> bool:
        """
        Gets the value of collectSubModels or its default value.
        """

class HasLoss(Params):
    """
    Mixin for param loss: the loss function to be optimized.
    """
    loss: Param[str]
    def __init__(self) -> None: ...
    def getLoss(self) -> str:
        """
        Gets the value of loss or its default value.
        """

class HasDistanceMeasure(Params):
    """
    Mixin for param distanceMeasure: the distance measure. Supported options: 'euclidean' and 'cosine'.
    """
    distanceMeasure: Param[str]
    def __init__(self) -> None: ...
    def getDistanceMeasure(self) -> str:
        """
        Gets the value of distanceMeasure or its default value.
        """

class HasValidationIndicatorCol(Params):
    """
    Mixin for param validationIndicatorCol: name of the column that indicates whether each row is for training or for validation. False indicates training; true indicates validation.
    """
    validationIndicatorCol: Param[str]
    def __init__(self) -> None: ...
    def getValidationIndicatorCol(self) -> str:
        """
        Gets the value of validationIndicatorCol or its default value.
        """

class HasBlockSize(Params):
    """
    Mixin for param blockSize: block size for stacking input data in matrices. Data is stacked within partitions. If block size is more than remaining data in a partition then it is adjusted to the size of this data.
    """
    blockSize: Param[int]
    def __init__(self) -> None: ...
    def getBlockSize(self) -> int:
        """
        Gets the value of blockSize or its default value.
        """

class HasMaxBlockSizeInMB(Params):
    """
    Mixin for param maxBlockSizeInMB: maximum memory in MB for stacking input data into blocks. Data is stacked within partitions. If more than remaining data size in a partition then it is adjusted to the data size. Default 0.0 represents choosing optimal value, depends on specific algorithm. Must be >= 0.
    """
    maxBlockSizeInMB: Param[float]
    def __init__(self) -> None: ...
    def getMaxBlockSizeInMB(self) -> float:
        """
        Gets the value of maxBlockSizeInMB or its default value.
        """
