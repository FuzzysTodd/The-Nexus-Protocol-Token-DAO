import numpy as np
from _typeshed import Incomplete
from pandas import Categorical as Categorical
from pandas._libs import Interval as Interval, lib as lib
from pandas._typing import ArrayLike as ArrayLike, Axis as Axis, AxisInt as AxisInt, CorrelationMethod as CorrelationMethod, FillnaOptions as FillnaOptions, IndexLabel as IndexLabel, Manager as Manager, Manager2D as Manager2D, SingleManager as SingleManager, TakeIndexer as TakeIndexer
from pandas.core import algorithms as algorithms
from pandas.core.apply import GroupByApply as GroupByApply, maybe_mangle_lambdas as maybe_mangle_lambdas, reconstruct_func as reconstruct_func, validate_func_kwargs as validate_func_kwargs
from pandas.core.dtypes.common import ensure_int64 as ensure_int64, is_bool as is_bool, is_categorical_dtype as is_categorical_dtype, is_dict_like as is_dict_like, is_integer_dtype as is_integer_dtype, is_interval_dtype as is_interval_dtype, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby import base as base
from pandas.core.groupby.groupby import GroupBy as GroupBy, GroupByPlot as GroupByPlot
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, all_indexes_same as all_indexes_same, default_index as default_index
from pandas.core.series import Series as Series
from pandas.core.util.numba_ import maybe_use_numba as maybe_use_numba
from pandas.errors import SpecificationError as SpecificationError
from pandas.plotting import boxplot_frame_groupby as boxplot_frame_groupby
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, doc as doc
from typing import Any, Callable, Hashable, Literal, Mapping, NamedTuple, Sequence, TypeVar

AggScalar = str | Callable[..., Any]
ScalarResult = TypeVar('ScalarResult')

class NamedAgg(NamedTuple):
    '''
    Helper for column specific aggregation with control over output column names.

    Subclass of typing.NamedTuple.

    Parameters
    ----------
    column : Hashable
        Column label in the DataFrame to apply aggfunc.
    aggfunc : function or str
        Function to apply to the provided column. If string, the name of a built-in
        pandas function.

    Examples
    --------
    >>> df = pd.DataFrame({"key": [1, 1, 2], "a": [-1, 0, 1], 1: [10, 11, 12]})
    >>> agg_a = pd.NamedAgg(column="a", aggfunc="min")
    >>> agg_1 = pd.NamedAgg(column=1, aggfunc=np.mean)
    >>> df.groupby("key").agg(result_a=agg_a, result_1=agg_1)
         result_a  result_1
    key
    1          -1      10.5
    2           1      12.0
    '''
    column: Hashable
    aggfunc: AggScalar

