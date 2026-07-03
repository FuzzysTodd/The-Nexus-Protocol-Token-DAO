from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.param import TypeConverters as TypeConverters
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class Lambda(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        transformFunc (object): holder for dataframe function
        transformSchemaFunc (object): the output schema after the transformation
    """
    transformFunc: Incomplete
    transformSchemaFunc: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, transformFunc: Incomplete | None = None, transformSchemaFunc: Incomplete | None = None) -> None: ...
    def setParams(self, transformFunc: Incomplete | None = None, transformSchemaFunc: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setTransformFunc(self, value):
        """
        Args:
            transformFunc: holder for dataframe function
        """
    def setTransformSchemaFunc(self, value):
        """
        Args:
            transformSchemaFunc: the output schema after the transformation
        """
    def getTransformFunc(self):
        """
        Returns:
            transformFunc: holder for dataframe function
        """
    def getTransformSchemaFunc(self):
        """
        Returns:
            transformSchemaFunc: the output schema after the transformation
        """
