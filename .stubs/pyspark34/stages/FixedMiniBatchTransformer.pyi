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

class FixedMiniBatchTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        batchSize (int): The max size of the buffer
        buffered (bool): Whether or not to buffer batches in memory
        maxBufferSize (int): The max size of the buffer
    """
    batchSize: Incomplete
    buffered: Incomplete
    maxBufferSize: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, batchSize: Incomplete | None = None, buffered: bool = False, maxBufferSize: int = 2147483647) -> None: ...
    def setParams(self, batchSize: Incomplete | None = None, buffered: bool = False, maxBufferSize: int = 2147483647):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBatchSize(self, value):
        """
        Args:
            batchSize: The max size of the buffer
        """
    def setBuffered(self, value):
        """
        Args:
            buffered: Whether or not to buffer batches in memory
        """
    def setMaxBufferSize(self, value):
        """
        Args:
            maxBufferSize: The max size of the buffer
        """
    def getBatchSize(self):
        """
        Returns:
            batchSize: The max size of the buffer
        """
    def getBuffered(self):
        """
        Returns:
            buffered: Whether or not to buffer batches in memory
        """
    def getMaxBufferSize(self):
        """
        Returns:
            maxBufferSize: The max size of the buffer
        """
