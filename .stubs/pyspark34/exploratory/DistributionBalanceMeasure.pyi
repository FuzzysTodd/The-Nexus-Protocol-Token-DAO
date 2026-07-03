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

class DistributionBalanceMeasure(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        featureNameCol (str): Output column name for feature names.
        outputCol (str): output column name
        referenceDistribution (object): An ordered list of reference distributions that correspond to each of the sensitive columns.
        sensitiveCols (list): Sensitive columns to use.
        verbose (bool): Whether to show intermediate measures and calculations, such as Positive Rate.
    """
    featureNameCol: Incomplete
    outputCol: Incomplete
    referenceDistribution: Incomplete
    sensitiveCols: Incomplete
    verbose: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, featureNameCol: str = 'FeatureName', outputCol: str = 'DistributionBalanceMeasure', referenceDistribution: Incomplete | None = None, sensitiveCols: Incomplete | None = None, verbose: bool = False) -> None: ...
    def setParams(self, featureNameCol: str = 'FeatureName', outputCol: str = 'DistributionBalanceMeasure', referenceDistribution: Incomplete | None = None, sensitiveCols: Incomplete | None = None, verbose: bool = False):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setFeatureNameCol(self, value):
        """
        Args:
            featureNameCol: Output column name for feature names.
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: output column name
        """
    def setReferenceDistribution(self, value):
        """
        Args:
            referenceDistribution: An ordered list of reference distributions that correspond to each of the sensitive columns.
        """
    def setSensitiveCols(self, value):
        """
        Args:
            sensitiveCols: Sensitive columns to use.
        """
    def setVerbose(self, value):
        """
        Args:
            verbose: Whether to show intermediate measures and calculations, such as Positive Rate.
        """
    def getFeatureNameCol(self):
        """
        Returns:
            featureNameCol: Output column name for feature names.
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: output column name
        """
    def getReferenceDistribution(self):
        """
        Returns:
            referenceDistribution: An ordered list of reference distributions that correspond to each of the sensitive columns.
        """
    def getSensitiveCols(self):
        """
        Returns:
            sensitiveCols: Sensitive columns to use.
        """
    def getVerbose(self):
        """
        Returns:
            verbose: Whether to show intermediate measures and calculations, such as Positive Rate.
        """
