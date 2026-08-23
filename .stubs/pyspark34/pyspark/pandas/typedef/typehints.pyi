import pandas as pd
import pyspark.sql.types as types
from _typeshed import Incomplete
from pyspark.pandas._typing import Dtype as Dtype, T as T
from pyspark.pandas.internal import InternalField as InternalField
from pyspark.sql.pandas.types import from_arrow_type as from_arrow_type, to_arrow_type as to_arrow_type
from typing import Any, Callable, Generic, List, Tuple, Type

extension_dtypes: Tuple[type, ...]
extension_dtypes_available: bool
extension_object_dtypes_available: bool
extension_float_dtypes_available: bool

class SeriesType(Generic[T]):
    dtype: Incomplete
    spark_type: Incomplete
    def __init__(self, dtype: Dtype, spark_type: types.DataType) -> None: ...

class DataFrameType:
    index_fields: Incomplete
    data_fields: Incomplete
    fields: Incomplete
    def __init__(self, index_fields: List['InternalField'], data_fields: List['InternalField']) -> None: ...
    @property
    def dtypes(self) -> List[Dtype]: ...
    @property
    def spark_type(self) -> types.StructType: ...

class ScalarType:
    dtype: Incomplete
    spark_type: Incomplete
    def __init__(self, dtype: Dtype, spark_type: types.DataType) -> None: ...

class UnknownType:
    tpe: Incomplete
    def __init__(self, tpe: Any) -> None: ...

class IndexNameTypeHolder:
    name: Incomplete
    tpe: Incomplete
    short_name: str

class NameTypeHolder:
    name: Incomplete
    tpe: Incomplete
    short_name: str

def as_spark_type(tpe: str | type | Dtype, *, raise_error: bool = True, prefer_timestamp_ntz: bool = False) -> types.DataType:
    """
    Given a Python type, returns the equivalent spark type.
    Accepts:
    - the built-in types in Python
    - the built-in types in numpy
    - list of pairs of (field_name, type)
    - dictionaries of field_name -> type
    - Python3's typing system
    """
def spark_type_to_pandas_dtype(spark_type: types.DataType, *, use_extension_dtypes: bool = False) -> Dtype:
    """Return the given Spark DataType to pandas dtype."""
def pandas_on_spark_type(tpe: str | type | Dtype) -> Tuple[Dtype, types.DataType]:
    """
    Convert input into a pandas only dtype object or a numpy dtype object,
    and its corresponding Spark DataType.

    Parameters
    ----------
    tpe : object to be converted

    Returns
    -------
    tuple of np.dtype or a pandas dtype, and Spark DataType

    Raises
    ------
    TypeError if not a dtype

    Examples
    --------
    >>> pandas_on_spark_type(int)
    (dtype('int64'), LongType())
    >>> pandas_on_spark_type(str)
    (dtype('<U'), StringType())
    >>> pandas_on_spark_type(datetime.date)
    (dtype('O'), DateType())
    >>> pandas_on_spark_type(datetime.datetime)
    (dtype('<M8[ns]'), TimestampType())
    >>> pandas_on_spark_type(datetime.timedelta)
    (dtype('<m8[ns]'), DayTimeIntervalType(0, 3))
    >>> pandas_on_spark_type(List[bool])
    (dtype('O'), ArrayType(BooleanType(), True))
    """
def infer_pd_series_spark_type(pser: pd.Series, dtype: Dtype, prefer_timestamp_ntz: bool = False) -> types.DataType:
    """Infer Spark DataType from pandas Series dtype.

    :param pser: :class:`pandas.Series` to be inferred
    :param dtype: the Series' dtype
    :param prefer_timestamp_ntz: if true, infers datetime without timezone as
        TimestampNTZType type. If false, infers it as TimestampType.
    :return: the inferred Spark data type
    """
