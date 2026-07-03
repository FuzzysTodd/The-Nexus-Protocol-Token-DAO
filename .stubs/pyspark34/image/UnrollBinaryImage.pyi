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

class UnrollBinaryImage(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        height (int): the width of the image
        inputCol (str): The name of the input column
        nChannels (int): the number of channels of the target image
        outputCol (str): The name of the output column
        width (int): the width of the image
    """
    height: Incomplete
    inputCol: Incomplete
    nChannels: Incomplete
    outputCol: Incomplete
    width: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, height: Incomplete | None = None, inputCol: str = 'image', nChannels: Incomplete | None = None, outputCol: str = 'UnrollImage_00fc9fe41544_output', width: Incomplete | None = None) -> None: ...
    def setParams(self, height: Incomplete | None = None, inputCol: str = 'image', nChannels: Incomplete | None = None, outputCol: str = 'UnrollImage_00fc9fe41544_output', width: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setHeight(self, value):
        """
        Args:
            height: the width of the image
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setNChannels(self, value):
        """
        Args:
            nChannels: the number of channels of the target image
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setWidth(self, value):
        """
        Args:
            width: the width of the image
        """
    def getHeight(self):
        """
        Returns:
            height: the width of the image
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getNChannels(self):
        """
        Returns:
            nChannels: the number of channels of the target image
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getWidth(self):
        """
        Returns:
            width: the width of the image
        """
