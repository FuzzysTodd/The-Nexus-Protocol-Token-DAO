from _typeshed import Incomplete
from collections.abc import Generator
from pandas import Categorical, CategoricalIndex, DataFrame, DatetimeIndex, Index, IntervalIndex, PeriodIndex, RangeIndex, Series, TimedeltaIndex
from pandas._config.localization import can_set_locale as can_set_locale, get_locales as get_locales, set_locale as set_locale
from pandas._testing._io import close as close, network as network, round_trip_localpath as round_trip_localpath, round_trip_pathlib as round_trip_pathlib, round_trip_pickle as round_trip_pickle, write_to_compressed as write_to_compressed
from pandas._testing._random import rands as rands
from pandas._testing._warnings import assert_produces_warning as assert_produces_warning, maybe_produces_warning as maybe_produces_warning
from pandas._testing.asserters import assert_almost_equal as assert_almost_equal, assert_attr_equal as assert_attr_equal, assert_categorical_equal as assert_categorical_equal, assert_class_equal as assert_class_equal, assert_contains_all as assert_contains_all, assert_copy as assert_copy, assert_datetime_array_equal as assert_datetime_array_equal, assert_dict_equal as assert_dict_equal, assert_equal as assert_equal, assert_extension_array_equal as assert_extension_array_equal, assert_frame_equal as assert_frame_equal, assert_index_equal as assert_index_equal, assert_indexing_slices_equivalent as assert_indexing_slices_equivalent, assert_interval_array_equal as assert_interval_array_equal, assert_is_sorted as assert_is_sorted, assert_is_valid_plot_return_object as assert_is_valid_plot_return_object, assert_metadata_equivalent as assert_metadata_equivalent, assert_numpy_array_equal as assert_numpy_array_equal, assert_period_array_equal as assert_period_array_equal, assert_series_equal as assert_series_equal, assert_sp_array_equal as assert_sp_array_equal, assert_timedelta_array_equal as assert_timedelta_array_equal, raise_assert_detail as raise_assert_detail
from pandas._testing.compat import get_dtype as get_dtype, get_obj as get_obj
from pandas._testing.contexts import decompress_file as decompress_file, ensure_clean as ensure_clean, ensure_safe_environment_variables as ensure_safe_environment_variables, raises_chained_assignment_error as raises_chained_assignment_error, set_timezone as set_timezone, use_numexpr as use_numexpr, with_csv_dialect as with_csv_dialect
from pandas._typing import Dtype, Frequency, NpDtype
from typing import Callable, ContextManager, Iterable

__all__ = ['ALL_INT_EA_DTYPES', 'ALL_INT_NUMPY_DTYPES', 'ALL_NUMPY_DTYPES', 'ALL_REAL_NUMPY_DTYPES', 'all_timeseries_index_generator', 'assert_almost_equal', 'assert_attr_equal', 'assert_categorical_equal', 'assert_class_equal', 'assert_contains_all', 'assert_copy', 'assert_datetime_array_equal', 'assert_dict_equal', 'assert_equal', 'assert_extension_array_equal', 'assert_frame_equal', 'assert_index_equal', 'assert_indexing_slices_equivalent', 'assert_interval_array_equal', 'assert_is_sorted', 'assert_is_valid_plot_return_object', 'assert_metadata_equivalent', 'assert_numpy_array_equal', 'assert_period_array_equal', 'assert_produces_warning', 'assert_series_equal', 'assert_sp_array_equal', 'assert_timedelta_array_equal', 'at', 'BOOL_DTYPES', 'box_expected', 'BYTES_DTYPES', 'can_set_locale', 'close', 'COMPLEX_DTYPES', 'convert_rows_list_to_csv_str', 'DATETIME64_DTYPES', 'decompress_file', 'EMPTY_STRING_PATTERN', 'ENDIAN', 'ensure_clean', 'ensure_safe_environment_variables', 'equalContents', 'external_error_raised', 'FLOAT_EA_DTYPES', 'FLOAT_NUMPY_DTYPES', 'getCols', 'get_cython_table_params', 'get_dtype', 'getitem', 'get_locales', 'getMixedTypeDict', 'get_obj', 'get_op_from_name', 'getPeriodData', 'getSeriesData', 'getTimeSeriesData', 'iat', 'iloc', 'index_subclass_makers_generator', 'loc', 'makeBoolIndex', 'makeCategoricalIndex', 'makeCustomDataframe', 'makeCustomIndex', 'makeDataFrame', 'makeDateIndex', 'makeFloatIndex', 'makeFloatSeries', 'makeIntervalIndex', 'makeIntIndex', 'makeMissingDataframe', 'makeMixedDataFrame', 'makeMultiIndex', 'makeNumericIndex', 'makeObjectSeries', 'makePeriodFrame', 'makePeriodIndex', 'makePeriodSeries', 'make_rand_series', 'makeRangeIndex', 'makeStringIndex', 'makeStringSeries', 'makeTimeDataFrame', 'makeTimedeltaIndex', 'makeTimeSeries', 'makeUIntIndex', 'maybe_produces_warning', 'NARROW_NP_DTYPES', 'network', 'NP_NAT_OBJECTS', 'NULL_OBJECTS', 'OBJECT_DTYPES', 'raise_assert_detail', 'rands', 'reset_display_options', 'raises_chained_assignment_error', 'round_trip_localpath', 'round_trip_pathlib', 'round_trip_pickle', 'setitem', 'set_locale', 'set_timezone', 'shares_memory', 'SIGNED_INT_EA_DTYPES', 'SIGNED_INT_NUMPY_DTYPES', 'STRING_DTYPES', 'SubclassedCategorical', 'SubclassedDataFrame', 'SubclassedSeries', 'TIMEDELTA64_DTYPES', 'to_array', 'UNSIGNED_INT_EA_DTYPES', 'UNSIGNED_INT_NUMPY_DTYPES', 'use_numexpr', 'with_csv_dialect', 'write_to_compressed']

