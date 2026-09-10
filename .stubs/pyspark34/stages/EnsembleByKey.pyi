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

class EnsembleByKey(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        colNames (list): Names of the result of each col
        collapseGroup (bool): Whether to collapse all items in group to one entry
        cols (list): Cols to ensemble
        keys (list): Keys to group by
        strategy (str): How to ensemble the scores, ex: mean
        vectorDims (dict): the dimensions of any vector columns, used to avoid materialization
    """
    colNames: Incomplete
    collapseGroup: Incomplete
    cols: Incomplete
    keys: Incomplete
    strategy: Incomplete
    vectorDims: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, colNames: Incomplete | None = None, collapseGroup: bool = True, cols: Incomplete | None = None, keys: Incomplete | None = None, strategy: str = 'mean', vectorDims: Incomplete | None = None) -> None: ...
    def setParams(self, colNames: Incomplete | None = None, collapseGroup: bool = True, cols: Incomplete | None = None, keys: Incomplete | None = None, strategy: str = 'mean', vectorDims: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setColNames(self, value):
        """
        Args:
            colNames: Names of the result of each col
        """
    def setCollapseGroup(self, value):
        """
        Args:
            collapseGroup: Whether to collapse all items in group to one entry
        """
    def setCols(self, value):
        """
        Args:
            cols: Cols to ensemble
        """
    def setKeys(self, value):
        """
        Args:
            keys: Keys to group by
        """
    def setStrategy(self, value):
        """
        Args:
            strategy: How to ensemble the scores, ex: mean
        """
    def setVectorDims(self, value):
        """
        Args:
            vectorDims: the dimensions of any vector columns, used to avoid materialization
        """
    def getColNames(self):
        """
        Returns:
            colNames: Names of the result of each col
        """
    def getCollapseGroup(self):
        """
        Returns:
            collapseGroup: Whether to collapse all items in group to one entry
        """
    def getCols(self):
        """
        Returns:
            cols: Cols to ensemble
        """
    def getKeys(self):
        """
        Returns:
            keys: Keys to group by
        """
    def getStrategy(self):
        """
        Returns:
            strategy: How to ensemble the scores, ex: mean
        """
    def getVectorDims(self):
        """
        Returns:
            vectorDims: the dimensions of any vector columns, used to avoid materialization
        """
