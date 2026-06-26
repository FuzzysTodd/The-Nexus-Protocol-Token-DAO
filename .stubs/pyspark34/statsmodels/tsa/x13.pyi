from _typeshed import Incomplete

__all__ = ['x13_arima_select_order', 'x13_arima_analysis']

class _freq_to_period:
    def __getitem__(self, key): ...

class Spec:
    @property
    def spec_name(self): ...
    def create_spec(self, **kwargs): ...
    options: Incomplete
    def set_options(self, **kwargs) -> None: ...

class SeriesSpec(Spec):
    """
    Parameters
    ----------
    data
    appendbcst : bool
    appendfcst : bool
    comptype
    compwt
    decimals
    modelspan
    name
    period
    precision
    to_print
    to_save
    span
    start
    title
    type

    Notes
    -----
    Rarely used arguments

    divpower
    missingcode
    missingval
    saveprecision
    trimzero
    """
    def __init__(self, data, name: str = 'Unnamed Series', appendbcst: bool = False, appendfcst: bool = False, comptype: Incomplete | None = None, compwt: int = 1, decimals: int = 0, modelspan=(), period: int = 12, precision: int = 0, to_print=[], to_save=[], span=(), start=(1, 1), title: str = '', series_type: Incomplete | None = None, divpower: Incomplete | None = None, missingcode: int = -99999, missingval: int = 1000000000) -> None: ...

def x13_arima_analysis(endog, maxorder=(2, 1), maxdiff=(2, 1), diff: Incomplete | None = None, exog: Incomplete | None = None, log: Incomplete | None = None, outlier: bool = True, trading: bool = False, forecast_periods: Incomplete | None = None, retspec: bool = False, speconly: bool = False, start: Incomplete | None = None, freq: Incomplete | None = None, print_stdout: bool = False, x12path: Incomplete | None = None, prefer_x13: bool = True, tempdir: Incomplete | None = None):
    """
    Perform x13-arima analysis for monthly or quarterly data.

    Parameters
    ----------
    endog : array_like, pandas.Series
        The series to model. It is best to use a pandas object with a
        DatetimeIndex or PeriodIndex. However, you can pass an array-like
        object. If your object does not have a dates index then ``start`` and
        ``freq`` are not optional.
    maxorder : tuple
        The maximum order of the regular and seasonal ARMA polynomials to
        examine during the model identification. The order for the regular
        polynomial must be greater than zero and no larger than 4. The
        order for the seasonal polynomial may be 1 or 2.
    maxdiff : tuple
        The maximum orders for regular and seasonal differencing in the
        automatic differencing procedure. Acceptable inputs for regular
        differencing are 1 and 2. The maximum order for seasonal differencing
        is 1. If ``diff`` is specified then ``maxdiff`` should be None.
        Otherwise, ``diff`` will be ignored. See also ``diff``.
    diff : tuple
        Fixes the orders of differencing for the regular and seasonal
        differencing. Regular differencing may be 0, 1, or 2. Seasonal
        differencing may be 0 or 1. ``maxdiff`` must be None, otherwise
        ``diff`` is ignored.
    exog : array_like
        Exogenous variables.
    log : bool or None
        If None, it is automatically determined whether to log the series or
        not. If False, logs are not taken. If True, logs are taken.
    outlier : bool
        Whether or not outliers are tested for and corrected, if detected.
    trading : bool
        Whether or not trading day effects are tested for.
    forecast_periods : int
        Number of forecasts produced. The default is None.
    retspec : bool
        Whether to return the created specification file. Can be useful for
        debugging.
    speconly : bool
        Whether to create the specification file and then return it without
        performing the analysis. Can be useful for debugging.
    start : str, datetime
        Must be given if ``endog`` does not have date information in its index.
        Anything accepted by pandas.DatetimeIndex for the start value.
    freq : str
        Must be givein if ``endog`` does not have date information in its
        index. Anything accepted by pandas.DatetimeIndex for the freq value.
    print_stdout : bool
        The stdout from X12/X13 is suppressed. To print it out, set this
        to True. Default is False.
    x12path : str or None
        The path to x12 or x13 binary. If None, the program will attempt
        to find x13as or x12a on the PATH or by looking at X13PATH or
        X12PATH depending on the value of prefer_x13.
    prefer_x13 : bool
        If True, will look for x13as first and will fallback to the X13PATH
        environmental variable. If False, will look for x12a first and will
        fallback to the X12PATH environmental variable. If x12path points
        to the path for the X12/X13 binary, it does nothing.
    tempdir : str
        The path to where temporary files are created by the function.
        If None, files are created in the default temporary file location.

    Returns
    -------
    Bunch
        A bunch object containing the listed attributes.

        - results : str
          The full output from the X12/X13 run.
        - seasadj : pandas.Series
          The final seasonally adjusted ``endog``.
        - trend : pandas.Series
          The trend-cycle component of ``endog``.
        - irregular : pandas.Series
          The final irregular component of ``endog``.
        - stdout : str
          The captured stdout produced by x12/x13.
        - spec : str, optional
          Returned if ``retspec`` is True. The only thing returned if
          ``speconly`` is True.

    Notes
    -----
    This works by creating a specification file, writing it to a temporary
    directory, invoking X12/X13 in a subprocess, and reading the output
    directory, invoking exog12/X13 in a subprocess, and reading the output
    back in.
    """
