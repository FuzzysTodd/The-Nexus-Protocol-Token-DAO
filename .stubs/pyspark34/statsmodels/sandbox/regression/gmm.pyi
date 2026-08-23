from _typeshed import Incomplete
from statsmodels.base.model import LikelihoodModel as LikelihoodModel, LikelihoodModelResults as LikelihoodModelResults, Model as Model
from statsmodels.compat.python import lrange as lrange
from statsmodels.regression.linear_model import OLS as OLS, RegressionResults as RegressionResults, RegressionResultsWrapper as RegressionResultsWrapper
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.numdiff import approx_fprime as approx_fprime

DEBUG: int

def maxabs(x):
    """just a shortcut to np.abs(x).max()
    """

class IV2SLS(LikelihoodModel):
    """
    Instrumental variables estimation using Two-Stage Least-Squares (2SLS)


    Parameters
    ----------
    endog : ndarray
       Endogenous variable, 1-dimensional or 2-dimensional array nobs by 1
    exog : ndarray
       Explanatory variables, 1-dimensional or 2-dimensional array nobs by k
    instrument : ndarray
       Instruments for explanatory variables. Must contain both exog
       variables that are not being instrumented and instruments

    Notes
    -----
    All variables in exog are instrumented in the calculations. If variables
    in exog are not supposed to be instrumented, then these variables
    must also to be included in the instrument array.

    Degrees of freedom in the calculation of the standard errors uses
    `df_resid = (nobs - k_vars)`.
    (This corresponds to the `small` option in Stata's ivreg2.)
    """
    df_resid: Incomplete
    df_model: Incomplete
    def __init__(self, endog, exog, instrument: Incomplete | None = None) -> None: ...
    wendog: Incomplete
    wexog: Incomplete
    def initialize(self) -> None: ...
    def whiten(self, X) -> None:
        """Not implemented"""
    xhatparams: Incomplete
    xhatprod: Incomplete
    normalized_cov_params: Incomplete
    def fit(self):
        """estimate model using 2SLS IV regression

        Returns
        -------
        results : instance of RegressionResults
           regression result

        Notes
        -----
        This returns a generic RegressioResults instance as defined for the
        linear models.

        Parameter estimates and covariance are correct, but other results
        have not been tested yet, to see whether they apply without changes.

        """
    def predict(self, params, exog: Incomplete | None = None):
        """
        Return linear predicted values from a design matrix.

        Parameters
        ----------
        exog : array_like
            Design / exogenous data
        params : array_like, optional after fit has been called
            Parameters of a linear model

        Returns
        -------
        An array of fitted values

        Notes
        -----
        If the model as not yet been fit, params is not optional.
        """

class IVRegressionResults(RegressionResults):
    """
    Results class for for an OLS model.

    Most of the methods and attributes are inherited from RegressionResults.
    The special methods that are only available for OLS are:

    - get_influence
    - outlier_test
    - el_test
    - conf_int_el

    See Also
    --------
    RegressionResults
    """
    def fvalue(self): ...
    def spec_hausman(self, dof: Incomplete | None = None):
        """Hausman's specification test

        See Also
        --------
        spec_hausman : generic function for Hausman's specification test

        """
    diagn: Incomplete
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """Summarize the Regression Results

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Default is `var_##` for ## in p the number of regressors
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
        statsmodels.iolib.summary.Summary : class to hold summary
            results
        """

