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

class TuneHyperparameters(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        evaluationMetric (str): Metric to evaluate models with
        models (object): Estimators to run
        numFolds (int): Number of folds
        numRuns (int): Termination criteria for randomized search
        parallelism (int): The number of models to run in parallel
        paramSpace (object): Parameter space for generating hyperparameters
        seed (long): Random number generator seed
    """
    evaluationMetric: Incomplete
    models: Incomplete
    numFolds: Incomplete
    numRuns: Incomplete
    parallelism: Incomplete
    paramSpace: Incomplete
    seed: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, evaluationMetric: Incomplete | None = None, models: Incomplete | None = None, numFolds: Incomplete | None = None, numRuns: Incomplete | None = None, parallelism: Incomplete | None = None, paramSpace: Incomplete | None = None, seed: int = 0) -> None: ...
    def setParams(self, evaluationMetric: Incomplete | None = None, models: Incomplete | None = None, numFolds: Incomplete | None = None, numRuns: Incomplete | None = None, parallelism: Incomplete | None = None, paramSpace: Incomplete | None = None, seed: int = 0):
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
            models: Estimators to run
        """
    def setNumFolds(self, value):
        """
        Args:
            numFolds: Number of folds
        """
    def setNumRuns(self, value):
        """
        Args:
            numRuns: Termination criteria for randomized search
        """
    def setParallelism(self, value):
        """
        Args:
            parallelism: The number of models to run in parallel
        """
    def setParamSpace(self, value):
        """
        Args:
            paramSpace: Parameter space for generating hyperparameters
        """
    def setSeed(self, value):
        """
        Args:
            seed: Random number generator seed
        """
    def getEvaluationMetric(self):
        """
        Returns:
            evaluationMetric: Metric to evaluate models with
        """
    def getModels(self):
        """
        Returns:
            models: Estimators to run
        """
    def getNumFolds(self):
        """
        Returns:
            numFolds: Number of folds
        """
    def getNumRuns(self):
        """
        Returns:
            numRuns: Termination criteria for randomized search
        """
    def getParallelism(self):
        """
        Returns:
            parallelism: The number of models to run in parallel
        """
    def getParamSpace(self):
        """
        Returns:
            paramSpace: Parameter space for generating hyperparameters
        """
    def getSeed(self):
        """
        Returns:
            seed: Random number generator seed
        """
