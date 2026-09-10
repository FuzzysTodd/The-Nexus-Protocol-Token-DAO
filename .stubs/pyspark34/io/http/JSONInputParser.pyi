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

class JSONInputParser(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        headers (dict): headers of the request
        inputCol (str): The name of the input column
        method (str): method to use for request, (PUT, POST, PATCH)
        outputCol (str): The name of the output column
        url (str): Url of the service
    """
    headers: Incomplete
    inputCol: Incomplete
    method: Incomplete
    outputCol: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, headers={}, inputCol: Incomplete | None = None, method: str = 'POST', outputCol: Incomplete | None = None, url: Incomplete | None = None) -> None: ...
    def setParams(self, headers={}, inputCol: Incomplete | None = None, method: str = 'POST', outputCol: Incomplete | None = None, url: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setHeaders(self, value):
        """
        Args:
            headers: headers of the request
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setMethod(self, value):
        """
        Args:
            method: method to use for request, (PUT, POST, PATCH)
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def getHeaders(self):
        """
        Returns:
            headers: headers of the request
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getMethod(self):
        """
        Returns:
            method: method to use for request, (PUT, POST, PATCH)
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
