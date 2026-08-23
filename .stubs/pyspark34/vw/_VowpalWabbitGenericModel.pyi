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

class _VowpalWabbitGenericModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        inputCol (str): The name of the input column
        model (list): The VW model....
        oneStepAheadPredictions (object): 1-step ahead predictions collected during training
        performanceStatistics (object): Performance statistics collected during training
        testArgs (str): Additional arguments passed to VW at test time
    """
    inputCol: Incomplete
    model: Incomplete
    oneStepAheadPredictions: Incomplete
    performanceStatistics: Incomplete
    testArgs: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, inputCol: Incomplete | None = None, model: Incomplete | None = None, oneStepAheadPredictions: Incomplete | None = None, performanceStatistics: Incomplete | None = None, testArgs: str = '') -> None: ...
    def setParams(self, inputCol: Incomplete | None = None, model: Incomplete | None = None, oneStepAheadPredictions: Incomplete | None = None, performanceStatistics: Incomplete | None = None, testArgs: str = ''):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
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
    def setTestArgs(self, value):
        """
        Args:
            testArgs: Additional arguments passed to VW at test time
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
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
    def getTestArgs(self):
        """
        Returns:
            testArgs: Additional arguments passed to VW at test time
        """
