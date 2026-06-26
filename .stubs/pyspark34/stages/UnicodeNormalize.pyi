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

class UnicodeNormalize(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        form (str): Unicode normalization form: NFC, NFD, NFKC, NFKD
        inputCol (str): The name of the input column
        lower (bool): Lowercase text
        outputCol (str): The name of the output column
    """
    form: Incomplete
    inputCol: Incomplete
    lower: Incomplete
    outputCol: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, form: Incomplete | None = None, inputCol: Incomplete | None = None, lower: Incomplete | None = None, outputCol: Incomplete | None = None) -> None: ...
    def setParams(self, form: Incomplete | None = None, inputCol: Incomplete | None = None, lower: Incomplete | None = None, outputCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setForm(self, value):
        """
        Args:
            form: Unicode normalization form: NFC, NFD, NFKC, NFKD
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setLower(self, value):
        """
        Args:
            lower: Lowercase text
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def getForm(self):
        """
        Returns:
            form: Unicode normalization form: NFC, NFD, NFKC, NFKD
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getLower(self):
        """
        Returns:
            lower: Lowercase text
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
