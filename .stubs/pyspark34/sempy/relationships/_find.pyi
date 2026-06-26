import pandas as pd
from sempy._utils._log import log_tables as log_tables
from sempy.relationships._multiplicity import Multiplicity as Multiplicity
from sempy.relationships._stats import DataFrameStats as DataFrameStats

def find_relationships(tables: dict[str, pd.DataFrame] | list[pd.DataFrame], coverage_threshold: float = 1.0, name_similarity_threshold: float = 0.8, exclude: list[tuple[str]] | pd.DataFrame | None = None, include_many_to_many: bool = False, verbose: int = 0) -> pd.DataFrame:
    '''
    Suggest possible relationships based on coverage threshold.

    By default `include_many_to_many` is `False`, which is the most common case.
    Generated relationship are m:1 (i.e. the "to" attribute is the primary key)
    and will also include 1:1 relationships.

    If `include_many_to_many` is set to `True` (less common case), we will search for additional many to many
    relationships. The results will be a superset of default m:1 case.

    Empty dataframes are not considered for relationships.

    Parameters
    ----------
    tables : dict[str, pandas.DataFrame] or list[pandas.DataFrame]
        A dictionary that maps table names to the dataframes with table content.
        If a list of dataframes is provided, the function will try to infer the names from the
        session variables and if it cannot, it will use the positional index to describe them in
        the results.
    coverage_threshold : float, default=1.0
        A minimum threshold to report a potential relationship. Coverage is a ratio of unique values in the
        "from" column that are found (covered by) the value in the "to" (key) column.
    name_similarity_threshold : float, default=0.8
        Minimum similarity of column names before analyzing for relationship.
        The value of 0 means that any 2 columns will be considered.
        The value of 1 means that only column that match exactly will be considered.
    exclude : pandas.DataFrame, default=None
        A dataframe with relationships to exclude. Its columns should  contain the columns
        "From Table", "From Column", "To Table", "To Column", which matches the output of
        :func:`~sempy.relationships.find_relationships`.
    include_many_to_many : bool, default=True
        Whether to also search for m:m relationships.
    verbose : int, default=0
        Verbosity. 0 means no verbosity.

    Returns
    -------
    pandas.DataFrame
        A dataframe with candidate relationships identified by: from_table, from_column,
        to_table, to_column. Also provides auxiliary statistics to help with evaluation.
        If no suitable candidates are found, returns an empty DataFrame.
    '''
def determine_multiplicity(stats_from, stats_to): ...
