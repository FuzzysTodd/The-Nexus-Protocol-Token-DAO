from .initialization import Initialization as Initialization
from .kalman_filter import INVERT_UNIVARIATE as INVERT_UNIVARIATE, SOLVE_LU as SOLVE_LU
from .mlemodel import MLEModel as MLEModel, MLEResults as MLEResults, MLEResultsWrapper as MLEResultsWrapper
from .tools import concat as concat, constrain_stationary_multivariate as constrain_stationary_multivariate, is_invertible as is_invertible, prepare_exog as prepare_exog, prepare_trend_data as prepare_trend_data, prepare_trend_spec as prepare_trend_spec, unconstrain_stationary_multivariate as unconstrain_stationary_multivariate
from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.sm_exceptions import EstimationWarning as EstimationWarning
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.vector_ar import var_model as var_model

class VARMAX(MLEModel):
    '''
    Vector Autoregressive Moving Average with eXogenous regressors model

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`, , shaped nobs x k_endog.
    exog : array_like, optional
        Array of exogenous regressors, shaped nobs x k.
    order : iterable
        The (p,q) order of the model for the number of AR and MA parameters to
        use.
    trend : str{\'n\',\'c\',\'t\',\'ct\'} or iterable, optional
        Parameter controlling the deterministic trend polynomial :math:`A(t)`.
        Can be specified as a string where \'c\' indicates a constant (i.e. a
        degree zero component of the trend polynomial), \'t\' indicates a
        linear trend with time, and \'ct\' is both. Can also be specified as an
        iterable defining the non-zero polynomial exponents to include, in
        increasing order. For example, `[1,1,0,1]` denotes
        :math:`a + bt + ct^3`. Default is a constant trend component.
    error_cov_type : {\'diagonal\', \'unstructured\'}, optional
        The structure of the covariance matrix of the error term, where
        "unstructured" puts no restrictions on the matrix and "diagonal"
        requires it to be a diagonal matrix (uncorrelated errors). Default is
        "unstructured".
    measurement_error : bool, optional
        Whether or not to assume the endogenous observations `endog` were
        measured with error. Default is False.
    enforce_stationarity : bool, optional
        Whether or not to transform the AR parameters to enforce stationarity
        in the autoregressive component of the model. Default is True.
    enforce_invertibility : bool, optional
        Whether or not to transform the MA parameters to enforce invertibility
        in the moving average component of the model. Default is True.
    trend_offset : int, optional
        The offset at which to start time trend values. Default is 1, so that
        if `trend=\'t\'` the trend is equal to 1, 2, ..., nobs. Typically is only
        set when the model created by extending a previous dataset.
    **kwargs
        Keyword arguments may be used to provide default values for state space
        matrices or for Kalman filtering options. See `Representation`, and
        `KalmanFilter` for more details.

    Attributes
    ----------
    order : iterable
        The (p,q) order of the model for the number of AR and MA parameters to
        use.
    trend : str{\'n\',\'c\',\'t\',\'ct\'} or iterable
        Parameter controlling the deterministic trend polynomial :math:`A(t)`.
        Can be specified as a string where \'c\' indicates a constant (i.e. a
        degree zero component of the trend polynomial), \'t\' indicates a
        linear trend with time, and \'ct\' is both. Can also be specified as an
        iterable defining the non-zero polynomial exponents to include, in
        increasing order. For example, `[1,1,0,1]` denotes
        :math:`a + bt + ct^3`.
    error_cov_type : {\'diagonal\', \'unstructured\'}, optional
        The structure of the covariance matrix of the error term, where
        "unstructured" puts no restrictions on the matrix and "diagonal"
        requires it to be a diagonal matrix (uncorrelated errors). Default is
        "unstructured".
    measurement_error : bool, optional
        Whether or not to assume the endogenous observations `endog` were
        measured with error. Default is False.
    enforce_stationarity : bool, optional
        Whether or not to transform the AR parameters to enforce stationarity
        in the autoregressive component of the model. Default is True.
    enforce_invertibility : bool, optional
        Whether or not to transform the MA parameters to enforce invertibility
        in the moving average component of the model. Default is True.

    Notes
    -----
    Generically, the VARMAX model is specified (see for example chapter 18 of
    [1]_):

    .. math::

        y_t = A(t) + A_1 y_{t-1} + \\dots + A_p y_{t-p} + B x_t + \\epsilon_t +
        M_1 \\epsilon_{t-1} + \\dots M_q \\epsilon_{t-q}

    where :math:`\\epsilon_t \\sim N(0, \\Omega)`, and where :math:`y_t` is a
    `k_endog x 1` vector. Additionally, this model allows considering the case
    where the variables are measured with error.

    Note that in the full VARMA(p,q) case there is a fundamental identification
    problem in that the coefficient matrices :math:`\\{A_i, M_j\\}` are not
    generally unique, meaning that for a given time series process there may
    be multiple sets of matrices that equivalently represent it. See Chapter 12
    of [1]_ for more information. Although this class can be used to estimate
    VARMA(p,q) models, a warning is issued to remind users that no steps have
    been taken to ensure identification in this case.

    References
    ----------
    .. [1] Lütkepohl, Helmut. 2007.
       New Introduction to Multiple Time Series Analysis.
       Berlin: Springer.
    '''
    error_cov_type: Incomplete
    measurement_error: Incomplete
    enforce_stationarity: Incomplete
    enforce_invertibility: Incomplete
    order: Incomplete
    k_ar: Incomplete
    k_ma: Incomplete
    trend: Incomplete
    trend_offset: Incomplete
    mle_regression: Incomplete
    parameters: Incomplete
    k_params: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, order=(1, 0), trend: str = 'c', error_cov_type: str = 'unstructured', measurement_error: bool = False, enforce_stationarity: bool = True, enforce_invertibility: bool = True, trend_offset: int = 1, **kwargs) -> None: ...
    def clone(self, endog, exog: Incomplete | None = None, **kwargs): ...
    @property
    def start_params(self): ...
    @property
    def param_names(self): ...
    def transform_params(self, unconstrained):
        """
        Transform unconstrained parameters used by the optimizer to constrained
        parameters used in likelihood evaluation

        Parameters
        ----------
        unconstrained : array_like
            Array of unconstrained parameters used by the optimizer, to be
            transformed.

        Returns
        -------
        constrained : array_like
            Array of constrained parameters which may be used in likelihood
            evaluation.

        Notes
        -----
        Constrains the factor transition to be stationary and variances to be
        positive.
        """
    def untransform_params(self, constrained):
        """
        Transform constrained parameters used in likelihood evaluation
        to unconstrained parameters used by the optimizer.

        Parameters
        ----------
        constrained : array_like
            Array of constrained parameters used in likelihood evaluation, to
            be transformed.

        Returns
        -------
        unconstrained : array_like
            Array of unconstrained parameters used by the optimizer.
        """
    def update(self, params, transformed: bool = True, includes_fixed: bool = False, complex_step: bool = False) -> None: ...
    def simulate(self, params, nsimulations, measurement_shocks: Incomplete | None = None, state_shocks: Incomplete | None = None, initial_state: Incomplete | None = None, anchor: Incomplete | None = None, repetitions: Incomplete | None = None, exog: Incomplete | None = None, extend_model: Incomplete | None = None, extend_kwargs: Incomplete | None = None, transformed: bool = True, includes_fixed: bool = False, **kwargs): ...