def infer_return_type(f: Callable) -> SeriesType | DataFrameType | ScalarType | UnknownType:
    '''
    Infer the return type from the return type annotation of the given function.

    The returned type class indicates both dtypes (a pandas only dtype object
    or a numpy dtype object) and its corresponding Spark DataType.

    >>> def func() -> int:
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtype
    dtype(\'int64\')
    >>> inferred.spark_type
    LongType()

    >>> def func() -> ps.Series[int]:
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtype
    dtype(\'int64\')
    >>> inferred.spark_type
    LongType()

    >>> def func() -> ps.DataFrame[float, str]:
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'float64\'), dtype(\'<U\')]
    >>> inferred.spark_type
    StructType([StructField(\'c0\', DoubleType(), True), StructField(\'c1\', StringType(), True)])

    >>> def func() -> ps.DataFrame[float]:
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'float64\')]
    >>> inferred.spark_type
    StructType([StructField(\'c0\', DoubleType(), True)])

    >>> def func() -> \'int\':
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtype
    dtype(\'int64\')
    >>> inferred.spark_type
    LongType()

    >>> def func() -> \'ps.Series[int]\':
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtype
    dtype(\'int64\')
    >>> inferred.spark_type
    LongType()

    >>> def func() -> \'ps.DataFrame[float, str]\':
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'float64\'), dtype(\'<U\')]
    >>> inferred.spark_type
    StructType([StructField(\'c0\', DoubleType(), True), StructField(\'c1\', StringType(), True)])

    >>> def func() -> \'ps.DataFrame[float]\':
    ...    pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'float64\')]
    >>> inferred.spark_type
    StructType([StructField(\'c0\', DoubleType(), True)])

    >>> def func() -> ps.DataFrame[\'a\': float, \'b\': int]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'float64\'), dtype(\'int64\')]
    >>> inferred.spark_type
    StructType([StructField(\'a\', DoubleType(), True), StructField(\'b\', LongType(), True)])

    >>> def func() -> "ps.DataFrame[\'a\': float, \'b\': int]":
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'float64\'), dtype(\'int64\')]
    >>> inferred.spark_type
    StructType([StructField(\'a\', DoubleType(), True), StructField(\'b\', LongType(), True)])

    >>> pdf = pd.DataFrame({"a": [1, 2, 3], "b": [3, 4, 5]})
    >>> def func() -> ps.DataFrame[pdf.dtypes]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), dtype(\'int64\')]
    >>> inferred.spark_type
    StructType([StructField(\'c0\', LongType(), True), StructField(\'c1\', LongType(), True)])

    >>> pdf = pd.DataFrame({"a": [1, 2, 3], "b": [3, 4, 5]})
    >>> def func() -> ps.DataFrame[zip(pdf.columns, pdf.dtypes)]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), dtype(\'int64\')]
    >>> inferred.spark_type
    StructType([StructField(\'a\', LongType(), True), StructField(\'b\', LongType(), True)])

    >>> pdf = pd.DataFrame({("x", "a"): [1, 2, 3], ("y", "b"): [3, 4, 5]})
    >>> def func() -> ps.DataFrame[zip(pdf.columns, pdf.dtypes)]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), dtype(\'int64\')]
    >>> inferred.spark_type
    StructType([StructField(\'(x, a)\', LongType(), True), StructField(\'(y, b)\', LongType(), True)])

    >>> pdf = pd.DataFrame({"a": [1, 2, 3], "b": pd.Categorical([3, 4, 5])})
    >>> def func() -> ps.DataFrame[pdf.dtypes]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), CategoricalDtype(categories=[3, 4, 5], ordered=False)]
    >>> inferred.spark_type
    StructType([StructField(\'c0\', LongType(), True), StructField(\'c1\', LongType(), True)])

    >>> def func() -> ps.DataFrame[zip(pdf.columns, pdf.dtypes)]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), CategoricalDtype(categories=[3, 4, 5], ordered=False)]
    >>> inferred.spark_type
    StructType([StructField(\'a\', LongType(), True), StructField(\'b\', LongType(), True)])

    >>> def func() -> ps.Series[pdf.b.dtype]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtype
    CategoricalDtype(categories=[3, 4, 5], ordered=False)
    >>> inferred.spark_type
    LongType()

    >>> def func() -> ps.DataFrame[int, [int, int]]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), dtype(\'int64\'), dtype(\'int64\')]
    >>> inferred.spark_type.simpleString()
    \'struct<__index_level_0__:bigint,c0:bigint,c1:bigint>\'
    >>> inferred.index_fields
    [InternalField(dtype=int64, struct_field=StructField(\'__index_level_0__\', LongType(), True))]

    >>> def func() -> ps.DataFrame[pdf.index.dtype, pdf.dtypes]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), dtype(\'int64\'), CategoricalDtype(categories=[3, 4, 5], ordered=False)]
    >>> inferred.spark_type.simpleString()
    \'struct<__index_level_0__:bigint,c0:bigint,c1:bigint>\'
    >>> inferred.index_fields
    [InternalField(dtype=int64, struct_field=StructField(\'__index_level_0__\', LongType(), True))]

    >>> def func() -> ps.DataFrame[
    ...     ("index", CategoricalDtype(categories=[3, 4, 5], ordered=False)),
    ...     [("id", int), ("A", int)]]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [CategoricalDtype(categories=[3, 4, 5], ordered=False), dtype(\'int64\'), dtype(\'int64\')]
    >>> inferred.spark_type.simpleString()
    \'struct<index:bigint,id:bigint,A:bigint>\'
    >>> inferred.index_fields
    [InternalField(dtype=category, struct_field=StructField(\'index\', LongType(), True))]

    >>> def func() -> ps.DataFrame[
    ...         (pdf.index.name, pdf.index.dtype), zip(pdf.columns, pdf.dtypes)]:
    ...     pass
    >>> inferred = infer_return_type(func)
    >>> inferred.dtypes
    [dtype(\'int64\'), dtype(\'int64\'), CategoricalDtype(categories=[3, 4, 5], ordered=False)]
    >>> inferred.spark_type.simpleString()
    \'struct<__index_level_0__:bigint,a:bigint,b:bigint>\'
    >>> inferred.index_fields
    [InternalField(dtype=int64, struct_field=StructField(\'__index_level_0__\', LongType(), True))]
    '''
