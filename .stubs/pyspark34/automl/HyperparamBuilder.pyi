from pyspark.sql.types import *
from _typeshed import Incomplete
from pyspark.ml.common import inherit_doc as inherit_doc

basestring = str

class HyperparamBuilder:
    """
    Specifies the search space for hyperparameters.
    """
    jvm: Incomplete
    hyperparams: Incomplete
    def __init__(self) -> None: ...
    def addHyperparam(self, est, param, hyperParam):
        """
        Add a hyperparam to the builder

        Args:
            param (Param): The param to tune
            dist (Dist): Distribution of values

        """
    def build(self):
        """
        Builds the search space of hyperparameters, returns the map of hyperparameters to search through.

        """

class DiscreteHyperParam:
    """
    Specifies a discrete list of values.
    """
    jvm: Incomplete
    hyperParam: Incomplete
    def __init__(self, values, seed: int = 0) -> None: ...
    def get(self): ...

class RangeHyperParam:
    """
    Specifies a range of values.
    """
    jvm: Incomplete
    rangeParam: Incomplete
    def __init__(self, min, max, seed: int = 0) -> None: ...
    def get(self): ...

class GridSpace:
    """
    Specifies a predetermined grid of values to search through.
    """
    jvm: Incomplete
    gridSpace: Incomplete
    def __init__(self, paramValues) -> None: ...
    def space(self): ...

class RandomSpace:
    """
    Specifies a random streaming range of values to search through.
    """
    jvm: Incomplete
    paramSpace: Incomplete
    def __init__(self, paramDistributions) -> None: ...
    def space(self): ...
