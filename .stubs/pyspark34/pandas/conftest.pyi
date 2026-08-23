import pytest
from _typeshed import Incomplete
from collections.abc import Generator
from pandas import DataFrame as DataFrame, Interval as Interval, Period as Period, Series as Series, Timedelta as Timedelta, Timestamp as Timestamp, compat as compat
from pandas.core import ops as ops
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, IntervalDtype as IntervalDtype
from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex
from typing import Callable, Hashable

has_pyarrow: bool
zoneinfo: Incomplete

def pytest_addoption(parser) -> None: ...
def ignore_doctest_warning(item: pytest.Item, path: str, message: str) -> None:
    '''Ignore doctest warning.

    Parameters
    ----------
    item : pytest.Item
        pytest test item.
    path : str
        Module path to Python object, e.g. "pandas.core.frame.DataFrame.append". A
        warning will be filtered when item.name ends with in given path. So it is
        sufficient to specify e.g. "DataFrame.append".
    message : str
        Message to be filtered.
    '''
def pytest_collection_modifyitems(items, config) -> None: ...

cls: Incomplete

def add_doctest_imports(doctest_namespace) -> None:
    """
    Make `np` and `pd` names available for doctests.
    """
def configure_tests() -> None:
    """
    Configure settings for all tests and test modules.
    """
def axis(request):
    """
    Fixture for returning the axis numbers of a DataFrame.
    """
axis_frame = axis

def axis_1(request):
    """
    Fixture for returning aliases of axis 1 of a DataFrame.
    """
def observed(request):
    """
    Pass in the observed keyword to groupby for [True, False]
    This indicates whether categoricals should return values for
    values which are not in the grouper [False / None], or only values which
    appear in the grouper [True]. [None] is supported for future compatibility
    if we decide to change the default (and would need to warn if this
    parameter is not passed).
    """
def ordered(request):
    """
    Boolean 'ordered' parameter for Categorical.
    """
def skipna(request):
    """
    Boolean 'skipna' parameter.
    """
def keep(request):
    """
    Valid values for the 'keep' parameter used in
    .duplicated or .drop_duplicates
    """
def inclusive_endpoints_fixture(request):
    """
    Fixture for trying all interval 'inclusive' parameters.
    """
def closed(request):
    """
    Fixture for trying all interval closed parameters.
    """
def other_closed(request):
    """
    Secondary closed fixture to allow parametrizing over all pairs of closed.
    """
def compression(request):
    """
    Fixture for trying common compression types in compression tests.
    """
def compression_only(request):
    """
    Fixture for trying common compression types in compression tests excluding
    uncompressed case.
    """
def writable(request):
    """
    Fixture that an array is writable.
    """
def join_type(request):
    """
    Fixture for trying all types of join operations.
    """
def nselect_method(request):
    """
    Fixture for trying all nselect methods.
    """
def nulls_fixture(request):
    """
    Fixture for each null type in pandas.
    """
nulls_fixture2 = nulls_fixture

def unique_nulls_fixture(request):
    """
    Fixture for each null type in pandas, each null type exactly once.
    """
unique_nulls_fixture2 = unique_nulls_fixture

def np_nat_fixture(request):
    """
    Fixture for each NaT type in numpy.
    """
np_nat_fixture2 = np_nat_fixture

def frame_or_series(request):
    """
    Fixture to parametrize over DataFrame and Series.
    """
def index_or_series(request):
    '''
    Fixture to parametrize over Index and Series, made necessary by a mypy
    bug, giving an error:

    List item 0 has incompatible type "Type[Series]"; expected "Type[PandasObject]"

    See GH#29725
    '''
index_or_series2 = index_or_series

def index_or_series_or_array(request):
    """
    Fixture to parametrize over Index, Series, and ExtensionArray
    """
def box_with_array(request):
    """
    Fixture to test behavior for Index, Series, DataFrame, and pandas Array
    classes
    """
box_with_array2 = box_with_array

def dict_subclass():
    """
    Fixture for a dictionary subclass.
    """
