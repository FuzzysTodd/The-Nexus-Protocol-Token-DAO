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

class FeatureBalanceMeasure(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        classACol (str): Output column name for the first feature value to compare.
        classBCol (str): Output column name for the second feature value to compare.
        featureNameCol (str): Output column name for feature names.
        labelCol (str): label column name
        outputCol (str): output column name
        sensitiveCols (list): Sensitive columns to use.
        verbose (bool): Whether to show intermediate measures and calculations, such as Positive Rate.
    """
    classACol: Incomplete
    classBCol: Incomplete
    featureNameCol: Incomplete
    labelCol: Incomplete
    outputCol: Incomplete
    sensitiveCols: Incomplete
    verbose: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, classACol: str = 'ClassA', classBCol: str = 'ClassB', featureNameCol: str = 'FeatureName', labelCol: str = 'label', outputCol: str = 'FeatureBalanceMeasure', sensitiveCols: Incomplete | None = None, verbose: bool = False) -> None: ...
    def setParams(self, classACol: str = 'ClassA', classBCol: str = 'ClassB', featureNameCol: str = 'FeatureName', labelCol: str = 'label', outputCol: str = 'FeatureBalanceMeasure', sensitiveCols: Incomplete | None = None, verbose: bool = False):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setClassACol(self, value):
        """
        Args:
            classACol: Output column name for the first feature value to compare.
        """
    def setClassBCol(self, value):
        """
        Args:
            classBCol: Output column name for the second feature value to compare.
        """
    def setFeatureNameCol(self, value):
        """
        Args:
            featureNameCol: Output column name for feature names.
        """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: output column name
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
    def getClassACol(self):
        """
        Returns:
            classACol: Output column name for the first feature value to compare.
        """
    def getClassBCol(self):
        """
        Returns:
            classBCol: Output column name for the second feature value to compare.
        """
    def getFeatureNameCol(self):
        """
        Returns:
            featureNameCol: Output column name for feature names.
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: output column name
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