class GMM(Model):
    """
    Class for estimation by Generalized Method of Moments

    needs to be subclassed, where the subclass defined the moment conditions
    `momcond`

    Parameters
    ----------
    endog : ndarray
        endogenous variable, see notes
    exog : ndarray
        array of exogenous variables, see notes
    instrument : ndarray
        array of instruments, see notes
    nmoms : None or int
        number of moment conditions, if None then it is set equal to the
        number of columns of instruments. Mainly needed to determine the shape
        or size of start parameters and starting weighting matrix.
    kwds : anything
        this is mainly if additional variables need to be stored for the
        calculations of the moment conditions

    Attributes
    ----------
    results : instance of GMMResults
        currently just a storage class for params and cov_params without it's
        own methods
    bse : property
        return bse



    Notes
    -----
    The GMM class only uses the moment conditions and does not use any data
    directly. endog, exog, instrument and kwds in the creation of the class
    instance are only used to store them for access in the moment conditions.
    Which of this are required and how they are used depends on the moment
    conditions of the subclass.

    Warning:

    Options for various methods have not been fully implemented and
    are still missing in several methods.


    TODO:
    currently onestep (maxiter=0) still produces an updated estimate of bse
    and cov_params.

    """
    results_class: str
    nobs: Incomplete
    nmoms: Incomplete
    k_params: Incomplete
    epsilon_iter: float
    def __init__(self, endog, exog, instrument, k_moms: Incomplete | None = None, k_params: Incomplete | None = None, missing: str = 'none', **kwds) -> None:
        """
        maybe drop and use mixin instead

        TODO: GMM does not really care about the data, just the moment conditions
        """
    def set_param_names(self, param_names, k_params: Incomplete | None = None) -> None:
        """set the parameter names in the model

        Parameters
        ----------
        param_names : list[str]
            param_names should have the same length as the number of params
        k_params : None or int
            If k_params is None, then the k_params attribute is used, unless
            it is None.
            If k_params is not None, then it will also set the k_params
            attribute.
        """
    results: Incomplete
    def fit(self, start_params: Incomplete | None = None, maxiter: int = 10, inv_weights: Incomplete | None = None, weights_method: str = 'cov', wargs=(), has_optimal_weights: bool = True, optim_method: str = 'bfgs', optim_args: Incomplete | None = None):
        """
        Estimate parameters using GMM and return GMMResults

        TODO: weight and covariance arguments still need to be made consistent
        with similar options in other models,
        see RegressionResult.get_robustcov_results

        Parameters
        ----------
        start_params : array (optional)
            starting value for parameters ub minimization. If None then
            fitstart method is called for the starting values.
        maxiter : int or 'cue'
            Number of iterations in iterated GMM. The onestep estimate can be
            obtained with maxiter=0 or 1. If maxiter is large, then the
            iteration will stop either at maxiter or on convergence of the
            parameters (TODO: no options for convergence criteria yet.)
            If `maxiter == 'cue'`, the the continuously updated GMM is
            calculated which updates the weight matrix during the minimization
            of the GMM objective function. The CUE estimation uses the onestep
            parameters as starting values.
        inv_weights : None or ndarray
            inverse of the starting weighting matrix. If inv_weights are not
            given then the method `start_weights` is used which depends on
            the subclass, for IV subclasses `inv_weights = z'z` where `z` are
            the instruments, otherwise an identity matrix is used.
        weights_method : str, defines method for robust
            Options here are similar to :mod:`statsmodels.stats.robust_covariance`
            default is heteroscedasticity consistent, HC0

            currently available methods are

            - `cov` : HC0, optionally with degrees of freedom correction
            - `hac` :
            - `iid` : untested, only for Z*u case, IV cases with u as error indep of Z
            - `ac` : not available yet
            - `cluster` : not connected yet
            - others from robust_covariance

        wargs` : tuple or dict,
            required and optional arguments for weights_method

            - `centered` : bool,
              indicates whether moments are centered for the calculation of the weights
              and covariance matrix, applies to all weight_methods
            - `ddof` : int
              degrees of freedom correction, applies currently only to `cov`
            - `maxlag` : int
              number of lags to include in HAC calculation , applies only to `hac`
            - others not yet, e.g. groups for cluster robust

        has_optimal_weights: If true, then the calculation of the covariance
              matrix assumes that we have optimal GMM with :math:`W = S^{-1}`.
              Default is True.
              TODO: do we want to have a different default after `onestep`?
        optim_method : str, default is 'bfgs'
            numerical optimization method. Currently not all optimizers that
            are available in LikelihoodModels are connected.
        optim_args : dict
            keyword arguments for the numerical optimizer.

        Returns
        -------
        results : instance of GMMResults
            this is also attached as attribute results

        Notes
        -----

        Warning: One-step estimation, `maxiter` either 0 or 1, still has
        problems (at least compared to Stata's gmm).
        By default it uses a heteroscedasticity robust covariance matrix, but
        uses the assumption that the weight matrix is optimal.
        See options for cov_params in the results instance.

        The same options as for weight matrix also apply to the calculation of
        the estimate of the covariance matrix of the parameter estimates.

        """
    def fitgmm(self, start, weights: Incomplete | None = None, optim_method: str = 'bfgs', optim_args: Incomplete | None = None):
        """estimate parameters using GMM

        Parameters
        ----------
        start : array_like
            starting values for minimization
        weights : ndarray
            weighting matrix for moment conditions. If weights is None, then
            the identity matrix is used


        Returns
        -------
        paramest : ndarray
            estimated parameters

        Notes
        -----
        todo: add fixed parameter option, not here ???

        uses scipy.optimize.fmin

        """
    def fitgmm_cu(self, start, optim_method: str = 'bfgs', optim_args: Incomplete | None = None):
        """estimate parameters using continuously updating GMM

        Parameters
        ----------
        start : array_like
            starting values for minimization

        Returns
        -------
        paramest : ndarray
            estimated parameters

        Notes
        -----
        todo: add fixed parameter option, not here ???

        uses scipy.optimize.fmin

        """
    def start_weights(self, inv: bool = True):
        """Create identity matrix for starting weights"""
    def gmmobjective(self, params, weights):
        """
        objective function for GMM minimization

        Parameters
        ----------
        params : ndarray
            parameter values at which objective is evaluated
        weights : ndarray
            weighting matrix

        Returns
        -------
        jval : float
            value of objective function

        """
    def gmmobjective_cu(self, params, weights_method: str = 'cov', wargs=()):
        """
        objective function for continuously updating  GMM minimization

        Parameters
        ----------
        params : ndarray
            parameter values at which objective is evaluated

        Returns
        -------
        jval : float
            value of objective function

        """
    history: Incomplete
    def fititer(self, start, maxiter: int = 2, start_invweights: Incomplete | None = None, weights_method: str = 'cov', wargs=(), optim_method: str = 'bfgs', optim_args: Incomplete | None = None):
        """iterative estimation with updating of optimal weighting matrix

        stopping criteria are maxiter or change in parameter estimate less
        than self.epsilon_iter, with default 1e-6.

        Parameters
        ----------
        start : ndarray
            starting value for parameters
        maxiter : int
            maximum number of iterations
        start_weights : array (nmoms, nmoms)
            initial weighting matrix; if None, then the identity matrix
            is used
        weights_method : {'cov', ...}
            method to use to estimate the optimal weighting matrix,
            see calc_weightmatrix for details

        Returns
        -------
        params : ndarray
            estimated parameters
        weights : ndarray
            optimal weighting matrix calculated with final parameter
            estimates

        Notes
        -----




        """
    def calc_weightmatrix(self, moms, weights_method: str = 'cov', wargs=(), params: Incomplete | None = None):
        """
        calculate omega or the weighting matrix

        Parameters
        ----------
        moms : ndarray
            moment conditions (nobs x nmoms) for all observations evaluated at
            a parameter value
        weights_method : str 'cov'
            If method='cov' is cov then the matrix is calculated as simple
            covariance of the moment conditions.
            see fit method for available aoptions for the weight and covariance
            matrix
        wargs : tuple or dict
            parameters that are required by some kernel methods to
            estimate the long-run covariance. Not used yet.

        Returns
        -------
        w : array (nmoms, nmoms)
            estimate for the weighting matrix or covariance of the moment
            condition


        Notes
        -----

        currently a constant cutoff window is used
        TODO: implement long-run cov estimators, kernel-based

        Newey-West
        Andrews
        Andrews-Moy????

        References
        ----------
        Greene
        Hansen, Bruce

        """
    def momcond_mean(self, params):
        """
        mean of moment conditions,

        """
    def gradient_momcond(self, params, epsilon: float = 0.0001, centered: bool = True):
        """gradient of moment conditions

        Parameters
        ----------
        params : ndarray
            parameter at which the moment conditions are evaluated
        epsilon : float
            stepsize for finite difference calculation
        centered : bool
            This refers to the finite difference calculation. If `centered`
            is true, then the centered finite difference calculation is
            used. Otherwise the one-sided forward differences are used.

        TODO: looks like not used yet
              missing argument `weights`

        """
    def score(self, params, weights, epsilon: Incomplete | None = None, centered: bool = True):
        """Score"""
    def score_cu(self, params, epsilon: Incomplete | None = None, centered: bool = True):
        """Score cu"""

