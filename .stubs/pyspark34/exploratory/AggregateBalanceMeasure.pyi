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

class AggregateBalanceMeasure(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        epsilon (float): Epsilon value for Atkinson Index. Inverse of alpha (1 - alpha).
        errorTolerance (float): Error tolerance value for Atkinson Index.
        outputCol (str): output column name
        sensitiveCols (list): Sensitive columns to use.
        verbose (bool): Whether to show intermediate measures and calculations, such as Positive Rate.
    """
    epsilon: Incomplete
    errorTolerance: Incomplete
    outputCol: Incomplete
    sensitiveCols: Incomplete
    verbose: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, epsilon: float = 1.0, errorTolerance: float = 1e-12, outputCol: str = 'AggregateBalanceMeasure', sensitiveCols: Incomplete | None = None, verbose: bool = False) -> None: ...
    def setParams(self, epsilon: float = 1.0, errorTolerance: float = 1e-12, outputCol: str = 'AggregateBalanceMeasure', sensitiveCols: Incomplete | None = None, verbose: bool = False):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setEpsilon(self, value):
        """
        Args:
            epsilon: Epsilon value for Atkinson Index. Inverse of alpha (1 - alpha).
        """
    def setErrorTolerance(self, value):
        """
        Args:
            errorTolerance: Error tolerance value for Atkinson Index.
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
    def getEpsilon(self):
        """
        Returns:
            epsilon: Epsilon value for Atkinson Index. Inverse of alpha (1 - alpha).
        """
    def getErrorTolerance(self):
        """
        Returns:
            errorTolerance: Error tolerance value for Atkinson Index.
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
