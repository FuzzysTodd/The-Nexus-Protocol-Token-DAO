import numpy as np
from _typeshed import Incomplete
from collections.abc import Generator
from statsmodels.compat.pandas import deprecate_kwarg as deprecate_kwarg
from statsmodels.tools.validation import array_like as array_like, bool_like as bool_like, dict_like as dict_like, float_like as float_like, int_like as int_like, string_like as string_like
from statsmodels.tsa.base.tsa_model import TimeSeriesModel as TimeSeriesModel
from statsmodels.tsa.holtwinters._exponential_smoothers import HoltWintersArgs as HoltWintersArgs
from statsmodels.tsa.holtwinters._smoothers import to_restricted as to_restricted, to_unrestricted as to_unrestricted
from statsmodels.tsa.holtwinters.results import HoltWintersResults as HoltWintersResults, HoltWintersResultsWrapper as HoltWintersResultsWrapper
from statsmodels.tsa.tsatools import freq_to_period as freq_to_period
from typing import Any

SMOOTHERS: Incomplete
PY_SMOOTHERS: Incomplete

def opt_wrapper(func): ...

class _OptConfig:
    alpha: float
    beta: float
    phi: float
    gamma: float
    level: float
    trend: float
    seasonal: np.ndarray
    y: np.ndarray
    params: np.ndarray
    mask: np.ndarray
    mle_retvals: Any
    def unpack_parameters(self, params) -> _OptConfig: ...

