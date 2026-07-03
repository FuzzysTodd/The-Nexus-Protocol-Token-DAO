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

class StratifiedRepartition(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        labelCol (str): The name of the label column
        mode (str): Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic
        seed (long): random seed
    """
    labelCol: Incomplete
    mode: Incomplete
    seed: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, labelCol: Incomplete | None = None, mode: str = 'mixed', seed: int = 1518410069) -> None: ...
    def setParams(self, labelCol: Incomplete | None = None, mode: str = 'mixed', seed: int = 1518410069):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: The name of the label column
        """
    def setMode(self, value):
        """
        Args:
            mode: Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic
        """
    def setSeed(self, value):
        """
        Args:
            seed: random seed
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: The name of the label column
        """
    def getMode(self):
        """
        Returns:
            mode: Specify equal to repartition with replacement across all labels, specify original to keep the ratios in the original dataset, or specify mixed to use a heuristic
        """
    def getSeed(self):
        """
        Returns:
            seed: random seed
        """
