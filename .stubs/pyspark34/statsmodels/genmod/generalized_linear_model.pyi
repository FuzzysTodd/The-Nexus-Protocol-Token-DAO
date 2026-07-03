import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.base._prediction_inference import PredictionResultsMean as PredictionResultsMean

__all__ = ['GLM', 'PredictionResultsMean']

class _ModuleVariable:
    @property
    def use_bic_llf(self): ...
    def set_use_bic_llf(self, val) -> None: ...

class GLM(base.LikelihoodModel):
    __doc__: Incomplete
    freq_weights: Incomplete
    var_weights: Incomplete
    nobs: Incomplete
    n_trials: Incomplete
    scaletype: Incomplete
    def __init__(self, endog, exog, family: Incomplete | None = None, offset: Incomplete | None = None, exposure: Incomplete | None = None, freq_weights: Incomplete | None = None, var_weights: Incomplete | None = None, missing: str = 'none', **kwargs) -> None: ...
    df_model: Incomplete
    wnobs: Incomplete
    df_resid: Incomplete
    def initialize(self) -> None:
        """
        Initialize a generalized linear model.
        """
    def loglike_mu(self, mu, scale: float = 1.0):
        """
        Evaluate the log-likelihood for a generalized linear model.
        """
    def loglike(self, params, scale: Incomplete | None = None):
        """
        Evaluate the log-likelihood for a generalized linear model.
        """
    def score_obs(self, params, scale: Incomplete | None = None):
        """score first derivative of the loglikelihood for each observation.

        Parameters
        ----------
        params : ndarray
            Parameter at which score is evaluated.
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.

        Returns
        -------
        score_obs : ndarray, 2d
            The first derivative of the loglikelihood function evaluated at
            params for each observation.
        """
    def score(self, params, scale: Incomplete | None = None):
        """score, first derivative of the loglikelihood function

        Parameters
        ----------
        params : ndarray
            Parameter at which score is evaluated.
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.

        Returns
        -------
        score : ndarray_1d
            The first derivative of the loglikelihood function calculated as
            the sum of `score_obs`
        """
    def score_factor(self, params, scale: Incomplete | None = None):
        """weights for score for each observation

        This can be considered as score residuals.

        Parameters
        ----------
        params : ndarray
            parameter at which score is evaluated
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.

        Returns
        -------
        score_factor : ndarray_1d
            A 1d weight vector used in the calculation of the score_obs.
            The score_obs are obtained by `score_factor[:, None] * exog`
        """
    def hessian_factor(self, params, scale: Incomplete | None = None, observed: bool = True):
        """Weights for calculating Hessian

        Parameters
        ----------
        params : ndarray
            parameter at which Hessian is evaluated
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.
        observed : bool
            If True, then the observed Hessian is returned. If false then the
            expected information matrix is returned.

        Returns
        -------
        hessian_factor : ndarray, 1d
            A 1d weight vector used in the calculation of the Hessian.
            The hessian is obtained by `(exog.T * hessian_factor).dot(exog)`
        """
    def hessian(self, params, scale: Incomplete | None = None, observed: Incomplete | None = None):
        """Hessian, second derivative of loglikelihood function

        Parameters
        ----------
        params : ndarray
            parameter at which Hessian is evaluated
        scale : None or float
            If scale is None, then the default scale will be calculated.
            Default scale is defined by `self.scaletype` and set in fit.
            If scale is not None, then it is used as a fixed scale.
        observed : bool
            If True, then the observed Hessian is returned (default).
            If False, then the expected information matrix is returned.

        Returns
        -------
        hessian : ndarray
            Hessian, i.e. observed information, or expected information matrix.
        """
    def information(self, params, scale: Incomplete | None = None):
        """
        Fisher information matrix.
        """
    def score_test(self, params_constrained, k_constraints: Incomplete | None = None, exog_extra: Incomplete | None = None, observed: bool = True):
        """score test for restrictions or for omitted variables

        The covariance matrix for the score is based on the Hessian, i.e.
        observed information matrix or optionally on the expected information
        matrix..

        Parameters
        ----------
        params_constrained : array_like
            estimated parameter of the restricted model. This can be the
            parameter estimate for the current when testing for omitted
            variables.
        k_constraints : int or None
            Number of constraints that were used in the estimation of params
            restricted relative to the number of exog in the model.
            This must be provided if no exog_extra are given. If exog_extra is
            not None, then k_constraints is assumed to be zero if it is None.
        exog_extra : None or array_like
            Explanatory variables that are jointly tested for inclusion in the
            model, i.e. omitted variables.
        observed : bool
            If True, then the observed Hessian is used in calculating the
            covariance matrix of the score. If false then the expected
            information matrix is used.

        Returns
        -------
        chi2_stat : float
            chisquare statistic for the score test
        p-value : float
            P-value of the score test based on the chisquare distribution.
        df : int
            Degrees of freedom used in the p-value calculation. This is equal
            to the number of constraints.

        Notes
        -----
        not yet verified for case with scale not equal to 1.
        """
    def estimate_scale(self, mu):
        """
        Estimate the dispersion/scale.

        Type of scale can be chose in the fit method.

        Parameters
        ----------
        mu : ndarray
            mu is the mean response estimate

        Returns
        -------
        Estimate of scale

        Notes
        -----
        The default scale for Binomial, Poisson and Negative Binomial
        families is 1.  The default for the other families is Pearson's
        Chi-Square estimate.

        See Also
        --------
        statsmodels.genmod.generalized_linear_model.GLM.fit
        """
    def estimate_tweedie_power(self, mu, method: str = 'brentq', low: float = 1.01, high: float = 5.0):
        """
        Tweedie specific function to estimate scale and the variance parameter.
        The variance parameter is also referred to as p, xi, or shape.

        Parameters
        ----------
        mu : array_like
            Fitted mean response variable
        method : str, defaults to 'brentq'
            Scipy optimizer used to solve the Pearson equation. Only brentq
            currently supported.
        low : float, optional
            Low end of the bracketing interval [a,b] to be used in the search
            for the power. Defaults to 1.01.
        high : float, optional
            High end of the bracketing interval [a,b] to be used in the search
            for the power. Defaults to 5.

        Returns
        -------
        power : float
            The estimated shape or power.
        """
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None):
        """
        Return predicted values for a design matrix

        Parameters
        ----------
        params : array_like
            Parameters / coefficients of a GLM.
        exog : array_like, optional
            Design / exogenous data. Is exog is None, model exog is used.
        exposure : array_like, optional
            Exposure time values, only can be used with the log link
            function.  See notes for details.
        offset : array_like, optional
            Offset values.  See notes for details.
        which : 'mean', 'linear', 'var'(optional)
            Statitistic to predict. Default is 'mean'.

            - 'mean' returns the conditional expectation of endog E(y | x),
              i.e. inverse of the model's link function of linear predictor.
            - 'linear' returns the linear predictor of the mean function.
            - 'var_unscaled' variance of endog implied by the likelihood model.
              This does not include scale or var_weights.

        linear : bool
            The ``linear` keyword is deprecated and will be removed,
            use ``which`` keyword instead.
            If True, returns the linear predicted values.  If False or None,
            then the statistic specified by ``which`` will be returned.


        Returns
        -------
        An array of fitted values

        Notes
        -----
        Any `exposure` and `offset` provided here take precedence over
        the `exposure` and `offset` used in the model fit.  If `exog`
        is passed as an argument here, then any `exposure` and
        `offset` values in the fit will be ignored.

        Exposure values must be strictly positive.
        """
    def get_distribution(self, params, scale: Incomplete | None = None, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, var_weights: float = 1.0, n_trials: float = 1.0):
        """
        Return a instance of the predictive distribution.

        Parameters
        ----------
        params : array_like
            The model parameters.
        scale : scalar
            The scale parameter.
        exog : array_like
            The predictor variable matrix.
        offset : array_like or None
            Offset variable for predicted mean.
        exposure : array_like or None
            Log(exposure) will be added to the linear prediction.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is None.
        n_trials : int
            Number of trials for the binomial distribution. The default is 1
            which corresponds to a Bernoulli random variable.

        Returns
        -------
        gen
            Instance of a scipy frozen distribution based on estimated
            parameters.
            Use the ``rvs`` method to generate random values.

        Notes
        -----
        Due to the behavior of ``scipy.stats.distributions objects``, the
        returned random number generator must be called with ``gen.rvs(n)``
        where ``n`` is the number of observations in the data set used
        to fit the model.  If any other value is used for ``n``, misleading
        results will be produced.
        """
    def fit(self, start_params: Incomplete | None = None, maxiter: int = 100, method: str = 'IRLS', tol: float = 1e-08, scale: Incomplete | None = None, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, full_output: bool = True, disp: bool = False, max_start_irls: int = 3, **kwargs):
        """
        Fits a generalized linear model for a given family.

        Parameters
        ----------
        start_params : array_like, optional
            Initial guess of the solution for the loglikelihood maximization.
            The default is family-specific and is given by the
            ``family.starting_mu(endog)``. If start_params is given then the
            initial mean will be calculated as ``np.dot(exog, start_params)``.
        maxiter : int, optional
            Default is 100.
        method : str
            Default is 'IRLS' for iteratively reweighted least squares.
            Otherwise gradient optimization is used.
        tol : float
            Convergence tolerance.  Default is 1e-8.
        scale : str or float, optional
            `scale` can be 'X2', 'dev', or a float
            The default value is None, which uses `X2` for Gamma, Gaussian,
            and Inverse Gaussian.
            `X2` is Pearson's chi-square divided by `df_resid`.
            The default is 1 for the Binomial and Poisson families.
            `dev` is the deviance divided by df_resid
        cov_type : str
            The type of parameter estimate covariance matrix to compute.
        cov_kwds : dict-like
            Extra arguments for calculating the covariance of the parameter
            estimates.
        use_t : bool
            If True, the Student t-distribution is used for inference.
        full_output : bool, optional
            Set to True to have all available output in the Results object's
            mle_retvals attribute. The output is dependent on the solver.
            See LikelihoodModelResults notes section for more information.
            Not used if methhod is IRLS.
        disp : bool, optional
            Set to True to print convergence messages.  Not used if method is
            IRLS.
        max_start_irls : int
            The number of IRLS iterations used to obtain starting
            values for gradient optimization.  Only relevant if
            `method` is set to something other than 'IRLS'.
        atol : float, optional
            (available with IRLS fits) The absolute tolerance criterion that
            must be satisfied. Defaults to ``tol``. Convergence is attained
            when: :math:`rtol * prior + atol > abs(current - prior)`
        rtol : float, optional
            (available with IRLS fits) The relative tolerance criterion that
            must be satisfied. Defaults to 0 which means ``rtol`` is not used.
            Convergence is attained when:
            :math:`rtol * prior + atol > abs(current - prior)`
        tol_criterion : str, optional
            (available with IRLS fits) Defaults to ``'deviance'``. Can
            optionally be ``'params'``.
        wls_method : str, optional
            (available with IRLS fits) options are 'lstsq', 'pinv' and 'qr'
            specifies which linear algebra function to use for the irls
            optimization. Default is `lstsq` which uses the same underlying
            svd based approach as 'pinv', but is faster during iterations.
            'lstsq' and 'pinv' regularize the estimate in singular and
            near-singular cases by truncating small singular values based
            on `rcond` of the respective numpy.linalg function. 'qr' is
            only valid for cases that are not singular nor near-singular.
        optim_hessian : {'eim', 'oim'}, optional
            (available with scipy optimizer fits) When 'oim'--the default--the
            observed Hessian is used in fitting. 'eim' is the expected Hessian.
            This may provide more stable fits, but adds assumption that the
            Hessian is correctly specified.

        Notes
        -----
        If method is 'IRLS', then an additional keyword 'attach_wls' is
        available. This is currently for internal use only and might change
        in future versions. If attach_wls' is true, then the final WLS
        instance of the IRLS iteration is attached to the results instance
        as `results_wls` attribute.
        """
    mu: Incomplete
    scale: Incomplete
    def fit_regularized(self, method: str = 'elastic_net', alpha: float = 0.0, start_params: Incomplete | None = None, refit: bool = False, opt_method: str = 'bfgs', **kwargs):
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
        opt_method : string
            The method used for numerical optimization.
        **kwargs
            Additional keyword arguments used when fitting the model.

        Returns
        -------
        GLMResults
            An array or a GLMResults object, same type returned by `fit`.

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
            Convergence threshold for maximum parameter change after
            one sweep through all coefficients.
        zero_tol : float
            Coefficients below this threshold are treated as zero.
        """
    def fit_constrained(self, constraints, start_params: Incomplete | None = None, **fit_kwds):
        """fit the model subject to linear equality constraints

        The constraints are of the form   `R params = q`
        where R is the constraint_matrix and q is the vector of
        constraint_values.

        The estimation creates a new model with transformed design matrix,
        exog, and converts the results back to the original parameterization.


        Parameters
        ----------
        constraints : formula expression or tuple
            If it is a tuple, then the constraint needs to be given by two
            arrays (constraint_matrix, constraint_value), i.e. (R, q).
            Otherwise, the constraints can be given as strings or list of
            strings.
            see t_test for details
        start_params : None or array_like
            starting values for the optimization. `start_params` needs to be
            given in the original parameter space and are internally
            transformed.
        **fit_kwds : keyword arguments
            fit_kwds are used in the optimization of the transformed model.

        Returns
        -------
        results : Results instance
        """

class GLMResults(base.LikelihoodModelResults):
    """
    Class to contain GLM results.

    GLMResults inherits from statsmodels.LikelihoodModelResults

    Attributes
    ----------
    df_model : float
        See GLM.df_model
    df_resid : float
        See GLM.df_resid
    fit_history : dict
        Contains information about the iterations. Its keys are `iterations`,
        `deviance` and `params`.
    model : class instance
        Pointer to GLM model instance that called fit.
    nobs : float
        The number of observations n.
    normalized_cov_params : ndarray
        See GLM docstring
    params : ndarray
        The coefficients of the fitted model.  Note that interpretation
        of the coefficients often depends on the distribution family and the
        data.
    pvalues : ndarray
        The two-tailed p-values for the parameters.
    scale : float
        The estimate of the scale / dispersion for the model fit.
        See GLM.fit and GLM.estimate_scale for more information.
    stand_errors : ndarray
        The standard errors of the fitted GLM.   #TODO still named bse

    See Also
    --------
    statsmodels.base.model.LikelihoodModelResults
    """
    family: Incomplete
    nobs: Incomplete
    df_resid: Incomplete
    df_model: Incomplete
    use_t: bool
    cov_type: str
    cov_kwds: Incomplete
    def __init__(self, model, params, normalized_cov_params, scale, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None) -> None: ...
    def resid_response(self):
        """
        Response residuals.  The response residuals are defined as
        `endog` - `fittedvalues`
        """
    def resid_pearson(self):
        """
        Pearson residuals.  The Pearson residuals are defined as
        (`endog` - `mu`)/sqrt(VAR(`mu`)) where VAR is the distribution
        specific variance function.  See statsmodels.families.family and
        statsmodels.families.varfuncs for more information.
        """
    def resid_working(self):
        """
        Working residuals.  The working residuals are defined as
        `resid_response`/link'(`mu`).  See statsmodels.family.links for the
        derivatives of the link functions.  They are defined analytically.
        """
    def resid_anscombe(self):
        """
        Anscombe residuals.  See statsmodels.families.family for distribution-
        specific Anscombe residuals. Currently, the unscaled residuals are
        provided. In a future version, the scaled residuals will be provided.
        """
    def resid_anscombe_scaled(self):
        """
        Scaled Anscombe residuals.  See statsmodels.families.family for
        distribution-specific Anscombe residuals.
        """
    def resid_anscombe_unscaled(self):
        """
        Unscaled Anscombe residuals.  See statsmodels.families.family for
        distribution-specific Anscombe residuals.
        """
    def resid_deviance(self):
        """
        Deviance residuals.  See statsmodels.families.family for distribution-
        specific deviance residuals.
        """
    def pearson_chi2(self):
        """
        Pearson's Chi-Squared statistic is defined as the sum of the squares
        of the Pearson residuals.
        """
    def fittedvalues(self):
        """
        The estimated mean response.

        This is the value of the inverse of the link function at
        lin_pred, where lin_pred is the linear predicted value
        obtained by multiplying the design matrix by the coefficient
        vector.
        """
    def mu(self):
        """
        See GLM docstring.
        """
    def null(self):
        """
        Fitted values of the null model
        """
    def deviance(self):
        """
        See statsmodels.families.family for the distribution-specific deviance
        functions.
        """
    def null_deviance(self):
        """The value of the deviance function for the model fit with a constant
        as the only regressor."""
    def llnull(self):
        """
        Log-likelihood of the model fit with a constant as the only regressor
        """
    def llf_scaled(self, scale: Incomplete | None = None):
        """
        Return the log-likelihood at the given scale, using the
        estimated scale if the provided scale is None.  In the Gaussian
        case with linear link, the concentrated log-likelihood is
        returned.
        """
    def llf(self):
        """
        Value of the loglikelihood function evalued at params.
        See statsmodels.families.family for distribution-specific
        loglikelihoods.  The result uses the concentrated
        log-likelihood if the family is Gaussian and the link is linear,
        otherwise it uses the non-concentrated log-likelihood evaluated
        at the estimated scale.
        """
    def pseudo_rsquared(self, kind: str = 'cs'):
        '''
        Pseudo R-squared

        Cox-Snell likelihood ratio pseudo R-squared is valid for both discrete
        and continuous data. McFadden\'s pseudo R-squared is only valid for
        discrete data.

        Cox & Snell\'s pseudo-R-squared:  1 - exp((llnull - llf)*(2/nobs))

        McFadden\'s pseudo-R-squared: 1 - (llf / llnull)

        Parameters
        ----------
        kind : P"cs", "mcf"}
            Type of pseudo R-square to return

        Returns
        -------
        float
            Pseudo R-squared
        '''
    def aic(self):
        """
        Akaike Information Criterion
        -2 * `llf` + 2 * (`df_model` + 1)
        """
    @property
    def bic(self):
        """
        Bayes Information Criterion

        `deviance` - `df_resid` * log(`nobs`)

        .. warning::

            The current definition is based on the deviance rather than the
            log-likelihood. This is not consistent with the AIC definition,
            and after 0.13 both will make use of the log-likelihood definition.

        Notes
        -----
        The log-likelihood version is defined
        -2 * `llf` + (`df_model` + 1)*log(n)
        """
    def bic_deviance(self):
        """
        Bayes Information Criterion

        Based on the deviance,
        `deviance` - `df_resid` * log(`nobs`)
        """
    def bic_llf(self):
        """
        Bayes Information Criterion

        Based on the log-likelihood,
        -2 * `llf` + log(n) * (`df_model` + 1)
        """
    def info_criteria(self, crit, scale: Incomplete | None = None, dk_params: int = 0):
        """Return an information criterion for the model.

        Parameters
        ----------
        crit : string
            One of 'aic', 'bic', or 'qaic'.
        scale : float
            The scale parameter estimated using the parent model,
            used only for qaic.
        dk_params : int or float
            Correction to the number of parameters used in the information
            criterion. By default, only mean parameters are included, the
            scale parameter is not included in the parameter count.
            Use ``dk_params=1`` to include scale in the parameter count.

        Returns
        -------
        Value of information criterion.

        Notes
        -----
        The quasi-Akaike Information criterion (qaic) is -2 *
        `llf`/`scale` + 2 * (`df_model` + 1).  It may not give
        meaningful results except for Poisson and related models.

        The QAIC (ic_type='qaic') must be evaluated with a provided
        scale parameter.  Two QAIC values are only comparable if they
        are calculated using the same scale parameter.  The scale
        parameter should be estimated using the largest model among
        all models being compared.

        References
        ----------
        Burnham KP, Anderson KR (2002). Model Selection and Multimodel
        Inference; Springer New York.
        """
    def get_prediction(self, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, transform: bool = True, which: Incomplete | None = None, linear: Incomplete | None = None, average: bool = False, agg_weights: Incomplete | None = None, row_labels: Incomplete | None = None):
        '''
    Compute prediction results for GLM compatible models.

    Options and return class depend on whether "which" is None or not.

    Parameters
    ----------
    exog : array_like, optional
        The values for which you want to predict.
    exposure : array_like, optional
        Exposure time values, only can be used with the log link
        function.
    offset : array_like, optional
        Offset values.
    transform : bool, optional
        If the model was fit via a formula, do you want to pass
        exog through the formula. Default is True. E.g., if you fit
        a model y ~ log(x1) + log(x2), and transform is True, then
        you can pass a data structure that contains x1 and x2 in
        their original form. Otherwise, you\'d need to log the data
        first.
    which : \'mean\', \'linear\', \'var\'(optional)
        Statitistic to predict. Default is \'mean\'.
        If which is None, then the deprecated keyword "linear" applies.
        If which is not None, then a generic Prediction results class will
        be returned. Some options are only available if which is not None.
        See notes.

        - \'mean\' returns the conditional expectation of endog E(y | x),
          i.e. inverse of the model\'s link function of linear predictor.
        - \'linear\' returns the linear predictor of the mean function.
        - \'var_unscaled\' variance of endog implied by the likelihood model.
          This does not include scale or var_weights.

    linear : bool
        The ``linear` keyword is deprecated and will be removed,
        use ``which`` keyword instead.
        If which is None, then the linear keyword is used, otherwise it will
        be ignored.
        If True and which is None, the linear predicted values are returned.
        If False or None, then the statistic specified by ``which`` will be
        returned.
    average : bool
        Keyword is only used if ``which`` is not None.
        If average is True, then the mean prediction is computed, that is,
        predictions are computed for individual exog and then the average
        over observation is used.
        If average is False, then the results are the predictions for all
        observations, i.e. same length as ``exog``.
    agg_weights : ndarray, optional
        Keyword is only used if ``which`` is not None.
        Aggregation weights, only used if average is True.
    row_labels : list of str or None
        If row_lables are provided, then they will replace the generated
        labels.

    Returns
    -------
    prediction_results : instance of a PredictionResults class.
        The prediction results instance contains prediction and prediction
        variance and can on demand calculate confidence intervals and summary
        tables for the prediction of the mean and of new observations.
        The Results class of the return depends on the value of ``which``.

    See Also
    --------
    GLM.predict
    GLMResults.predict

    Notes
    -----
    Changes in statsmodels 0.14: The ``which`` keyword has been added.
    If ``which`` is None, then the behavior is the same as in previous
    versions, and returns the mean and linear prediction results.
    If the ``which`` keyword is not None, then a generic prediction results
    class is returned and is not backwards compatible with the old prediction
    results class, e.g. column names of summary_frame differs.
    There are more choices for the returned predicted statistic using
    ``which``. More choices will be added in the next release.
    Two additional keyword, average and agg_weights options are now also
    available if ``which`` is not None.
    In a future version ``which`` will become not None and the backwards
    compatible prediction results class will be removed.

    '''
    def score_test(self, exog_extra: Incomplete | None = None, params_constrained: Incomplete | None = None, hypothesis: str = 'joint', cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, k_constraints: Incomplete | None = None, observed: bool = True): ...
    def get_hat_matrix_diag(self, observed: bool = True):
        """
        Compute the diagonal of the hat matrix

        Parameters
        ----------
        observed : bool
            If true, then observed hessian is used in the hat matrix
            computation. If false, then the expected hessian is used.
            In the case of a canonical link function both are the same.

        Returns
        -------
        hat_matrix_diag : ndarray
            The diagonal of the hat matrix computed from the observed
            or expected hessian.
        """
    def get_influence(self, observed: bool = True):
        """
        Get an instance of GLMInfluence with influence and outlier measures

        Parameters
        ----------
        observed : bool
            If true, then observed hessian is used in the hat matrix
            computation. If false, then the expected hessian is used.
            In the case of a canonical link function both are the same.

        Returns
        -------
        infl : GLMInfluence instance
            The instance has methods to calculate the main influence and
            outlier measures as attributes.

        See Also
        --------
        statsmodels.stats.outliers_influence.GLMInfluence
        """
    def get_distribution(self, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, var_weights: float = 1.0, n_trials: float = 1.0):
        """
        Return a instance of the predictive distribution.

        Parameters
        ----------
        scale : scalar
            The scale parameter.
        exog : array_like
            The predictor variable matrix.
        offset : array_like or None
            Offset variable for predicted mean.
        exposure : array_like or None
            Log(exposure) will be added to the linear prediction.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is None.
        n_trials : int
            Number of trials for the binomial distribution. The default is 1
            which corresponds to a Bernoulli random variable.

        Returns
        -------
        gen
            Instance of a scipy frozen distribution based on estimated
            parameters.
            Use the ``rvs`` method to generate random values.

        Notes
        -----
        Due to the behavior of ``scipy.stats.distributions objects``, the
        returned random number generator must be called with ``gen.rvs(n)``
        where ``n`` is the number of observations in the data set used
        to fit the model.  If any other value is used for ``n``, misleading
        results will be produced.
        """
    def remove_data(self) -> None: ...
    def plot_added_variable(self, focus_exog, resid_type: Incomplete | None = None, use_glm_weights: bool = True, fit_kwargs: Incomplete | None = None, ax: Incomplete | None = None): ...
    def plot_partial_residuals(self, focus_exog, ax: Incomplete | None = None): ...
    def plot_ceres_residuals(self, focus_exog, frac: float = 0.66, cond_means: Incomplete | None = None, ax: Incomplete | None = None): ...
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """
        Summarize the Regression Results

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Names for the exogenous variables, default is `var_#` for ## in
            the number of regressors. Must match the number of parameters in
            the model
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float
            significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : class to hold summary results
        """
    method: str
    def summary2(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05, float_format: str = '%.4f'):
        """Experimental summary for regression Results

        Parameters
        ----------
        yname : str
            Name of the dependent variable (optional)
        xname : list[str], optional
            Names for the exogenous variables, default is `var_#` for ## in
            the number of regressors. Must match the number of parameters in
            the model
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float
            significance level for the confidence intervals
        float_format : str
            print format for floats in parameters summary

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary2.Summary : class to hold summary results
        """

class GLMResultsWrapper(lm.RegressionResultsWrapper): ...