class ExponentialSmoothing(TimeSeriesModel):
    '''
    Holt Winter\'s Exponential Smoothing

    Parameters
    ----------
    endog : array_like
        The time series to model.
    trend : {"add", "mul", "additive", "multiplicative", None}, optional
        Type of trend component.
    damped_trend : bool, optional
        Should the trend component be damped.
    seasonal : {"add", "mul", "additive", "multiplicative", None}, optional
        Type of seasonal component.
    seasonal_periods : int, optional
        The number of periods in a complete seasonal cycle, e.g., 4 for
        quarterly data or 7 for daily data with a weekly cycle.
    initialization_method : str, optional
        Method for initialize the recursions. One of:

        * None
        * \'estimated\'
        * \'heuristic\'
        * \'legacy-heuristic\'
        * \'known\'

        None defaults to the pre-0.12 behavior where initial values
        are passed as part of ``fit``. If any of the other values are
        passed, then the initial values must also be set when constructing
        the model. If \'known\' initialization is used, then `initial_level`
        must be passed, as well as `initial_trend` and `initial_seasonal` if
        applicable. Default is \'estimated\'. "legacy-heuristic" uses the same
        values that were used in statsmodels 0.11 and earlier.
    initial_level : float, optional
        The initial level component. Required if estimation method is "known".
        If set using either "estimated" or "heuristic" this value is used.
        This allows one or more of the initial values to be set while
        deferring to the heuristic for others or estimating the unset
        parameters.
    initial_trend : float, optional
        The initial trend component. Required if estimation method is "known".
        If set using either "estimated" or "heuristic" this value is used.
        This allows one or more of the initial values to be set while
        deferring to the heuristic for others or estimating the unset
        parameters.
    initial_seasonal : array_like, optional
        The initial seasonal component. An array of length `seasonal`
        or length `seasonal - 1` (in which case the last initial value
        is computed to make the average effect zero). Only used if
        initialization is \'known\'. Required if estimation method is "known".
        If set using either "estimated" or "heuristic" this value is used.
        This allows one or more of the initial values to be set while
        deferring to the heuristic for others or estimating the unset
        parameters.
    use_boxcox : {True, False, \'log\', float}, optional
        Should the Box-Cox transform be applied to the data first? If \'log\'
        then apply the log. If float then use the value as lambda.
    bounds : dict[str, tuple[float, float]], optional
        An dictionary containing bounds for the parameters in the model,
        excluding the initial values if estimated. The keys of the dictionary
        are the variable names, e.g., smoothing_level or initial_slope.
        The initial seasonal variables are labeled initial_seasonal.<j>
        for j=0,...,m-1 where m is the number of period in a full season.
        Use None to indicate a non-binding constraint, e.g., (0, None)
        constrains a parameter to be non-negative.
    dates : array_like of datetime, optional
        An array-like object of datetime objects. If a Pandas object is given
        for endog, it is assumed to have a DateIndex.
    freq : str, optional
        The frequency of the time-series. A Pandas offset or \'B\', \'D\', \'W\',
        \'M\', \'A\', or \'Q\'. This is optional if dates are given.
    missing : str
        Available options are \'none\', \'drop\', and \'raise\'. If \'none\', no nan
        checking is done. If \'drop\', any observations with nans are dropped.
        If \'raise\', an error is raised. Default is \'none\'.

    Notes
    -----
    This is a full implementation of the holt winters exponential smoothing as
    per [1]_. This includes all the unstable methods as well as the stable
    methods. The implementation of the library covers the functionality of the
    R library as much as possible whilst still being Pythonic.

    See the notebook `Exponential Smoothing
    <../examples/notebooks/generated/exponential_smoothing.html>`__
    for an overview.

    References
    ----------
    .. [1] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles
        and practice. OTexts, 2014.
    '''
    trend: Incomplete
    damped_trend: Incomplete
    seasonal: Incomplete
    has_trend: Incomplete
    has_seasonal: Incomplete
    seasonal_periods: Incomplete
    nobs: Incomplete
    def __init__(self, endog, trend: Incomplete | None = None, damped_trend: bool = False, seasonal: Incomplete | None = None, *, seasonal_periods: Incomplete | None = None, initialization_method: str = 'estimated', initial_level: Incomplete | None = None, initial_trend: Incomplete | None = None, initial_seasonal: Incomplete | None = None, use_boxcox: bool = False, bounds: Incomplete | None = None, dates: Incomplete | None = None, freq: Incomplete | None = None, missing: str = 'none') -> None: ...
    def fix_params(self, values) -> Generator[None, None, None]:
        '''
        Temporarily fix parameters for estimation.

        Parameters
        ----------
        values : dict
            Values to fix. The key is the parameter name and the value is the
            fixed value.

        Yields
        ------
        None
            No value returned.

        Examples
        --------
        >>> from statsmodels.datasets.macrodata import load_pandas
        >>> data = load_pandas()
        >>> import statsmodels.tsa.api as tsa
        >>> mod = tsa.ExponentialSmoothing(data.data.realcons, trend="add",
        ...                                initialization_method="estimated")
        >>> with mod.fix_params({"smoothing_level": 0.2}):
        ...     mod.fit()
        '''
    def predict(self, params, start: Incomplete | None = None, end: Incomplete | None = None):
        """
        In-sample and out-of-sample prediction.

        Parameters
        ----------
        params : ndarray
            The fitted model parameters.
        start : int, str, or datetime
            Zero-indexed observation number at which to start forecasting, ie.,
            the first forecast is start. Can also be a date string to
            parse or a datetime type.
        end : int, str, or datetime
            Zero-indexed observation number at which to end forecasting, ie.,
            the first forecast is start. Can also be a date string to
            parse or a datetime type.

        Returns
        -------
        ndarray
            The predicted values.
        """
    def fit(self, smoothing_level: Incomplete | None = None, smoothing_trend: Incomplete | None = None, smoothing_seasonal: Incomplete | None = None, damping_trend: Incomplete | None = None, *, optimized: bool = True, remove_bias: bool = False, start_params: Incomplete | None = None, method: Incomplete | None = None, minimize_kwargs: Incomplete | None = None, use_brute: bool = True, use_boxcox: Incomplete | None = None, use_basinhopping: Incomplete | None = None, initial_level: Incomplete | None = None, initial_trend: Incomplete | None = None):
        '''
        Fit the model

        Parameters
        ----------
        smoothing_level : float, optional
            The alpha value of the simple exponential smoothing, if the value
            is set then this value will be used as the value.
        smoothing_trend :  float, optional
            The beta value of the Holt\'s trend method, if the value is
            set then this value will be used as the value.
        smoothing_seasonal : float, optional
            The gamma value of the holt winters seasonal method, if the value
            is set then this value will be used as the value.
        damping_trend : float, optional
            The phi value of the damped method, if the value is
            set then this value will be used as the value.
        optimized : bool, optional
            Estimate model parameters by maximizing the log-likelihood.
        remove_bias : bool, optional
            Remove bias from forecast values and fitted values by enforcing
            that the average residual is equal to zero.
        start_params : array_like, optional
            Starting values to used when optimizing the fit.  If not provided,
            starting values are determined using a combination of grid search
            and reasonable values based on the initial values of the data. See
            the notes for the structure of the model parameters.
        method : str, default "L-BFGS-B"
            The minimizer used. Valid options are "L-BFGS-B" , "TNC",
            "SLSQP" (default), "Powell", "trust-constr", "basinhopping" (also
            "bh") and "least_squares" (also "ls"). basinhopping tries multiple
            starting values in an attempt to find a global minimizer in
            non-convex problems, and so is slower than the others.
        minimize_kwargs : dict[str, Any]
            A dictionary of keyword arguments passed to SciPy\'s minimize
            function if method is one of "L-BFGS-B", "TNC",
            "SLSQP", "Powell", or "trust-constr", or SciPy\'s basinhopping
            or least_squares functions. The valid keywords are optimizer
            specific. Consult SciPy\'s documentation for the full set of
            options.
        use_brute : bool, optional
            Search for good starting values using a brute force (grid)
            optimizer. If False, a naive set of starting values is used.
        use_boxcox : {True, False, \'log\', float}, optional
            Should the Box-Cox transform be applied to the data first? If \'log\'
            then apply the log. If float then use the value as lambda.

            .. deprecated:: 0.12

               Set use_boxcox when constructing the model

        use_basinhopping : bool, optional
            Deprecated. Using Basin Hopping optimizer to find optimal values.
            Use ``method`` instead.

            .. deprecated:: 0.12

               Use ``method`` instead.

        initial_level : float, optional
            Value to use when initializing the fitted level.

            .. deprecated:: 0.12

               Set initial_level when constructing the model

        initial_trend : float, optional
            Value to use when initializing the fitted trend.

            .. deprecated:: 0.12

               Set initial_trend when constructing the model
               or set initialization_method.

        Returns
        -------
        HoltWintersResults
            See statsmodels.tsa.holtwinters.HoltWintersResults.

        Notes
        -----
        This is a full implementation of the holt winters exponential smoothing
        as per [1]. This includes all the unstable methods as well as the
        stable methods. The implementation of the library covers the
        functionality of the R library as much as possible whilst still
        being Pythonic.

        The parameters are ordered

        [alpha, beta, gamma, initial_level, initial_trend, phi]

        which are then followed by m seasonal values if the model contains
        a seasonal smoother. Any parameter not relevant for the model is
        omitted. For example, a model that has a level and a seasonal
        component, but no trend and is not damped, would have starting
        values

        [alpha, gamma, initial_level, s0, s1, ..., s<m-1>]

        where sj is the initial value for seasonal component j.

        References
        ----------
        [1] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles
            and practice. OTexts, 2014.
        '''
    def initial_values(self, initial_level: Incomplete | None = None, initial_trend: Incomplete | None = None, force: bool = False):
        """
        Compute initial values used in the exponential smoothing recursions.

        Parameters
        ----------
        initial_level : {float, None}
            The initial value used for the level component.
        initial_trend : {float, None}
            The initial value used for the trend component.
        force : bool
            Force the calculation even if initial values exist.

        Returns
        -------
        initial_level : float
            The initial value used for the level component.
        initial_trend : {float, None}
            The initial value used for the trend component.
        initial_seasons : list
            The initial values used for the seasonal components.

        Notes
        -----
        Convenience function the exposes the values used to initialize the
        recursions. When optimizing parameters these are used as starting
        values.

        Method used to compute the initial value depends on when components
        are included in the model.  In a simple exponential smoothing model
        without trend or a seasonal components, the initial value is set to the
        first observation. When a trend is added, the trend is initialized
        either using y[1]/y[0], if multiplicative, or y[1]-y[0]. When the
        seasonal component is added the initialization adapts to account for
        the modified structure.
        """

