import pandas as pd
from numpy import ndarray
from sempy.functions import _SSeries
from typing import Any, Iterable

class FabricSeries(_SSeries):
    """
    A series for storage and propogation of PowerBI metadata.

    Parameters
    ----------
    data : numpy.ndarray, typing.Iterable, dict, pandas.Series, default=None
        Contains data stored in Series. If data is a dict, argument order is
        maintained. Can also be a scalar value.
    *args : list
        Remaining arguments to be passed to standard pandas constructor.
    column_metadata : dict, default=None
        Information about series column to be stored and propogated.
    **kwargs : dict
        Remaining kwargs to be passed to standard pandas constructor.
    """
    def __init__(self, data: ndarray | Iterable | dict | pd.DataFrame | None = None, *args: Any, column_metadata: dict[str, Any] | None = None, **kwargs: Any) -> None: ...
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
