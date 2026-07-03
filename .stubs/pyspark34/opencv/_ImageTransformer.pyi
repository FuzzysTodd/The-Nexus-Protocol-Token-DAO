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

class _ImageTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        autoConvertToColor (bool): Whether to automatically convert black and white images to color
        colorScaleFactor (float): The scale factor for color values. Used for normalization. The color values will be multiplied with the scale factor.
        ignoreDecodingErrors (bool): Whether to throw on decoding errors or just return null
        inputCol (str): The name of the input column
        normalizeMean (list): The mean value to use for normalization for each channel. The length of the array must match the number of channels of the input image.
        normalizeStd (list): The standard deviation to use for normalization for each channel. The length of the array must match the number of channels of the input image.
        outputCol (str): The name of the output column
        stages (object): Image transformation stages
        tensorChannelOrder (str): The color channel order of the output channels. Valid values are RGB and GBR. Default: RGB.
        tensorElementType (object): The element data type for the output tensor. Only used when toTensor is set to true. Valid values are DoubleType or FloatType. Default value: FloatType.
        toTensor (bool): Convert output image to tensor in the shape of (C * H * W)
    """
    autoConvertToColor: Incomplete
    colorScaleFactor: Incomplete
    ignoreDecodingErrors: Incomplete
    inputCol: Incomplete
    normalizeMean: Incomplete
    normalizeStd: Incomplete
    outputCol: Incomplete
    stages: Incomplete
    tensorChannelOrder: Incomplete
    tensorElementType: Incomplete
    toTensor: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, autoConvertToColor: bool = False, colorScaleFactor: Incomplete | None = None, ignoreDecodingErrors: bool = False, inputCol: str = 'image', normalizeMean: Incomplete | None = None, normalizeStd: Incomplete | None = None, outputCol: str = 'ImageTransformer_a702300092bb_output', stages: Incomplete | None = None, tensorChannelOrder: str = 'RGB', tensorElementType: Incomplete | None = None, toTensor: bool = False) -> None: ...
    def setParams(self, autoConvertToColor: bool = False, colorScaleFactor: Incomplete | None = None, ignoreDecodingErrors: bool = False, inputCol: str = 'image', normalizeMean: Incomplete | None = None, normalizeStd: Incomplete | None = None, outputCol: str = 'ImageTransformer_a702300092bb_output', stages: Incomplete | None = None, tensorChannelOrder: str = 'RGB', tensorElementType: Incomplete | None = None, toTensor: bool = False):
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
            autoConvertToColor: Whether to automatically convert black and white images to color
        """
    def setColorScaleFactor(self, value):
        """
        Args:
            colorScaleFactor: The scale factor for color values. Used for normalization. The color values will be multiplied with the scale factor.
        """
    def setIgnoreDecodingErrors(self, value):
        """
        Args:
            ignoreDecodingErrors: Whether to throw on decoding errors or just return null
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setNormalizeMean(self, value):
        """
        Args:
            normalizeMean: The mean value to use for normalization for each channel. The length of the array must match the number of channels of the input image.
        """
    def setNormalizeStd(self, value):
        """
        Args:
            normalizeStd: The standard deviation to use for normalization for each channel. The length of the array must match the number of channels of the input image.
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setStages(self, value):
        """
        Args:
            stages: Image transformation stages
        """
    def setTensorChannelOrder(self, value):
        """
        Args:
            tensorChannelOrder: The color channel order of the output channels. Valid values are RGB and GBR. Default: RGB.
        """
    def setTensorElementType(self, value):
        """
        Args:
            tensorElementType: The element data type for the output tensor. Only used when toTensor is set to true. Valid values are DoubleType or FloatType. Default value: FloatType.
        """
    def setToTensor(self, value):
        """
        Args:
            toTensor: Convert output image to tensor in the shape of (C * H * W)
        """
    def getAutoConvertToColor(self):
        """
        Returns:
            autoConvertToColor: Whether to automatically convert black and white images to color
        """
    def getColorScaleFactor(self):
        """
        Returns:
            colorScaleFactor: The scale factor for color values. Used for normalization. The color values will be multiplied with the scale factor.
        """
    def getIgnoreDecodingErrors(self):
        """
        Returns:
            ignoreDecodingErrors: Whether to throw on decoding errors or just return null
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getNormalizeMean(self):
        """
        Returns:
            normalizeMean: The mean value to use for normalization for each channel. The length of the array must match the number of channels of the input image.
        """
    def getNormalizeStd(self):
        """
        Returns:
            normalizeStd: The standard deviation to use for normalization for each channel. The length of the array must match the number of channels of the input image.
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getStages(self):
        """
        Returns:
            stages: Image transformation stages
        """
    def getTensorChannelOrder(self):
        """
        Returns:
            tensorChannelOrder: The color channel order of the output channels. Valid values are RGB and GBR. Default: RGB.
        """
    def getTensorElementType(self):
        """
        Returns:
            tensorElementType: The element data type for the output tensor. Only used when toTensor is set to true. Valid values are DoubleType or FloatType. Default value: FloatType.
        """
    def getToTensor(self):
        """
        Returns:
            toTensor: Convert output image to tensor in the shape of (C * H * W)
        """
