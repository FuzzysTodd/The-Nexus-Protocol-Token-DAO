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

class LightGBMRegressor(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        alpha (float): parameter for Huber loss and Quantile regression
        baggingFraction (float): Bagging fraction
        baggingFreq (int): Bagging frequency
        baggingSeed (int): Bagging seed
        binSampleCount (int): Number of samples considered at computing histogram bins
        boostFromAverage (bool): Adjusts initial score to the mean of labels for faster convergence
        boostingType (str): Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). 
        catSmooth (float): this can reduce the effect of noises in categorical features, especially for categories with few data
        categoricalSlotIndexes (list): List of categorical column indexes, the slot index in the features column
        categoricalSlotNames (list): List of categorical column slot names, the slot name in the features column
        catl2 (float): L2 regularization in categorical split
        chunkSize (int): Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.
        dataRandomSeed (int): Random seed for sampling data to construct histogram bins.
        dataTransferMode (str): Specify how SynapseML transfers data from Spark to LightGBM.  Values can be streaming, bulk. Default is bulk, which is the legacy mode.
        defaultListenPort (int): The default listen port on executors, used for testing
        deterministic (bool): Used only with cpu devide type. Setting this to true should ensure stable results when using the same data and the same parameters.  Note: setting this to true may slow down training.  To avoid potential instability due to numerical issues, please set force_col_wise=true or force_row_wise=true when setting deterministic=true
        driverListenPort (int): The listen port on a driver. Default value is 0 (random)
        dropRate (float): Dropout rate: a fraction of previous trees to drop during the dropout
        dropSeed (int): Random seed to choose dropping models. Only used in dart.
        earlyStoppingRound (int): Early stopping round
        executionMode (str): Deprecated. Please use dataTransferMode.
        extraSeed (int): Random seed for selecting threshold when extra_trees is true
        featureFraction (float): Feature fraction
        featureFractionByNode (float): Feature fraction by node
        featureFractionSeed (int): Feature fraction seed
        featuresCol (str): features column name
        featuresShapCol (str): Output SHAP vector column name after prediction containing the feature contribution values
        fobj (object): Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).
        improvementTolerance (float): Tolerance to consider improvement in metric
        initScoreCol (str): The name of the initial score column, used for continued training
        isEnableSparse (bool): Used to enable/disable sparse optimization
        isProvideTrainingMetric (bool): Whether output metric result over training dataset.
        labelCol (str): label column name
        lambdaL1 (float): L1 regularization
        lambdaL2 (float): L2 regularization
        leafPredictionCol (str): Predicted leaf indices's column name
        learningRate (float): Learning rate or shrinkage rate
        matrixType (str): Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.
        maxBin (int): Max bin
        maxBinByFeature (list): Max number of bins for each feature
        maxCatThreshold (int): limit number of split points considered for categorical features
        maxCatToOnehot (int): when number of categories of one feature smaller than or equal to this, one-vs-other split algorithm will be used
        maxDeltaStep (float): Used to limit the max output of tree leaves
        maxDepth (int): Max depth
        maxDrop (int): Max number of dropped trees during one boosting iteration
        maxNumClasses (int): Number of max classes to infer numClass in multi-class classification.
        maxStreamingOMPThreads (int): Maximum number of OpenMP threads used by a LightGBM thread. Used only for thread-safe buffer allocation. Use -1 to use OpenMP default, but in a Spark environment it's best to set a fixed value.
        metric (str): Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. 
        microBatchSize (int): Specify how many elements are sent in a streaming micro-batch.
        minDataInLeaf (int): Minimal number of data in one leaf. Can be used to deal with over-fitting.
        minDataPerBin (int): Minimal number of data inside one bin
        minDataPerGroup (int): minimal number of data per categorical group
        minGainToSplit (float): The minimal gain to perform split
        minSumHessianInLeaf (float): Minimal sum hessian in one leaf
        modelString (str): LightGBM model to retrain
        monotoneConstraints (list): used for constraints of monotonic features. 1 means increasing, -1 means decreasing, 0 means non-constraint. Specify all features in order.
        monotoneConstraintsMethod (str): Monotone constraints method. basic, intermediate, or advanced.
        monotonePenalty (float): A penalization parameter X forbids any monotone splits on the first X (rounded down) level(s) of the tree.
        negBaggingFraction (float): Negative Bagging fraction
        numBatches (int): If greater than 0, splits data into separate batches during training
        numIterations (int): Number of iterations, LightGBM constructs num_class * num_iterations trees
        numLeaves (int): Number of leaves
        numTasks (int): Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.
        numThreads (int): Number of threads per executor for LightGBM. For the best speed, set this to the number of real CPU cores.
        objective (str): The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. 
        objectiveSeed (int): Random seed for objectives, if random process is needed.  Currently used only for rank_xendcg objective.
        otherRate (float): The retain ratio of small gradient data. Only used in goss.
        parallelism (str): Tree learner parallelism, can be set to data_parallel or voting_parallel
        passThroughArgs (str): Direct string to pass through to LightGBM library (appended with other explicitly set params). Will override any parameters given with explicit setters. Can include multiple parameters in one string. e.g., force_row_wise=true
        posBaggingFraction (float): Positive Bagging fraction
        predictDisableShapeCheck (bool): control whether or not LightGBM raises an error when you try to predict on data with a different number of features than the training data
        predictionCol (str): prediction column name
        referenceDataset (list): The reference Dataset that was used for the fit. If using samplingMode=custom, this must be set before fit().
        repartitionByGroupingColumn (bool): Repartition training data according to grouping column, on by default.
        samplingMode (str): Data sampling for streaming mode. Sampled data is used to define bins. 'global': sample from all data, 'subset': sample from first N rows, or 'fixed': Take first N rows as sample.Values can be global, subset, or fixed. Default is subset.
        samplingSubsetSize (int): Specify subset size N for the sampling mode 'subset'. 'binSampleCount' rows will be chosen from the first N values of the dataset. Subset can be used when rows are expected to be random and data is huge.
        seed (int): Main seed, used to generate other seeds
        skipDrop (float): Probability of skipping the dropout procedure during a boosting iteration
        slotNames (list): List of slot names in the features column
        timeout (float): Timeout in seconds
        topK (int): The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0
        topRate (float): The retain ratio of large gradient data. Only used in goss.
        tweedieVariancePower (float): control the variance of tweedie distribution, must be between 1 and 2
        uniformDrop (bool): Set this to true to use uniform drop in dart mode
        useBarrierExecutionMode (bool): Barrier execution mode which uses a barrier stage, off by default.
        useMissing (bool): Set this to false to disable the special handle of missing value
        useSingleDatasetMode (bool): Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead.
        validationIndicatorCol (str): Indicates whether the row is for training or validation
        verbosity (int): Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug
        weightCol (str): The name of the weight column
        xGBoostDartMode (bool): Set this to true to use xgboost dart mode
        zeroAsMissing (bool): Set to true to treat all zero as missing values (including the unshown values in LibSVM / sparse matrices). Set to false to use na for representing missing values
    """
    alpha: Incomplete
    baggingFraction: Incomplete
    baggingFreq: Incomplete
    baggingSeed: Incomplete
    binSampleCount: Incomplete
    boostFromAverage: Incomplete
    boostingType: Incomplete
    catSmooth: Incomplete
    categoricalSlotIndexes: Incomplete
    categoricalSlotNames: Incomplete
    catl2: Incomplete
    chunkSize: Incomplete
    dataRandomSeed: Incomplete
    dataTransferMode: Incomplete
    defaultListenPort: Incomplete
    deterministic: Incomplete
    driverListenPort: Incomplete
    dropRate: Incomplete
    dropSeed: Incomplete
    earlyStoppingRound: Incomplete
    executionMode: Incomplete
    extraSeed: Incomplete
    featureFraction: Incomplete
    featureFractionByNode: Incomplete
    featureFractionSeed: Incomplete
    featuresCol: Incomplete
    featuresShapCol: Incomplete
    fobj: Incomplete
    improvementTolerance: Incomplete
    initScoreCol: Incomplete
    isEnableSparse: Incomplete
    isProvideTrainingMetric: Incomplete
    labelCol: Incomplete
    lambdaL1: Incomplete
    lambdaL2: Incomplete
    leafPredictionCol: Incomplete
    learningRate: Incomplete
    matrixType: Incomplete
    maxBin: Incomplete
    maxBinByFeature: Incomplete
    maxCatThreshold: Incomplete
    maxCatToOnehot: Incomplete
    maxDeltaStep: Incomplete
    maxDepth: Incomplete
    maxDrop: Incomplete
    maxNumClasses: Incomplete
    maxStreamingOMPThreads: Incomplete
    metric: Incomplete
    microBatchSize: Incomplete
    minDataInLeaf: Incomplete
    minDataPerBin: Incomplete
    minDataPerGroup: Incomplete
    minGainToSplit: Incomplete
    minSumHessianInLeaf: Incomplete
    modelString: Incomplete
    monotoneConstraints: Incomplete
    monotoneConstraintsMethod: Incomplete
    monotonePenalty: Incomplete
    negBaggingFraction: Incomplete
    numBatches: Incomplete
    numIterations: Incomplete
    numLeaves: Incomplete
    numTasks: Incomplete
    numThreads: Incomplete
    objective: Incomplete
    objectiveSeed: Incomplete
    otherRate: Incomplete
    parallelism: Incomplete
    passThroughArgs: Incomplete
    posBaggingFraction: Incomplete
    predictDisableShapeCheck: Incomplete
    predictionCol: Incomplete
    referenceDataset: Incomplete
    repartitionByGroupingColumn: Incomplete
    samplingMode: Incomplete
    samplingSubsetSize: Incomplete
    seed: Incomplete
    skipDrop: Incomplete
    slotNames: Incomplete
    timeout: Incomplete
    topK: Incomplete
    topRate: Incomplete
    tweedieVariancePower: Incomplete
    uniformDrop: Incomplete
    useBarrierExecutionMode: Incomplete
    useMissing: Incomplete
    useSingleDatasetMode: Incomplete
    validationIndicatorCol: Incomplete
    verbosity: Incomplete
    weightCol: Incomplete
    xGBoostDartMode: Incomplete
    zeroAsMissing: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, alpha: float = 0.9, baggingFraction: float = 1.0, baggingFreq: int = 0, baggingSeed: int = 3, binSampleCount: int = 200000, boostFromAverage: bool = True, boostingType: str = 'gbdt', catSmooth: float = 10.0, categoricalSlotIndexes=[], categoricalSlotNames=[], catl2: float = 10.0, chunkSize: int = 10000, dataRandomSeed: int = 1, dataTransferMode: str = 'streaming', defaultListenPort: int = 12400, deterministic: bool = False, driverListenPort: int = 0, dropRate: float = 0.1, dropSeed: int = 4, earlyStoppingRound: int = 0, executionMode: Incomplete | None = None, extraSeed: int = 6, featureFraction: float = 1.0, featureFractionByNode: Incomplete | None = None, featureFractionSeed: int = 2, featuresCol: str = 'features', featuresShapCol: str = '', fobj: Incomplete | None = None, improvementTolerance: float = 0.0, initScoreCol: Incomplete | None = None, isEnableSparse: bool = True, isProvideTrainingMetric: bool = False, labelCol: str = 'label', lambdaL1: float = 0.0, lambdaL2: float = 0.0, leafPredictionCol: str = '', learningRate: float = 0.1, matrixType: str = 'auto', maxBin: int = 255, maxBinByFeature=[], maxCatThreshold: int = 32, maxCatToOnehot: int = 4, maxDeltaStep: float = 0.0, maxDepth: int = -1, maxDrop: int = 50, maxNumClasses: int = 100, maxStreamingOMPThreads: int = 16, metric: str = '', microBatchSize: int = 100, minDataInLeaf: int = 20, minDataPerBin: int = 3, minDataPerGroup: int = 100, minGainToSplit: float = 0.0, minSumHessianInLeaf: float = 0.001, modelString: str = '', monotoneConstraints=[], monotoneConstraintsMethod: str = 'basic', monotonePenalty: float = 0.0, negBaggingFraction: float = 1.0, numBatches: int = 0, numIterations: int = 100, numLeaves: int = 31, numTasks: int = 0, numThreads: int = 0, objective: str = 'regression', objectiveSeed: int = 5, otherRate: float = 0.1, parallelism: str = 'data_parallel', passThroughArgs: str = '', posBaggingFraction: float = 1.0, predictDisableShapeCheck: bool = False, predictionCol: str = 'prediction', referenceDataset: Incomplete | None = None, repartitionByGroupingColumn: bool = True, samplingMode: str = 'subset', samplingSubsetSize: int = 1000000, seed: Incomplete | None = None, skipDrop: float = 0.5, slotNames=[], timeout: float = 1200.0, topK: int = 20, topRate: float = 0.2, tweedieVariancePower: float = 1.5, uniformDrop: bool = False, useBarrierExecutionMode: bool = False, useMissing: bool = True, useSingleDatasetMode: bool = True, validationIndicatorCol: Incomplete | None = None, verbosity: int = -1, weightCol: Incomplete | None = None, xGBoostDartMode: bool = False, zeroAsMissing: bool = False) -> None: ...
    def setParams(self, alpha: float = 0.9, baggingFraction: float = 1.0, baggingFreq: int = 0, baggingSeed: int = 3, binSampleCount: int = 200000, boostFromAverage: bool = True, boostingType: str = 'gbdt', catSmooth: float = 10.0, categoricalSlotIndexes=[], categoricalSlotNames=[], catl2: float = 10.0, chunkSize: int = 10000, dataRandomSeed: int = 1, dataTransferMode: str = 'streaming', defaultListenPort: int = 12400, deterministic: bool = False, driverListenPort: int = 0, dropRate: float = 0.1, dropSeed: int = 4, earlyStoppingRound: int = 0, executionMode: Incomplete | None = None, extraSeed: int = 6, featureFraction: float = 1.0, featureFractionByNode: Incomplete | None = None, featureFractionSeed: int = 2, featuresCol: str = 'features', featuresShapCol: str = '', fobj: Incomplete | None = None, improvementTolerance: float = 0.0, initScoreCol: Incomplete | None = None, isEnableSparse: bool = True, isProvideTrainingMetric: bool = False, labelCol: str = 'label', lambdaL1: float = 0.0, lambdaL2: float = 0.0, leafPredictionCol: str = '', learningRate: float = 0.1, matrixType: str = 'auto', maxBin: int = 255, maxBinByFeature=[], maxCatThreshold: int = 32, maxCatToOnehot: int = 4, maxDeltaStep: float = 0.0, maxDepth: int = -1, maxDrop: int = 50, maxNumClasses: int = 100, maxStreamingOMPThreads: int = 16, metric: str = '', microBatchSize: int = 100, minDataInLeaf: int = 20, minDataPerBin: int = 3, minDataPerGroup: int = 100, minGainToSplit: float = 0.0, minSumHessianInLeaf: float = 0.001, modelString: str = '', monotoneConstraints=[], monotoneConstraintsMethod: str = 'basic', monotonePenalty: float = 0.0, negBaggingFraction: float = 1.0, numBatches: int = 0, numIterations: int = 100, numLeaves: int = 31, numTasks: int = 0, numThreads: int = 0, objective: str = 'regression', objectiveSeed: int = 5, otherRate: float = 0.1, parallelism: str = 'data_parallel', passThroughArgs: str = '', posBaggingFraction: float = 1.0, predictDisableShapeCheck: bool = False, predictionCol: str = 'prediction', referenceDataset: Incomplete | None = None, repartitionByGroupingColumn: bool = True, samplingMode: str = 'subset', samplingSubsetSize: int = 1000000, seed: Incomplete | None = None, skipDrop: float = 0.5, slotNames=[], timeout: float = 1200.0, topK: int = 20, topRate: float = 0.2, tweedieVariancePower: float = 1.5, uniformDrop: bool = False, useBarrierExecutionMode: bool = False, useMissing: bool = True, useSingleDatasetMode: bool = True, validationIndicatorCol: Incomplete | None = None, verbosity: int = -1, weightCol: Incomplete | None = None, xGBoostDartMode: bool = False, zeroAsMissing: bool = False):
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
            alpha: parameter for Huber loss and Quantile regression
        """
    def setBaggingFraction(self, value):
        """
        Args:
            baggingFraction: Bagging fraction
        """
    def setBaggingFreq(self, value):
        """
        Args:
            baggingFreq: Bagging frequency
        """
    def setBaggingSeed(self, value):
        """
        Args:
            baggingSeed: Bagging seed
        """
    def setBinSampleCount(self, value):
        """
        Args:
            binSampleCount: Number of samples considered at computing histogram bins
        """
    def setBoostFromAverage(self, value):
        """
        Args:
            boostFromAverage: Adjusts initial score to the mean of labels for faster convergence
        """
    def setBoostingType(self, value):
        """
        Args:
            boostingType: Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). 
        """
    def setCatSmooth(self, value):
        """
        Args:
            catSmooth: this can reduce the effect of noises in categorical features, especially for categories with few data
        """
    def setCategoricalSlotIndexes(self, value):
        """
        Args:
            categoricalSlotIndexes: List of categorical column indexes, the slot index in the features column
        """
    def setCategoricalSlotNames(self, value):
        """
        Args:
            categoricalSlotNames: List of categorical column slot names, the slot name in the features column
        """
    def setCatl2(self, value):
        """
        Args:
            catl2: L2 regularization in categorical split
        """
    def setChunkSize(self, value):
        """
        Args:
            chunkSize: Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.
        """
    def setDataRandomSeed(self, value):
        """
        Args:
            dataRandomSeed: Random seed for sampling data to construct histogram bins.
        """
    def setDataTransferMode(self, value):
        """
        Args:
            dataTransferMode: Specify how SynapseML transfers data from Spark to LightGBM.  Values can be streaming, bulk. Default is bulk, which is the legacy mode.
        """
    def setDefaultListenPort(self, value):
        """
        Args:
            defaultListenPort: The default listen port on executors, used for testing
        """
    def setDeterministic(self, value):
        """
        Args:
            deterministic: Used only with cpu devide type. Setting this to true should ensure stable results when using the same data and the same parameters.  Note: setting this to true may slow down training.  To avoid potential instability due to numerical issues, please set force_col_wise=true or force_row_wise=true when setting deterministic=true
        """
    def setDriverListenPort(self, value):
        """
        Args:
            driverListenPort: The listen port on a driver. Default value is 0 (random)
        """
    def setDropRate(self, value):
        """
        Args:
            dropRate: Dropout rate: a fraction of previous trees to drop during the dropout
        """
    def setDropSeed(self, value):
        """
        Args:
            dropSeed: Random seed to choose dropping models. Only used in dart.
        """
    def setEarlyStoppingRound(self, value):
        """
        Args:
            earlyStoppingRound: Early stopping round
        """
    def setExecutionMode(self, value):
        """
        Args:
            executionMode: Deprecated. Please use dataTransferMode.
        """
    def setExtraSeed(self, value):
        """
        Args:
            extraSeed: Random seed for selecting threshold when extra_trees is true
        """
    def setFeatureFraction(self, value):
        """
        Args:
            featureFraction: Feature fraction
        """
    def setFeatureFractionByNode(self, value):
        """
        Args:
            featureFractionByNode: Feature fraction by node
        """
    def setFeatureFractionSeed(self, value):
        """
        Args:
            featureFractionSeed: Feature fraction seed
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: features column name
        """
    def setFeaturesShapCol(self, value):
        """
        Args:
            featuresShapCol: Output SHAP vector column name after prediction containing the feature contribution values
        """
    def setFobj(self, value):
        """
        Args:
            fobj: Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).
        """
    def setImprovementTolerance(self, value):
        """
        Args:
            improvementTolerance: Tolerance to consider improvement in metric
        """
    def setInitScoreCol(self, value):
        """
        Args:
            initScoreCol: The name of the initial score column, used for continued training
        """
    def setIsEnableSparse(self, value):
        """
        Args:
            isEnableSparse: Used to enable/disable sparse optimization
        """
    def setIsProvideTrainingMetric(self, value):
        """
        Args:
            isProvideTrainingMetric: Whether output metric result over training dataset.
        """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
    def setLambdaL1(self, value):
        """
        Args:
            lambdaL1: L1 regularization
        """
    def setLambdaL2(self, value):
        """
        Args:
            lambdaL2: L2 regularization
        """
    def setLeafPredictionCol(self, value):
        """
        Args:
            leafPredictionCol: Predicted leaf indices's column name
        """
    def setLearningRate(self, value):
        """
        Args:
            learningRate: Learning rate or shrinkage rate
        """
    def setMatrixType(self, value):
        """
        Args:
            matrixType: Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.
        """
    def setMaxBin(self, value):
        """
        Args:
            maxBin: Max bin
        """
    def setMaxBinByFeature(self, value):
        """
        Args:
            maxBinByFeature: Max number of bins for each feature
        """
    def setMaxCatThreshold(self, value):
        """
        Args:
            maxCatThreshold: limit number of split points considered for categorical features
        """
    def setMaxCatToOnehot(self, value):
        """
        Args:
            maxCatToOnehot: when number of categories of one feature smaller than or equal to this, one-vs-other split algorithm will be used
        """
    def setMaxDeltaStep(self, value):
        """
        Args:
            maxDeltaStep: Used to limit the max output of tree leaves
        """
    def setMaxDepth(self, value):
        """
        Args:
            maxDepth: Max depth
        """
    def setMaxDrop(self, value):
        """
        Args:
            maxDrop: Max number of dropped trees during one boosting iteration
        """
    def setMaxNumClasses(self, value):
        """
        Args:
            maxNumClasses: Number of max classes to infer numClass in multi-class classification.
        """
    def setMaxStreamingOMPThreads(self, value):
        """
        Args:
            maxStreamingOMPThreads: Maximum number of OpenMP threads used by a LightGBM thread. Used only for thread-safe buffer allocation. Use -1 to use OpenMP default, but in a Spark environment it's best to set a fixed value.
        """
    def setMetric(self, value):
        """
        Args:
            metric: Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. 
        """
    def setMicroBatchSize(self, value):
        """
        Args:
            microBatchSize: Specify how many elements are sent in a streaming micro-batch.
        """
    def setMinDataInLeaf(self, value):
        """
        Args:
            minDataInLeaf: Minimal number of data in one leaf. Can be used to deal with over-fitting.
        """
    def setMinDataPerBin(self, value):
        """
        Args:
            minDataPerBin: Minimal number of data inside one bin
        """
    def setMinDataPerGroup(self, value):
        """
        Args:
            minDataPerGroup: minimal number of data per categorical group
        """
    def setMinGainToSplit(self, value):
        """
        Args:
            minGainToSplit: The minimal gain to perform split
        """
    def setMinSumHessianInLeaf(self, value):
        """
        Args:
            minSumHessianInLeaf: Minimal sum hessian in one leaf
        """
    def setModelString(self, value):
        """
        Args:
            modelString: LightGBM model to retrain
        """
    def setMonotoneConstraints(self, value):
        """
        Args:
            monotoneConstraints: used for constraints of monotonic features. 1 means increasing, -1 means decreasing, 0 means non-constraint. Specify all features in order.
        """
    def setMonotoneConstraintsMethod(self, value):
        """
        Args:
            monotoneConstraintsMethod: Monotone constraints method. basic, intermediate, or advanced.
        """
    def setMonotonePenalty(self, value):
        """
        Args:
            monotonePenalty: A penalization parameter X forbids any monotone splits on the first X (rounded down) level(s) of the tree.
        """
    def setNegBaggingFraction(self, value):
        """
        Args:
            negBaggingFraction: Negative Bagging fraction
        """
    def setNumBatches(self, value):
        """
        Args:
            numBatches: If greater than 0, splits data into separate batches during training
        """
    def setNumIterations(self, value):
        """
        Args:
            numIterations: Number of iterations, LightGBM constructs num_class * num_iterations trees
        """
    def setNumLeaves(self, value):
        """
        Args:
            numLeaves: Number of leaves
        """
    def setNumTasks(self, value):
        """
        Args:
            numTasks: Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.
        """
    def setNumThreads(self, value):
        """
        Args:
            numThreads: Number of threads per executor for LightGBM. For the best speed, set this to the number of real CPU cores.
        """
    def setObjective(self, value):
        """
        Args:
            objective: The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. 
        """
    def setObjectiveSeed(self, value):
        """
        Args:
            objectiveSeed: Random seed for objectives, if random process is needed.  Currently used only for rank_xendcg objective.
        """
    def setOtherRate(self, value):
        """
        Args:
            otherRate: The retain ratio of small gradient data. Only used in goss.
        """
    def setParallelism(self, value):
        """
        Args:
            parallelism: Tree learner parallelism, can be set to data_parallel or voting_parallel
        """
    def setPassThroughArgs(self, value):
        """
        Args:
            passThroughArgs: Direct string to pass through to LightGBM library (appended with other explicitly set params). Will override any parameters given with explicit setters. Can include multiple parameters in one string. e.g., force_row_wise=true
        """
    def setPosBaggingFraction(self, value):
        """
        Args:
            posBaggingFraction: Positive Bagging fraction
        """
    def setPredictDisableShapeCheck(self, value):
        """
        Args:
            predictDisableShapeCheck: control whether or not LightGBM raises an error when you try to predict on data with a different number of features than the training data
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
    def setReferenceDataset(self, value):
        """
        Args:
            referenceDataset: The reference Dataset that was used for the fit. If using samplingMode=custom, this must be set before fit().
        """
    def setRepartitionByGroupingColumn(self, value):
        """
        Args:
            repartitionByGroupingColumn: Repartition training data according to grouping column, on by default.
        """
    def setSamplingMode(self, value):
        """
        Args:
            samplingMode: Data sampling for streaming mode. Sampled data is used to define bins. 'global': sample from all data, 'subset': sample from first N rows, or 'fixed': Take first N rows as sample.Values can be global, subset, or fixed. Default is subset.
        """
    def setSamplingSubsetSize(self, value):
        """
        Args:
            samplingSubsetSize: Specify subset size N for the sampling mode 'subset'. 'binSampleCount' rows will be chosen from the first N values of the dataset. Subset can be used when rows are expected to be random and data is huge.
        """
    def setSeed(self, value):
        """
        Args:
            seed: Main seed, used to generate other seeds
        """
    def setSkipDrop(self, value):
        """
        Args:
            skipDrop: Probability of skipping the dropout procedure during a boosting iteration
        """
    def setSlotNames(self, value):
        """
        Args:
            slotNames: List of slot names in the features column
        """
    def setTimeout(self, value):
        """
        Args:
            timeout: Timeout in seconds
        """
    def setTopK(self, value):
        """
        Args:
            topK: The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0
        """
    def setTopRate(self, value):
        """
        Args:
            topRate: The retain ratio of large gradient data. Only used in goss.
        """
    def setTweedieVariancePower(self, value):
        """
        Args:
            tweedieVariancePower: control the variance of tweedie distribution, must be between 1 and 2
        """
    def setUniformDrop(self, value):
        """
        Args:
            uniformDrop: Set this to true to use uniform drop in dart mode
        """
    def setUseBarrierExecutionMode(self, value):
        """
        Args:
            useBarrierExecutionMode: Barrier execution mode which uses a barrier stage, off by default.
        """
    def setUseMissing(self, value):
        """
        Args:
            useMissing: Set this to false to disable the special handle of missing value
        """
    def setUseSingleDatasetMode(self, value):
        """
        Args:
            useSingleDatasetMode: Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead.
        """
    def setValidationIndicatorCol(self, value):
        """
        Args:
            validationIndicatorCol: Indicates whether the row is for training or validation
        """
    def setVerbosity(self, value):
        """
        Args:
            verbosity: Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug
        """
    def setWeightCol(self, value):
        """
        Args:
            weightCol: The name of the weight column
        """
    def setXGBoostDartMode(self, value):
        """
        Args:
            xGBoostDartMode: Set this to true to use xgboost dart mode
        """
    def setZeroAsMissing(self, value):
        """
        Args:
            zeroAsMissing: Set to true to treat all zero as missing values (including the unshown values in LibSVM / sparse matrices). Set to false to use na for representing missing values
        """
    def getAlpha(self):
        """
        Returns:
            alpha: parameter for Huber loss and Quantile regression
        """
    def getBaggingFraction(self):
        """
        Returns:
            baggingFraction: Bagging fraction
        """
    def getBaggingFreq(self):
        """
        Returns:
            baggingFreq: Bagging frequency
        """
    def getBaggingSeed(self):
        """
        Returns:
            baggingSeed: Bagging seed
        """
    def getBinSampleCount(self):
        """
        Returns:
            binSampleCount: Number of samples considered at computing histogram bins
        """
    def getBoostFromAverage(self):
        """
        Returns:
            boostFromAverage: Adjusts initial score to the mean of labels for faster convergence
        """
    def getBoostingType(self):
        """
        Returns:
            boostingType: Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). 
        """
    def getCatSmooth(self):
        """
        Returns:
            catSmooth: this can reduce the effect of noises in categorical features, especially for categories with few data
        """
    def getCategoricalSlotIndexes(self):
        """
        Returns:
            categoricalSlotIndexes: List of categorical column indexes, the slot index in the features column
        """
    def getCategoricalSlotNames(self):
        """
        Returns:
            categoricalSlotNames: List of categorical column slot names, the slot name in the features column
        """
    def getCatl2(self):
        """
        Returns:
            catl2: L2 regularization in categorical split
        """
    def getChunkSize(self):
        """
        Returns:
            chunkSize: Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.
        """
    def getDataRandomSeed(self):
        """
        Returns:
            dataRandomSeed: Random seed for sampling data to construct histogram bins.
        """
    def getDataTransferMode(self):
        """
        Returns:
            dataTransferMode: Specify how SynapseML transfers data from Spark to LightGBM.  Values can be streaming, bulk. Default is bulk, which is the legacy mode.
        """
    def getDefaultListenPort(self):
        """
        Returns:
            defaultListenPort: The default listen port on executors, used for testing
        """
    def getDeterministic(self):
        """
        Returns:
            deterministic: Used only with cpu devide type. Setting this to true should ensure stable results when using the same data and the same parameters.  Note: setting this to true may slow down training.  To avoid potential instability due to numerical issues, please set force_col_wise=true or force_row_wise=true when setting deterministic=true
        """
    def getDriverListenPort(self):
        """
        Returns:
            driverListenPort: The listen port on a driver. Default value is 0 (random)
        """
    def getDropRate(self):
        """
        Returns:
            dropRate: Dropout rate: a fraction of previous trees to drop during the dropout
        """
    def getDropSeed(self):
        """
        Returns:
            dropSeed: Random seed to choose dropping models. Only used in dart.
        """
    def getEarlyStoppingRound(self):
        """
        Returns:
            earlyStoppingRound: Early stopping round
        """
    def getExecutionMode(self):
        """
        Returns:
            executionMode: Deprecated. Please use dataTransferMode.
        """
    def getExtraSeed(self):
        """
        Returns:
            extraSeed: Random seed for selecting threshold when extra_trees is true
        """
    def getFeatureFraction(self):
        """
        Returns:
            featureFraction: Feature fraction
        """
    def getFeatureFractionByNode(self):
        """
        Returns:
            featureFractionByNode: Feature fraction by node
        """
    def getFeatureFractionSeed(self):
        """
        Returns:
            featureFractionSeed: Feature fraction seed
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: features column name
        """
    def getFeaturesShapCol(self):
        """
        Returns:
            featuresShapCol: Output SHAP vector column name after prediction containing the feature contribution values
        """
    def getFobj(self):
        """
        Returns:
            fobj: Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).
        """
    def getImprovementTolerance(self):
        """
        Returns:
            improvementTolerance: Tolerance to consider improvement in metric
        """
    def getInitScoreCol(self):
        """
        Returns:
            initScoreCol: The name of the initial score column, used for continued training
        """
    def getIsEnableSparse(self):
        """
        Returns:
            isEnableSparse: Used to enable/disable sparse optimization
        """
    def getIsProvideTrainingMetric(self):
        """
        Returns:
            isProvideTrainingMetric: Whether output metric result over training dataset.
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getLambdaL1(self):
        """
        Returns:
            lambdaL1: L1 regularization
        """
    def getLambdaL2(self):
        """
        Returns:
            lambdaL2: L2 regularization
        """
    def getLeafPredictionCol(self):
        """
        Returns:
            leafPredictionCol: Predicted leaf indices's column name
        """
    def getLearningRate(self):
        """
        Returns:
            learningRate: Learning rate or shrinkage rate
        """
    def getMatrixType(self):
        """
        Returns:
            matrixType: Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.
        """
    def getMaxBin(self):
        """
        Returns:
            maxBin: Max bin
        """
    def getMaxBinByFeature(self):
        """
        Returns:
            maxBinByFeature: Max number of bins for each feature
        """
    def getMaxCatThreshold(self):
        """
        Returns:
            maxCatThreshold: limit number of split points considered for categorical features
        """
    def getMaxCatToOnehot(self):
        """
        Returns:
            maxCatToOnehot: when number of categories of one feature smaller than or equal to this, one-vs-other split algorithm will be used
        """
    def getMaxDeltaStep(self):
        """
        Returns:
            maxDeltaStep: Used to limit the max output of tree leaves
        """
    def getMaxDepth(self):
        """
        Returns:
            maxDepth: Max depth
        """
    def getMaxDrop(self):
        """
        Returns:
            maxDrop: Max number of dropped trees during one boosting iteration
        """
    def getMaxNumClasses(self):
        """
        Returns:
            maxNumClasses: Number of max classes to infer numClass in multi-class classification.
        """
    def getMaxStreamingOMPThreads(self):
        """
        Returns:
            maxStreamingOMPThreads: Maximum number of OpenMP threads used by a LightGBM thread. Used only for thread-safe buffer allocation. Use -1 to use OpenMP default, but in a Spark environment it's best to set a fixed value.
        """
    def getMetric(self):
        """
        Returns:
            metric: Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. 
        """
    def getMicroBatchSize(self):
        """
        Returns:
            microBatchSize: Specify how many elements are sent in a streaming micro-batch.
        """
    def getMinDataInLeaf(self):
        """
        Returns:
            minDataInLeaf: Minimal number of data in one leaf. Can be used to deal with over-fitting.
        """
    def getMinDataPerBin(self):
        """
        Returns:
            minDataPerBin: Minimal number of data inside one bin
        """
    def getMinDataPerGroup(self):
        """
        Returns:
            minDataPerGroup: minimal number of data per categorical group
        """
    def getMinGainToSplit(self):
        """
        Returns:
            minGainToSplit: The minimal gain to perform split
        """
    def getMinSumHessianInLeaf(self):
        """
        Returns:
            minSumHessianInLeaf: Minimal sum hessian in one leaf
        """
    def getModelString(self):
        """
        Returns:
            modelString: LightGBM model to retrain
        """
    def getMonotoneConstraints(self):
        """
        Returns:
            monotoneConstraints: used for constraints of monotonic features. 1 means increasing, -1 means decreasing, 0 means non-constraint. Specify all features in order.
        """
    def getMonotoneConstraintsMethod(self):
        """
        Returns:
            monotoneConstraintsMethod: Monotone constraints method. basic, intermediate, or advanced.
        """
    def getMonotonePenalty(self):
        """
        Returns:
            monotonePenalty: A penalization parameter X forbids any monotone splits on the first X (rounded down) level(s) of the tree.
        """
    def getNegBaggingFraction(self):
        """
        Returns:
            negBaggingFraction: Negative Bagging fraction
        """
    def getNumBatches(self):
        """
        Returns:
            numBatches: If greater than 0, splits data into separate batches during training
        """
    def getNumIterations(self):
        """
        Returns:
            numIterations: Number of iterations, LightGBM constructs num_class * num_iterations trees
        """
    def getNumLeaves(self):
        """
        Returns:
            numLeaves: Number of leaves
        """
    def getNumTasks(self):
        """
        Returns:
            numTasks: Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.
        """
    def getNumThreads(self):
        """
        Returns:
            numThreads: Number of threads per executor for LightGBM. For the best speed, set this to the number of real CPU cores.
        """
    def getObjective(self):
        """
        Returns:
            objective: The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. 
        """
    def getObjectiveSeed(self):
        """
        Returns:
            objectiveSeed: Random seed for objectives, if random process is needed.  Currently used only for rank_xendcg objective.
        """
    def getOtherRate(self):
        """
        Returns:
            otherRate: The retain ratio of small gradient data. Only used in goss.
        """
    def getParallelism(self):
        """
        Returns:
            parallelism: Tree learner parallelism, can be set to data_parallel or voting_parallel
        """
    def getPassThroughArgs(self):
        """
        Returns:
            passThroughArgs: Direct string to pass through to LightGBM library (appended with other explicitly set params). Will override any parameters given with explicit setters. Can include multiple parameters in one string. e.g., force_row_wise=true
        """
    def getPosBaggingFraction(self):
        """
        Returns:
            posBaggingFraction: Positive Bagging fraction
        """
    def getPredictDisableShapeCheck(self):
        """
        Returns:
            predictDisableShapeCheck: control whether or not LightGBM raises an error when you try to predict on data with a different number of features than the training data
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
    def getReferenceDataset(self):
        """
        Returns:
            referenceDataset: The reference Dataset that was used for the fit. If using samplingMode=custom, this must be set before fit().
        """
    def getRepartitionByGroupingColumn(self):
        """
        Returns:
            repartitionByGroupingColumn: Repartition training data according to grouping column, on by default.
        """
    def getSamplingMode(self):
        """
        Returns:
            samplingMode: Data sampling for streaming mode. Sampled data is used to define bins. 'global': sample from all data, 'subset': sample from first N rows, or 'fixed': Take first N rows as sample.Values can be global, subset, or fixed. Default is subset.
        """
    def getSamplingSubsetSize(self):
        """
        Returns:
            samplingSubsetSize: Specify subset size N for the sampling mode 'subset'. 'binSampleCount' rows will be chosen from the first N values of the dataset. Subset can be used when rows are expected to be random and data is huge.
        """
    def getSeed(self):
        """
        Returns:
            seed: Main seed, used to generate other seeds
        """
    def getSkipDrop(self):
        """
        Returns:
            skipDrop: Probability of skipping the dropout procedure during a boosting iteration
        """
    def getSlotNames(self):
        """
        Returns:
            slotNames: List of slot names in the features column
        """
    def getTimeout(self):
        """
        Returns:
            timeout: Timeout in seconds
        """
    def getTopK(self):
        """
        Returns:
            topK: The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0
        """
    def getTopRate(self):
        """
        Returns:
            topRate: The retain ratio of large gradient data. Only used in goss.
        """
    def getTweedieVariancePower(self):
        """
        Returns:
            tweedieVariancePower: control the variance of tweedie distribution, must be between 1 and 2
        """
    def getUniformDrop(self):
        """
        Returns:
            uniformDrop: Set this to true to use uniform drop in dart mode
        """
    def getUseBarrierExecutionMode(self):
        """
        Returns:
            useBarrierExecutionMode: Barrier execution mode which uses a barrier stage, off by default.
        """
    def getUseMissing(self):
        """
        Returns:
            useMissing: Set this to false to disable the special handle of missing value
        """
    def getUseSingleDatasetMode(self):
        """
        Returns:
            useSingleDatasetMode: Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead.
        """
    def getValidationIndicatorCol(self):
        """
        Returns:
            validationIndicatorCol: Indicates whether the row is for training or validation
        """
    def getVerbosity(self):
        """
        Returns:
            verbosity: Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug
        """
    def getWeightCol(self):
        """
        Returns:
            weightCol: The name of the weight column
        """
    def getXGBoostDartMode(self):
        """
        Returns:
            xGBoostDartMode: Set this to true to use xgboost dart mode
        """
    def getZeroAsMissing(self):
        """
        Returns:
            zeroAsMissing: Set to true to treat all zero as missing values (including the unshown values in LibSVM / sparse matrices). Set to false to use na for representing missing values
        """
