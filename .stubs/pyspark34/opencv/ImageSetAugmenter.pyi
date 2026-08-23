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

class ImageSetAugmenter(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        flipLeftRight (bool): Symmetric Left-Right
        flipUpDown (bool): Symmetric Up-Down
        inputCol (str): The name of the input column
        outputCol (str): The name of the output column
    """
    flipLeftRight: Incomplete
    flipUpDown: Incomplete
    inputCol: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, flipLeftRight: bool = True, flipUpDown: bool = False, inputCol: str = 'image', outputCol: str = 'ImageSetAugmenter_1d423832ae76_output') -> None: ...
    def setParams(self, flipLeftRight: bool = True, flipUpDown: bool = False, inputCol: str = 'image', outputCol: str = 'ImageSetAugmenter_1d423832ae76_output'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setFlipLeftRight(self, value):
        """
        Args:
            flipLeftRight: Symmetric Left-Right
        """
    def setFlipUpDown(self, value):
        """
        Args:
            flipUpDown: Symmetric Up-Down
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
    def getFlipLeftRight(self):
        """
        Returns:
            flipLeftRight: Symmetric Left-Right
        """
    def getFlipUpDown(self):
        """
        Returns:
            flipUpDown: Symmetric Up-Down
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
