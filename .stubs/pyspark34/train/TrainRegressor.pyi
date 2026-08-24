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

class TrainRegressor(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        featuresCol (str): The name of the features column
        inputCols (list): The names of the input columns
        labelCol (str): The name of the label column
        model (object): Regressor to run
        numFeatures (int): Number of features to hash to
    """
    featuresCol: Incomplete
    inputCols: Incomplete
    labelCol: Incomplete
    model: Incomplete
    numFeatures: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, featuresCol: str = 'TrainRegressor_c696cca90654_features', inputCols: Incomplete | None = None, labelCol: Incomplete | None = None, model: Incomplete | None = None, numFeatures: int = 0) -> None: ...
    def setParams(self, featuresCol: str = 'TrainRegressor_c696cca90654_features', inputCols: Incomplete | None = None, labelCol: Incomplete | None = None, model: Incomplete | None = None, numFeatures: int = 0):
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
    def setInputCols(self, value):
        """
        Args:
            inputCols: The names of the input columns
        """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: The name of the label column
        """
    def setModel(self, value):
        """
        Args:
            model: Regressor to run
        """
    def setNumFeatures(self, value):
        """
        Args:
            numFeatures: Number of features to hash to
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The name of the features column
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: The name of the label column
        """
    def getModel(self):
        """
        Returns:
            model: Regressor to run
        """
    def getNumFeatures(self):
        """
        Returns:
            numFeatures: Number of features to hash to
        """
