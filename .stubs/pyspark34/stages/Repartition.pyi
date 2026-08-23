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

class Repartition(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        disable (bool): Whether to disable repartitioning (so that one can turn it off for evaluation)
        n (int): Number of partitions
    """
    disable: Incomplete
    n: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, disable: bool = False, n: Incomplete | None = None) -> None: ...
    def setParams(self, disable: bool = False, n: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setDisable(self, value):
        """
        Args:
            disable: Whether to disable repartitioning (so that one can turn it off for evaluation)
        """
    def setN(self, value):
        """
        Args:
            n: Number of partitions
        """
    def getDisable(self):
        """
        Returns:
            disable: Whether to disable repartitioning (so that one can turn it off for evaluation)
        """
    def getN(self):
        """
        Returns:
            n: Number of partitions
        """
