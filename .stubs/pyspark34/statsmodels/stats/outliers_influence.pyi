from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.compat.python import lzip as lzip
from statsmodels.regression.linear_model import OLS as OLS
from statsmodels.stats.multitest import multipletests as multipletests
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.tools import maybe_unwrap_results as maybe_unwrap_results

def outlier_test(model_results, method: str = 'bonf', alpha: float = 0.05, labels: Incomplete | None = None, order: bool = False, cutoff: Incomplete | None = None):
    """
    Outlier Tests for RegressionResults instances.

    Parameters
    ----------
    model_results : RegressionResults
        Linear model results
    method : str
        - `bonferroni` : one-step correction
        - `sidak` : one-step correction
        - `holm-sidak` :
        - `holm` :
        - `simes-hochberg` :
        - `hommel` :
        - `fdr_bh` : Benjamini/Hochberg
        - `fdr_by` : Benjamini/Yekutieli
        See `statsmodels.stats.multitest.multipletests` for details.
    alpha : float
        familywise error rate
    labels : None or array_like
        If `labels` is not None, then it will be used as index to the
        returned pandas DataFrame. See also Returns below
    order : bool
        Whether or not to order the results by the absolute value of the
        studentized residuals. If labels are provided they will also be sorted.
    cutoff : None or float in [0, 1]
        If cutoff is not None, then the return only includes observations with
        multiple testing corrected p-values strictly below the cutoff. The
        returned array or dataframe can be empty if there are no outlier
        candidates at the specified cutoff.

    Returns
    -------
    table : ndarray or DataFrame
        Returns either an ndarray or a DataFrame if labels is not None.
        Will attempt to get labels from model_results if available. The
        columns are the Studentized residuals, the unadjusted p-value,
        and the corrected p-value according to method.

    Notes
    -----
    The unadjusted p-value is stats.t.sf(abs(resid), df) where
    df = df_resid - 1.
    """
def reset_ramsey(res, degree: int = 5):
    """Ramsey's RESET specification test for linear models

    This is a general specification test, for additional non-linear effects
    in a model.

    Parameters
    ----------
    degree : int
        Maximum power to include in the RESET test.  Powers 0 and 1 are
        excluded, so that degree tests powers 2, ..., degree of the fitted
        values.

    Notes
    -----
    The test fits an auxiliary OLS regression where the design matrix, exog,
    is augmented by powers 2 to degree of the fitted values. Then it performs
    an F-test whether these additional terms are significant.

    If the p-value of the f-test is below a threshold, e.g. 0.1, then this
    indicates that there might be additional non-linear effects in the model
    and that the linear model is mis-specified.

    References
    ----------
    https://en.wikipedia.org/wiki/Ramsey_RESET_test
    """
def variance_inflation_factor(exog, exog_idx):
    """
    Variance inflation factor, VIF, for one exogenous variable

    The variance inflation factor is a measure for the increase of the
    variance of the parameter estimates if an additional variable, given by
    exog_idx is added to the linear regression. It is a measure for
    multicollinearity of the design matrix, exog.

    One recommendation is that if VIF is greater than 5, then the explanatory
    variable given by exog_idx is highly collinear with the other explanatory
    variables, and the parameter estimates will have large standard errors
    because of this.

    Parameters
    ----------
    exog : {ndarray, DataFrame}
        design matrix with all explanatory variables, as for example used in
        regression
    exog_idx : int
        index of the exogenous variable in the columns of exog

    Returns
    -------
    float
        variance inflation factor

    Notes
    -----
    This function does not save the auxiliary regression.

    See Also
    --------
    xxx : class for regression diagnostics  TODO: does not exist yet

    References
    ----------
    https://en.wikipedia.org/wiki/Variance_inflation_factor
    """

class _BaseInfluenceMixin:
    """common methods between OLSInfluence and MLE/GLMInfluence
    """
    def plot_influence(self, external: Incomplete | None = None, alpha: float = 0.05, criterion: str = 'cooks', size: int = 48, plot_alpha: float = 0.75, ax: Incomplete | None = None, **kwargs): ...
    def plot_index(self, y_var: str = 'cooks', threshold: Incomplete | None = None, title: Incomplete | None = None, ax: Incomplete | None = None, idx: Incomplete | None = None, **kwds):
        '''index plot for influence attributes

        Parameters
        ----------
        y_var : str
            Name of attribute or shortcut for predefined attributes that will
            be plotted on the y-axis.
        threshold : None or float
            Threshold for adding annotation with observation labels.
            Observations for which the absolute value of the y_var is larger
            than the threshold will be annotated. Set to a negative number to
            label all observations or to a large number to have no annotation.
        title : str
            If provided, the title will replace the default "Index Plot" title.
        ax : matplolib axis instance
            The plot will be added to the `ax` if provided, otherwise a new
            figure is created.
        idx : {None, int}
            Some attributes require an additional index to select the y-var.
            In dfbetas this refers to the column indes.
        kwds : optional keywords
            Keywords will be used in the call to matplotlib scatter function.
        '''

