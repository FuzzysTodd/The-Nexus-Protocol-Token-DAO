from pandas._libs.lib import item_from_zerodim as item_from_zerodim
from pandas._libs.missing import is_matching_na as is_matching_na
from pandas._typing import F as F
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndex as ABCIndex, ABCSeries as ABCSeries
from typing import Callable

def unpack_zerodim_and_defer(name: str) -> Callable[[F], F]:
    """
    Boilerplate for pandas conventions in arithmetic and comparison methods.

    Parameters
    ----------
    name : str

    Returns
    -------
    decorator
    """
def get_op_result_name(left, right):
    """
    Find the appropriate name to pin to an operation result.  This result
    should always be either an Index or a Series.

    Parameters
    ----------
    left : {Series, Index}
    right : object

    Returns
    -------
    name : object
        Usually a string
    """
