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

class _ONNXModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        argMaxDict (dict): A map between output dataframe columns, where the value column will be computed from taking the argmax of the key column. This can be used to convert probability output to predicted label.
        deviceType (str): Specify a device type the model inference runs on. Supported types are: CPU or CUDA.If not specified, auto detection will be used.
        feedDict (dict):  Provide a map from CNTK/ONNX model input variable names (keys) to column names of the input dataframe (values)
        fetchDict (dict): Provide a map from column names of the output dataframe (keys) to CNTK/ONNX model output variable names (values)
        miniBatcher (object): Minibatcher to use
        modelPayload (list): Array of bytes containing the serialized ONNX model.
        optimizationLevel (str): Specify the optimization level for the ONNX graph optimizations. Details at https://onnxruntime.ai/docs/resources/graph-optimizations.html#graph-optimization-levels. Supported values are: NO_OPT; BASIC_OPT; EXTENDED_OPT; ALL_OPT. Default: ALL_OPT.
        softMaxDict (dict): A map between output dataframe columns, where the value column will be computed from taking the softmax of the key column. If the \'rawPrediction\' column contains logits outputs, then one can set softMaxDict to `Map("rawPrediction" -> "probability")` to obtain the probability outputs.
    '''
    argMaxDict: Incomplete
    deviceType: Incomplete
    feedDict: Incomplete
    fetchDict: Incomplete
    miniBatcher: Incomplete
    modelPayload: Incomplete
    optimizationLevel: Incomplete
    softMaxDict: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, argMaxDict: Incomplete | None = None, deviceType: Incomplete | None = None, feedDict: Incomplete | None = None, fetchDict: Incomplete | None = None, miniBatcher: Incomplete | None = None, modelPayload: Incomplete | None = None, optimizationLevel: str = 'ALL_OPT', softMaxDict: Incomplete | None = None) -> None: ...
    def setParams(self, argMaxDict: Incomplete | None = None, deviceType: Incomplete | None = None, feedDict: Incomplete | None = None, fetchDict: Incomplete | None = None, miniBatcher: Incomplete | None = None, modelPayload: Incomplete | None = None, optimizationLevel: str = 'ALL_OPT', softMaxDict: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setArgMaxDict(self, value):
        """
        Args:
            argMaxDict: A map between output dataframe columns, where the value column will be computed from taking the argmax of the key column. This can be used to convert probability output to predicted label.
        """
    def setDeviceType(self, value):
        """
        Args:
            deviceType: Specify a device type the model inference runs on. Supported types are: CPU or CUDA.If not specified, auto detection will be used.
        """
    def setFeedDict(self, value):
        """
        Args:
            feedDict:  Provide a map from CNTK/ONNX model input variable names (keys) to column names of the input dataframe (values)
        """
    def setFetchDict(self, value):
        """
        Args:
            fetchDict: Provide a map from column names of the output dataframe (keys) to CNTK/ONNX model output variable names (values)
        """
    def setMiniBatcher(self, value):
        """
        Args:
            miniBatcher: Minibatcher to use
        """
    def setModelPayload(self, value):
        """
        Args:
            modelPayload: Array of bytes containing the serialized ONNX model.
        """
    def setOptimizationLevel(self, value):
        """
        Args:
            optimizationLevel: Specify the optimization level for the ONNX graph optimizations. Details at https://onnxruntime.ai/docs/resources/graph-optimizations.html#graph-optimization-levels. Supported values are: NO_OPT; BASIC_OPT; EXTENDED_OPT; ALL_OPT. Default: ALL_OPT.
        """
    def setSoftMaxDict(self, value):
        '''
        Args:
            softMaxDict: A map between output dataframe columns, where the value column will be computed from taking the softmax of the key column. If the \'rawPrediction\' column contains logits outputs, then one can set softMaxDict to `Map("rawPrediction" -> "probability")` to obtain the probability outputs.
        '''
    def getArgMaxDict(self):
        """
        Returns:
            argMaxDict: A map between output dataframe columns, where the value column will be computed from taking the argmax of the key column. This can be used to convert probability output to predicted label.
        """
    def getDeviceType(self):
        """
        Returns:
            deviceType: Specify a device type the model inference runs on. Supported types are: CPU or CUDA.If not specified, auto detection will be used.
        """
    def getFeedDict(self):
        """
        Returns:
            feedDict:  Provide a map from CNTK/ONNX model input variable names (keys) to column names of the input dataframe (values)
        """
    def getFetchDict(self):
        """
        Returns:
            fetchDict: Provide a map from column names of the output dataframe (keys) to CNTK/ONNX model output variable names (values)
        """
    def getMiniBatcher(self):
        """
        Returns:
            miniBatcher: Minibatcher to use
        """
    def getModelPayload(self):
        """
        Returns:
            modelPayload: Array of bytes containing the serialized ONNX model.
        """
    def getOptimizationLevel(self):
        """
        Returns:
            optimizationLevel: Specify the optimization level for the ONNX graph optimizations. Details at https://onnxruntime.ai/docs/resources/graph-optimizations.html#graph-optimization-levels. Supported values are: NO_OPT; BASIC_OPT; EXTENDED_OPT; ALL_OPT. Default: ALL_OPT.
        """
    def getSoftMaxDict(self):
        '''
        Returns:
            softMaxDict: A map between output dataframe columns, where the value column will be computed from taking the softmax of the key column. If the \'rawPrediction\' column contains logits outputs, then one can set softMaxDict to `Map("rawPrediction" -> "probability")` to obtain the probability outputs.
        '''
