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

class ImageLIME(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        cellSize (float): Number that controls the size of the superpixels
        inputCol (str): input column name
        kernelWidth (float): Kernel width. Default value: sqrt (number of features) * 0.75
        metricsCol (str): Column name for fitting metrics
        model (object): The model to be interpreted.
        modifier (float): Controls the trade-off spatial and color distance
        numSamples (int): Number of samples to generate.
        outputCol (str): output column name
        regularization (float): Regularization param for the lasso. Default value: 0.
        samplingFraction (float): The fraction of superpixels (for image) or tokens (for text) to keep on
        superpixelCol (str): The column holding the superpixel decompositions
        targetClasses (list): The indices of the classes for multinomial classification models. Default: 0.For regression models this parameter is ignored.
        targetClassesCol (str): The name of the column that specifies the indices of the classes for multinomial classification models.
        targetCol (str): The column name of the prediction target to explain (i.e. the response variable). This is usually set to "prediction" for regression models and "probability" for probabilistic classification models. Default value: probability
    '''
    cellSize: Incomplete
    inputCol: Incomplete
    kernelWidth: Incomplete
    metricsCol: Incomplete
    model: Incomplete
    modifier: Incomplete
    numSamples: Incomplete
    outputCol: Incomplete
    regularization: Incomplete
    samplingFraction: Incomplete
    superpixelCol: Incomplete
    targetClasses: Incomplete
    targetClassesCol: Incomplete
    targetCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, cellSize: float = 16.0, inputCol: Incomplete | None = None, kernelWidth: float = 0.75, metricsCol: str = 'r2', model: Incomplete | None = None, modifier: float = 130.0, numSamples: int = 900, outputCol: str = 'ImageLIME_4e3e263ec78e__output', regularization: float = 0.0, samplingFraction: float = 0.7, superpixelCol: str = 'superpixels', targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability') -> None: ...
    def setParams(self, cellSize: float = 16.0, inputCol: Incomplete | None = None, kernelWidth: float = 0.75, metricsCol: str = 'r2', model: Incomplete | None = None, modifier: float = 130.0, numSamples: int = 900, outputCol: str = 'ImageLIME_4e3e263ec78e__output', regularization: float = 0.0, samplingFraction: float = 0.7, superpixelCol: str = 'superpixels', targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setCellSize(self, value):
        """
        Args:
            cellSize: Number that controls the size of the superpixels
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: input column name
        """
    def setKernelWidth(self, value):
        """
        Args:
            kernelWidth: Kernel width. Default value: sqrt (number of features) * 0.75
        """
    def setMetricsCol(self, value):
        """
        Args:
            metricsCol: Column name for fitting metrics
        """
    def setModel(self, value):
        """
        Args:
            model: The model to be interpreted.
        """
    def setModifier(self, value):
        """
        Args:
            modifier: Controls the trade-off spatial and color distance
        """
    def setNumSamples(self, value):
        """
        Args:
            numSamples: Number of samples to generate.
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: output column name
        """
    def setRegularization(self, value):
        """
        Args:
            regularization: Regularization param for the lasso. Default value: 0.
        """
    def setSamplingFraction(self, value):
        """
        Args:
            samplingFraction: The fraction of superpixels (for image) or tokens (for text) to keep on
        """
    def setSuperpixelCol(self, value):
        """
        Args:
            superpixelCol: The column holding the superpixel decompositions
        """
    def setTargetClasses(self, value):
        """
        Args:
            targetClasses: The indices of the classes for multinomial classification models. Default: 0.For regression models this parameter is ignored.
        """
    def setTargetClassesCol(self, value):
        """
        Args:
            targetClassesCol: The name of the column that specifies the indices of the classes for multinomial classification models.
        """
    def setTargetCol(self, value):
        '''
        Args:
            targetCol: The column name of the prediction target to explain (i.e. the response variable). This is usually set to "prediction" for regression models and "probability" for probabilistic classification models. Default value: probability
        '''
    def getCellSize(self):
        """
        Returns:
            cellSize: Number that controls the size of the superpixels
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: input column name
        """
    def getKernelWidth(self):
        """
        Returns:
            kernelWidth: Kernel width. Default value: sqrt (number of features) * 0.75
        """
    def getMetricsCol(self):
        """
        Returns:
            metricsCol: Column name for fitting metrics
        """
    def getModel(self):
        """
        Returns:
            model: The model to be interpreted.
        """
    def getModifier(self):
        """
        Returns:
            modifier: Controls the trade-off spatial and color distance
        """
    def getNumSamples(self):
        """
        Returns:
            numSamples: Number of samples to generate.
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: output column name
        """
    def getRegularization(self):
        """
        Returns:
            regularization: Regularization param for the lasso. Default value: 0.
        """
    def getSamplingFraction(self):
        """
        Returns:
            samplingFraction: The fraction of superpixels (for image) or tokens (for text) to keep on
        """
    def getSuperpixelCol(self):
        """
        Returns:
            superpixelCol: The column holding the superpixel decompositions
        """
    def getTargetClasses(self):
        """
        Returns:
            targetClasses: The indices of the classes for multinomial classification models. Default: 0.For regression models this parameter is ignored.
        """
    def getTargetClassesCol(self):
        """
        Returns:
            targetClassesCol: The name of the column that specifies the indices of the classes for multinomial classification models.
        """
    def getTargetCol(self):
        '''
        Returns:
            targetCol: The column name of the prediction target to explain (i.e. the response variable). This is usually set to "prediction" for regression models and "probability" for probabilistic classification models. Default value: probability
        '''
