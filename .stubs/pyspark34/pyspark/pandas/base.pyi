import pandas as pd
from abc import ABCMeta, abstractmethod
from pyspark.pandas._typing import Axis as Axis, Dtype as Dtype, IndexOpsLike as IndexOpsLike, Label as Label, SeriesOrIndex as SeriesOrIndex
from pyspark.pandas.config import get_option as get_option, option_context as option_context
from pyspark.pandas.data_type_ops.base import DataTypeOps as DataTypeOps
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.internal import InternalField as InternalField, InternalFrame as InternalFrame, NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_DEFAULT_INDEX_NAME as SPARK_DEFAULT_INDEX_NAME
from pyspark.pandas.series import Series as Series
from pyspark.pandas.spark.accessors import SparkIndexOpsMethods as SparkIndexOpsMethods
from pyspark.pandas.typedef import extension_dtypes as extension_dtypes
from pyspark.pandas.utils import ERROR_MESSAGE_CANNOT_COMBINE as ERROR_MESSAGE_CANNOT_COMBINE, combine_frames as combine_frames, same_anchor as same_anchor, scol_for as scol_for, validate_axis as validate_axis
from pyspark.sql import Column as Column, Window as Window
from pyspark.sql._typing import ColumnOrName as ColumnOrName
from pyspark.sql.types import BooleanType as BooleanType, LongType as LongType, NumericType as NumericType
from typing import Any, Callable, Sequence, Tuple

def should_alignment_for_column_op(self, other: SeriesOrIndex) -> bool: ...
def align_diff_index_ops(func: Callable[..., Column], this_index_ops: SeriesOrIndex, *args: Any) -> SeriesOrIndex:
    """
    Align the `IndexOpsMixin` objects and apply the function.

    Parameters
    ----------
    func : The function to apply
    this_index_ops : IndexOpsMixin
        A base `IndexOpsMixin` object
    args : list of other arguments including other `IndexOpsMixin` objects

    Returns
    -------
    `Index` if all `this_index_ops` and arguments are `Index`; otherwise `Series`
    """
def booleanize_null(scol: Column, f: Callable[..., Column]) -> Column:
    """
    Booleanize Null in Spark Column
    """
def column_op(f: Callable[..., Column]) -> Callable[..., SeriesOrIndex]:
    """
    A decorator that wraps APIs taking/returning Spark Column so that pandas-on-Spark Series can be
    supported too. If this decorator is used for the `f` function that takes Spark Column and
    returns Spark Column, decorated `f` takes pandas-on-Spark Series as well and returns
    pandas-on-Spark Series.

    :param f: a function that takes Spark Column and returns Spark Column.
    :param self: pandas-on-Spark Series
    :param args: arguments that the function `f` takes.
    """
def numpy_column_op(f: Callable[..., Column]) -> Callable[..., SeriesOrIndex]: ...

