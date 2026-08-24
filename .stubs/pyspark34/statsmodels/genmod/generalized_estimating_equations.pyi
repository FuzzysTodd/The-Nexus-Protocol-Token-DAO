import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete
from statsmodels.compat.pandas import Appender as Appender
from statsmodels.compat.python import lzip as lzip
from statsmodels.discrete.discrete_margins import margeff_cov_with_se as margeff_cov_with_se
from statsmodels.genmod import families as families
from statsmodels.genmod.families.links import Link as Link
from statsmodels.genmod.generalized_linear_model import GLM as GLM, GLMResults as GLMResults
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.sm_exceptions import ConvergenceWarning as ConvergenceWarning, DomainWarning as DomainWarning, IterationLimitWarning as IterationLimitWarning, ValueWarning as ValueWarning

class ParameterConstraint:
    """
    A class for managing linear equality constraints for a parameter
    vector.
    """
    lhs: Incomplete
    rhs: Incomplete
    lhs0: Incomplete
    lhs1: Incomplete
    lhsf: Incomplete
    param0: Incomplete
    orig_exog: Incomplete
    exog_fulltrans: Incomplete
    def __init__(self, lhs, rhs, exog) -> None:
        """
        Parameters
        ----------
        lhs : ndarray
           A q x p matrix which is the left hand side of the
           constraint lhs * param = rhs.  The number of constraints is
           q >= 1 and p is the dimension of the parameter vector.
        rhs : ndarray
          A 1-dimensional vector of length q which is the right hand
          side of the constraint equation.
        exog : ndarray
          The n x p exognenous data for the full model.
        """
    def offset_increment(self):
        """
        Returns a vector that should be added to the offset vector to
        accommodate the constraint.

        Parameters
        ----------
        exog : array_like
           The exogeneous data for the model.
        """
    def reduced_exog(self):
        """
        Returns a linearly transformed exog matrix whose columns span
        the constrained model space.

        Parameters
        ----------
        exog : array_like
           The exogeneous data for the model.
        """
    def restore_exog(self):
        """
        Returns the full exog matrix before it was reduced to
        satisfy the constraint.
        """
    def unpack_param(self, params):
        """
        Converts the parameter vector `params` from reduced to full
        coordinates.
        """
    def unpack_cov(self, bcov):
        """
        Converts the covariance matrix `bcov` from reduced to full
        coordinates.
        """