def x13_arima_select_order(endog, maxorder=(2, 1), maxdiff=(2, 1), diff: Incomplete | None = None, exog: Incomplete | None = None, log: Incomplete | None = None, outlier: bool = True, trading: bool = False, forecast_periods: Incomplete | None = None, start: Incomplete | None = None, freq: Incomplete | None = None, print_stdout: bool = False, x12path: Incomplete | None = None, prefer_x13: bool = True, tempdir: Incomplete | None = None):
    """
    Perform automatic seasonal ARIMA order identification using x12/x13 ARIMA.

    Parameters
    ----------
    endog : array_like, pandas.Series
        The series to model. It is best to use a pandas object with a
        DatetimeIndex or PeriodIndex. However, you can pass an array-like
        object. If your object does not have a dates index then ``start`` and
        ``freq`` are not optional.
    maxorder : tuple
        The maximum order of the regular and seasonal ARMA polynomials to
        examine during the model identification. The order for the regular
        polynomial must be greater than zero and no larger than 4. The
        order for the seasonal polynomial may be 1 or 2.
    maxdiff : tuple
        The maximum orders for regular and seasonal differencing in the
        automatic differencing procedure. Acceptable inputs for regular
        differencing are 1 and 2. The maximum order for seasonal differencing
        is 1. If ``diff`` is specified then ``maxdiff`` should be None.
        Otherwise, ``diff`` will be ignored. See also ``diff``.
    diff : tuple
        Fixes the orders of differencing for the regular and seasonal
        differencing. Regular differencing may be 0, 1, or 2. Seasonal
        differencing may be 0 or 1. ``maxdiff`` must be None, otherwise
        ``diff`` is ignored.
    exog : array_like
        Exogenous variables.
    log : bool or None
        If None, it is automatically determined whether to log the series or
        not. If False, logs are not taken. If True, logs are taken.
    outlier : bool
        Whether or not outliers are tested for and corrected, if detected.
    trading : bool
        Whether or not trading day effects are tested for.
    forecast_periods : int
        Number of forecasts produced. The default is None.
    start : str, datetime
        Must be given if ``endog`` does not have date information in its index.
        Anything accepted by pandas.DatetimeIndex for the start value.
    freq : str
        Must be givein if ``endog`` does not have date information in its
        index. Anything accepted by pandas.DatetimeIndex for the freq value.
    print_stdout : bool
        The stdout from X12/X13 is suppressed. To print it out, set this
        to True. Default is False.
    x12path : str or None
        The path to x12 or x13 binary. If None, the program will attempt
        to find x13as or x12a on the PATH or by looking at X13PATH or X12PATH
        depending on the value of prefer_x13.
    prefer_x13 : bool
        If True, will look for x13as first and will fallback to the X13PATH
        environmental variable. If False, will look for x12a first and will
        fallback to the X12PATH environmental variable. If x12path points
        to the path for the X12/X13 binary, it does nothing.
    tempdir : str
        The path to where temporary files are created by the function.
        If None, files are created in the default temporary file location.

    Returns
    -------
    Bunch
        A bunch object containing the listed attributes.

        - order : tuple
          The regular order.
        - sorder : tuple
          The seasonal order.
        - include_mean : bool
          Whether to include a mean or not.
        - results : str
          The full results from the X12/X13 analysis.
        - stdout : str
          The captured stdout from the X12/X13 analysis.

    Notes
    -----
    This works by creating a specification file, writing it to a temporary
    directory, invoking X12/X13 in a subprocess, and reading the output back
    in.
    """

class X13ArimaAnalysisResult:
    def __init__(self, **kwargs) -> None: ...
    def plot(self): ...
