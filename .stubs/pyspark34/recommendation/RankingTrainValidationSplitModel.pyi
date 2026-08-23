from pyspark.ml.util import *
from synapse.ml.recommendation._RankingTrainValidationSplitModel import _RankingTrainValidationSplitModel

basestring = str

class RankingTrainValidationSplitModel(_RankingTrainValidationSplitModel):
    def recommendForAllUsers(self, numItems): ...
    def recommendForAllItems(self, numUsers): ...
