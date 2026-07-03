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

class VowpalWabbitCSETransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        maxImportanceWeight (float): Clip importance weight at this upper bound. Defaults to 100.
        metricsStratificationCols (list): Optional list of column names to stratify rewards by.
        minImportanceWeight (float): Clip importance weight at this lower bound. Defaults to 0.
    """
    maxImportanceWeight: Incomplete
    metricsStratificationCols: Incomplete
    minImportanceWeight: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, maxImportanceWeight: float = 100.0, metricsStratificationCols=[], minImportanceWeight: float = 0.0) -> None: ...
    def setParams(self, maxImportanceWeight: float = 100.0, metricsStratificationCols=[], minImportanceWeight: float = 0.0):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setMaxImportanceWeight(self, value):
        """
        Args:
            maxImportanceWeight: Clip importance weight at this upper bound. Defaults to 100.
        """
    def setMetricsStratificationCols(self, value):
        """
        Args:
            metricsStratificationCols: Optional list of column names to stratify rewards by.
        """
    def setMinImportanceWeight(self, value):
        """
        Args:
            minImportanceWeight: Clip importance weight at this lower bound. Defaults to 0.
        """
    def getMaxImportanceWeight(self):
        """
        Returns:
            maxImportanceWeight: Clip importance weight at this upper bound. Defaults to 100.
        """
    def getMetricsStratificationCols(self):
        """
        Returns:
            metricsStratificationCols: Optional list of column names to stratify rewards by.
        """
    def getMinImportanceWeight(self):
        """
        Returns:
            minImportanceWeight: Clip importance weight at this lower bound. Defaults to 0.
        """
