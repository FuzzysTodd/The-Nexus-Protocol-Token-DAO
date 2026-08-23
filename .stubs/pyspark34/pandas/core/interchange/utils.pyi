from pandas._typing import DtypeObj as DtypeObj
from pandas.api.types import is_datetime64_dtype as is_datetime64_dtype

class ArrowCTypes:
    """
    Enum for Apache Arrow C type format strings.

    The Arrow C data interface:
    https://arrow.apache.org/docs/format/CDataInterface.html#data-type-description-format-strings
    """
    NULL: str
    BOOL: str
    INT8: str
    UINT8: str
    INT16: str
    UINT16: str
    INT32: str
    UINT32: str
    INT64: str
    UINT64: str
    FLOAT16: str
    FLOAT32: str
    FLOAT64: str
    STRING: str
    LARGE_STRING: str
    DATE32: str
    DATE64: str
    TIMESTAMP: str
    TIME: str

class Endianness:
    """Enum indicating the byte-order of a data-type."""
    LITTLE: str
    BIG: str
    NATIVE: str
    NA: str

def dtype_to_arrow_c_fmt(dtype: DtypeObj) -> str:
    """
    Represent pandas `dtype` as a format string in Apache Arrow C notation.

    Parameters
    ----------
    dtype : np.dtype
        Datatype of pandas DataFrame to represent.

    Returns
    -------
    str
        Format string in Apache Arrow C notation of the given `dtype`.
    """
