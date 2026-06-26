import pandas as pd
from numpy import ndarray
from typing import Any, Iterable

class MDataFrame(pd.DataFrame):
    """
    An extension of a Pandas DataFrame that allows storage and propogation of column metadata.

    For operations between multiple objects, propogation is as follows:
        * ``merge`` - left object's metadata takes precedence.
        * ``concat`` - first object's metadata is used.

    Parameters
    ----------
    data : ndarray (structured or homogeneous), Iterable, dict or DataFrame
        Dict can contain Series, arrays, constants, dataclass or list-like objects. If
        data is a dict, column order follows insertion-order. If a dict contains Series
        which have an index defined, it is aligned by its index. This alignment also
        occurs if data is a Series or a DataFrame itself. Alignment is done on
        Series/DataFrame inputs.

        If data is a list of dicts, column order follows insertion-order.
    *args : Any
        Remaining arguments to be passed to standard pandas constructor.
    column_metadata : dict, default=None
        Information about dataframe columns to be stored and propogated.
    **kwargs : Any
        Remaining kwargs to be passed to standard pandas constructor.
    """
    def __init__(self, data: ndarray | Iterable | dict | pd.DataFrame | None = None, *args: Any, column_metadata: dict[str, Any] | None = None, **kwargs: Any) -> None: ...
    def __finalize__(self, other, method: str | None = None, **kwargs) -> MDataFrame:
        '''
        Override pandas __finalize__ to propagate metadata from other to self

        This is the only method of propagation for "General functions" such as
        pandas.concat([df1, df2]), pandas.merge(df1, df2) that are not executed on an object instance.
        Overriding the DataFrame method is therefore not an option.
        '''
    def to_parquet(self, path: Any, *args, **kwargs) -> None:
        """
        Write the DataFrame including metadata to a parquet file specified by path parameter using Arrow.

        Parameters
        ----------
        path : Any
            String containing the filepath to where the parquet should be saved.
        *args : Any
            Other args to be passed to PyArrow ``write_table``.
        **kwargs : Any
            Other kwargs to be passed to PyArrow ``write_table``.
        """
    @property
    def column_metadata(self) -> dict | None:
        """
        Information for the columns in the table.
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
    def __getattribute__(self, name: str) -> Any:
        """
        Override/wrap pandas calls to tweak metadata.

        This could also be done by defining methods explicitly. Current arguments for doing it here:
        1. Likely less code, as multiple methods can be handled by a single code fragment.
        2. 'Catch all' approach will hopefully cover future needs.

        This design decision should be continuously evaluated as the code evolves.
        """