class GEE(GLM):
    __doc__: Incomplete
    cached_means: Incomplete
    missing: Incomplete
    dep_data: Incomplete
    constraint: Incomplete
    update_dep: Incomplete
    family: Incomplete
    cov_struct: Incomplete
    exog: Incomplete
    group_indices: Incomplete
    group_labels: Incomplete
    endog_li: Incomplete
    exog_li: Incomplete
    weights_li: Incomplete
    num_group: Incomplete
    time: Incomplete
    time_li: Incomplete
    offset_li: Incomplete
    nobs: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    def __init__(self, endog, exog, groups, time: Incomplete | None = None, family: Incomplete | None = None, cov_struct: Incomplete | None = None, missing: str = 'none', offset: Incomplete | None = None, exposure: Incomplete | None = None, dep_data: Incomplete | None = None, constraint: Incomplete | None = None, update_dep: bool = True, weights: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def from_formula(cls, formula, groups, data, subset: Incomplete | None = None, time: Incomplete | None = None, offset: Incomplete | None = None, exposure: Incomplete | None = None, *args, **kwargs): ...
    def cluster_list(self, array):
        """
        Returns `array` split into subarrays corresponding to the
        cluster structure.
        """
    scaletype: Incomplete
    ddof_scale: Incomplete
    scaling_factor: int
    def compare_score_test(self, submodel):
        '''
        Perform a score test for the given submodel against this model.

        Parameters
        ----------
        submodel : GEEResults instance
            A fitted GEE model that is a submodel of this model.

        Returns
        -------
        A dictionary with keys "statistic", "p-value", and "df",
        containing the score test statistic, its chi^2 p-value,
        and the degrees of freedom used to compute the p-value.

        Notes
        -----
        The score test can be performed without calling \'fit\' on the
        larger model.  The provided submodel must be obtained from a
        fitted GEE.

        This method performs the same score test as can be obtained by
        fitting the GEE with a linear constraint and calling `score_test`
        on the results.

        References
        ----------
        Xu Guo and Wei Pan (2002). "Small sample performance of the score
        test in GEE".
        http://www.sph.umn.edu/faculty1/wp-content/uploads/2012/11/rr2002-013.pdf
        '''
    def estimate_scale(self):
        """
        Estimate the dispersion/scale.
        """
    def mean_deriv(self, exog, lin_pred):
        """
        Derivative of the expected endog with respect to the parameters.

        Parameters
        ----------
        exog : array_like
           The exogeneous data at which the derivative is computed.
        lin_pred : array_like
           The values of the linear predictor.

        Returns
        -------
        The value of the derivative of the expected endog with respect
        to the parameter vector.

        Notes
        -----
        If there is an offset or exposure, it should be added to
        `lin_pred` prior to calling this function.
        """
    def mean_deriv_exog(self, exog, params, offset_exposure: Incomplete | None = None):
        """
        Derivative of the expected endog with respect to exog.

        Parameters
        ----------
        exog : array_like
            Values of the independent variables at which the derivative
            is calculated.
        params : array_like
            Parameter values at which the derivative is calculated.
        offset_exposure : array_like, optional
            Combined offset and exposure.

        Returns
        -------
        The derivative of the expected endog with respect to exog.
        """
    def update_cached_means(self, mean_params) -> None:
        """
        cached_means should always contain the most recent calculation
        of the group-wise mean vectors.  This function should be
        called every time the regression parameters are changed, to
        keep the cached means up to date.
        """
    fit_history: Incomplete
    def fit(self, maxiter: int = 60, ctol: float = 1e-06, start_params: Incomplete | None = None, params_niter: int = 1, first_dep_update: int = 0, cov_type: str = 'robust', ddof_scale: Incomplete | None = None, scaling_factor: float = 1.0, scale: Incomplete | None = None): ...
    def fit_regularized(self, pen_wt, scad_param: float = 3.7, maxiter: int = 100, ddof_scale: Incomplete | None = None, update_assoc: int = 5, ctol: float = 1e-05, ztol: float = 0.001, eps: float = 1e-06, scale: Incomplete | None = None):
        '''
        Regularized estimation for GEE.

        Parameters
        ----------
        pen_wt : float
            The penalty weight (a non-negative scalar).
        scad_param : float
            Non-negative scalar determining the shape of the Scad
            penalty.
        maxiter : int
            The maximum number of iterations.
        ddof_scale : int
            Value to subtract from `nobs` when calculating the
            denominator degrees of freedom for t-statistics, defaults
            to the number of columns in `exog`.
        update_assoc : int
            The dependence parameters are updated every `update_assoc`
            iterations of the mean structure parameter updates.
        ctol : float
            Convergence criterion, default is one order of magnitude
            smaller than proposed in section 3.1 of Wang et al.
        ztol : float
            Coefficients smaller than this value are treated as
            being zero, default is based on section 5 of Wang et al.
        eps : non-negative scalar
            Numerical constant, see section 3.2 of Wang et al.
        scale : float or string
            If a float, this value is used as the scale parameter.
            If "X2", the scale parameter is always estimated using
            Pearson\'s chi-square method (e.g. as in a quasi-Poisson
            analysis).  If None, the default approach for the family
            is used to estimate the scale parameter.

        Returns
        -------
        GEEResults instance.  Note that not all methods of the results
        class make sense when the model has been fit with regularization.

        Notes
        -----
        This implementation assumes that the link is canonical.

        References
        ----------
        Wang L, Zhou J, Qu A. (2012). Penalized generalized estimating
        equations for high-dimensional longitudinal data analysis.
        Biometrics. 2012 Jun;68(2):353-60.
        doi: 10.1111/j.1541-0420.2011.01678.x.
        https://www.ncbi.nlm.nih.gov/pubmed/21955051
        http://users.stat.umn.edu/~wangx346/research/GEE_selection.pdf
        '''
    def qic(self, params, scale, cov_params, n_step: int = 1000):
        """
        Returns quasi-information criteria and quasi-likelihood values.

        Parameters
        ----------
        params : array_like
            The GEE estimates of the regression parameters.
        scale : scalar
            Estimated scale parameter
        cov_params : array_like
            An estimate of the covariance matrix for the
            model parameters.  Conventionally this is the robust
            covariance matrix.
        n_step : integer
            The number of points in the trapezoidal approximation
            to the quasi-likelihood function.

        Returns
        -------
        ql : scalar
            The quasi-likelihood value
        qic : scalar
            A QIC that can be used to compare the mean and covariance
            structures of the model.
        qicu : scalar
            A simplified QIC that can be used to compare mean structures
            but not covariance structures

        Notes
        -----
        The quasi-likelihood used here is obtained by numerically evaluating
        Wedderburn's integral representation of the quasi-likelihood function.
        This approach is valid for all families and  links.  Many other
        packages use analytical expressions for quasi-likelihoods that are
        valid in special cases where the link function is canonical.  These
        analytical expressions may omit additive constants that only depend
        on the data.  Therefore, the numerical values of our QL and QIC values
        will differ from the values reported by other packages.  However only
        the differences between two QIC values calculated for different models
        using the same data are meaningful.  Our QIC should produce the same
        QIC differences as other software.

        When using the QIC for models with unknown scale parameter, use a
        common estimate of the scale parameter for all models being compared.

        References
        ----------
        .. [*] W. Pan (2001).  Akaike's information criterion in generalized
               estimating equations.  Biometrics (57) 1.
        """

class GEEResults(GLMResults):
    __doc__: Incomplete
    df_resid: Incomplete
    df_model: Incomplete
    family: Incomplete
    cov_type: Incomplete
    cov_params_default: Incomplete
    def __init__(self, model, params, cov_params, scale, cov_type: str = 'robust', use_t: bool = False, regularized: bool = False, **kwds) -> None: ...
    def resid(self):
        """
        The response residuals.
        """
    def standard_errors(self, cov_type: str = 'robust'):
        '''
        This is a convenience function that returns the standard
        errors for any covariance type.  The value of `bse` is the
        standard errors for whichever covariance type is specified as
        an argument to `fit` (defaults to "robust").

        Parameters
        ----------
        cov_type : str
            One of "robust", "naive", or "bias_reduced".  Determines
            the covariance used to compute standard errors.  Defaults
            to "robust".
        '''
    def bse(self): ...
    def score_test(self):
        '''
        Return the results of a score test for a linear constraint.

        Returns
        -------
        A\x7fdictionary containing the p-value, the test statistic,
        and the degrees of freedom for the score test.

        Notes
        -----
        See also GEE.compare_score_test for an alternative way to perform
        a score test.  GEEResults.score_test is more general, in that it
        supports testing arbitrary linear equality constraints.   However
        GEE.compare_score_test might be easier to use when comparing
        two explicit models.

        References
        ----------
        Xu Guo and Wei Pan (2002). "Small sample performance of the score
        test in GEE".
        http://www.sph.umn.edu/faculty1/wp-content/uploads/2012/11/rr2002-013.pdf
        '''
    def resid_split(self):
        """
        Returns the residuals, the endogeneous data minus the fitted
        values from the model.  The residuals are returned as a list
        of arrays containing the residuals for each cluster.
        """
    def resid_centered(self):
        """
        Returns the residuals centered within each group.
        """
    def resid_centered_split(self):
        """
        Returns the residuals centered within each group.  The
        residuals are returned as a list of arrays containing the
        centered residuals for each cluster.
        """
    def qic(self, scale: Incomplete | None = None, n_step: int = 1000):
        """
        Returns the QIC and QICu information criteria.

        See GEE.qic for documentation.
        """
    split_resid = resid_split
    centered_resid = resid_centered
    split_centered_resid = resid_centered_split
    def plot_added_variable(self, focus_exog, resid_type: Incomplete | None = None, use_glm_weights: bool = True, fit_kwargs: Incomplete | None = None, ax: Incomplete | None = None): ...
    def plot_partial_residuals(self, focus_exog, ax: Incomplete | None = None): ...
    def plot_ceres_residuals(self, focus_exog, frac: float = 0.66, cond_means: Incomplete | None = None, ax: Incomplete | None = None): ...
    def conf_int(self, alpha: float = 0.05, cols: Incomplete | None = None, cov_type: Incomplete | None = None):
        """
        Returns confidence intervals for the fitted parameters.

        Parameters
        ----------
        alpha : float, optional
             The `alpha` level for the confidence interval.  i.e., The
             default `alpha` = .05 returns a 95% confidence interval.
        cols : array_like, optional
             `cols` specifies which confidence intervals to return
        cov_type : str
             The covariance type used for computing standard errors;
             must be one of 'robust', 'naive', and 'bias reduced'.
             See `GEE` for details.

        Notes
        -----
        The confidence interval is based on the Gaussian distribution.
        """
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """
        Summarize the GEE regression results

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Names for the exogenous variables, default is `var_#` for ## in
            the number of regressors. Must match the number of parameters in
            the model
        title : str, optional
            Title for the top table. If not None, then this replaces
            the default title
        alpha : float
            significance level for the confidence intervals
        cov_type : str
            The covariance type used to compute the standard errors;
            one of 'robust' (the usual robust sandwich-type covariance
            estimate), 'naive' (ignores dependence), and 'bias
            reduced' (the Mancl/DeRouen estimate).

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be
            printed or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : class to hold summary results
        """
    def get_margeff(self, at: str = 'overall', method: str = 'dydx', atexog: Incomplete | None = None, dummy: bool = False, count: bool = False):
        """Get marginal effects of the fitted model.

        Parameters
        ----------
        at : str, optional
            Options are:

            - 'overall', The average of the marginal effects at each
              observation.
            - 'mean', The marginal effects at the mean of each regressor.
            - 'median', The marginal effects at the median of each regressor.
            - 'zero', The marginal effects at zero for each regressor.
            - 'all', The marginal effects at each observation. If `at` is 'all'
              only margeff will be available.

            Note that if `exog` is specified, then marginal effects for all
            variables not specified by `exog` are calculated using the `at`
            option.
        method : str, optional
            Options are:

            - 'dydx' - dy/dx - No transformation is made and marginal effects
              are returned.  This is the default.
            - 'eyex' - estimate elasticities of variables in `exog` --
              d(lny)/d(lnx)
            - 'dyex' - estimate semi-elasticity -- dy/d(lnx)
            - 'eydx' - estimate semi-elasticity -- d(lny)/dx

            Note that tranformations are done after each observation is
            calculated.  Semi-elasticities for binary variables are computed
            using the midpoint method. 'dyex' and 'eyex' do not make sense
            for discrete variables.
        atexog : array_like, optional
            Optionally, you can provide the exogenous variables over which to
            get the marginal effects.  This should be a dictionary with the key
            as the zero-indexed column number and the value of the dictionary.
            Default is None for all independent variables less the constant.
        dummy : bool, optional
            If False, treats binary variables (if present) as continuous.  This
            is the default.  Else if True, treats binary variables as
            changing from 0 to 1.  Note that any variable that is either 0 or 1
            is treated as binary.  Each binary variable is treated separately
            for now.
        count : bool, optional
            If False, treats count variables (if present) as continuous.  This
            is the default.  Else if True, the marginal effect is the
            change in probabilities when each observation is increased by one.

        Returns
        -------
        effects : ndarray
            the marginal effect corresponding to the input options

        Notes
        -----
        When using after Poisson, returns the expected number of events
        per period, assuming that the model is loglinear.
        """
    def plot_isotropic_dependence(self, ax: Incomplete | None = None, xpoints: int = 10, min_n: int = 50):
        """
        Create a plot of the pairwise products of within-group
        residuals against the corresponding time differences.  This
        plot can be used to assess the possible form of an isotropic
        covariance structure.

        Parameters
        ----------
        ax : AxesSubplot
            An axes on which to draw the graph.  If None, new
            figure and axes objects are created
        xpoints : scalar or array_like
            If scalar, the number of points equally spaced points on
            the time difference axis used to define bins for
            calculating local means.  If an array, the specific points
            that define the bins.
        min_n : int
            The minimum sample size in a bin for the mean residual
            product to be included on the plot.
        """
    def sensitivity_params(self, dep_params_first, dep_params_last, num_steps):
        """
        Refits the GEE model using a sequence of values for the
        dependence parameters.

        Parameters
        ----------
        dep_params_first : array_like
            The first dep_params in the sequence
        dep_params_last : array_like
            The last dep_params in the sequence
        num_steps : int
            The number of dep_params in the sequence

        Returns
        -------
        results : array_like
            The GEEResults objects resulting from the fits.
        """
    params_sensitivity = sensitivity_params

class GEEResultsWrapper(lm.RegressionResultsWrapper): ...

class OrdinalGEE(GEE):
    __doc__: Incomplete
    def __init__(self, endog, exog, groups, time: Incomplete | None = None, family: Incomplete | None = None, cov_struct: Incomplete | None = None, missing: str = 'none', offset: Incomplete | None = None, dep_data: Incomplete | None = None, constraint: Incomplete | None = None, **kwargs) -> None: ...
    endog_orig: Incomplete
    exog_orig: Incomplete
    groups_orig: Incomplete
    offset_orig: Incomplete
    time_orig: Incomplete
    endog_values: Incomplete
    def setup_ordinal(self, endog, exog, groups, time, offset):
        """
        Restructure ordinal data as binary indicators so that they can
        be analyzed using Generalized Estimating Equations.
        """
    def fit(self, maxiter: int = 60, ctol: float = 1e-06, start_params: Incomplete | None = None, params_niter: int = 1, first_dep_update: int = 0, cov_type: str = 'robust'): ...

class OrdinalGEEResults(GEEResults):
    __doc__: Incomplete
    def plot_distribution(self, ax: Incomplete | None = None, exog_values: Incomplete | None = None):
        '''
        Plot the fitted probabilities of endog in an ordinal model,
        for specified values of the predictors.

        Parameters
        ----------
        ax : AxesSubplot
            An axes on which to draw the graph.  If None, new
            figure and axes objects are created
        exog_values : array_like
            A list of dictionaries, with each dictionary mapping
            variable names to values at which the variable is held
            fixed.  The values P(endog=y | exog) are plotted for all
            possible values of y, at the given exog value.  Variables
            not included in a dictionary are held fixed at the mean
            value.

        Example:
        --------
        We have a model with covariates \'age\' and \'sex\', and wish to
        plot the probabilities P(endog=y | exog) for males (sex=0) and
        for females (sex=1), as separate paths on the plot.  Since
        \'age\' is not included below in the map, it is held fixed at
        its mean value.

        >>> ev = [{"sex": 1}, {"sex": 0}]
        >>> rslt.distribution_plot(exog_values=ev)
        '''

class OrdinalGEEResultsWrapper(GEEResultsWrapper): ...

class NominalGEE(GEE):
    __doc__: Incomplete
    def __init__(self, endog, exog, groups, time: Incomplete | None = None, family: Incomplete | None = None, cov_struct: Incomplete | None = None, missing: str = 'none', offset: Incomplete | None = None, dep_data: Incomplete | None = None, constraint: Incomplete | None = None, **kwargs) -> None: ...
    endog_orig: Incomplete
    exog_orig: Incomplete
    groups_orig: Incomplete
    offset_orig: Incomplete
    time_orig: Incomplete
    endog_values: Incomplete
    ncut: Incomplete
    def setup_nominal(self, endog, exog, groups, time, offset):
        """
        Restructure nominal data as binary indicators so that they can
        be analyzed using Generalized Estimating Equations.
        """
    def mean_deriv(self, exog, lin_pred):
        """
        Derivative of the expected endog with respect to the parameters.

        Parameters
        ----------
        exog : array_like
           The exogeneous data at which the derivative is computed,
           number of rows must be a multiple of `ncut`.
        lin_pred : array_like
           The values of the linear predictor, length must be multiple
           of `ncut`.

        Returns
        -------
        The derivative of the expected endog with respect to the
        parameters.
        """
    def mean_deriv_exog(self, exog, params, offset_exposure: Incomplete | None = None):
        """
        Derivative of the expected endog with respect to exog for the
        multinomial model, used in analyzing marginal effects.

        Parameters
        ----------
        exog : array_like
           The exogeneous data at which the derivative is computed,
           number of rows must be a multiple of `ncut`.
        lpr : array_like
           The linear predictor values, length must be multiple of
           `ncut`.

        Returns
        -------
        The value of the derivative of the expected endog with respect
        to exog.

        Notes
        -----
        offset_exposure must be set at None for the multinomial family.
        """
    def fit(self, maxiter: int = 60, ctol: float = 1e-06, start_params: Incomplete | None = None, params_niter: int = 1, first_dep_update: int = 0, cov_type: str = 'robust'): ...

class NominalGEEResults(GEEResults):
    __doc__: Incomplete
    def plot_distribution(self, ax: Incomplete | None = None, exog_values: Incomplete | None = None):
        '''
        Plot the fitted probabilities of endog in an nominal model,
        for specified values of the predictors.

        Parameters
        ----------
        ax : AxesSubplot
            An axes on which to draw the graph.  If None, new
            figure and axes objects are created
        exog_values : array_like
            A list of dictionaries, with each dictionary mapping
            variable names to values at which the variable is held
            fixed.  The values P(endog=y | exog) are plotted for all
            possible values of y, at the given exog value.  Variables
            not included in a dictionary are held fixed at the mean
            value.

        Example:
        --------
        We have a model with covariates \'age\' and \'sex\', and wish to
        plot the probabilities P(endog=y | exog) for males (sex=0) and
        for females (sex=1), as separate paths on the plot.  Since
        \'age\' is not included below in the map, it is held fixed at
        its mean value.

        >>> ex = [{"sex": 1}, {"sex": 0}]
        >>> rslt.distribution_plot(exog_values=ex)
        '''

class NominalGEEResultsWrapper(GEEResultsWrapper): ...

class _MultinomialLogit(Link):
    """
    The multinomial logit transform, only for use with GEE.

    Notes
    -----
    The data are assumed coded as binary indicators, where each
    observed multinomial value y is coded as I(y == S[0]), ..., I(y ==
    S[-1]), where S is the set of possible response labels, excluding
    the largest one.  Thererefore functions in this class should only
    be called using vector argument whose length is a multiple of |S|
    = ncut, which is an argument to be provided when initializing the
    class.

    call and derivative use a private method _clean to trim p by 1e-10
    so that p is in (0, 1)
    """
    ncut: Incomplete
    def __init__(self, ncut) -> None: ...
    def inverse(self, lpr):
        """
        Inverse of the multinomial logit transform, which gives the
        expected values of the data as a function of the linear
        predictors.

        Parameters
        ----------
        lpr : array_like (length must be divisible by `ncut`)
            The linear predictors

        Returns
        -------
        prob : ndarray
            Probabilities, or expected values
        """

class _Multinomial(families.Family):
    """
    Pseudo-link function for fitting nominal multinomial models with
    GEE.  Not for use outside the GEE class.
    """
    links: Incomplete
    variance: Incomplete
    safe_links: Incomplete
    def __init__(self, nlevels, check_link: bool = True) -> None:
        """
        Parameters
        ----------
        nlevels : int
            The number of distinct categories for the multinomial
            distribution.
        """
    ncut: Incomplete
    link: Incomplete
    def initialize(self, nlevels) -> None: ...

class GEEMargins:
    """
    Estimated marginal effects for a regression model fit with GEE.

    Parameters
    ----------
    results : GEEResults instance
        The results instance of a fitted discrete choice model
    args : tuple
        Args are passed to `get_margeff`. This is the same as
        results.get_margeff. See there for more information.
    kwargs : dict
        Keyword args are passed to `get_margeff`. This is the same as
        results.get_margeff. See there for more information.
    """
    results: Incomplete
    def __init__(self, results, args, kwargs={}) -> None: ...
    def tvalues(self): ...
    def summary_frame(self, alpha: float = 0.05):
        """
        Returns a DataFrame summarizing the marginal effects.

        Parameters
        ----------
        alpha : float
            Number between 0 and 1. The confidence intervals have the
            probability 1-alpha.

        Returns
        -------
        frame : DataFrames
            A DataFrame summarizing the marginal effects.
        """
    def pvalues(self): ...
    def conf_int(self, alpha: float = 0.05):
        """
        Returns the confidence intervals of the marginal effects

        Parameters
        ----------
        alpha : float
            Number between 0 and 1. The confidence intervals have the
            probability 1-alpha.

        Returns
        -------
        conf_int : ndarray
            An array with lower, upper confidence intervals for the marginal
            effects.
        """
    def summary(self, alpha: float = 0.05):
        """
        Returns a summary table for marginal effects

        Parameters
        ----------
        alpha : float
            Number between 0 and 1. The confidence intervals have the
            probability 1-alpha.

        Returns
        -------
        Summary : SummaryTable
            A SummaryTable instance
        """
    margeff_options: Incomplete
    margeff: Incomplete
    margeff_cov: Incomplete
    margeff_se: Incomplete
    def get_margeff(self, at: str = 'overall', method: str = 'dydx', atexog: Incomplete | None = None, dummy: bool = False, count: bool = False) -> None: ...
