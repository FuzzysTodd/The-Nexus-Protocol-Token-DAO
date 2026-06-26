import statsmodels.base.model as base
from _typeshed import Incomplete
from statsmodels.base import model as model
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class PHSurvivalTime:
    nstrat_orig: Incomplete
    nstrat: Incomplete
    offset_s: Incomplete
    n_obs: Incomplete
    stratum_rows: Incomplete
    stratum_names: Incomplete
    time_s: Incomplete
    exog_s: Incomplete
    status_s: Incomplete
    entry_s: Incomplete
    def __init__(self, time, status, exog, strata: Incomplete | None = None, entry: Incomplete | None = None, offset: Incomplete | None = None) -> None:
        """
        Represent a collection of survival times with possible
        stratification and left truncation.

        Parameters
        ----------
        time : array_like
            The times at which either the event (failure) occurs or
            the observation is censored.
        status : array_like
            Indicates whether the event (failure) occurs at `time`
            (`status` is 1), or if `time` is a censoring time (`status`
            is 0).
        exog : array_like
            The exogeneous (covariate) data matrix, cases are rows and
            variables are columns.
        strata : array_like
            Grouping variable defining the strata.  If None, all
            observations are in a single stratum.
        entry : array_like
            Entry (left truncation) times.  The observation is not
            part of the risk set for times before the entry time.  If
            None, the entry time is treated as being zero, which
            gives no left truncation.  The entry time must be less
            than or equal to `time`.
        offset : array_like
            An optional array of offsets
        """