UNSIGNED_INT_NUMPY_DTYPES: list[NpDtype]
UNSIGNED_INT_EA_DTYPES: list[Dtype]
SIGNED_INT_NUMPY_DTYPES: list[NpDtype]
SIGNED_INT_EA_DTYPES: list[Dtype]
ALL_INT_NUMPY_DTYPES: Incomplete
ALL_INT_EA_DTYPES: Incomplete
FLOAT_NUMPY_DTYPES: list[NpDtype]
FLOAT_EA_DTYPES: list[Dtype]
COMPLEX_DTYPES: list[Dtype]
STRING_DTYPES: list[Dtype]
DATETIME64_DTYPES: list[Dtype]
TIMEDELTA64_DTYPES: list[Dtype]
BOOL_DTYPES: list[Dtype]
BYTES_DTYPES: list[Dtype]
OBJECT_DTYPES: list[Dtype]
ALL_REAL_NUMPY_DTYPES: Incomplete
ALL_NUMPY_DTYPES: Incomplete
NARROW_NP_DTYPES: Incomplete
ENDIAN: Incomplete
NULL_OBJECTS: Incomplete
NP_NAT_OBJECTS: Incomplete
EMPTY_STRING_PATTERN: Incomplete

def reset_display_options() -> None:
    """
    Reset the display options for printing and representing objects.
    """
def equalContents(arr1, arr2) -> bool:
    """
    Checks if the set of unique elements of arr1 and arr2 are equivalent.
    """
def box_expected(expected, box_cls, transpose: bool = True):
    """
    Helper function to wrap the expected output of a test in a given box_class.

    Parameters
    ----------
    expected : np.ndarray, Index, Series
    box_cls : {Index, Series, DataFrame}

    Returns
    -------
    subclass of box_cls
    """
def to_array(obj):
    """
    Similar to pd.array, but does not cast numpy dtypes to nullable dtypes.
    """
def getCols(k) -> str: ...
def makeStringIndex(k: int = 10, name: Incomplete | None = None) -> Index: ...
def makeCategoricalIndex(k: int = 10, n: int = 3, name: Incomplete | None = None, **kwargs) -> CategoricalIndex:
    """make a length k index or n categories"""
def makeIntervalIndex(k: int = 10, name: Incomplete | None = None, **kwargs) -> IntervalIndex:
    """make a length k IntervalIndex"""
