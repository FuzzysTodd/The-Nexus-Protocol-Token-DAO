from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel as JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class ClassBalancer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        broadcastJoin (bool): Whether to broadcast the class to weight mapping to the worker
        inputCol (str): The name of the input column
        outputCol (str): The name of the output column
    """
    broadcastJoin: Incomplete
    inputCol: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, broadcastJoin: bool = True, inputCol: Incomplete | None = None, outputCol: str = 'weight') -> None: ...
    def setParams(self, broadcastJoin: bool = True, inputCol: Incomplete | None = None, outputCol: str = 'weight'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBroadcastJoin(self, value):
        """
        Args:
            broadcastJoin: Whether to broadcast the class to weight mapping to the worker
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
    def getBroadcastJoin(self):
        """
        Returns:
            broadcastJoin: Whether to broadcast the class to weight mapping to the worker
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