class SimpleExpSmoothing(ExponentialSmoothing):
    '''
    Simple Exponential Smoothing

    Parameters
    ----------
    endog : array_like
        The time series to model.
    initialization_method : str, optional
        Method for initialize the recursions. One of:

        * None
        * \'estimated\'
        * \'heuristic\'
        * \'legacy-heuristic\'
        * \'known\'

        None defaults to the pre-0.12 behavior where initial values
        are passed as part of ``fit``. If any of the other values are
        passed, then the initial values must also be set when constructing
        the model. If \'known\' initialization is used, then `initial_level`
        must be passed, as well as `initial_trend` and `initial_seasonal` if
        applicable. Default is \'estimated\'. "legacy-heuristic" uses the same
        values that were used in statsmodels 0.11 and earlier.
    initial_level : float, optional
        The initial level component. Required if estimation method is "known".
        If set using either "estimated" or "heuristic" this value is used.
        This allows one or more of the initial values to be set while
        deferring to the heuristic for others or estimating the unset
        parameters.

    See Also
    --------
    ExponentialSmoothing
        Exponential smoothing with trend and seasonal components.
    Holt
        Exponential smoothing with a trend component.

    Notes
    -----
    This is a full implementation of the simple exponential smoothing as
    per [1]_.  `SimpleExpSmoothing` is a restricted version of
    :class:`ExponentialSmoothing`.

    See the notebook `Exponential Smoothing
    <../examples/notebooks/generated/exponential_smoothing.html>`__
    for an overview.

    References
    ----------
    .. [1] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles
        and practice. OTexts, 2014.
    '''
    def __init__(self, endog, initialization_method: Incomplete | None = None, initial_level: Incomplete | None = None) -> None: ...
    def fit(self, smoothing_level: Incomplete | None = None, *, optimized: bool = True, start_params: Incomplete | None = None, initial_level: Incomplete | None = None, use_brute: bool = True, use_boxcox: Incomplete | None = None, remove_bias: bool = False, method: Incomplete | None = None, minimize_kwargs: Incomplete | None = None):
        '''
        Fit the model

        Parameters
        ----------
        smoothing_level : float, optional
            The smoothing_level value of the simple exponential smoothing, if
            the value is set then this value will be used as the value.
        optimized : bool, optional
            Estimate model parameters by maximizing the log-likelihood.
        start_params : ndarray, optional
            Starting values to used when optimizing the fit.  If not provided,
            starting values are determined using a combination of grid search
            and reasonable values based on the initial values of the data.
        initial_level : float, optional
            Value to use when initializing the fitted level.
        use_brute : bool, optional
            Search for good starting values using a brute force (grid)
            optimizer. If False, a naive set of starting values is used.
        use_boxcox : {True, False, \'log\', float}, optional
            Should the Box-Cox transform be applied to the data first? If \'log\'
            then apply the log. If float then use the value as lambda.
        remove_bias : bool, optional
            Remove bias from forecast values and fitted values by enforcing
            that the average residual is equal to zero.
        method : str, default "L-BFGS-B"
            The minimizer used. Valid options are "L-BFGS-B" (default), "TNC",
            "SLSQP", "Powell", "trust-constr", "basinhopping" (also "bh") and
            "least_squares" (also "ls"). basinhopping tries multiple starting
            values in an attempt to find a global minimizer in non-convex
            problems, and so is slower than the others.
        minimize_kwargs : dict[str, Any]
            A dictionary of keyword arguments passed to SciPy\'s minimize
            function if method is one of "L-BFGS-B" (default), "TNC",
            "SLSQP", "Powell", or "trust-constr", or SciPy\'s basinhopping
            or least_squares. The valid keywords are optimizer specific.
            Consult SciPy\'s documentation for the full set of options.

        Returns
        -------
        HoltWintersResults
            See statsmodels.tsa.holtwinters.HoltWintersResults.

        Notes
        -----
        This is a full implementation of the simple exponential smoothing as
        per [1].

        References
        ----------
        [1] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles
            and practice. OTexts, 2014.
        '''

