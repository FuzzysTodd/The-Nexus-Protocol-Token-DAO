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

class _LightGBMClassificationModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        actualNumClasses (int): Inferred number of classes based on dataset metadata or, if there is no metadata, unique count
        featuresCol (str): features column name
        featuresShapCol (str): Output SHAP vector column name after prediction containing the feature contribution values
        labelCol (str): label column name
        leafPredictionCol (str): Predicted leaf indices's column name
        lightGBMBooster (object): The trained LightGBM booster
        numIterations (int): Sets the total number of iterations used in the prediction.If <= 0, all iterations from ``start_iteration`` are used (no limits).
        predictDisableShapeCheck (bool): control whether or not LightGBM raises an error when you try to predict on data with a different number of features than the training data
        predictionCol (str): prediction column name
        probabilityCol (str): Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        rawPredictionCol (str): raw prediction (a.k.a. confidence) column name
        startIteration (int): Sets the start index of the iteration to predict. If <= 0, starts from the first iteration.
        thresholds (list): Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
    """
    actualNumClasses: Incomplete
    featuresCol: Incomplete
    featuresShapCol: Incomplete
    labelCol: Incomplete
    leafPredictionCol: Incomplete
    lightGBMBooster: Incomplete
    numIterations: Incomplete
    predictDisableShapeCheck: Incomplete
    predictionCol: Incomplete
    probabilityCol: Incomplete
    rawPredictionCol: Incomplete
    startIteration: Incomplete
    thresholds: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, actualNumClasses: Incomplete | None = None, featuresCol: str = 'features', featuresShapCol: str = '', labelCol: str = 'label', leafPredictionCol: str = '', lightGBMBooster: Incomplete | None = None, numIterations: int = -1, predictDisableShapeCheck: bool = False, predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', startIteration: int = 0, thresholds: Incomplete | None = None) -> None: ...
    def setParams(self, actualNumClasses: Incomplete | None = None, featuresCol: str = 'features', featuresShapCol: str = '', labelCol: str = 'label', leafPredictionCol: str = '', lightGBMBooster: Incomplete | None = None, numIterations: int = -1, predictDisableShapeCheck: bool = False, predictionCol: str = 'prediction', probabilityCol: str = 'probability', rawPredictionCol: str = 'rawPrediction', startIteration: int = 0, thresholds: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setActualNumClasses(self, value):
        """
        Args:
            actualNumClasses: Inferred number of classes based on dataset metadata or, if there is no metadata, unique count
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: features column name
        """
    def setFeaturesShapCol(self, value):
        """
        Args:
            featuresShapCol: Output SHAP vector column name after prediction containing the feature contribution values
        """
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
    def setLeafPredictionCol(self, value):
        """
        Args:
            leafPredictionCol: Predicted leaf indices's column name
        """
    def setLightGBMBooster(self, value):
        """
        Args:
            lightGBMBooster: The trained LightGBM booster
        """
    def setNumIterations(self, value):
        """
        Args:
            numIterations: Sets the total number of iterations used in the prediction.If <= 0, all iterations from ``start_iteration`` are used (no limits).
        """
    def setPredictDisableShapeCheck(self, value):
        """
        Args:
            predictDisableShapeCheck: control whether or not LightGBM raises an error when you try to predict on data with a different number of features than the training data
        """
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
    def setProbabilityCol(self, value):
        """
        Args:
            probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        """
    def setRawPredictionCol(self, value):
        """
        Args:
            rawPredictionCol: raw prediction (a.k.a. confidence) column name
        """
    def setStartIteration(self, value):
        """
        Args:
            startIteration: Sets the start index of the iteration to predict. If <= 0, starts from the first iteration.
        """
    def setThresholds(self, value):
        """
        Args:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
    def getActualNumClasses(self):
        """
        Returns:
            actualNumClasses: Inferred number of classes based on dataset metadata or, if there is no metadata, unique count
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: features column name
        """
    def getFeaturesShapCol(self):
        """
        Returns:
            featuresShapCol: Output SHAP vector column name after prediction containing the feature contribution values
        """
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
    def getLeafPredictionCol(self):
        """
        Returns:
            leafPredictionCol: Predicted leaf indices's column name
        """
    def getLightGBMBooster(self):
        """
        Returns:
            lightGBMBooster: The trained LightGBM booster
        """
    def getNumIterations(self):
        """
        Returns:
            numIterations: Sets the total number of iterations used in the prediction.If <= 0, all iterations from ``start_iteration`` are used (no limits).
        """
    def getPredictDisableShapeCheck(self):
        """
        Returns:
            predictDisableShapeCheck: control whether or not LightGBM raises an error when you try to predict on data with a different number of features than the training data
        """
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
    def getProbabilityCol(self):
        """
        Returns:
            probabilityCol: Column name for predicted class conditional probabilities. Note: Not all models output well-calibrated probability estimates! These probabilities should be treated as confidences, not precise probabilities
        """
    def getRawPredictionCol(self):
        """
        Returns:
            rawPredictionCol: raw prediction (a.k.a. confidence) column name
        """
    def getStartIteration(self):
        """
        Returns:
            startIteration: Sets the start index of the iteration to predict. If <= 0, starts from the first iteration.
        """
    def getThresholds(self):
        """
        Returns:
            thresholds: Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes, with values > 0 excepting that at most one value may be 0. The class with largest value p/t is predicted, where p is the original probability of that class and t is the class's threshold
        """
