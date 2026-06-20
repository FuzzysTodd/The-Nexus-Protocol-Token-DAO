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

class KNN(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        featuresCol (str): The name of the features column
        k (int): number of matches to return
        leafSize (int): max size of the leaves of the tree
        outputCol (str): The name of the output column
        valuesCol (str): column holding values for each feature (key) that will be returned when queried
    """
    featuresCol: Incomplete
    k: Incomplete
    leafSize: Incomplete
    outputCol: Incomplete
    valuesCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, featuresCol: str = 'features', k: int = 5, leafSize: int = 50, outputCol: str = 'KNN_a338037a83f0_output', valuesCol: str = 'values') -> None: ...
    def setParams(self, featuresCol: str = 'features', k: int = 5, leafSize: int = 50, outputCol: str = 'KNN_a338037a83f0_output', valuesCol: str = 'values'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: The name of the features column
        """
    def setK(self, value):
        """
        Args:
            k: number of matches to return
        """
    def setLeafSize(self, value):
        """
        Args:
            leafSize: max size of the leaves of the tree
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setValuesCol(self, value):
        """
        Args:
            valuesCol: column holding values for each feature (key) that will be returned when queried
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The name of the features column
        """
    def getK(self):
        """
        Returns:
            k: number of matches to return
        """
    def getLeafSize(self):
        """
        Returns:
            leafSize: max size of the leaves of the tree
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getValuesCol(self):
        """
        Returns:
            valuesCol: column holding values for each feature (key) that will be returned when queried
        """
