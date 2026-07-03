from _typeshed import Incomplete

class DataFrameDependencyStats:
    """
    Cache of the dataframe value statistics for improved performance of
    dependency operations.

    Parameters
    ----------
    df : pandas or pyspark.pandas dataframe
        The source dataframe to extract value statistics from
    """
    column_stats: Incomplete
    df: Incomplete
    nrows: Incomplete
    def __init__(self, df) -> None: ...
    def __getitem__(self, key): ...
    def confirm_dependency(self, determinant_col, dependent_col, verbose: int = 0): ...
    def conditional_entropy(self, a, b, dropna, verbose: int = 0):
        """
        Conditional entropy H(a|b) and H(b|a) for columns a and b

        Parameters
        ----------
        a : str
            First column name
        b : str
            Second column name

        Returns
        -------
        h_a_b : float
            Conditional entropy of a given b.
        h_b_a : float
            Conditional entropy of b given a.
        """

class PandasColumnDependencyStats:
    """
    Cache of the column value statistics for improved performance of
    relationship operations.

    Parameters
    ----------
    column : str
        Column names
    df : dataframe
        The source dataframe to extract value statistics from
    nrows : int
        Number of rows in the dataframe
    """
    codes: Incomplete
    nunique_null_inclusive: Incomplete
    null_mask: Incomplete
    null_count: Incomplete
    cached_entropy: Incomplete
    def __init__(self, column, df, nrows) -> None: ...
    def entropy(self): ...
