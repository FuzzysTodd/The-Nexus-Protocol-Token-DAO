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

class VowpalWabbitDSJsonTransformer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        dsJsonColumn (str): Column containing ds-json. defaults to "value".
        rewards (dict): Extract bandit reward(s) from DS json. Defaults to _label_cost.
    '''
    dsJsonColumn: Incomplete
    rewards: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, dsJsonColumn: str = 'value', rewards={'reward': '_label_cost'}) -> None: ...
    def setParams(self, dsJsonColumn: str = 'value', rewards={'reward': '_label_cost'}):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setDsJsonColumn(self, value):
        '''
        Args:
            dsJsonColumn: Column containing ds-json. defaults to "value".
        '''
    def setRewards(self, value):
        """
        Args:
            rewards: Extract bandit reward(s) from DS json. Defaults to _label_cost.
        """
    def getDsJsonColumn(self):
        '''
        Returns:
            dsJsonColumn: Column containing ds-json. defaults to "value".
        '''
    def getRewards(self):
        """
        Returns:
            rewards: Extract bandit reward(s) from DS json. Defaults to _label_cost.
        """
