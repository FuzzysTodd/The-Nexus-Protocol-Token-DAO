import datetime
import pandas as pd
from _typeshed import Incomplete
from collections.abc import Mapping
from pandas.tseries.frequencies import DateOffset
from pyspark import SparkContext as SparkContext, pandas as ps
from pyspark.pandas._typing import Axis as Axis, Dtype as Dtype, Label as Label, Name as Name, Scalar as Scalar, T as T
from pyspark.pandas.accessors import PandasOnSparkSeriesMethods as PandasOnSparkSeriesMethods
from pyspark.pandas.base import IndexOpsMixin as IndexOpsMixin
from pyspark.pandas.categorical import CategoricalAccessor as CategoricalAccessor
from pyspark.pandas.config import get_option as get_option
from pyspark.pandas.correlation import CORRELATION_CORR_OUTPUT_COLUMN as CORRELATION_CORR_OUTPUT_COLUMN, CORRELATION_COUNT_OUTPUT_COLUMN as CORRELATION_COUNT_OUTPUT_COLUMN, CORRELATION_VALUE_1_COLUMN as CORRELATION_VALUE_1_COLUMN, CORRELATION_VALUE_2_COLUMN as CORRELATION_VALUE_2_COLUMN, compute as compute
from pyspark.pandas.datetimes import DatetimeMethods as DatetimeMethods
from pyspark.pandas.exceptions import SparkPandasIndexingError as SparkPandasIndexingError
from pyspark.pandas.frame import DataFrame as DataFrame
from pyspark.pandas.generic import Frame as Frame
from pyspark.pandas.groupby import SeriesGroupBy as SeriesGroupBy
from pyspark.pandas.indexes import Index as Index
from pyspark.pandas.internal import DEFAULT_SERIES_NAME as DEFAULT_SERIES_NAME, InternalField as InternalField, InternalFrame as InternalFrame, NATURAL_ORDER_COLUMN_NAME as NATURAL_ORDER_COLUMN_NAME, SPARK_DEFAULT_INDEX_NAME as SPARK_DEFAULT_INDEX_NAME, SPARK_DEFAULT_SERIES_NAME as SPARK_DEFAULT_SERIES_NAME
from pyspark.pandas.missing.series import MissingPandasLikeSeries as MissingPandasLikeSeries
from pyspark.pandas.plot import PandasOnSparkPlotAccessor as PandasOnSparkPlotAccessor
from pyspark.pandas.resample import SeriesResampler as SeriesResampler
from pyspark.pandas.spark.accessors import SparkIndexOpsMethods as SparkIndexOpsMethods, SparkSeriesMethods as SparkSeriesMethods
from pyspark.pandas.strings import StringMethods as StringMethods
from pyspark.pandas.typedef import ScalarType as ScalarType, SeriesType as SeriesType, create_type_for_series_type as create_type_for_series_type, infer_return_type as infer_return_type, spark_type_to_pandas_dtype as spark_type_to_pandas_dtype
from pyspark.pandas.typedef.typehints import as_spark_type as as_spark_type
from pyspark.pandas.utils import SPARK_CONF_ARROW_ENABLED as SPARK_CONF_ARROW_ENABLED, combine_frames as combine_frames, is_name_like_tuple as is_name_like_tuple, is_name_like_value as is_name_like_value, log_advice as log_advice, name_like_string as name_like_string, same_anchor as same_anchor, scol_for as scol_for, sql_conf as sql_conf, validate_arguments_and_invoke_function as validate_arguments_and_invoke_function, validate_axis as validate_axis, validate_bool_kwarg as validate_bool_kwarg, verify_temp_column_name as verify_temp_column_name
from pyspark.sql import Column as Column, DataFrame as SparkDataFrame
from pyspark.sql._typing import ColumnOrName as ColumnOrName
from pyspark.sql.types import ArrayType as ArrayType, BooleanType as BooleanType, DecimalType as DecimalType, DoubleType as DoubleType, FloatType as FloatType, IntegerType as IntegerType, IntegralType as IntegralType, LongType as LongType, NumericType as NumericType, Row as Row, StructType as StructType, TimestampType as TimestampType
from pyspark.sql.window import Window as Window
from typing import Any, Callable, Dict, Generic, IO, Iterable, List, Sequence, Tuple, Type, overload

REPR_PATTERN: Incomplete
str_type = str