class SeriesGroupBy(GroupBy[Series]):
    def apply(self, func, *args, **kwargs) -> Series: ...
    def aggregate(self, func: Incomplete | None = None, *args, engine: Incomplete | None = None, engine_kwargs: Incomplete | None = None, **kwargs): ...
    agg = aggregate
    def transform(self, func, *args, engine: Incomplete | None = None, engine_kwargs: Incomplete | None = None, **kwargs): ...
    def filter(self, func, dropna: bool = True, *args, **kwargs):
        """
        Filter elements from groups that don't satisfy a criterion.

        Elements from groups are filtered if they do not satisfy the
        boolean criterion specified by func.

        Parameters
        ----------
        func : function
            Criterion to apply to each group. Should return True or False.
        dropna : bool
            Drop groups that do not pass the filter. True by default; if False,
            groups that evaluate False are filled with NaNs.

        Returns
        -------
        Series

        Notes
        -----
        Functions that mutate the passed object can produce unexpected
        behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
        for more details.

        Examples
        --------
        >>> df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
        ...                           'foo', 'bar'],
        ...                    'B' : [1, 2, 3, 4, 5, 6],
        ...                    'C' : [2.0, 5., 8., 1., 2., 9.]})
        >>> grouped = df.groupby('A')
        >>> df.groupby('A').B.filter(lambda x: x.mean() > 3.)
        1    2
        3    4
        5    6
        Name: B, dtype: int64
        """
    def nunique(self, dropna: bool = True) -> Series | DataFrame:
        """
        Return number of unique elements in the group.

        Returns
        -------
        Series
            Number of unique values within each group.
        """
    def describe(self, **kwargs): ...
    def value_counts(self, normalize: bool = False, sort: bool = True, ascending: bool = False, bins: Incomplete | None = None, dropna: bool = True) -> Series | DataFrame: ...
    def fillna(self, value: object | ArrayLike | None = None, method: FillnaOptions | None = None, axis: Axis | None = None, inplace: bool = False, limit: int | None = None, downcast: dict | None = None) -> Series | None:
        '''
        Fill NA/NaN values using the specified method within groups.

        Parameters
        ----------
        value : scalar, dict, Series, or DataFrame
            Value to use to fill holes (e.g. 0), alternately a
            dict/Series/DataFrame of values specifying which value to use for
            each index (for a Series) or column (for a DataFrame).  Values not
            in the dict/Series/DataFrame will not be filled. This value cannot
            be a list. Users wanting to use the ``value`` argument and not ``method``
            should prefer :meth:`.Series.fillna` as this
            will produce the same result and be more performant.
        method : {{\'bfill\', \'ffill\', None}}, default None
            Method to use for filling holes. ``\'ffill\'`` will propagate
            the last valid observation forward within a group.
            ``\'bfill\'`` will use next valid observation to fill the gap.
        axis : {0 or \'index\', 1 or \'columns\'}
            Unused, only for compatibility with :meth:`DataFrameGroupBy.fillna`.
        inplace : bool, default False
            Broken. Do not set to True.
        limit : int, default None
            If method is specified, this is the maximum number of consecutive
            NaN values to forward/backward fill within a group. In other words,
            if there is a gap with more than this number of consecutive NaNs,
            it will only be partially filled. If method is not specified, this is the
            maximum number of entries along the entire axis where NaNs will be
            filled. Must be greater than 0 if not None.
        downcast : dict, default is None
            A dict of item->dtype of what to downcast if possible,
            or the string \'infer\' which will try to downcast to an appropriate
            equal type (e.g. float64 to int64 if possible).

        Returns
        -------
        Series
            Object with missing values filled within groups.

        See Also
        --------
        ffill : Forward fill values within a group.
        bfill : Backward fill values within a group.

        Examples
        --------
        >>> ser = pd.Series([np.nan, np.nan, 2, 3, np.nan, np.nan])
        >>> ser
        0    NaN
        1    NaN
        2    2.0
        3    3.0
        4    NaN
        5    NaN
        dtype: float64

        Propagate non-null values forward or backward within each group.

        >>> ser.groupby([0, 0, 0, 1, 1, 1]).fillna(method="ffill")
        0    NaN
        1    NaN
        2    2.0
        3    3.0
        4    3.0
        5    3.0
        dtype: float64

        >>> ser.groupby([0, 0, 0, 1, 1, 1]).fillna(method="bfill")
        0    2.0
        1    2.0
        2    2.0
        3    3.0
        4    NaN
        5    NaN
        dtype: float64

        Only replace the first NaN element within a group.

        >>> ser.groupby([0, 0, 0, 1, 1, 1]).fillna(method="ffill", limit=1)
        0    NaN
        1    NaN
        2    2.0
        3    3.0
        4    3.0
        5    NaN
        dtype: float64
        '''
    def take(self, indices: TakeIndexer, axis: Axis = 0, **kwargs) -> Series:
        '''
        Return the elements in the given *positional* indices in each group.

        This means that we are not indexing according to actual values in
        the index attribute of the object. We are indexing according to the
        actual position of the element in the object.

        If a requested index does not exist for some group, this method will raise.
        To get similar behavior that ignores indices that don\'t exist, see
        :meth:`.SeriesGroupBy.nth`.

        Parameters
        ----------
        indices : array-like
            An array of ints indicating which positions to take in each group.
        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            The axis on which to select elements. ``0`` means that we are
            selecting rows, ``1`` means that we are selecting columns.
            For `SeriesGroupBy` this parameter is unused and defaults to 0.
        **kwargs
            For compatibility with :meth:`numpy.take`. Has no effect on the
            output.

        Returns
        -------
        Series
            A Series containing the elements taken from each group.

        See Also
        --------
        Series.take : Take elements from a Series along an axis.
        Series.loc : Select a subset of a DataFrame by labels.
        Series.iloc : Select a subset of a DataFrame by positions.
        numpy.take : Take elements from an array along an axis.
        SeriesGroupBy.nth : Similar to take, won\'t raise if indices don\'t exist.

        Examples
        --------
        >>> df = pd.DataFrame([(\'falcon\', \'bird\', 389.0),
        ...                    (\'parrot\', \'bird\', 24.0),
        ...                    (\'lion\', \'mammal\', 80.5),
        ...                    (\'monkey\', \'mammal\', np.nan),
        ...                    (\'rabbit\', \'mammal\', 15.0)],
        ...                   columns=[\'name\', \'class\', \'max_speed\'],
        ...                   index=[4, 3, 2, 1, 0])
        >>> df
             name   class  max_speed
        4  falcon    bird      389.0
        3  parrot    bird       24.0
        2    lion  mammal       80.5
        1  monkey  mammal        NaN
        0  rabbit  mammal       15.0
        >>> gb = df["name"].groupby([1, 1, 2, 2, 2])

        Take elements at positions 0 and 1 along the axis 0 in each group (default).

        >>> gb.take([0, 1])
        1  4    falcon
           3    parrot
        2  2      lion
           1    monkey
        Name: name, dtype: object

        We may take elements using negative integers for positive indices,
        starting from the end of the object, just like with Python lists.

        >>> gb.take([-1, -2])
        1  3    parrot
           4    falcon
        2  0    rabbit
           1    monkey
        Name: name, dtype: object
        '''
    def skew(self, axis: Axis | lib.NoDefault = ..., skipna: bool = True, numeric_only: bool = False, **kwargs) -> Series:
        '''
        Return unbiased skew within groups.

        Normalized by N-1.

        Parameters
        ----------
        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            Axis for the function to be applied on.
            This parameter is only for compatibility with DataFrame and is unused.

        skipna : bool, default True
            Exclude NA/null values when computing the result.

        numeric_only : bool, default False
            Include only float, int, boolean columns. Not implemented for Series.

        **kwargs
            Additional keyword arguments to be passed to the function.

        Returns
        -------
        Series

        See Also
        --------
        Series.skew : Return unbiased skew over requested axis.

        Examples
        --------
        >>> ser = pd.Series([390., 350., 357., np.nan, 22., 20., 30.],
        ...                 index=[\'Falcon\', \'Falcon\', \'Falcon\', \'Falcon\',
        ...                        \'Parrot\', \'Parrot\', \'Parrot\'],
        ...                 name="Max Speed")
        >>> ser
        Falcon    390.0
        Falcon    350.0
        Falcon    357.0
        Falcon      NaN
        Parrot     22.0
        Parrot     20.0
        Parrot     30.0
        Name: Max Speed, dtype: float64
        >>> ser.groupby(level=0).skew()
        Falcon    1.525174
        Parrot    1.457863
        Name: Max Speed, dtype: float64
        >>> ser.groupby(level=0).skew(skipna=False)
        Falcon         NaN
        Parrot    1.457863
        Name: Max Speed, dtype: float64
        '''
    @property
    def plot(self): ...
    def nlargest(self, n: int = 5, keep: Literal['first', 'last', 'all'] = 'first') -> Series: ...
    def nsmallest(self, n: int = 5, keep: Literal['first', 'last', 'all'] = 'first') -> Series: ...
    def idxmin(self, axis: Axis = 0, skipna: bool = True) -> Series: ...
    def idxmax(self, axis: Axis = 0, skipna: bool = True) -> Series: ...
    def corr(self, other: Series, method: CorrelationMethod = 'pearson', min_periods: int | None = None) -> Series: ...
    def cov(self, other: Series, min_periods: int | None = None, ddof: int | None = 1) -> Series: ...
    @property
    def is_monotonic_increasing(self) -> Series: ...
    @property
    def is_monotonic_decreasing(self) -> Series: ...
    def hist(self, by: Incomplete | None = None, ax: Incomplete | None = None, grid: bool = True, xlabelsize: int | None = None, xrot: float | None = None, ylabelsize: int | None = None, yrot: float | None = None, figsize: tuple[int, int] | None = None, bins: int | Sequence[int] = 10, backend: str | None = None, legend: bool = False, **kwargs): ...
    @property
    def dtype(self) -> Series: ...
    def unique(self) -> Series: ...

