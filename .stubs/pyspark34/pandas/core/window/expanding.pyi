from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Series as Series
from pandas._typing import Axis as Axis, QuantileInterpolation as QuantileInterpolation, WindowingRankType as WindowingRankType
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.indexers.objects import BaseIndexer as BaseIndexer, ExpandingIndexer as ExpandingIndexer, GroupbyIndexer as GroupbyIndexer
from pandas.core.window.doc import create_section_header as create_section_header, kwargs_numeric_only as kwargs_numeric_only, numba_notes as numba_notes, template_header as template_header, template_returns as template_returns, template_see_also as template_see_also, window_agg_numba_parameters as window_agg_numba_parameters, window_apply_parameters as window_apply_parameters
from pandas.core.window.rolling import BaseWindowGroupby as BaseWindowGroupby, RollingAndExpandingMixin as RollingAndExpandingMixin
from pandas.util._decorators import doc as doc
from typing import Any, Callable

class Expanding(RollingAndExpandingMixin):
    '''
    Provide expanding window calculations.

    Parameters
    ----------
    min_periods : int, default 1
        Minimum number of observations in window required to have a value;
        otherwise, result is ``np.nan``.

    axis : int or str, default 0
        If ``0`` or ``\'index\'``, roll across the rows.

        If ``1`` or ``\'columns\'``, roll across the columns.

        For `Series` this parameter is unused and defaults to 0.

    method : str {\'single\', \'table\'}, default \'single\'
        Execute the rolling operation per single column or row (``\'single\'``)
        or over the entire object (``\'table\'``).

        This argument is only implemented when specifying ``engine=\'numba\'``
        in the method call.

        .. versionadded:: 1.3.0

    Returns
    -------
    ``Expanding`` subclass

    See Also
    --------
    rolling : Provides rolling window calculations.
    ewm : Provides exponential weighted functions.

    Notes
    -----
    See :ref:`Windowing Operations <window.expanding>` for further usage details
    and examples.

    Examples
    --------
    >>> df = pd.DataFrame({"B": [0, 1, 2, np.nan, 4]})
    >>> df
         B
    0  0.0
    1  1.0
    2  2.0
    3  NaN
    4  4.0

    **min_periods**

    Expanding sum with 1 vs 3 observations needed to calculate a value.

    >>> df.expanding(1).sum()
         B
    0  0.0
    1  1.0
    2  3.0
    3  3.0
    4  7.0
    >>> df.expanding(3).sum()
         B
    0  NaN
    1  NaN
    2  3.0
    3  3.0
    4  7.0
    '''
    def __init__(self, obj: NDFrame, min_periods: int = 1, axis: Axis = 0, method: str = 'single', selection: Incomplete | None = None) -> None: ...
    def aggregate(self, func, *args, **kwargs): ...
    agg = aggregate
    def count(self, numeric_only: bool = False): ...
    def apply(self, func: Callable[..., Any], raw: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None, args: tuple[Any, ...] | None = None, kwargs: dict[str, Any] | None = None): ...
    def sum(self, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def max(self, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def min(self, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def mean(self, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def median(self, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def std(self, ddof: int = 1, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def var(self, ddof: int = 1, numeric_only: bool = False, engine: str | None = None, engine_kwargs: dict[str, bool] | None = None): ...
    def sem(self, ddof: int = 1, numeric_only: bool = False): ...
    def skew(self, numeric_only: bool = False): ...
    def kurt(self, numeric_only: bool = False): ...
    def quantile(self, quantile: float, interpolation: QuantileInterpolation = 'linear', numeric_only: bool = False): ...
    def rank(self, method: WindowingRankType = 'average', ascending: bool = True, pct: bool = False, numeric_only: bool = False): ...
    def cov(self, other: DataFrame | Series | None = None, pairwise: bool | None = None, ddof: int = 1, numeric_only: bool = False): ...
    def corr(self, other: DataFrame | Series | None = None, pairwise: bool | None = None, ddof: int = 1, numeric_only: bool = False): ...

class ExpandingGroupby(BaseWindowGroupby, Expanding):
    """
    Provide a expanding groupby implementation.
    """