class PHReg(model.LikelihoodModel):
    """
    Cox Proportional Hazards Regression Model

    The Cox PH Model is for right censored data.

    Parameters
    ----------
    endog : array_like
        The observed times (event or censoring)
    exog : 2D array_like
        The covariates or exogeneous variables
    status : array_like
        The censoring status values; status=1 indicates that an
        event occurred (e.g. failure or death), status=0 indicates
        that the observation was right censored. If None, defaults
        to status=1 for all cases.
    entry : array_like
        The entry times, if left truncation occurs
    strata : array_like
        Stratum labels.  If None, all observations are taken to be
        in a single stratum.
    ties : str
        The method used to handle tied times, must be either 'breslow'
        or 'efron'.
    offset : array_like
        Array of offset values
    missing : str
        The method used to handle missing data

    Notes
    -----
    Proportional hazards regression models should not include an
    explicit or implicit intercept.  The effect of an intercept is
    not identified using the partial likelihood approach.

    `endog`, `event`, `strata`, `entry`, and the first dimension
    of `exog` all must have the same length
    """
    status: Incomplete
    entry: Incomplete
    strata: Incomplete
    offset: Incomplete
    surv: Incomplete
    nobs: Incomplete
    groups: Incomplete
    missing: Incomplete
    df_resid: Incomplete
    df_model: Incomplete
    ties: Incomplete
    def __init__(self, endog, exog, status: Incomplete | None = None, entry: Incomplete | None = None, strata: Incomplete | None = None, offset: Incomplete | None = None, ties: str = 'breslow', missing: str = 'drop', **kwargs) -> None: ...
    @classmethod
    def from_formula(cls, formula, data, status: Incomplete | None = None, entry: Incomplete | None = None, strata: Incomplete | None = None, offset: Incomplete | None = None, subset: Incomplete | None = None, ties: str = 'breslow', missing: str = 'drop', *args, **kwargs):
        '''
        Create a proportional hazards regression model from a formula
        and dataframe.

        Parameters
        ----------
        formula : str or generic Formula object
            The formula specifying the model
        data : array_like
            The data for the model. See Notes.
        status : array_like
            The censoring status values; status=1 indicates that an
            event occurred (e.g. failure or death), status=0 indicates
            that the observation was right censored. If None, defaults
            to status=1 for all cases.
        entry : array_like
            The entry times, if left truncation occurs
        strata : array_like
            Stratum labels.  If None, all observations are taken to be
            in a single stratum.
        offset : array_like
            Array of offset values
        subset : array_like
            An array-like object of booleans, integers, or index
            values that indicate the subset of df to use in the
            model. Assumes df is a `pandas.DataFrame`
        ties : str
            The method used to handle tied times, must be either \'breslow\'
            or \'efron\'.
        missing : str
            The method used to handle missing data
        args : extra arguments
            These are passed to the model
        kwargs : extra keyword arguments
            These are passed to the model with one exception. The
            ``eval_env`` keyword is passed to patsy. It can be either a
            :class:`patsy:patsy.EvalEnvironment` object or an integer
            indicating the depth of the namespace to use. For example, the
            default ``eval_env=0`` uses the calling namespace. If you wish
            to use a "clean" environment set ``eval_env=-1``.

        Returns
        -------
        model : PHReg model instance
        '''
    def fit(self, groups: Incomplete | None = None, **args):
        """
        Fit a proportional hazards regression model.

        Parameters
        ----------
        groups : array_like
            Labels indicating groups of observations that may be
            dependent.  If present, the standard errors account for
            this dependence. Does not affect fitted values.

        Returns
        -------
        PHRegResults
            Returns a results instance.
        """
    def fit_regularized(self, method: str = 'elastic_net', alpha: float = 0.0, start_params: Incomplete | None = None, refit: bool = False, **kwargs):
        """
        Return a regularized fit to a linear regression model.

        Parameters
        ----------
        method : {'elastic_net'}
            Only the `elastic_net` approach is currently implemented.
        alpha : scalar or array_like
            The penalty weight.  If a scalar, the same penalty weight
            applies to all variables in the model.  If a vector, it
            must have the same length as `params`, and contains a
            penalty weight for each coefficient.
        start_params : array_like
            Starting values for `params`.
        refit : bool
            If True, the model is refit using only the variables that
            have non-zero coefficients in the regularized fit.  The
            refitted model is not regularized.
        **kwargs
            Additional keyword arguments used to fit the model.

        Returns
        -------
        PHRegResults
            Returns a results instance.

        Notes
        -----
        The penalty is the ``elastic net`` penalty, which is a
        combination of L1 and L2 penalties.

        The function that is minimized is:

        .. math::

            -loglike/n + alpha*((1-L1\\_wt)*|params|_2^2/2 + L1\\_wt*|params|_1)

        where :math:`|*|_1` and :math:`|*|_2` are the L1 and L2 norms.

        Post-estimation results are based on the same data used to
        select variables, hence may be subject to overfitting biases.

        The elastic_net method uses the following keyword arguments:

        maxiter : int
            Maximum number of iterations
        L1_wt  : float
            Must be in [0, 1].  The L1 penalty has weight L1_wt and the
            L2 penalty has weight 1 - L1_wt.
        cnvrg_tol : float
            Convergence threshold for line searches
        zero_tol : float
            Coefficients below this threshold are treated as zero.
        """
    def loglike(self, params):
        """
        Returns the log partial likelihood function evaluated at
        `params`.
        """
    def score(self, params):
        """
        Returns the score function evaluated at `params`.
        """
    def hessian(self, params):
        """
        Returns the Hessian matrix of the log partial likelihood
        function evaluated at `params`.
        """
    def breslow_loglike(self, params):
        """
        Returns the value of the log partial likelihood function
        evaluated at `params`, using the Breslow method to handle tied
        times.
        """
    def efron_loglike(self, params):
        """
        Returns the value of the log partial likelihood function
        evaluated at `params`, using the Efron method to handle tied
        times.
        """
    def breslow_gradient(self, params):
        """
        Returns the gradient of the log partial likelihood, using the
        Breslow method to handle tied times.
        """
    def efron_gradient(self, params):
        """
        Returns the gradient of the log partial likelihood evaluated
        at `params`, using the Efron method to handle tied times.
        """
    def breslow_hessian(self, params):
        """
        Returns the Hessian of the log partial likelihood evaluated at
        `params`, using the Breslow method to handle tied times.
        """
    def efron_hessian(self, params):
        """
        Returns the Hessian matrix of the partial log-likelihood
        evaluated at `params`, using the Efron method to handle tied
        times.
        """
    def robust_covariance(self, params):
        '''
        Returns a covariance matrix for the proportional hazards model
        regresion coefficient estimates that is robust to certain
        forms of model misspecification.

        Parameters
        ----------
        params : ndarray
            The parameter vector at which the covariance matrix is
            calculated.

        Returns
        -------
        The robust covariance matrix as a square ndarray.

        Notes
        -----
        This function uses the `groups` argument to determine groups
        within which observations may be dependent.  The covariance
        matrix is calculated using the Huber-White "sandwich" approach.
        '''
    def score_residuals(self, params):
        """
        Returns the score residuals calculated at a given vector of
        parameters.

        Parameters
        ----------
        params : ndarray
            The parameter vector at which the score residuals are
            calculated.

        Returns
        -------
        The score residuals, returned as a ndarray having the same
        shape as `exog`.

        Notes
        -----
        Observations in a stratum with no observed events have undefined
        score residuals, and contain NaN in the returned matrix.
        """
    def weighted_covariate_averages(self, params):
        """
        Returns the hazard-weighted average of covariate values for
        subjects who are at-risk at a particular time.

        Parameters
        ----------
        params : ndarray
            Parameter vector

        Returns
        -------
        averages : list of ndarrays
            averages[stx][i,:] is a row vector containing the weighted
            average values (for all the covariates) of at-risk
            subjects a the i^th largest observed failure time in
            stratum `stx`, using the hazard multipliers as weights.

        Notes
        -----
        Used to calculate leverages and score residuals.
        """
    def baseline_cumulative_hazard(self, params):
        """
        Estimate the baseline cumulative hazard and survival
        functions.

        Parameters
        ----------
        params : ndarray
            The model parameters.

        Returns
        -------
        A list of triples (time, hazard, survival) containing the time
        values and corresponding cumulative hazard and survival
        function values for each stratum.

        Notes
        -----
        Uses the Nelson-Aalen estimator.
        """
    def baseline_cumulative_hazard_function(self, params):
        """
        Returns a function that calculates the baseline cumulative
        hazard function for each stratum.

        Parameters
        ----------
        params : ndarray
            The model parameters.

        Returns
        -------
        A dict mapping stratum names to the estimated baseline
        cumulative hazard function.
        """
    def predict(self, params, exog: Incomplete | None = None, cov_params: Incomplete | None = None, endog: Incomplete | None = None, strata: Incomplete | None = None, offset: Incomplete | None = None, pred_type: str = 'lhr', pred_only: bool = False): ...
    def get_distribution(self, params, scale: float = 1.0, exog: Incomplete | None = None):
        """
        Returns a scipy distribution object corresponding to the
        distribution of uncensored endog (duration) values for each
        case.

        Parameters
        ----------
        params : array_like
            The proportional hazards model parameters.
        scale : float
            Present for compatibility, not used.
        exog : array_like
            A design matrix, defaults to model.exog.

        Returns
        -------
        A list of objects of type scipy.stats.distributions.rv_discrete

        Notes
        -----
        The distributions are obtained from a simple discrete estimate
        of the survivor function that puts all mass on the observed
        failure times within a stratum.
        """

