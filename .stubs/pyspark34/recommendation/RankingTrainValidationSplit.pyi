from pyspark.ml.tuning import _ValidatorParams
from synapse.ml.recommendation._RankingTrainValidationSplit import _RankingTrainValidationSplit

basestring = str

class RankingTrainValidationSplit(_ValidatorParams, _RankingTrainValidationSplit):
    def __init__(self, **kwargs) -> None: ...
