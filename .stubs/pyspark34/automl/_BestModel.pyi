from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.param import TypeConverters as TypeConverters
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class _BestModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        allModelMetrics (object): all model metrics
        bestModel (object): the best model found
        bestModelMetrics (object): the metrics from the best model
        rocCurve (object): the roc curve of the best model
        scoredDataset (object): dataset scored by best model
    """
    allModelMetrics: Incomplete
    bestModel: Incomplete
    bestModelMetrics: Incomplete
    rocCurve: Incomplete
    scoredDataset: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, allModelMetrics: Incomplete | None = None, bestModel: Incomplete | None = None, bestModelMetrics: Incomplete | None = None, rocCurve: Incomplete | None = None, scoredDataset: Incomplete | None = None) -> None: ...
    def setParams(self, allModelMetrics: Incomplete | None = None, bestModel: Incomplete | None = None, bestModelMetrics: Incomplete | None = None, rocCurve: Incomplete | None = None, scoredDataset: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAllModelMetrics(self, value):
        """
        Args:
            allModelMetrics: all model metrics
        """
    def setBestModel(self, value):
        """
        Args:
            bestModel: the best model found
        """
    def setBestModelMetrics(self, value):
        """
        Args:
            bestModelMetrics: the metrics from the best model
        """
    def setRocCurve(self, value):
        """
        Args:
            rocCurve: the roc curve of the best model
        """
    def setScoredDataset(self, value):
        """
        Args:
            scoredDataset: dataset scored by best model
        """
    def getAllModelMetrics(self):
        """
        Returns:
            allModelMetrics: all model metrics
        """
    def getBestModel(self):
        """
        Returns:
            bestModel: the best model found
        """
    def getBestModelMetrics(self):
        """
        Returns:
            bestModelMetrics: the metrics from the best model
        """
    def getRocCurve(self):
        """
        Returns:
            rocCurve: the roc curve of the best model
        """
    def getScoredDataset(self):
        """
        Returns:
            scoredDataset: dataset scored by best model
        """
