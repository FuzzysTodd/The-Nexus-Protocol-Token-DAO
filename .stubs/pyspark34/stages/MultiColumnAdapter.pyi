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

class MultiColumnAdapter(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        baseStage (object): base pipeline stage to apply to every column
        inputCols (list): list of column names encoded as a string
        outputCols (list): list of column names encoded as a string
    """
    baseStage: Incomplete
    inputCols: Incomplete
    outputCols: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, baseStage: Incomplete | None = None, inputCols: Incomplete | None = None, outputCols: Incomplete | None = None) -> None: ...
    def setParams(self, baseStage: Incomplete | None = None, inputCols: Incomplete | None = None, outputCols: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBaseStage(self, value):
        """
        Args:
            baseStage: base pipeline stage to apply to every column
        """
    def setInputCols(self, value):
        """
        Args:
            inputCols: list of column names encoded as a string
        """
    def setOutputCols(self, value):
        """
        Args:
            outputCols: list of column names encoded as a string
        """
    def getBaseStage(self):
        """
        Returns:
            baseStage: base pipeline stage to apply to every column
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: list of column names encoded as a string
        """
    def getOutputCols(self):
        """
        Returns:
            outputCols: list of column names encoded as a string
        """
