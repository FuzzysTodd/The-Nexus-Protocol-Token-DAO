import numpy as np
from _typeshed import Incomplete
from pandas._libs.window.indexers import calculate_variable_window_bounds as calculate_variable_window_bounds
from pandas.core.dtypes.common import ensure_platform_int as ensure_platform_int
from pandas.tseries.offsets import Nano as Nano
from pandas.util._decorators import Appender as Appender

get_window_bounds_doc: str

class BaseIndexer:
    """Base class for window bounds calculations."""
    index_array: Incomplete
    window_size: Incomplete
    def __init__(self, index_array: np.ndarray | None = None, window_size: int = 0, **kwargs) -> None:
        """
        Parameters
        ----------
        **kwargs :
            keyword arguments that will be available when get_window_bounds is called
        """
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class FixedWindowIndexer(BaseIndexer):
    """Creates window boundaries that are of fixed length."""
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class VariableWindowIndexer(BaseIndexer):
    """Creates window boundaries that are of variable length, namely for time series."""
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class VariableOffsetWindowIndexer(BaseIndexer):
    """Calculate window boundaries based on a non-fixed offset such as a BusinessDay."""
    index: Incomplete
    offset: Incomplete
    def __init__(self, index_array: np.ndarray | None = None, window_size: int = 0, index: Incomplete | None = None, offset: Incomplete | None = None, **kwargs) -> None: ...
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class ExpandingIndexer(BaseIndexer):
    """Calculate expanding window bounds, mimicking df.expanding()"""
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class FixedForwardWindowIndexer(BaseIndexer):
    """
    Creates window boundaries for fixed-length windows that include the current row.

    Examples
    --------
    >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
    >>> df
         B
    0  0.0
    1  1.0
    2  2.0
    3  NaN
    4  4.0

    >>> indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size=2)
    >>> df.rolling(window=indexer, min_periods=1).sum()
         B
    0  1.0
    1  3.0
    2  2.0
    3  4.0
    4  4.0
    """
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class GroupbyIndexer(BaseIndexer):
    """Calculate bounds to compute groupby rolling, mimicking df.groupby().rolling()"""
    groupby_indices: Incomplete
    window_indexer: Incomplete
    indexer_kwargs: Incomplete
    def __init__(self, index_array: np.ndarray | None = None, window_size: int | BaseIndexer = 0, groupby_indices: dict | None = None, window_indexer: type[BaseIndexer] = ..., indexer_kwargs: dict | None = None, **kwargs) -> None:
        """
        Parameters
        ----------
        index_array : np.ndarray or None
            np.ndarray of the index of the original object that we are performing
            a chained groupby operation over. This index has been pre-sorted relative to
            the groups
        window_size : int or BaseIndexer
            window size during the windowing operation
        groupby_indices : dict or None
            dict of {group label: [positional index of rows belonging to the group]}
        window_indexer : BaseIndexer
            BaseIndexer class determining the start and end bounds of each group
        indexer_kwargs : dict or None
            Custom kwargs to be passed to window_indexer
        **kwargs :
            keyword arguments that will be available when get_window_bounds is called
        """
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...

class ExponentialMovingWindowIndexer(BaseIndexer):
    """Calculate ewm window bounds (the entire window)"""
    def get_window_bounds(self, num_values: int = 0, min_periods: int | None = None, center: bool | None = None, closed: str | None = None, step: int | None = None) -> tuple[np.ndarray, np.ndarray]: ...
