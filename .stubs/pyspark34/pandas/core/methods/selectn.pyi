from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Series as Series
from pandas._typing import DtypeObj as DtypeObj, IndexLabel as IndexLabel
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_complex_dtype as is_complex_dtype, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.dtypes import BaseMaskedDtype as BaseMaskedDtype

class SelectN:
    obj: Incomplete
    n: Incomplete
    keep: Incomplete
    def __init__(self, obj, n: int, keep: str) -> None: ...
    def compute(self, method: str) -> DataFrame | Series: ...
    def nlargest(self): ...
    def nsmallest(self): ...
    @staticmethod
    def is_valid_dtype_n_method(dtype: DtypeObj) -> bool:
        """
        Helper function to determine if dtype is valid for
        nsmallest/nlargest methods
        """

class SelectNSeries(SelectN):
    """
    Implement n largest/smallest for Series

    Parameters
    ----------
    obj : Series
    n : int
    keep : {'first', 'last'}, default 'first'

    Returns
    -------
    nordered : Series
    """
    def compute(self, method: str) -> Series: ...

class SelectNFrame(SelectN):
    """
    Implement n largest/smallest for DataFrame

    Parameters
    ----------
    obj : DataFrame
    n : int
    keep : {'first', 'last'}, default 'first'
    columns : list or str

    Returns
    -------
    nordered : DataFrame
    """
    columns: Incomplete
    def __init__(self, obj: DataFrame, n: int, keep: str, columns: IndexLabel) -> None: ...
    def compute(self, method: str) -> DataFrame: ...
