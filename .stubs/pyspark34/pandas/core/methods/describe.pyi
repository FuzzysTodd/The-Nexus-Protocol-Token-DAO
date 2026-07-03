import abc
import numpy as np
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from pandas import DataFrame as DataFrame, Series as Series
from pandas._libs.tslibs import Timestamp as Timestamp
from pandas._typing import DtypeObj as DtypeObj, NDFrameT as NDFrameT, npt as npt
from pandas.core.arrays.arrow.dtype import ArrowDtype as ArrowDtype
from pandas.core.arrays.floating import Float64Dtype as Float64Dtype
from pandas.core.dtypes.common import is_bool_dtype as is_bool_dtype, is_complex_dtype as is_complex_dtype, is_extension_array_dtype as is_extension_array_dtype, is_numeric_dtype as is_numeric_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype
from pandas.core.reshape.concat import concat as concat
from pandas.io.formats.format import format_percentiles as format_percentiles
from pandas.util._validators import validate_percentile as validate_percentile
from typing import Any, Callable, Hashable, Sequence

def describe_ndframe(*, obj: NDFrameT, include: str | Sequence[str] | None, exclude: str | Sequence[str] | None, percentiles: Sequence[float] | np.ndarray | None) -> NDFrameT:
    """Describe series or dataframe.

    Called from pandas.core.generic.NDFrame.describe()

    Parameters
    ----------
    obj: DataFrame or Series
        Either dataframe or series to be described.
    include : 'all', list-like of dtypes or None (default), optional
        A white list of data types to include in the result. Ignored for ``Series``.
    exclude : list-like of dtypes or None (default), optional,
        A black list of data types to omit from the result. Ignored for ``Series``.
    percentiles : list-like of numbers, optional
        The percentiles to include in the output. All should fall between 0 and 1.
        The default is ``[.25, .5, .75]``, which returns the 25th, 50th, and
        75th percentiles.

    Returns
    -------
    Dataframe or series description.
    """

class NDFrameDescriberAbstract(ABC, metaclass=abc.ABCMeta):
    """Abstract class for describing dataframe or series.

    Parameters
    ----------
    obj : Series or DataFrame
        Object to be described.
    """
    obj: Incomplete
    def __init__(self, obj: DataFrame | Series) -> None: ...
    @abstractmethod
    def describe(self, percentiles: Sequence[float] | np.ndarray) -> DataFrame | Series:
        """Do describe either series or dataframe.

        Parameters
        ----------
        percentiles : list-like of numbers
            The percentiles to include in the output.
        """

class SeriesDescriber(NDFrameDescriberAbstract):
    """Class responsible for creating series description."""
    obj: Series
    def describe(self, percentiles: Sequence[float] | np.ndarray) -> Series: ...

class DataFrameDescriber(NDFrameDescriberAbstract):
    """Class responsible for creating dataobj description.

    Parameters
    ----------
    obj : DataFrame
        DataFrame to be described.
    include : 'all', list-like of dtypes or None
        A white list of data types to include in the result.
    exclude : list-like of dtypes or None
        A black list of data types to omit from the result.
    """
    include: Incomplete
    exclude: Incomplete
    def __init__(self, obj: DataFrame, *, include: str | Sequence[str] | None, exclude: str | Sequence[str] | None) -> None: ...
    def describe(self, percentiles: Sequence[float] | np.ndarray) -> DataFrame: ...

def reorder_columns(ldesc: Sequence[Series]) -> list[Hashable]:
    """Set a convenient order for rows for display."""
def describe_numeric_1d(series: Series, percentiles: Sequence[float]) -> Series:
    """Describe series containing numerical data.

    Parameters
    ----------
    series : Series
        Series to be described.
    percentiles : list-like of numbers
        The percentiles to include in the output.
    """
def describe_categorical_1d(data: Series, percentiles_ignored: Sequence[float]) -> Series:
    """Describe series containing categorical data.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles_ignored : list-like of numbers
        Ignored, but in place to unify interface.
    """
def describe_timestamp_as_categorical_1d(data: Series, percentiles_ignored: Sequence[float]) -> Series:
    """Describe series containing timestamp data treated as categorical.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles_ignored : list-like of numbers
        Ignored, but in place to unify interface.
    """
def describe_timestamp_1d(data: Series, percentiles: Sequence[float]) -> Series:
    """Describe series containing datetime64 dtype.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles : list-like of numbers
        The percentiles to include in the output.
    """
def select_describe_func(data: Series) -> Callable:
    """Select proper function for describing series based on data type.

    Parameters
    ----------
    data : Series
        Series to be described.
    """
def refine_percentiles(percentiles: Sequence[float] | np.ndarray | None) -> np.ndarray[Any, np.dtype[np.float64]]:
    """
    Ensure that percentiles are unique and sorted.

    Parameters
    ----------
    percentiles : list-like of numbers, optional
        The percentiles to include in the output.
    """
