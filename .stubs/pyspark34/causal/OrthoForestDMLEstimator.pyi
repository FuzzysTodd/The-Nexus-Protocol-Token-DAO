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

class OrthoForestDMLEstimator(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        confidenceLevel (float): confidence level, default value is 0.975
        confounderVecCol (str): Confounders to control for
        featuresCol (str): The name of the features column
        heterogeneityVecCol (str): Vector to divide the treatment by
        maxDepth (int): Max Depth of Tree
        maxIter (int): maximum number of iterations (>= 0)
        minSamplesLeaf (int): Max Depth of Tree
        numTrees (int): Number of trees
        outcomeCol (str): outcome column
        outcomeModel (object): outcome model to run
        outcomeResidualCol (str): Outcome Residual Column
        outputCol (str): The name of the output column
        outputHighCol (str): Output Confidence Interval Low
        outputLowCol (str): Output Confidence Interval Low
        parallelism (int): the number of threads to use when running parallel algorithms
        sampleSplitRatio (list): Sample split ratio for cross-fitting. Default: [0.5, 0.5].
        treatmentCol (str): treatment column
        treatmentModel (object): treatment model to run
        treatmentResidualCol (str): Treatment Residual Column
        weightCol (str): The name of the weight column
    """
    confidenceLevel: Incomplete
    confounderVecCol: Incomplete
    featuresCol: Incomplete
    heterogeneityVecCol: Incomplete
    maxDepth: Incomplete
    maxIter: Incomplete
    minSamplesLeaf: Incomplete
    numTrees: Incomplete
    outcomeCol: Incomplete
    outcomeModel: Incomplete
    outcomeResidualCol: Incomplete
    outputCol: Incomplete
    outputHighCol: Incomplete
    outputLowCol: Incomplete
    parallelism: Incomplete
    sampleSplitRatio: Incomplete
    treatmentCol: Incomplete
    treatmentModel: Incomplete
    treatmentResidualCol: Incomplete
    weightCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, confidenceLevel: float = 0.975, confounderVecCol: str = 'XW', featuresCol: Incomplete | None = None, heterogeneityVecCol: str = 'X', maxDepth: int = 5, maxIter: int = 1, minSamplesLeaf: int = 10, numTrees: int = 20, outcomeCol: Incomplete | None = None, outcomeModel: Incomplete | None = None, outcomeResidualCol: str = 'OutcomeResidual', outputCol: str = 'EffectAverage', outputHighCol: str = 'EffectUpperBound', outputLowCol: str = 'EffectLowerBound', parallelism: int = 10, sampleSplitRatio=[0.5, 0.5], treatmentCol: Incomplete | None = None, treatmentModel: Incomplete | None = None, treatmentResidualCol: str = 'TreatmentResidual', weightCol: Incomplete | None = None) -> None: ...
    def setParams(self, confidenceLevel: float = 0.975, confounderVecCol: str = 'XW', featuresCol: Incomplete | None = None, heterogeneityVecCol: str = 'X', maxDepth: int = 5, maxIter: int = 1, minSamplesLeaf: int = 10, numTrees: int = 20, outcomeCol: Incomplete | None = None, outcomeModel: Incomplete | None = None, outcomeResidualCol: str = 'OutcomeResidual', outputCol: str = 'EffectAverage', outputHighCol: str = 'EffectUpperBound', outputLowCol: str = 'EffectLowerBound', parallelism: int = 10, sampleSplitRatio=[0.5, 0.5], treatmentCol: Incomplete | None = None, treatmentModel: Incomplete | None = None, treatmentResidualCol: str = 'TreatmentResidual', weightCol: Incomplete | None = None):
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
    def setConfounderVecCol(self, value):
        """
        Args:
            confounderVecCol: Confounders to control for
        """
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: The name of the features column
        """
    def setHeterogeneityVecCol(self, value):
        """
        Args:
            heterogeneityVecCol: Vector to divide the treatment by
        """
    def setMaxDepth(self, value):
        """
        Args:
            maxDepth: Max Depth of Tree
        """
    def setMaxIter(self, value):
        """
        Args:
            maxIter: maximum number of iterations (>= 0)
        """
    def setMinSamplesLeaf(self, value):
        """
        Args:
            minSamplesLeaf: Max Depth of Tree
        """
    def setNumTrees(self, value):
        """
        Args:
            numTrees: Number of trees
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
    def setOutcomeResidualCol(self, value):
        """
        Args:
            outcomeResidualCol: Outcome Residual Column
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setOutputHighCol(self, value):
        """
        Args:
            outputHighCol: Output Confidence Interval Low
        """
    def setOutputLowCol(self, value):
        """
        Args:
            outputLowCol: Output Confidence Interval Low
        """
    def setParallelism(self, value):
        """
        Args:
            parallelism: the number of threads to use when running parallel algorithms
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
    def setTreatmentResidualCol(self, value):
        """
        Args:
            treatmentResidualCol: Treatment Residual Column
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
    def getConfounderVecCol(self):
        """
        Returns:
            confounderVecCol: Confounders to control for
        """
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: The name of the features column
        """
    def getHeterogeneityVecCol(self):
        """
        Returns:
            heterogeneityVecCol: Vector to divide the treatment by
        """
    def getMaxDepth(self):
        """
        Returns:
            maxDepth: Max Depth of Tree
        """
    def getMaxIter(self):
        """
        Returns:
            maxIter: maximum number of iterations (>= 0)
        """
    def getMinSamplesLeaf(self):
        """
        Returns:
            minSamplesLeaf: Max Depth of Tree
        """
    def getNumTrees(self):
        """
        Returns:
            numTrees: Number of trees
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
    def getOutcomeResidualCol(self):
        """
        Returns:
            outcomeResidualCol: Outcome Residual Column
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getOutputHighCol(self):
        """
        Returns:
            outputHighCol: Output Confidence Interval Low
        """
    def getOutputLowCol(self):
        """
        Returns:
            outputLowCol: Output Confidence Interval Low
        """
    def getParallelism(self):
        """
        Returns:
            parallelism: the number of threads to use when running parallel algorithms
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
    def getTreatmentResidualCol(self):
        """
        Returns:
            treatmentResidualCol: Treatment Residual Column
        """
    def getWeightCol(self):
        """
        Returns:
            weightCol: The name of the weight column
        """
