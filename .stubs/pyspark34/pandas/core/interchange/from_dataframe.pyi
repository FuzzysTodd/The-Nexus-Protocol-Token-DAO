import numpy as np
import pandas as pd
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.interchange.dataframe_protocol import Buffer as Buffer, Column as Column, ColumnNullType as ColumnNullType, DataFrame as DataFrameXchg, DtypeKind as DtypeKind
from pandas.core.interchange.utils import ArrowCTypes as ArrowCTypes, Endianness as Endianness
from typing import Any

def from_dataframe(df, allow_copy: bool = True) -> pd.DataFrame:
    """
    Build a ``pd.DataFrame`` from any DataFrame supporting the interchange protocol.

    Parameters
    ----------
    df : DataFrameXchg
        Object supporting the interchange protocol, i.e. `__dataframe__` method.
    allow_copy : bool, default: True
        Whether to allow copying the memory to perform the conversion
        (if false then zero-copy approach is requested).

    Returns
    -------
    pd.DataFrame
    """
def protocol_df_chunk_to_pandas(df: DataFrameXchg) -> pd.DataFrame:
    """
    Convert interchange protocol chunk to ``pd.DataFrame``.

    Parameters
    ----------
    df : DataFrameXchg

    Returns
    -------
    pd.DataFrame
    """
def primitive_column_to_ndarray(col: Column) -> tuple[np.ndarray, Any]:
    """
    Convert a column holding one of the primitive dtypes to a NumPy array.

    A primitive type is one of: int, uint, float, bool.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
        that keeps the memory alive.
    """
def categorical_column_to_series(col: Column) -> tuple[pd.Series, Any]:
    """
    Convert a column holding categorical data to a pandas Series.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of pd.Series holding the data and the memory owner object
        that keeps the memory alive.
    """
def string_column_to_ndarray(col: Column) -> tuple[np.ndarray, Any]:
    """
    Convert a column holding string data to a NumPy array.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
        that keeps the memory alive.
    """
def parse_datetime_format_str(format_str, data):
    """Parse datetime `format_str` to interpret the `data`."""
def datetime_column_to_ndarray(col: Column) -> tuple[np.ndarray, Any]:
    """
    Convert a column holding DateTime data to a NumPy array.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
        that keeps the memory alive.
    """
def buffer_to_ndarray(buffer: Buffer, dtype: tuple[DtypeKind, int, str, str], *, length: int, offset: int = 0) -> np.ndarray:
    """
    Build a NumPy array from the passed buffer.

    Parameters
    ----------
    buffer : Buffer
        Buffer to build a NumPy array from.
    dtype : tuple
        Data type of the buffer conforming protocol dtypes format.
    offset : int, default: 0
        Number of elements to offset from the start of the buffer.
    length : int, optional
        If the buffer is a bit-mask, specifies a number of bits to read
        from the buffer. Has no effect otherwise.

    Returns
    -------
    np.ndarray

    Notes
    -----
    The returned array doesn't own the memory. The caller of this function is
    responsible for keeping the memory owner object alive as long as
    the returned NumPy array is being used.
    """
def set_nulls(data: np.ndarray | pd.Series, col: Column, validity: tuple[Buffer, tuple[DtypeKind, int, str, str]] | None, allow_modify_inplace: bool = True):
    """
    Set null values for the data according to the column null kind.

    Parameters
    ----------
    data : np.ndarray or pd.Series
        Data to set nulls in.
    col : Column
        Column object that describes the `data`.
    validity : tuple(Buffer, dtype) or None
        The return value of ``col.buffers()``. We do not access the ``col.buffers()``
        here to not take the ownership of the memory of buffer objects.
    allow_modify_inplace : bool, default: True
        Whether to modify the `data` inplace when zero-copy is possible (True) or always
        modify a copy of the `data` (False).

    Returns
    -------
    np.ndarray or pd.Series
        Data with the nulls being set.
    """