class GMMResults(LikelihoodModelResults):
    """just a storage class right now"""
    use_t: bool
    nobs: Incomplete
    df_resid: Incomplete
    cov_params_default: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def q(self):
        """Objective function at params"""
    def jval(self):
        """nobs_moms attached by momcond_mean"""
    def calc_cov_params(self, moms, gradmoms, weights: Incomplete | None = None, use_weights: bool = False, has_optimal_weights: bool = True, weights_method: str = 'cov', wargs=()):
        """calculate covariance of parameter estimates

        not all options tried out yet

        If weights matrix is given, then the formula use to calculate cov_params
        depends on whether has_optimal_weights is true.
        If no weights are given, then the weight matrix is calculated with
        the given method, and has_optimal_weights is assumed to be true.

        (API Note: The latter assumption could be changed if we allow for
        has_optimal_weights=None.)

        """
    @property
    def bse_(self):
        """standard error of the parameter estimates
        """
    def get_bse(self, **kwds):
        """standard error of the parameter estimates with options

        Parameters
        ----------
        kwds : optional keywords
            options for calculating cov_params

        Returns
        -------
        bse : ndarray
            estimated standard error of parameter estimates

        """
    def jtest(self):
        """overidentification test

        I guess this is missing a division by nobs,
        what's the normalization in jval ?
        """
    def compare_j(self, other):
        """overidentification test for comparing two nested gmm estimates

        This assumes that some moment restrictions have been dropped in one
        of the GMM estimates relative to the other.

        Not tested yet

        We are comparing two separately estimated models, that use different
        weighting matrices. It is not guaranteed that the resulting
        difference is positive.

        TODO: Check in which cases Stata programs use the same weigths

        """
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05):
        """Summarize the Regression Results

        Parameters
        ----------
        yname : str, optional
            Default is `y`
        xname : list[str], optional
            Default is `var_##` for ## in p the number of regressors
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
        statsmodels.iolib.summary.Summary : class to hold summary
            results
        """