class MLEInfluence(_BaseInfluenceMixin):
    """Global Influence and outlier measures (experimental)

    Parameters
    ----------
    results : instance of results class
        This only works for model and results classes that have the necessary
        helper methods.
    other arguments :
        Those are only available to override default behavior and are used
        instead of the corresponding attribute of the results class.
        By default resid_pearson is used as resid.

    Attributes
    ----------
    hat_matrix_diag (hii) : This is the generalized leverage computed as the
        local derivative of fittedvalues (predicted mean) with respect to the
        observed response for each observation.
        Not available for ZeroInflated models because of nondifferentiability.
    d_params : Change in parameters computed with one Newton step using the
        full Hessian corrected by division by (1 - hii).
        If hat_matrix_diag is not available, then the division by (1 - hii) is
        not included.
    dbetas : change in parameters divided by the standard error of parameters
        from the full model results, ``bse``.
    cooks_distance : quadratic form for change in parameters weighted by
        ``cov_params`` from the full model divided by the number of variables.
        It includes p-values based on the F-distribution which are only
        approximate outside of linear Gaussian models.
    resid_studentized : In the general MLE case resid_studentized are
        computed from the score residuals scaled by hessian factor and
        leverage. This does not use ``cov_params``.
    d_fittedvalues : local change of expected mean given the change in the
        parameters as computed in ``d_params``.
    d_fittedvalues_scaled : same as d_fittedvalues but scaled by the standard
        errors of a predicted mean of the response.
    params_one : is the one step parameter estimate computed as ``params``
        from the full sample minus ``d_params``.

    Notes
    -----
    MLEInfluence uses generic definitions based on maximum likelihood models.

    MLEInfluence produces the same results as GLMInfluence for canonical
    links (verified for GLM Binomial, Poisson and Gaussian). There will be
    some differences for non-canonical links or if a robust cov_type is used.
    For example, the generalized leverage differs from the definition of the
    GLM hat matrix in the case of Probit, which corresponds to family
    Binomial with a non-canonical link.

    The extension to non-standard models, e.g. multi-link model like
    BetaModel and the ZeroInflated models is still experimental and might still
    change.
    Additonally, ZeroInflated and some threshold models have a
    nondifferentiability in the generalized leverage. How this case is treated
    might also change.

    Warning: This does currently not work for constrained or penalized models,
    e.g. models estimated with fit_constrained or fit_regularized.

    This has not yet been tested for correctness when offset or exposure
    are used, although they should be supported by the code.

    status: experimental,
    This class will need changes to support different kinds of models, e.g.
    extra parameters in discrete.NegativeBinomial or two-part models like
    ZeroInflatedPoisson.
    """
    results: Incomplete
    k_params: Incomplete
    endog: Incomplete
    exog: Incomplete
    scale: Incomplete
    resid: Incomplete
    cov_params: Incomplete
    model_class: Incomplete
    hessian: Incomplete
    score_obs: Incomplete
    def __init__(self, results, resid: Incomplete | None = None, endog: Incomplete | None = None, exog: Incomplete | None = None, hat_matrix_diag: Incomplete | None = None, cov_params: Incomplete | None = None, scale: Incomplete | None = None) -> None: ...
    def hat_matrix_diag(self):
        """Diagonal of the generalized leverage

        This is the analogue of the hat matrix diagonal for general MLE.
        """
    def hat_matrix_exog_diag(self):
        """Diagonal of the hat_matrix using only exog as in OLS

        """
    def d_params(self):
        """Approximate change in parameter estimates when dropping observation.

        This uses one-step approximation of the parameter change to deleting
        one observation.
        """
    def dfbetas(self):
        """Scaled change in parameter estimates.

        The one-step change of parameters in d_params is rescaled by dividing
        by the standard error of the parameter estimate given by results.bse.
        """
    def params_one(self):
        """Parameter estimate based on one-step approximation.

        This the one step parameter estimate computed as
        ``params`` from the full sample minus ``d_params``.
        """
    def cooks_distance(self):
        """Cook's distance and p-values.

        Based on one step approximation d_params and on results.cov_params
        Cook's distance divides by the number of explanatory variables.

        p-values are based on the F-distribution which are only approximate
        outside of linear Gaussian models.

        Warning: The definition of p-values might change if we switch to using
        chi-square distribution instead of F-distribution, or if we make it
        dependent on the fit keyword use_t.
        """
    def resid_studentized(self):
        """studentized default residuals.

        This uses the residual in `resid` attribute, which is by default
        resid_pearson and studentizes is using the generalized leverage.

        self.resid / np.sqrt(1 - self.hat_matrix_diag)

        Studentized residuals are not available if hat_matrix_diag is None.

        """
    def resid_score_factor(self):
        """Score residual divided by sqrt of hessian factor.

        experimental, agrees with GLMInfluence for Binomial and Gaussian.
        This corresponds to considering the linear predictors as parameters
        of the model.

        Note: Nhis might have nan values if second derivative, hessian_factor,
        is positive, i.e. loglikelihood is not globally concave w.r.t. linear
        predictor. (This occured in an example for GeneralizedPoisson)
        """
    def resid_score(self, joint: bool = True, index: Incomplete | None = None, studentize: bool = False):
        """Score observations scaled by inverse hessian.

        Score residual in resid_score are defined in analogy to a score test
        statistic for each observation.

        Parameters
        ----------
        joint : bool
            If joint is true, then a quadratic form similar to score_test is
            returned for each observation.
            If joint is false, then standardized score_obs are returned. The
            returned array is two-dimensional
        index : ndarray (optional)
            Optional index to select a subset of score_obs columns.
            By default, all columns of score_obs will be used.
        studentize : bool
            If studentize is true, the the scaled residuals are also
            studentized using the generalized leverage.

        Returns
        -------
        array :  1-D or 2-D residuals

        Notes
        -----
        Status: experimental

        Because of the one srep approacimation of d_params, score residuals
        are identical to cooks_distance, except for

        - cooks_distance is normalized by the number of parameters
        - cooks_distance uses cov_params, resid_score is based on Hessian.
          This will make them differ in the case of robust cov_params.

        """
    def d_fittedvalues(self):
        """Change in expected response, fittedvalues.

        Local change of expected mean given the change in the parameters as
        computed in d_params.

        Notes
        -----
        This uses the one-step approximation of the parameter change to
        deleting one observation ``d_params``.
        """
    @property
    def d_fittedvalues_scaled(self):
        """
        Change in fittedvalues scaled by standard errors.

        This uses one-step approximation of the parameter change to deleting
        one observation ``d_params``, and divides by the standard errors
        for the predicted mean provided by results.get_prediction.
        """
    def summary_frame(self):
        """
        Creates a DataFrame with influence results.

        Returns
        -------
        frame : pandas DataFrame
            A DataFrame with selected results for each observation.
            The index will be the same as provided to the model.

        Notes
        -----
        The resultant DataFrame contains six variables in addition to the
        ``dfbetas``. These are:

        * cooks_d : Cook's Distance defined in ``cooks_distance``
        * standard_resid : Standardized residuals defined in
          `resid_studentizedl`
        * hat_diag : The diagonal of the projection, or hat, matrix defined in
          `hat_matrix_diag`. Not included if None.
        * dffits_internal : DFFITS statistics using internally Studentized
          residuals defined in `d_fittedvalues_scaled`
        """

