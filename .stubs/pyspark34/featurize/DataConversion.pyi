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

class DataConversion(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        cols (list): Comma separated list of columns whose type will be converted
        convertTo (str): The result type
        dateTimeFormat (str): Format for DateTime when making DateTime:String conversions
    """
    cols: Incomplete
    convertTo: Incomplete
    dateTimeFormat: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, cols: Incomplete | None = None, convertTo: str = '', dateTimeFormat: str = 'yyyy-MM-dd HH:mm:ss') -> None: ...
    def setParams(self, cols: Incomplete | None = None, convertTo: str = '', dateTimeFormat: str = 'yyyy-MM-dd HH:mm:ss'):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setCols(self, value):
        """
        Args:
            cols: Comma separated list of columns whose type will be converted
        """
    def setConvertTo(self, value):
        """
        Args:
            convertTo: The result type
        """
    def setDateTimeFormat(self, value):
        """
        Args:
            dateTimeFormat: Format for DateTime when making DateTime:String conversions
        """
    def getCols(self):
        """
        Returns:
            cols: Comma separated list of columns whose type will be converted
        """
    def getConvertTo(self):
        """
        Returns:
            convertTo: The result type
        """
    def getDateTimeFormat(self):
        """
        Returns:
            dateTimeFormat: Format for DateTime when making DateTime:String conversions
        """