def makeBoolIndex(k: int = 10, name: Incomplete | None = None) -> Index: ...
def makeNumericIndex(k: int = 10, *, name: Incomplete | None = None, dtype: Dtype | None) -> Index: ...
def makeIntIndex(k: int = 10, *, name: Incomplete | None = None, dtype: Dtype = 'int64') -> Index: ...
def makeUIntIndex(k: int = 10, *, name: Incomplete | None = None, dtype: Dtype = 'uint64') -> Index: ...
def makeRangeIndex(k: int = 10, name: Incomplete | None = None, **kwargs) -> RangeIndex: ...
def makeFloatIndex(k: int = 10, *, name: Incomplete | None = None, dtype: Dtype = 'float64') -> Index: ...
def makeDateIndex(k: int = 10, freq: Frequency = 'B', name: Incomplete | None = None, **kwargs) -> DatetimeIndex: ...
def makeTimedeltaIndex(k: int = 10, freq: Frequency = 'D', name: Incomplete | None = None, **kwargs) -> TimedeltaIndex: ...
def makePeriodIndex(k: int = 10, name: Incomplete | None = None, **kwargs) -> PeriodIndex: ...
def makeMultiIndex(k: int = 10, names: Incomplete | None = None, **kwargs): ...
def index_subclass_makers_generator() -> Generator[Incomplete, Incomplete, None]: ...
def all_timeseries_index_generator(k: int = 10) -> Iterable[Index]:
    """
    Generator which can be iterated over to get instances of all the classes
    which represent time-series.

    Parameters
    ----------
    k: length of each of the index instances
    """
def make_rand_series(name: Incomplete | None = None, dtype=...) -> Series: ...
def makeFloatSeries(name: Incomplete | None = None) -> Series: ...
def makeStringSeries(name: Incomplete | None = None) -> Series: ...
def makeObjectSeries(name: Incomplete | None = None) -> Series: ...
def getSeriesData() -> dict[str, Series]: ...
def makeTimeSeries(nper: Incomplete | None = None, freq: Frequency = 'B', name: Incomplete | None = None) -> Series: ...
def makePeriodSeries(nper: Incomplete | None = None, name: Incomplete | None = None) -> Series: ...
def getTimeSeriesData(nper: Incomplete | None = None, freq: Frequency = 'B') -> dict[str, Series]: ...
def getPeriodData(nper: Incomplete | None = None) -> dict[str, Series]: ...
def makeTimeDataFrame(nper: Incomplete | None = None, freq: Frequency = 'B') -> DataFrame: ...
def makeDataFrame() -> DataFrame: ...
def getMixedTypeDict(): ...
def makeMixedDataFrame() -> DataFrame: ...
def makePeriodFrame(nper: Incomplete | None = None) -> DataFrame: ...
def makeCustomIndex(nentries, nlevels, prefix: str = '#', names: bool | str | list[str] | None = False, ndupe_l: Incomplete | None = None, idx_type: Incomplete | None = None) -> Index:
    '''
    Create an index/multindex with given dimensions, levels, names, etc\'

    nentries - number of entries in index
    nlevels - number of levels (> 1 produces multindex)
    prefix - a string prefix for labels
    names - (Optional), bool or list of strings. if True will use default
       names, if false will use no names, if a list is given, the name of
       each level in the index will be taken from the list.
    ndupe_l - (Optional), list of ints, the number of rows for which the
       label will repeated at the corresponding level, you can specify just
       the first few, the rest will use the default ndupe_l of 1.
       len(ndupe_l) <= nlevels.
    idx_type - "i"/"f"/"s"/"dt"/"p"/"td".
       If idx_type is not None, `idx_nlevels` must be 1.
       "i"/"f" creates an integer/float index,
       "s" creates a string
       "dt" create a datetime index.
       "td" create a datetime index.

        if unspecified, string labels will be generated.
    '''