def create_type_for_series_type(param: Any) -> Type[SeriesType]:
    '''
    Supported syntax:

    >>> str(ps.Series[float]).endswith("SeriesType[float]")
    True
    '''
def create_tuple_for_frame_type(params: Any) -> object:
    '''
    This is a workaround to support variadic generic in DataFrame.

    See https://github.com/python/typing/issues/193
    we always wraps the given type hints by a tuple to mimic the variadic generic.

    Supported syntax:

    >>> import pandas as pd
    >>> pdf = pd.DataFrame({\'a\': range(1)})

    Typing data columns only:

        >>> ps.DataFrame[float, float]  # doctest: +ELLIPSIS
        typing.Tuple[...NameType, ...NameType]
        >>> ps.DataFrame[pdf.dtypes]  # doctest: +ELLIPSIS
        typing.Tuple[...NameType]
        >>> ps.DataFrame["id": int, "A": int]  # doctest: +ELLIPSIS
        typing.Tuple[...NameType, ...NameType]
        >>> ps.DataFrame[zip(pdf.columns, pdf.dtypes)]  # doctest: +ELLIPSIS
        typing.Tuple[...NameType]

    Typing data columns with an index:

        >>> ps.DataFrame[int, [int, int]]  # doctest: +ELLIPSIS
        typing.Tuple[...IndexNameType, ...NameType, ...NameType]
        >>> ps.DataFrame[pdf.index.dtype, pdf.dtypes]  # doctest: +ELLIPSIS
        typing.Tuple[...IndexNameType, ...NameType]
        >>> ps.DataFrame[("index", int), [("id", int), ("A", int)]]  # doctest: +ELLIPSIS
        typing.Tuple[...IndexNameType, ...NameType, ...NameType]
        >>> ps.DataFrame[(pdf.index.name, pdf.index.dtype), zip(pdf.columns, pdf.dtypes)]
        ... # doctest: +ELLIPSIS
        typing.Tuple[...IndexNameType, ...NameType]

    Typing data columns with an Multi-index:
        >>> arrays = [[1, 1, 2], [\'red\', \'blue\', \'red\']]
        >>> idx = pd.MultiIndex.from_arrays(arrays, names=(\'number\', \'color\'))
        >>> pdf = pd.DataFrame({\'a\': range(3)}, index=idx)
        >>> ps.DataFrame[[int, int], [int, int]]  # doctest: +ELLIPSIS
        typing.Tuple[...IndexNameType, ...IndexNameType, ...NameType, ...NameType]
        >>> ps.DataFrame[pdf.index.dtypes, pdf.dtypes]  # doctest: +ELLIPSIS, +SKIP
        typing.Tuple[...IndexNameType, ...NameType]
        >>> ps.DataFrame[[("index-1", int), ("index-2", int)], [("id", int), ("A", int)]]
        ... # doctest: +ELLIPSIS
        typing.Tuple[...IndexNameType, ...IndexNameType, ...NameType, ...NameType]
        >>> ps.DataFrame[zip(pdf.index.names, pdf.index.dtypes), zip(pdf.columns, pdf.dtypes)]
        ... # doctest: +ELLIPSIS, +SKIP
        typing.Tuple[...IndexNameType, ...NameType]
    '''
