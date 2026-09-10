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

class _TuneHyperparametersModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        bestMetric (float): the best metric from the runs
        bestModel (object): the best model found
    """
    bestMetric: Incomplete
    bestModel: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, bestMetric: Incomplete | None = None, bestModel: Incomplete | None = None) -> None: ...
    def setParams(self, bestMetric: Incomplete | None = None, bestModel: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBestMetric(self, value):
        """
        Args:
            bestMetric: the best metric from the runs
        """
    def setBestModel(self, value):
        """
        Args:
            bestModel: the best model found
        """
    def getBestMetric(self):
        """
        Returns:
            bestMetric: the best metric from the runs
        """
    def getBestModel(self):
        """
        Returns:
            bestModel: the best model found
        """
