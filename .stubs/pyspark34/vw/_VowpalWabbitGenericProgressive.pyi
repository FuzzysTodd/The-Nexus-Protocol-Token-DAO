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

class _VowpalWabbitGenericProgressive(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        hashSeed (int): Seed used for hashing
        ignoreNamespaces (str): Namespaces to be ignored (first letter only)
        initialModel (list): Initial model to start from
        inputCol (str): The name of the input column
        interactions (list): Interaction terms as specified by -q
        l1 (float): l_1 lambda
        l2 (float): l_2 lambda
        learningRate (float): Learning rate
        numBits (int): Number of bits used
        numPasses (int): Number of passes over the data
        numSyncsPerPass (int): Number of times weights should be synchronized within each pass. 0 disables inter-pass synchronization.
        passThroughArgs (str): VW command line arguments passed
        powerT (float): t power value
        useBarrierExecutionMode (bool): Use barrier execution mode, on by default.
    """
    hashSeed: Incomplete
    ignoreNamespaces: Incomplete
    initialModel: Incomplete
    inputCol: Incomplete
    interactions: Incomplete
    l1: Incomplete
    l2: Incomplete
    learningRate: Incomplete
    numBits: Incomplete
    numPasses: Incomplete
    numSyncsPerPass: Incomplete
    passThroughArgs: Incomplete
    powerT: Incomplete
    useBarrierExecutionMode: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, hashSeed: int = 0, ignoreNamespaces: Incomplete | None = None, initialModel: Incomplete | None = None, inputCol: str = 'input', interactions: Incomplete | None = None, l1: Incomplete | None = None, l2: Incomplete | None = None, learningRate: Incomplete | None = None, numBits: int = 18, numPasses: int = 1, numSyncsPerPass: int = 0, passThroughArgs: str = '', powerT: Incomplete | None = None, useBarrierExecutionMode: bool = True) -> None: ...
    def setParams(self, hashSeed: int = 0, ignoreNamespaces: Incomplete | None = None, initialModel: Incomplete | None = None, inputCol: str = 'input', interactions: Incomplete | None = None, l1: Incomplete | None = None, l2: Incomplete | None = None, learningRate: Incomplete | None = None, numBits: int = 18, numPasses: int = 1, numSyncsPerPass: int = 0, passThroughArgs: str = '', powerT: Incomplete | None = None, useBarrierExecutionMode: bool = True):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setHashSeed(self, value):
        """
        Args:
            hashSeed: Seed used for hashing
        """
    def setIgnoreNamespaces(self, value):
        """
        Args:
            ignoreNamespaces: Namespaces to be ignored (first letter only)
        """
    def setInitialModel(self, value):
        """
        Args:
            initialModel: Initial model to start from
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setInteractions(self, value):
        """
        Args:
            interactions: Interaction terms as specified by -q
        """
    def setL1(self, value):
        """
        Args:
            l1: l_1 lambda
        """
    def setL2(self, value):
        """
        Args:
            l2: l_2 lambda
        """
    def setLearningRate(self, value):
        """
        Args:
            learningRate: Learning rate
        """
    def setNumBits(self, value):
        """
        Args:
            numBits: Number of bits used
        """
    def setNumPasses(self, value):
        """
        Args:
            numPasses: Number of passes over the data
        """
    def setNumSyncsPerPass(self, value):
        """
        Args:
            numSyncsPerPass: Number of times weights should be synchronized within each pass. 0 disables inter-pass synchronization.
        """
    def setPassThroughArgs(self, value):
        """
        Args:
            passThroughArgs: VW command line arguments passed
        """
    def setPowerT(self, value):
        """
        Args:
            powerT: t power value
        """
    def setUseBarrierExecutionMode(self, value):
        """
        Args:
            useBarrierExecutionMode: Use barrier execution mode, on by default.
        """
    def getHashSeed(self):
        """
        Returns:
            hashSeed: Seed used for hashing
        """
    def getIgnoreNamespaces(self):
        """
        Returns:
            ignoreNamespaces: Namespaces to be ignored (first letter only)
        """
    def getInitialModel(self):
        """
        Returns:
            initialModel: Initial model to start from
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getInteractions(self):
        """
        Returns:
            interactions: Interaction terms as specified by -q
        """
    def getL1(self):
        """
        Returns:
            l1: l_1 lambda
        """
    def getL2(self):
        """
        Returns:
            l2: l_2 lambda
        """
    def getLearningRate(self):
        """
        Returns:
            learningRate: Learning rate
        """
    def getNumBits(self):
        """
        Returns:
            numBits: Number of bits used
        """
    def getNumPasses(self):
        """
        Returns:
            numPasses: Number of passes over the data
        """
    def getNumSyncsPerPass(self):
        """
        Returns:
            numSyncsPerPass: Number of times weights should be synchronized within each pass. 0 disables inter-pass synchronization.
        """
    def getPassThroughArgs(self):
        """
        Returns:
            passThroughArgs: VW command line arguments passed
        """
    def getPowerT(self):
        """
        Returns:
            powerT: t power value
        """
    def getUseBarrierExecutionMode(self):
        """
        Returns:
            useBarrierExecutionMode: Use barrier execution mode, on by default.
        """
