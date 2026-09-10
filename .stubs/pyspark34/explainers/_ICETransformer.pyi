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

class _ICETransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        categoricalFeatures (object): The list of categorical features to explain.
        dependenceNameCol (str): Output column name which corresponds to dependence values of PDP-based-feature-importance option (kind == `feature`)
        featureNameCol (str): Output column name which corresponds to names of the features used in calculation of PDP-based-feature-importance option (kind == `feature`)
        kind (str): Whether to return the partial dependence plot (PDP) averaged across all the samples in the dataset or individual feature importance (ICE) per sample. Allowed values are "average" for PDP, "individual" for ICE and "feature" for PDP-based feature importance.
        model (object): The model to be interpreted.
        numSamples (int): Number of samples to generate.
        numericFeatures (object): The list of numeric features to explain.
        targetClasses (list): The indices of the classes for multinomial classification models. Default: 0.For regression models this parameter is ignored.
        targetClassesCol (str): The name of the column that specifies the indices of the classes for multinomial classification models.
        targetCol (str): The column name of the prediction target to explain (i.e. the response variable). This is usually set to "prediction" for regression models and "probability" for probabilistic classification models. Default value: probability
    '''
    categoricalFeatures: Incomplete
    dependenceNameCol: Incomplete
    featureNameCol: Incomplete
    kind: Incomplete
    model: Incomplete
    numSamples: Incomplete
    numericFeatures: Incomplete
    targetClasses: Incomplete
    targetClassesCol: Incomplete
    targetCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, categoricalFeatures=[], dependenceNameCol: str = 'pdpBasedDependence', featureNameCol: str = 'featureNames', kind: str = 'individual', model: Incomplete | None = None, numSamples: Incomplete | None = None, numericFeatures=[], targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability') -> None: ...
    def setParams(self, categoricalFeatures=[], dependenceNameCol: str = 'pdpBasedDependence', featureNameCol: str = 'featureNames', kind: str = 'individual', model: Incomplete | None = None, numSamples: Incomplete | None = None, numericFeatures=[], targetClasses=[], targetClassesCol: Incomplete | None = None, targetCol: str = 'probability'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setCategoricalFeatures(self, value):
        """
        Args:
            categoricalFeatures: The list of categorical features to explain.
        """
    def setDependenceNameCol(self, value):
        """
        Args:
            dependenceNameCol: Output column name which corresponds to dependence values of PDP-based-feature-importance option (kind == `feature`)
        """
    def setFeatureNameCol(self, value):
        """
        Args:
            featureNameCol: Output column name which corresponds to names of the features used in calculation of PDP-based-feature-importance option (kind == `feature`)
        """
    def setKind(self, value):
        '''
        Args:
            kind: Whether to return the partial dependence plot (PDP) averaged across all the samples in the dataset or individual feature importance (ICE) per sample. Allowed values are "average" for PDP, "individual" for ICE and "feature" for PDP-based feature importance.
        '''
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
    def setNumericFeatures(self, value):
        """
        Args:
            numericFeatures: The list of numeric features to explain.
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
    def getCategoricalFeatures(self):
        """
        Returns:
            categoricalFeatures: The list of categorical features to explain.
        """
    def getDependenceNameCol(self):
        """
        Returns:
            dependenceNameCol: Output column name which corresponds to dependence values of PDP-based-feature-importance option (kind == `feature`)
        """
    def getFeatureNameCol(self):
        """
        Returns:
            featureNameCol: Output column name which corresponds to names of the features used in calculation of PDP-based-feature-importance option (kind == `feature`)
        """
    def getKind(self):
        '''
        Returns:
            kind: Whether to return the partial dependence plot (PDP) averaged across all the samples in the dataset or individual feature importance (ICE) per sample. Allowed values are "average" for PDP, "individual" for ICE and "feature" for PDP-based feature importance.
        '''
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
    def getNumericFeatures(self):
        """
        Returns:
            numericFeatures: The list of numeric features to explain.
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
