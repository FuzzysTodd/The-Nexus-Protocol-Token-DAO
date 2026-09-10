import pandas as pd
from sempy._utils._log import log_tables as log_tables
from sempy.relationships._multiplicity import Multiplicity as Multiplicity
from sempy.relationships._stats import DataFrameStats as DataFrameStats

def list_relationship_violations(tables: dict[str, pd.DataFrame] | list[pd.DataFrame], relationships: pd.DataFrame, missing_key_errors: str = 'raise', coverage_threshold: float = 1.0, n_keys: int = 10) -> pd.DataFrame:
    '''
    Validate to see if the content of tables matches relationships.

    The function examines results of joins for provided relationships and
    searches for inconsistencies with the specified relationship multiplicity.

    Relationships from empty tables (dataframes) are assumed as valid.

    Parameters
    ----------
    tables : dict[str, pandas.DataFrame] or list[pandas.DataFrame]
        A dictionary that maps table names to the dataframes with table content.
        If a list of dataframes is provided, the function will try to infer the names from the
        session variables and if it cannot, it will use the positional index to describe them in
        the results.
    relationships : pandas.DataFrame
        A dataframe with relationships to use for validation. Its columns should  contain the columns
        "Multiplicity", "From Table", "From Column", "To Table", "To Column", which matches the
        output of :func:`~sempy.relationships.find_relationships`.
    missing_key_errors : str, default=\'raise\'
        One of \'raise\', \'warn\', \'ignore\'. Action to take when either table or column
        of the relationship is not found in the elements of the argument *tables*.
    coverage_threshold : float, default=1.0
        Fraction of rows in the "from" part that need to join in inner join.
    n_keys : int, default=10
        Number of missing keys to report. Random collection can be reported.

    Returns
    -------
    pandas.DataFrame
        Dataframe with relationships, error type and error message.
        If there are no violations, returns an empty DataFrame.
    '''