def non_dict_mapping_subclass():
    """
    Fixture for a non-mapping dictionary subclass.
    """
def multiindex_year_month_day_dataframe_random_data():
    """
    DataFrame with 3 level MultiIndex (year, month, day) covering
    first 100 business days from 2000-01-01 with random data
    """
def lexsorted_two_level_string_multiindex() -> MultiIndex:
    """
    2-level MultiIndex, lexsorted, with string names.
    """
def multiindex_dataframe_random_data(lexsorted_two_level_string_multiindex) -> DataFrame:
    """DataFrame with 2 level MultiIndex with random data"""

indices_dict: Incomplete
idx: Incomplete

def index(request):
    '''
    Fixture for many "simple" kinds of indices.

    These indices are unlikely to cover corner cases, e.g.
        - no names
        - no NaTs/NaNs
        - no values near implementation bounds
        - ...
    '''
index_fixture2 = index

def index_flat(request):
    """
    index fixture, but excluding MultiIndex cases.
    """
index_flat2 = index_flat

def index_with_missing(request):
    """
    Fixture for indices with missing values.

    Integer-dtype and empty cases are excluded because they cannot hold missing
    values.

    MultiIndex is excluded because isna() is not defined for MultiIndex.
    """
def string_series() -> Series:
    """
    Fixture for Series of floats with Index of unique strings
    """
def object_series() -> Series:
    """
    Fixture for Series of dtype object with Index of unique strings
    """
def datetime_series() -> Series:
    """
    Fixture for Series of floats with DatetimeIndex
    """
def series_with_simple_index(index) -> Series:
    """
    Fixture for tests on series with changing types of indices.
    """
def series_with_multilevel_index() -> Series:
    """
    Fixture with a Series with a 2-level MultiIndex.
    """
def index_or_series_obj(request):
    """
    Fixture for tests on indexes, series and series with a narrow dtype
    copy to avoid mutation, e.g. setting .name
    """
def int_frame() -> DataFrame:
    """
    Fixture for DataFrame of ints with index of unique strings

    Columns are ['A', 'B', 'C', 'D']

                A  B  C  D
    vpBeWjM651  1  0  1  0
    5JyxmrP1En -1  0  0  0
    qEDaoD49U2 -1  1  0  0
    m66TkTfsFe  0  0  0  0
    EHPaNzEUFm -1  0 -1  0
    fpRJCevQhi  2  0  0  0
    OlQvnmfi3Q  0  0 -2  0
    ...        .. .. .. ..
    uB1FPlz4uP  0  0  0  1
    EcSe6yNzCU  0  0 -1  0
    L50VudaiI8 -1  1 -2  0
    y3bpw4nwIp  0 -1  0  0
    H0RdLLwrCT  1  1  0  0
    rY82K0vMwm  0  0  0  0
    1OPIUjnkjk  2  0  0  0

    [30 rows x 4 columns]
    """
def datetime_frame() -> DataFrame:
    """
    Fixture for DataFrame of floats with DatetimeIndex

    Columns are ['A', 'B', 'C', 'D']

                       A         B         C         D
    2000-01-03 -1.122153  0.468535  0.122226  1.693711
    2000-01-04  0.189378  0.486100  0.007864 -1.216052
    2000-01-05  0.041401 -0.835752 -0.035279 -0.414357
    2000-01-06  0.430050  0.894352  0.090719  0.036939
    2000-01-07 -0.620982 -0.668211 -0.706153  1.466335
    2000-01-10 -0.752633  0.328434 -0.815325  0.699674
    2000-01-11 -2.236969  0.615737 -0.829076 -1.196106
    ...              ...       ...       ...       ...
    2000-02-03  1.642618 -0.579288  0.046005  1.385249
    2000-02-04 -0.544873 -1.160962 -0.284071 -1.418351
    2000-02-07 -2.656149 -0.601387  1.410148  0.444150
    2000-02-08 -1.201881 -1.289040  0.772992 -1.445300
    2000-02-09  1.377373  0.398619  1.008453 -0.928207
    2000-02-10  0.473194 -0.636677  0.984058  0.511519
    2000-02-11 -0.965556  0.408313 -1.312844 -0.381948

    [30 rows x 4 columns]
    """