class OLSInfluence(_BaseInfluenceMixin):
    """class to calculate outlier and influence measures for OLS result

    Parameters
    ----------
    results : RegressionResults
        currently assumes the results are from an OLS regression

    Notes
    -----
    One part of the results can be calculated without any auxiliary regression
    (some of which have the `_internal` postfix in the name. Other statistics
    require leave-one-observation-out (LOOO) auxiliary regression, and will be
    slower (mainly results with `_external` postfix in the name).
    The auxiliary LOOO regression only the required results are stored.

    Using the LOO measures is currently only recommended if the data set
    is not too large. One possible approach for LOOO measures would be to
    identify possible problem observations with the _internal measures, and
    then run the leave-one-observation-out only with observations that are
    possible outliers. (However, this is not yet available in an automated way.)

    This should be extended to general least squares.

    The leave-one-variable-out (LOVO) auxiliary regression are currently not
    used.
    """
    results: Incomplete
    endog: Incomplete
    exog: Incomplete
    resid: Incomplete
    model_class: Incomplete
    scale: Incomplete
    aux_regression_exog: Incomplete
    aux_regression_endog: Incomplete
    def __init__(self, results) -> None: ...
    def hat_matrix_diag(self):
        """Diagonal of the hat_matrix for OLS

        Notes
        -----
        temporarily calculated here, this should go to model class
        """
    def resid_press(self):
        """PRESS residuals
        """
    def influence(self):
        """Influence measure

        matches the influence measure that gretl reports
        u * h / (1 - h)
        where u are the residuals and h is the diagonal of the hat_matrix
        """
    def hat_diag_factor(self):
        """Factor of diagonal of hat_matrix used in influence

        this might be useful for internal reuse
        h / (1 - h)
        """
    def ess_press(self):
        """Error sum of squares of PRESS residuals
        """
    def resid_studentized(self):
        """Studentized residuals using variance from OLS

        alias for resid_studentized_internal for compatibility with
        MLEInfluence this uses sigma from original estimate and does
        not require leave one out loop
        """
    def resid_studentized_internal(self):
        """Studentized residuals using variance from OLS

        this uses sigma from original estimate
        does not require leave one out loop
        """
    def resid_studentized_external(self):
        """Studentized residuals using LOOO variance

        this uses sigma from leave-one-out estimates

        requires leave one out loop for observations
        """
    def get_resid_studentized_external(self, sigma: Incomplete | None = None):
        """calculate studentized residuals

        Parameters
        ----------
        sigma : None or float
            estimate of the standard deviation of the residuals. If None, then
            the estimate from the regression results is used.

        Returns
        -------
        stzd_resid : ndarray
            studentized residuals

        Notes
        -----
        studentized residuals are defined as ::

           resid / sigma / np.sqrt(1 - hii)

        where resid are the residuals from the regression, sigma is an
        estimate of the standard deviation of the residuals, and hii is the
        diagonal of the hat_matrix.
        """
    def cooks_distance(self):
        """
        Cooks distance

        Uses original results, no nobs loop

        References
        ----------
        .. [*] Eubank, R. L. (1999). Nonparametric regression and spline
            smoothing. CRC press.
        .. [*] Cook's distance. (n.d.). In Wikipedia. July 2019, from
            https://en.wikipedia.org/wiki/Cook%27s_distance
        """
    def dffits_internal(self):
        """dffits measure for influence of an observation

        based on resid_studentized_internal
        uses original results, no nobs loop
        """
    def dffits(self):
        """
        dffits measure for influence of an observation

        based on resid_studentized_external,
        uses results from leave-one-observation-out loop

        It is recommended that observations with dffits large than a
        threshold of 2 sqrt{k / n} where k is the number of parameters, should
        be investigated.

        Returns
        -------
        dffits : float
        dffits_threshold : float

        References
        ----------
        `Wikipedia <https://en.wikipedia.org/wiki/DFFITS>`_
        """
    def dfbetas(self):
        """dfbetas

        uses results from leave-one-observation-out loop
        """
    def dfbeta(self):
        """dfbetas

        uses results from leave-one-observation-out loop
        """
    def sigma2_not_obsi(self):
        """error variance for all LOOO regressions

        This is 'mse_resid' from each auxiliary regression.

        uses results from leave-one-observation-out loop
        """
    @property
    def params_not_obsi(self):
        """parameter estimates for all LOOO regressions

        uses results from leave-one-observation-out loop
        """
    @property
    def det_cov_params_not_obsi(self):
        """determinant of cov_params of all LOOO regressions

        uses results from leave-one-observation-out loop
        """
    def cov_ratio(self):
        """covariance ratio between LOOO and original

        This uses determinant of the estimate of the parameter covariance
        from leave-one-out estimates.
        requires leave one out loop for observations
        """
    def resid_var(self):
        """estimate of variance of the residuals

        ::

           sigma2 = sigma2_OLS * (1 - hii)

        where hii is the diagonal of the hat matrix
        """
    def resid_std(self):
        """estimate of standard deviation of the residuals

        See Also
        --------
        resid_var
        """
    def summary_frame(self):
        """
        Creates a DataFrame with all available influence results.

        Returns
        -------
        frame : DataFrame
            A DataFrame with all results.

        Notes
        -----
        The resultant DataFrame contains six variables in addition to the
        DFBETAS. These are:

        * cooks_d : Cook's Distance defined in `Influence.cooks_distance`
        * standard_resid : Standardized residuals defined in
          `Influence.resid_studentized_internal`
        * hat_diag : The diagonal of the projection, or hat, matrix defined in
          `Influence.hat_matrix_diag`
        * dffits_internal : DFFITS statistics using internally Studentized
          residuals defined in `Influence.dffits_internal`
        * dffits : DFFITS statistics using externally Studentized residuals
          defined in `Influence.dffits`
        * student_resid : Externally Studentized residuals defined in
          `Influence.resid_studentized_external`
        """
    table_data: Incomplete
    def summary_table(self, float_fmt: str = '%6.3f'):
        """create a summary table with all influence and outlier measures

        This does currently not distinguish between statistics that can be
        calculated from the original regression results and for which a
        leave-one-observation-out loop is needed

        Returns
        -------
        res : SimpleTable
           SimpleTable instance with the results, can be printed

        Notes
        -----
        This also attaches table_data to the instance.
        """

