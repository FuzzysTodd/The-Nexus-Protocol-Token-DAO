from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.tools import Bunch as Bunch
from statsmodels.tsa.statespace.mlemodel import MLEModel as MLEModel, MLEResults as MLEResults, MLEResultsWrapper as MLEResultsWrapper, PredictionResults as PredictionResults, PredictionResultsWrapper as PredictionResultsWrapper
from statsmodels.tsa.statespace.tools import concat as concat

class RecursiveLS(MLEModel):
    """
    Recursive least squares

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`
    exog : array_like
        Array of exogenous regressors, shaped nobs x k.
    constraints : array_like, str, or tuple
            - array : An r x k array where r is the number of restrictions to
              test and k is the number of regressors. It is assumed that the
              linear combination is equal to zero.
            - str : The full hypotheses to test can be given as a string.
              See the examples.
            - tuple : A tuple of arrays in the form (R, q), ``q`` can be
              either a scalar or a length p row vector.

    Notes
    -----
    Recursive least squares (RLS) corresponds to expanding window ordinary
    least squares (OLS).

    This model applies the Kalman filter to compute recursive estimates of the
    coefficients and recursive residuals.

    References
    ----------
    .. [*] Durbin, James, and Siem Jan Koopman. 2012.
       Time Series Analysis by State Space Methods: Second Edition.
       Oxford University Press.
    """
    k_exog: Incomplete
    k_constraints: int
    k_endog: int
    def __init__(self, endog, exog, constraints: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def from_formula(cls, formula, data, subset: Incomplete | None = None, constraints: Incomplete | None = None): ...
    def fit(self):
        """
        Fits the model by application of the Kalman filter

        Returns
        -------
        RecursiveLSResults
        """
    def filter(self, return_ssm: bool = False, **kwargs): ...
    def smooth(self, return_ssm: bool = False, **kwargs): ...
    @property
    def endog_names(self): ...
    @property
    def param_names(self): ...
    @property
    def start_params(self): ...
    def update(self, params, **kwargs) -> None:
        """
        Update the parameters of the model

        Updates the representation matrices to fill in the new parameter
        values.

        Parameters
        ----------
        params : array_like
            Array of new parameters.
        transformed : bool, optional
            Whether or not `params` is already transformed. If set to False,
            `transform_params` is called. Default is True..

        Returns
        -------
        params : array_like
            Array of parameters.
        """

class RecursiveLSResults(MLEResults):
    """
    Class to hold results from fitting a recursive least squares model.

    Parameters
    ----------
    model : RecursiveLS instance
        The fitted model instance

    Attributes
    ----------
    specification : dictionary
        Dictionary including all attributes from the recursive least squares
        model instance.

    See Also
    --------
    statsmodels.tsa.statespace.kalman_filter.FilterResults
    statsmodels.tsa.statespace.mlemodel.MLEResults
    """
    df_model: Incomplete
    df_resid: Incomplete
    specification: Incomplete
    def __init__(self, model, params, filter_results, cov_type: str = 'opg', **kwargs) -> None: ...
    @property
    def recursive_coefficients(self):
        """
        Estimates of regression coefficients, recursively estimated

        Returns
        -------
        out: Bunch
            Has the following attributes:

            - `filtered`: a time series array with the filtered estimate of
                          the component
            - `filtered_cov`: a time series array with the filtered estimate of
                          the variance/covariance of the component
            - `smoothed`: a time series array with the smoothed estimate of
                          the component
            - `smoothed_cov`: a time series array with the smoothed estimate of
                          the variance/covariance of the component
            - `offset`: an integer giving the offset in the state vector where
                        this component begins
        """
    def resid_recursive(self):
        '''
        Recursive residuals

        Returns
        -------
        resid_recursive : array_like
            An array of length `nobs` holding the recursive
            residuals.

        Notes
        -----
        These quantities are defined in, for example, Harvey (1989)
        section 5.4. In fact, there he defines the standardized innovations in
        equation 5.4.1, but in his version they have non-unit variance, whereas
        the standardized forecast errors computed by the Kalman filter here
        assume unit variance. To convert to Harvey\'s definition, we need to
        multiply by the standard deviation.

        Harvey notes that in smaller samples, "although the second moment
        of the :math:`\\tilde \\sigma_*^{-1} \\tilde v_t`\'s is unity, the
        variance is not necessarily equal to unity as the mean need not be
        equal to zero", and he defines an alternative version (which are
        not provided here).
        '''
    def cusum(self):
        '''
        Cumulative sum of standardized recursive residuals statistics

        Returns
        -------
        cusum : array_like
            An array of length `nobs - k_exog` holding the
            CUSUM statistics.

        Notes
        -----
        The CUSUM statistic takes the form:

        .. math::

            W_t = \\frac{1}{\\hat \\sigma} \\sum_{j=k+1}^t w_j

        where :math:`w_j` is the recursive residual at time :math:`j` and
        :math:`\\hat \\sigma` is the estimate of the standard deviation
        from the full sample.

        Excludes the first `k_exog` datapoints.

        Due to differences in the way :math:`\\hat \\sigma` is calculated, the
        output of this function differs slightly from the output in the
        R package strucchange and the Stata contributed .ado file cusum6. The
        calculation in this package is consistent with the description of
        Brown et al. (1975)

        References
        ----------
        .. [*] Brown, R. L., J. Durbin, and J. M. Evans. 1975.
           "Techniques for Testing the Constancy of
           Regression Relationships over Time."
           Journal of the Royal Statistical Society.
           Series B (Methodological) 37 (2): 149-92.
        '''
    def cusum_squares(self):
        '''
        Cumulative sum of squares of standardized recursive residuals
        statistics

        Returns
        -------
        cusum_squares : array_like
            An array of length `nobs - k_exog` holding the
            CUSUM of squares statistics.

        Notes
        -----
        The CUSUM of squares statistic takes the form:

        .. math::

            s_t = \\left ( \\sum_{j=k+1}^t w_j^2 \\right ) \\Bigg /
                  \\left ( \\sum_{j=k+1}^T w_j^2 \\right )

        where :math:`w_j` is the recursive residual at time :math:`j`.

        Excludes the first `k_exog` datapoints.

        References
        ----------
        .. [*] Brown, R. L., J. Durbin, and J. M. Evans. 1975.
           "Techniques for Testing the Constancy of
           Regression Relationships over Time."
           Journal of the Royal Statistical Society.
           Series B (Methodological) 37 (2): 149-92.
        '''
    def llf_recursive_obs(self):
        """
        (float) Loglikelihood at observation, computed from recursive residuals
        """
    def llf_recursive(self):
        """
        (float) Loglikelihood defined by recursive residuals, equivalent to OLS
        """
    def ssr(self):
        """ssr"""
    def centered_tss(self):
        """Centered tss"""
    def uncentered_tss(self):
        """uncentered tss"""
    def ess(self):
        """ess"""
    def rsquared(self):
        """rsquared"""
    def mse_model(self):
        """mse_model"""
    def mse_resid(self):
        """mse_resid"""
    def mse_total(self):
        """mse_total"""
    def get_prediction(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, information_set: str = 'predicted', signal_only: bool = False, index: Incomplete | None = None, **kwargs): ...
    def plot_recursive_coefficient(self, variables: int = 0, alpha: float = 0.05, legend_loc: str = 'upper left', fig: Incomplete | None = None, figsize: Incomplete | None = None):
        """
        Plot the recursively estimated coefficients on a given variable

        Parameters
        ----------
        variables : {int, str, list[int], list[str]}, optional
            Integer index or string name of the variable whose coefficient will
            be plotted. Can also be an iterable of integers or strings. Default
            is the first variable.
        alpha : float, optional
            The confidence intervals for the coefficient are (1 - alpha) %
        legend_loc : str, optional
            The location of the legend in the plot. Default is upper left.
        fig : Figure, optional
            If given, subplots are created in this figure instead of in a new
            figure. Note that the grid will be created in the provided
            figure using `fig.add_subplot()`.
        figsize : tuple, optional
            If a figure is created, this argument allows specifying a size.
            The tuple is (width, height).

        Notes
        -----
        All plots contain (1 - `alpha`) %  confidence intervals.
        """
    def plot_cusum(self, alpha: float = 0.05, legend_loc: str = 'upper left', fig: Incomplete | None = None, figsize: Incomplete | None = None):
        '''
        Plot the CUSUM statistic and significance bounds.

        Parameters
        ----------
        alpha : float, optional
            The plotted significance bounds are alpha %.
        legend_loc : str, optional
            The location of the legend in the plot. Default is upper left.
        fig : Figure, optional
            If given, subplots are created in this figure instead of in a new
            figure. Note that the grid will be created in the provided
            figure using `fig.add_subplot()`.
        figsize : tuple, optional
            If a figure is created, this argument allows specifying a size.
            The tuple is (width, height).

        Notes
        -----
        Evidence of parameter instability may be found if the CUSUM statistic
        moves out of the significance bounds.

        References
        ----------
        .. [*] Brown, R. L., J. Durbin, and J. M. Evans. 1975.
           "Techniques for Testing the Constancy of
           Regression Relationships over Time."
           Journal of the Royal Statistical Society.
           Series B (Methodological) 37 (2): 149-92.
        '''
    def plot_cusum_squares(self, alpha: float = 0.05, legend_loc: str = 'upper left', fig: Incomplete | None = None, figsize: Incomplete | None = None):
        '''
        Plot the CUSUM of squares statistic and significance bounds.

        Parameters
        ----------
        alpha : float, optional
            The plotted significance bounds are alpha %.
        legend_loc : str, optional
            The location of the legend in the plot. Default is upper left.
        fig : Figure, optional
            If given, subplots are created in this figure instead of in a new
            figure. Note that the grid will be created in the provided
            figure using `fig.add_subplot()`.
        figsize : tuple, optional
            If a figure is created, this argument allows specifying a size.
            The tuple is (width, height).

        Notes
        -----
        Evidence of parameter instability may be found if the CUSUM of squares
        statistic moves out of the significance bounds.

        Critical values used in creating the significance bounds are computed
        using the approximate formula of [1]_.

        References
        ----------
        .. [*] Brown, R. L., J. Durbin, and J. M. Evans. 1975.
           "Techniques for Testing the Constancy of
           Regression Relationships over Time."
           Journal of the Royal Statistical Society.
           Series B (Methodological) 37 (2): 149-92.
        .. [1] Edgerton, David, and Curt Wells. 1994.
           "Critical Values for the Cusumsq Statistic
           in Medium and Large Sized Samples."
           Oxford Bulletin of Economics and Statistics 56 (3): 355-65.
        '''

class RecursiveLSResultsWrapper(MLEResultsWrapper): ...