def float_frame() -> DataFrame:
    """
    Fixture for DataFrame of floats with index of unique strings

    Columns are ['A', 'B', 'C', 'D'].

                       A         B         C         D
    P7GACiRnxd -0.465578 -0.361863  0.886172 -0.053465
    qZKh6afn8n -0.466693 -0.373773  0.266873  1.673901
    tkp0r6Qble  0.148691 -0.059051  0.174817  1.598433
    wP70WOCtv8  0.133045 -0.581994 -0.992240  0.261651
    M2AeYQMnCz -1.207959 -0.185775  0.588206  0.563938
    QEPzyGDYDo -0.381843 -0.758281  0.502575 -0.565053
    r78Jwns6dn -0.653707  0.883127  0.682199  0.206159
    ...              ...       ...       ...       ...
    IHEGx9NO0T -0.277360  0.113021 -1.018314  0.196316
    lPMj8K27FA -1.313667 -0.604776 -1.305618 -0.863999
    qa66YMWQa5  1.110525  0.475310 -0.747865  0.032121
    yOa0ATsmcE -0.431457  0.067094  0.096567 -0.264962
    65znX3uRNG  1.528446  0.160416 -0.109635 -0.032987
    eCOBvKqf3e  0.235281  1.622222  0.781255  0.392871
    xSucinXxuV -1.263557  0.252799 -0.552247  0.400426

    [30 rows x 4 columns]
    """
def mixed_type_frame() -> DataFrame:
    """
    Fixture for DataFrame of float/int/string columns with RangeIndex
    Columns are ['a', 'b', 'c', 'float32', 'int32'].
    """
def rand_series_with_duplicate_datetimeindex() -> Series:
    """
    Fixture for Series with a DatetimeIndex that has duplicates.
    """
def ea_scalar_and_dtype(request): ...
def all_arithmetic_operators(request):
    """
    Fixture for dunder names for common arithmetic operations.
    """
def all_binary_operators(request):
    """
    Fixture for operator and roperator arithmetic, comparison, and logical ops.
    """
def all_arithmetic_functions(request):
    """
    Fixture for operator and roperator arithmetic functions.

    Notes
    -----
    This includes divmod and rdivmod, whereas all_arithmetic_operators
    does not.
    """
def all_numeric_reductions(request):
    """
    Fixture for numeric reduction names.
    """
def all_boolean_reductions(request):
    """
    Fixture for boolean reduction names.
    """
def all_reductions(request):
    """
    Fixture for all (boolean + numeric) reduction names.
    """
def comparison_op(request):
    """
    Fixture for operator module comparison functions.
    """
def compare_operators_no_eq_ne(request):
    """
    Fixture for dunder names for compare operations except == and !=

    * >=
    * >
    * <
    * <=
    """
def all_logical_operators(request):
    """
    Fixture for dunder names for common logical operations

    * |
    * &
    * ^
    """
def all_numeric_accumulations(request):
    """
    Fixture for numeric accumulation names
    """
def strict_data_files(pytestconfig):
    """
    Returns the configuration for the test setting `--strict-data-files`.
    """
def datapath(strict_data_files: str) -> Callable[..., str]:
    """
    Get the path to a data file.

    Parameters
    ----------
    path : str
        Path to the file, relative to ``pandas/tests/``

    Returns
    -------
    path including ``pandas/tests``.

    Raises
    ------
    ValueError
        If the path doesn't exist and the --strict-data-files option is set.
    """
def iris(datapath) -> DataFrame:
    """
    The iris dataset as a DataFrame.
    """

TIMEZONES: Incomplete
TIMEZONE_IDS: Incomplete

def tz_naive_fixture(request):
    """
    Fixture for trying timezones including default (None): {0}
    """
def tz_aware_fixture(request):
    """
    Fixture for trying explicit timezones: {0}
    """
tz_aware_fixture2 = tz_aware_fixture

def utc_fixture(request):
    """
    Fixture to provide variants of UTC timezone strings and tzinfo objects.
    """
