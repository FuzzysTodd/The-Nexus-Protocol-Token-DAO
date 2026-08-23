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

class CustomInputParser(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        inputCol (str): The name of the input column
        outputCol (str): The name of the output column
        udfPython (object): User Defined Python Function to be applied to the DF input col
        udfScala (object): User Defined Function to be applied to the DF input col
    """
    inputCol: Incomplete
    outputCol: Incomplete
    udfPython: Incomplete
    udfScala: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, udfPython: Incomplete | None = None, udfScala: Incomplete | None = None) -> None: ...
    def setParams(self, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, udfPython: Incomplete | None = None, udfScala: Incomplete | None = None):
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
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setUdfPython(self, value):
        """
        Args:
            udfPython: User Defined Python Function to be applied to the DF input col
        """
    def setUdfScala(self, value):
        """
        Args:
            udfScala: User Defined Function to be applied to the DF input col
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
    def getUdfPython(self):
        """
        Returns:
            udfPython: User Defined Python Function to be applied to the DF input col
        """
    def getUdfScala(self):
        """
        Returns:
            udfScala: User Defined Function to be applied to the DF input col
        """
