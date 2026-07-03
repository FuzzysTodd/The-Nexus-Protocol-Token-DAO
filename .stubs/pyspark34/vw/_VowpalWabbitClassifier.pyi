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

class _VowpalWabbitClassifier(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        additionalFeatures (list): Additional feature columns
        featuresCol (str): features column name
        hashSeed (int): Seed used for hashing
        ignoreNamespaces (str): Namespaces to be ignored (first letter only)
        initialModel (list): Initial model to start from
        interactions (list): Interaction terms as specified by -q
        l1 (float): l_1 lambda
        l2 (float): l_2 lambda
        labelCol (str): label column name
        labelConversion (bool): Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to false.
        learningRate (float): Learning rate
        numBits (int): Number of bits used
        numClasses (int): Number of classes. Defaults to binary. Needs to match oaa/csoaa/multilabel_oaa/...
        numPasses (int): Number of passes over the data
        numSyncsPerPass (int): Number of times weights should be synchronized within each pass. 0 disables inter-pass synchronization.
        passThroughArgs (str): VW command line arguments passed
        powerT (float): t power value
        predictionCol (str): prediction column name
        predictionIdCol (str): The ID column returned for predictions
        probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        rawPredictionCol (str): raw prediction (a.k.a. confidence) column name
        splitCol (str): The column to split on for inter-pass sync
        splitColValues (list): Sorted values to use to select each split to train on. If not specified, computed from data
        thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        useBarrierExecutionMode (bool): Use barrier execution mode, on by default.
        weightCol (str): The name of the weight column
    """
    additionalFeatures: Incomplete
    featuresCol: Incomplete
    hashSeed: Incomplete
    ignoreNamespaces: Incomplete
    initialModel: Incomplete
    interactions: Incomplete
    l1: Incomplete
    l2: Incomplete
    labelCol: Incomplete
    labelConversion: Incomplete
    learningRate: Incomplete
    numBits: Incomplete
    numClasses: Incomplete
    numPasses: Incomplete
    numSyncsPerPass: Incomplete
    passThroughArgs: Incomplete
    powerT: Incomplete
    predictionCol: Incomplete
    predictionIdCol: Incomplete
    probabilityCol: Incomplete
    rawPredictionCol: Incomplete
    splitCol: Incomplete
    splitColValues: Incomplete
    thresholds: Incomplete
    useBarrierExecutionMode: Incomplete
    weightCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, additionalFeatures=[], featuresCol: str = 'features', hashSeed: int = 0, ignoreNamespaces: Incomplete | None = None, initialModel: Incomplete | None = None, interactions: Incomplete | None = None, l1: Incomplete | None = None, l2: Incomplete | None = None, labelCol: str = 'label', labelConversion: bool = False, learningRate: Incomplete | None = None, numBits: int = 18, numClasses: int = 2, numPasses: int = 1, numSyncsPerPass: int = 0, passThroughArgs: str = '', powerT: Incomplete | None = None, predictionCol: str = 'prediction', predictionIdCol: Incomplete | None = None, probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', splitCol: Incomplete | None = None, splitColValues: Incomplete | None = None, thresholds: Incomplete | None = None, useBarrierExecutionMode: bool = True, weightCol: Incomplete | None = None) -> None: ...
    def setParams(self, additionalFeatures=[], featuresCol: str = 'features', hashSeed: int = 0, ignoreNamespaces: Incomplete | None = None, initialModel: Incomplete | None = None, interactions: Incomplete | None = None, l1: Incomplete | None = None, l2: Incomplete | None = None, labelCol: str = 'label', labelConversion: bool = False, learningRate: Incomplete | None = None, numBits: int = 18, numClasses: int = 2, numPasses: int = 1, numSyncsPerPass: int = 0, passThroughArgs: str = '', powerT: Incomplete | None = None, predictionCol: str = 'prediction', predictionIdCol: Incomplete | None = None, probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', splitCol: Incomplete | None = None, splitColValues: Incomplete | None = None, thresholds: Incomplete | None = None, useBarrierExecutionMode: bool = True, weightCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAdditionalFeatures(self, value):
        """
        Args:
            additionalFeatures: Additional feature columns
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: features column name
        """
    def setHashSeed(self, value):
        """
        Args:
            hashSeed: Seed used for hashing
        """
    def setIgnoreNamespaces(self, value):
        """
        Args:
            ignoreNamespaces: Namespaces to be ignored (first letter only)
        """
    def setInitialModel(self, value):
        """
        Args:
            initialModel: Initial model to start from
        """
    def setInteractions(self, value):
        """
        Args:
            interactions: Interaction terms as specified by -q
        """
    def setL1(self, value):
        """
        Args:
            l1: l_1 lambda
        """
    def setL2(self, value):
        """
        Args:
            l2: l_2 lambda
        """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
    def setLabelConversion(self, value):
        """
        Args:
            labelConversion: Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to false.
        """
    def setLearningRate(self, value):
        """
        Args:
            learningRate: Learning rate
        """
    def setNumBits(self, value):
        """
        Args:
            numBits: Number of bits used
        """
    def setNumClasses(self, value):
        """
        Args:
            numClasses: Number of classes. Defaults to binary. Needs to match oaa/csoaa/multilabel_oaa/...
        """
    def setNumPasses(self, value):
        """
        Args:
            numPasses: Number of passes over the data
        """
    def setNumSyncsPerPass(self, value):
        """
        Args:
            numSyncsPerPass: Number of times weights should be synchronized within each pass. 0 disables inter-pass synchronization.
        """
    def setPassThroughArgs(self, value):
        """
        Args:
            passThroughArgs: VW command line arguments passed
        """
    def setPowerT(self, value):
        """
        Args:
            powerT: t power value
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
    def setPredictionIdCol(self, value):
        """
        Args:
            predictionIdCol: The ID column returned for predictions
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
    def setSplitCol(self, value):
        """
        Args:
            splitCol: The column to split on for inter-pass sync
        """
    def setSplitColValues(self, value):
        """
        Args:
            splitColValues: Sorted values to use to select each split to train on. If not specified, computed from data
        """
    def setThresholds(self, value):
        """
        Args:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
    def setUseBarrierExecutionMode(self, value):
        """
        Args:
            useBarrierExecutionMode: Use barrier execution mode, on by default.
        """
    def setWeightCol(self, value):
        """
        Args:
            weightCol: The name of the weight column
        """
    def getAdditionalFeatures(self):
        """
        Returns:
            additionalFeatures: Additional feature columns
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: features column name
        """
    def getHashSeed(self):
        """
        Returns:
            hashSeed: Seed used for hashing
        """
    def getIgnoreNamespaces(self):
        """
        Returns:
            ignoreNamespaces: Namespaces to be ignored (first letter only)
        """
    def getInitialModel(self):
        """
        Returns:
            initialModel: Initial model to start from
        """
    def getInteractions(self):
        """
        Returns:
            interactions: Interaction terms as specified by -q
        """
    def getL1(self):
        """
        Returns:
            l1: l_1 lambda
        """
    def getL2(self):
        """
        Returns:
            l2: l_2 lambda
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getLabelConversion(self):
        """
        Returns:
            labelConversion: Convert 0/1 Spark ML style labels to -1/1 VW style labels. Defaults to false.
        """
    def getLearningRate(self):
        """
        Returns:
            learningRate: Learning rate
        """
    def getNumBits(self):
        """
        Returns:
            numBits: Number of bits used
        """
    def getNumClasses(self):
        """
        Returns:
            numClasses: Number of classes. Defaults to binary. Needs to match oaa/csoaa/multilabel_oaa/...
        """
    def getNumPasses(self):
        """
        Returns:
            numPasses: Number of passes over the data
        """
    def getNumSyncsPerPass(self):
        """
        Returns:
            numSyncsPerPass: Number of times weights should be synchronized within each pass. 0 disables inter-pass synchronization.
        """
    def getPassThroughArgs(self):
        """
        Returns:
            passThroughArgs: VW command line arguments passed
        """
    def getPowerT(self):
        """
        Returns:
            powerT: t power value
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
    def getPredictionIdCol(self):
        """
        Returns:
            predictionIdCol: The ID column returned for predictions
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
    def getSplitCol(self):
        """
        Returns:
            splitCol: The column to split on for inter-pass sync
        """
    def getSplitColValues(self):
        """
        Returns:
            splitColValues: Sorted values to use to select each split to train on. If not specified, computed from data
        """
    def getThresholds(self):
        """
        Returns:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
    def getUseBarrierExecutionMode(self):
        """
        Returns:
            useBarrierExecutionMode: Use barrier execution mode, on by default.
        """
    def getWeightCol(self):
        """
        Returns:
            weightCol: The name of the weight column
        """
