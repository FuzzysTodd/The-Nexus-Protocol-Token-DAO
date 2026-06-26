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

class RankingAdapter(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        itemCol (str): Column of items
        k (int): number of items
        labelCol (str): The name of the label column
        minRatingsPerItem (int): min ratings for items > 0
        minRatingsPerUser (int): min ratings for users > 0
        mode (str): recommendation mode
        ratingCol (str): Column of ratings
        recommender (object): estimator for selection
        userCol (str): Column of users
    """
    itemCol: Incomplete
    k: Incomplete
    labelCol: Incomplete
    minRatingsPerItem: Incomplete
    minRatingsPerUser: Incomplete
    mode: Incomplete
    ratingCol: Incomplete
    recommender: Incomplete
    userCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, itemCol: Incomplete | None = None, k: int = 10, labelCol: str = 'label', minRatingsPerItem: int = 1, minRatingsPerUser: int = 1, mode: str = 'allUsers', ratingCol: Incomplete | None = None, recommender: Incomplete | None = None, userCol: Incomplete | None = None) -> None: ...
    def setParams(self, itemCol: Incomplete | None = None, k: int = 10, labelCol: str = 'label', minRatingsPerItem: int = 1, minRatingsPerUser: int = 1, mode: str = 'allUsers', ratingCol: Incomplete | None = None, recommender: Incomplete | None = None, userCol: Incomplete | None = None):
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
            labelCol: The name of the label column
        """
    def setMinRatingsPerItem(self, value):
        """
        Args:
            minRatingsPerItem: min ratings for items > 0
        """
    def setMinRatingsPerUser(self, value):
        """
        Args:
            minRatingsPerUser: min ratings for users > 0
        """
    def setMode(self, value):
        """
        Args:
            mode: recommendation mode
        """
    def setRatingCol(self, value):
        """
        Args:
            ratingCol: Column of ratings
        """
    def setRecommender(self, value):
        """
        Args:
            recommender: estimator for selection
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
            labelCol: The name of the label column
        """
    def getMinRatingsPerItem(self):
        """
        Returns:
            minRatingsPerItem: min ratings for items > 0
        """
    def getMinRatingsPerUser(self):
        """
        Returns:
            minRatingsPerUser: min ratings for users > 0
        """
    def getMode(self):
        """
        Returns:
            mode: recommendation mode
        """
    def getRatingCol(self):
        """
        Returns:
            ratingCol: Column of ratings
        """
    def getRecommender(self):
        """
        Returns:
            recommender: estimator for selection
        """
    def getUserCol(self):
        """
        Returns:
            userCol: Column of users
        """