class DataFrameGroupBy(GroupBy[DataFrame]):
    def aggregate(self, func: Incomplete | None = None, *args, engine: Incomplete | None = None, engine_kwargs: Incomplete | None = None, **kwargs): ...
    agg = aggregate
    def transform(self, func, *args, engine: Incomplete | None = None, engine_kwargs: Incomplete | None = None, **kwargs): ...
    def filter(self, func, dropna: bool = True, *args, **kwargs):
        """
        Filter elements from groups that don't satisfy a criterion.

        Elements from groups are filtered if they do not satisfy the
        boolean criterion specified by func.

        Parameters
        ----------
        func : function
            Criterion to apply to each group. Should return True or False.
        dropna : bool
            Drop groups that do not pass the filter. True by default; if False,
            groups that evaluate False are filled with NaNs.

        Returns
        -------
        DataFrame

        Notes
        -----
        Each subframe is endowed the attribute 'name' in case you need to know
        which group you are working on.

        Functions that mutate the passed object can produce unexpected
        behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
        for more details.

        Examples
        --------
        >>> df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
        ...                           'foo', 'bar'],
        ...                    'B' : [1, 2, 3, 4, 5, 6],
        ...                    'C' : [2.0, 5., 8., 1., 2., 9.]})
        >>> grouped = df.groupby('A')
        >>> grouped.filter(lambda x: x['B'].mean() > 3.)
             A  B    C
        1  bar  2  5.0
        3  bar  4  1.0
        5  bar  6  9.0
        """
    def __getitem__(self, key) -> DataFrameGroupBy | SeriesGroupBy: ...
    def nunique(self, dropna: bool = True) -> DataFrame:
        """
        Return DataFrame with counts of unique elements in each position.

        Parameters
        ----------
        dropna : bool, default True
            Don't include NaN in the counts.

        Returns
        -------
        nunique: DataFrame

        Examples
        --------
        >>> df = pd.DataFrame({'id': ['spam', 'egg', 'egg', 'spam',
        ...                           'ham', 'ham'],
        ...                    'value1': [1, 5, 5, 2, 5, 5],
        ...                    'value2': list('abbaxy')})
        >>> df
             id  value1 value2
        0  spam       1      a
        1   egg       5      b
        2   egg       5      b
        3  spam       2      a
        4   ham       5      x
        5   ham       5      y

        >>> df.groupby('id').nunique()
              value1  value2
        id
        egg        1       1
        ham        1       2
        spam       2       1

        Check for rows with the same id but conflicting values:

        >>> df.groupby('id').filter(lambda g: (g.nunique() > 1).any())
             id  value1 value2
        0  spam       1      a
        3  spam       2      a
        4   ham       5      x
        5   ham       5      y
        """
    def idxmax(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = False) -> DataFrame:
        '''
        Return index of first occurrence of maximum over requested axis.

        NA/null values are excluded.

        Parameters
        ----------
        axis : {{0 or \'index\', 1 or \'columns\'}}, default None
            The axis to use. 0 or \'index\' for row-wise, 1 or \'columns\' for column-wise.
            If axis is not provided, grouper\'s axis is used.

            .. versionchanged:: 2.0.0

        skipna : bool, default True
            Exclude NA/null values. If an entire row/column is NA, the result
            will be NA.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

        Returns
        -------
        Series
            Indexes of maxima along the specified axis.

        Raises
        ------
        ValueError
            * If the row/column is empty

        See Also
        --------
        Series.idxmax : Return index of the maximum element.

        Notes
        -----
        This method is the DataFrame version of ``ndarray.argmax``.

        Examples
        --------
        Consider a dataset containing food consumption in Argentina.

        >>> df = pd.DataFrame({\'consumption\': [10.51, 103.11, 55.48],
        ...                    \'co2_emissions\': [37.2, 19.66, 1712]},
        ...                    index=[\'Pork\', \'Wheat Products\', \'Beef\'])

        >>> df
                        consumption  co2_emissions
        Pork                  10.51         37.20
        Wheat Products       103.11         19.66
        Beef                  55.48       1712.00

        By default, it returns the index for the maximum value in each column.

        >>> df.idxmax()
        consumption     Wheat Products
        co2_emissions             Beef
        dtype: object

        To return the index for the maximum value in each row, use ``axis="columns"``.

        >>> df.idxmax(axis="columns")
        Pork              co2_emissions
        Wheat Products     consumption
        Beef              co2_emissions
        dtype: object
        '''
    def idxmin(self, axis: Axis | None = None, skipna: bool = True, numeric_only: bool = False) -> DataFrame:
        '''
        Return index of first occurrence of minimum over requested axis.

        NA/null values are excluded.

        Parameters
        ----------
        axis : {{0 or \'index\', 1 or \'columns\'}}, default None
            The axis to use. 0 or \'index\' for row-wise, 1 or \'columns\' for column-wise.
            If axis is not provided, grouper\'s axis is used.

            .. versionchanged:: 2.0.0

        skipna : bool, default True
            Exclude NA/null values. If an entire row/column is NA, the result
            will be NA.
        numeric_only : bool, default False
            Include only `float`, `int` or `boolean` data.

            .. versionadded:: 1.5.0

        Returns
        -------
        Series
            Indexes of minima along the specified axis.

        Raises
        ------
        ValueError
            * If the row/column is empty

        See Also
        --------
        Series.idxmin : Return index of the minimum element.

        Notes
        -----
        This method is the DataFrame version of ``ndarray.argmin``.

        Examples
        --------
        Consider a dataset containing food consumption in Argentina.

        >>> df = pd.DataFrame({\'consumption\': [10.51, 103.11, 55.48],
        ...                    \'co2_emissions\': [37.2, 19.66, 1712]},
        ...                    index=[\'Pork\', \'Wheat Products\', \'Beef\'])

        >>> df
                        consumption  co2_emissions
        Pork                  10.51         37.20
        Wheat Products       103.11         19.66
        Beef                  55.48       1712.00

        By default, it returns the index for the minimum value in each column.

        >>> df.idxmin()
        consumption                Pork
        co2_emissions    Wheat Products
        dtype: object

        To return the index for the minimum value in each row, use ``axis="columns"``.

        >>> df.idxmin(axis="columns")
        Pork                consumption
        Wheat Products    co2_emissions
        Beef                consumption
        dtype: object
        '''
    boxplot = boxplot_frame_groupby
    def value_counts(self, subset: Sequence[Hashable] | None = None, normalize: bool = False, sort: bool = True, ascending: bool = False, dropna: bool = True) -> DataFrame | Series:
        """
        Return a Series or DataFrame containing counts of unique rows.

        .. versionadded:: 1.4.0

        Parameters
        ----------
        subset : list-like, optional
            Columns to use when counting unique combinations.
        normalize : bool, default False
            Return proportions rather than frequencies.
        sort : bool, default True
            Sort by frequencies.
        ascending : bool, default False
            Sort in ascending order.
        dropna : bool, default True
            Don’t include counts of rows that contain NA values.

        Returns
        -------
        Series or DataFrame
            Series if the groupby as_index is True, otherwise DataFrame.

        See Also
        --------
        Series.value_counts: Equivalent method on Series.
        DataFrame.value_counts: Equivalent method on DataFrame.
        SeriesGroupBy.value_counts: Equivalent method on SeriesGroupBy.

        Notes
        -----
        - If the groupby as_index is True then the returned Series will have a
          MultiIndex with one level per input column.
        - If the groupby as_index is False then the returned DataFrame will have an
          additional column with the value_counts. The column is labelled 'count' or
          'proportion', depending on the ``normalize`` parameter.

        By default, rows that contain any NA values are omitted from
        the result.

        By default, the result will be in descending order so that the
        first element of each group is the most frequently-occurring row.

        Examples
        --------
        >>> df = pd.DataFrame({
        ...    'gender': ['male', 'male', 'female', 'male', 'female', 'male'],
        ...    'education': ['low', 'medium', 'high', 'low', 'high', 'low'],
        ...    'country': ['US', 'FR', 'US', 'FR', 'FR', 'FR']
        ... })

        >>> df
                gender  education   country
        0       male    low         US
        1       male    medium      FR
        2       female  high        US
        3       male    low         FR
        4       female  high        FR
        5       male    low         FR

        >>> df.groupby('gender').value_counts()
        gender  education  country
        female  high       FR         1
                           US         1
        male    low        FR         2
                           US         1
                medium     FR         1
        Name: count, dtype: int64

        >>> df.groupby('gender').value_counts(ascending=True)
        gender  education  country
        female  high       FR         1
                           US         1
        male    low        US         1
                medium     FR         1
                low        FR         2
        Name: count, dtype: int64

        >>> df.groupby('gender').value_counts(normalize=True)
        gender  education  country
        female  high       FR         0.50
                           US         0.50
        male    low        FR         0.50
                           US         0.25
                medium     FR         0.25
        Name: proportion, dtype: float64

        >>> df.groupby('gender', as_index=False).value_counts()
           gender education country  count
        0  female      high      FR      1
        1  female      high      US      1
        2    male       low      FR      2
        3    male       low      US      1
        4    male    medium      FR      1

        >>> df.groupby('gender', as_index=False).value_counts(normalize=True)
           gender education country  proportion
        0  female      high      FR        0.50
        1  female      high      US        0.50
        2    male       low      FR        0.50
        3    male       low      US        0.25
        4    male    medium      FR        0.25
        """
    def fillna(self, value: Hashable | Mapping | Series | DataFrame = None, method: FillnaOptions | None = None, axis: Axis | None = None, inplace: bool = False, limit: Incomplete | None = None, downcast: Incomplete | None = None) -> DataFrame | None:
        '''
        Fill NA/NaN values using the specified method within groups.

        Parameters
        ----------
        value : scalar, dict, Series, or DataFrame
            Value to use to fill holes (e.g. 0), alternately a
            dict/Series/DataFrame of values specifying which value to use for
            each index (for a Series) or column (for a DataFrame).  Values not
            in the dict/Series/DataFrame will not be filled. This value cannot
            be a list. Users wanting to use the ``value`` argument and not ``method``
            should prefer :meth:`.DataFrame.fillna` as this
            will produce the same result and be more performant.
        method : {{\'bfill\', \'ffill\', None}}, default None
            Method to use for filling holes. ``\'ffill\'`` will propagate
            the last valid observation forward within a group.
            ``\'bfill\'`` will use next valid observation to fill the gap.
        axis : {0 or \'index\', 1 or \'columns\'}
            Axis along which to fill missing values. When the :class:`DataFrameGroupBy`
            ``axis`` argument is ``0``, using ``axis=1`` here will produce
            the same results as :meth:`.DataFrame.fillna`. When the
            :class:`DataFrameGroupBy` ``axis`` argument is ``1``, using ``axis=0``
            or ``axis=1`` here will produce the same results.
        inplace : bool, default False
            Broken. Do not set to True.
        limit : int, default None
            If method is specified, this is the maximum number of consecutive
            NaN values to forward/backward fill within a group. In other words,
            if there is a gap with more than this number of consecutive NaNs,
            it will only be partially filled. If method is not specified, this is the
            maximum number of entries along the entire axis where NaNs will be
            filled. Must be greater than 0 if not None.
        downcast : dict, default is None
            A dict of item->dtype of what to downcast if possible,
            or the string \'infer\' which will try to downcast to an appropriate
            equal type (e.g. float64 to int64 if possible).

        Returns
        -------
        DataFrame
            Object with missing values filled.

        See Also
        --------
        ffill : Forward fill values within a group.
        bfill : Backward fill values within a group.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     {
        ...         "key": [0, 0, 1, 1, 1],
        ...         "A": [np.nan, 2, np.nan, 3, np.nan],
        ...         "B": [2, 3, np.nan, np.nan, np.nan],
        ...         "C": [np.nan, np.nan, 2, np.nan, np.nan],
        ...     }
        ... )
        >>> df
           key    A    B   C
        0    0  NaN  2.0 NaN
        1    0  2.0  3.0 NaN
        2    1  NaN  NaN 2.0
        3    1  3.0  NaN NaN
        4    1  NaN  NaN NaN

        Propagate non-null values forward or backward within each group along columns.

        >>> df.groupby("key").fillna(method="ffill")
             A    B   C
        0  NaN  2.0 NaN
        1  2.0  3.0 NaN
        2  NaN  NaN 2.0
        3  3.0  NaN 2.0
        4  3.0  NaN 2.0

        >>> df.groupby("key").fillna(method="bfill")
             A    B   C
        0  2.0  2.0 NaN
        1  2.0  3.0 NaN
        2  3.0  NaN 2.0
        3  3.0  NaN NaN
        4  NaN  NaN NaN

        Propagate non-null values forward or backward within each group along rows.

        >>> df.groupby([0, 0, 1, 1], axis=1).fillna(method="ffill")
           key    A    B    C
        0  0.0  0.0  2.0  2.0
        1  0.0  2.0  3.0  3.0
        2  1.0  1.0  NaN  2.0
        3  1.0  3.0  NaN  NaN
        4  1.0  1.0  NaN  NaN

        >>> df.groupby([0, 0, 1, 1], axis=1).fillna(method="bfill")
           key    A    B    C
        0  0.0  NaN  2.0  NaN
        1  0.0  2.0  3.0  NaN
        2  1.0  NaN  2.0  2.0
        3  1.0  3.0  NaN  NaN
        4  1.0  NaN  NaN  NaN

        Only replace the first NaN element within a group along rows.

        >>> df.groupby("key").fillna(method="ffill", limit=1)
             A    B    C
        0  NaN  2.0  NaN
        1  2.0  3.0  NaN
        2  NaN  NaN  2.0
        3  3.0  NaN  2.0
        4  3.0  NaN  NaN
        '''
    def take(self, indices: TakeIndexer, axis: Axis | None = 0, **kwargs) -> DataFrame:
        """
        Return the elements in the given *positional* indices in each group.

        This means that we are not indexing according to actual values in
        the index attribute of the object. We are indexing according to the
        actual position of the element in the object.

        If a requested index does not exist for some group, this method will raise.
        To get similar behavior that ignores indices that don't exist, see
        :meth:`.DataFrameGroupBy.nth`.

        Parameters
        ----------
        indices : array-like
            An array of ints indicating which positions to take.
        axis : {0 or 'index', 1 or 'columns', None}, default 0
            The axis on which to select elements. ``0`` means that we are
            selecting rows, ``1`` means that we are selecting columns.
        **kwargs
            For compatibility with :meth:`numpy.take`. Has no effect on the
            output.

        Returns
        -------
        DataFrame
            An DataFrame containing the elements taken from each group.

        See Also
        --------
        DataFrame.take : Take elements from a Series along an axis.
        DataFrame.loc : Select a subset of a DataFrame by labels.
        DataFrame.iloc : Select a subset of a DataFrame by positions.
        numpy.take : Take elements from an array along an axis.

        Examples
        --------
        >>> df = pd.DataFrame([('falcon', 'bird', 389.0),
        ...                    ('parrot', 'bird', 24.0),
        ...                    ('lion', 'mammal', 80.5),
        ...                    ('monkey', 'mammal', np.nan),
        ...                    ('rabbit', 'mammal', 15.0)],
        ...                   columns=['name', 'class', 'max_speed'],
        ...                   index=[4, 3, 2, 1, 0])
        >>> df
             name   class  max_speed
        4  falcon    bird      389.0
        3  parrot    bird       24.0
        2    lion  mammal       80.5
        1  monkey  mammal        NaN
        0  rabbit  mammal       15.0
        >>> gb = df.groupby([1, 1, 2, 2, 2])

        Take elements at positions 0 and 1 along the axis 0 (default).

        Note how the indices selected in the result do not correspond to
        our input indices 0 and 1. That's because we are selecting the 0th
        and 1st rows, not rows whose indices equal 0 and 1.

        >>> gb.take([0, 1])
               name   class  max_speed
        1 4  falcon    bird      389.0
          3  parrot    bird       24.0
        2 2    lion  mammal       80.5
          1  monkey  mammal        NaN

        The order of the specified indices influences the order in the result.
        Here, the order is swapped from the previous example.

        >>> gb.take([1, 0])
               name   class  max_speed
        1 3  parrot    bird       24.0
          4  falcon    bird      389.0
        2 1  monkey  mammal        NaN
          2    lion  mammal       80.5

        Take elements at indices 1 and 2 along the axis 1 (column selection).

        We may take elements using negative integers for positive indices,
        starting from the end of the object, just like with Python lists.

        >>> gb.take([-1, -2])
               name   class  max_speed
        1 3  parrot    bird       24.0
          4  falcon    bird      389.0
        2 0  rabbit  mammal       15.0
          1  monkey  mammal        NaN
        """
    def skew(self, axis: Axis | None | lib.NoDefault = ..., skipna: bool = True, numeric_only: bool = False, **kwargs) -> DataFrame:
        '''
        Return unbiased skew within groups.

        Normalized by N-1.

        Parameters
        ----------
        axis : {0 or \'index\', 1 or \'columns\', None}, default 0
            Axis for the function to be applied on.

            Specifying ``axis=None`` will apply the aggregation across both axes.

            .. versionadded:: 2.0.0

        skipna : bool, default True
            Exclude NA/null values when computing the result.

        numeric_only : bool, default False
            Include only float, int, boolean columns.

        **kwargs
            Additional keyword arguments to be passed to the function.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.skew : Return unbiased skew over requested axis.

        Examples
        --------
        >>> arrays = [[\'falcon\', \'parrot\', \'cockatoo\', \'kiwi\',
        ...            \'lion\', \'monkey\', \'rabbit\'],
        ...           [\'bird\', \'bird\', \'bird\', \'bird\',
        ...            \'mammal\', \'mammal\', \'mammal\']]
        >>> index = pd.MultiIndex.from_arrays(arrays, names=(\'name\', \'class\'))
        >>> df = pd.DataFrame({\'max_speed\': [389.0, 24.0, 70.0, np.nan,
        ...                                  80.5, 21.5, 15.0]},
        ...                   index=index)
        >>> df
                        max_speed
        name     class
        falcon   bird        389.0
        parrot   bird         24.0
        cockatoo bird         70.0
        kiwi     bird          NaN
        lion     mammal       80.5
        monkey   mammal       21.5
        rabbit   mammal       15.0
        >>> gb = df.groupby(["class"])
        >>> gb.skew()
                max_speed
        class
        bird     1.628296
        mammal   1.669046
        >>> gb.skew(skipna=False)
                max_speed
        class
        bird          NaN
        mammal   1.669046
        '''
    @property
    def plot(self) -> GroupByPlot: ...
    def corr(self, method: str | Callable[[np.ndarray, np.ndarray], float] = 'pearson', min_periods: int = 1, numeric_only: bool = False) -> DataFrame: ...
    def cov(self, min_periods: int | None = None, ddof: int | None = 1, numeric_only: bool = False) -> DataFrame: ...
    def hist(self, column: IndexLabel = None, by: Incomplete | None = None, grid: bool = True, xlabelsize: int | None = None, xrot: float | None = None, ylabelsize: int | None = None, yrot: float | None = None, ax: Incomplete | None = None, sharex: bool = False, sharey: bool = False, figsize: tuple[int, int] | None = None, layout: tuple[int, int] | None = None, bins: int | Sequence[int] = 10, backend: str | None = None, legend: bool = False, **kwargs): ...
    @property
    def dtypes(self) -> Series: ...
    def corrwith(self, other: DataFrame | Series, axis: Axis = 0, drop: bool = False, method: CorrelationMethod = 'pearson', numeric_only: bool = False) -> DataFrame: ...
