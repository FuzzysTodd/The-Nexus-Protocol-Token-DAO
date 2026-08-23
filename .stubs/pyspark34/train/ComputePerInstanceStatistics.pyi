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

class ComputePerInstanceStatistics(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        evaluationMetric (str): Metric to evaluate models with
        labelCol (str): The name of the label column
        scoredLabelsCol (str): Scored labels column name, only required if using SparkML estimators
        scoredProbabilitiesCol (str): Scored probabilities, usually calibrated from raw scores, only required if using SparkML estimators
        scoresCol (str): Scores or raw prediction column name, only required if using SparkML estimators
    """
    evaluationMetric: Incomplete
    labelCol: Incomplete
    scoredLabelsCol: Incomplete
    scoredProbabilitiesCol: Incomplete
    scoresCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, evaluationMetric: str = 'all', labelCol: Incomplete | None = None, scoredLabelsCol: Incomplete | None = None, scoredProbabilitiesCol: Incomplete | None = None, scoresCol: Incomplete | None = None) -> None: ...
    def setParams(self, evaluationMetric: str = 'all', labelCol: Incomplete | None = None, scoredLabelsCol: Incomplete | None = None, scoredProbabilitiesCol: Incomplete | None = None, scoresCol: Incomplete | None = None):
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
    def setLabelCol(self, value):
        """
        Args:
            labelCol: The name of the label column
        """
    def setScoredLabelsCol(self, value):
        """
        Args:
            scoredLabelsCol: Scored labels column name, only required if using SparkML estimators
        """
    def setScoredProbabilitiesCol(self, value):
        """
        Args:
            scoredProbabilitiesCol: Scored probabilities, usually calibrated from raw scores, only required if using SparkML estimators
        """
    def setScoresCol(self, value):
        """
        Args:
            scoresCol: Scores or raw prediction column name, only required if using SparkML estimators
        """
    def getEvaluationMetric(self):
        """
        Returns:
            evaluationMetric: Metric to evaluate models with
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: The name of the label column
        """
    def getScoredLabelsCol(self):
        """
        Returns:
            scoredLabelsCol: Scored labels column name, only required if using SparkML estimators
        """
    def getScoredProbabilitiesCol(self):
        """
        Returns:
            scoredProbabilitiesCol: Scored probabilities, usually calibrated from raw scores, only required if using SparkML estimators
        """
    def getScoresCol(self):
        """
        Returns:
            scoresCol: Scores or raw prediction column name, only required if using SparkML estimators
        """
