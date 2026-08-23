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

class MultiNGram(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        inputCol (str): The name of the input column
        lengths (object): the collection of lengths to use for ngram extraction
        outputCol (str): The name of the output column
    """
    inputCol: Incomplete
    lengths: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, inputCol: Incomplete | None = None, lengths: Incomplete | None = None, outputCol: str = 'MultiNGram_478a138ed2d4_output') -> None: ...
    def setParams(self, inputCol: Incomplete | None = None, lengths: Incomplete | None = None, outputCol: str = 'MultiNGram_478a138ed2d4_output'):
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
    def setLengths(self, value):
        """
        Args:
            lengths: the collection of lengths to use for ngram extraction
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getLengths(self):
        """
        Returns:
            lengths: the collection of lengths to use for ngram extraction
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