utc_fixture2 = utc_fixture

def string_dtype(request):
    """
    Parametrized fixture for string dtypes.

    * str
    * 'str'
    * 'U'
    """
def nullable_string_dtype(request):
    """
    Parametrized fixture for string dtypes.

    * 'string[python]'
    * 'string[pyarrow]'
    """
def string_storage(request):
    """
    Parametrized fixture for pd.options.mode.string_storage.

    * 'python'
    * 'pyarrow'
    """
def dtype_backend(request):
    """
    Parametrized fixture for pd.options.mode.string_storage.

    * 'python'
    * 'pyarrow'
    """
string_storage2 = string_storage

def bytes_dtype(request):
    """
    Parametrized fixture for bytes dtypes.

    * bytes
    * 'bytes'
    """
def object_dtype(request):
    """
    Parametrized fixture for object dtypes.

    * object
    * 'object'
    """
def any_string_dtype(request):
    """
    Parametrized fixture for string dtypes.
    * 'object'
    * 'string[python]'
    * 'string[pyarrow]'
    """
def datetime64_dtype(request):
    """
    Parametrized fixture for datetime64 dtypes.

    * 'datetime64[ns]'
    * 'M8[ns]'
    """
def timedelta64_dtype(request):
    """
    Parametrized fixture for timedelta64 dtypes.

    * 'timedelta64[ns]'
    * 'm8[ns]'
    """
def fixed_now_ts() -> Timestamp:
    """
    Fixture emits fixed Timestamp.now()
    """
def float_numpy_dtype(request):
    """
    Parameterized fixture for float dtypes.

    * float
    * 'float32'
    * 'float64'
    """
def float_ea_dtype(request):
    """
    Parameterized fixture for float dtypes.

    * 'Float32'
    * 'Float64'
    """
def any_float_dtype(request):
    """
    Parameterized fixture for float dtypes.

    * float
    * 'float32'
    * 'float64'
    * 'Float32'
    * 'Float64'
    """
def complex_dtype(request):
    """
    Parameterized fixture for complex dtypes.

    * complex
    * 'complex64'
    * 'complex128'
    """
def any_signed_int_numpy_dtype(request):
    """
    Parameterized fixture for signed integer dtypes.

    * int
    * 'int8'
    * 'int16'
    * 'int32'
    * 'int64'
    """
def any_unsigned_int_numpy_dtype(request):
    """
    Parameterized fixture for unsigned integer dtypes.

    * 'uint8'
    * 'uint16'
    * 'uint32'
    * 'uint64'
    """
def any_int_numpy_dtype(request):
    """
    Parameterized fixture for any integer dtype.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    """
def any_int_ea_dtype(request):
    """
    Parameterized fixture for any nullable integer dtype.

    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    """
def any_int_dtype(request):
    """
    Parameterized fixture for any nullable integer dtype.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    """
def any_numeric_ea_dtype(request):
    """
    Parameterized fixture for any nullable integer dtype and
    any float ea dtypes.

    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    * 'Float32'
    * 'Float64'
    """
def any_numeric_ea_and_arrow_dtype(request):
    """
    Parameterized fixture for any nullable integer dtype and
    any float ea dtypes.

    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    * 'Float32'
    * 'Float64'
    * 'uint8[pyarrow]'
    * 'int8[pyarrow]'
    * 'uint16[pyarrow]'
    * 'int16[pyarrow]'
    * 'uint32[pyarrow]'
    * 'int32[pyarrow]'
    * 'uint64[pyarrow]'
    * 'int64[pyarrow]'
    * 'float32[pyarrow]'
    * 'float64[pyarrow]'
    """
def any_signed_int_ea_dtype(request):
    """
    Parameterized fixture for any signed nullable integer dtype.

    * 'Int8'
    * 'Int16'
    * 'Int32'
    * 'Int64'
    """
def any_real_numpy_dtype(request):
    """
    Parameterized fixture for any (purely) real numeric dtype.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * float
    * 'float32'
    * 'float64'
    """
