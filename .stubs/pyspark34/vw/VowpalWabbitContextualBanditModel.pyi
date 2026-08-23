from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.vw.VowpalWabbitPythonBase import VowpalWabbitPythonBaseModel
from synapse.ml.vw._VowpalWabbitContextualBanditModel import _VowpalWabbitContextualBanditModel

class VowpalWabbitContextualBanditModel(_VowpalWabbitContextualBanditModel, VowpalWabbitPythonBaseModel): ...
