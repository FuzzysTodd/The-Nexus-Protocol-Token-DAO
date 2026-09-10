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

class TrainedRegressorModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        featuresCol (str): The name of the features column
        labelCol (str): The name of the label column
        model (object): model produced by training
    """
    featuresCol: Incomplete
    labelCol: Incomplete
    model: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, featuresCol: Incomplete | None = None, labelCol: Incomplete | None = None, model: Incomplete | None = None) -> None: ...
    def setParams(self, featuresCol: Incomplete | None = None, labelCol: Incomplete | None = None, model: Incomplete | None = None):
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
    def setLabelCol(self, value):
        """
        Args:
            labelCol: The name of the label column
        """
    def setModel(self, value):
        """
        Args:
            model: model produced by training
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The name of the features column
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: The name of the label column
        """
    def getModel(self):
        """
        Returns:
            model: model produced by training
        """
