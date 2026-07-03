from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCSeries as ABCSeries
from pandas.core.ops import roperator as roperator

def add_flex_arithmetic_methods(cls) -> None:
    """
    Adds the full suite of flex arithmetic methods (``pow``, ``mul``, ``add``)
    to the class.

    Parameters
    ----------
    cls : class
        flex methods will be defined and pinned to this class
    """
