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

class FindBestModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        evaluationMetric (str): Metric to evaluate models with
        models (object): List of models to be evaluated
    """
    evaluationMetric: Incomplete
    models: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, evaluationMetric: str = 'accuracy', models: Incomplete | None = None) -> None: ...
    def setParams(self, evaluationMetric: str = 'accuracy', models: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setEvaluationMetric(self, value):
        """
        Args:
            evaluationMetric: Metric to evaluate models with
        """
    def setModels(self, value):
        """
        Args:
            models: List of models to be evaluated
        """
    def getEvaluationMetric(self):
        """
        Returns:
            evaluationMetric: Metric to evaluate models with
        """
    def getModels(self):
        """
        Returns:
            models: List of models to be evaluated
        """