def summary_table(res, alpha: float = 0.05):
    """
    Generate summary table of outlier and influence similar to SAS

    Parameters
    ----------
    alpha : float
       significance level for confidence interval

    Returns
    -------
    st : SimpleTable
       table with results that can be printed
    data : ndarray
       calculated measures and statistics for the table
    ss2 : list[str]
       column_names for table (Note: rows of table are observations)
    """

class GLMInfluence(MLEInfluence):
    """Influence and outlier measures (experimental)

    This uses partly formulas specific to GLM, specifically cooks_distance
    is based on the hessian, i.e. observed or expected information matrix and
    not on cov_params, in contrast to MLEInfluence.
    Standardization for changes in parameters, in fittedvalues and in
    the linear predictor are based on cov_params.

    Parameters
    ----------
    results : instance of results class
        This only works for model and results classes that have the necessary
        helper methods.
    other arguments are only to override default behavior and are used instead
    of the corresponding attribute of the results class.
    By default resid_pearson is used as resid.

    Attributes
    ----------
    dbetas
        change in parameters divided by the standard error of parameters from
        the full model results, ``bse``.
    d_fittedvalues_scaled
        same as d_fittedvalues but scaled by the standard errors of a
        predicted mean of the response.
    d_linpred
        local change in linear prediction.
    d_linpred_scale
        local change in linear prediction scaled by the standard errors for
        the prediction based on cov_params.

    Notes
    -----
    This has not yet been tested for correctness when offset or exposure
    are used, although they should be supported by the code.

    Some GLM specific measures like d_deviance are still missing.

    Computing an explicit leave-one-observation-out (LOOO) loop is included
    but no influence measures are currently computed from it.
    """
    def hat_matrix_diag(self):
        """
        Diagonal of the hat_matrix for GLM

        Notes
        -----
        This returns the diagonal of the hat matrix that was provided as
        argument to GLMInfluence or computes it using the results method
        `get_hat_matrix`.
        """
    def d_params(self):
        """Change in parameter estimates

        Notes
        -----
        This uses one-step approximation of the parameter change to deleting
        one observation.
        """
    def resid_studentized(self):
        """
        Internally studentized pearson residuals

        Notes
        -----
        residuals / sqrt( scale * (1 - hii))

        where residuals are those provided to GLMInfluence which are
        pearson residuals by default, and
        hii is the diagonal of the hat matrix.
        """
    def cooks_distance(self):
        """Cook's distance

        Notes
        -----
        Based on one step approximation using resid_studentized and
        hat_matrix_diag for the computation.

        Cook's distance divides by the number of explanatory variables.

        Computed using formulas for GLM and does not use results.cov_params.
        It includes p-values based on the F-distribution which are only
        approximate outside of linear Gaussian models.
        """
    @property
    def d_linpred(self):
        """
        Change in linear prediction

        This uses one-step approximation of the parameter change to deleting
        one observation ``d_params``.
        """
    @property
    def d_linpred_scaled(self):
        """
        Change in linpred scaled by standard errors

        This uses one-step approximation of the parameter change to deleting
        one observation ``d_params``, and divides by the standard errors
        for linpred provided by results.get_prediction.
        """