def makeCustomDataframe(nrows, ncols, c_idx_names: bool | list[str] = True, r_idx_names: bool | list[str] = True, c_idx_nlevels: int = 1, r_idx_nlevels: int = 1, data_gen_f: Incomplete | None = None, c_ndupe_l: Incomplete | None = None, r_ndupe_l: Incomplete | None = None, dtype: Incomplete | None = None, c_idx_type: Incomplete | None = None, r_idx_type: Incomplete | None = None) -> DataFrame:
    '''
    Create a DataFrame using supplied parameters.

    Parameters
    ----------
    nrows,  ncols - number of data rows/cols
    c_idx_names, r_idx_names  - False/True/list of strings,  yields No names ,
            default names or uses the provided names for the levels of the
            corresponding index. You can provide a single string when
            c_idx_nlevels ==1.
    c_idx_nlevels - number of levels in columns index. > 1 will yield MultiIndex
    r_idx_nlevels - number of levels in rows index. > 1 will yield MultiIndex
    data_gen_f - a function f(row,col) which return the data value
            at that position, the default generator used yields values of the form
            "RxCy" based on position.
    c_ndupe_l, r_ndupe_l - list of integers, determines the number
            of duplicates for each label at a given level of the corresponding
            index. The default `None` value produces a multiplicity of 1 across
            all levels, i.e. a unique index. Will accept a partial list of length
            N < idx_nlevels, for just the first N levels. If ndupe doesn\'t divide
            nrows/ncol, the last label might have lower multiplicity.
    dtype - passed to the DataFrame constructor as is, in case you wish to
            have more control in conjunction with a custom `data_gen_f`
    r_idx_type, c_idx_type -  "i"/"f"/"s"/"dt"/"td".
        If idx_type is not None, `idx_nlevels` must be 1.
        "i"/"f" creates an integer/float index,
        "s" creates a string index
        "dt" create a datetime index.
        "td" create a timedelta index.

            if unspecified, string labels will be generated.

    Examples
    --------
    # 5 row, 3 columns, default names on both, single index on both axis
    >> makeCustomDataframe(5,3)

    # make the data a random int between 1 and 100
    >> mkdf(5,3,data_gen_f=lambda r,c:randint(1,100))

    # 2-level multiindex on rows with each label duplicated
    # twice on first level, default names on both axis, single
    # index on both axis
    >> a=makeCustomDataframe(5,3,r_idx_nlevels=2,r_ndupe_l=[2])

    # DatetimeIndex on row, index with unicode labels on columns
    # no names on either axis
    >> a=makeCustomDataframe(5,3,c_idx_names=False,r_idx_names=False,
                             r_idx_type="dt",c_idx_type="u")

    # 4-level multindex on rows with names provided, 2-level multindex
    # on columns with default labels and default names.
    >> a=makeCustomDataframe(5,3,r_idx_nlevels=4,
                             r_idx_names=["FEE","FIH","FOH","FUM"],
                             c_idx_nlevels=2)

    >> a=mkdf(5,3,r_idx_nlevels=2,c_idx_nlevels=4)
    '''
def makeMissingDataframe(density: float = 0.9, random_state: Incomplete | None = None) -> DataFrame: ...

class SubclassedSeries(Series): ...
class SubclassedDataFrame(DataFrame): ...
class SubclassedCategorical(Categorical): ...

def convert_rows_list_to_csv_str(rows_list: list[str]) -> str:
    """
    Convert list of CSV rows to single CSV-formatted string for current OS.

    This method is used for creating expected value of to_csv() method.

    Parameters
    ----------
    rows_list : List[str]
        Each element represents the row of csv.

    Returns
    -------
    str
        Expected output of to_csv() in current OS.
    """
def external_error_raised(expected_exception: type[Exception]) -> ContextManager:
    """
    Helper function to mark pytest.raises that have an external error message.

    Parameters
    ----------
    expected_exception : Exception
        Expected error to raise.

    Returns
    -------
    Callable
        Regular `pytest.raises` function with `match` equal to `None`.
    """
def get_cython_table_params(ndframe, func_names_and_expected):
    """
    Combine frame, functions from com._cython_table
    keys and expected result.

    Parameters
    ----------
    ndframe : DataFrame or Series
    func_names_and_expected : Sequence of two items
        The first item is a name of a NDFrame method ('sum', 'prod') etc.
        The second item is the expected return value.

    Returns
    -------
    list
        List of three items (DataFrame, function, expected result)
    """
def get_op_from_name(op_name: str) -> Callable:
    '''
    The operator function for a given op name.

    Parameters
    ----------
    op_name : str
        The op name, in form of "add" or "__add__".

    Returns
    -------
    function
        A function performing the operation.
    '''
def getitem(x): ...
def setitem(x): ...
def loc(x): ...
def iloc(x): ...
def at(x): ...
def iat(x): ...
def shares_memory(left, right) -> bool:
    """
    Pandas-compat for np.shares_memory.
    """