class Series(Frame, IndexOpsMixin, Generic[T]):
    """
    pandas-on-Spark Series that corresponds to pandas Series logically. This holds Spark Column
    internally.

    :ivar _internal: an internal immutable Frame to manage metadata.
    :type _internal: InternalFrame
    :ivar _psdf: Parent's pandas-on-Spark DataFrame
    :type _psdf: ps.DataFrame

    Parameters
    ----------
    data : array-like, dict, or scalar value, pandas Series
        Contains data stored in Series
        Note that if `data` is a pandas Series, other arguments should not be used.
    index : array-like or Index (1d)
        Values must be hashable and have the same length as `data`.
        Non-unique index values are allowed. Will default to
        RangeIndex (0, 1, 2, ..., n) if not provided. If both a dict and index
        sequence is used, the index will override the keys found in the
        dict.
    dtype : numpy.dtype or None
        If None, dtype will be inferred
    copy : boolean, default False
        Copy input data
    """
    def __init__(self, data: Incomplete | None = None, index: Incomplete | None = None, dtype: Incomplete | None = None, name: Incomplete | None = None, copy: bool = False, fastpath: bool = False) -> None: ...
    spark: SparkIndexOpsMethods
    @property
    def dtypes(self) -> Dtype:
        """Return the dtype object of the underlying data.

        >>> s = ps.Series(list('abc'))
        >>> s.dtype == s.dtypes
        True
        """
    @property
    def axes(self) -> List['Index']:
        """
        Return a list of the row axis labels.

        Examples
        --------

        >>> psser = ps.Series([1, 2, 3])
        >>> psser.axes
        [Int64Index([0, 1, 2], dtype='int64')]
        """
    def add(self, other: Any) -> Series: ...
    def radd(self, other: Any) -> Series: ...
    def div(self, other: Any) -> Series: ...
    divide = div
    def rdiv(self, other: Any) -> Series: ...
    def truediv(self, other: Any) -> Series: ...
    def rtruediv(self, other: Any) -> Series: ...
    def mul(self, other: Any) -> Series: ...
    multiply = mul
    def rmul(self, other: Any) -> Series: ...
    def sub(self, other: Any) -> Series: ...
    subtract = sub
    def rsub(self, other: Any) -> Series: ...
    def mod(self, other: Any) -> Series: ...
    def rmod(self, other: Any) -> Series: ...
    def pow(self, other: Any) -> Series: ...
    def rpow(self, other: Any) -> Series: ...
    def floordiv(self, other: Any) -> Series: ...
    def rfloordiv(self, other: Any) -> Series: ...
    pandas_on_spark: Incomplete
    koalas: Incomplete
    def eq(self, other: Any) -> Series:
        """
        Compare if the current value is equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.a == 1
        a     True
        b    False
        c    False
        d    False
        Name: a, dtype: bool

        >>> df.b.eq(1)
        a     True
        b    False
        c     True
        d    False
        Name: b, dtype: bool
        """
    equals = eq
    def gt(self, other: Any) -> Series:
        """
        Compare if the current value is greater than the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.a > 1
        a    False
        b     True
        c     True
        d     True
        Name: a, dtype: bool

        >>> df.b.gt(1)
        a    False
        b    False
        c    False
        d    False
        Name: b, dtype: bool
        """
    def ge(self, other: Any) -> Series:
        """
        Compare if the current value is greater than or equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.a >= 2
        a    False
        b     True
        c     True
        d     True
        Name: a, dtype: bool

        >>> df.b.ge(2)
        a    False
        b    False
        c    False
        d    False
        Name: b, dtype: bool
        """
    def lt(self, other: Any) -> Series:
        """
        Compare if the current value is less than the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.a < 1
        a    False
        b    False
        c    False
        d    False
        Name: a, dtype: bool

        >>> df.b.lt(2)
        a     True
        b    False
        c     True
        d    False
        Name: b, dtype: bool
        """
    def le(self, other: Any) -> Series:
        """
        Compare if the current value is less than or equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.a <= 2
        a     True
        b     True
        c    False
        d    False
        Name: a, dtype: bool

        >>> df.b.le(2)
        a     True
        b    False
        c     True
        d    False
        Name: b, dtype: bool
        """
    def ne(self, other: Any) -> Series:
        """
        Compare if the current value is not equal to the other.

        >>> df = ps.DataFrame({'a': [1, 2, 3, 4],
        ...                    'b': [1, np.nan, 1, np.nan]},
        ...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

        >>> df.a != 1
        a    False
        b     True
        c     True
        d     True
        Name: a, dtype: bool

        >>> df.b.ne(1)
        a    False
        b     True
        c    False
        d     True
        Name: b, dtype: bool
        """
    def divmod(self, other: Any) -> Tuple['Series', 'Series']:
        """
        Return Integer division and modulo of series and other, element-wise
        (binary operator `divmod`).

        Parameters
        ----------
        other : Series or scalar value

        Returns
        -------
        2-Tuple of Series
            The result of the operation.

        See Also
        --------
        Series.rdivmod
        """
    def rdivmod(self, other: Any) -> Tuple['Series', 'Series']:
        """
        Return Integer division and modulo of series and other, element-wise
        (binary operator `rdivmod`).

        Parameters
        ----------
        other : Series or scalar value

        Returns
        -------
        2-Tuple of Series
            The result of the operation.

        See Also
        --------
        Series.divmod
        """
    def between(self, left: Any, right: Any, inclusive: bool | str = 'both') -> Series:
        '''
        Return boolean Series equivalent to left <= series <= right.
        This function returns a boolean vector containing `True` wherever the
        corresponding Series element is between the boundary values `left` and
        `right`. NA values are treated as `False`.

        Parameters
        ----------
        left : scalar or list-like
            Left boundary.
        right : scalar or list-like
            Right boundary.
        inclusive : {"both", "neither", "left", "right"} or boolean. "both" by default.
            Include boundaries. Whether to set each bound as closed or open.
            Booleans are deprecated in favour of `both` or `neither`.

        Returns
        -------
        Series
            Series representing whether each element is between left and
            right (inclusive).

        See Also
        --------
        Series.gt : Greater than of series and other.
        Series.lt : Less than of series and other.

        Notes
        -----
        This function is equivalent to ``(left <= ser) & (ser <= right)``

        Examples
        --------
        >>> s = ps.Series([2, 0, 4, 8, np.nan])

        Boundary values are included by default:

        >>> s.between(0, 4)
        0     True
        1     True
        2     True
        3    False
        4    False
        dtype: bool

        With `inclusive` set to "neither" boundary values are excluded:

        >>> s.between(0, 4, inclusive="neither")
        0     True
        1    False
        2    False
        3    False
        4    False
        dtype: bool

        With `inclusive` set to "right" only right boundary value is included:

        >>> s.between(0, 4, inclusive="right")
        0     True
        1    False
        2     True
        3    False
        4    False
        dtype: bool

        With `inclusive` set to "left" only left boundary value is included:

        >>> s.between(0, 4, inclusive="left")
        0     True
        1     True
        2    False
        3    False
        4    False
        dtype: bool

        `left` and `right` can be any scalar value:

        >>> s = ps.Series([\'Alice\', \'Bob\', \'Carol\', \'Eve\'])
        >>> s.between(\'Anna\', \'Daniel\')
        0    False
        1     True
        2     True
        3    False
        dtype: bool
        '''
    def cov(self, other: Series, min_periods: int | None = None, ddof: int = 1) -> float:
        '''
        Compute covariance with Series, excluding missing values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        other : Series
            Series with which to compute the covariance.
        min_periods : int, optional
            Minimum number of observations needed to have a valid result.
        ddof : int, default 1
            Delta degrees of freedom. The divisor used in calculations
            is ``N - ddof``, where ``N`` represents the number of elements.

            .. versionadded:: 3.4.0

        Returns
        -------
        float
            Covariance between Series and other

        Examples
        --------
        >>> from pyspark.pandas.config import set_option, reset_option
        >>> s1 = ps.Series([0.90010907, 0.13484424, 0.62036035])
        >>> s2 = ps.Series([0.12528585, 0.26962463, 0.51111198])
        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.cov(s2)
        -0.016857...
        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.cov(s2, ddof=2)
        -0.033715...
        '''
    def map(self, arg: Dict | Callable[[Any], Any] | pd.Series, na_action: str | None = None) -> Series:
        """
        Map values of Series according to input correspondence.

        Used for substituting each value in a Series with another value,
        that may be derived from a function, a ``dict``.

        .. note:: make sure the size of the dictionary is not huge because it could
            downgrade the performance or throw OutOfMemoryError due to a huge
            expression within Spark. Consider the input as a function as an
            alternative instead in this case.

        Parameters
        ----------
        arg : function, dict or pd.Series
            Mapping correspondence.
        na_action :
            If `ignore`, propagate NA values, without passing them to the mapping correspondence.

        Returns
        -------
        Series
            Same index as caller.

        See Also
        --------
        Series.apply : For applying more complex functions on a Series.
        DataFrame.applymap : Apply a function element-wise on a whole DataFrame.

        Notes
        -----
        When ``arg`` is a dictionary, values in Series that are not in the
        dictionary (as keys) is converted to ``None``. However, if the
        dictionary is a ``dict`` subclass that defines ``__missing__`` (i.e.
        provides a method for default values), then this default is used
        rather than ``None``.

        Examples
        --------
        >>> s = ps.Series(['cat', 'dog', None, 'rabbit'])
        >>> s
        0       cat
        1       dog
        2      None
        3    rabbit
        dtype: object

        ``map`` accepts a ``dict``. Values that are not found
        in the ``dict`` are converted to ``None``, unless the dict has a default
        value (e.g. ``defaultdict``):

        >>> s.map({'cat': 'kitten', 'dog': 'puppy'})
        0    kitten
        1     puppy
        2      None
        3      None
        dtype: object

        It also accepts a pandas Series:

        >>> pser = pd.Series(['kitten', 'puppy'], index=['cat', 'dog'])
        >>> s.map(pser)
        0    kitten
        1     puppy
        2      None
        3      None
        dtype: object

        It also accepts a function:

        >>> def format(x) -> str:
        ...     return 'I am a {}'.format(x)

        >>> s.map(format)
        0       I am a cat
        1       I am a dog
        2      I am a None
        3    I am a rabbit
        dtype: object

        To avoid applying the function to missing values (and keep them as NaN)
        na_action='ignore' can be used:

        >>> s.map('I am a {}'.format, na_action='ignore')
        0       I am a cat
        1       I am a dog
        2             None
        3    I am a rabbit
        dtype: object
        """
    @property
    def shape(self) -> Tuple[int]:
        """Return a tuple of the shape of the underlying data."""
    @property
    def name(self) -> Name:
        """Return name of the Series."""
    @name.setter
    def name(self, name: Name) -> None: ...
    def rename(self, index: Name | Callable[[Any], Any] | None = None, **kwargs: Any) -> Series:
        '''
        Alter Series index labels or name.

        Parameters
        ----------
        index : scalar or function, optional
            Functions are transformations to apply to the index.
            Scalar will alter the Series.name attribute.

        inplace : bool, default False
            Whether to return a new Series. If True then value of copy is
            ignored.

        Returns
        -------
        Series
            Series with index labels or name altered.

        Examples
        --------

        >>> s = ps.Series([1, 2, 3])
        >>> s
        0    1
        1    2
        2    3
        dtype: int64

        >>> s.rename("my_name")  # scalar, changes Series.name
        0    1
        1    2
        2    3
        Name: my_name, dtype: int64

        >>> s.rename(lambda x: x ** 2)  # function, changes labels
        0    1
        1    2
        4    3
        dtype: int64
        '''
    def rename_axis(self, mapper: Any | None = None, index: Any | None = None, inplace: bool = False) -> Series | None:
        '''
        Set the name of the axis for the index or columns.

        Parameters
        ----------
        mapper, index :  scalar, list-like, dict-like or function, optional
            A scalar, list-like, dict-like or functions transformations to
            apply to the index values.
        inplace : bool, default False
            Modifies the object directly, instead of creating a new Series.

        Returns
        -------
        Series, or None if `inplace` is True.

        See Also
        --------
        Series.rename : Alter Series index labels or name.
        DataFrame.rename : Alter DataFrame index labels or name.
        Index.rename : Set new names on index.

        Examples
        --------
        >>> s = ps.Series(["dog", "cat", "monkey"], name="animal")
        >>> s  # doctest: +NORMALIZE_WHITESPACE
        0       dog
        1       cat
        2    monkey
        Name: animal, dtype: object
        >>> s.rename_axis("index").sort_index()  # doctest: +NORMALIZE_WHITESPACE
        index
        0       dog
        1       cat
        2    monkey
        Name: animal, dtype: object

        **MultiIndex**

        >>> index = pd.MultiIndex.from_product([[\'mammal\'],
        ...                                        [\'dog\', \'cat\', \'monkey\']],
        ...                                       names=[\'type\', \'name\'])
        >>> s = ps.Series([4, 4, 2], index=index, name=\'num_legs\')
        >>> s  # doctest: +NORMALIZE_WHITESPACE
        type    name
        mammal  dog       4
                cat       4
                monkey    2
        Name: num_legs, dtype: int64
        >>> s.rename_axis(index={\'type\': \'class\'}).sort_index()  # doctest: +NORMALIZE_WHITESPACE
        class   name
        mammal  cat       4
                dog       4
                monkey    2
        Name: num_legs, dtype: int64
        >>> s.rename_axis(index=str.upper).sort_index()  # doctest: +NORMALIZE_WHITESPACE
        TYPE    NAME
        mammal  cat       4
                dog       4
                monkey    2
        Name: num_legs, dtype: int64
        '''
    @property
    def index(self) -> ps.Index:
        """The index (axis labels) Column of the Series.

        See Also
        --------
        Index
        """
    @property
    def is_unique(self) -> bool:
        """
        Return boolean if values in the object are unique

        Returns
        -------
        is_unique : boolean

        >>> ps.Series([1, 2, 3]).is_unique
        True
        >>> ps.Series([1, 2, 2]).is_unique
        False
        >>> ps.Series([1, 2, 3, None]).is_unique
        True
        """
    def reset_index(self, level: int | Name | Sequence[int | Name] | None = None, drop: bool = False, name: Name | None = None, inplace: bool = False) -> Series | DataFrame | None:
        """
        Generate a new DataFrame or Series with the index reset.

        This is useful when the index needs to be treated as a column,
        or when the index is meaningless and needs to be reset
        to the default before another operation.

        Parameters
        ----------
        level : int, str, tuple, or list, default optional
            For a Series with a MultiIndex, only remove the specified levels from the index.
            Removes all levels by default.
        drop : bool, default False
            Just reset the index, without inserting it as a column in the new DataFrame.
        name : object, optional
            The name to use for the column containing the original Series values.
            Uses self.name by default. This argument is ignored when drop is True.
        inplace : bool, default False
            Modify the Series in place (do not create a new object).

        Returns
        -------
        Series or DataFrame
            When `drop` is False (the default), a DataFrame is returned.
            The newly created columns will come first in the DataFrame,
            followed by the original Series values.
            When `drop` is True, a `Series` is returned.
            In either case, if ``inplace=True``, no value is returned.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4], index=pd.Index(['a', 'b', 'c', 'd'], name='idx'))

        Generate a DataFrame with default index.

        >>> s.reset_index()
          idx  0
        0   a  1
        1   b  2
        2   c  3
        3   d  4

        To specify the name of the new column use `name`.

        >>> s.reset_index(name='values')
          idx  values
        0   a       1
        1   b       2
        2   c       3
        3   d       4

        To generate a new Series with the default set `drop` to True.

        >>> s.reset_index(drop=True)
        0    1
        1    2
        2    3
        3    4
        dtype: int64

        To update the Series in place, without generating a new one
        set `inplace` to True. Note that it also requires ``drop=True``.

        >>> s.reset_index(inplace=True, drop=True)
        >>> s
        0    1
        1    2
        2    3
        3    4
        dtype: int64
        """
    def to_frame(self, name: Name | None = None) -> DataFrame:
        '''
        Convert Series to DataFrame.

        Parameters
        ----------
        name : object, default None
            The passed name should substitute for the series name (if it has
            one).

        Returns
        -------
        DataFrame
            DataFrame representation of Series.

        Examples
        --------
        >>> s = ps.Series(["a", "b", "c"])
        >>> s.to_frame()
           0
        0  a
        1  b
        2  c

        >>> s = ps.Series(["a", "b", "c"], name="vals")
        >>> s.to_frame()
          vals
        0    a
        1    b
        2    c
        '''
    to_dataframe = to_frame
    def to_string(self, buf: IO[str] | None = None, na_rep: str = 'NaN', float_format: Callable[[float], str] | None = None, header: bool = True, index: bool = True, length: bool = False, dtype: bool = False, name: bool = False, max_rows: int | None = None) -> str | None:
        """
        Render a string representation of the Series.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory. If the input
                  is large, set max_rows parameter.

        Parameters
        ----------
        buf : StringIO-like, optional
            buffer to write to
        na_rep : string, optional
            string representation of NAN to use, default 'NaN'
        float_format : one-parameter function, optional
            formatter function to apply to columns' elements if they are floats
            default None
        header : boolean, default True
            Add the Series header (index name)
        index : bool, optional
            Add index (row) labels, default True
        length : boolean, default False
            Add the Series length
        dtype : boolean, default False
            Add the Series dtype
        name : boolean, default False
            Add the Series name if not None
        max_rows : int, optional
            Maximum number of rows to show before truncating. If None, show
            all.

        Returns
        -------
        formatted : string (if not buffer passed)

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)], columns=['dogs', 'cats'])
        >>> print(df['dogs'].to_string())
        0    0.2
        1    0.0
        2    0.6
        3    0.2

        >>> print(df['dogs'].to_string(max_rows=2))
        0    0.2
        1    0.0
        """
    def to_clipboard(self, excel: bool = True, sep: str | None = None, **kwargs: Any) -> None: ...
    def to_dict(self, into: Type = ...) -> Mapping:
        """
        Convert Series to {label -> value} dict or dict-like object.

        .. note:: This method should only be used if the resulting pandas DataFrame is expected
            to be small, as all the data is loaded into the driver's memory.

        Parameters
        ----------
        into : class, default dict
            The collections.abc.Mapping subclass to use as the return
            object. Can be the actual class or an empty
            instance of the mapping type you want.  If you want a
            collections.defaultdict, you must pass it initialized.

        Returns
        -------
        collections.abc.Mapping
            Key-value representation of Series.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4])
        >>> s_dict = s.to_dict()
        >>> sorted(s_dict.items())
        [(0, 1), (1, 2), (2, 3), (3, 4)]

        >>> from collections import OrderedDict, defaultdict
        >>> s.to_dict(OrderedDict)
        OrderedDict([(0, 1), (1, 2), (2, 3), (3, 4)])

        >>> dd = defaultdict(list)
        >>> s.to_dict(dd)  # doctest: +ELLIPSIS
        defaultdict(<class 'list'>, {...})
        """
    def to_latex(self, buf: IO[str] | None = None, columns: List[Name] | None = None, col_space: int | None = None, header: bool = True, index: bool = True, na_rep: str = 'NaN', formatters: List[Callable[[Any], str]] | Dict[Name, Callable[[Any], str]] | None = None, float_format: Callable[[float], str] | None = None, sparsify: bool | None = None, index_names: bool = True, bold_rows: bool = False, column_format: str | None = None, longtable: bool | None = None, escape: bool | None = None, encoding: str | None = None, decimal: str = '.', multicolumn: bool | None = None, multicolumn_format: str | None = None, multirow: bool | None = None) -> str | None: ...
    def to_pandas(self) -> pd.Series:
        """
        Return a pandas Series.

        .. note:: This method should only be used if the resulting pandas object is expected
                  to be small, as all the data is loaded into the driver's memory.

        Examples
        --------
        >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)], columns=['dogs', 'cats'])
        >>> df['dogs'].to_pandas()
        0    0.2
        1    0.0
        2    0.6
        3    0.2
        Name: dogs, dtype: float64
        """
    def to_list(self) -> List:
        """
        Return a list of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        .. note:: This method should only be used if the resulting list is expected
            to be small, as all the data is loaded into the driver's memory.

        """
    tolist = to_list
    def duplicated(self, keep: bool | str = 'first') -> Series:
        """
        Indicate duplicate Series values.

        Duplicated values are indicated as ``True`` values in the resulting
        Series. Either all duplicates, all except the first or all except the
        last occurrence of duplicates can be indicated.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        keep : {'first', 'last', False}, default 'first'
            Method to handle marking duplicates:
            - 'first' : Mark duplicates as ``True`` except for the first occurrence.
            - 'last' : Mark duplicates as ``True`` except for the last occurrence.
            - ``False`` : Mark all duplicates as ``True``.

        Returns
        -------
        Series
            Series indicating whether each value has occurred in the
            preceding values

        See Also
        --------
        Index.drop_duplicates : Remove duplicate values from Index.
        DataFrame.duplicated : Equivalent method on DataFrame.
        Series.drop_duplicates : Remove duplicate values from Series.

        Examples
        --------
        By default, for each set of duplicated values, the first occurrence is
        set on False and all others on True:

        >>> animals = ps.Series(['lama', 'cow', 'lama', 'beetle', 'lama'])
        >>> animals.duplicated().sort_index()
        0    False
        1    False
        2     True
        3    False
        4     True
        dtype: bool

        which is equivalent to

        >>> animals.duplicated(keep='first').sort_index()
        0    False
        1    False
        2     True
        3    False
        4     True
        dtype: bool

        By using 'last', the last occurrence of each set of duplicated values
        is set on False and all others on True:

        >>> animals.duplicated(keep='last').sort_index()
        0     True
        1    False
        2     True
        3    False
        4    False
        dtype: bool

        By setting keep on ``False``, all duplicates are True:

        >>> animals.duplicated(keep=False).sort_index()
        0     True
        1    False
        2     True
        3    False
        4     True
        dtype: bool
        """
    def drop_duplicates(self, keep: bool | str = 'first', inplace: bool = False) -> Series | None:
        """
        Return Series with duplicate values removed.

        Parameters
        ----------
        keep : {'first', 'last', ``False``}, default 'first'
            Method to handle dropping duplicates:
            - 'first' : Drop duplicates except for the first occurrence.
            - 'last' : Drop duplicates except for the last occurrence.
            - ``False`` : Drop all duplicates.
        inplace : bool, default ``False``
            If ``True``, performs operation inplace and returns None.

        Returns
        -------
        Series
            Series with duplicates dropped.

        Examples
        --------
        Generate a Series with duplicated entries.

        >>> s = ps.Series(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'],
        ...               name='animal')
        >>> s.sort_index()
        0      lama
        1       cow
        2      lama
        3    beetle
        4      lama
        5     hippo
        Name: animal, dtype: object

        With the 'keep' parameter, the selection behavior of duplicated values
        can be changed. The value 'first' keeps the first occurrence for each
        set of duplicated entries. The default value of keep is 'first'.

        >>> s.drop_duplicates().sort_index()
        0      lama
        1       cow
        3    beetle
        5     hippo
        Name: animal, dtype: object

        The value 'last' for parameter 'keep' keeps the last occurrence for
        each set of duplicated entries.

        >>> s.drop_duplicates(keep='last').sort_index()
        1       cow
        3    beetle
        4      lama
        5     hippo
        Name: animal, dtype: object

        The value ``False`` for parameter 'keep' discards all sets of
        duplicated entries. Setting the value of 'inplace' to ``True`` performs
        the operation inplace and returns ``None``.

        >>> s.drop_duplicates(keep=False, inplace=True)
        >>> s.sort_index()
        1       cow
        3    beetle
        5     hippo
        Name: animal, dtype: object
        """
    def reindex(self, index: Any | None = None, fill_value: Any | None = None) -> Series:
        '''
        Conform Series to new index with optional filling logic, placing
        NA/NaN in locations having no value in the previous index. A new object
        is produced.

        Parameters
        ----------
        index: array-like, optional
            New labels / index to conform to, should be specified using keywords.
            Preferably an Index object to avoid duplicating data
        fill_value : scalar, default np.NaN
            Value to use for missing values. Defaults to NaN, but can be any
            "compatible" value.

        Returns
        -------
        Series with changed index.

        See Also
        --------
        Series.reset_index : Remove row labels or move them to new columns.

        Examples
        --------

        Create a series with some fictional data.

        >>> index = [\'Firefox\', \'Chrome\', \'Safari\', \'IE10\', \'Konqueror\']
        >>> ser = ps.Series([200, 200, 404, 404, 301],
        ...                 index=index, name=\'http_status\')
        >>> ser
        Firefox      200
        Chrome       200
        Safari       404
        IE10         404
        Konqueror    301
        Name: http_status, dtype: int64

        Create a new index and reindex the Series. By default
        values in the new index that do not have corresponding
        records in the Series are assigned ``NaN``.

        >>> new_index= [\'Safari\', \'Iceweasel\', \'Comodo Dragon\', \'IE10\',
        ...             \'Chrome\']
        >>> ser.reindex(new_index).sort_index()
        Chrome           200.0
        Comodo Dragon      NaN
        IE10             404.0
        Iceweasel          NaN
        Safari           404.0
        Name: http_status, dtype: float64

        We can fill in the missing values by passing a value to
        the keyword ``fill_value``.

        >>> ser.reindex(new_index, fill_value=0).sort_index()
        Chrome           200
        Comodo Dragon      0
        IE10             404
        Iceweasel          0
        Safari           404
        Name: http_status, dtype: int64

        To further illustrate the filling functionality in
        ``reindex``, we will create a Series with a
        monotonically increasing index (for example, a sequence
        of dates).

        >>> date_index = pd.date_range(\'1/1/2010\', periods=6, freq=\'D\')
        >>> ser2 = ps.Series([100, 101, np.nan, 100, 89, 88],
        ...                  name=\'prices\', index=date_index)
        >>> ser2.sort_index()
        2010-01-01    100.0
        2010-01-02    101.0
        2010-01-03      NaN
        2010-01-04    100.0
        2010-01-05     89.0
        2010-01-06     88.0
        Name: prices, dtype: float64

        Suppose we decide to expand the series to cover a wider
        date range.

        >>> date_index2 = pd.date_range(\'12/29/2009\', periods=10, freq=\'D\')
        >>> ser2.reindex(date_index2).sort_index()
        2009-12-29      NaN
        2009-12-30      NaN
        2009-12-31      NaN
        2010-01-01    100.0
        2010-01-02    101.0
        2010-01-03      NaN
        2010-01-04    100.0
        2010-01-05     89.0
        2010-01-06     88.0
        2010-01-07      NaN
        Name: prices, dtype: float64
        '''
    def reindex_like(self, other: Series | DataFrame) -> Series:
        '''
        Return a Series with matching indices as other object.

        Conform the object to the same index on all axes. Places NA/NaN in locations
        having no value in the previous index.

        Parameters
        ----------
        other : Series or DataFrame
            Its row and column indices are used to define the new indices
            of this object.

        Returns
        -------
        Series
            Series with changed indices on each axis.

        See Also
        --------
        DataFrame.set_index : Set row labels.
        DataFrame.reset_index : Remove row labels or move them to new columns.
        DataFrame.reindex : Change to new indices or expand indices.

        Notes
        -----
        Same as calling
        ``.reindex(index=other.index, ...)``.

        Examples
        --------

        >>> s1 = ps.Series([24.3, 31.0, 22.0, 35.0],
        ...                index=pd.date_range(start=\'2014-02-12\',
        ...                                    end=\'2014-02-15\', freq=\'D\'),
        ...                name="temp_celsius")
        >>> s1
        2014-02-12    24.3
        2014-02-13    31.0
        2014-02-14    22.0
        2014-02-15    35.0
        Name: temp_celsius, dtype: float64

        >>> s2 = ps.Series(["low", "low", "medium"],
        ...                index=pd.DatetimeIndex([\'2014-02-12\', \'2014-02-13\',
        ...                                        \'2014-02-15\']),
        ...                name="winspeed")
        >>> s2
        2014-02-12       low
        2014-02-13       low
        2014-02-15    medium
        Name: winspeed, dtype: object

        >>> s2.reindex_like(s1).sort_index()
        2014-02-12       low
        2014-02-13       low
        2014-02-14      None
        2014-02-15    medium
        Name: winspeed, dtype: object
        '''
    def fillna(self, value: Any | None = None, method: str | None = None, axis: Axis | None = None, inplace: bool = False, limit: int | None = None) -> Series | None:
        """Fill NA/NaN values.

        .. note:: the current implementation of 'method' parameter in fillna uses Spark's Window
            without specifying partition specification. This leads to moveing all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        value : scalar, dict, Series
            Value to use to fill holes. alternately a dict/Series of values
            specifying which value to use for each column.
            DataFrame is not supported.
        method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
            Method to use for filling holes in reindexed Series pad / ffill: propagate last valid
            observation forward to next valid backfill / bfill:
            use NEXT valid observation to fill gap
        axis : {0 or `index`}
            1 and `columns` are not supported.
        inplace : boolean, default False
            Fill in place (do not create a new object)
        limit : int, default None
            If method is specified, this is the maximum number of consecutive NaN values to
            forward/backward fill. In other words, if there is a gap with more than this number of
            consecutive NaNs, it will only be partially filled. If method is not specified,
            this is the maximum number of entries along the entire axis where NaNs will be filled.
            Must be greater than 0 if not None

        Returns
        -------
        Series
            Series with NA entries filled.

        Examples
        --------
        >>> s = ps.Series([np.nan, 2, 3, 4, np.nan, 6], name='x')
        >>> s
        0    NaN
        1    2.0
        2    3.0
        3    4.0
        4    NaN
        5    6.0
        Name: x, dtype: float64

        Replace all NaN elements with 0s.

        >>> s.fillna(0)
        0    0.0
        1    2.0
        2    3.0
        3    4.0
        4    0.0
        5    6.0
        Name: x, dtype: float64

        We can also propagate non-null values forward or backward.

        >>> s.fillna(method='ffill')
        0    NaN
        1    2.0
        2    3.0
        3    4.0
        4    4.0
        5    6.0
        Name: x, dtype: float64

        >>> s = ps.Series([np.nan, 'a', 'b', 'c', np.nan], name='x')
        >>> s.fillna(method='ffill')
        0    None
        1       a
        2       b
        3       c
        4       c
        Name: x, dtype: object
        """
    def interpolate(self, method: str = 'linear', limit: int | None = None, limit_direction: str | None = None, limit_area: str | None = None) -> Series: ...
    def dropna(self, axis: Axis = 0, inplace: bool = False, **kwargs: Any) -> Series | None:
        """
        Return a new Series with missing values removed.

        Parameters
        ----------
        axis : {0 or 'index'}, default 0
            There is only one axis to drop values from.
        inplace : bool, default False
            If True, do operation inplace and return None.
        **kwargs
            Not in use.

        Returns
        -------
        Series
            Series with NA entries dropped from it.

        Examples
        --------
        >>> ser = ps.Series([1., 2., np.nan])
        >>> ser
        0    1.0
        1    2.0
        2    NaN
        dtype: float64

        Drop NA values from a Series.

        >>> ser.dropna()
        0    1.0
        1    2.0
        dtype: float64

        Keep the Series with valid entries in the same variable.

        >>> ser.dropna(inplace=True)
        >>> ser
        0    1.0
        1    2.0
        dtype: float64
        """
    def clip(self, lower: float | int = None, upper: float | int = None, inplace: bool = False) -> Series:
        '''
        Trim values at input threshold(s).

        Assigns values outside boundary-to-boundary values.

        Parameters
        ----------
        lower : float or int, default None
            Minimum threshold value. All values below this threshold will be set to it.
        upper : float or int, default None
            Maximum threshold value. All values above this threshold will be set to it.
        inplace : bool, default False
             if True, perform operation in-place

        Returns
        -------
        Series
            Series with the values outside the clip boundaries replaced

        Examples
        --------
        >>> psser = ps.Series([0, 2, 4])
        >>> psser
        0    0
        1    2
        2    4
        dtype: int64

        >>> psser.clip(1, 3)
        0    1
        1    2
        2    3
        dtype: int64

        Clip can be performed in-place.

        >>> psser.clip(2, 3, inplace=True)
        >>> psser
        0    2
        1    2
        2    3
        dtype: int64

        Notes
        -----
        One difference between this implementation and pandas is that running
        `pd.Series([\'a\', \'b\']).clip(0, 1)` will crash with "TypeError: \'<=\' not supported between
        instances of \'str\' and \'int\'" while `ps.Series([\'a\', \'b\']).clip(0, 1)` will output the
        original Series, simply ignoring the incompatible types.
        '''
    def drop(self, labels: Name | List[Name] | None = None, index: Name | List[Name] | None = None, columns: Name | List[Name] | None = None, level: int | None = None, inplace: bool = False) -> Series:
        """
        Return Series with specified index labels removed.

        Remove elements of a Series based on specifying the index labels.
        When using a multi-index, labels on different levels can be removed by specifying the level.

        Parameters
        ----------
        labels : single label or list-like
            Index labels to drop.
        index : single label or list-like
            Redundant for application on Series, but index can be used instead of labels.
        columns : single label or list-like
            No change is made to the Series; use ‘index’ or ‘labels’ instead.

            .. versionadded:: 3.4.0
        level : int or level name, optional
            For MultiIndex, level for which the labels will be removed.
        inplace: bool, default False
            If True, do operation inplace and return None

            .. versionadded:: 3.4.0

        Returns
        -------
        Series
            Series with specified index labels removed.

        See Also
        --------
        Series.dropna

        Examples
        --------
        >>> s = ps.Series(data=np.arange(3), index=['A', 'B', 'C'])
        >>> s
        A    0
        B    1
        C    2
        dtype: int64

        Drop single label A

        >>> s.drop('A')
        B    1
        C    2
        dtype: int64

        Drop labels B and C

        >>> s.drop(labels=['B', 'C'])
        A    0
        dtype: int64

        With 'index' rather than 'labels' returns exactly same result.

        >>> s.drop(index='A')
        B    1
        C    2
        dtype: int64

        >>> s.drop(index=['B', 'C'])
        A    0
        dtype: int64

        With 'columns', no change is made to the Series.

        >>> s.drop(columns=['A'])
        A    0
        B    1
        C    2
        dtype: int64

        With 'inplace=True', do operation inplace and return None.

        >>> s.drop(index=['B', 'C'], inplace=True)
        >>> s
        A    0
        dtype: int64

        Also support for MultiIndex

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...               index=midx)
        >>> s
        lama    speed      45.0
                weight    200.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.drop(labels='weight', level=1)
        lama    speed      45.0
                length      1.2
        cow     speed      30.0
                length      1.5
        falcon  speed     320.0
                length      0.3
        dtype: float64

        >>> s.drop(('lama', 'weight'))
        lama    speed      45.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.drop([('lama', 'speed'), ('falcon', 'weight')])
        lama    weight    200.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                length      0.3
        dtype: float64
        """
    def head(self, n: int = 5) -> Series:
        """
        Return the first n rows.

        This function returns the first n rows for the object based on position.
        It is useful for quickly testing if your object has the right type of data in it.

        Parameters
        ----------
        n : Integer, default =  5

        Returns
        -------
        The first n rows of the caller object.

        Examples
        --------
        >>> df = ps.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion']})
        >>> df.animal.head(2)  # doctest: +NORMALIZE_WHITESPACE
        0     alligator
        1     bee
        Name: animal, dtype: object
        """
    def last(self, offset: str | DateOffset) -> Series:
        """
        Select final periods of time series data based on a date offset.

        When having a Series with dates as index, this function can
        select the last few elements based on a date offset.

        Parameters
        ----------
        offset : str or DateOffset
            The offset length of the data that will be selected. For instance,
            '3D' will display all the rows having their index within the last 3 days.

        Returns
        -------
        Series
            A subset of the caller.

        Raises
        ------
        TypeError
            If the index is not a :class:`DatetimeIndex`

        Examples
        --------
        >>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
        >>> psser = ps.Series([1, 2, 3, 4], index=index)
        >>> psser
        2018-04-09    1
        2018-04-11    2
        2018-04-13    3
        2018-04-15    4
        dtype: int64

        Get the rows for the last 3 days:

        >>> psser.last('3D')
        2018-04-13    3
        2018-04-15    4
        dtype: int64

        Notice the data for 3 last calendar days were returned, not the last
        3 observed days in the dataset, and therefore data for 2018-04-11 was
        not returned.
        """
    def first(self, offset: str | DateOffset) -> Series:
        """
        Select first periods of time series data based on a date offset.

        When having a Series with dates as index, this function can
        select the first few elements based on a date offset.

        Parameters
        ----------
        offset : str or DateOffset
            The offset length of the data that will be selected. For instance,
            '3D' will display all the rows having their index within the first 3 days.

        Returns
        -------
        Series
            A subset of the caller.

        Raises
        ------
        TypeError
            If the index is not a :class:`DatetimeIndex`

        Examples
        --------
        >>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
        >>> psser = ps.Series([1, 2, 3, 4], index=index)
        >>> psser
        2018-04-09    1
        2018-04-11    2
        2018-04-13    3
        2018-04-15    4
        dtype: int64

        Get the rows for the first 3 days:

        >>> psser.first('3D')
        2018-04-09    1
        2018-04-11    2
        dtype: int64

        Notice the data for 3 first calendar days were returned, not the first
        3 observed days in the dataset, and therefore data for 2018-04-13 was
        not returned.
        """
    def unique(self) -> Series:
        """
        Return unique values of Series object.

        Uniques are returned in order of appearance. Hash table-based unique,
        therefore does NOT sort.

        .. note:: This method returns newly created Series whereas pandas returns
                  the unique values as a NumPy array.

        Returns
        -------
        Returns the unique values as a Series.

        See Also
        --------
        Index.unique
        groupby.SeriesGroupBy.unique

        Examples
        --------
        >>> psser = ps.Series([2, 1, 3, 3], name='A')
        >>> psser.unique().sort_values()
        1    1
        0    2
        2    3
        Name: A, dtype: int64

        >>> ps.Series([pd.Timestamp('2016-01-01') for _ in range(3)]).unique()
        0   2016-01-01
        dtype: datetime64[ns]

        >>> psser.name = ('x', 'a')
        >>> psser.unique().sort_values()
        1    1
        0    2
        2    3
        Name: (x, a), dtype: int64
        """
    def sort_values(self, ascending: bool = True, inplace: bool = False, na_position: str = 'last', ignore_index: bool = False) -> Series | None:
        """
        Sort by the values.

        Sort a Series in ascending or descending order by some criterion.

        Parameters
        ----------
        ascending : bool or list of bool, default True
             Sort ascending vs. descending. Specify list for multiple sort
             orders.  If this is a list of bools, must match the length of
             the by.
        inplace : bool, default False
             if True, perform operation in-place
        na_position : {'first', 'last'}, default 'last'
             `first` puts NaNs at the beginning, `last` puts NaNs at the end
        ignore_index : bool, default False
             If True, the resulting axis will be labeled 0, 1, …, n - 1.

             .. versionadded:: 3.4.0

        Returns
        -------
        sorted_obj : Series ordered by values.

        Examples
        --------
        >>> s = ps.Series([np.nan, 1, 3, 10, 5])
        >>> s
        0     NaN
        1     1.0
        2     3.0
        3    10.0
        4     5.0
        dtype: float64

        Sort values ascending order (default behaviour)

        >>> s.sort_values(ascending=True)
        1     1.0
        2     3.0
        4     5.0
        3    10.0
        0     NaN
        dtype: float64

        Sort values descending order

        >>> s.sort_values(ascending=False)
        3    10.0
        4     5.0
        2     3.0
        1     1.0
        0     NaN
        dtype: float64

        Sort values descending order and ignoring index

        >>> s.sort_values(ascending=False, ignore_index=True)
        0    10.0
        1     5.0
        2     3.0
        3     1.0
        4     NaN
        dtype: float64

        Sort values inplace

        >>> s.sort_values(ascending=False, inplace=True)
        >>> s
        3    10.0
        4     5.0
        2     3.0
        1     1.0
        0     NaN
        dtype: float64

        Sort values putting NAs first

        >>> s.sort_values(na_position='first')
        0     NaN
        1     1.0
        2     3.0
        4     5.0
        3    10.0
        dtype: float64

        Sort a series of strings

        >>> s = ps.Series(['z', 'b', 'd', 'a', 'c'])
        >>> s
        0    z
        1    b
        2    d
        3    a
        4    c
        dtype: object

        >>> s.sort_values()
        3    a
        1    b
        4    c
        2    d
        0    z
        dtype: object
        """
    def sort_index(self, axis: Axis = 0, level: int | List[int] | None = None, ascending: bool = True, inplace: bool = False, kind: str = None, na_position: str = 'last', ignore_index: bool = False) -> Series | None:
        """
        Sort object by labels (along an axis)

        Parameters
        ----------
        axis : index, columns to direct sorting. Currently, only axis = 0 is supported.
        level : int or level name or list of ints or list of level names
            if not None, sort on values in specified index level(s)
        ascending : boolean, default True
            Sort ascending vs. descending
        inplace : bool, default False
            if True, perform operation in-place
        kind : str, default None
            pandas-on-Spark does not allow specifying the sorting algorithm now,
            default None
        na_position : {‘first’, ‘last’}, default ‘last’
            first puts NaNs at the beginning, last puts NaNs at the end. Not implemented for
            MultiIndex.
        ignore_index : bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.

            .. versionadded:: 3.4.0

        Returns
        -------
        sorted_obj : Series

        Examples
        --------
        >>> s = ps.Series([2, 1, np.nan], index=['b', 'a', np.nan])

        >>> s.sort_index()  # doctest: +SKIP
        a       1.0
        b       2.0
        None    NaN
        dtype: float64

        >>> s.sort_index(ignore_index=True)
        0    1.0
        1    2.0
        2    NaN
        dtype: float64

        >>> s.sort_index(ascending=False)  # doctest: +SKIP
        b       2.0
        a       1.0
        None    NaN
        dtype: float64

        >>> s.sort_index(na_position='first')  # doctest: +SKIP
        None    NaN
        a       1.0
        b       2.0
        dtype: float64

        >>> s.sort_index(inplace=True)
        >>> s  # doctest: +SKIP
        a       1.0
        b       2.0
        None    NaN
        dtype: float64

        Multi-index series.

        >>> s = ps.Series(range(4), index=[['b', 'b', 'a', 'a'], [1, 0, 1, 0]], name='0')

        >>> s.sort_index()
        a  0    3
           1    2
        b  0    1
           1    0
        Name: 0, dtype: int64

        >>> s.sort_index(level=1)  # doctest: +SKIP
        a  0    3
        b  0    1
        a  1    2
        b  1    0
        Name: 0, dtype: int64

        >>> s.sort_index(level=[1, 0])
        a  0    3
        b  0    1
        a  1    2
        b  1    0
        Name: 0, dtype: int64
        """
    def swaplevel(self, i: int | Name = -2, j: int | Name = -1, copy: bool = True) -> Series:
        """
        Swap levels i and j in a MultiIndex.
        Default is to swap the two innermost levels of the index.

        Parameters
        ----------
        i, j : int, str
            Level of the indices to be swapped. Can pass level name as string.
        copy : bool, default True
            Whether to copy underlying data. Must be True.

        Returns
        -------
        Series
            Series with levels swapped in MultiIndex.

        Examples
        --------
        >>> midx = pd.MultiIndex.from_arrays([['a', 'b'], [1, 2]], names = ['word', 'number'])
        >>> midx  # doctest: +SKIP
        MultiIndex([('a', 1),
                    ('b', 2)],
                   names=['word', 'number'])
        >>> psser = ps.Series(['x', 'y'], index=midx)
        >>> psser
        word  number
        a     1         x
        b     2         y
        dtype: object
        >>> psser.swaplevel()
        number  word
        1       a       x
        2       b       y
        dtype: object
        >>> psser.swaplevel(0, 1)
        number  word
        1       a       x
        2       b       y
        dtype: object
        >>> psser.swaplevel('number', 'word')
        number  word
        1       a       x
        2       b       y
        dtype: object
        """
    def swapaxes(self, i: Axis, j: Axis, copy: bool = True) -> Series:
        '''
        Interchange axes and swap values axes appropriately.

        Parameters
        ----------
        i: {0 or \'index\', 1 or \'columns\'}. The axis to swap.
        j: {0 or \'index\', 1 or \'columns\'}. The axis to swap.
        copy : bool, default True.

        Returns
        -------
        Series

        Examples
        --------
        >>> psser = ps.Series([1, 2, 3], index=["x", "y", "z"])
        >>> psser
        x    1
        y    2
        z    3
        dtype: int64
        >>>
        >>> psser.swapaxes(0, 0)
        x    1
        y    2
        z    3
        dtype: int64
        '''
    def add_prefix(self, prefix: str) -> Series:
        """
        Prefix labels with string `prefix`.

        For Series, the row labels are prefixed.
        For DataFrame, the column labels are prefixed.

        Parameters
        ----------
        prefix : str
           The string to add before each label.

        Returns
        -------
        Series
           New Series with updated labels.

        See Also
        --------
        Series.add_suffix: Suffix column labels with string `suffix`.
        DataFrame.add_suffix: Suffix column labels with string `suffix`.
        DataFrame.add_prefix: Prefix column labels with string `prefix`.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4])
        >>> s
        0    1
        1    2
        2    3
        3    4
        dtype: int64

        >>> s.add_prefix('item_')
        item_0    1
        item_1    2
        item_2    3
        item_3    4
        dtype: int64
        """
    def add_suffix(self, suffix: str) -> Series:
        """
        Suffix labels with string suffix.

        For Series, the row labels are suffixed.
        For DataFrame, the column labels are suffixed.

        Parameters
        ----------
        suffix : str
           The string to add after each label.

        Returns
        -------
        Series
           New Series with updated labels.

        See Also
        --------
        Series.add_prefix: Prefix row labels with string `prefix`.
        DataFrame.add_prefix: Prefix column labels with string `prefix`.
        DataFrame.add_suffix: Suffix column labels with string `suffix`.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4])
        >>> s
        0    1
        1    2
        2    3
        3    4
        dtype: int64

        >>> s.add_suffix('_item')
        0_item    1
        1_item    2
        2_item    3
        3_item    4
        dtype: int64
        """
    def autocorr(self, lag: int = 1) -> float:
        """
        Compute the lag-N autocorrelation.

        This method computes the Pearson correlation between
        the Series and its shifted self.

        .. note:: the current implementation of rank uses Spark's Window without
            specifying partition specification. This leads to moveing all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        lag : int, default 1
            Number of lags to apply before performing autocorrelation.

        Returns
        -------
        float
            The Pearson correlation between self and self.shift(lag).

        See Also
        --------
        Series.corr : Compute the correlation between two Series.
        Series.shift : Shift index by desired number of periods.
        DataFrame.corr : Compute pairwise correlation of columns.

        Notes
        -----
        If the Pearson correlation is not well defined return 'NaN'.

        Examples
        --------
        >>> s = ps.Series([.2, .0, .6, .2, np.nan, .5, .6])
        >>> s.autocorr()  # doctest: +ELLIPSIS
        -0.141219...
        >>> s.autocorr(0)  # doctest: +ELLIPSIS
        1.0...
        >>> s.autocorr(2)  # doctest: +ELLIPSIS
        0.970725...
        >>> s.autocorr(-3)  # doctest: +ELLIPSIS
        0.277350...
        >>> s.autocorr(5)  # doctest: +ELLIPSIS
        -1.000000...
        >>> s.autocorr(6)  # doctest: +ELLIPSIS
        nan

        If the Pearson correlation is not well defined, then 'NaN' is returned.

        >>> s = ps.Series([1, 0, 0, 0])
        >>> s.autocorr()
        nan
        """
    def corr(self, other: Series, method: str = 'pearson', min_periods: int | None = None) -> float:
        '''
        Compute correlation with `other` Series, excluding missing values.

        .. versionadded:: 3.3.0

        Parameters
        ----------
        other : Series
        method : {\'pearson\', \'spearman\', \'kendall\'}
            * pearson : standard correlation coefficient
            * spearman : Spearman rank correlation
            * kendall : Kendall Tau correlation coefficient

            .. versionchanged:: 3.4.0
               support \'kendall\' for method parameter
        min_periods : int, optional
            Minimum number of observations needed to have a valid result.

            .. versionadded:: 3.4.0

        Returns
        -------
        correlation : float

        Notes
        -----
        The complexity of Kendall correlation is O(#row * #row), if the dataset is too
        large, sampling ahead of correlation computation is recommended.

        Examples
        --------
        >>> df = ps.DataFrame({\'s1\': [.2, .0, .6, .2],
        ...                    \'s2\': [.3, .6, .0, .1]})
        >>> s1 = df.s1
        >>> s2 = df.s2
        >>> s1.corr(s2, method=\'pearson\')
        -0.85106...

        >>> s1.corr(s2, method=\'spearman\')
        -0.94868...

        >>> s1.corr(s2, method=\'kendall\')
        -0.91287...

        >>> s1 = ps.Series([1, np.nan, 2, 1, 1, 2, 3])
        >>> s2 = ps.Series([3, 4, 1, 1, 5])

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.corr(s2, method="pearson")
        -0.52223...

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.corr(s2, method="spearman")
        -0.54433...

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.corr(s2, method="kendall")
        -0.51639...

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.corr(s2, method="kendall", min_periods=5)
        nan
        '''
    def nsmallest(self, n: int = 5) -> Series:
        """
        Return the smallest `n` elements.

        Parameters
        ----------
        n : int, default 5
            Return this many ascending sorted values.

        Returns
        -------
        Series
            The `n` smallest values in the Series, sorted in increasing order.

        See Also
        --------
        Series.nlargest: Get the `n` largest elements.
        Series.sort_values: Sort Series by values.
        Series.head: Return the first `n` rows.

        Notes
        -----
        Faster than ``.sort_values().head(n)`` for small `n` relative to
        the size of the ``Series`` object.
        In pandas-on-Spark, thanks to Spark's lazy execution and query optimizer,
        the two would have same performance.

        Examples
        --------
        >>> data = [1, 2, 3, 4, np.nan ,6, 7, 8]
        >>> s = ps.Series(data)
        >>> s
        0    1.0
        1    2.0
        2    3.0
        3    4.0
        4    NaN
        5    6.0
        6    7.0
        7    8.0
        dtype: float64

        The `n` largest elements where ``n=5`` by default.

        >>> s.nsmallest()
        0    1.0
        1    2.0
        2    3.0
        3    4.0
        5    6.0
        dtype: float64

        >>> s.nsmallest(3)
        0    1.0
        1    2.0
        2    3.0
        dtype: float64
        """
    def nlargest(self, n: int = 5) -> Series:
        """
        Return the largest `n` elements.

        Parameters
        ----------
        n : int, default 5

        Returns
        -------
        Series
            The `n` largest values in the Series, sorted in decreasing order.

        See Also
        --------
        Series.nsmallest: Get the `n` smallest elements.
        Series.sort_values: Sort Series by values.
        Series.head: Return the first `n` rows.

        Notes
        -----
        Faster than ``.sort_values(ascending=False).head(n)`` for small `n`
        relative to the size of the ``Series`` object.

        In pandas-on-Spark, thanks to Spark's lazy execution and query optimizer,
        the two would have same performance.

        Examples
        --------
        >>> data = [1, 2, 3, 4, np.nan ,6, 7, 8]
        >>> s = ps.Series(data)
        >>> s
        0    1.0
        1    2.0
        2    3.0
        3    4.0
        4    NaN
        5    6.0
        6    7.0
        7    8.0
        dtype: float64

        The `n` largest elements where ``n=5`` by default.

        >>> s.nlargest()
        7    8.0
        6    7.0
        5    6.0
        3    4.0
        2    3.0
        dtype: float64

        >>> s.nlargest(n=3)
        7    8.0
        6    7.0
        5    6.0
        dtype: float64


        """
    def append(self, to_append: Series, ignore_index: bool = False, verify_integrity: bool = False) -> Series:
        """
        Concatenate two or more Series.

        .. deprecated:: 3.4.0

        Parameters
        ----------
        to_append : Series or list/tuple of Series
        ignore_index : boolean, default False
            If True, do not use the index labels.
        verify_integrity : boolean, default False
            If True, raise Exception on creating index with duplicates

        Returns
        -------
        appended : Series

        Examples
        --------
        >>> s1 = ps.Series([1, 2, 3])
        >>> s2 = ps.Series([4, 5, 6])
        >>> s3 = ps.Series([4, 5, 6], index=[3,4,5])

        >>> s1.append(s2)
        0    1
        1    2
        2    3
        0    4
        1    5
        2    6
        dtype: int64

        >>> s1.append(s3)
        0    1
        1    2
        2    3
        3    4
        4    5
        5    6
        dtype: int64

        With ignore_index set to True:

        >>> s1.append(s2, ignore_index=True)
        0    1
        1    2
        2    3
        3    4
        4    5
        5    6
        dtype: int64
        """
    def sample(self, n: int | None = None, frac: float | None = None, replace: bool = False, random_state: int | None = None, ignore_index: bool = False) -> Series: ...
    def hist(self, bins: int = 10, **kwds): ...
    def apply(self, func: Callable, args: Sequence[Any] = (), **kwds: Any) -> Series:
        """
        Invoke function on values of Series.

        Can be a Python function that only works on the Series.

        .. note:: this API executes the function once to infer the type which is
             potentially expensive, for instance, when the dataset is created after
             aggregations or sorting.

             To avoid this, specify return type in ``func``, for instance, as below:

             >>> def square(x) -> np.int32:
             ...     return x ** 2

             pandas-on-Spark uses return type hint and does not try to infer the type.

        Parameters
        ----------
        func : function
            Python function to apply. Note that type hint for return type is required.
        args : tuple
            Positional arguments passed to func after the series value.
        **kwds
            Additional keyword arguments passed to func.

        Returns
        -------
        Series

        See Also
        --------
        Series.aggregate : Only perform aggregating type operations.
        Series.transform : Only perform transforming type operations.
        DataFrame.apply : The equivalent function for DataFrame.

        Examples
        --------
        Create a Series with typical summer temperatures for each city.

        >>> s = ps.Series([20, 21, 12],
        ...               index=['London', 'New York', 'Helsinki'])
        >>> s
        London      20
        New York    21
        Helsinki    12
        dtype: int64


        Square the values by defining a function and passing it as an
        argument to ``apply()``.

        >>> def square(x) -> np.int64:
        ...     return x ** 2
        >>> s.apply(square)
        London      400
        New York    441
        Helsinki    144
        dtype: int64


        Define a custom function that needs additional positional
        arguments and pass these additional arguments using the
        ``args`` keyword

        >>> def subtract_custom_value(x, custom_value) -> np.int64:
        ...     return x - custom_value

        >>> s.apply(subtract_custom_value, args=(5,))
        London      15
        New York    16
        Helsinki     7
        dtype: int64


        Define a custom function that takes keyword arguments
        and pass these arguments to ``apply``

        >>> def add_custom_values(x, **kwargs) -> np.int64:
        ...     for month in kwargs:
        ...         x += kwargs[month]
        ...     return x

        >>> s.apply(add_custom_values, june=30, july=20, august=25)
        London      95
        New York    96
        Helsinki    87
        dtype: int64


        Use a function from the Numpy library

        >>> def numpy_log(col) -> np.float64:
        ...     return np.log(col)
        >>> s.apply(numpy_log)
        London      2.995732
        New York    3.044522
        Helsinki    2.484907
        dtype: float64


        You can omit the type hint and let pandas-on-Spark infer its type.

        >>> s.apply(np.log)
        London      2.995732
        New York    3.044522
        Helsinki    2.484907
        dtype: float64

        """
    def aggregate(self, func: str | List[str]) -> Scalar | Series:
        """Aggregate using one or more operations over the specified axis.

        Parameters
        ----------
        func : str or a list of str
            function name(s) as string apply to series.

        Returns
        -------
        scalar, Series
            The return can be:
            - scalar : when Series.agg is called with single function
            - Series : when Series.agg is called with several functions

        Notes
        -----
        `agg` is an alias for `aggregate`. Use the alias.

        See Also
        --------
        Series.apply : Invoke function on a Series.
        Series.transform : Only perform transforming type operations.
        Series.groupby : Perform operations over groups.
        DataFrame.aggregate : The equivalent function for DataFrame.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4])
        >>> s.agg('min')
        1

        >>> s.agg(['min', 'max']).sort_index()
        max    4
        min    1
        dtype: int64
        """
    agg = aggregate
    def transpose(self, *args: Any, **kwargs: Any) -> Series:
        """
        Return the transpose, which is self.

        Examples
        --------
        It returns the same object as the transpose of the given series object, which is by
        definition self.

        >>> s = ps.Series([1, 2, 3])
        >>> s
        0    1
        1    2
        2    3
        dtype: int64

        >>> s.transpose()
        0    1
        1    2
        2    3
        dtype: int64
        """
    T: Incomplete
    def transform(self, func: Callable | List[Callable], axis: Axis = 0, *args: Any, **kwargs: Any) -> Series | DataFrame:
        """
        Call ``func`` producing the same type as `self` with transformed values
        and that has the same axis length as input.

        .. note:: this API executes the function once to infer the type which is
             potentially expensive, for instance, when the dataset is created after
             aggregations or sorting.

             To avoid this, specify return type in ``func``, for instance, as below:

             >>> def square(x) -> np.int32:
             ...     return x ** 2

             pandas-on-Spark uses return type hint and does not try to infer the type.

        Parameters
        ----------
        func : function or list
            A function or a list of functions to use for transforming the data.
        axis : int, default 0 or 'index'
            Can only be set to 0 now.
        *args
            Positional arguments to pass to `func`.
        **kwargs
            Keyword arguments to pass to `func`.

        Returns
        -------
        An instance of the same type with `self` that must have the same length as input.

        See Also
        --------
        Series.aggregate : Only perform aggregating type operations.
        Series.apply : Invoke function on Series.
        DataFrame.transform : The equivalent function for DataFrame.

        Examples
        --------

        >>> s = ps.Series(range(3))
        >>> s
        0    0
        1    1
        2    2
        dtype: int64

        >>> def sqrt(x) -> float:
        ...     return np.sqrt(x)
        >>> s.transform(sqrt)
        0    0.000000
        1    1.000000
        2    1.414214
        dtype: float64

        Even though the resulting instance must have the same length as the
        input, it is possible to provide several input functions:

        >>> def exp(x) -> float:
        ...     return np.exp(x)
        >>> s.transform([sqrt, exp])
               sqrt       exp
        0  0.000000  1.000000
        1  1.000000  2.718282
        2  1.414214  7.389056

        You can omit the type hint and let pandas-on-Spark infer its type.

        >>> s.transform([np.sqrt, np.exp])
               sqrt       exp
        0  0.000000  1.000000
        1  1.000000  2.718282
        2  1.414214  7.389056
        """
    def round(self, decimals: int = 0) -> Series:
        """
        Round each value in a Series to the given number of decimals.

        Parameters
        ----------
        decimals : int
            Number of decimal places to round to (default: 0).
            If decimals are negative, it specifies the number of
            positions to the left of the decimal point.

        Returns
        -------
        Series object

        See Also
        --------
        DataFrame.round

        Examples
        --------
        >>> df = ps.Series([0.028208, 0.038683, 0.877076], name='x')
        >>> df
        0    0.028208
        1    0.038683
        2    0.877076
        Name: x, dtype: float64

        >>> df.round(2)
        0    0.03
        1    0.04
        2    0.88
        Name: x, dtype: float64
        """
    def quantile(self, q: float | Iterable[float] = 0.5, accuracy: int = 10000) -> Scalar | Series:
        """
        Return value at the given quantile.

        .. note:: Unlike pandas', the quantile in pandas-on-Spark is an approximated quantile
            based upon approximate percentile computation because computing quantile across
            a large dataset is extremely expensive.

        Parameters
        ----------
        q : float or array-like, default 0.5 (50% quantile)
            0 <= q <= 1, the quantile(s) to compute.
        accuracy : int, optional
            Default accuracy of approximation. Larger value means better accuracy.
            The relative error can be deduced by 1.0 / accuracy.

        Returns
        -------
        float or Series
            If the current object is a Series and ``q`` is an array, a Series will be
            returned where the index is ``q`` and the values are the quantiles, otherwise
            a float will be returned.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4, 5])
        >>> s.quantile(.5)
        3.0

        >>> (s + 1).quantile(.5)
        4.0

        >>> s.quantile([.25, .5, .75])
        0.25    2.0
        0.50    3.0
        0.75    4.0
        dtype: float64

        >>> (s + 1).quantile([.25, .5, .75])
        0.25    3.0
        0.50    4.0
        0.75    5.0
        dtype: float64
        """
    def rank(self, method: str = 'average', ascending: bool = True, numeric_only: bool | None = None) -> Series:
        """
        Compute numerical data ranks (1 through n) along axis. Equal values are
        assigned a rank that is the average of the ranks of those values.

        .. note:: the current implementation of rank uses Spark's Window without
            specifying partition specification. This leads to moveing all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        method : {'average', 'min', 'max', 'first', 'dense'}
            * average: average rank of group
            * min: lowest rank in group
            * max: highest rank in group
            * first: ranks assigned in order they appear in the array
            * dense: like 'min', but rank always increases by 1 between groups
        ascending : boolean, default True
            False for ranks by high (1) to low (N)
        numeric_only : bool, optional
            If set to True, rank numeric Series, or return an empty Series for non-numeric Series

        Returns
        -------
        ranks : same type as caller

        Examples
        --------
        >>> s = ps.Series([1, 2, 2, 3], name='A')
        >>> s
        0    1
        1    2
        2    2
        3    3
        Name: A, dtype: int64

        >>> s.rank()
        0    1.0
        1    2.5
        2    2.5
        3    4.0
        Name: A, dtype: float64

        If method is set to 'min', it uses lowest rank in group.

        >>> s.rank(method='min')
        0    1.0
        1    2.0
        2    2.0
        3    4.0
        Name: A, dtype: float64

        If method is set to 'max', it uses highest rank in group.

        >>> s.rank(method='max')
        0    1.0
        1    3.0
        2    3.0
        3    4.0
        Name: A, dtype: float64

        If method is set to 'first', it is assigned rank in order without groups.

        >>> s.rank(method='first')
        0    1.0
        1    2.0
        2    3.0
        3    4.0
        Name: A, dtype: float64

        If method is set to 'dense', it leaves no gaps in group.

        >>> s.rank(method='dense')
        0    1.0
        1    2.0
        2    2.0
        3    3.0
        Name: A, dtype: float64

        If numeric_only is set to 'True', rank only numeric Series,
        return an empty Series otherwise.

        >>> s = ps.Series(['a', 'b', 'c'], name='A', index=['x', 'y', 'z'])
        >>> s
        x    a
        y    b
        z    c
        Name: A, dtype: object

        >>> s.rank(numeric_only=True)
        Series([], Name: A, dtype: float64)
        """
    def filter(self, items: Sequence[Any] | None = None, like: str | None = None, regex: str | None = None, axis: Axis | None = None) -> Series: ...
    def describe(self, percentiles: List[float] | None = None) -> Series: ...
    def diff(self, periods: int = 1) -> Series:
        """
        First discrete difference of element.

        Calculates the difference of a Series element compared with another element in the
        DataFrame (default is the element in the same column of the previous row).

        .. note:: the current implementation of diff uses Spark's Window without
            specifying partition specification. This leads to moveing all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for calculating difference, accepts negative values.

        Returns
        -------
        diffed : Series

        Examples
        --------
        >>> df = ps.DataFrame({'a': [1, 2, 3, 4, 5, 6],
        ...                    'b': [1, 1, 2, 3, 5, 8],
        ...                    'c': [1, 4, 9, 16, 25, 36]}, columns=['a', 'b', 'c'])
        >>> df
           a  b   c
        0  1  1   1
        1  2  1   4
        2  3  2   9
        3  4  3  16
        4  5  5  25
        5  6  8  36

        >>> df.b.diff()
        0    NaN
        1    0.0
        2    1.0
        3    1.0
        4    2.0
        5    3.0
        Name: b, dtype: float64

        Difference with previous value

        >>> df.c.diff(periods=3)
        0     NaN
        1     NaN
        2     NaN
        3    15.0
        4    21.0
        5    27.0
        Name: c, dtype: float64

        Difference with following value

        >>> df.c.diff(periods=-1)
        0    -3.0
        1    -5.0
        2    -7.0
        3    -9.0
        4   -11.0
        5     NaN
        Name: c, dtype: float64
        """
    def idxmax(self, skipna: bool = True) -> Tuple | Any:
        """
        Return the row label of the maximum value.

        If multiple values equal the maximum, the first row label with that
        value is returned.

        Parameters
        ----------
        skipna : bool, default True
            Exclude NA/null values. If the entire Series is NA, the result
            will be NA.

        Returns
        -------
        Index
            Label of the maximum value.

        Raises
        ------
        ValueError
            If the Series is empty.

        See Also
        --------
        Series.idxmin : Return index *label* of the first occurrence
            of minimum of values.

        Examples
        --------
        >>> s = ps.Series(data=[1, None, 4, 3, 5],
        ...               index=['A', 'B', 'C', 'D', 'E'])
        >>> s
        A    1.0
        B    NaN
        C    4.0
        D    3.0
        E    5.0
        dtype: float64

        >>> s.idxmax()
        'E'

        If `skipna` is False and there is an NA value in the data,
        the function returns ``nan``.

        >>> s.idxmax(skipna=False)
        nan

        In case of multi-index, you get a tuple:

        >>> index = pd.MultiIndex.from_arrays([
        ...     ['a', 'a', 'b', 'b'], ['c', 'd', 'e', 'f']], names=('first', 'second'))
        >>> s = ps.Series(data=[1, None, 4, 5], index=index)
        >>> s
        first  second
        a      c         1.0
               d         NaN
        b      e         4.0
               f         5.0
        dtype: float64

        >>> s.idxmax()
        ('b', 'f')

        If multiple values equal the maximum, the first row label with that
        value is returned.

        >>> s = ps.Series([1, 100, 1, 100, 1, 100], index=[10, 3, 5, 2, 1, 8])
        >>> s
        10      1
        3     100
        5       1
        2     100
        1       1
        8     100
        dtype: int64

        >>> s.idxmax()
        3
        """
    def idxmin(self, skipna: bool = True) -> Tuple | Any:
        """
        Return the row label of the minimum value.

        If multiple values equal the minimum, the first row label with that
        value is returned.

        Parameters
        ----------
        skipna : bool, default True
            Exclude NA/null values. If the entire Series is NA, the result
            will be NA.

        Returns
        -------
        Index
            Label of the minimum value.

        Raises
        ------
        ValueError
            If the Series is empty.

        See Also
        --------
        Series.idxmax : Return index *label* of the first occurrence
            of maximum of values.

        Notes
        -----
        This method is the Series version of ``ndarray.argmin``. This method
        returns the label of the minimum, while ``ndarray.argmin`` returns
        the position. To get the position, use ``series.values.argmin()``.

        Examples
        --------
        >>> s = ps.Series(data=[1, None, 4, 0],
        ...               index=['A', 'B', 'C', 'D'])
        >>> s
        A    1.0
        B    NaN
        C    4.0
        D    0.0
        dtype: float64

        >>> s.idxmin()
        'D'

        If `skipna` is False and there is an NA value in the data,
        the function returns ``nan``.

        >>> s.idxmin(skipna=False)
        nan

        In case of multi-index, you get a tuple:

        >>> index = pd.MultiIndex.from_arrays([
        ...     ['a', 'a', 'b', 'b'], ['c', 'd', 'e', 'f']], names=('first', 'second'))
        >>> s = ps.Series(data=[1, None, 4, 0], index=index)
        >>> s
        first  second
        a      c         1.0
               d         NaN
        b      e         4.0
               f         0.0
        dtype: float64

        >>> s.idxmin()
        ('b', 'f')

        If multiple values equal the minimum, the first row label with that
        value is returned.

        >>> s = ps.Series([1, 100, 1, 100, 1, 100], index=[10, 3, 5, 2, 1, 8])
        >>> s
        10      1
        3     100
        5       1
        2     100
        1       1
        8     100
        dtype: int64

        >>> s.idxmin()
        10
        """
    def pop(self, item: Name) -> Series | Scalar:
        """
        Return item and drop from series.

        Parameters
        ----------
        item : label
            Label of index to be popped.

        Returns
        -------
        Value that is popped from series.

        Examples
        --------
        >>> s = ps.Series(data=np.arange(3), index=['A', 'B', 'C'])
        >>> s
        A    0
        B    1
        C    2
        dtype: int64

        >>> s.pop('A')
        0

        >>> s
        B    1
        C    2
        dtype: int64

        >>> s = ps.Series(data=np.arange(3), index=['A', 'A', 'C'])
        >>> s
        A    0
        A    1
        C    2
        dtype: int64

        >>> s.pop('A')
        A    0
        A    1
        dtype: int64

        >>> s
        C    2
        dtype: int64

        Also support for MultiIndex

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...               index=midx)
        >>> s
        lama    speed      45.0
                weight    200.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.pop('lama')
        speed      45.0
        weight    200.0
        length      1.2
        dtype: float64

        >>> s
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        Also support for MultiIndex with several indexes.

        >>> midx = pd.MultiIndex([['a', 'b', 'c'],
        ...                       ['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 0, 0, 0, 1, 1, 1],
        ...                       [0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 0, 2]]
        ...  )
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...              index=midx)
        >>> s
        a  lama    speed      45.0
                   weight    200.0
                   length      1.2
           cow     speed      30.0
                   weight    250.0
                   length      1.5
        b  falcon  speed     320.0
                   speed       1.0
                   length      0.3
        dtype: float64

        >>> s.pop(('a', 'lama'))
        speed      45.0
        weight    200.0
        length      1.2
        dtype: float64

        >>> s
        a  cow     speed      30.0
                   weight    250.0
                   length      1.5
        b  falcon  speed     320.0
                   speed       1.0
                   length      0.3
        dtype: float64

        >>> s.pop(('b', 'falcon', 'speed'))
        (b, falcon, speed)    320.0
        (b, falcon, speed)      1.0
        dtype: float64
        """
    def copy(self, deep: bool = True) -> Series:
        '''
        Make a copy of this object\'s indices and data.

        Parameters
        ----------
        deep : bool, default True
            this parameter is not supported but just dummy parameter to match pandas.

        Returns
        -------
        copy : Series

        Examples
        --------
        >>> s = ps.Series([1, 2], index=["a", "b"])
        >>> s
        a    1
        b    2
        dtype: int64
        >>> s_copy = s.copy()
        >>> s_copy
        a    1
        b    2
        dtype: int64
        '''
    def mode(self, dropna: bool = True) -> Series:
        """
        Return the mode(s) of the dataset.

        Always returns Series even if only one value is returned.

        .. versionchanged:: 3.4.0
           Series name is preserved to follow pandas 1.4+ behavior.

        Parameters
        ----------
        dropna : bool, default True
            Don't consider counts of NaN/NaT.

        Returns
        -------
        Series
            Modes of the Series.

        Examples
        --------
        >>> s = ps.Series([0, 0, 1, 1, 1, np.nan, np.nan, np.nan])
        >>> s
        0    0.0
        1    0.0
        2    1.0
        3    1.0
        4    1.0
        5    NaN
        6    NaN
        7    NaN
        dtype: float64

        >>> s.mode()
        0    1.0
        dtype: float64

        If there are several same modes, all items are shown

        >>> s = ps.Series([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3,
        ...                np.nan, np.nan, np.nan])
        >>> s
        0     0.0
        1     0.0
        2     1.0
        3     1.0
        4     1.0
        5     2.0
        6     2.0
        7     2.0
        8     3.0
        9     3.0
        10    3.0
        11    NaN
        12    NaN
        13    NaN
        dtype: float64

        >>> s.mode().sort_values()
        0    1.0
        1    2.0
        2    3.0
        dtype: float64

        With 'dropna' set to 'False', we can also see NaN in the result

        >>> s.mode(False).sort_values()
        0    1.0
        1    2.0
        2    3.0
        3    NaN
        dtype: float64
        """
    def keys(self) -> ps.Index:
        """
        Return alias for index.

        Returns
        -------
        Index
            Index of the Series.

        Examples
        --------
        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> psser = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)

        >>> psser.keys()  # doctest: +SKIP
        MultiIndex([(  'lama',  'speed'),
                    (  'lama', 'weight'),
                    (  'lama', 'length'),
                    (   'cow',  'speed'),
                    (   'cow', 'weight'),
                    (   'cow', 'length'),
                    ('falcon',  'speed'),
                    ('falcon', 'weight'),
                    ('falcon', 'length')],
                   )
        """
    def replace(self, to_replace: Any | List | Tuple | Dict | None = None, value: List | Tuple | None = None, regex: str | bool = False) -> Series:
        """
        Replace values given in to_replace with value.
        Values of the Series are replaced with other values dynamically.

        .. note:: For partial pattern matching, the replacement is against the whole string,
            which is different from pandas. That's by the nature of underlying Spark API.

        Parameters
        ----------
        to_replace : str, list, tuple, dict, Series, int, float, or None
            How to find the values that will be replaced.
            * numeric, str:

                - numeric: numeric values equal to to_replace will be replaced with value
                - str: string exactly matching to_replace will be replaced with value

            * list of str or numeric:

                - if to_replace and value are both lists or tuples, they must be the same length.
                - str and numeric rules apply as above.

            * dict:

                - Dicts can be used to specify different replacement values for different
                  existing values.
                  For example, {'a': 'b', 'y': 'z'} replaces the value ‘a’ with ‘b’ and ‘y’
                  with ‘z’. To use a dict in this way the value parameter should be None.
                - For a DataFrame a dict can specify that different values should be replaced
                  in different columns. For example, {'a': 1, 'b': 'z'} looks for the value 1
                  in column ‘a’ and the value ‘z’ in column ‘b’ and replaces these values with
                  whatever is specified in value.
                  The value parameter should not be None in this case.
                  You can treat this as a special case of passing two lists except that you are
                  specifying the column to search in.

            See the examples section for examples of each of these.

        value : scalar, dict, list, tuple, str default None
            Value to replace any values matching to_replace with.
            For a DataFrame a dict of values can be used to specify which value to use
            for each column (columns not in the dict will not be filled).
            Regular expressions, strings and lists or dicts of such objects are also allowed.

        regex: bool or str, default False
            Whether to interpret to_replace and/or value as regular expressions.
            If this is True then to_replace must be a string.
            Alternatively, this could be a regular expression in which case to_replace must be None.


        Returns
        -------
        Series
            Object after replacement.

        Examples
        --------

        Scalar `to_replace` and `value`

        >>> s = ps.Series([0, 1, 2, 3, 4])
        >>> s
        0    0
        1    1
        2    2
        3    3
        4    4
        dtype: int64

        >>> s.replace(0, 5)
        0    5
        1    1
        2    2
        3    3
        4    4
        dtype: int64

        List-like `to_replace`

        >>> s.replace([0, 4], 5000)
        0    5000
        1       1
        2       2
        3       3
        4    5000
        dtype: int64

        >>> s.replace([1, 2, 3], [10, 20, 30])
        0     0
        1    10
        2    20
        3    30
        4     4
        dtype: int64

        Dict-like `to_replace`

        >>> s.replace({1: 1000, 2: 2000, 3: 3000, 4: 4000})
        0       0
        1    1000
        2    2000
        3    3000
        4    4000
        dtype: int64

        Also support for MultiIndex

        >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...               index=midx)
        >>> s
        lama    speed      45.0
                weight    200.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.replace(45, 450)
        lama    speed     450.0
                weight    200.0
                length      1.2
        cow     speed      30.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.replace([45, 30, 320], 500)
        lama    speed     500.0
                weight    200.0
                length      1.2
        cow     speed     500.0
                weight    250.0
                length      1.5
        falcon  speed     500.0
                weight      1.0
                length      0.3
        dtype: float64

        >>> s.replace({45: 450, 30: 300})
        lama    speed     450.0
                weight    200.0
                length      1.2
        cow     speed     300.0
                weight    250.0
                length      1.5
        falcon  speed     320.0
                weight      1.0
                length      0.3
        dtype: float64

        Regular expression `to_replace`

        >>> psser = ps.Series(['bat', 'foo', 'bait', 'abc', 'bar', 'zoo'])
        >>> psser.replace(to_replace=r'^ba.$', value='new', regex=True)
        0     new
        1     foo
        2    bait
        3     abc
        4     new
        5     zoo
        dtype: object

        >>> psser.replace(value='new', regex=r'^.oo$')
        0     bat
        1     new
        2    bait
        3     abc
        4     bar
        5     new
        dtype: object

        For partial pattern matching, the replacement is against the whole string

        >>> psser.replace('ba', 'xx', regex=True)
        0     xx
        1    foo
        2     xx
        3    abc
        4     xx
        5    zoo
        dtype: object
        """
    def update(self, other: Series) -> None:
        '''
        Modify Series in place using non-NA values from passed Series. Aligns on index.

        Parameters
        ----------
        other : Series

        Examples
        --------
        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> s = ps.Series([1, 2, 3])
        >>> s.update(ps.Series([4, 5, 6]))
        >>> s.sort_index()
        0    4
        1    5
        2    6
        dtype: int64

        >>> s = ps.Series([\'a\', \'b\', \'c\'])
        >>> s.update(ps.Series([\'d\', \'e\'], index=[0, 2]))
        >>> s.sort_index()
        0    d
        1    b
        2    e
        dtype: object

        >>> s = ps.Series([1, 2, 3])
        >>> s.update(ps.Series([4, 5, 6, 7, 8]))
        >>> s.sort_index()
        0    4
        1    5
        2    6
        dtype: int64

        >>> s = ps.Series([1, 2, 3], index=[10, 11, 12])
        >>> s
        10    1
        11    2
        12    3
        dtype: int64

        >>> s.update(ps.Series([4, 5, 6]))
        >>> s.sort_index()
        10    1
        11    2
        12    3
        dtype: int64

        >>> s.update(ps.Series([4, 5, 6], index=[11, 12, 13]))
        >>> s.sort_index()
        10    1
        11    4
        12    5
        dtype: int64

        If ``other`` contains NaNs the corresponding values are not updated
        in the original Series.

        >>> s = ps.Series([1, 2, 3])
        >>> s.update(ps.Series([4, np.nan, 6]))
        >>> s.sort_index()
        0    4.0
        1    2.0
        2    6.0
        dtype: float64

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def where(self, cond: Series, other: Any = ...) -> Series:
        '''
        Replace values where the condition is False.

        Parameters
        ----------
        cond : boolean Series
            Where cond is True, keep the original value. Where False,
            replace with corresponding value from other.
        other : scalar, Series
            Entries where cond is False are replaced with corresponding value from other.

        Returns
        -------
        Series

        Examples
        --------

        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> s1 = ps.Series([0, 1, 2, 3, 4])
        >>> s2 = ps.Series([100, 200, 300, 400, 500])
        >>> s1.where(s1 > 0).sort_index()
        0    NaN
        1    1.0
        2    2.0
        3    3.0
        4    4.0
        dtype: float64

        >>> s1.where(s1 > 1, 10).sort_index()
        0    10
        1    10
        2     2
        3     3
        4     4
        dtype: int64

        >>> s1.where(s1 > 1, s1 + 100).sort_index()
        0    100
        1    101
        2      2
        3      3
        4      4
        dtype: int64

        >>> s1.where(s1 > 1, s2).sort_index()
        0    100
        1    200
        2      2
        3      3
        4      4
        dtype: int64

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def mask(self, cond: Series, other: Any = ...) -> Series:
        '''
        Replace values where the condition is True.

        Parameters
        ----------
        cond : boolean Series
            Where cond is False, keep the original value. Where True,
            replace with corresponding value from other.
        other : scalar, Series
            Entries where cond is True are replaced with corresponding value from other.

        Returns
        -------
        Series

        Examples
        --------

        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> s1 = ps.Series([0, 1, 2, 3, 4])
        >>> s2 = ps.Series([100, 200, 300, 400, 500])
        >>> s1.mask(s1 > 0).sort_index()
        0    0.0
        1    NaN
        2    NaN
        3    NaN
        4    NaN
        dtype: float64

        >>> s1.mask(s1 > 1, 10).sort_index()
        0     0
        1     1
        2    10
        3    10
        4    10
        dtype: int64

        >>> s1.mask(s1 > 1, s1 + 100).sort_index()
        0      0
        1      1
        2    102
        3    103
        4    104
        dtype: int64

        >>> s1.mask(s1 > 1, s2).sort_index()
        0      0
        1      1
        2    300
        3    400
        4    500
        dtype: int64

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def xs(self, key: Name, level: int | None = None) -> Series:
        """
        Return cross-section from the Series.

        This method takes a `key` argument to select data at a particular
        level of a MultiIndex.

        Parameters
        ----------
        key : label or tuple of label
            Label contained in the index, or partially in a MultiIndex.
        level : object, defaults to first n levels (n=1 or len(key))
            In case of a key partially contained in a MultiIndex, indicate
            which levels are used. Levels can be referred by label or position.

        Returns
        -------
        Series
            Cross-section from the original Series
            corresponding to the selected index levels.

        Examples
        --------
        >>> midx = pd.MultiIndex([['a', 'b', 'c'],
        ...                       ['lama', 'cow', 'falcon'],
        ...                       ['speed', 'weight', 'length']],
        ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
        ...               index=midx)
        >>> s
        a  lama    speed      45.0
                   weight    200.0
                   length      1.2
        b  cow     speed      30.0
                   weight    250.0
                   length      1.5
        c  falcon  speed     320.0
                   weight      1.0
                   length      0.3
        dtype: float64

        Get values at specified index

        >>> s.xs('a')
        lama  speed      45.0
              weight    200.0
              length      1.2
        dtype: float64

        Get values at several indexes

        >>> s.xs(('a', 'lama'))
        speed      45.0
        weight    200.0
        length      1.2
        dtype: float64

        Get values at specified index and level

        >>> s.xs('lama', level=1)
        a  speed      45.0
           weight    200.0
           length      1.2
        dtype: float64
        """
    def pct_change(self, periods: int = 1) -> Series:
        """
        Percentage change between the current and a prior element.

        .. note:: the current implementation of this API uses Spark's Window without
            specifying partition specification. This leads to moveing all data into
            a single partition in a single machine and could cause serious
            performance degradation. Avoid this method with very large datasets.

        Parameters
        ----------
        periods : int, default 1
            Periods to shift for forming percent change.

        Returns
        -------
        Series

        Examples
        --------

        >>> psser = ps.Series([90, 91, 85], index=[2, 4, 1])
        >>> psser
        2    90
        4    91
        1    85
        dtype: int64

        >>> psser.pct_change()
        2         NaN
        4    0.011111
        1   -0.065934
        dtype: float64

        >>> psser.sort_index().pct_change()
        1         NaN
        2    0.058824
        4    0.011111
        dtype: float64

        >>> psser.pct_change(periods=2)
        2         NaN
        4         NaN
        1   -0.055556
        dtype: float64
        """
    def combine_first(self, other: Series) -> Series:
        '''
        Combine Series values, choosing the calling Series\'s values first.

        Parameters
        ----------
        other : Series
            The value(s) to be combined with the `Series`.

        Returns
        -------
        Series
            The result of combining the Series with the other object.

        See Also
        --------
        Series.combine : Perform element-wise operation on two Series
            using a given function.

        Notes
        -----
        Result index will be the union of the two indexes.

        Examples
        --------
        >>> s1 = ps.Series([1, np.nan])
        >>> s2 = ps.Series([3, 4])
        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s1.combine_first(s2)
        0    1.0
        1    4.0
        dtype: float64
        '''
    def dot(self, other: Series | DataFrame) -> Scalar | Series:
        '''
        Compute the dot product between the Series and the columns of other.

        This method computes the dot product between the Series and another
        one, or the Series and each columns of a DataFrame.

        It can also be called using `self @ other` in Python >= 3.5.

        .. note:: This API is slightly different from pandas when indexes from both Series
            are not aligned and config \'compute.eager_check\' is False. pandas raise an exception;
            however, pandas-on-Spark just proceeds and performs by ignoring mismatches with NaN
            permissively.

            >>> pdf1 = pd.Series([1, 2, 3], index=[0, 1, 2])
            >>> pdf2 = pd.Series([1, 2, 3], index=[0, 1, 3])
            >>> pdf1.dot(pdf2)  # doctest: +SKIP
            ...
            ValueError: matrices are not aligned

            >>> psdf1 = ps.Series([1, 2, 3], index=[0, 1, 2])
            >>> psdf2 = ps.Series([1, 2, 3], index=[0, 1, 3])
            >>> with ps.option_context("compute.eager_check", False):
            ...     psdf1.dot(psdf2)  # doctest: +SKIP
            ...
            5

        Parameters
        ----------
        other : Series, DataFrame.
            The other object to compute the dot product with its columns.

        Returns
        -------
        scalar, Series
            Return the dot product of the Series and other if other is a
            Series, the Series of the dot product of Series and each row of
            other if other is a DataFrame.

        Notes
        -----
        The Series and other must share the same index if other are a Series
        or a DataFrame.

        Examples
        --------
        >>> s = ps.Series([0, 1, 2, 3])

        >>> s.dot(s)
        14

        >>> s @ s
        14

        >>> psdf = ps.DataFrame({\'x\': [0, 1, 2, 3], \'y\': [0, -1, -2, -3]})
        >>> psdf
           x  y
        0  0  0
        1  1 -1
        2  2 -2
        3  3 -3

        >>> with ps.option_context("compute.ops_on_diff_frames", True):
        ...     s.dot(psdf)
        ...
        x    14
        y   -14
        dtype: int64
        '''
    def __matmul__(self, other: Series | DataFrame) -> Scalar | Series:
        """
        Matrix multiplication using binary `@` operator in Python>=3.5.
        """
    def repeat(self, repeats: int | Series) -> Series:
        """
        Repeat elements of a Series.

        Returns a new Series where each element of the current Series
        is repeated consecutively a given number of times.

        Parameters
        ----------
        repeats : int or Series
            The number of repetitions for each element. This should be a
            non-negative integer. Repeating 0 times will return an empty
            Series.

        Returns
        -------
        Series
            Newly created Series with repeated elements.

        See Also
        --------
        Index.repeat : Equivalent function for Index.

        Examples
        --------
        >>> s = ps.Series(['a', 'b', 'c'])
        >>> s
        0    a
        1    b
        2    c
        dtype: object
        >>> s.repeat(2)
        0    a
        1    b
        2    c
        0    a
        1    b
        2    c
        dtype: object
        >>> ps.Series([1, 2, 3]).repeat(0)
        Series([], dtype: int64)
        """
    def asof(self, where: Any | List) -> Scalar | Series:
        '''
        Return the last row(s) without any NaNs before `where`.

        The last row (for each element in `where`, if list) without any
        NaN is taken.

        If there is no good value, NaN is returned.

        .. note:: This API is dependent on :meth:`Index.is_monotonic_increasing`
            which is expensive.

        Parameters
        ----------
        where : index or array-like of indices

        Returns
        -------
        scalar or Series

            The return can be:

            * scalar : when `self` is a Series and `where` is a scalar
            * Series: when `self` is a Series and `where` is an array-like

            Return scalar or Series

        Notes
        -----
        Indices are assumed to be sorted. Raises if this is not the case and config
        \'compute.eager_check\' is True. If \'compute.eager_check\' is False pandas-on-Spark just
        proceeds and performs by ignoring the indeces\'s order

        Examples
        --------
        >>> s = ps.Series([1, 2, np.nan, 4], index=[10, 20, 30, 40])
        >>> s
        10    1.0
        20    2.0
        30    NaN
        40    4.0
        dtype: float64

        A scalar `where`.

        >>> s.asof(20)
        2.0

        For a sequence `where`, a Series is returned. The first value is
        NaN, because the first element of `where` is before the first
        index value.

        >>> s.asof([5, 20]).sort_index()
        5     NaN
        20    2.0
        dtype: float64

        Missing values are not considered. The following is ``2.0``, not
        NaN, even though NaN is at the index location for ``30``.

        >>> s.asof(30)
        2.0

        >>> s = ps.Series([1, 2, np.nan, 4], index=[10, 30, 20, 40])
        >>> with ps.option_context("compute.eager_check", False):
        ...     s.asof(20)
        ...
        1.0
        '''
    def mad(self) -> float:
        """
        Return the mean absolute deviation of values.

        .. deprecated:: 3.4.0

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4])
        >>> s
        0    1
        1    2
        2    3
        3    4
        dtype: int64

        >>> s.mad()
        1.0
        """
    def unstack(self, level: int = -1) -> DataFrame:
        """
        Unstack, a.k.a. pivot, Series with MultiIndex to produce DataFrame.
        The level involved will automatically get sorted.

        Notes
        -----
        Unlike pandas, pandas-on-Spark doesn't check whether an index is duplicated or not
        because the checking of duplicated index requires scanning whole data which
        can be quite expensive.

        Parameters
        ----------
        level : int, str, or list of these, default last level
            Level(s) to unstack, can pass level name.

        Returns
        -------
        DataFrame
            Unstacked Series.

        Examples
        --------
        >>> s = ps.Series([1, 2, 3, 4],
        ...               index=pd.MultiIndex.from_product([['one', 'two'],
        ...                                                 ['a', 'b']]))
        >>> s
        one  a    1
             b    2
        two  a    3
             b    4
        dtype: int64

        >>> s.unstack(level=-1).sort_index()
             a  b
        one  1  2
        two  3  4

        >>> s.unstack(level=0).sort_index()
           one  two
        a    1    3
        b    2    4
        """
    def item(self) -> Scalar:
        """
        Return the first element of the underlying data as a Python scalar.

        Returns
        -------
        scalar
            The first element of Series.

        Raises
        ------
        ValueError
            If the data is not length-1.

        Examples
        --------
        >>> psser = ps.Series([10])
        >>> psser.item()
        10
        """
    def items(self) -> Iterable[Tuple[Name, Any]]:
        '''
        Lazily iterate over (index, value) tuples.

        This method returns an iterable tuple (index, value). This is
        convenient if you want to create a lazy iterator.

        .. note:: Unlike pandas\', the iteritems in pandas-on-Spark returns generator rather
            zip object

        Returns
        -------
        iterable
            Iterable of tuples containing the (index, value) pairs from a
            Series.

        See Also
        --------
        DataFrame.items : Iterate over (column name, Series) pairs.
        DataFrame.iterrows : Iterate over DataFrame rows as (index, Series) pairs.

        Examples
        --------
        >>> s = ps.Series([\'A\', \'B\', \'C\'])
        >>> for index, value in s.items():
        ...     print("Index : {}, Value : {}".format(index, value))
        Index : 0, Value : A
        Index : 1, Value : B
        Index : 2, Value : C
        '''
    def iteritems(self) -> Iterable[Tuple[Name, Any]]:
        """
        This is an alias of ``items``.

        .. deprecated:: 3.4.0
            iteritems is deprecated and will be removed in a future version.
            Use .items instead.
        """
    def droplevel(self, level: int | Name | List[int | Name]) -> Series:
        '''
        Return Series with requested index level(s) removed.

        Parameters
        ----------
        level : int, str, or list-like
            If a string is given, must be the name of a level
            If list-like, elements must be names or positional indexes
            of levels.

        Returns
        -------
        Series
            Series with requested index level(s) removed.

        Examples
        --------
        >>> psser = ps.Series(
        ...     [1, 2, 3],
        ...     index=pd.MultiIndex.from_tuples(
        ...         [("x", "a"), ("x", "b"), ("y", "c")], names=["level_1", "level_2"]
        ...     ),
        ... )
        >>> psser
        level_1  level_2
        x        a          1
                 b          2
        y        c          3
        dtype: int64

        Removing specific index level by level

        >>> psser.droplevel(0)
        level_2
        a    1
        b    2
        c    3
        dtype: int64

        Removing specific index level by name

        >>> psser.droplevel("level_2")
        level_1
        x    1
        x    2
        y    3
        dtype: int64
        '''
    def tail(self, n: int = 5) -> Series:
        """
        Return the last `n` rows.

        This function returns last `n` rows from the object based on
        position. It is useful for quickly verifying data, for example,
        after sorting or appending rows.

        For negative values of `n`, this function returns all rows except
        the first `n` rows, equivalent to ``df[n:]``.

        Parameters
        ----------
        n : int, default 5
            Number of rows to select.

        Returns
        -------
        type of caller
            The last `n` rows of the caller object.

        See Also
        --------
        DataFrame.head : The first `n` rows of the caller object.

        Examples
        --------
        >>> psser = ps.Series([1, 2, 3, 4, 5])
        >>> psser
        0    1
        1    2
        2    3
        3    4
        4    5
        dtype: int64

        >>> psser.tail(3)  # doctest: +SKIP
        2    3
        3    4
        4    5
        dtype: int64
        """
    def explode(self) -> Series:
        """
        Transform each element of a list-like to a row.

        Returns
        -------
        Series
            Exploded lists to rows; index will be duplicated for these rows.

        See Also
        --------
        Series.str.split : Split string values on specified separator.
        Series.unstack : Unstack, a.k.a. pivot, Series with MultiIndex
            to produce DataFrame.
        DataFrame.melt : Unpivot a DataFrame from wide format to long format.
        DataFrame.explode : Explode a DataFrame from list-like
            columns to long format.

        Examples
        --------
        >>> psser = ps.Series([[1, 2, 3], [], [3, 4]])
        >>> psser
        0    [1, 2, 3]
        1           []
        2       [3, 4]
        dtype: object

        >>> psser.explode()  # doctest: +SKIP
        0    1.0
        0    2.0
        0    3.0
        1    NaN
        2    3.0
        2    4.0
        dtype: float64
        """
    def argsort(self) -> Series:
        """
        Return the integer indices that would sort the Series values.
        Unlike pandas, the index order is not preserved in the result.

        Returns
        -------
        Series
            Positions of values within the sort order with -1 indicating
            nan values.

        Examples
        --------
        >>> psser = ps.Series([3, 3, 4, 1, 6, 2, 3, 7, 8, 7, 10])
        >>> psser
        0      3
        1      3
        2      4
        3      1
        4      6
        5      2
        6      3
        7      7
        8      8
        9      7
        10    10
        dtype: int64

        >>> psser.argsort().sort_index()
        0      3
        1      5
        2      0
        3      1
        4      6
        5      2
        6      4
        7      7
        8      9
        9      8
        10    10
        dtype: int64
        """
    def argmax(self, axis: Axis = None, skipna: bool = True) -> int:
        """
        Return int position of the largest value in the Series.

        If the maximum is achieved in multiple locations,
        the first row position is returned.

        Parameters
        ----------
        axis : None
            Dummy argument for consistency with Series.
        skipna : bool, default True
            Exclude NA/null values.

        Returns
        -------
        int
            Row position of the maximum value.

        Examples
        --------
        Consider dataset containing cereal calories

        >>> s = ps.Series({'Corn Flakes': 100.0, 'Almond Delight': 110.0, 'Unknown': np.nan,
        ...                'Cinnamon Toast Crunch': 120.0, 'Cocoa Puff': 110.0})
        >>> s
        Corn Flakes              100.0
        Almond Delight           110.0
        Unknown                    NaN
        Cinnamon Toast Crunch    120.0
        Cocoa Puff               110.0
        dtype: float64

        >>> s.argmax()
        3

        >>> s.argmax(skipna=False)
        -1
        """
    def argmin(self, axis: Axis = None, skipna: bool = True) -> int:
        """
        Return int position of the smallest value in the Series.

        If the minimum is achieved in multiple locations,
        the first row position is returned.

        Parameters
        ----------
        axis : None
            Dummy argument for consistency with Series.
        skipna : bool, default True
            Exclude NA/null values.

        Returns
        -------
        int
            Row position of the minimum value.

        Examples
        --------
        Consider dataset containing cereal calories

        >>> s = ps.Series({'Corn Flakes': 100.0, 'Almond Delight': 110.0,
        ...                'Cinnamon Toast Crunch': 120.0, 'Cocoa Puff': 110.0})
        >>> s  # doctest: +SKIP
        Corn Flakes              100.0
        Almond Delight           110.0
        Cinnamon Toast Crunch    120.0
        Cocoa Puff               110.0
        dtype: float64

        >>> s.argmin()  # doctest: +SKIP
        0
        """
    def compare(self, other: Series, keep_shape: bool = False, keep_equal: bool = False) -> DataFrame:
        '''
        Compare to another Series and show the differences.

        .. note:: This API is slightly different from pandas when indexes from both Series
            are not identical and config \'compute.eager_check\' is False. pandas raise an exception;
            however, pandas-on-Spark just proceeds and performs by ignoring mismatches.

            >>> psser1 = ps.Series([1, 2, 3, 4, 5], index=pd.Index([1, 2, 3, 4, 5]))
            >>> psser2 = ps.Series([1, 2, 3, 4, 5], index=pd.Index([1, 2, 4, 3, 6]))
            >>> psser1.compare(psser2)  # doctest: +SKIP
            ...
            ValueError: Can only compare identically-labeled Series objects

            >>> with ps.option_context("compute.eager_check", False):
            ...     psser1.compare(psser2)  # doctest: +SKIP
            ...
               self  other
            3   3.0    4.0
            4   4.0    3.0
            5   5.0    NaN
            6   NaN    5.0

        Parameters
        ----------
        other : Series
            Object to compare with.
        keep_shape : bool, default False
            If true, all rows and columns are kept.
            Otherwise, only the ones with different values are kept.
        keep_equal : bool, default False
            If true, the result keeps values that are equal.
            Otherwise, equal values are shown as NaNs.

        Returns
        -------
        DataFrame

        Notes
        -----
        Matching NaNs will not appear as a difference.

        Examples
        --------

        >>> from pyspark.pandas.config import set_option, reset_option
        >>> set_option("compute.ops_on_diff_frames", True)
        >>> s1 = ps.Series(["a", "b", "c", "d", "e"])
        >>> s2 = ps.Series(["a", "a", "c", "b", "e"])

        Align the differences on columns

        >>> s1.compare(s2).sort_index()
          self other
        1    b     a
        3    d     b

        Keep all original rows

        >>> s1.compare(s2, keep_shape=True).sort_index()
           self other
        0  None  None
        1     b     a
        2  None  None
        3     d     b
        4  None  None

        Keep all original rows and all original values

        >>> s1.compare(s2, keep_shape=True, keep_equal=True).sort_index()
          self other
        0    a     a
        1    b     a
        2    c     c
        3    d     b
        4    e     e

        >>> reset_option("compute.ops_on_diff_frames")
        '''
    def searchsorted(self, value: Any, side: str = 'left') -> int:
        '''
        Find indices where elements should be inserted to maintain order.

        Find the indices into a sorted Series self such that, if the corresponding elements
        in value were inserted before the indices, the order of self would be preserved.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        value : scalar
            Values to insert into self.
        side : {‘left’, ‘right’}, optional
            If ‘left’, the index of the first suitable location found is given.
            If ‘right’, return the last such index. If there is no suitable index,
            return either 0 or N (where N is the length of self).

        Returns
        -------
        int
            insertion point

        Notes
        -----
        The Series must be monotonically sorted, otherwise wrong locations will likely be returned.

        Examples
        --------
        >>> ser = ps.Series([1, 2, 2, 3])
        >>> ser.searchsorted(0)
        0
        >>> ser.searchsorted(1)
        0
        >>> ser.searchsorted(2)
        1
        >>> ser.searchsorted(5)
        4
        >>> ser.searchsorted(0, side="right")
        0
        >>> ser.searchsorted(1, side="right")
        1
        >>> ser.searchsorted(2, side="right")
        3
        >>> ser.searchsorted(5, side="right")
        4
        '''
    def align(self, other: DataFrame | Series, join: str = 'outer', axis: Axis | None = None, copy: bool = True) -> Tuple['Series', DataFrame | Series]:
        '''
        Align two objects on their axes with the specified join method.

        Join method is specified for each axis Index.

        Parameters
        ----------
        other : DataFrame or Series
        join : {{\'outer\', \'inner\', \'left\', \'right\'}}, default \'outer\'
        axis : allowed axis of the other object, default None
            Align on index (0), columns (1), or both (None).
        copy : bool, default True
            Always returns new objects. If copy=False and no reindexing is
            required then original objects are returned.

        Returns
        -------
        (left, right) : (Series, type of other)
            Aligned objects.

        Examples
        --------
        >>> ps.set_option("compute.ops_on_diff_frames", True)
        >>> s1 = ps.Series([7, 8, 9], index=[10, 11, 12])
        >>> s2 = ps.Series(["g", "h", "i"], index=[10, 20, 30])

        >>> aligned_l, aligned_r = s1.align(s2)
        >>> aligned_l.sort_index()
        10    7.0
        11    8.0
        12    9.0
        20    NaN
        30    NaN
        dtype: float64
        >>> aligned_r.sort_index()
        10       g
        11    None
        12    None
        20       h
        30       i
        dtype: object

        Align with the join type "inner":

        >>> aligned_l, aligned_r = s1.align(s2, join="inner")
        >>> aligned_l.sort_index()
        10    7
        dtype: int64
        >>> aligned_r.sort_index()
        10    g
        dtype: object

        Align with a DataFrame:

        >>> df = ps.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]}, index=[10, 20, 30])
        >>> aligned_l, aligned_r = s1.align(df)
        >>> aligned_l.sort_index()
        10    7.0
        11    8.0
        12    9.0
        20    NaN
        30    NaN
        dtype: float64
        >>> aligned_r.sort_index()
              a     b
        10  1.0     a
        11  NaN  None
        12  NaN  None
        20  2.0     b
        30  3.0     c

        >>> ps.reset_option("compute.ops_on_diff_frames")
        '''
    def between_time(self, start_time: datetime.time | str, end_time: datetime.time | str, include_start: bool = True, include_end: bool = True, axis: Axis = 0) -> Series:
        """
        Select values between particular times of the day (example: 9:00-9:30 AM).

        By setting ``start_time`` to be later than ``end_time``,
        you can get the times that are *not* between the two times.

        Parameters
        ----------
        start_time : datetime.time or str
            Initial time as a time filter limit.
        end_time : datetime.time or str
            End time as a time filter limit.
        include_start : bool, default True
            Whether the start time needs to be included in the result.

            .. deprecated:: 3.4.0

        include_end : bool, default True
            Whether the end time needs to be included in the result.

            .. deprecated:: 3.4.0

        axis : {0 or 'index', 1 or 'columns'}, default 0
            Determine range time on index or columns value.

        Returns
        -------
        Series
            Data from the original object filtered to the specified dates range.

        Raises
        ------
        TypeError
            If the index is not  a :class:`DatetimeIndex`

        See Also
        --------
        at_time : Select values at a particular time of the day.
        last : Select final periods of time series based on a date offset.
        DatetimeIndex.indexer_between_time : Get just the index locations for
            values between particular times of the day.

        Examples
        --------
        >>> idx = pd.date_range('2018-04-09', periods=4, freq='1D20min')
        >>> psser = ps.Series([1, 2, 3, 4], index=idx)
        >>> psser
        2018-04-09 00:00:00    1
        2018-04-10 00:20:00    2
        2018-04-11 00:40:00    3
        2018-04-12 01:00:00    4
        dtype: int64

        >>> psser.between_time('0:15', '0:45')
        2018-04-10 00:20:00    2
        2018-04-11 00:40:00    3
        dtype: int64
        """
    def at_time(self, time: datetime.time | str, asof: bool = False, axis: Axis = 0) -> Series:
        """
        Select values at particular time of day (example: 9:30AM).

        Parameters
        ----------
        time : datetime.time or str
        axis : {0 or 'index', 1 or 'columns'}, default 0

        Returns
        -------
        Series

        Raises
        ------
        TypeError
            If the index is not  a :class:`DatetimeIndex`

        See Also
        --------
        between_time : Select values between particular times of the day.
        DatetimeIndex.indexer_at_time : Get just the index locations for
            values at particular time of the day.

        Examples
        --------
        >>> idx = pd.date_range('2018-04-09', periods=4, freq='12H')
        >>> psser = ps.Series([1, 2, 3, 4], index=idx)
        >>> psser
        2018-04-09 00:00:00    1
        2018-04-09 12:00:00    2
        2018-04-10 00:00:00    3
        2018-04-10 12:00:00    4
        dtype: int64

        >>> psser.at_time('12:00')
        2018-04-09 12:00:00    2
        2018-04-10 12:00:00    4
        dtype: int64
        """
    dt: Incomplete
    str: Incomplete
    cat: Incomplete
    plot: Incomplete
    def groupby(self, by: Name | Series | List[Name | Series], axis: Axis = 0, as_index: bool = True, dropna: bool = True) -> SeriesGroupBy: ...
    def resample(self, rule: str_type, closed: str_type | None = None, label: str_type | None = None, on: Series | None = None) -> SeriesResampler:
        """
        Resample time-series data.

        Convenience method for frequency conversion and resampling of time series.
        The object must have a datetime-like index (only support `DatetimeIndex` for now),
        or the caller must pass the label of a datetime-like
        series/index to the ``on`` keyword parameter.

        .. versionadded:: 3.4.0

        Parameters
        ----------
        rule : str
            The offset string or object representing target conversion.
            Currently, supported units are {'Y', 'A', 'M', 'D', 'H',
            'T', 'MIN', 'S'}.
        closed : {{'right', 'left'}}, default None
            Which side of bin interval is closed. The default is 'left'
            for all frequency offsets except for 'A', 'Y' and 'M' which all
            have a default of 'right'.
        label : {{'right', 'left'}}, default None
            Which bin edge label to label bucket with. The default is 'left'
            for all frequency offsets except for 'A', 'Y' and 'M' which all
            have a default of 'right'.
        on : Series, optional
            For a DataFrame, column to use instead of index for resampling.
            Column must be datetime-like.

        Returns
        -------
        SeriesResampler


        Examples
        --------
        Start by creating a series with 9 one minute timestamps.

        >>> index = pd.date_range('1/1/2000', periods=9, freq='T')
        >>> series = ps.Series(range(9), index=index, name='V')
        >>> series
        2000-01-01 00:00:00    0
        2000-01-01 00:01:00    1
        2000-01-01 00:02:00    2
        2000-01-01 00:03:00    3
        2000-01-01 00:04:00    4
        2000-01-01 00:05:00    5
        2000-01-01 00:06:00    6
        2000-01-01 00:07:00    7
        2000-01-01 00:08:00    8
        Name: V, dtype: int64

        Downsample the series into 3 minute bins and sum the values
        of the timestamps falling into a bin.

        >>> series.resample('3T').sum().sort_index()
        2000-01-01 00:00:00     3.0
        2000-01-01 00:03:00    12.0
        2000-01-01 00:06:00    21.0
        Name: V, dtype: float64

        Downsample the series into 3 minute bins as above, but label each
        bin using the right edge instead of the left. Please note that the
        value in the bucket used as the label is not included in the bucket,
        which it labels. For example, in the original series the
        bucket ``2000-01-01 00:03:00`` contains the value 3, but the summed
        value in the resampled bucket with the label ``2000-01-01 00:03:00``
        does not include 3 (if it did, the summed value would be 6, not 3).
        To include this value, close the right side of the bin interval as
        illustrated in the example below this one.

        >>> series.resample('3T', label='right').sum().sort_index()
        2000-01-01 00:03:00     3.0
        2000-01-01 00:06:00    12.0
        2000-01-01 00:09:00    21.0
        Name: V, dtype: float64

        Downsample the series into 3 minute bins as above, but close the right
        side of the bin interval.

        >>> series.resample('3T', label='right', closed='right').sum().sort_index()
        2000-01-01 00:00:00     0.0
        2000-01-01 00:03:00     6.0
        2000-01-01 00:06:00    15.0
        2000-01-01 00:09:00    15.0
        Name: V, dtype: float64

        Upsample the series into 30 second bins.

        >>> series.resample('30S').sum().sort_index()[0:5]   # Select first 5 rows
        2000-01-01 00:00:00    0.0
        2000-01-01 00:00:30    0.0
        2000-01-01 00:01:00    1.0
        2000-01-01 00:01:30    0.0
        2000-01-01 00:02:00    2.0
        Name: V, dtype: float64

        See Also
        --------
        DataFrame.resample : Resample a DataFrame.
        groupby : Group by mapping, function, label, or list of labels.
        """
    def __getitem__(self, key: Any) -> Any: ...
    def __getattr__(self, item: str_type) -> Any: ...
    def __dir__(self) -> Iterable[str_type]: ...
    def __iter__(self) -> None: ...
    def __class_getitem__(cls, params: Any) -> Type[SeriesType]: ...

def unpack_scalar(sdf: SparkDataFrame) -> Any:
    """
    Takes a dataframe that is supposed to contain a single row with a single scalar value,
    and returns this value.
    """
@overload
def first_series(df: DataFrame) -> Series: ...
@overload
def first_series(df: pd.DataFrame) -> pd.Series: ...