class IVGMM(GMM):
    """
    Basic class for instrumental variables estimation using GMM

    A linear function for the conditional mean is defined as default but the
    methods should be overwritten by subclasses, currently `LinearIVGMM` and
    `NonlinearIVGMM` are implemented as subclasses.

    See Also
    --------
    LinearIVGMM
    NonlinearIVGMM

    """
    results_class: str
    def fitstart(self):
        """Create array of zeros"""
    def start_weights(self, inv: bool = True):
        """Starting weights"""
    def get_error(self, params):
        """Get error at params"""
    def predict(self, params, exog: Incomplete | None = None):
        """Get prediction at params"""
    def momcond(self, params):
        """Error times instrument"""

class LinearIVGMM(IVGMM):
    """class for linear instrumental variables models estimated with GMM

    Uses closed form expression instead of nonlinear optimizers for each step
    of the iterative GMM.

    The model is assumed to have the following moment condition

        E( z * (y - x beta)) = 0

    Where `y` is the dependent endogenous variable, `x` are the explanatory
    variables and `z` are the instruments. Variables in `x` that are exogenous
    need also be included in `z`.

    Notation Warning: our name `exog` stands for the explanatory variables,
    and includes both exogenous and explanatory variables that are endogenous,
    i.e. included endogenous variables

    Parameters
    ----------
    endog : array_like
        dependent endogenous variable
    exog : array_like
        explanatory, right hand side variables, including explanatory variables
        that are endogenous
    instrument : array_like
        Instrumental variables, variables that are exogenous to the error
        in the linear model containing both included and excluded exogenous
        variables
    """
    def fitgmm(self, start, weights: Incomplete | None = None, optim_method: Incomplete | None = None, **kwds):
        """estimate parameters using GMM for linear model

        Uses closed form expression instead of nonlinear optimizers

        Parameters
        ----------
        start : not used
            starting values for minimization, not used, only for consistency
            of method signature
        weights : ndarray
            weighting matrix for moment conditions. If weights is None, then
            the identity matrix is used
        optim_method : not used,
            optimization method, not used, only for consistency of method
            signature
        **kwds : keyword arguments
            not used, will be silently ignored (for compatibility with generic)


        Returns
        -------
        paramest : ndarray
            estimated parameters

        """
    def predict(self, params, exog: Incomplete | None = None): ...
    def gradient_momcond(self, params, **kwds): ...
    def score(self, params, weights, **kwds): ...

