from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class RankingEvaluator(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEvaluator):
    """
    Args:
        itemCol (str): Column of items
        k (int): number of items
        labelCol (str): label column name
        metricName (str): metric name in evaluation (ndcgAt|map|precisionAtk|recallAtK|diversityAtK|maxDiversity|mrr|fcp)
        nItems (long): number of items
        predictionCol (str): prediction column name
        ratingCol (str): Column of ratings
        userCol (str): Column of users
    """
    itemCol: Incomplete
    k: Incomplete
    labelCol: Incomplete
    metricName: Incomplete
    nItems: Incomplete
    predictionCol: Incomplete
    ratingCol: Incomplete
    userCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, itemCol: Incomplete | None = None, k: int = 10, labelCol: str = 'label', metricName: str = 'ndcgAt', nItems: int = -1, predictionCol: str = 'prediction', ratingCol: Incomplete | None = None, userCol: Incomplete | None = None) -> None: ...
    def setParams(self, itemCol: Incomplete | None = None, k: int = 10, labelCol: str = 'label', metricName: str = 'ndcgAt', nItems: int = -1, predictionCol: str = 'prediction', ratingCol: Incomplete | None = None, userCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setItemCol(self, value):
        """
        Args:
            itemCol: Column of items
        """
    def setK(self, value):
        """
        Args:
            k: number of items
        """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
    def setMetricName(self, value):
        """
        Args:
            metricName: metric name in evaluation (ndcgAt|map|precisionAtk|recallAtK|diversityAtK|maxDiversity|mrr|fcp)
        """
    def setNItems(self, value):
        """
        Args:
            nItems: number of items
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
    def setRatingCol(self, value):
        """
        Args:
            ratingCol: Column of ratings
        """
    def setUserCol(self, value):
        """
        Args:
            userCol: Column of users
        """
    def getItemCol(self):
        """
        Returns:
            itemCol: Column of items
        """
    def getK(self):
        """
        Returns:
            k: number of items
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getMetricName(self):
        """
        Returns:
            metricName: metric name in evaluation (ndcgAt|map|precisionAtk|recallAtK|diversityAtK|maxDiversity|mrr|fcp)
        """
    def getNItems(self):
        """
        Returns:
            nItems: number of items
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
    def getRatingCol(self):
        """
        Returns:
            ratingCol: Column of ratings
        """
    def getUserCol(self):
        """
        Returns:
            userCol: Column of users
        """