class PHRegResults(base.LikelihoodModelResults):
    """
    Class to contain results of fitting a Cox proportional hazards
    survival model.

    PHregResults inherits from statsmodels.LikelihoodModelResults

    Parameters
    ----------
    See statsmodels.LikelihoodModelResults

    Attributes
    ----------
    model : class instance
        PHreg model instance that called fit.
    normalized_cov_params : ndarray
        The sampling covariance matrix of the estimates
    params : ndarray
        The coefficients of the fitted model.  Each coefficient is the
        log hazard ratio corresponding to a 1 unit difference in a
        single covariate while holding the other covariates fixed.
    bse : ndarray
        The standard errors of the fitted parameters.

    See Also
    --------
    statsmodels.LikelihoodModelResults
    """
    covariance_type: Incomplete
    df_resid: Incomplete
    df_model: Incomplete
    def __init__(self, model, params, cov_params, scale: float = 1.0, covariance_type: str = 'naive') -> None: ...
    def standard_errors(self):
        """
        Returns the standard errors of the parameter estimates.
        """
    def bse(self):
        """
        Returns the standard errors of the parameter estimates.
        """
    def get_distribution(self):
        """
        Returns a scipy distribution object corresponding to the
        distribution of uncensored endog (duration) values for each
        case.

        Returns
        -------
        A list of objects of type scipy.stats.distributions.rv_discrete

        Notes
        -----
        The distributions are obtained from a simple discrete estimate
        of the survivor function that puts all mass on the observed
        failure times within a stratum.
        """
    def predict(self, endog: Incomplete | None = None, exog: Incomplete | None = None, strata: Incomplete | None = None, offset: Incomplete | None = None, transform: bool = True, pred_type: str = 'lhr'): ...
    def weighted_covariate_averages(self):
        """
        The average covariate values within the at-risk set at each
        event time point, weighted by hazard.
        """
    def score_residuals(self):
        """
        A matrix containing the score residuals.
        """
    def baseline_cumulative_hazard(self):
        """
        A list (corresponding to the strata) containing the baseline
        cumulative hazard function evaluated at the event points.
        """
    def baseline_cumulative_hazard_function(self):
        """
        A list (corresponding to the strata) containing function
        objects that calculate the cumulative hazard function.
        """
    def schoenfeld_residuals(self):
        """
        A matrix containing the Schoenfeld residuals.

        Notes
        -----
        Schoenfeld residuals for censored observations are set to zero.
        """
    def martingale_residuals(self):
        """
        The martingale residuals.
        """
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """
        Summarize the proportional hazards regression results.

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Names for the exogenous variables, default is `x#` for ## in p the
            number of regressors. Must match the number of parameters in
            the model
        title : str, optional
            Title for the top table. If not None, then this replaces
            the default title
        alpha : float
            significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be
            printed or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary2.Summary : class to hold summary results
        """

