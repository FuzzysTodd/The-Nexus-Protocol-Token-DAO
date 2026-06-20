from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class TimerModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        disableMaterialization (bool): Whether to disable timing (so that one can turn it off for evaluation)
        logToScala (bool): Whether to output the time to the scala console
        stage (object): The stage to time
        transformer (object): inner model to time
    """
    disableMaterialization: Incomplete
    logToScala: Incomplete
    stage: Incomplete
    transformer: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, disableMaterialization: bool = True, logToScala: bool = True, stage: Incomplete | None = None, transformer: Incomplete | None = None) -> None: ...
    def setParams(self, disableMaterialization: bool = True, logToScala: bool = True, stage: Incomplete | None = None, transformer: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setDisableMaterialization(self, value):
        """
        Args:
            disableMaterialization: Whether to disable timing (so that one can turn it off for evaluation)
        """
    def setLogToScala(self, value):
        """
        Args:
            logToScala: Whether to output the time to the scala console
        """
    def setStage(self, value):
        """
        Args:
            stage: The stage to time
        """
    def setTransformer(self, value):
        """
        Args:
            transformer: inner model to time
        """
    def getDisableMaterialization(self):
        """
        Returns:
            disableMaterialization: Whether to disable timing (so that one can turn it off for evaluation)
        """
    def getLogToScala(self):
        """
        Returns:
            logToScala: Whether to output the time to the scala console
        """
    def getStage(self):
        """
        Returns:
            stage: The stage to time
        """
    def getTransformer(self):
        """
        Returns:
            transformer: inner model to time
        """
