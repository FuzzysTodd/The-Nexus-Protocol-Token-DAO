import numpy as np
from _typeshed import Incomplete
from pandas import DataFrame as DataFrame, Series as Series
from pandas._libs.tslibs import Timedelta as Timedelta
from pandas._typing import Axis as Axis, TimedeltaConvertibleTypes as TimedeltaConvertibleTypes
from pandas.core import common as common
from pandas.core.dtypes.common import is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_numeric_dtype as is_numeric_dtype
from pandas.core.dtypes.missing import isna as isna
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.indexers.objects import BaseIndexer as BaseIndexer, ExponentialMovingWindowIndexer as ExponentialMovingWindowIndexer, GroupbyIndexer as GroupbyIndexer
from pandas.core.util.numba_ import get_jit_arguments as get_jit_arguments, maybe_use_numba as maybe_use_numba
from pandas.core.window.common import zsqrt as zsqrt
from pandas.core.window.doc import create_section_header as create_section_header, kwargs_numeric_only as kwargs_numeric_only, numba_notes as numba_notes, template_header as template_header, template_returns as template_returns, template_see_also as template_see_also, window_agg_numba_parameters as window_agg_numba_parameters
from pandas.core.window.numba_ import generate_numba_ewm_func as generate_numba_ewm_func, generate_numba_ewm_table_func as generate_numba_ewm_table_func
from pandas.core.window.online import EWMMeanState as EWMMeanState, generate_online_numba_ewma_func as generate_online_numba_ewma_func
from pandas.core.window.rolling import BaseWindow as BaseWindow, BaseWindowGroupby as BaseWindowGroupby
from pandas.util._decorators import doc as doc

def get_center_of_mass(comass: float | None, span: float | None, halflife: float | None, alpha: float | None) -> float: ...

