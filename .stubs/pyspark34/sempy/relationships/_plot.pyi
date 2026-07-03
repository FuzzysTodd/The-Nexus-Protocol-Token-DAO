import graphviz
import pandas as pd
from sempy._utils._log import log_tables as log_tables
from sempy.relationships._multiplicity import Multiplicity as Multiplicity

def plot_relationship_metadata(metadata_df: pd.DataFrame, tables: dict[str, pd.DataFrame] | list[pd.DataFrame] | None = None, include_columns: str = 'keys', missing_key_errors: str = 'raise', *, graph_attributes: dict | None = None) -> graphviz.Digraph:
    '''
    Plot a graph of relationships based on metadata contained in the provided dataframe.

    The input "metadata" dataframe should contain one row per relationship.
    Each row names the "from" and "to" table/columns that participate in the relationship, and their
    multiplicity as defined by :func:`~sempy.relationships.Multiplicity`.

    Parameters
    ----------
    metadata_df : pandas.DataFrame, default=None
        A "metadata" dataframe with relationships to plot. It should  contain the columns  "multiplicity",
        "From Table", "From Column", "To Table", "To Column", which matches the
        output of :func:`~sempy.relationships.find_relationships`.
    tables : dict[str, pandas.DataFrame] or list[pandas.DataFrame], default=None
        It needs to provided only when `include_columns` = \'all\' and it will be used
        for mapping table names from relationships to the dataframe columns.
    include_columns : str, default=\'keys\'
        One of \'keys\', \'all\', \'none\'. Indicates which columns should be included in the graph.
    missing_key_errors : str, default=\'raise\'
        One of \'raise\', \'warn\', \'ignore\'. Action to take when either table or column
        of the relationship is not found in the elements of the argument *tables*.
    graph_attributes : dict, default=None
        Attributes passed to graphviz. Note that all values need to be strings. Useful attributes are:

        - *rankdir*: "TB" (top-bottom) or "LR" (left-right)
        - *dpi*:  "100", "30", etc. (dots per inch)
        - *splines*: "ortho", "compound", "line", "curved", "spline" (line shape)

    Returns
    -------
    graphviz.Digraph
        Graph object containing all relationships.
        If include_attributes is true, attributes are represented as ports in the graph.
    '''
