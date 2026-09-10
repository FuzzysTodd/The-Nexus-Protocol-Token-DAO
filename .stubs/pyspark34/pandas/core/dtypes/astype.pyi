from pandas._libs import lib as lib
from pandas._libs.tslibs.timedeltas import array_to_timedelta64 as array_to_timedelta64
from pandas._typing import ArrayLike as ArrayLike, DtypeObj as DtypeObj, IgnoreRaise as IgnoreRaise
from pandas.core.arrays import ExtensionArray as ExtensionArray
from pandas.core.dtypes.common import is_datetime64_dtype as is_datetime64_dtype, is_dtype_equal as is_dtype_equal, is_integer_dtype as is_integer_dtype, is_object_dtype as is_object_dtype, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import ExtensionDtype as ExtensionDtype, PandasDtype as PandasDtype
from pandas.errors import IntCastingNaNError as IntCastingNaNError

def astype_array(values: ArrayLike, dtype: DtypeObj, copy: bool = False) -> ArrayLike:
    """
    Cast array (ndarray or ExtensionArray) to the new dtype.

    Parameters
    ----------
    values : ndarray or ExtensionArray
    dtype : dtype object
    copy : bool, default False
        copy if indicated

    Returns
    -------
    ndarray or ExtensionArray
    """
def astype_array_safe(values: ArrayLike, dtype, copy: bool = False, errors: IgnoreRaise = 'raise') -> ArrayLike:
    """
    Cast array (ndarray or ExtensionArray) to the new dtype.

    This basically is the implementation for DataFrame/Series.astype and
    includes all custom logic for pandas (NaN-safety, converting str to object,
    not allowing )

    Parameters
    ----------
    values : ndarray or ExtensionArray
    dtype : str, dtype convertible
    copy : bool, default False
        copy if indicated
    errors : str, {'raise', 'ignore'}, default 'raise'
        - ``raise`` : allow exceptions to be raised
        - ``ignore`` : suppress exceptions. On error return original object

    Returns
    -------
    ndarray or ExtensionArray
    """
def astype_is_view(dtype: DtypeObj, new_dtype: DtypeObj) -> bool:
    """Checks if astype avoided copying the data.

    Parameters
    ----------
    dtype : Original dtype
    new_dtype : target dtype

    Returns
    -------
    True if new data is a view or not guaranteed to be a copy, False otherwise
    """