class Holt(ExponentialSmoothing):
    '''
    Holt\'s Exponential Smoothing

    Parameters
    ----------
    endog : array_like
        The time series to model.
    exponential : bool, optional
        Type of trend component.
    damped_trend : bool, optional
        Should the trend component be damped.
    initialization_method : str, optional
        Method for initialize the recursions. One of:

        * None
        * \'estimated\'
        * \'heuristic\'
        * \'legacy-heuristic\'
        * \'known\'

        None defaults to the pre-0.12 behavior where initial values
        are passed as part of ``fit``. If any of the other values are
        passed, then the initial values must also be set when constructing
        the model. If \'known\' initialization is used, then `initial_level`
        must be passed, as well as `initial_trend` and `initial_seasonal` if
        applicable. Default is \'estimated\'. "legacy-heuristic" uses the same
        values that were used in statsmodels 0.11 and earlier.
    initial_level : float, optional
        The initial level component. Required if estimation method is "known".
        If set using either "estimated" or "heuristic" this value is used.
        This allows one or more of the initial values to be set while
        deferring to the heuristic for others or estimating the unset
        parameters.
    initial_trend : float, optional
        The initial trend component. Required if estimation method is "known".
        If set using either "estimated" or "heuristic" this value is used.
        This allows one or more of the initial values to be set while
        deferring to the heuristic for others or estimating the unset
        parameters.

    See Also
    --------
    ExponentialSmoothing
        Exponential smoothing with trend and seasonal components.
    SimpleExpSmoothing
        Basic exponential smoothing with only a level component.

    Notes
    -----
    This is a full implementation of the Holt\'s exponential smoothing as
    per [1]_. `Holt` is a restricted version of :class:`ExponentialSmoothing`.

    See the notebook `Exponential Smoothing
    <../examples/notebooks/generated/exponential_smoothing.html>`__
    for an overview.

    References
    ----------
    .. [1] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles
        and practice. OTexts, 2014.
    '''
    def __init__(self, endog, exponential: bool = False, damped_trend: bool = False, initialization_method: Incomplete | None = None, initial_level: Incomplete | None = None, initial_trend: Incomplete | None = None) -> None: ...
    def fit(self, smoothing_level: Incomplete | None = None, smoothing_trend: Incomplete | None = None, *, damping_trend: Incomplete | None = None, optimized: bool = True, start_params: Incomplete | None = None, initial_level: Incomplete | None = None, initial_trend: Incomplete | None = None, use_brute: bool = True, use_boxcox: Incomplete | None = None, remove_bias: bool = False, method: Incomplete | None = None, minimize_kwargs: Incomplete | None = None):
        '''
        Fit the model

        Parameters
        ----------
        smoothing_level : float, optional
            The alpha value of the simple exponential smoothing, if the value
            is set then this value will be used as the value.
        smoothing_trend :  float, optional
            The beta value of the Holt\'s trend method, if the value is
            set then this value will be used as the value.
        damping_trend : float, optional
            The phi value of the damped method, if the value is
            set then this value will be used as the value.
        optimized : bool, optional
            Estimate model parameters by maximizing the log-likelihood.
        start_params : ndarray, optional
            Starting values to used when optimizing the fit.  If not provided,
            starting values are determined using a combination of grid search
            and reasonable values based on the initial values of the data.
        initial_level : float, optional
            Value to use when initializing the fitted level.

            .. deprecated:: 0.12

               Set initial_level when constructing the model

        initial_trend : float, optional
            Value to use when initializing the fitted trend.

            .. deprecated:: 0.12

               Set initial_trend when constructing the model

        use_brute : bool, optional
            Search for good starting values using a brute force (grid)
            optimizer. If False, a naive set of starting values is used.
        use_boxcox : {True, False, \'log\', float}, optional
            Should the Box-Cox transform be applied to the data first? If \'log\'
            then apply the log. If float then use the value as lambda.
        remove_bias : bool, optional
            Remove bias from forecast values and fitted values by enforcing
            that the average residual is equal to zero.
        method : str, default "L-BFGS-B"
            The minimizer used. Valid options are "L-BFGS-B" (default), "TNC",
            "SLSQP", "Powell", "trust-constr", "basinhopping" (also "bh") and
            "least_squares" (also "ls"). basinhopping tries multiple starting
            values in an attempt to find a global minimizer in non-convex
            problems, and so is slower than the others.
        minimize_kwargs : dict[str, Any]
            A dictionary of keyword arguments passed to SciPy\'s minimize
            function if method is one of "L-BFGS-B" (default), "TNC",
            "SLSQP", "Powell", or "trust-constr", or SciPy\'s basinhopping
            or least_squares. The valid keywords are optimizer specific.
            Consult SciPy\'s documentation for the full set of options.

        Returns
        -------
        HoltWintersResults
            See statsmodels.tsa.holtwinters.HoltWintersResults.

        Notes
        -----
        This is a full implementation of the Holt\'s exponential smoothing as
        per [1].

        References
        ----------
        [1] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles
            and practice. OTexts, 2014.
        '''
