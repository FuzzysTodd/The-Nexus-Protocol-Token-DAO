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

class SummarizeData(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        basic (bool): Compute basic statistics
        counts (bool): Compute count statistics
        errorThreshold (float): Threshold for quantiles - 0 is exact
        percentiles (bool): Compute percentiles
        sample (bool): Compute sample statistics
    """
    basic: Incomplete
    counts: Incomplete
    errorThreshold: Incomplete
    percentiles: Incomplete
    sample: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, basic: bool = True, counts: bool = True, errorThreshold: float = 0.0, percentiles: bool = True, sample: bool = True) -> None: ...
    def setParams(self, basic: bool = True, counts: bool = True, errorThreshold: float = 0.0, percentiles: bool = True, sample: bool = True):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBasic(self, value):
        """
        Args:
            basic: Compute basic statistics
        """
    def setCounts(self, value):
        """
        Args:
            counts: Compute count statistics
        """
    def setErrorThreshold(self, value):
        """
        Args:
            errorThreshold: Threshold for quantiles - 0 is exact
        """
    def setPercentiles(self, value):
        """
        Args:
            percentiles: Compute percentiles
        """
    def setSample(self, value):
        """
        Args:
            sample: Compute sample statistics
        """
    def getBasic(self):
        """
        Returns:
            basic: Compute basic statistics
        """
    def getCounts(self):
        """
        Returns:
            counts: Compute count statistics
        """
    def getErrorThreshold(self):
        """
        Returns:
            errorThreshold: Threshold for quantiles - 0 is exact
        """
    def getPercentiles(self):
        """
        Returns:
            percentiles: Compute percentiles
        """
    def getSample(self):
        """
        Returns:
            sample: Compute sample statistics
        """
