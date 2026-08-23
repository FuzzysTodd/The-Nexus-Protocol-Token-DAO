from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.vw.VowpalWabbitPythonBase import VowpalWabbitPythonBaseModel
from synapse.ml.vw._VowpalWabbitGenericModel import _VowpalWabbitGenericModel

class VowpalWabbitGenericModel(_VowpalWabbitGenericModel, VowpalWabbitPythonBaseModel): ...
