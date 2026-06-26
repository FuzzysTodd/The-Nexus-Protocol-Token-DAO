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

class Featurize(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        imputeMissing (bool): Whether to impute missing values
        inputCols (list): The names of the input columns
        numFeatures (int): Number of features to hash string columns to
        oneHotEncodeCategoricals (bool): One-hot encode categorical columns
        outputCol (str): The name of the output column
    """
    imputeMissing: Incomplete
    inputCols: Incomplete
    numFeatures: Incomplete
    oneHotEncodeCategoricals: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, imputeMissing: bool = True, inputCols: Incomplete | None = None, numFeatures: int = 262144, oneHotEncodeCategoricals: bool = True, outputCol: Incomplete | None = None) -> None: ...
    def setParams(self, imputeMissing: bool = True, inputCols: Incomplete | None = None, numFeatures: int = 262144, oneHotEncodeCategoricals: bool = True, outputCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setImputeMissing(self, value):
        """
        Args:
            imputeMissing: Whether to impute missing values
        """
    def setInputCols(self, value):
        """
        Args:
            inputCols: The names of the input columns
        """
    def setNumFeatures(self, value):
        """
        Args:
            numFeatures: Number of features to hash string columns to
        """
    def setOneHotEncodeCategoricals(self, value):
        """
        Args:
            oneHotEncodeCategoricals: One-hot encode categorical columns
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getImputeMissing(self):
        """
        Returns:
            imputeMissing: Whether to impute missing values
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
    def getNumFeatures(self):
        """
        Returns:
            numFeatures: Number of features to hash string columns to
        """
    def getOneHotEncodeCategoricals(self):
        """
        Returns:
            oneHotEncodeCategoricals: One-hot encode categorical columns
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
