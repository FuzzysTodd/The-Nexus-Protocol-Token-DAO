from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class CleanMissingDataModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        colsToFill (list): The columns to fill with
        fillValues (object): what to replace in the columns
        inputCols (list): The names of the input columns
        outputCols (list): The names of the output columns
    """
    colsToFill: Incomplete
    fillValues: Incomplete
    inputCols: Incomplete
    outputCols: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, colsToFill: Incomplete | None = None, fillValues: Incomplete | None = None, inputCols: Incomplete | None = None, outputCols: Incomplete | None = None) -> None: ...
    def setParams(self, colsToFill: Incomplete | None = None, fillValues: Incomplete | None = None, inputCols: Incomplete | None = None, outputCols: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setColsToFill(self, value):
        """
        Args:
            colsToFill: The columns to fill with
        """
    def setFillValues(self, value):
        """
        Args:
            fillValues: what to replace in the columns
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
    def getColsToFill(self):
        """
        Returns:
            colsToFill: The columns to fill with
        """
    def getFillValues(self):
        """
        Returns:
            fillValues: what to replace in the columns
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
