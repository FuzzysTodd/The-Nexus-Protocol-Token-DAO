from pandas import DataFrame as DataFrame
from pandas._typing import DtypeObj as DtypeObj

def get_dtype(obj) -> DtypeObj: ...
def get_obj(df: DataFrame, klass):
    """
    For sharing tests using frame_or_series, either return the DataFrame
    unchanged or return it's first column as a Series.
    """
