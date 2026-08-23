import numpy as np
from pandas import DataFrame as DataFrame, MultiIndex as MultiIndex, Series as Series, concat as concat
from pandas._typing import Dict as Dict, IndexLabel as IndexLabel
from pandas.core.dtypes.missing import remove_na_arraylike as remove_na_arraylike
from pandas.plotting._matplotlib.misc import unpack_single_str_list as unpack_single_str_list

def create_iter_data_given_by(data: DataFrame, kind: str = 'hist') -> Dict[str, DataFrame | Series]:
    """
    Create data for iteration given `by` is assigned or not, and it is only
    used in both hist and boxplot.

    If `by` is assigned, return a dictionary of DataFrames in which the key of
    dictionary is the values in groups.
    If `by` is not assigned, return input as is, and this preserves current
    status of iter_data.

    Parameters
    ----------
    data : reformatted grouped data from `_compute_plot_data` method.
    kind : str, plot kind. This function is only used for `hist` and `box` plots.

    Returns
    -------
    iter_data : DataFrame or Dictionary of DataFrames

    Examples
    --------
    If `by` is assigned:

    >>> import numpy as np
    >>> tuples = [('h1', 'a'), ('h1', 'b'), ('h2', 'a'), ('h2', 'b')]
    >>> mi = MultiIndex.from_tuples(tuples)
    >>> value = [[1, 3, np.nan, np.nan],
    ...          [3, 4, np.nan, np.nan], [np.nan, np.nan, 5, 6]]
    >>> data = DataFrame(value, columns=mi)
    >>> create_iter_data_given_by(data)
    {'h1':     h1
         a    b
    0  1.0  3.0
    1  3.0  4.0
    2  NaN  NaN, 'h2':     h2
         a    b
    0  NaN  NaN
    1  NaN  NaN
    2  5.0  6.0}
    """
def reconstruct_data_with_by(data: DataFrame, by: IndexLabel, cols: IndexLabel) -> DataFrame:
    """
    Internal function to group data, and reassign multiindex column names onto the
    result in order to let grouped data be used in _compute_plot_data method.

    Parameters
    ----------
    data : Original DataFrame to plot
    by : grouped `by` parameter selected by users
    cols : columns of data set (excluding columns used in `by`)

    Returns
    -------
    Output is the reconstructed DataFrame with MultiIndex columns. The first level
    of MI is unique values of groups, and second level of MI is the columns
    selected by users.

    Examples
    --------
    >>> d = {'h': ['h1', 'h1', 'h2'], 'a': [1, 3, 5], 'b': [3, 4, 6]}
    >>> df = DataFrame(d)
    >>> reconstruct_data_with_by(df, by='h', cols=['a', 'b'])
       h1      h2
       a     b     a     b
    0  1.0   3.0   NaN   NaN
    1  3.0   4.0   NaN   NaN
    2  NaN   NaN   5.0   6.0
    """
def reformat_hist_y_given_by(y: Series | np.ndarray, by: IndexLabel | None) -> Series | np.ndarray:
    """Internal function to reformat y given `by` is applied or not for hist plot.

    If by is None, input y is 1-d with NaN removed; and if by is not None, groupby
    will take place and input y is multi-dimensional array.
    """
