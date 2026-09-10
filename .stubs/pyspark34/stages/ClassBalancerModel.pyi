from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class ClassBalancerModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        broadcastJoin (bool): whether to broadcast join
        inputCol (str): The name of the input column
        outputCol (str): The name of the output column
        weights (object): the dataframe of weights
    """
    broadcastJoin: Incomplete
    inputCol: Incomplete
    outputCol: Incomplete
    weights: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, broadcastJoin: Incomplete | None = None, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, weights: Incomplete | None = None) -> None: ...
    def setParams(self, broadcastJoin: Incomplete | None = None, inputCol: Incomplete | None = None, outputCol: Incomplete | None = None, weights: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBroadcastJoin(self, value):
        """
        Args:
            broadcastJoin: whether to broadcast join
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setWeights(self, value):
        """
        Args:
            weights: the dataframe of weights
        """
    def getBroadcastJoin(self):
        """
        Returns:
            broadcastJoin: whether to broadcast join
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getWeights(self):
        """
        Returns:
            weights: the dataframe of weights
        """
