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

class CleanMissingData(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        cleaningMode (str): Cleaning mode
        customValue (str): Custom value for replacement
        inputCols (list): The names of the input columns
        outputCols (list): The names of the output columns
    """
    cleaningMode: Incomplete
    customValue: Incomplete
    inputCols: Incomplete
    outputCols: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, cleaningMode: str = 'Mean', customValue: Incomplete | None = None, inputCols: Incomplete | None = None, outputCols: Incomplete | None = None) -> None: ...
    def setParams(self, cleaningMode: str = 'Mean', customValue: Incomplete | None = None, inputCols: Incomplete | None = None, outputCols: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setCleaningMode(self, value):
        """
        Args:
            cleaningMode: Cleaning mode
        """
    def setCustomValue(self, value):
        """
        Args:
            customValue: Custom value for replacement
        """
    def setInputCols(self, value):
        """
        Args:
            inputCols: The names of the input columns
        """
    def setOutputCols(self, value):
        """
        Args:
            outputCols: The names of the output columns
        """
    def getCleaningMode(self):
        """
        Returns:
            cleaningMode: Cleaning mode
        """
    def getCustomValue(self):
        """
        Returns:
            customValue: Custom value for replacement
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
    def getOutputCols(self):
        """
        Returns:
            outputCols: The names of the output columns
        """
