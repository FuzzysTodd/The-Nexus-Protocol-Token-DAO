import pandas as pd
from _typeshed import Incomplete
from typing import Any

class MSeries(pd.Series):
    """
    An extension of a Pandas Series that allows storage and propogation of column metadata.

    Parameters
    ----------
    data : numpy.ndarray, iterable, dict or scalar value
        Contains data stored in Series. If data is a dict, argument order is
        maintained.
    *args : Any
        Remaining arguments to be passed to standard pandas constructor.
    column_metadata : dict, default=None
        Information about series column to be stored and propogated.
    **kwargs : Any
        Remaining kwargs to be passed to standard pandas constructor.
    """
    def __init__(self, data: Incomplete | None = None, *args, column_metadata: dict[str, Any] | None = None, **kwargs) -> None: ...
    def __finalize__(self, other, method: str | None = None, **kwargs) -> MSeries:
        """Override pandas __finalize__ to propagate metadata from other to self"""
    @property
    def column_metadata(self) -> dict | None:
        """
        Information for Series values.
        """
    @column_metadata.setter
    def column_metadata(self, value: dict | None) -> None:
        """
        Update column_metadata to new value.

        Parameters
        ----------
        value : dict
            New value for column_metadata.
        """
