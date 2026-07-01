from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from py4j.java_collections import ListConverter as ListConverter, MapConverter as MapConverter, SetConverter as SetConverter
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter
from synapse.ml.ebm._VisualizationModelWrap import _ClassificationWrap
from typing import List

basestring = str

class EbmClassificationModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        binSamplingSeed (long): The random seed used in the process for finding the thresholds to discretize continuous features.
        checkpointFrequency (int): Perform a checkpoint on the accumulated predictions after every this many rounds of boosting. If zero, no checkpointing will be done, which requires that all rounds have their predictions in memory.
        earlyStoppingRound (int): Number of rounds of no improvement to trigger early stopping.
        featureScoresCol (str): Feature scores column name
        featuresCol (str): features column name
        featuresInGroup (int): Max number of features to put into a single-round boosting group.
        improvementTolerance (float): Tolerance that dictates the smallest delta required to be considered an improvement when considering early stopping.
        innerBaggedSamples (int): If non-zero, learn each adjustment to the feature function over the average of this many a quasi-bagged samples.
        labelCol (str): label column name
        learningRate (float): Scale each update by this amount.
        maxBins (int): Max number of bins for discretizing continuous features.  Must be at least 2 and at least number of categories for any categorical feature.
        maxInteractionBins (int): Max number of bins for discretizing continuous features, for the purpose specifically of pairwise interactions. This should be less than `maxBins`.
        numInteractionPairs (int): The maximum number of pairs of features to consider for interaction functions.
        maxInteractionRounds (int): Perform this many iterations on pairwise interactions.
        maxRounds (int): Perform this many iterations on main features
        mbInChunk (float): During the initial phase of dataset preparation, try to keep the chunks of data at around about this threshold, as measured in MiB. Note that this is a threshold not a lower bound.
        minSplit (int): Ensure that at least this many instances lie on one side of a split when considering splits.
        outerBaggedSamples (int): If non-zero, learns effectively multiple models.
        predictionCol (str): prediction column name
        probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        rawPredictionCol (str): raw prediction (a.k.a. confidence) column name
        sampleSeed (int): Additional salt for sampling seeds.
        splits (int): When learning the local functions, in each round of each sample, perform this many splits.
        thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        validationIndicatorCol (str): name of the column that indicates whether each row is for training or for validation. False indicates training; true indicates validation.
        weightCol (str): weight column name. If this is not set or empty, we treat all instance weights as 1.0
    """
    binSamplingSeed: Incomplete
    checkpointFrequency: Incomplete
    earlyStoppingRound: Incomplete
    featureScoresCol: Incomplete
    featuresCol: Incomplete
    featuresInGroup: Incomplete
    improvementTolerance: Incomplete
    innerBaggedSamples: Incomplete
    labelCol: Incomplete
    learningRate: Incomplete
    maxBins: Incomplete
    maxInteractionBins: Incomplete
    numInteractionPairs: Incomplete
    maxInteractionRounds: Incomplete
    maxRounds: Incomplete
    mbInChunk: Incomplete
    minSplit: Incomplete
    outerBaggedSamples: Incomplete
    predictionCol: Incomplete
    probabilityCol: Incomplete
    rawPredictionCol: Incomplete
    sampleSeed: Incomplete
    splits: Incomplete
    thresholds: Incomplete
    validationIndicatorCol: Incomplete
    weightCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, binSamplingSeed: int = 1, checkpointFrequency: int = 10, earlyStoppingRound: int = 50, featureScoresCol: str = '', featuresCol: str = 'features', featuresInGroup: int = 1, improvementTolerance: float = 0.0, innerBaggedSamples: int = 50, labelCol: str = 'label', learningRate: float = 0.1, maxBins: int = 256, maxInteractionBins: int = 32, numInteractionPairs: int = 10, maxInteractionRounds: int = 100, maxRounds: int = 100, mbInChunk: float = 100.0, minSplit: int = 1, outerBaggedSamples: int = 8, predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', sampleSeed: int = 0, splits: int = 3, thresholds: Incomplete | None = None, validationIndicatorCol: Incomplete | None = None, weightCol: Incomplete | None = None) -> None: ...
    def setParams(self, binSamplingSeed: int = 1, checkpointFrequency: int = 10, earlyStoppingRound: int = 50, featureScoresCol: str = '', featuresCol: str = 'features', featuresInGroup: int = 1, improvementTolerance: float = 0.0, innerBaggedSamples: int = 50, labelCol: str = 'label', learningRate: float = 0.1, maxBins: int = 256, maxInteractionBins: int = 32, numInteractionPairs: int = 10, maxInteractionRounds: int = 100, maxRounds: int = 100, mbInChunk: float = 100.0, minSplit: int = 1, outerBaggedSamples: int = 8, predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', sampleSeed: int = 0, splits: int = 3, thresholds: Incomplete | None = None, validationIndicatorCol: Incomplete | None = None, weightCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setFeatureScoresCol(self, value):
        """
        Args:
            featureScoresCol: Feature scores column name
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: features column name
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
    def setProbabilityCol(self, value):
        """
        Args:
            probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        """
    def setRawPredictionCol(self, value):
        """
        Args:
            rawPredictionCol: raw prediction (a.k.a. confidence) column name
        """
    def setThresholds(self, value):
        """
        Args:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
    def getBinSamplingSeed(self):
        """
        Returns:
            binSamplingSeed: The random seed used in the process for finding the thresholds to discretize continuous features.
        """
    def getCheckpointFrequency(self):
        """
        Returns:
            checkpointFrequency: Perform a checkpoint on the accumulated predictions after every this many rounds of boosting. If zero, no checkpointing will be done, which requires that all rounds have their predictions in memory.
        """
    def getEarlyStoppingRound(self):
        """
        Returns:
            earlyStoppingRound: Number of rounds of no improvement to trigger early stopping.
        """
    def getFeatureScoresCol(self):
        """
        Returns:
            featureScoresCol: Feature scores column name
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: features column name
        """
    def getFeaturesInGroup(self):
        """
        Returns:
            featuresInGroup: Max number of features to put into a single-round boosting group.
        """
    def getImprovementTolerance(self):
        """
        Returns:
            improvementTolerance: Tolerance that dictates the smallest delta required to be considered an improvement when considering early stopping.
        """
    def getInnerBaggedSamples(self):
        """
        Returns:
            innerBaggedSamples: If non-zero, learn each adjustment to the feature function over the average of this many a quasi-bagged samples.
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getLearningRate(self):
        """
        Returns:
            learningRate: Scale each update by this amount.
        """
    def getMaxBins(self):
        """
        Returns:
            maxBins: Max number of bins for discretizing continuous features.  Must be at least 2 and at least number of categories for any categorical feature.
        """
    def getMaxInteractionBins(self):
        """
        Returns:
            maxInteractionBins: Max number of bins for discretizing continuous features, for the purpose specifically of pairwise interactions. This should be less than `maxBins`.
        """
    def getMaxInteractionRounds(self):
        """
        Returns:
            maxInteractionRounds: Perform this many iterations on pairwise interactions.
        """
    def getMaxRounds(self):
        """
        Returns:
            maxRounds: Perform this many iterations on main features
        """
    def getMbInChunk(self):
        """
        Returns:
            mbInChunk: During the initial phase of dataset preparation, try to keep the chunks of data at around about this threshold, as measured in MiB. Note that this is a threshold not a lower bound.
        """
    def getMinSplit(self):
        """
        Returns:
            minSplit: Ensure that at least this many instances lie on one side of a split when considering splits.
        """
    def getOuterBaggedSamples(self):
        """
        Returns:
            outerBaggedSamples: If non-zero, learns effectively multiple models.
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
    def getProbabilityCol(self):
        """
        Returns:
            probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        """
    def getRawPredictionCol(self):
        """
        Returns:
            rawPredictionCol: raw prediction (a.k.a. confidence) column name
        """
    def getSampleSeed(self):
        """
        Returns:
            sampleSeed: Additional salt for sampling seeds.
        """
    def getSplits(self):
        """
        Returns:
            splits: When learning the local functions, in each round of each sample, perform this many splits.
        """
    def getThresholds(self):
        """
        Returns:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
    def getValidationIndicatorCol(self):
        """
        Returns:
            validationIndicatorCol: name of the column that indicates whether each row is for training or for validation. False indicates training; true indicates validation.
        """
    def getWeightCol(self):
        """
        Returns:
            weightCol: weight column name. If this is not set or empty, we treat all instance weights as 1.0
        """
    def getVizWrapper(self) -> _ClassificationWrap: ...
    @property
    def numClasses(self) -> int: ...
    @property
    def numFeatures(self) -> int: ...
    def validationLossPerRound(self) -> List[float] | None: ...
    def trainingLossPerRound(self) -> List[float]: ...
    def bestRound(self) -> int | None: ...
    def featureScoresMean(self) -> List[float]: ...
    def featureImportances(self) -> List[float]: ...
    def binWeights(self, fIdx: int) -> List[float]: ...
    def binCounts(self, fIdx: int) -> List[int]: ...
    def featureMaxes(self) -> List[float]: ...
    def featureMins(self) -> List[float]: ...
    def featureNames(self) -> List[str] | None: ...
    def stddevForBin(self, fIdx: int) -> List[float] | None: ...
    def valuesForBin(self, fIdx: int) -> List[float]: ...
    def numBins(self, fIdx: int) -> int: ...
    def featureOffsets(self) -> List[float]: ...
    @property
    def offset(self) -> float: ...
    def binThresholds(self, fIdx: int) -> List[float] | None: ...
