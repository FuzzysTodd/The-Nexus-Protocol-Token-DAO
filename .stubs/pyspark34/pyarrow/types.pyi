from pyarrow.lib import is_boolean_value as is_boolean_value, is_float_value as is_float_value, is_integer_value as is_integer_value

def is_null(t):
    """
    Return True if value is an instance of a null type.

    Parameters
    ----------
    t : DataType
    """
def is_boolean(t):
    """
    Return True if value is an instance of a boolean type.

    Parameters
    ----------
    t : DataType
    """
def is_integer(t):
    """
    Return True if value is an instance of any integer type.

    Parameters
    ----------
    t : DataType
    """
def is_signed_integer(t):
    """
    Return True if value is an instance of any signed integer type.

    Parameters
    ----------
    t : DataType
    """
def is_unsigned_integer(t):
    """
    Return True if value is an instance of any unsigned integer type.

    Parameters
    ----------
    t : DataType
    """
def is_int8(t):
    """
    Return True if value is an instance of an int8 type.

    Parameters
    ----------
    t : DataType
    """
def is_int16(t):
    """
    Return True if value is an instance of an int16 type.

    Parameters
    ----------
    t : DataType
    """
def is_int32(t):
    """
    Return True if value is an instance of an int32 type.

    Parameters
    ----------
    t : DataType
    """
def is_int64(t):
    """
    Return True if value is an instance of an int64 type.

    Parameters
    ----------
    t : DataType
    """
def is_uint8(t):
    """
    Return True if value is an instance of an uint8 type.

    Parameters
    ----------
    t : DataType
    """
def is_uint16(t):
    """
    Return True if value is an instance of an uint16 type.

    Parameters
    ----------
    t : DataType
    """
def is_uint32(t):
    """
    Return True if value is an instance of an uint32 type.

    Parameters
    ----------
    t : DataType
    """
def is_uint64(t):
    """
    Return True if value is an instance of an uint64 type.

    Parameters
    ----------
    t : DataType
    """
def is_floating(t):
    """
    Return True if value is an instance of a floating point numeric type.

    Parameters
    ----------
    t : DataType
    """
def is_float16(t):
    """
    Return True if value is an instance of a float16 (half-precision) type.

    Parameters
    ----------
    t : DataType
    """
def is_float32(t):
    """
    Return True if value is an instance of a float32 (single precision) type.

    Parameters
    ----------
    t : DataType
    """
def is_float64(t):
    """
    Return True if value is an instance of a float64 (double precision) type.

    Parameters
    ----------
    t : DataType
    """
def is_list(t):
    """
    Return True if value is an instance of a list type.

    Parameters
    ----------
    t : DataType
    """
def is_large_list(t):
    """
    Return True if value is an instance of a large list type.

    Parameters
    ----------
    t : DataType
    """
def is_fixed_size_list(t):
    """
    Return True if value is an instance of a fixed size list type.

    Parameters
    ----------
    t : DataType
    """
def is_struct(t):
    """
    Return True if value is an instance of a struct type.

    Parameters
    ----------
    t : DataType
    """
def is_union(t):
    """
    Return True if value is an instance of a union type.

    Parameters
    ----------
    t : DataType
    """
def is_nested(t):
    """
    Return True if value is an instance of a nested type.

    Parameters
    ----------
    t : DataType
    """
def is_run_end_encoded(t):
    """
    Return True if value is an instance of a run-end encoded type.

    Parameters
    ----------
    t : DataType
    """
def is_temporal(t):
    """
    Return True if value is an instance of date, time, timestamp or duration.

    Parameters
    ----------
    t : DataType
    """
def is_timestamp(t):
    """
    Return True if value is an instance of a timestamp type.

    Parameters
    ----------
    t : DataType
    """
def is_duration(t):
    """
    Return True if value is an instance of a duration type.

    Parameters
    ----------
    t : DataType
    """
def is_time(t):
    """
    Return True if value is an instance of a time type.

    Parameters
    ----------
    t : DataType
    """
def is_time32(t):
    """
    Return True if value is an instance of a time32 type.

    Parameters
    ----------
    t : DataType
    """
def is_time64(t):
    """
    Return True if value is an instance of a time64 type.

    Parameters
    ----------
    t : DataType
    """
def is_binary(t):
    """
    Return True if value is an instance of a variable-length binary type.

    Parameters
    ----------
    t : DataType
    """
def is_large_binary(t):
    """
    Return True if value is an instance of a large variable-length
    binary type.

    Parameters
    ----------
    t : DataType
    """
def is_unicode(t):
    """
    Alias for is_string.

    Parameters
    ----------
    t : DataType
    """
def is_string(t):
    """
    Return True if value is an instance of string (utf8 unicode) type.

    Parameters
    ----------
    t : DataType
    """
def is_large_unicode(t):
    """
    Alias for is_large_string.

    Parameters
    ----------
    t : DataType
    """
def is_large_string(t):
    """
    Return True if value is an instance of large string (utf8 unicode) type.

    Parameters
    ----------
    t : DataType
    """
def is_fixed_size_binary(t):
    """
    Return True if value is an instance of a fixed size binary type.

    Parameters
    ----------
    t : DataType
    """
def is_date(t):
    """
    Return True if value is an instance of a date type.

    Parameters
    ----------
    t : DataType
    """
def is_date32(t):
    """
    Return True if value is an instance of a date32 (days) type.

    Parameters
    ----------
    t : DataType
    """
def is_date64(t):
    """
    Return True if value is an instance of a date64 (milliseconds) type.

    Parameters
    ----------
    t : DataType
    """
def is_map(t):
    """
    Return True if value is an instance of a map logical type.

    Parameters
    ----------
    t : DataType
    """
def is_decimal(t):
    """
    Return True if value is an instance of a decimal type.

    Parameters
    ----------
    t : DataType
    """
def is_decimal128(t):
    """
    Return True if value is an instance of a decimal type.

    Parameters
    ----------
    t : DataType
    """
def is_decimal256(t):
    """
    Return True if value is an instance of a decimal type.

    Parameters
    ----------
    t : DataType
    """
def is_dictionary(t):
    """
    Return True if value is an instance of a dictionary-encoded type.

    Parameters
    ----------
    t : DataType
    """
def is_interval(t):
    """
    Return True if the value is an instance of an interval type.

    Parameters
    ----------
    t : DateType
    """
def is_primitive(t):
    """
    Return True if the value is an instance of a primitive type.

    Parameters
    ----------
    t : DataType
    """
