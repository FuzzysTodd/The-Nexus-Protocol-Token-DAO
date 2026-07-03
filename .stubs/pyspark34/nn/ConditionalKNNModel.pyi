from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class ConditionalKNNModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        ballTree (object): the ballTree model used for perfoming queries
        conditionerCol (str): column holding identifiers for features that will be returned when queried
        featuresCol (str): The name of the features column
        k (int): number of matches to return
        labelCol (str): The name of the label column
        leafSize (int): max size of the leaves of the tree
        outputCol (str): The name of the output column
        valuesCol (str): column holding values for each feature (key) that will be returned when queried
    """
    ballTree: Incomplete
    conditionerCol: Incomplete
    featuresCol: Incomplete
    k: Incomplete
    labelCol: Incomplete
    leafSize: Incomplete
    outputCol: Incomplete
    valuesCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, ballTree: Incomplete | None = None, conditionerCol: Incomplete | None = None, featuresCol: Incomplete | None = None, k: Incomplete | None = None, labelCol: Incomplete | None = None, leafSize: Incomplete | None = None, outputCol: Incomplete | None = None, valuesCol: Incomplete | None = None) -> None: ...
    def setParams(self, ballTree: Incomplete | None = None, conditionerCol: Incomplete | None = None, featuresCol: Incomplete | None = None, k: Incomplete | None = None, labelCol: Incomplete | None = None, leafSize: Incomplete | None = None, outputCol: Incomplete | None = None, valuesCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBallTree(self, value):
        """
        Args:
            ballTree: the ballTree model used for perfoming queries
        """
    def setConditionerCol(self, value):
        """
        Args:
            conditionerCol: column holding identifiers for features that will be returned when queried
        """
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
    def setLabelCol(self, value):
        """
        Args:
            labelCol: The name of the label column
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
    def getBallTree(self):
        """
        Returns:
            ballTree: the ballTree model used for perfoming queries
        """
    def getConditionerCol(self):
        """
        Returns:
            conditionerCol: column holding identifiers for features that will be returned when queried
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
    def getLabelCol(self):
        """
        Returns:
            labelCol: The name of the label column
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
