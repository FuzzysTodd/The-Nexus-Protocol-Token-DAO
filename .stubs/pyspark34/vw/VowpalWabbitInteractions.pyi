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

class VowpalWabbitInteractions(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        inputCols (list): The names of the input columns
        numBits (int): Number of bits used to mask
        outputCol (str): The name of the output column
        sumCollisions (bool): Sums collisions if true, otherwise removes them
    """
    inputCols: Incomplete
    numBits: Incomplete
    outputCol: Incomplete
    sumCollisions: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, inputCols: Incomplete | None = None, numBits: int = 30, outputCol: Incomplete | None = None, sumCollisions: bool = True) -> None: ...
    def setParams(self, inputCols: Incomplete | None = None, numBits: int = 30, outputCol: Incomplete | None = None, sumCollisions: bool = True):
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
    def setNumBits(self, value):
        """
        Args:
            numBits: Number of bits used to mask
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setSumCollisions(self, value):
        """
        Args:
            sumCollisions: Sums collisions if true, otherwise removes them
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
    def getNumBits(self):
        """
        Returns:
            numBits: Number of bits used to mask
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getSumCollisions(self):
        """
        Returns:
            sumCollisions: Sums collisions if true, otherwise removes them
        """
