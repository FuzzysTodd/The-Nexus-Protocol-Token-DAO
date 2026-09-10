from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class ResidualTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        classIndex (int): The index of the class to compute residual for classification outputs. Default value is 1.
        observedCol (str): observed data (label column)
        outputCol (str): The name of the output column
        predictedCol (str): predicted data (prediction or probability columns
    """
    classIndex: Incomplete
    observedCol: Incomplete
    outputCol: Incomplete
    predictedCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, classIndex: int = 1, observedCol: str = 'label', outputCol: str = 'residual', predictedCol: str = 'prediction') -> None: ...
    def setParams(self, classIndex: int = 1, observedCol: str = 'label', outputCol: str = 'residual', predictedCol: str = 'prediction'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setClassIndex(self, value):
        """
        Args:
            classIndex: The index of the class to compute residual for classification outputs. Default value is 1.
        """
    def setObservedCol(self, value):
        """
        Args:
            observedCol: observed data (label column)
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPredictedCol(self, value):
        """
        Args:
            predictedCol: predicted data (prediction or probability columns
        """
    def getClassIndex(self):
        """
        Returns:
            classIndex: The index of the class to compute residual for classification outputs. Default value is 1.
        """
    def getObservedCol(self):
        """
        Returns:
            observedCol: observed data (label column)
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPredictedCol(self):
        """
        Returns:
            predictedCol: predicted data (prediction or probability columns
        """
