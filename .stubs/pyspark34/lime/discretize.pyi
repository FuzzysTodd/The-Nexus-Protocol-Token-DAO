import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod

class BaseDiscretizer(metaclass=abc.ABCMeta):
    """
    Abstract class - Build a class that inherits from this class to implement
    a custom discretizer.
    Method bins() is to be redefined in the child class, as it is the actual
    custom part of the discretizer.
    """
    __metaclass__ = ABCMeta
    to_discretize: Incomplete
    data_stats: Incomplete
    names: Incomplete
    lambdas: Incomplete
    means: Incomplete
    stds: Incomplete
    mins: Incomplete
    maxs: Incomplete
    random_state: Incomplete
    def __init__(self, data, categorical_features, feature_names, labels: Incomplete | None = None, random_state: Incomplete | None = None, data_stats: Incomplete | None = None) -> None:
        """Initializer
        Args:
            data: numpy 2d array
            categorical_features: list of indices (ints) corresponding to the
                categorical columns. These features will not be discretized.
                Everything else will be considered continuous, and will be
                discretized.
            categorical_names: map from int to list of names, where
                categorical_names[x][y] represents the name of the yth value of
                column x.
            feature_names: list of names (strings) corresponding to the columns
                in the training data.
            data_stats: must have 'means', 'stds', 'mins' and 'maxs', use this
                if you don't want these values to be computed from data
        """
    @abstractmethod
    def bins(self, data, labels):
        """
        To be overridden
        Returns for each feature to discretize the boundaries
        that form each bin of the discretizer
        """
    def discretize(self, data):
        """Discretizes the data.
        Args:
            data: numpy 2d or 1d array
        Returns:
            numpy array of same dimension, discretized.
        """
    def get_undiscretize_values(self, feature, values): ...
    def undiscretize(self, data): ...

class StatsDiscretizer(BaseDiscretizer):
    """
        Class to be used to supply the data stats info when discretize_continuous is true
    """
    def __init__(self, data, categorical_features, feature_names, labels: Incomplete | None = None, random_state: Incomplete | None = None, data_stats: Incomplete | None = None) -> None: ...
    def bins(self, data, labels): ...

class QuartileDiscretizer(BaseDiscretizer):
    def __init__(self, data, categorical_features, feature_names, labels: Incomplete | None = None, random_state: Incomplete | None = None) -> None: ...
    def bins(self, data, labels): ...

class DecileDiscretizer(BaseDiscretizer):
    def __init__(self, data, categorical_features, feature_names, labels: Incomplete | None = None, random_state: Incomplete | None = None) -> None: ...
    def bins(self, data, labels): ...

class EntropyDiscretizer(BaseDiscretizer):
    def __init__(self, data, categorical_features, feature_names, labels: Incomplete | None = None, random_state: Incomplete | None = None) -> None: ...
    def bins(self, data, labels): ...
