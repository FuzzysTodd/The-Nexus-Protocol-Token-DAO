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

class PageSplitter(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        boundaryRegex (str): how to split into words
        inputCol (str): The name of the input column
        maximumPageLength (int): the maximum number of characters to be in a page
        minimumPageLength (int): the the minimum number of characters to have on a page in order to preserve work boundaries
        outputCol (str): The name of the output column
    """
    boundaryRegex: Incomplete
    inputCol: Incomplete
    maximumPageLength: Incomplete
    minimumPageLength: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, boundaryRegex: str = '\\s', inputCol: Incomplete | None = None, maximumPageLength: int = 5000, minimumPageLength: int = 4500, outputCol: str = 'PageSplitter_57f6c6c9dc3b_output') -> None: ...
    def setParams(self, boundaryRegex: str = '\\s', inputCol: Incomplete | None = None, maximumPageLength: int = 5000, minimumPageLength: int = 4500, outputCol: str = 'PageSplitter_57f6c6c9dc3b_output'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBoundaryRegex(self, value):
        """
        Args:
            boundaryRegex: how to split into words
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setMaximumPageLength(self, value):
        """
        Args:
            maximumPageLength: the maximum number of characters to be in a page
        """
    def setMinimumPageLength(self, value):
        """
        Args:
            minimumPageLength: the the minimum number of characters to have on a page in order to preserve work boundaries
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getBoundaryRegex(self):
        """
        Returns:
            boundaryRegex: how to split into words
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getMaximumPageLength(self):
        """
        Returns:
            maximumPageLength: the maximum number of characters to be in a page
        """
    def getMinimumPageLength(self):
        """
        Returns:
            minimumPageLength: the the minimum number of characters to have on a page in order to preserve work boundaries
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
