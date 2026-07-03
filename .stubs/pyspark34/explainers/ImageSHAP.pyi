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

class ImageSHAP(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        cellSize (float): Number that controls the size of the superpixels
        infWeight (float): The double value to represent infinite weight. Default: 1E8.
        inputCol (str): input column name
        metricsCol (str): Column name for fitting metrics
        model (object): The model to be interpreted.
        modifier (float): Controls the trade-off spatial and color distance
        numSamples (int): Number of samples to generate.
        outputCol (str): output column name
        superpixelCol (str): The column holding the superpixel decompositions
        targetClasses (list): The indices of the classes for multinomial classification models. Default: 0.For regression models this parameter is ignored.
        targetClassesCol (str): The name of the column that specifies the indices of the classes for multinomial classification models.
        targetCol (str): The column name of the prediction target to explain (i.e. the response variable). This is usually set to "prediction" for regression models and "probability" for probabilistic classification models. Default value: probability
    '''
    cellSize: Incomplete
    infWeight: Incomplete
    inputCol: Incomplete
    metricsCol: Incomplete
    model: Incomplete
    modifier: Incomplete
    numSamples: Incomplete
    outputCol: Incomplete
    superpixelCol: Incomplete
    targetClasses: Incomplete
    targetClassesCol: Incomplete
    targetCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, cellSize: float = 16.0, infWeight: float = 100000000.0, inputCol: Incomplete | None = None, metricsCol: str = 'r2', model: Incomplete | None = None, modifier: float = 130.0, numSamples: Incomplete | None = None, outputCol: str = 'ImageSHAP_3c561e807e09__output', superpixelCol: str = 'superpixels', targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability') -> None: ...
    def setParams(self, cellSize: float = 16.0, infWeight: float = 100000000.0, inputCol: Incomplete | None = None, metricsCol: str = 'r2', model: Incomplete | None = None, modifier: float = 130.0, numSamples: Incomplete | None = None, outputCol: str = 'ImageSHAP_3c561e807e09__output', superpixelCol: str = 'superpixels', targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability'):
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
    def setInfWeight(self, value):
        """
        Args:
            infWeight: The double value to represent infinite weight. Default: 1E8.
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: input column name
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
    def getInfWeight(self):
        """
        Returns:
            infWeight: The double value to represent infinite weight. Default: 1E8.
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: input column name
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
