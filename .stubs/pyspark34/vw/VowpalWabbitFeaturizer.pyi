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

class VowpalWabbitFeaturizer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        inputCols (list): The names of the input columns
        numBits (int): Number of bits used to mask
        outputCol (str): The name of the output column
        prefixStringsWithColumnName (bool): Prefix string features with column name
        preserveOrderNumBits (int): Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words
        seed (int): Hash seed
        stringSplitInputCols (list): Input cols that should be split at word boundaries
        sumCollisions (bool): Sums collisions if true, otherwise removes them
    """
    inputCols: Incomplete
    numBits: Incomplete
    outputCol: Incomplete
    prefixStringsWithColumnName: Incomplete
    preserveOrderNumBits: Incomplete
    seed: Incomplete
    stringSplitInputCols: Incomplete
    sumCollisions: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, inputCols=[], numBits: int = 30, outputCol: str = 'features', prefixStringsWithColumnName: bool = True, preserveOrderNumBits: int = 0, seed: int = 0, stringSplitInputCols=[], sumCollisions: bool = True) -> None: ...
    def setParams(self, inputCols=[], numBits: int = 30, outputCol: str = 'features', prefixStringsWithColumnName: bool = True, preserveOrderNumBits: int = 0, seed: int = 0, stringSplitInputCols=[], sumCollisions: bool = True):
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
    def setPrefixStringsWithColumnName(self, value):
        """
        Args:
            prefixStringsWithColumnName: Prefix string features with column name
        """
    def setPreserveOrderNumBits(self, value):
        """
        Args:
            preserveOrderNumBits: Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words
        """
    def setSeed(self, value):
        """
        Args:
            seed: Hash seed
        """
    def setStringSplitInputCols(self, value):
        """
        Args:
            stringSplitInputCols: Input cols that should be split at word boundaries
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
    def getPrefixStringsWithColumnName(self):
        """
        Returns:
            prefixStringsWithColumnName: Prefix string features with column name
        """
    def getPreserveOrderNumBits(self):
        """
        Returns:
            preserveOrderNumBits: Number of bits used to preserve the feature order. This will reduce the hash size. Needs to be large enough to fit count the maximum number of words
        """
    def getSeed(self):
        """
        Returns:
            seed: Hash seed
        """
    def getStringSplitInputCols(self):
        """
        Returns:
            stringSplitInputCols: Input cols that should be split at word boundaries
        """
    def getSumCollisions(self):
        """
        Returns:
            sumCollisions: Sums collisions if true, otherwise removes them
        """
