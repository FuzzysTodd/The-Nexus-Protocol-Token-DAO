from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from synapse.ml.automl._TuneHyperparametersModel import _TuneHyperparametersModel

basestring = str

class TuneHyperparametersModel(_TuneHyperparametersModel):
    def getBestModel(self):
        """
        Returns the best model.
        """
    def getBestModelInfo(self):
        """
        Returns the best model parameter info.
        """
