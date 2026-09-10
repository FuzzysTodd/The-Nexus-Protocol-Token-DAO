import abc
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Generator
from statsmodels.compat.python import with_metaclass as with_metaclass

class BaseCrossValidator(Incomplete, metaclass=abc.ABCMeta):
    """
    The BaseCrossValidator class is a base class for all the iterators that
    split the data in train and test as for example KFolds or LeavePOut
    """
    def __init__(self) -> None: ...
    @abstractmethod
    def split(self): ...

class KFold(BaseCrossValidator):
    """
    K-Folds cross validation iterator:
    Provides train/test indexes to split data in train test sets

    Parameters
    ----------
    k: int
        number of folds
    shuffle : bool
        If true, then the index is shuffled before splitting into train and
        test indices.

    Notes
    -----
    All folds except for last fold have size trunc(n/k), the last fold has
    the remainder.
    """
    nobs: Incomplete
    k_folds: Incomplete
    shuffle: Incomplete
    def __init__(self, k_folds, shuffle: bool = False) -> None: ...
    def split(self, X, y: Incomplete | None = None, label: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """yield index split into train and test sets
        """
