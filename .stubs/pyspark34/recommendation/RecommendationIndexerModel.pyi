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

class RecommendationIndexerModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        itemIndexModel (object): itemIndexModel
        itemInputCol (str): Item Input Col
        itemOutputCol (str): Item Output Col
        ratingCol (str): Rating Col
        userIndexModel (object): userIndexModel
        userInputCol (str): User Input Col
        userOutputCol (str): User Output Col
    """
    itemIndexModel: Incomplete
    itemInputCol: Incomplete
    itemOutputCol: Incomplete
    ratingCol: Incomplete
    userIndexModel: Incomplete
    userInputCol: Incomplete
    userOutputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, itemIndexModel: Incomplete | None = None, itemInputCol: Incomplete | None = None, itemOutputCol: Incomplete | None = None, ratingCol: Incomplete | None = None, userIndexModel: Incomplete | None = None, userInputCol: Incomplete | None = None, userOutputCol: Incomplete | None = None) -> None: ...
    def setParams(self, itemIndexModel: Incomplete | None = None, itemInputCol: Incomplete | None = None, itemOutputCol: Incomplete | None = None, ratingCol: Incomplete | None = None, userIndexModel: Incomplete | None = None, userInputCol: Incomplete | None = None, userOutputCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setItemIndexModel(self, value):
        """
        Args:
            itemIndexModel: itemIndexModel
        """
    def setItemInputCol(self, value):
        """
        Args:
            itemInputCol: Item Input Col
        """
    def setItemOutputCol(self, value):
        """
        Args:
            itemOutputCol: Item Output Col
        """
    def setRatingCol(self, value):
        """
        Args:
            ratingCol: Rating Col
        """
    def setUserIndexModel(self, value):
        """
        Args:
            userIndexModel: userIndexModel
        """
    def setUserInputCol(self, value):
        """
        Args:
            userInputCol: User Input Col
        """
    def setUserOutputCol(self, value):
        """
        Args:
            userOutputCol: User Output Col
        """
    def getItemIndexModel(self):
        """
        Returns:
            itemIndexModel: itemIndexModel
        """
    def getItemInputCol(self):
        """
        Returns:
            itemInputCol: Item Input Col
        """
    def getItemOutputCol(self):
        """
        Returns:
            itemOutputCol: Item Output Col
        """
    def getRatingCol(self):
        """
        Returns:
            ratingCol: Rating Col
        """
    def getUserIndexModel(self):
        """
        Returns:
            userIndexModel: userIndexModel
        """
    def getUserInputCol(self):
        """
        Returns:
            userInputCol: User Input Col
        """
    def getUserOutputCol(self):
        """
        Returns:
            userOutputCol: User Output Col
        """
