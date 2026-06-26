from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class ValueIndexerModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        dataType (str): The datatype of the levels as a Json string
        inputCol (str): The name of the input column
        levels (object): Levels in categorical array
        outputCol (str): The name of the output column
    """
    dataType: Incomplete
    inputCol: Incomplete
    levels: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, dataType: str = 'string', inputCol: str = 'input', levels: Incomplete | None = None, outputCol: str = 'ValueIndexerModel_379318a6bc09_output') -> None: ...
    def setParams(self, dataType: str = 'string', inputCol: str = 'input', levels: Incomplete | None = None, outputCol: str = 'ValueIndexerModel_379318a6bc09_output'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setDataType(self, value):
        """
        Args:
            dataType: The datatype of the levels as a Json string
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setLevels(self, value):
        """
        Args:
            levels: Levels in categorical array
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getDataType(self):
        """
        Returns:
            dataType: The datatype of the levels as a Json string
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getLevels(self):
        """
        Returns:
            levels: Levels in categorical array
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
