from _typeshed import Incomplete
from pandas import DataFrame as DataFrame
from pandas._libs import lib as lib
from pandas._typing import AggFuncType as AggFuncType, AggFuncTypeBase as AggFuncTypeBase, AggFuncTypeDict as AggFuncTypeDict, IndexLabel as IndexLabel
from pandas.core.dtypes.cast import maybe_downcast_to_dtype as maybe_downcast_to_dtype
from pandas.core.dtypes.common import is_extension_array_dtype as is_extension_array_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_nested_list_like as is_nested_list_like, is_scalar as is_scalar
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.groupby import Grouper as Grouper
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, get_objs_combined_axis as get_objs_combined_axis
from pandas.core.reshape.concat import concat as concat
from pandas.core.reshape.util import cartesian_product as cartesian_product
from pandas.core.series import Series as Series
from pandas.util._decorators import Appender as Appender, Substitution as Substitution
from typing import Hashable

def pivot_table(data: DataFrame, values: Incomplete | None = None, index: Incomplete | None = None, columns: Incomplete | None = None, aggfunc: AggFuncType = 'mean', fill_value: Incomplete | None = None, margins: bool = False, dropna: bool = True, margins_name: Hashable = 'All', observed: bool = False, sort: bool = True) -> DataFrame: ...
def pivot(data: DataFrame, *, columns: IndexLabel, index: IndexLabel | lib.NoDefault = ..., values: IndexLabel | lib.NoDefault = ...) -> DataFrame: ...
def crosstab(index, columns, values: Incomplete | None = None, rownames: Incomplete | None = None, colnames: Incomplete | None = None, aggfunc: Incomplete | None = None, margins: bool = False, margins_name: Hashable = 'All', dropna: bool = True, normalize: bool = False) -> DataFrame:
    '''
    Compute a simple cross tabulation of two (or more) factors.

    By default, computes a frequency table of the factors unless an
    array of values and an aggregation function are passed.

    Parameters
    ----------
    index : array-like, Series, or list of arrays/Series
        Values to group by in the rows.
    columns : array-like, Series, or list of arrays/Series
        Values to group by in the columns.
    values : array-like, optional
        Array of values to aggregate according to the factors.
        Requires `aggfunc` be specified.
    rownames : sequence, default None
        If passed, must match number of row arrays passed.
    colnames : sequence, default None
        If passed, must match number of column arrays passed.
    aggfunc : function, optional
        If specified, requires `values` be specified as well.
    margins : bool, default False
        Add row/column margins (subtotals).
    margins_name : str, default \'All\'
        Name of the row/column that will contain the totals
        when margins is True.
    dropna : bool, default True
        Do not include columns whose entries are all NaN.
    normalize : bool, {\'all\', \'index\', \'columns\'}, or {0,1}, default False
        Normalize by dividing all values by the sum of values.

        - If passed \'all\' or `True`, will normalize over all values.
        - If passed \'index\' will normalize over each row.
        - If passed \'columns\' will normalize over each column.
        - If margins is `True`, will also normalize margin values.

    Returns
    -------
    DataFrame
        Cross tabulation of the data.

    See Also
    --------
    DataFrame.pivot : Reshape data based on column values.
    pivot_table : Create a pivot table as a DataFrame.

    Notes
    -----
    Any Series passed will have their name attributes used unless row or column
    names for the cross-tabulation are specified.

    Any input passed containing Categorical data will have **all** of its
    categories included in the cross-tabulation, even if the actual data does
    not contain any instances of a particular category.

    In the event that there aren\'t overlapping indexes an empty DataFrame will
    be returned.

    Reference :ref:`the user guide <reshaping.crosstabulations>` for more examples.

    Examples
    --------
    >>> a = np.array(["foo", "foo", "foo", "foo", "bar", "bar",
    ...               "bar", "bar", "foo", "foo", "foo"], dtype=object)
    >>> b = np.array(["one", "one", "one", "two", "one", "one",
    ...               "one", "two", "two", "two", "one"], dtype=object)
    >>> c = np.array(["dull", "dull", "shiny", "dull", "dull", "shiny",
    ...               "shiny", "dull", "shiny", "shiny", "shiny"],
    ...              dtype=object)
    >>> pd.crosstab(a, [b, c], rownames=[\'a\'], colnames=[\'b\', \'c\'])
    b   one        two
    c   dull shiny dull shiny
    a
    bar    1     2    1     0
    foo    2     2    1     2

    Here \'c\' and \'f\' are not represented in the data and will not be
    shown in the output because dropna is True by default. Set
    dropna=False to preserve categories with no data.

    >>> foo = pd.Categorical([\'a\', \'b\'], categories=[\'a\', \'b\', \'c\'])
    >>> bar = pd.Categorical([\'d\', \'e\'], categories=[\'d\', \'e\', \'f\'])
    >>> pd.crosstab(foo, bar)
    col_0  d  e
    row_0
    a      1  0
    b      0  1
    >>> pd.crosstab(foo, bar, dropna=False)
    col_0  d  e  f
    row_0
    a      1  0  0
    b      0  1  0
    c      0  0  0
    '''
