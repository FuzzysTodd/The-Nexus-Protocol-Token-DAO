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

class _VowpalWabbitClassificationModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        additionalFeatures (list): Additional feature columns
        featuresCol (str): features column name
        labelCol (str): label column name
        model (list): The VW model....
        numClassesModel (int): Number of classes.
        oneStepAheadPredictions (object): 1-step ahead predictions collected during training
        performanceStatistics (object): Performance statistics collected during training
        predictionCol (str): prediction column name
        probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        rawPredictionCol (str): raw prediction (a.k.a. confidence) column name
        testArgs (str): Additional arguments passed to VW at test time
        thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
    """
    additionalFeatures: Incomplete
    featuresCol: Incomplete
    labelCol: Incomplete
    model: Incomplete
    numClassesModel: Incomplete
    oneStepAheadPredictions: Incomplete
    performanceStatistics: Incomplete
    predictionCol: Incomplete
    probabilityCol: Incomplete
    rawPredictionCol: Incomplete
    testArgs: Incomplete
    thresholds: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, additionalFeatures: Incomplete | None = None, featuresCol: str = 'features', labelCol: str = 'label', model: Incomplete | None = None, numClassesModel: Incomplete | None = None, oneStepAheadPredictions: Incomplete | None = None, performanceStatistics: Incomplete | None = None, predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', testArgs: str = '', thresholds: Incomplete | None = None) -> None: ...
    def setParams(self, additionalFeatures: Incomplete | None = None, featuresCol: str = 'features', labelCol: str = 'label', model: Incomplete | None = None, numClassesModel: Incomplete | None = None, oneStepAheadPredictions: Incomplete | None = None, performanceStatistics: Incomplete | None = None, predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', testArgs: str = '', thresholds: Incomplete | None = None):
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
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
    def setModel(self, value):
        """
        Args:
            model: The VW model....
        """
    def setNumClassesModel(self, value):
        """
        Args:
            numClassesModel: Number of classes.
        """
    def setOneStepAheadPredictions(self, value):
        """
        Args:
            oneStepAheadPredictions: 1-step ahead predictions collected during training
        """
    def setPerformanceStatistics(self, value):
        """
        Args:
            performanceStatistics: Performance statistics collected during training
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
    def setTestArgs(self, value):
        """
        Args:
            testArgs: Additional arguments passed to VW at test time
        """
    def setThresholds(self, value):
        """
        Args:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
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
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getModel(self):
        """
        Returns:
            model: The VW model....
        """
    def getNumClassesModel(self):
        """
        Returns:
            numClassesModel: Number of classes.
        """
    def getOneStepAheadPredictions(self):
        """
        Returns:
            oneStepAheadPredictions: 1-step ahead predictions collected during training
        """
    def getPerformanceStatistics(self):
        """
        Returns:
            performanceStatistics: Performance statistics collected during training
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
    def getTestArgs(self):
        """
        Returns:
            testArgs: Additional arguments passed to VW at test time
        """
    def getThresholds(self):
        """
        Returns:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
