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

class SuperpixelTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        cellSize (float): Number that controls the size of the superpixels
        inputCol (str): The name of the input column
        modifier (float): Controls the trade-off spatial and color distance
        outputCol (str): The name of the output column
    """
    cellSize: Incomplete
    inputCol: Incomplete
    modifier: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, cellSize: float = 16.0, inputCol: Incomplete | None = None, modifier: float = 130.0, outputCol: str = 'SuperpixelTransformer_61a489c14d63_output') -> None: ...
    def setParams(self, cellSize: float = 16.0, inputCol: Incomplete | None = None, modifier: float = 130.0, outputCol: str = 'SuperpixelTransformer_61a489c14d63_output'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setCellSize(self, value):
        """
        Args:
            cellSize: Number that controls the size of the superpixels
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setModifier(self, value):
        """
        Args:
            modifier: Controls the trade-off spatial and color distance
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getCellSize(self):
        """
        Returns:
            cellSize: Number that controls the size of the superpixels
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getModifier(self):
        """
        Returns:
            modifier: Controls the trade-off spatial and color distance
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
