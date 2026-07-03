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

class OrthoForestVariableTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        outcomeResidualCol (str): Outcome Residual Col
        outputCol (str): The name of the output column
        treatmentResidualCol (str): Treatment Residual Col
        weightsCol (str): Weights Col
    """
    outcomeResidualCol: Incomplete
    outputCol: Incomplete
    treatmentResidualCol: Incomplete
    weightsCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, outcomeResidualCol: str = 'OResid', outputCol: str = '_tmp_tsOutcome', treatmentResidualCol: str = 'TResid', weightsCol: str = '_tmp_twOutcome') -> None: ...
    def setParams(self, outcomeResidualCol: str = 'OResid', outputCol: str = '_tmp_tsOutcome', treatmentResidualCol: str = 'TResid', weightsCol: str = '_tmp_twOutcome'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setOutcomeResidualCol(self, value):
        """
        Args:
            outcomeResidualCol: Outcome Residual Col
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setTreatmentResidualCol(self, value):
        """
        Args:
            treatmentResidualCol: Treatment Residual Col
        """
    def setWeightsCol(self, value):
        """
        Args:
            weightsCol: Weights Col
        """
    def getOutcomeResidualCol(self):
        """
        Returns:
            outcomeResidualCol: Outcome Residual Col
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getTreatmentResidualCol(self):
        """
        Returns:
            treatmentResidualCol: Treatment Residual Col
        """
    def getWeightsCol(self):
        """
        Returns:
            weightsCol: Weights Col
        """
