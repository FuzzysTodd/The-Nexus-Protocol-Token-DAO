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

class HTTPTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        handler (object): Which strategy to use when handling requests
        inputCol (str): The name of the input column
        outputCol (str): The name of the output column
        timeout (float): number of seconds to wait before closing the connection
    """
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    handler: Incomplete
    inputCol: Incomplete
    outputCol: Incomplete
    timeout: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, handler: Incomplete | None = None, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, timeout: float = 60.0) -> None: ...
    def setParams(self, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, handler: Incomplete | None = None, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, timeout: float = 60.0):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setConcurrency(self, value):
        """
        Args:
            concurrency: max number of concurrent calls
        """
    def setConcurrentTimeout(self, value):
        """
        Args:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
    def getConcurrency(self):
        """
        Returns:
            concurrency: max number of concurrent calls
        """
    def getConcurrentTimeout(self):
        """
        Returns:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