class VARMAXResults(MLEResults):
    """
    Class to hold results from fitting an VARMAX model.

    Parameters
    ----------
    model : VARMAX instance
        The fitted model instance

    Attributes
    ----------
    specification : dictionary
        Dictionary including all attributes from the VARMAX model instance.
    coefficient_matrices_var : ndarray
        Array containing autoregressive lag polynomial coefficient matrices,
        ordered from lowest degree to highest.
    coefficient_matrices_vma : ndarray
        Array containing moving average lag polynomial coefficients,
        ordered from lowest degree to highest.

    See Also
    --------
    statsmodels.tsa.statespace.kalman_filter.FilterResults
    statsmodels.tsa.statespace.mlemodel.MLEResults
    """
    specification: Incomplete
    coefficient_matrices_var: Incomplete
    coefficient_matrices_vma: Incomplete
    def __init__(self, model, params, filter_results, cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, **kwargs) -> None: ...
    def extend(self, endog, exog: Incomplete | None = None, **kwargs): ...
    def get_prediction(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, information_set: str = 'predicted', index: Incomplete | None = None, exog: Incomplete | None = None, **kwargs): ...
    def simulate(self, nsimulations, measurement_shocks: Incomplete | None = None, state_shocks: Incomplete | None = None, initial_state: Incomplete | None = None, anchor: Incomplete | None = None, repetitions: Incomplete | None = None, exog: Incomplete | None = None, extend_model: Incomplete | None = None, extend_kwargs: Incomplete | None = None, **kwargs): ...
    def summary(self, alpha: float = 0.05, start: Incomplete | None = None, separate_params: bool = True): ...

class VARMAXResultsWrapper(MLEResultsWrapper): ...