class IndexOpsMixin(metaclass=ABCMeta):
    """common ops mixin to support a unified interface / docs for Series / Index

    Assuming there are following attributes or properties and functions.
    """
    @property
    @abstractmethod
    def spark(self) -> SparkIndexOpsMethods[IndexOpsLike]: ...
    @abstractmethod
    def copy(self) -> IndexOpsLike: ...
    def __neg__(self) -> IndexOpsLike: ...
    def __add__(self, other: Any) -> SeriesOrIndex: ...
    def __sub__(self, other: Any) -> SeriesOrIndex: ...
    def __mul__(self, other: Any) -> SeriesOrIndex: ...
    def __truediv__(self, other: Any) -> SeriesOrIndex:
        """
        __truediv__ has different behaviour between pandas and PySpark for several cases.
        1. When dividing np.inf by zero, PySpark returns null whereas pandas returns np.inf
        2. When dividing a positive number by zero, PySpark returns null
        whereas pandas returns np.inf
        3. When divide -np.inf by zero, PySpark returns null whereas pandas returns -np.inf
        4. When divide negative number by zero, PySpark returns null whereas pandas returns -np.inf

        +-------------------------------------------+
        | dividend (divisor: 0) | PySpark |  pandas |
        |-----------------------|---------|---------|
        |         np.inf        |   null  |  np.inf |
        |        -np.inf        |   null  | -np.inf |
        |           10          |   null  |  np.inf |
        |          -10          |   null  | -np.inf |
        +-----------------------|---------|---------+
        """
    def __mod__(self, other: Any) -> SeriesOrIndex: ...
    def __radd__(self, other: Any) -> SeriesOrIndex: ...
    def __rsub__(self, other: Any) -> SeriesOrIndex: ...
    def __rmul__(self, other: Any) -> SeriesOrIndex: ...
    def __rtruediv__(self, other: Any) -> SeriesOrIndex: ...
    def __floordiv__(self, other: Any) -> SeriesOrIndex:
        """
        __floordiv__ has different behaviour between pandas and PySpark for several cases.
        1. When dividing np.inf by zero, PySpark returns null whereas pandas returns np.inf
        2. When dividing a positive number by zero, PySpark returns null
        whereas pandas returns np.inf
        3. When divide -np.inf by zero, PySpark returns null whereas pandas returns -np.inf
        4. When divide negative number by zero, PySpark returns null whereas pandas returns -np.inf

        +-------------------------------------------+
        | dividend (divisor: 0) | PySpark |  pandas |
        |-----------------------|---------|---------|
        |         np.inf        |   null  |  np.inf |
        |        -np.inf        |   null  | -np.inf |
        |           10          |   null  |  np.inf |
        |          -10          |   null  | -np.inf |
        +-----------------------|---------|---------+
        """
    def __rfloordiv__(self, other: Any) -> SeriesOrIndex: ...
    def __rmod__(self, other: Any) -> SeriesOrIndex: ...
    def __pow__(self, other: Any) -> SeriesOrIndex: ...
    def __rpow__(self, other: Any) -> SeriesOrIndex: ...
    def __abs__(self) -> IndexOpsLike: ...
    def __eq__(self, other: Any) -> SeriesOrIndex: ...
    def __ne__(self, other: Any) -> SeriesOrIndex: ...
    def __lt__(self, other: Any) -> SeriesOrIndex: ...
    def __le__(self, other: Any) -> SeriesOrIndex: ...
    def __ge__(self, other: Any) -> SeriesOrIndex: ...
    def __gt__(self, other: Any) -> SeriesOrIndex: ...
    def __invert__(self) -> IndexOpsLike: ...
    def __and__(self, other: Any) -> SeriesOrIndex: ...
    def __or__(self, other: Any) -> SeriesOrIndex: ...
    def __rand__(self, other: Any) -> SeriesOrIndex: ...
    def __ror__(self, other: Any) -> SeriesOrIndex: ...
    def __xor__(self, other: Any) -> SeriesOrIndex: ...
    def __rxor__(self, other: Any) -> SeriesOrIndex: ...
    def __len__(self) -> int: ...
    def __array_ufunc__(self, ufunc: Callable, method: str, *inputs: Any, **kwargs: Any) -> SeriesOrIndex: ...
    @property
    def dtype(self) -> Dtype:
        '''Return the dtype object of the underlying data.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3])
        >>> s.dtype
        dtype(\'int64\')

        >>> s = ps.Series(list(\'abc\'))
        >>> s.dtype
        dtype(\'O\')

        >>> s = ps.Series(pd.date_range(\'20130101\', periods=3))
        >>> s.dtype
        dtype(\'<M8[ns]\')

        >>> s.rename("a").to_frame().set_index("a").index.dtype
        dtype(\'<M8[ns]\')
        '''
    @property
    def empty(self) -> bool:
        """
        Returns true if the current object is empty. Otherwise, it returns false.

        >>> ps.range(10).id.empty
        False

        >>> ps.range(0).id.empty
        True

        >>> ps.DataFrame({}, index=list('abc')).index.empty
        False
        """
    @property
    def hasnans(self) -> bool:
        '''
        Return True if it has any missing values. Otherwise, it returns False.

        >>> ps.DataFrame({}, index=list(\'abc\')).index.hasnans
        False

        >>> ps.Series([\'a\', None]).hasnans
        True

        >>> ps.Series([1.0, 2.0, np.nan]).hasnans
        True

        >>> ps.Series([1, 2, 3]).hasnans
        False

        >>> (ps.Series([1.0, 2.0, np.nan]) + 1).hasnans
        True

        >>> ps.Series([1, 2, 3]).rename("a").to_frame().set_index("a").index.hasnans
        False
        '''
    @property
    def is_monotonic(self) -> bool:
        '''
        Return boolean if values in the object are monotonically increasing.

        .. note:: the current implementation of is_monotonic requires to shuffle
            and aggregate multiple times to check the order locally and globally,
            which is potentially expensive. In case of multi-index, all data is
            transferred to a single node which can easily cause out-of-memory errors.

        .. note:: Disable the Spark config `spark.sql.optimizer.nestedSchemaPruning.enabled`
            for multi-index if you\'re using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

        .. deprecated:: 3.4.0

        Returns
        -------
        is_monotonic : bool

        Examples
        --------
        >>> ser = ps.Series([\'1/1/2018\', \'3/1/2018\', \'4/1/2018\'])
        >>> ser.is_monotonic
        True

        >>> df = ps.DataFrame({\'dates\': [None, \'1/1/2018\', \'2/1/2018\', \'3/1/2018\']})
        >>> df.dates.is_monotonic
        False

        >>> df.index.is_monotonic
        True

        >>> ser = ps.Series([1])
        >>> ser.is_monotonic
        True

        >>> ser = ps.Series([])
        >>> ser.is_monotonic
        True

        >>> ser.rename("a").to_frame().set_index("a").index.is_monotonic
        True

        >>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
        >>> ser.is_monotonic
        False

        >>> ser.index.is_monotonic
        True

        Support for MultiIndex

        >>> midx = ps.MultiIndex.from_tuples(
        ... [(\'x\', \'a\'), (\'x\', \'b\'), (\'y\', \'c\'), (\'y\', \'d\'), (\'z\', \'e\')])
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'x\', \'a\'),
                    (\'x\', \'b\'),
                    (\'y\', \'c\'),
                    (\'y\', \'d\'),
                    (\'z\', \'e\')],
                   )
        >>> midx.is_monotonic
        True

        >>> midx = ps.MultiIndex.from_tuples(
        ... [(\'z\', \'a\'), (\'z\', \'b\'), (\'y\', \'c\'), (\'y\', \'d\'), (\'x\', \'e\')])
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'z\', \'a\'),
                    (\'z\', \'b\'),
                    (\'y\', \'c\'),
                    (\'y\', \'d\'),
                    (\'x\', \'e\')],
                   )
        >>> midx.is_monotonic
        False
        '''
    @property
    def is_monotonic_increasing(self) -> bool:
        '''
        Return boolean if values in the object are monotonically increasing.

        .. note:: the current implementation of is_monotonic_increasing requires to shuffle
            and aggregate multiple times to check the order locally and globally,
            which is potentially expensive. In case of multi-index, all data is
            transferred to a single node which can easily cause out-of-memory errors.

        .. note:: Disable the Spark config `spark.sql.optimizer.nestedSchemaPruning.enabled`
            for multi-index if you\'re using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

        Returns
        -------
        is_monotonic : bool

        Examples
        --------
        >>> ser = ps.Series([\'1/1/2018\', \'3/1/2018\', \'4/1/2018\'])
        >>> ser.is_monotonic_increasing
        True

        >>> df = ps.DataFrame({\'dates\': [None, \'1/1/2018\', \'2/1/2018\', \'3/1/2018\']})
        >>> df.dates.is_monotonic_increasing
        False

        >>> df.index.is_monotonic_increasing
        True

        >>> ser = ps.Series([1])
        >>> ser.is_monotonic_increasing
        True

        >>> ser = ps.Series([])
        >>> ser.is_monotonic_increasing
        True

        >>> ser.rename("a").to_frame().set_index("a").index.is_monotonic_increasing
        True

        >>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
        >>> ser.is_monotonic_increasing
        False

        >>> ser.index.is_monotonic_increasing
        True

        Support for MultiIndex

        >>> midx = ps.MultiIndex.from_tuples(
        ... [(\'x\', \'a\'), (\'x\', \'b\'), (\'y\', \'c\'), (\'y\', \'d\'), (\'z\', \'e\')])
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'x\', \'a\'),
                    (\'x\', \'b\'),
                    (\'y\', \'c\'),
                    (\'y\', \'d\'),
                    (\'z\', \'e\')],
                   )
        >>> midx.is_monotonic_increasing
        True

        >>> midx = ps.MultiIndex.from_tuples(
        ... [(\'z\', \'a\'), (\'z\', \'b\'), (\'y\', \'c\'), (\'y\', \'d\'), (\'x\', \'e\')])
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'z\', \'a\'),
                    (\'z\', \'b\'),
                    (\'y\', \'c\'),
                    (\'y\', \'d\'),
                    (\'x\', \'e\')],
                   )
        >>> midx.is_monotonic_increasing
        False
        '''
    @property
    def is_monotonic_decreasing(self) -> bool:
        '''
        Return boolean if values in the object are monotonically decreasing.

        .. note:: the current implementation of is_monotonic_decreasing requires to shuffle
            and aggregate multiple times to check the order locally and globally,
            which is potentially expensive. In case of multi-index, all data is transferred
            to a single node which can easily cause out-of-memory errors.

        .. note:: Disable the Spark config `spark.sql.optimizer.nestedSchemaPruning.enabled`
            for multi-index if you\'re using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

        Returns
        -------
        is_monotonic : bool

        Examples
        --------
        >>> ser = ps.Series([\'4/1/2018\', \'3/1/2018\', \'1/1/2018\'])
        >>> ser.is_monotonic_decreasing
        True

        >>> df = ps.DataFrame({\'dates\': [None, \'3/1/2018\', \'2/1/2018\', \'1/1/2018\']})
        >>> df.dates.is_monotonic_decreasing
        False

        >>> df.index.is_monotonic_decreasing
        False

        >>> ser = ps.Series([1])
        >>> ser.is_monotonic_decreasing
        True

        >>> ser = ps.Series([])
        >>> ser.is_monotonic_decreasing
        True

        >>> ser.rename("a").to_frame().set_index("a").index.is_monotonic_decreasing
        True

        >>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
        >>> ser.is_monotonic_decreasing
        True

        >>> ser.index.is_monotonic_decreasing
        False

        Support for MultiIndex

        >>> midx = ps.MultiIndex.from_tuples(
        ... [(\'x\', \'a\'), (\'x\', \'b\'), (\'y\', \'c\'), (\'y\', \'d\'), (\'z\', \'e\')])
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'x\', \'a\'),
                    (\'x\', \'b\'),
                    (\'y\', \'c\'),
                    (\'y\', \'d\'),
                    (\'z\', \'e\')],
                   )
        >>> midx.is_monotonic_decreasing
        False

        >>> midx = ps.MultiIndex.from_tuples(
        ... [(\'z\', \'e\'), (\'z\', \'d\'), (\'y\', \'c\'), (\'y\', \'b\'), (\'x\', \'a\')])
        >>> midx  # doctest: +SKIP
        MultiIndex([(\'z\', \'a\'),
                    (\'z\', \'b\'),
                    (\'y\', \'c\'),
                    (\'y\', \'d\'),
                    (\'x\', \'e\')],
                   )
        >>> midx.is_monotonic_decreasing
        True
        '''
    @property
    def ndim(self) -> int:
        """
        Return an int representing the number of array dimensions.

        Return 1 for Series / Index / MultiIndex.

        Examples
        --------

        For Series

        >>> s = ps.Series([None, 1, 2, 3, 4], index=[4, 5, 2, 1, 8])
        >>> s.ndim
        1

        For Index

        >>> s.index.ndim
        1

        For MultiIndex

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
        >>> s.index.ndim
        1
        """
    def astype(self, dtype: str | type | Dtype) -> IndexOpsLike:
        '''
        Cast a pandas-on-Spark object to a specified dtype ``dtype``.

        Parameters
        ----------
        dtype : data type
            Use a numpy.dtype or Python type to cast entire pandas object to
            the same type.

        Returns
        -------
        casted : same type as caller

        See Also
        --------
        to_datetime : Convert argument to datetime.

        Examples
        --------
        >>> ser = ps.Series([1, 2], dtype=\'int32\')
        >>> ser
        0    1
        1    2
        dtype: int32

        >>> ser.astype(\'int64\')
        0    1
        1    2
        dtype: int64

        >>> ser.rename("a").to_frame().set_index("a").index.astype(\'int64\')
        Int64Index([1, 2], dtype=\'int64\', name=\'a\')
        '''
    def isin(self, values: Sequence[Any]) -> IndexOpsLike:
        '''
        Check whether `values` are contained in Series or Index.

        Return a boolean Series or Index showing whether each element in the Series
        matches an element in the passed sequence of `values` exactly.

        Parameters
        ----------
        values : set or list-like
            The sequence of values to test.

        Returns
        -------
        isin : Series (bool dtype) or Index (bool dtype)

        Examples
        --------
        >>> s = ps.Series([\'lama\', \'cow\', \'lama\', \'beetle\', \'lama\',
        ...                \'hippo\'], name=\'animal\')
        >>> s.isin([\'cow\', \'lama\'])
        0     True
        1     True
        2     True
        3    False
        4     True
        5    False
        Name: animal, dtype: bool

        Passing a single string as ``s.isin(\'lama\')`` will raise an error. Use
        a list of one element instead:

        >>> s.isin([\'lama\'])
        0     True
        1    False
        2     True
        3    False
        4     True
        5    False
        Name: animal, dtype: bool

        >>> s.rename("a").to_frame().set_index("a").index.isin([\'lama\'])  # doctest: +SKIP
        Index([True, False, True, False, True, False], dtype=\'bool\', name=\'a\')
        '''
    def isnull(self) -> IndexOpsLike:
        '''
        Detect existing (non-missing) values.

        Return a boolean same-sized object indicating if the values are NA.
        NA values, such as None or numpy.NaN, get mapped to True values.
        Everything else gets mapped to False values. Characters such as empty strings \'\' or
        numpy.inf are not considered NA values
        (unless you set pandas.options.mode.use_inf_as_na = True).

        Returns
        -------
        Series or Index : Mask of bool values for each element in Series
            that indicates whether an element is not an NA value.

        Examples
        --------
        >>> ser = ps.Series([5, 6, np.NaN])
        >>> ser.isna()  # doctest: +NORMALIZE_WHITESPACE
        0    False
        1    False
        2     True
        dtype: bool

        >>> ser.rename("a").to_frame().set_index("a").index.isna()  # doctest: +SKIP
        Index([False, False, True], dtype=\'bool\', name=\'a\')
        '''
    isna = isnull
    def notnull(self) -> IndexOpsLike:
        '''
        Detect existing (non-missing) values.
        Return a boolean same-sized object indicating if the values are not NA.
        Non-missing values get mapped to True.
        Characters such as empty strings \'\' or numpy.inf are not considered NA values
        (unless you set pandas.options.mode.use_inf_as_na = True).
        NA values, such as None or numpy.NaN, get mapped to False values.

        Returns
        -------
        Series or Index : Mask of bool values for each element in Series
            that indicates whether an element is not an NA value.

        Examples
        --------
        Show which entries in a Series are not NA.

        >>> ser = ps.Series([5, 6, np.NaN])
        >>> ser
        0    5.0
        1    6.0
        2    NaN
        dtype: float64

        >>> ser.notna()
        0     True
        1     True
        2    False
        dtype: bool

        >>> ser.rename("a").to_frame().set_index("a").index.notna()  # doctest: +SKIP
        Index([True, True, False], dtype=\'bool\', name=\'a\')
        '''
    notna = notnull
    def all(self, axis: Axis = 0, skipna: bool = True) -> bool:
        '''
        Return whether all elements are True.

        Returns True unless there at least one element within a series that is
        False or equivalent (e.g. zero or empty)

        Parameters
        ----------
        axis : {0 or \'index\'}, default 0
            Indicate which axis or axes should be reduced.

            * 0 / \'index\' : reduce the index, return a Series whose index is the
              original column labels.

        skipna : boolean, default True
            Exclude NA values, such as None or numpy.NaN.
            If an entire row/column is NA values and `skipna` is True,
            then the result will be True, as for an empty row/column.
            If `skipna` is False, numpy.NaNs are treated as True because these are
            not equal to zero, Nones are treated as False.

        Examples
        --------
        >>> ps.Series([True, True]).all()
        True

        >>> ps.Series([True, False]).all()
        False

        >>> ps.Series([0, 1]).all()
        False

        >>> ps.Series([1, 2, 3]).all()
        True

        >>> ps.Series([True, True, None]).all()
        True

        >>> ps.Series([True, True, None]).all(skipna=False)
        False

        >>> ps.Series([True, False, None]).all()
        False

        >>> ps.Series([]).all()
        True

        >>> ps.Series([np.nan]).all()
        True

        >>> ps.Series([np.nan]).all(skipna=False)
        True

        >>> ps.Series([None]).all()
        True

        >>> ps.Series([None]).all(skipna=False)
        False

        >>> df = ps.Series([True, False, None]).rename("a").to_frame()
        >>> df.set_index("a").index.all()
        False
        '''
    def any(self, axis: Axis = 0) -> bool:
        '''
        Return whether any element is True.

        Returns False unless there is at least one element within a series that is
        True or equivalent (e.g. non-zero or non-empty).

        Parameters
        ----------
        axis : {0 or \'index\'}, default 0
            Indicate which axis or axes should be reduced.

            * 0 / \'index\' : reduce the index, return a Series whose index is the
              original column labels.

        Examples
        --------
        >>> ps.Series([False, False]).any()
        False

        >>> ps.Series([True, False]).any()
        True

        >>> ps.Series([0, 0]).any()
        False

        >>> ps.Series([0, 1, 2]).any()
        True

        >>> ps.Series([False, False, None]).any()
        False

        >>> ps.Series([True, False, None]).any()
        True

        >>> ps.Series([]).any()
        False

        >>> ps.Series([np.nan]).any()
        False

        >>> df = ps.Series([True, False, None]).rename("a").to_frame()
        >>> df.set_index("a").index.any()
        True
        '''
    def shift(self, periods: int = 1, fill_value: Any | None = None) -> IndexOpsLike:
        """
        Shift Series/Index by desired number of periods.

        .. note:: the current implementation of shift uses Spark's Window without
            specifying partition specification. This leads to moveing all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        periods : int
            Number of periods to shift. Can be positive or negative.
        fill_value : object, optional
            The scalar value to use for newly introduced missing values.
            The default depends on the dtype of self. For numeric data, np.nan is used.

        Returns
        -------
        Copy of input Series/Index, shifted.

        Examples
        --------
        >>> df = ps.DataFrame({'Col1': [10, 20, 15, 30, 45],
        ...                    'Col2': [13, 23, 18, 33, 48],
        ...                    'Col3': [17, 27, 22, 37, 52]},
        ...                   columns=['Col1', 'Col2', 'Col3'])

        >>> df.Col1.shift(periods=3)
        0     NaN
        1     NaN
        2     NaN
        3    10.0
        4    20.0
        Name: Col1, dtype: float64

        >>> df.Col2.shift(periods=3, fill_value=0)
        0     0
        1     0
        2     0
        3    13
        4    23
        Name: Col2, dtype: int64

        >>> df.index.shift(periods=3, fill_value=0)
        Int64Index([0, 0, 0, 0, 1], dtype='int64')
        """
    def value_counts(self, normalize: bool = False, sort: bool = True, ascending: bool = False, bins: None = None, dropna: bool = True) -> Series:
        """
        Return a Series containing counts of unique values.
        The resulting object will be in descending order so that the
        first element is the most frequently-occurring element.
        Excludes NA values by default.

        Parameters
        ----------
        normalize : boolean, default False
            If True then the object returned will contain the relative
            frequencies of the unique values.
        sort : boolean, default True
            Sort by values.
        ascending : boolean, default False
            Sort in ascending order.
        bins : Not Yet Supported
        dropna : boolean, default True
            Don't include counts of NaN.

        Returns
        -------
        counts : Series

        See Also
        --------
        Series.count: Number of non-NA elements in a Series.

        Examples
        --------
        For Series

        >>> df = ps.DataFrame({'x':[0, 0, 1, 1, 1, np.nan]})
        >>> df.x.value_counts()  # doctest: +NORMALIZE_WHITESPACE
        1.0    3
        0.0    2
        Name: x, dtype: int64

        With `normalize` set to `True`, returns the relative frequency by
        dividing all values by the sum of values.

        >>> df.x.value_counts(normalize=True)  # doctest: +NORMALIZE_WHITESPACE
        1.0    0.6
        0.0    0.4
        Name: x, dtype: float64

        **dropna**
        With `dropna` set to `False` we can also see NaN index values.

        >>> df.x.value_counts(dropna=False)  # doctest: +NORMALIZE_WHITESPACE
        1.0    3
        0.0    2
        NaN    1
        Name: x, dtype: int64

        For Index

        >>> idx = ps.Index([3, 1, 2, 3, 4, np.nan])
        >>> idx
        Float64Index([3.0, 1.0, 2.0, 3.0, 4.0, nan], dtype='float64')

        >>> idx.value_counts().sort_index()
        1.0    1
        2.0    1
        3.0    2
        4.0    1
        dtype: int64

        **sort**

        With `sort` set to `False`, the result wouldn't be sorted by number of count.

        >>> idx.value_counts(sort=True).sort_index()
        1.0    1
        2.0    1
        3.0    2
        4.0    1
        dtype: int64

        **normalize**

        With `normalize` set to `True`, returns the relative frequency by
        dividing all values by the sum of values.

        >>> idx.value_counts(normalize=True).sort_index()
        1.0    0.2
        2.0    0.2
        3.0    0.4
        4.0    0.2
        dtype: float64

        **dropna**

        With `dropna` set to `False` we can also see NaN index values.

        >>> idx.value_counts(dropna=False).sort_index()  # doctest: +SKIP
        1.0    1
        2.0    1
        3.0    2
        4.0    1
        NaN    1
        dtype: int64

        For MultiIndex.

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
        >>> s.index  # doctest: +SKIP
        MultiIndex([(  'lama', 'weight'),
                    (  'lama', 'weight'),
                    (  'lama', 'weight'),
                    (   'cow', 'weight'),
                    (   'cow', 'weight'),
                    (   'cow', 'length'),
                    ('falcon', 'weight'),
                    ('falcon', 'length'),
                    ('falcon', 'length')],
                   )

        >>> s.index.value_counts().sort_index()
        (cow, length)       1
        (cow, weight)       2
        (falcon, length)    2
        (falcon, weight)    1
        (lama, weight)      3
        dtype: int64

        >>> s.index.value_counts(normalize=True).sort_index()
        (cow, length)       0.111111
        (cow, weight)       0.222222
        (falcon, length)    0.222222
        (falcon, weight)    0.111111
        (lama, weight)      0.333333
        dtype: float64

        If Index has name, keep the name up.

        >>> idx = ps.Index([0, 0, 0, 1, 1, 2, 3], name='pandas-on-Spark')
        >>> idx.value_counts().sort_index()
        0    3
        1    2
        2    1
        3    1
        Name: pandas-on-Spark, dtype: int64
        """
    def nunique(self, dropna: bool = True, approx: bool = False, rsd: float = 0.05) -> int:
        """
        Return number of unique elements in the object.
        Excludes NA values by default.

        Parameters
        ----------
        dropna : bool, default True
            Don’t include NaN in the count.
        approx: bool, default False
            If False, will use the exact algorithm and return the exact number of unique.
            If True, it uses the HyperLogLog approximate algorithm, which is significantly faster
            for large amount of data.
            Note: This parameter is specific to pandas-on-Spark and is not found in pandas.
        rsd: float, default 0.05
            Maximum estimation error allowed in the HyperLogLog algorithm.
            Note: Just like ``approx`` this parameter is specific to pandas-on-Spark.

        Returns
        -------
        int

        See Also
        --------
        DataFrame.nunique: Method nunique for DataFrame.
        Series.count: Count non-NA/null observations in the Series.

        Examples
        --------
        >>> ps.Series([1, 2, 3, np.nan]).nunique()
        3

        >>> ps.Series([1, 2, 3, np.nan]).nunique(dropna=False)
        4

        On big data, we recommend using the approximate algorithm to speed up this function.
        The result will be very close to the exact unique count.

        >>> ps.Series([1, 2, 3, np.nan]).nunique(approx=True)
        3

        >>> idx = ps.Index([1, 1, 2, None])
        >>> idx
        Float64Index([1.0, 1.0, 2.0, nan], dtype='float64')

        >>> idx.nunique()
        2

        >>> idx.nunique(dropna=False)
        3
        """
    def take(self, indices: Sequence[int]) -> IndexOpsLike:
        '''
        Return the elements in the given *positional* indices along an axis.

        This means that we are not indexing according to actual values in
        the index attribute of the object. We are indexing according to the
        actual position of the element in the object.

        Parameters
        ----------
        indices : array-like
            An array of ints indicating which positions to take.

        Returns
        -------
        taken : same type as caller
            An array-like containing the elements taken from the object.

        See Also
        --------
        DataFrame.loc : Select a subset of a DataFrame by labels.
        DataFrame.iloc : Select a subset of a DataFrame by positions.
        numpy.take : Take elements from an array along an axis.

        Examples
        --------

        Series

        >>> psser = ps.Series([100, 200, 300, 400, 500])
        >>> psser
        0    100
        1    200
        2    300
        3    400
        4    500
        dtype: int64

        >>> psser.take([0, 2, 4]).sort_index()
        0    100
        2    300
        4    500
        dtype: int64

        Index

        >>> psidx = ps.Index([100, 200, 300, 400, 500])
        >>> psidx
        Int64Index([100, 200, 300, 400, 500], dtype=\'int64\')

        >>> psidx.take([0, 2, 4]).sort_values()
        Int64Index([100, 300, 500], dtype=\'int64\')

        MultiIndex

        >>> psmidx = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c")])
        >>> psmidx  # doctest: +SKIP
        MultiIndex([(\'x\', \'a\'),
                    (\'x\', \'b\'),
                    (\'x\', \'c\')],
                   )

        >>> psmidx.take([0, 2])  # doctest: +SKIP
        MultiIndex([(\'x\', \'a\'),
                    (\'x\', \'c\')],
                   )
        '''
    def factorize(self, sort: bool = True, na_sentinel: int | None = -1) -> Tuple[IndexOpsLike, pd.Index]:
        '''
        Encode the object as an enumerated type or categorical variable.

        This method is useful for obtaining a numeric representation of an
        array when all that matters is identifying distinct values.

        Parameters
        ----------
        sort : bool, default True
        na_sentinel : int or None, default -1
            Value to mark "not found". If None, will not drop the NaN
            from the uniques of the values.

            .. deprecated:: 3.4.0

        Returns
        -------
        codes : Series or Index
            A Series or Index that\'s an indexer into `uniques`.
            ``uniques.take(codes)`` will have the same values as `values`.
        uniques : pd.Index
            The unique valid values.

            .. note ::

               Even if there\'s a missing value in `values`, `uniques` will
               *not* contain an entry for it.

        Examples
        --------
        >>> psser = ps.Series([\'b\', None, \'a\', \'c\', \'b\'])
        >>> codes, uniques = psser.factorize()
        >>> codes
        0    1
        1   -1
        2    0
        3    2
        4    1
        dtype: int32
        >>> uniques
        Index([\'a\', \'b\', \'c\'], dtype=\'object\')

        >>> codes, uniques = psser.factorize(na_sentinel=None)
        >>> codes
        0    1
        1    3
        2    0
        3    2
        4    1
        dtype: int32
        >>> uniques
        Index([\'a\', \'b\', \'c\', None], dtype=\'object\')

        >>> codes, uniques = psser.factorize(na_sentinel=-2)
        >>> codes
        0    1
        1   -2
        2    0
        3    2
        4    1
        dtype: int32
        >>> uniques
        Index([\'a\', \'b\', \'c\'], dtype=\'object\')

        For Index:

        >>> psidx = ps.Index([\'b\', None, \'a\', \'c\', \'b\'])
        >>> codes, uniques = psidx.factorize()
        >>> codes
        Int64Index([1, -1, 0, 2, 1], dtype=\'int64\')
        >>> uniques
        Index([\'a\', \'b\', \'c\'], dtype=\'object\')
        '''
