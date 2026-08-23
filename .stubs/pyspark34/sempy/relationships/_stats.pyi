import pandas as pd
from _typeshed import Incomplete
from typing import Any

VALUE: str
SIZE: str

class DataFrameStats:
    """
    Cache of the dataframe value statistics for improved performance of
    relationship operations.

    Parameters
    ----------
    name : str
        The table name
    df : pandas.DataFrame
        The source dataframe to extract value statistics from
    """
    name: Incomplete
    column_stats: dict[str, Any]
    df: Incomplete
    def __init__(self, name: str, df: pd.DataFrame) -> None: ...
    def __getitem__(self, key: str): ...

class PandasColumnStats:
    """
    Cache of the column value statistics for improved performance of
    relationship operations.

    Parameters
    ----------
    column : str
        The column name
    df : pandas.DataFrame
        The source dataframe to extract value statistics from
    """
    value_counts: Incomplete
    nrows: Incomplete
    null_count: Incomplete
    nunique: Incomplete
    max_value_count: Incomplete
    def __init__(self, column: str, df: pd.DataFrame) -> None: ...
    def intersect_count(self, other):
        """
        Computes the size of an intersect of unique values

        This is size of the intersection divided by size of own unique values.

        Parameters
        ----------
        other : ColumnStats
            the statistics of the column beting compared to

        Returns
        -------
        intersect_count : int
            Size of the intersect
        """
    def issubset(self, other):
        """
        Checks if this value set is the subset of the other for exact foreign key coverage

        Parameters
        ----------
        other : ColumnStats
            the statistics of the column beting compared to

        Returns
        -------
        issubset : bool
            True if this value set is subset of the other
        """
    def n_missing_keys(self, other, n_keys: int = 10):
        """
        Picks randomly the first n missing keys

        Parameters
        ----------
        other : ColumnStats
            the statistics of the column beting compared to
        n_keys : int
            the number of keys to return

        Returns
        -------
        missing_keys : List[Tuple]
            List of missing keys expressed as tuple
        """
