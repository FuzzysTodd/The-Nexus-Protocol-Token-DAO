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

class VectorZipper(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        inputCols (list): The names of the input columns
        outputCol (str): The name of the output column
    """
    inputCols: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, inputCols: Incomplete | None = None, outputCol: Incomplete | None = None) -> None: ...
    def setParams(self, inputCols: Incomplete | None = None, outputCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setInputCols(self, value):
        """
        Args:
            inputCols: The names of the input columns
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
