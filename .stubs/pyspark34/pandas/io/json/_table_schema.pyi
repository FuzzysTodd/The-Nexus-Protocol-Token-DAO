from pandas import DataFrame as DataFrame, Series as Series
from pandas._libs.json import loads as loads
from pandas._libs.tslibs import timezones as timezones
from pandas._typing import DtypeObj as DtypeObj, JSONSerializable as JSONSerializable
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_extension_array_dtype as is_extension_array_dtype, is_integer_dtype as is_integer_dtype, is_numeric_dtype as is_numeric_dtype, is_period_dtype as is_period_dtype, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
from pandas.core.indexes.multi import MultiIndex as MultiIndex
from pandas.util._exceptions import find_stack_level as find_stack_level

TABLE_SCHEMA_VERSION: str

def as_json_table_type(x: DtypeObj) -> str:
    """
    Convert a NumPy / pandas type to its corresponding json_table.

    Parameters
    ----------
    x : np.dtype or ExtensionDtype

    Returns
    -------
    str
        the Table Schema data types

    Notes
    -----
    This table shows the relationship between NumPy / pandas dtypes,
    and Table Schema dtypes.

    ==============  =================
    Pandas type     Table Schema type
    ==============  =================
    int64           integer
    float64         number
    bool            boolean
    datetime64[ns]  datetime
    timedelta64[ns] duration
    object          str
    categorical     any
    =============== =================
    """
def set_default_names(data):
    """Sets index names to 'index' for regular, or 'level_x' for Multi"""
def convert_pandas_type_to_json_field(arr) -> dict[str, JSONSerializable]: ...
def convert_json_field_to_pandas_type(field) -> str | CategoricalDtype:
    '''
    Converts a JSON field descriptor into its corresponding NumPy / pandas type

    Parameters
    ----------
    field
        A JSON field descriptor

    Returns
    -------
    dtype

    Raises
    ------
    ValueError
        If the type of the provided field is unknown or currently unsupported

    Examples
    --------
    >>> convert_json_field_to_pandas_type({"name": "an_int", "type": "integer"})
    \'int64\'

    >>> convert_json_field_to_pandas_type(
    ...     {
    ...         "name": "a_categorical",
    ...         "type": "any",
    ...         "constraints": {"enum": ["a", "b", "c"]},
    ...         "ordered": True,
    ...     }
    ... )
    CategoricalDtype(categories=[\'a\', \'b\', \'c\'], ordered=True)

    >>> convert_json_field_to_pandas_type({"name": "a_datetime", "type": "datetime"})
    \'datetime64[ns]\'

    >>> convert_json_field_to_pandas_type(
    ...     {"name": "a_datetime_with_tz", "type": "datetime", "tz": "US/Central"}
    ... )
    \'datetime64[ns, US/Central]\'
    '''
def build_table_schema(data: DataFrame | Series, index: bool = True, primary_key: bool | None = None, version: bool = True) -> dict[str, JSONSerializable]:
    """
    Create a Table schema from ``data``.

    Parameters
    ----------
    data : Series, DataFrame
    index : bool, default True
        Whether to include ``data.index`` in the schema.
    primary_key : bool or None, default True
        Column names to designate as the primary key.
        The default `None` will set `'primaryKey'` to the index
        level or levels if the index is unique.
    version : bool, default True
        Whether to include a field `pandas_version` with the version
        of pandas that last revised the table schema. This version
        can be different from the installed pandas version.

    Returns
    -------
    dict

    Notes
    -----
    See `Table Schema
    <https://pandas.pydata.org/docs/user_guide/io.html#table-schema>`__ for
    conversion types.
    Timedeltas as converted to ISO8601 duration format with
    9 decimal places after the seconds field for nanosecond precision.

    Categoricals are converted to the `any` dtype, and use the `enum` field
    constraint to list the allowed values. The `ordered` attribute is included
    in an `ordered` field.

    Examples
    --------
    >>> from pandas.io.json._table_schema import build_table_schema
    >>> df = pd.DataFrame(
    ...     {'A': [1, 2, 3],
    ...      'B': ['a', 'b', 'c'],
    ...      'C': pd.date_range('2016-01-01', freq='d', periods=3),
    ...     }, index=pd.Index(range(3), name='idx'))
    >>> build_table_schema(df)
    {'fields': [{'name': 'idx', 'type': 'integer'}, {'name': 'A', 'type': 'integer'}, {'name': 'B', 'type': 'string'}, {'name': 'C', 'type': 'datetime'}], 'primaryKey': ['idx'], 'pandas_version': '1.4.0'}
    """
def parse_table_schema(json, precise_float):
    """
    Builds a DataFrame from a given schema

    Parameters
    ----------
    json :
        A JSON table schema
    precise_float : bool
        Flag controlling precision when decoding string to double values, as
        dictated by ``read_json``

    Returns
    -------
    df : DataFrame

    Raises
    ------
    NotImplementedError
        If the JSON table schema contains either timezone or timedelta data

    Notes
    -----
        Because :func:`DataFrame.to_json` uses the string 'index' to denote a
        name-less :class:`Index`, this function sets the name of the returned
        :class:`DataFrame` to ``None`` when said string is encountered with a
        normal :class:`Index`. For a :class:`MultiIndex`, the same limitation
        applies to any strings beginning with 'level_'. Therefore, an
        :class:`Index` name of 'index'  and :class:`MultiIndex` names starting
        with 'level_' are not supported.

    See Also
    --------
    build_table_schema : Inverse function.
    pandas.read_json
    """
