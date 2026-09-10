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

class _VowpalWabbitRegressionModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        additionalFeatures (list): Additional feature columns
        featuresCol (str): features column name
        labelCol (str): label column name
        model (list): The VW model....
        oneStepAheadPredictions (object): 1-step ahead predictions collected during training
        performanceStatistics (object): Performance statistics collected during training
        predictionCol (str): prediction column name
        rawPredictionCol (str): raw prediction (a.k.a. confidence) column name
        testArgs (str): Additional arguments passed to VW at test time
    """
    additionalFeatures: Incomplete
    featuresCol: Incomplete
    labelCol: Incomplete
    model: Incomplete
    oneStepAheadPredictions: Incomplete
    performanceStatistics: Incomplete
    predictionCol: Incomplete
    rawPredictionCol: Incomplete
    testArgs: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, additionalFeatures: Incomplete | None = None, featuresCol: str = 'features', labelCol: str = 'label', model: Incomplete | None = None, oneStepAheadPredictions: Incomplete | None = None, performanceStatistics: Incomplete | None = None, predictionCol: str = 'prediction', rawPredictionCol: str = 'rawPrediction', testArgs: str = '') -> None: ...
    def setParams(self, additionalFeatures: Incomplete | None = None, featuresCol: str = 'features', labelCol: str = 'label', model: Incomplete | None = None, oneStepAheadPredictions: Incomplete | None = None, performanceStatistics: Incomplete | None = None, predictionCol: str = 'prediction', rawPredictionCol: str = 'rawPrediction', testArgs: str = ''):
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