class ExponentialMovingWindow(BaseWindow):
    """
    Provide exponentially weighted (EW) calculations.

    Exactly one of ``com``, ``span``, ``halflife``, or ``alpha`` must be
    provided if ``times`` is not provided. If ``times`` is provided,
    ``halflife`` and one of ``com``, ``span`` or ``alpha`` may be provided.

    Parameters
    ----------
    com : float, optional
        Specify decay in terms of center of mass

        :math:`\\alpha = 1 / (1 + com)`, for :math:`com \\geq 0`.

    span : float, optional
        Specify decay in terms of span

        :math:`\\alpha = 2 / (span + 1)`, for :math:`span \\geq 1`.

    halflife : float, str, timedelta, optional
        Specify decay in terms of half-life

        :math:`\\alpha = 1 - \\exp\\left(-\\ln(2) / halflife\\right)`, for
        :math:`halflife > 0`.

        If ``times`` is specified, a timedelta convertible unit over which an
        observation decays to half its value. Only applicable to ``mean()``,
        and halflife value will not apply to the other functions.

        .. versionadded:: 1.1.0

    alpha : float, optional
        Specify smoothing factor :math:`\\alpha` directly

        :math:`0 < \\alpha \\leq 1`.

    min_periods : int, default 0
        Minimum number of observations in window required to have a value;
        otherwise, result is ``np.nan``.

    adjust : bool, default True
        Divide by decaying adjustment factor in beginning periods to account
        for imbalance in relative weightings (viewing EWMA as a moving average).

        - When ``adjust=True`` (default), the EW function is calculated using weights
          :math:`w_i = (1 - \\alpha)^i`. For example, the EW moving average of the series
          [:math:`x_0, x_1, ..., x_t`] would be:

        .. math::
            y_t = \\frac{x_t + (1 - \\alpha)x_{t-1} + (1 - \\alpha)^2 x_{t-2} + ... + (1 -
            \\alpha)^t x_0}{1 + (1 - \\alpha) + (1 - \\alpha)^2 + ... + (1 - \\alpha)^t}

        - When ``adjust=False``, the exponentially weighted function is calculated
          recursively:

        .. math::
            \\begin{split}
                y_0 &= x_0\\\\\n                y_t &= (1 - \\alpha) y_{t-1} + \\alpha x_t,
            \\end{split}
    ignore_na : bool, default False
        Ignore missing values when calculating weights.

        - When ``ignore_na=False`` (default), weights are based on absolute positions.
          For example, the weights of :math:`x_0` and :math:`x_2` used in calculating
          the final weighted average of [:math:`x_0`, None, :math:`x_2`] are
          :math:`(1-\\alpha)^2` and :math:`1` if ``adjust=True``, and
          :math:`(1-\\alpha)^2` and :math:`\\alpha` if ``adjust=False``.

        - When ``ignore_na=True``, weights are based
          on relative positions. For example, the weights of :math:`x_0` and :math:`x_2`
          used in calculating the final weighted average of
          [:math:`x_0`, None, :math:`x_2`] are :math:`1-\\alpha` and :math:`1` if
          ``adjust=True``, and :math:`1-\\alpha` and :math:`\\alpha` if ``adjust=False``.

    axis : {0, 1}, default 0
        If ``0`` or ``'index'``, calculate across the rows.

        If ``1`` or ``'columns'``, calculate across the columns.

        For `Series` this parameter is unused and defaults to 0.

    times : np.ndarray, Series, default None

        .. versionadded:: 1.1.0

        Only applicable to ``mean()``.

        Times corresponding to the observations. Must be monotonically increasing and
        ``datetime64[ns]`` dtype.

        If 1-D array like, a sequence with the same shape as the observations.

    method : str {'single', 'table'}, default 'single'
        .. versionadded:: 1.4.0

        Execute the rolling operation per single column or row (``'single'``)
        or over the entire object (``'table'``).

        This argument is only implemented when specifying ``engine='numba'``
        in the method call.

        Only applicable to ``mean()``

    Returns
    -------
    ``ExponentialMovingWindow`` subclass

    See Also
    --------
    rolling : Provides rolling window calculations.
    expanding : Provides expanding transformations.

    Notes
    -----
    See :ref:`Windowing Operations <window.exponentially_weighted>`
    for further usage details and examples.

    Examples
    --------
    >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
    >>> df
         B
    0  0.0
    1  1.0
    2  2.0
    3  NaN
    4  4.0

    >>> df.ewm(com=0.5).mean()
              B
    0  0.000000
    1  0.750000
    2  1.615385
    3  1.615385
    4  3.670213
    >>> df.ewm(alpha=2 / 3).mean()
              B
    0  0.000000
    1  0.750000
    2  1.615385
    3  1.615385
    4  3.670213

    **adjust**

    >>> df.ewm(com=0.5, adjust=True).mean()
              B
    0  0.000000
    1  0.750000
    2  1.615385
    3  1.615385
    4  3.670213
    >>> df.ewm(com=0.5, adjust=False).mean()
              B
    0  0.000000
    1  0.666667
    2  1.555556
    3  1.555556
    4  3.650794

    **ignore_na**

    >>> df.ewm(com=0.5, ignore_na=True).mean()
              B
    0  0.000000
    1  0.750000
    2  1.615385
    3  1.615385
    4  3.225000
    >>> df.ewm(com=0.5, ignore_na=False).mean()
              B
    0  0.000000
    1  0.750000
    2  1.615385
    3  1.615385
    4  3.670213

    **times**

    Exponentially weighted mean with weights calculated with a timedelta ``halflife``
    relative to ``times``.

    >>> times = ['2020-01-01', '2020-01-03', '2020-01-10', '2020-01-15', '2020-01-17']
    >>> df.ewm(halflife='4 days', times=pd.DatetimeIndex(times)).mean()
              B
    0  0.000000
    1  0.585786
    2  1.523889
    3  1.523889
    4  3.233686
    """
    com: Incomplete
    span: Incomplete
    halflife: Incomplete
    alpha: Incomplete
    adjust: Incomplete
    ignore_na: Incomplete
    times: Incomplete
    def __init__(self, obj: NDFrame, com: float | None = None, span: float | None = None, halflife: float | TimedeltaConvertibleTypes | None = None, alpha: float | None = None, min_periods: int | None = 0, adjust: bool = True, ignore_na: bool = False, axis: Axis = 0, times: np.ndarray | NDFrame | None = None, method: str = 'single', *, selection: Incomplete | None = None) -> None: ...
    def online(self, engine: str = 'numba', engine_kwargs: Incomplete | None = None) -> OnlineExponentialMovingWindow:
        """
        Return an ``OnlineExponentialMovingWindow`` object to calculate
        exponentially moving window aggregations in an online method.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        engine: str, default ``'numba'``
            Execution engine to calculate online aggregations.
            Applies to all supported aggregation methods.

        engine_kwargs : dict, default None
            Applies to all supported aggregation methods.

            * For ``'numba'`` engine, the engine can accept ``nopython``, ``nogil``
              and ``parallel`` dictionary keys. The values must either be ``True`` or
              ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is
              ``{{'nopython': True, 'nogil': False, 'parallel': False}}`` and will be
              applied to the function

        Returns
        -------
        OnlineExponentialMovingWindow
        """
    def aggregate(self, func, *args, **kwargs): ...
    agg = aggregate
    def mean(self, numeric_only: bool = False, engine: Incomplete | None = None, engine_kwargs: Incomplete | None = None): ...
    def sum(self, numeric_only: bool = False, engine: Incomplete | None = None, engine_kwargs: Incomplete | None = None): ...
    def std(self, bias: bool = False, numeric_only: bool = False): ...
    def var(self, bias: bool = False, numeric_only: bool = False): ...
    def cov(self, other: DataFrame | Series | None = None, pairwise: bool | None = None, bias: bool = False, numeric_only: bool = False): ...
    def corr(self, other: DataFrame | Series | None = None, pairwise: bool | None = None, numeric_only: bool = False): ...