class rv_discrete_float:
    """
    A class representing a collection of discrete distributions.

    Parameters
    ----------
    xk : 2d array_like
        The support points, should be non-decreasing within each
        row.
    pk : 2d array_like
        The probabilities, should sum to one within each row.

    Notes
    -----
    Each row of `xk`, and the corresponding row of `pk` describe a
    discrete distribution.

    `xk` and `pk` should both be two-dimensional ndarrays.  Each row
    of `pk` should sum to 1.

    This class is used as a substitute for scipy.distributions.
    rv_discrete, since that class does not allow non-integer support
    points, or vectorized operations.

    Only a limited number of methods are implemented here compared to
    the other scipy distribution classes.
    """
    xk: Incomplete
    pk: Incomplete
    cpk: Incomplete
    def __init__(self, xk, pk) -> None: ...
    def rvs(self, n: Incomplete | None = None):
        """
        Returns a random sample from the discrete distribution.

        A vector is returned containing a single draw from each row of
        `xk`, using the probabilities of the corresponding row of `pk`

        Parameters
        ----------
        n : not used
            Present for signature compatibility
        """
    def mean(self):
        """
        Returns a vector containing the mean values of the discrete
        distributions.

        A vector is returned containing the mean value of each row of
        `xk`, using the probabilities in the corresponding row of
        `pk`.
        """
    def var(self):
        """
        Returns a vector containing the variances of the discrete
        distributions.

        A vector is returned containing the variance for each row of
        `xk`, using the probabilities in the corresponding row of
        `pk`.
        """
    def std(self):
        """
        Returns a vector containing the standard deviations of the
        discrete distributions.

        A vector is returned containing the standard deviation for
        each row of `xk`, using the probabilities in the corresponding
        row of `pk`.
        """