class NonlinearIVGMM(IVGMM):
    """
    Class for non-linear instrumental variables estimation using GMM

    The model is assumed to have the following moment condition

        E[ z * (y - f(X, beta)] = 0

    Where `y` is the dependent endogenous variable, `x` are the explanatory
    variables and `z` are the instruments. Variables in `x` that are exogenous
    need also be included in z. `f` is a nonlinear function.

    Notation Warning: our name `exog` stands for the explanatory variables,
    and includes both exogenous and explanatory variables that are endogenous,
    i.e. included endogenous variables

    Parameters
    ----------
    endog : array_like
        dependent endogenous variable
    exog : array_like
        explanatory, right hand side variables, including explanatory variables
        that are endogenous.
    instruments : array_like
        Instrumental variables, variables that are exogenous to the error
        in the linear model containing both included and excluded exogenous
        variables
    func : callable
        function for the mean or conditional expectation of the endogenous
        variable. The function will be called with parameters and the array of
        explanatory, right hand side variables, `func(params, exog)`

    Notes
    -----
    This class uses numerical differences to obtain the derivative of the
    objective function. If the jacobian of the conditional mean function, `func`
    is available, then it can be used by subclassing this class and defining
    a method `jac_func`.

    TODO: check required signature of jac_error and jac_func
    """
    def fitstart(self): ...
    func: Incomplete
    def __init__(self, endog, exog, instrument, func, **kwds) -> None: ...
    def predict(self, params, exog: Incomplete | None = None): ...
    def jac_func(self, params, weights, args: Incomplete | None = None, centered: bool = True, epsilon: Incomplete | None = None): ...
    def jac_error(self, params, weights, args: Incomplete | None = None, centered: bool = True, epsilon: Incomplete | None = None): ...
    def score(self, params, weights, **kwds): ...

class IVGMMResults(GMMResults):
    """Results class of IVGMM"""
    def fittedvalues(self):
        """Fitted values"""
    def resid(self):
        """Residuals"""
    def ssr(self):
        """Sum of square errors"""

def spec_hausman(params_e, params_i, cov_params_e, cov_params_i, dof: Incomplete | None = None):
    """Hausmans specification test

    Parameters
    ----------
    params_e : ndarray
        efficient and consistent under Null hypothesis,
        inconsistent under alternative hypothesis
    params_i : ndarray
        consistent under Null hypothesis,
        consistent under alternative hypothesis
    cov_params_e : ndarray, 2d
        covariance matrix of parameter estimates for params_e
    cov_params_i : ndarray, 2d
        covariance matrix of parameter estimates for params_i

    example instrumental variables OLS estimator is `e`, IV estimator is `i`


    Notes
    -----

    Todos,Issues
    - check dof calculations and verify for linear case
    - check one-sided hypothesis


    References
    ----------
    Greene section 5.5 p.82/83


    """

class DistQuantilesGMM(GMM):
    """
    Estimate distribution parameters by GMM based on matching quantiles

    Currently mainly to try out different requirements for GMM when we cannot
    calculate the optimal weighting matrix.

    """
    epsilon_iter: float
    distfn: Incomplete
    endog: Incomplete
    pquant: Incomplete
    xquant: Incomplete
    nmoms: Incomplete
    exog: Incomplete
    instrument: Incomplete
    results: Incomplete
    def __init__(self, endog, exog, instrument, **kwds) -> None: ...
    def fitstart(self): ...
    def momcond(self, params):
        """moment conditions for estimating distribution parameters by matching
        quantiles, defines as many moment conditions as quantiles.

        Returns
        -------
        difference : ndarray
            difference between theoretical and empirical quantiles

        Notes
        -----
        This can be used for method of moments or for generalized method of
        moments.

        """
    def fitonce(self, start: Incomplete | None = None, weights: Incomplete | None = None, has_optimal_weights: bool = False):
        """fit without estimating an optimal weighting matrix and return results

        This is a convenience function that calls fitgmm and covparams with
        a given weight matrix or the identity weight matrix.
        This is useful if the optimal weight matrix is know (or is analytically
        given) or if an optimal weight matrix cannot be calculated.

        (Developer Notes: this function could go into GMM, but is needed in this
        class, at least at the moment.)

        Parameters
        ----------


        Returns
        -------
        results : GMMResult instance
            result instance with params and _cov_params attached

        See Also
        --------
        fitgmm
        cov_params

        """

results_class_dict: Incomplete
