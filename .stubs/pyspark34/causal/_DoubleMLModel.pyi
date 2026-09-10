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

class _DoubleMLModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        confidenceLevel (float): confidence level, default value is 0.975
        featuresCol (str): The name of the features column
        maxIter (int): maximum number of iterations (>= 0)
        outcomeCol (str): outcome column
        outcomeModel (object): outcome model to run
        parallelism (int): the number of threads to use when running parallel algorithms
        rawTreatmentEffects (list): raw treatment effect results for all iterations
        sampleSplitRatio (list): Sample split ratio for cross-fitting. Default: [0.5, 0.5].
        treatmentCol (str): treatment column
        treatmentModel (object): treatment model to run
        weightCol (str): The name of the weight column
    """
    confidenceLevel: Incomplete
    featuresCol: Incomplete
    maxIter: Incomplete
    outcomeCol: Incomplete
    outcomeModel: Incomplete
    parallelism: Incomplete
    rawTreatmentEffects: Incomplete
    sampleSplitRatio: Incomplete
    treatmentCol: Incomplete
    treatmentModel: Incomplete
    weightCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, confidenceLevel: float = 0.975, featuresCol: Incomplete | None = None, maxIter: int = 1, outcomeCol: Incomplete | None = None, outcomeModel: Incomplete | None = None, parallelism: int = 10, rawTreatmentEffects: Incomplete | None = None, sampleSplitRatio=[0.5, 0.5], treatmentCol: Incomplete | None = None, treatmentModel: Incomplete | None = None, weightCol: Incomplete | None = None) -> None: ...
    def setParams(self, confidenceLevel: float = 0.975, featuresCol: Incomplete | None = None, maxIter: int = 1, outcomeCol: Incomplete | None = None, outcomeModel: Incomplete | None = None, parallelism: int = 10, rawTreatmentEffects: Incomplete | None = None, sampleSplitRatio=[0.5, 0.5], treatmentCol: Incomplete | None = None, treatmentModel: Incomplete | None = None, weightCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setConfidenceLevel(self, value):
        """
        Args:
            confidenceLevel: confidence level, default value is 0.975
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: The name of the features column
        """
    def setMaxIter(self, value):
        """
        Args:
            maxIter: maximum number of iterations (>= 0)
        """
    def setOutcomeCol(self, value):
        """
        Args:
            outcomeCol: outcome column
        """
    def setOutcomeModel(self, value):
        """
        Args:
            outcomeModel: outcome model to run
        """
    def setParallelism(self, value):
        """
        Args:
            parallelism: the number of threads to use when running parallel algorithms
        """
    def setRawTreatmentEffects(self, value):
        """
        Args:
            rawTreatmentEffects: raw treatment effect results for all iterations
        """
    def setSampleSplitRatio(self, value):
        """
        Args:
            sampleSplitRatio: Sample split ratio for cross-fitting. Default: [0.5, 0.5].
        """
    def setTreatmentCol(self, value):
        """
        Args:
            treatmentCol: treatment column
        """
    def setTreatmentModel(self, value):
        """
        Args:
            treatmentModel: treatment model to run
        """
    def setWeightCol(self, value):
        """
        Args:
            weightCol: The name of the weight column
        """
    def getConfidenceLevel(self):
        """
        Returns:
            confidenceLevel: confidence level, default value is 0.975
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The name of the features column
        """
    def getMaxIter(self):
        """
        Returns:
            maxIter: maximum number of iterations (>= 0)
        """
    def getOutcomeCol(self):
        """
        Returns:
            outcomeCol: outcome column
        """
    def getOutcomeModel(self):
        """
        Returns:
            outcomeModel: outcome model to run
        """
    def getParallelism(self):
        """
        Returns:
            parallelism: the number of threads to use when running parallel algorithms
        """
    def getRawTreatmentEffects(self):
        """
        Returns:
            rawTreatmentEffects: raw treatment effect results for all iterations
        """
    def getSampleSplitRatio(self):
        """
        Returns:
            sampleSplitRatio: Sample split ratio for cross-fitting. Default: [0.5, 0.5].
        """
    def getTreatmentCol(self):
        """
        Returns:
            treatmentCol: treatment column
        """
    def getTreatmentModel(self):
        """
        Returns:
            treatmentModel: treatment model to run
        """
    def getWeightCol(self):
        """
        Returns:
            weightCol: The name of the weight column
        """