class ExponentialMovingWindowGroupby(BaseWindowGroupby, ExponentialMovingWindow):
    """
    Provide an exponential moving window groupby implementation.
    """
    def __init__(self, obj, *args, _grouper: Incomplete | None = None, **kwargs) -> None: ...

class OnlineExponentialMovingWindow(ExponentialMovingWindow):
    engine: Incomplete
    engine_kwargs: Incomplete
    def __init__(self, obj: NDFrame, com: float | None = None, span: float | None = None, halflife: float | TimedeltaConvertibleTypes | None = None, alpha: float | None = None, min_periods: int | None = 0, adjust: bool = True, ignore_na: bool = False, axis: Axis = 0, times: np.ndarray | NDFrame | None = None, engine: str = 'numba', engine_kwargs: dict[str, bool] | None = None, *, selection: Incomplete | None = None) -> None: ...
    def reset(self) -> None:
        """
        Reset the state captured by `update` calls.
        """
    def aggregate(self, func, *args, **kwargs) -> None: ...
    def std(self, bias: bool = False, *args, **kwargs): ...
    def corr(self, other: DataFrame | Series | None = None, pairwise: bool | None = None, numeric_only: bool = False): ...
    def cov(self, other: DataFrame | Series | None = None, pairwise: bool | None = None, bias: bool = False, numeric_only: bool = False): ...
    def var(self, bias: bool = False, numeric_only: bool = False): ...
    def mean(self, *args, update: Incomplete | None = None, update_times: Incomplete | None = None, **kwargs):
        '''
        Calculate an online exponentially weighted mean.

        Parameters
        ----------
        update: DataFrame or Series, default None
            New values to continue calculating the
            exponentially weighted mean from the last values and weights.
            Values should be float64 dtype.

            ``update`` needs to be ``None`` the first time the
            exponentially weighted mean is calculated.

        update_times: Series or 1-D np.ndarray, default None
            New times to continue calculating the
            exponentially weighted mean from the last values and weights.
            If ``None``, values are assumed to be evenly spaced
            in time.
            This feature is currently unsupported.

        Returns
        -------
        DataFrame or Series

        Examples
        --------
        >>> df = pd.DataFrame({"a": range(5), "b": range(5, 10)})
        >>> online_ewm = df.head(2).ewm(0.5).online()
        >>> online_ewm.mean()
              a     b
        0  0.00  5.00
        1  0.75  5.75
        >>> online_ewm.mean(update=df.tail(3))
                  a         b
        2  1.615385  6.615385
        3  2.550000  7.550000
        4  3.520661  8.520661
        >>> online_ewm.reset()
        >>> online_ewm.mean()
              a     b
        0  0.00  5.00
        1  0.75  5.75
        '''
