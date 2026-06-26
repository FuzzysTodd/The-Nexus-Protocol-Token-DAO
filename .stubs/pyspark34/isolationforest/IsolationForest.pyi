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

class IsolationForest(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        bootstrap (bool): If true, draw sample for each tree with replacement. If false, do not sample with replacement.
        contamination (float): The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter.
        contaminationError (float): The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value.
        featuresCol (str): The feature vector.
        maxFeatures (float): The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count.
        maxSamples (float): The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count.
        numEstimators (int): The number of trees in the ensemble.
        predictionCol (str): The predicted label.
        randomSeed (long): The seed used for the random number generator.
        scoreCol (str): The outlier score.
    """
    bootstrap: Incomplete
    contamination: Incomplete
    contaminationError: Incomplete
    featuresCol: Incomplete
    maxFeatures: Incomplete
    maxSamples: Incomplete
    numEstimators: Incomplete
    predictionCol: Incomplete
    randomSeed: Incomplete
    scoreCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, bootstrap: bool = False, contamination: float = 0.0, contaminationError: float = 0.0, featuresCol: str = 'features', maxFeatures: float = 1.0, maxSamples: float = 256.0, numEstimators: int = 100, predictionCol: str = 'predictedLabel', randomSeed: int = 1, scoreCol: str = 'outlierScore') -> None: ...
    def setParams(self, bootstrap: bool = False, contamination: float = 0.0, contaminationError: float = 0.0, featuresCol: str = 'features', maxFeatures: float = 1.0, maxSamples: float = 256.0, numEstimators: int = 100, predictionCol: str = 'predictedLabel', randomSeed: int = 1, scoreCol: str = 'outlierScore'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBootstrap(self, value):
        """
        Args:
            bootstrap: If true, draw sample for each tree with replacement. If false, do not sample with replacement.
        """
    def setContamination(self, value):
        """
        Args:
            contamination: The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter.
        """
    def setContaminationError(self, value):
        """
        Args:
            contaminationError: The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value.
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: The feature vector.
        """
    def setMaxFeatures(self, value):
        """
        Args:
            maxFeatures: The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count.
        """
    def setMaxSamples(self, value):
        """
        Args:
            maxSamples: The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count.
        """
    def setNumEstimators(self, value):
        """
        Args:
            numEstimators: The number of trees in the ensemble.
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: The predicted label.
        """
    def setRandomSeed(self, value):
        """
        Args:
            randomSeed: The seed used for the random number generator.
        """
    def setScoreCol(self, value):
        """
        Args:
            scoreCol: The outlier score.
        """
    def getBootstrap(self):
        """
        Returns:
            bootstrap: If true, draw sample for each tree with replacement. If false, do not sample with replacement.
        """
    def getContamination(self):
        """
        Returns:
            contamination: The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter.
        """
    def getContaminationError(self):
        """
        Returns:
            contaminationError: The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value.
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The feature vector.
        """
    def getMaxFeatures(self):
        """
        Returns:
            maxFeatures: The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count.
        """
    def getMaxSamples(self):
        """
        Returns:
            maxSamples: The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count.
        """
    def getNumEstimators(self):
        """
        Returns:
            numEstimators: The number of trees in the ensemble.
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: The predicted label.
        """
    def getRandomSeed(self):
        """
        Returns:
            randomSeed: The seed used for the random number generator.
        """
    def getScoreCol(self):
        """
        Returns:
            scoreCol: The outlier score.
        """
