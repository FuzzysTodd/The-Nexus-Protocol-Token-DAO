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

class _ImageFeaturizer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        autoConvertToColor (bool): Whether to automatically convert black and white images to color. default = true
        channelNormalizationMeans (list): Normalization means for color channels
        channelNormalizationStds (list): Normalization std's for color channels
        colorScaleFactor (float): Color scale factor
        dropNa (bool): Whether to drop na values before mapping
        featureTensorName (str): the name of the tensor to include in the fetch dict
        headless (bool): whether to use the feature tensor or the output tensor
        ignoreDecodingErrors (bool): Whether to throw on decoding errors or just return None
        imageHeight (int): Size required by model
        imageTensorName (str): the name of the tensor to include in the fetch dict
        imageWidth (int): Size required by model
        inputCol (str): The name of the input column
        onnxModel (object): The internal ONNX model used in the featurizer
        outputCol (str): The name of the output column
        outputTensorName (str): the name of the tensor to include in the fetch dict
    """
    autoConvertToColor: Incomplete
    channelNormalizationMeans: Incomplete
    channelNormalizationStds: Incomplete
    colorScaleFactor: Incomplete
    dropNa: Incomplete
    featureTensorName: Incomplete
    headless: Incomplete
    ignoreDecodingErrors: Incomplete
    imageHeight: Incomplete
    imageTensorName: Incomplete
    imageWidth: Incomplete
    inputCol: Incomplete
    onnxModel: Incomplete
    outputCol: Incomplete
    outputTensorName: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, autoConvertToColor: bool = True, channelNormalizationMeans=[0.485, 0.456, 0.406], channelNormalizationStds=[0.229, 0.224, 0.225], colorScaleFactor: float = 0.00392156862745098, dropNa: bool = True, featureTensorName: Incomplete | None = None, headless: bool = True, ignoreDecodingErrors: bool = False, imageHeight: Incomplete | None = None, imageTensorName: Incomplete | None = None, imageWidth: Incomplete | None = None, inputCol: Incomplete | None = None, onnxModel: Incomplete | None = None, outputCol: str = 'ImageFeaturizer_ddb7a15cc8d5_output', outputTensorName: str = '') -> None: ...
    def setParams(self, autoConvertToColor: bool = True, channelNormalizationMeans=[0.485, 0.456, 0.406], channelNormalizationStds=[0.229, 0.224, 0.225], colorScaleFactor: float = 0.00392156862745098, dropNa: bool = True, featureTensorName: Incomplete | None = None, headless: bool = True, ignoreDecodingErrors: bool = False, imageHeight: Incomplete | None = None, imageTensorName: Incomplete | None = None, imageWidth: Incomplete | None = None, inputCol: Incomplete | None = None, onnxModel: Incomplete | None = None, outputCol: str = 'ImageFeaturizer_ddb7a15cc8d5_output', outputTensorName: str = ''):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAutoConvertToColor(self, value):
        """
        Args:
            autoConvertToColor: Whether to automatically convert black and white images to color. default = true
        """
    def setChannelNormalizationMeans(self, value):
        """
        Args:
            channelNormalizationMeans: Normalization means for color channels
        """
    def setChannelNormalizationStds(self, value):
        """
        Args:
            channelNormalizationStds: Normalization std's for color channels
        """
    def setColorScaleFactor(self, value):
        """
        Args:
            colorScaleFactor: Color scale factor
        """
    def setDropNa(self, value):
        """
        Args:
            dropNa: Whether to drop na values before mapping
        """
    def setFeatureTensorName(self, value):
        """
        Args:
            featureTensorName: the name of the tensor to include in the fetch dict
        """
    def setHeadless(self, value):
        """
        Args:
            headless: whether to use the feature tensor or the output tensor
        """
    def setIgnoreDecodingErrors(self, value):
        """
        Args:
            ignoreDecodingErrors: Whether to throw on decoding errors or just return None
        """
    def setImageHeight(self, value):
        """
        Args:
            imageHeight: Size required by model
        """
    def setImageTensorName(self, value):
        """
        Args:
            imageTensorName: the name of the tensor to include in the fetch dict
        """
    def setImageWidth(self, value):
        """
        Args:
            imageWidth: Size required by model
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setOnnxModel(self, value):
        """
        Args:
            onnxModel: The internal ONNX model used in the featurizer
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setOutputTensorName(self, value):
        """
        Args:
            outputTensorName: the name of the tensor to include in the fetch dict
        """
    def getAutoConvertToColor(self):
        """
        Returns:
            autoConvertToColor: Whether to automatically convert black and white images to color. default = true
        """
    def getChannelNormalizationMeans(self):
        """
        Returns:
            channelNormalizationMeans: Normalization means for color channels
        """
    def getChannelNormalizationStds(self):
        """
        Returns:
            channelNormalizationStds: Normalization std's for color channels
        """
    def getColorScaleFactor(self):
        """
        Returns:
            colorScaleFactor: Color scale factor
        """
    def getDropNa(self):
        """
        Returns:
            dropNa: Whether to drop na values before mapping
        """
    def getFeatureTensorName(self):
        """
        Returns:
            featureTensorName: the name of the tensor to include in the fetch dict
        """
    def getHeadless(self):
        """
        Returns:
            headless: whether to use the feature tensor or the output tensor
        """
    def getIgnoreDecodingErrors(self):
        """
        Returns:
            ignoreDecodingErrors: Whether to throw on decoding errors or just return None
        """
    def getImageHeight(self):
        """
        Returns:
            imageHeight: Size required by model
        """
    def getImageTensorName(self):
        """
        Returns:
            imageTensorName: the name of the tensor to include in the fetch dict
        """
    def getImageWidth(self):
        """
        Returns:
            imageWidth: Size required by model
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getOnnxModel(self):
        """
        Returns:
            onnxModel: The internal ONNX model used in the featurizer
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getOutputTensorName(self):
        """
        Returns:
            outputTensorName: the name of the tensor to include in the fetch dict
        """
