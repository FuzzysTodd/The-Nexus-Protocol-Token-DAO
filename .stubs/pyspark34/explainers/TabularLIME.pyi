from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class TabularLIME(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        backgroundData (object): A dataframe containing background data
        categoricalFeatures (list): Name of features that should be treated as categorical variables.
        inputCols (list): input column names
        kernelWidth (float): Kernel width. Default value: sqrt (number of features) * 0.75
        metricsCol (str): Column name for fitting metrics
        model (object): The model to be interpreted.
        numSamples (int): Number of samples to generate.
        outputCol (str): output column name
        regularization (float): Regularization param for the lasso. Default value: 0.
        targetClasses (list): The indices of the classes for multinomial classification models. Default: 0.For regression models this parameter is ignored.
        targetClassesCol (str): The name of the column that specifies the indices of the classes for multinomial classification models.
        targetCol (str): The column name of the prediction target to explain (i.e. the response variable). This is usually set to "prediction" for regression models and "probability" for probabilistic classification models. Default value: probability
    '''
    backgroundData: Incomplete
    categoricalFeatures: Incomplete
    inputCols: Incomplete
    kernelWidth: Incomplete
    metricsCol: Incomplete
    model: Incomplete
    numSamples: Incomplete
    outputCol: Incomplete
    regularization: Incomplete
    targetClasses: Incomplete
    targetClassesCol: Incomplete
    targetCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, backgroundData: Incomplete | None = None, categoricalFeatures=[], inputCols: Incomplete | None = None, kernelWidth: float = 0.75, metricsCol: str = 'r2', model: Incomplete | None = None, numSamples: int = 1000, outputCol: str = 'TabularLIME_ed37bbcbe88f__output', regularization: float = 0.0, targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability') -> None: ...
    def setParams(self, backgroundData: Incomplete | None = None, categoricalFeatures=[], inputCols: Incomplete | None = None, kernelWidth: float = 0.75, metricsCol: str = 'r2', model: Incomplete | None = None, numSamples: int = 1000, outputCol: str = 'TabularLIME_ed37bbcbe88f__output', regularization: float = 0.0, targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBackgroundData(self, value):
        """
        Args:
            backgroundData: A dataframe containing background data
        """
    def setCategoricalFeatures(self, value):
        """
        Args:
            categoricalFeatures: Name of features that should be treated as categorical variables.
        """
    def setInputCols(self, value):
        """
        Args:
            inputCols: input column names
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
    def getBackgroundData(self):
        """
        Returns:
            backgroundData: A dataframe containing background data
        """
    def getCategoricalFeatures(self):
        """
        Returns:
            categoricalFeatures: Name of features that should be treated as categorical variables.
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: input column names
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