def any_real_numeric_dtype(request):
    """
    Parameterized fixture for any (purely) real numeric dtype.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * float
    * 'float32'
    * 'float64'

    and associated ea dtypes.
    """
def any_numpy_dtype(request):
    """
    Parameterized fixture for all numpy dtypes.

    * bool
    * 'bool'
    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * float
    * 'float32'
    * 'float64'
    * complex
    * 'complex64'
    * 'complex128'
    * str
    * 'str'
    * 'U'
    * bytes
    * 'bytes'
    * 'datetime64[ns]'
    * 'M8[ns]'
    * 'timedelta64[ns]'
    * 'm8[ns]'
    * object
    * 'object'
    """
def any_numeric_dtype(request):
    """
    Parameterized fixture for all numeric dtypes.

    * int
    * 'int8'
    * 'uint8'
    * 'int16'
    * 'uint16'
    * 'int32'
    * 'uint32'
    * 'int64'
    * 'uint64'
    * float
    * 'float32'
    * 'float64'
    * complex
    * 'complex64'
    * 'complex128'
    * 'UInt8'
    * 'Int8'
    * 'UInt16'
    * 'Int16'
    * 'UInt32'
    * 'Int32'
    * 'UInt64'
    * 'Int64'
    * 'Float32'
    * 'Float64'
    """

ids: Incomplete
_: Incomplete

def any_skipna_inferred_dtype(request):
    """
    Fixture for all inferred dtypes from _libs.lib.infer_dtype

    The covered (inferred) types are:
    * 'string'
    * 'empty'
    * 'bytes'
    * 'mixed'
    * 'mixed-integer'
    * 'mixed-integer-float'
    * 'floating'
    * 'integer'
    * 'decimal'
    * 'boolean'
    * 'datetime64'
    * 'datetime'
    * 'date'
    * 'timedelta'
    * 'time'
    * 'period'
    * 'interval'

    Returns
    -------
    inferred_dtype : str
        The string for the inferred dtype from _libs.lib.infer_dtype
    values : np.ndarray
        An array of object dtype that will be inferred to have
        `inferred_dtype`

    Examples
    --------
    >>> from pandas._libs import lib
    >>>
    >>> def test_something(any_skipna_inferred_dtype):
    ...     inferred_dtype, values = any_skipna_inferred_dtype
    ...     # will pass
    ...     assert lib.infer_dtype(values, skipna=True) == inferred_dtype
    """
def ip():
    """
    Get an instance of IPython.InteractiveShell.

    Will raise a skip if IPython is not installed.
    """
def spmatrix(request):
    """
    Yields scipy sparse matrix classes.
    """
def tick_classes(request):
    """
    Fixture for Tick based datetime offsets available for a time series.
    """
def sort_by_key(request):
    """
    Simple fixture for testing keys in sorting methods.
    Tests None (no key) and the identity key.
    """
def fsspectest() -> Generator[Incomplete, None, None]: ...
def names(request) -> tuple[Hashable, Hashable, Hashable]:
    """
    A 3-tuple of names, the first two for operands, the last for a result.
    """
def indexer_sli(request):
    """
    Parametrize over __setitem__, loc.__setitem__, iloc.__setitem__
    """
def indexer_li(request):
    """
    Parametrize over loc.__getitem__, iloc.__getitem__
    """
def indexer_si(request):
    """
    Parametrize over __setitem__, iloc.__setitem__
    """
def indexer_sl(request):
    """
    Parametrize over __setitem__, loc.__setitem__
    """
def indexer_al(request):
    """
    Parametrize over at.__setitem__, loc.__setitem__
    """
def indexer_ial(request):
    """
    Parametrize over iat.__setitem__, iloc.__setitem__
    """
def using_array_manager() -> bool:
    """
    Fixture to check if the array manager is being used.
    """
def using_copy_on_write() -> bool:
    """
    Fixture to check if Copy-on-Write is enabled.
    """

warsaws: Incomplete

def warsaw(request) -> str:
    """
    tzinfo for Europe/Warsaw using pytz, dateutil, or zoneinfo.
    """
