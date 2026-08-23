import statsmodels.base.model as base
import statsmodels.regression.linear_model as lm
from _typeshed import Incomplete

__all__ = ['Poisson', 'Logit', 'Probit', 'MNLogit', 'NegativeBinomial', 'GeneralizedPoisson', 'NegativeBinomialP', 'CountModel']

class DiscreteModel(base.LikelihoodModel):
    """
    Abstract class for discrete choice models.

    This class does not do anything itself but lays out the methods and
    call signature expected of child classes in addition to those of
    statsmodels.model.LikelihoodModel.
    """
    raise_on_perfect_prediction: bool
    k_extra: int
    def __init__(self, endog, exog, check_rank: bool = True, **kwargs) -> None: ...
    df_model: Incomplete
    df_resid: Incomplete
    def initialize(self) -> None:
        """
        Initialize is called by
        statsmodels.model.LikelihoodModel.__init__
        and should contain any preprocessing that needs to be done for a model.
        """
    def cdf(self, X) -> None:
        """
        The cumulative distribution function of the model.
        """
    def pdf(self, X) -> None:
        """
        The probability density (mass) function of the model.
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'newton', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, **kwargs):
        """
        Fit the model using maximum likelihood.

        The rest of the docstring is from
        statsmodels.base.model.LikelihoodModel.fit
        """
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: bool = True, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, qc_verbose: bool = False, **kwargs):
        '''
        Fit the model using a regularized maximum likelihood.

        The regularization method AND the solver used is determined by the
        argument method.

        Parameters
        ----------
        start_params : array_like, optional
            Initial guess of the solution for the loglikelihood maximization.
            The default is an array of zeros.
        method : \'l1\' or \'l1_cvxopt_cp\'
            See notes for details.
        maxiter : {int, \'defined_by_method\'}
            Maximum number of iterations to perform.
            If \'defined_by_method\', then use method defaults (see notes).
        full_output : bool
            Set to True to have all available output in the Results object\'s
            mle_retvals attribute. The output is dependent on the solver.
            See LikelihoodModelResults notes section for more information.
        disp : bool
            Set to True to print convergence messages.
        fargs : tuple
            Extra arguments passed to the likelihood function, i.e.,
            loglike(x,*args).
        callback : callable callback(xk)
            Called after each iteration, as callback(xk), where xk is the
            current parameter vector.
        retall : bool
            Set to True to return list of solutions at each iteration.
            Available in Results object\'s mle_retvals attribute.
        alpha : non-negative scalar or numpy array (same size as parameters)
            The weight multiplying the l1 penalty term.
        trim_mode : \'auto, \'size\', or \'off\'
            If not \'off\', trim (set to zero) parameters that would have been
            zero if the solver reached the theoretical minimum.
            If \'auto\', trim params using the Theory above.
            If \'size\', trim params if they have very small absolute value.
        size_trim_tol : float or \'auto\' (default = \'auto\')
            Tolerance used when trim_mode == \'size\'.
        auto_trim_tol : float
            Tolerance used when trim_mode == \'auto\'.
        qc_tol : float
            Print warning and do not allow auto trim when (ii) (above) is
            violated by this much.
        qc_verbose : bool
            If true, print out a full QC report upon failure.
        **kwargs
            Additional keyword arguments used when fitting the model.

        Returns
        -------
        Results
            A results instance.

        Notes
        -----
        Using \'l1_cvxopt_cp\' requires the cvxopt module.

        Extra parameters are not penalized if alpha is given as a scalar.
        An example is the shape parameter in NegativeBinomial `nb1` and `nb2`.

        Optional arguments for the solvers (available in Results.mle_settings)::

            \'l1\'
                acc : float (default 1e-6)
                    Requested accuracy as used by slsqp
            \'l1_cvxopt_cp\'
                abstol : float
                    absolute accuracy (default: 1e-7).
                reltol : float
                    relative accuracy (default: 1e-6).
                feastol : float
                    tolerance for feasibility conditions (default: 1e-7).
                refinement : int
                    number of iterative refinement steps when solving KKT
                    equations (default: 1).

        Optimization methodology

        With :math:`L` the negative log likelihood, we solve the convex but
        non-smooth problem

        .. math:: \\min_\\beta L(\\beta) + \\sum_k\\alpha_k |\\beta_k|

        via the transformation to the smooth, convex, constrained problem
        in twice as many variables (adding the "added variables" :math:`u_k`)

        .. math:: \\min_{\\beta,u} L(\\beta) + \\sum_k\\alpha_k u_k,

        subject to

        .. math:: -u_k \\leq \\beta_k \\leq u_k.

        With :math:`\\partial_k L` the derivative of :math:`L` in the
        :math:`k^{th}` parameter direction, theory dictates that, at the
        minimum, exactly one of two conditions holds:

        (i) :math:`|\\partial_k L| = \\alpha_k`  and  :math:`\\beta_k \\neq 0`
        (ii) :math:`|\\partial_k L| \\leq \\alpha_k`  and  :math:`\\beta_k = 0`
        '''
    def cov_params_func_l1(self, likelihood_model, xopt, retvals):
        """
        Computes cov_params on a reduced parameter space
        corresponding to the nonzero parameters resulting from the
        l1 regularized fit.

        Returns a full cov_params matrix, with entries corresponding
        to zero'd values set to np.nan.
        """
    def predict(self, params, exog: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None) -> None:
        """
        Predict response variable of a model given exogenous variables.
        """

class BinaryModel(DiscreteModel):
    def __init__(self, endog, exog, offset: Incomplete | None = None, check_rank: bool = True, **kwargs) -> None: ...
    def predict(self, params, exog: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None, offset: Incomplete | None = None):
        """
        Predict response variable of a model given exogenous variables.

        Parameters
        ----------
        params : array_like
            Fitted parameters of the model.
        exog : array_like
            1d or 2d array of exogenous values.  If not supplied, the
            whole exog attribute of the model is used.
        which : {'mean', 'linear', 'var', 'prob'}, optional
            Statistic to predict. Default is 'mean'.

            - 'mean' returns the conditional expectation of endog E(y | x),
              i.e. exp of linear predictor.
            - 'linear' returns the linear predictor of the mean function.
            - 'var' returns the estimated variance of endog implied by the
              model.

            .. versionadded: 0.14

               ``which`` replaces and extends the deprecated ``linear``
               argument.

        linear : bool
            If True, returns the linear predicted values.  If False or None,
            then the statistic specified by ``which`` will be returned.

            .. deprecated: 0.14

               The ``linear` keyword is deprecated and will be removed,
               use ``which`` keyword instead.

        Returns
        -------
        array
            Fitted values at exog.
        """
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def fit_constrained(self, constraints, start_params: Incomplete | None = None, **fit_kwds): ...
    def get_distribution(self, params, exog: Incomplete | None = None, offset: Incomplete | None = None):
        """Get frozen instance of distribution based on predicted parameters.

        Parameters
        ----------
        params : array_like
            The parameters of the model.
        exog : ndarray, optional
            Explanatory variables for the main count model.
            If ``exog`` is None, then the data from the model will be used.
        offset : ndarray, optional
            Offset is added to the linear predictor of the mean function with
            coefficient equal to 1.
            Default is zero if exog is not None, and the model offset if exog
            is None.
        exposure : ndarray, optional
            Log(exposure) is added to the linear predictor  of the mean
            function with coefficient equal to 1. If exposure is specified,
            then it will be logged by the method. The user does not need to
            log it first.
            Default is one if exog is is not None, and it is the model exposure
            if exog is None.

        Returns
        -------
        Instance of frozen scipy distribution.
        """

class MultinomialModel(BinaryModel):
    endog: Incomplete
    J: Incomplete
    K: Incomplete
    df_resid: Incomplete
    def initialize(self) -> None:
        """
        Preprocesses the data for MNLogit.
        """
    def predict(self, params, exog: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None):
        """
        Predict response variable of a model given exogenous variables.

        Parameters
        ----------
        params : array_like
            2d array of fitted parameters of the model. Should be in the
            order returned from the model.
        exog : array_like
            1d or 2d array of exogenous values.  If not supplied, the
            whole exog attribute of the model is used. If a 1d array is given
            it assumed to be 1 row of exogenous variables. If you only have
            one regressor and would like to do prediction, you must provide
            a 2d array with shape[1] == 1.
        which : {'mean', 'linear', 'var', 'prob'}, optional
            Statistic to predict. Default is 'mean'.

            - 'mean' returns the conditional expectation of endog E(y | x),
              i.e. exp of linear predictor.
            - 'linear' returns the linear predictor of the mean function.
            - 'var' returns the estimated variance of endog implied by the
              model.

            .. versionadded: 0.14

               ``which`` replaces and extends the deprecated ``linear``
               argument.

        linear : bool
            If True, returns the linear predicted values.  If False or None,
            then the statistic specified by ``which`` will be returned.

            .. deprecated: 0.14

               The ``linear` keyword is deprecated and will be removed,
               use ``which`` keyword instead.

        Notes
        -----
        Column 0 is the base case, the rest conform to the rows of params
        shifted up one for the base case.
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'newton', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def get_distribution(self, params, exog: Incomplete | None = None, offset: Incomplete | None = None) -> None:
        """get frozen instance of distribution
        """

class CountModel(DiscreteModel):
    exposure: Incomplete
    offset: Incomplete
    endog: Incomplete
    exog: Incomplete
    def __init__(self, endog, exog, offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', check_rank: bool = True, **kwargs) -> None: ...
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None):
        """
        Predict response variable of a count model given exogenous variables

        Parameters
        ----------
        params : array_like
            Model parameters
        exog : array_like, optional
            Design / exogenous data. Is exog is None, model exog is used.
        exposure : array_like, optional
            Log(exposure) is added to the linear prediction with
            coefficient equal to 1. If exposure is not provided and exog
            is None, uses the model's exposure if present.  If not, uses
            0 as the default value.
        offset : array_like, optional
            Offset is added to the linear prediction with coefficient
            equal to 1. If offset is not provided and exog
            is None, uses the model's offset if present.  If not, uses
            0 as the default value.
        which : 'mean', 'linear', 'var', 'prob' (optional)
            Statitistic to predict. Default is 'mean'.

            - 'mean' returns the conditional expectation of endog E(y | x),
              i.e. exp of linear predictor.
            - 'linear' returns the linear predictor of the mean function.
            - 'var' variance of endog implied by the likelihood model
            - 'prob' predicted probabilities for counts.

            .. versionadded: 0.14

               ``which`` replaces and extends the deprecated ``linear``
               argument.

        linear : bool
            If True, returns the linear predicted values.  If False or None,
            then the statistic specified by ``which`` will be returned.

            .. deprecated: 0.14

               The ``linear` keyword is deprecated and will be removed,
               use ``which`` keyword instead.


        Notes
        -----
        If exposure is specified, then it will be logged by the method.
        The user does not need to log it first.
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'newton', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...

class Poisson(CountModel):
    __doc__: Incomplete
    def family(self): ...
    def cdf(self, X):
        """
        Poisson model cumulative distribution function

        Parameters
        ----------
        X : array_like
            `X` is the linear predictor of the model.  See notes.

        Returns
        -------
        The value of the Poisson CDF at each point.

        Notes
        -----
        The CDF is defined as

        .. math:: \\exp\\left(-\\lambda\\right)\\sum_{i=0}^{y}\\frac{\\lambda^{i}}{i!}

        where :math:`\\lambda` assumes the loglinear model. I.e.,

        .. math:: \\ln\\lambda_{i}=X\\beta

        The parameter `X` is :math:`X\\beta` in the above formula.
        """
    def pdf(self, X):
        """
        Poisson model probability mass function

        Parameters
        ----------
        X : array_like
            `X` is the linear predictor of the model.  See notes.

        Returns
        -------
        pdf : ndarray
            The value of the Poisson probability mass function, PMF, for each
            point of X.

        Notes
        -----
        The PMF is defined as

        .. math:: \\frac{e^{-\\lambda_{i}}\\lambda_{i}^{y_{i}}}{y_{i}!}

        where :math:`\\lambda` assumes the loglinear model. I.e.,

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta

        The parameter `X` is :math:`x_{i}\\beta` in the above formula.
        """
    def loglike(self, params):
        """
        Loglikelihood of Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]
        """
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : array_like
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----
        .. math:: \\ln L_{i}=\\left[-\\lambda_{i}+y_{i}x_{i}^{\\prime}\\beta-\\ln y_{i}!\\right]

        for observations :math:`i=1,...,n`
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'newton', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
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
    def score(self, params):
        """
        Poisson model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L}{\\partial\\beta}=\\sum_{i=1}^{n}\\left(y_{i}-\\lambda_{i}\\right)x_{i}

        where the loglinear model is assumed

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
    def score_obs(self, params):
        """
        Poisson model Jacobian of the log-likelihood for each observation

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : array_like
            The score vector (nobs, k_vars) of the model evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta}=\\left(y_{i}-\\lambda_{i}\\right)x_{i}

        for observations :math:`i=1,...,n`

        where the loglinear model is assumed

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
    def score_factor(self, params):
        """
        Poisson model score_factor for each observation

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : array_like
            The score factor (nobs, ) of the model evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta}=\\left(y_{i}-\\lambda_{i}\\right)

        for observations :math:`i=1,...,n`

        where the loglinear model is assumed

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
    def hessian(self, params):
        """
        Poisson model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial^{2}\\ln L}{\\partial\\beta\\partial\\beta^{\\prime}}=-\\sum_{i=1}^{n}\\lambda_{i}x_{i}x_{i}^{\\prime}

        where the loglinear model is assumed

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
    def hessian_factor(self, params):
        """
        Poisson model Hessian factor

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (nobs,)
            The Hessian factor, second derivative of loglikelihood function
            with respect to the linear predictor evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial^{2}\\ln L}{\\partial\\beta\\partial\\beta^{\\prime}}=-\\sum_{i=1}^{n}\\lambda_{i}

        where the loglinear model is assumed

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None, y_values: Incomplete | None = None):
        '''
        Predict response variable of a model given exogenous variables.

        Parameters
        ----------
        params : array_like
            2d array of fitted parameters of the model. Should be in the
            order returned from the model.
        exog : array_like, optional
            1d or 2d array of exogenous values.  If not supplied, then the
            exog attribute of the model is used. If a 1d array is given
            it assumed to be 1 row of exogenous variables. If you only have
            one regressor and would like to do prediction, you must provide
            a 2d array with shape[1] == 1.
        offset : array_like, optional
            Offset is added to the linear predictor with coefficient equal
            to 1.
            Default is zero if exog is not None, and the model offset if exog
            is None.
        exposure : array_like, optional
            Log(exposure) is added to the linear prediction with coefficient
            equal to 1.
            Default is one if exog is is not None, and is the model exposure
            if exog is None.
        which : \'mean\', \'linear\', \'var\', \'prob\' (optional)
            Statitistic to predict. Default is \'mean\'.

            - \'mean\' returns the conditional expectation of endog E(y | x),
              i.e. exp of linear predictor.
            - \'linear\' returns the linear predictor of the mean function.
            - \'var\' returns the estimated variance of endog implied by the
              model.
            - \'prob\' return probabilities for counts from 0 to max(endog) or
              for y_values if those are provided.

            .. versionadded: 0.14

               ``which`` replaces and extends the deprecated ``linear``
               argument.

        linear : bool
            The ``linear` keyword is deprecated and will be removed,
            use ``which`` keyword instead.
            If True, returns the linear predicted values.  If False or None,
            then the statistic specified by ``which`` will be returned.

            .. deprecated: 0.14

               The ``linear` keyword is deprecated and will be removed,
               use ``which`` keyword instead.

        y_values : array_like
            Values of the random variable endog at which pmf is evaluated.
            Only used if ``which="prob"``
        '''
    def get_distribution(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None):
        """Get frozen instance of distribution based on predicted parameters.

        Parameters
        ----------
        params : array_like
            The parameters of the model.
        exog : ndarray, optional
            Explanatory variables for the main count model.
            If ``exog`` is None, then the data from the model will be used.
        offset : ndarray, optional
            Offset is added to the linear predictor of the mean function with
            coefficient equal to 1.
            Default is zero if exog is not None, and the model offset if exog
            is None.
        exposure : ndarray, optional
            Log(exposure) is added to the linear predictor  of the mean
            function with coefficient equal to 1. If exposure is specified,
            then it will be logged by the method. The user does not need to
            log it first.
            Default is one if exog is is not None, and it is the model exposure
            if exog is None.

        Returns
        -------
        Instance of frozen scipy distribution subclass.
        """

class GeneralizedPoisson(CountModel):
    __doc__: Incomplete
    parameterization: Incomplete
    k_extra: int
    def __init__(self, endog, exog, p: int = 1, offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', check_rank: bool = True, **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood of Generalized Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[\\mu_{i}+(y_{i}-1)*ln(\\mu_{i}+
            \\alpha*\\mu_{i}^{p-1}*y_{i})-y_{i}*ln(1+\\alpha*\\mu_{i}^{p-1})-
            ln(y_{i}!)-\\frac{\\mu_{i}+\\alpha*\\mu_{i}^{p-1}*y_{i}}{1+\\alpha*
            \\mu_{i}^{p-1}}\\right]
        """
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of Generalized Poisson model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : ndarray
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----
        .. math:: \\ln L=\\sum_{i=1}^{n}\\left[\\mu_{i}+(y_{i}-1)*ln(\\mu_{i}+
            \\alpha*\\mu_{i}^{p-1}*y_{i})-y_{i}*ln(1+\\alpha*\\mu_{i}^{p-1})-
            ln(y_{i}!)-\\frac{\\mu_{i}+\\alpha*\\mu_{i}^{p-1}*y_{i}}{1+\\alpha*
            \\mu_{i}^{p-1}}\\right]

        for observations :math:`i=1,...,n`
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, use_transparams: bool = False, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, optim_kwds_prelim: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def score_obs(self, params): ...
    def score(self, params): ...
    def score_factor(self, params, endog: Incomplete | None = None): ...
    def hessian(self, params):
        """
        Generalized Poisson model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`
        """
    def hessian_factor(self, params):
        """
        Generalized Poisson model Hessian matrix of the loglikelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (nobs, 3)
            The Hessian factor, second derivative of loglikelihood function
            with respect to linear predictor and dispersion parameter
            evaluated at `params`
            The first column contains the second derivative w.r.t. linpred,
            the second column contains the cross derivative, and the
            third column contains the second derivative w.r.t. the dispersion
            parameter.

        """
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', y_values: Incomplete | None = None): ...
    def get_distribution(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None):
        """get frozen instance of distribution
        """

class Logit(BinaryModel):
    __doc__: Incomplete
    def link(self): ...
    def cdf(self, X):
        """
        The logistic cumulative distribution function

        Parameters
        ----------
        X : array_like
            `X` is the linear predictor of the logit model.  See notes.

        Returns
        -------
        1/(1 + exp(-X))

        Notes
        -----
        In the logit model,

        .. math:: \\Lambda\\left(x^{\\prime}\\beta\\right)=
                  \\text{Prob}\\left(Y=1|x\\right)=
                  \\frac{e^{x^{\\prime}\\beta}}{1+e^{x^{\\prime}\\beta}}
        """
    def pdf(self, X):
        """
        The logistic probability density function

        Parameters
        ----------
        X : array_like
            `X` is the linear predictor of the logit model.  See notes.

        Returns
        -------
        pdf : ndarray
            The value of the Logit probability mass function, PMF, for each
            point of X. ``np.exp(-x)/(1+np.exp(-X))**2``

        Notes
        -----
        In the logit model,

        .. math:: \\lambda\\left(x^{\\prime}\\beta\\right)=\\frac{e^{-x^{\\prime}\\beta}}{\\left(1+e^{-x^{\\prime}\\beta}\\right)^{2}}
        """
    def family(self): ...
    def loglike(self, params):
        """
        Log-likelihood of logit model.

        Parameters
        ----------
        params : array_like
            The parameters of the logit model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math::

           \\ln L=\\sum_{i}\\ln\\Lambda
           \\left(q_{i}x_{i}^{\\prime}\\beta\\right)

        Where :math:`q=2y-1`. This simplification comes from the fact that the
        logistic distribution is symmetric.
        """
    def loglikeobs(self, params):
        """
        Log-likelihood of logit model for each observation.

        Parameters
        ----------
        params : array_like
            The parameters of the logit model.

        Returns
        -------
        loglike : ndarray
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----
        .. math::

           \\ln L=\\sum_{i}\\ln\\Lambda
           \\left(q_{i}x_{i}^{\\prime}\\beta\\right)

        for observations :math:`i=1,...,n`

        where :math:`q=2y-1`. This simplification comes from the fact that the
        logistic distribution is symmetric.
        """
    def score(self, params):
        """
        Logit model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L}{\\partial\\beta}=\\sum_{i=1}^{n}\\left(y_{i}-\\Lambda_{i}\\right)x_{i}
        """
    def score_obs(self, params):
        """
        Logit model Jacobian of the log-likelihood for each observation

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        jac : array_like
            The derivative of the loglikelihood for each observation evaluated
            at `params`.

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta}=\\left(y_{i}-\\Lambda_{i}\\right)x_{i}

        for observations :math:`i=1,...,n`
        """
    def score_factor(self, params):
        """
        Logit model derivative of the log-likelihood with respect to linpred.

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score_factor : array_like
            The derivative of the loglikelihood for each observation evaluated
            at `params`.

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta}=\\left(y_{i}-\\lambda_{i}\\right)

        for observations :math:`i=1,...,n`

        where the loglinear model is assumed

        .. math:: \\ln\\lambda_{i}=x_{i}\\beta
        """
    def hessian(self, params):
        """
        Logit model Hessian matrix of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial^{2}\\ln L}{\\partial\\beta\\partial\\beta^{\\prime}}=-\\sum_{i}\\Lambda_{i}\\left(1-\\Lambda_{i}\\right)x_{i}x_{i}^{\\prime}
        """
    def hessian_factor(self, params):
        """
        Logit model Hessian factor

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (nobs,)
            The Hessian factor, second derivative of loglikelihood function
            with respect to the linear predictor evaluated at `params`
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'newton', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, **kwargs): ...

class Probit(BinaryModel):
    __doc__: Incomplete
    def link(self): ...
    def cdf(self, X):
        """
        Probit (Normal) cumulative distribution function

        Parameters
        ----------
        X : array_like
            The linear predictor of the model (XB).

        Returns
        -------
        cdf : ndarray
            The cdf evaluated at `X`.

        Notes
        -----
        This function is just an alias for scipy.stats.norm.cdf
        """
    def pdf(self, X):
        """
        Probit (Normal) probability density function

        Parameters
        ----------
        X : array_like
            The linear predictor of the model (XB).

        Returns
        -------
        pdf : ndarray
            The value of the normal density function for each point of X.

        Notes
        -----
        This function is just an alias for scipy.stats.norm.pdf
        """
    def loglike(self, params):
        """
        Log-likelihood of probit model (i.e., the normal distribution).

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math:: \\ln L=\\sum_{i}\\ln\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)

        Where :math:`q=2y-1`. This simplification comes from the fact that the
        normal distribution is symmetric.
        """
    def loglikeobs(self, params):
        """
        Log-likelihood of probit model for each observation

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : array_like
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----
        .. math:: \\ln L_{i}=\\ln\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)

        for observations :math:`i=1,...,n`

        where :math:`q=2y-1`. This simplification comes from the fact that the
        normal distribution is symmetric.
        """
    def score(self, params):
        """
        Probit model score (gradient) vector

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L}{\\partial\\beta}=\\sum_{i=1}^{n}\\left[\\frac{q_{i}\\phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}{\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}\\right]x_{i}

        Where :math:`q=2y-1`. This simplification comes from the fact that the
        normal distribution is symmetric.
        """
    def score_obs(self, params):
        """
        Probit model Jacobian for each observation

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        jac : array_like
            The derivative of the loglikelihood for each observation evaluated
            at `params`.

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta}=\\left[\\frac{q_{i}\\phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}{\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}\\right]x_{i}

        for observations :math:`i=1,...,n`

        Where :math:`q=2y-1`. This simplification comes from the fact that the
        normal distribution is symmetric.
        """
    def score_factor(self, params):
        """
        Probit model Jacobian for each observation

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        score_factor : array_like (nobs,)
            The derivative of the loglikelihood function for each observation
            with respect to linear predictor evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta}=\\left[\\frac{q_{i}\\phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}{\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}\\right]x_{i}

        for observations :math:`i=1,...,n`

        Where :math:`q=2y-1`. This simplification comes from the fact that the
        normal distribution is symmetric.
        """
    def hessian(self, params):
        """
        Probit model Hessian matrix of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (k_vars, k_vars)
            The Hessian, second derivative of loglikelihood function,
            evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial^{2}\\ln L}{\\partial\\beta\\partial\\beta^{\\prime}}=-\\lambda_{i}\\left(\\lambda_{i}+x_{i}^{\\prime}\\beta\\right)x_{i}x_{i}^{\\prime}

        where

        .. math:: \\lambda_{i}=\\frac{q_{i}\\phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}{\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}

        and :math:`q=2y-1`
        """
    def hessian_factor(self, params):
        """
        Probit model Hessian factor of the log-likelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (nobs,)
            The Hessian factor, second derivative of loglikelihood function
            with respect to linear predictor evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial^{2}\\ln L}{\\partial\\beta\\partial\\beta^{\\prime}}=-\\lambda_{i}\\left(\\lambda_{i}+x_{i}^{\\prime}\\beta\\right)x_{i}x_{i}^{\\prime}

        where

        .. math:: \\lambda_{i}=\\frac{q_{i}\\phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}{\\Phi\\left(q_{i}x_{i}^{\\prime}\\beta\\right)}

        and :math:`q=2y-1`
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'newton', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, **kwargs): ...

class MNLogit(MultinomialModel):
    __doc__: Incomplete
    def __init__(self, endog, exog, check_rank: bool = True, **kwargs) -> None: ...
    def pdf(self, eXB) -> None:
        """
        NotImplemented
        """
    def cdf(self, X):
        """
        Multinomial logit cumulative distribution function.

        Parameters
        ----------
        X : ndarray
            The linear predictor of the model XB.

        Returns
        -------
        cdf : ndarray
            The cdf evaluated at `X`.

        Notes
        -----
        In the multinomial logit model.
        .. math:: \\frac{\\exp\\left(\\beta_{j}^{\\prime}x_{i}\\right)}{\\sum_{k=0}^{J}\\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}
        """
    def loglike(self, params):
        """
        Log-likelihood of the multinomial logit model.

        Parameters
        ----------
        params : array_like
            The parameters of the multinomial logit model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.

        Notes
        -----
        .. math::

           \\ln L=\\sum_{i=1}^{n}\\sum_{j=0}^{J}d_{ij}\\ln
           \\left(\\frac{\\exp\\left(\\beta_{j}^{\\prime}x_{i}\\right)}
           {\\sum_{k=0}^{J}
           \\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}\\right)

        where :math:`d_{ij}=1` if individual `i` chose alternative `j` and 0
        if not.
        """
    def loglikeobs(self, params):
        """
        Log-likelihood of the multinomial logit model for each observation.

        Parameters
        ----------
        params : array_like
            The parameters of the multinomial logit model.

        Returns
        -------
        loglike : array_like
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes

        Notes
        -----
        .. math::

           \\ln L_{i}=\\sum_{j=0}^{J}d_{ij}\\ln
           \\left(\\frac{\\exp\\left(\\beta_{j}^{\\prime}x_{i}\\right)}
           {\\sum_{k=0}^{J}
           \\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}\\right)

        for observations :math:`i=1,...,n`

        where :math:`d_{ij}=1` if individual `i` chose alternative `j` and 0
        if not.
        """
    def score(self, params):
        """
        Score matrix for multinomial logit model log-likelihood

        Parameters
        ----------
        params : ndarray
            The parameters of the multinomial logit model.

        Returns
        -------
        score : ndarray, (K * (J-1),)
            The 2-d score vector, i.e. the first derivative of the
            loglikelihood function, of the multinomial logit model evaluated at
            `params`.

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L}{\\partial\\beta_{j}}=\\sum_{i}\\left(d_{ij}-\\frac{\\exp\\left(\\beta_{j}^{\\prime}x_{i}\\right)}{\\sum_{k=0}^{J}\\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}\\right)x_{i}

        for :math:`j=1,...,J`

        In the multinomial model the score matrix is K x J-1 but is returned
        as a flattened array to work with the solvers.
        """
    def loglike_and_score(self, params):
        """
        Returns log likelihood and score, efficiently reusing calculations.

        Note that both of these returned quantities will need to be negated
        before being minimized by the maximum likelihood fitting machinery.
        """
    def score_obs(self, params):
        """
        Jacobian matrix for multinomial logit model log-likelihood

        Parameters
        ----------
        params : ndarray
            The parameters of the multinomial logit model.

        Returns
        -------
        jac : array_like
            The derivative of the loglikelihood for each observation evaluated
            at `params` .

        Notes
        -----
        .. math:: \\frac{\\partial\\ln L_{i}}{\\partial\\beta_{j}}=\\left(d_{ij}-\\frac{\\exp\\left(\\beta_{j}^{\\prime}x_{i}\\right)}{\\sum_{k=0}^{J}\\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}\\right)x_{i}

        for :math:`j=1,...,J`, for observations :math:`i=1,...,n`

        In the multinomial model the score vector is K x (J-1) but is returned
        as a flattened array. The Jacobian has the observations in rows and
        the flattened array of derivatives in columns.
        """
    def hessian(self, params):
        """
        Multinomial logit Hessian matrix of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hess : ndarray, (J*K, J*K)
            The Hessian, second derivative of loglikelihood function with
            respect to the flattened parameters, evaluated at `params`

        Notes
        -----
        .. math:: \\frac{\\partial^{2}\\ln L}{\\partial\\beta_{j}\\partial\\beta_{l}}=-\\sum_{i=1}^{n}\\frac{\\exp\\left(\\beta_{j}^{\\prime}x_{i}\\right)}{\\sum_{k=0}^{J}\\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}\\left[\\boldsymbol{1}\\left(j=l\\right)-\\frac{\\exp\\left(\\beta_{l}^{\\prime}x_{i}\\right)}{\\sum_{k=0}^{J}\\exp\\left(\\beta_{k}^{\\prime}x_{i}\\right)}\\right]x_{i}x_{l}^{\\prime}

        where
        :math:`\\boldsymbol{1}\\left(j=l\\right)` equals 1 if `j` = `l` and 0
        otherwise.

        The actual Hessian matrix has J**2 * K x K elements. Our Hessian
        is reshaped to be square (J*K, J*K) so that the solvers can use it.

        This implementation does not take advantage of the symmetry of
        the Hessian and could probably be refactored for speed.
        """

class NegativeBinomial(CountModel):
    __doc__: Incomplete
    loglike_method: Incomplete
    k_extra: int
    def __init__(self, endog, exog, loglike_method: str = 'nb2', offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', check_rank: bool = True, **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood for negative binomial model

        Parameters
        ----------
        params : array_like
            The parameters of the model. If `loglike_method` is nb1 or
            nb2, then the ancillary parameter is expected to be the
            last element.

        Returns
        -------
        llf : float
            The loglikelihood value at `params`

        Notes
        -----
        Following notation in Greene (2008), with negative binomial
        heterogeneity parameter :math:`\\alpha`:

        .. math::

           \\lambda_i &= exp(X\\beta) \\\\\n           \\theta &= 1 / \\alpha \\\\\n           g_i &= \\theta \\lambda_i^Q \\\\\n           w_i &= g_i/(g_i + \\lambda_i) \\\\\n           r_i &= \\theta / (\\theta+\\lambda_i) \\\\\n           ln \\mathcal{L}_i &= ln \\Gamma(y_i+g_i) - ln \\Gamma(1+y_i) + g_iln (r_i) + y_i ln(1-r_i)

        where :math`Q=0` for NB2 and geometric and :math:`Q=1` for NB1.
        For the geometric, :math:`\\alpha=0` as well.
        """
    def score_obs(self, params): ...
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', linear: Incomplete | None = None, y_values: Incomplete | None = None): ...
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, optim_kwds_prelim: Incomplete | None = None, **kwargs): ...
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def get_distribution(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None):
        """get frozen instance of distribution
        """

class NegativeBinomialP(CountModel):
    __doc__: Incomplete
    parameterization: Incomplete
    k_extra: int
    def __init__(self, endog, exog, p: int = 2, offset: Incomplete | None = None, exposure: Incomplete | None = None, missing: str = 'none', check_rank: bool = True, **kwargs) -> None: ...
    def loglike(self, params):
        """
        Loglikelihood of Generalized Negative Binomial (NB-P) model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : float
            The log-likelihood function of the model evaluated at `params`.
            See notes.
        """
    def loglikeobs(self, params):
        """
        Loglikelihood for observations of Generalized Negative Binomial (NB-P) model

        Parameters
        ----------
        params : array_like
            The parameters of the model.

        Returns
        -------
        loglike : ndarray
            The log likelihood for each observation of the model evaluated
            at `params`. See Notes
        """
    def score_obs(self, params):
        """
        Generalized Negative Binomial (NB-P) model score (gradient) vector of the log-likelihood for each observations.

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def score(self, params):
        """
        Generalized Negative Binomial (NB-P) model score (gradient) vector of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def score_factor(self, params, endog: Incomplete | None = None):
        """
        Generalized Negative Binomial (NB-P) model score (gradient) vector of the log-likelihood for each observations.

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        score : ndarray, 1-D
            The score vector of the model, i.e. the first derivative of the
            loglikelihood function, evaluated at `params`
        """
    def hessian(self, params):
        """
        Generalized Negative Binomial (NB-P) model hessian maxtrix of the log-likelihood

        Parameters
        ----------
        params : array_like
            The parameters of the model

        Returns
        -------
        hessian : ndarray, 2-D
            The hessian matrix of the model.
        """
    def hessian_factor(self, params):
        """
        Generalized Negative Binomial (NB-P) model hessian maxtrix of the log-likelihood

        Parameters
        ----------
        params : array-like
            The parameters of the model

        Returns
        -------
        hessian : ndarray, 2-D
            The hessian matrix of the model.
        """
    def fit(self, start_params: Incomplete | None = None, method: str = 'bfgs', maxiter: int = 35, full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, use_transparams: bool = False, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None, optim_kwds_prelim: Incomplete | None = None, **kwargs):
        '''
        use_transparams : bool
            This parameter enable internal transformation to impose
            non-negativity. True to enable. Default is False.
            use_transparams=True imposes the no underdispersion (alpha > 0)
            constraint. In case use_transparams=True and method="newton" or
            "ncg" transformation is ignored.
        '''
    def fit_regularized(self, start_params: Incomplete | None = None, method: str = 'l1', maxiter: str = 'defined_by_method', full_output: int = 1, disp: int = 1, callback: Incomplete | None = None, alpha: int = 0, trim_mode: str = 'auto', auto_trim_tol: float = 0.01, size_trim_tol: float = 0.0001, qc_tol: float = 0.03, **kwargs): ...
    def predict(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, which: str = 'mean', y_values: Incomplete | None = None): ...
    def convert_params(self, params, mu): ...
    def get_distribution(self, params, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None):
        """get frozen instance of distribution
        """

class DiscreteResults(base.LikelihoodModelResults):
    __doc__: Incomplete
    model: Incomplete
    method: str
    df_model: Incomplete
    df_resid: Incomplete
    nobs: Incomplete
    converged: Incomplete
    use_t: Incomplete
    cov_type: str
    cov_kwds: Incomplete
    def __init__(self, model, mlefit, cov_type: str = 'nonrobust', cov_kwds: Incomplete | None = None, use_t: Incomplete | None = None) -> None: ...
    def prsquared(self):
        """
        McFadden's pseudo-R-squared. `1 - (llf / llnull)`
        """
    def llr(self):
        """
        Likelihood ratio chi-squared statistic; `-2*(llnull - llf)`
        """
    def llr_pvalue(self):
        """
        The chi-squared probability of getting a log-likelihood ratio
        statistic greater than llr.  llr has a chi-squared distribution
        with degrees of freedom `df_model`.
        """
    def set_null_options(self, llnull: Incomplete | None = None, attach_results: bool = True, **kwargs) -> None:
        '''
        Set the fit options for the Null (constant-only) model.

        This resets the cache for related attributes which is potentially
        fragile. This only sets the option, the null model is estimated
        when llnull is accessed, if llnull is not yet in cache.

        Parameters
        ----------
        llnull : {None, float}
            If llnull is not None, then the value will be directly assigned to
            the cached attribute "llnull".
        attach_results : bool
            Sets an internal flag whether the results instance of the null
            model should be attached. By default without calling this method,
            thenull model results are not attached and only the loglikelihood
            value llnull is stored.
        **kwargs
            Additional keyword arguments used as fit keyword arguments for the
            null model. The override and model default values.

        Notes
        -----
        Modifies attributes of this instance, and so has no return.
        '''
    res_null: Incomplete
    def llnull(self):
        """
        Value of the constant-only loglikelihood
        """
    def fittedvalues(self):
        """
        Linear predictor XB.
        """
    def resid_response(self):
        """
        Respnose residuals. The response residuals are defined as
        `endog - fittedvalues`
        """
    def resid_pearson(self):
        """
        Pearson residuals defined as response residuals divided by standard
        deviation implied by the model.
        """
    def aic(self):
        """
        Akaike information criterion.  `-2*(llf - p)` where `p` is the number
        of regressors including the intercept.
        """
    def bic(self):
        """
        Bayesian information criterion. `-2*llf + ln(nobs)*p` where `p` is the
        number of regressors including the intercept.
        """
    def im_ratio(self): ...
    def info_criteria(self, crit, dk_params: int = 0):
        """Return an information criterion for the model.

        Parameters
        ----------
        crit : string
            One of 'aic', 'bic', 'tic' or 'gbic'.
        dk_params : int or float
            Correction to the number of parameters used in the information
            criterion.

        Returns
        -------
        Value of information criterion.

        Notes
        -----
        Tic and gbic

        References
        ----------
        Burnham KP, Anderson KR (2002). Model Selection and Multimodel
        Inference; Springer New York.
        """
    def score_test(self, exog_extra: Incomplete | None = None, params_constrained: Incomplete | None = None, hypothesis: str = 'joint', cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, k_constraints: Incomplete | None = None, observed: bool = True): ...
    def get_prediction(self, exog: Incomplete | None = None, transform: bool = True, which: str = 'mean', linear: Incomplete | None = None, row_labels: Incomplete | None = None, average: bool = False, agg_weights: Incomplete | None = None, y_values: Incomplete | None = None, **kwargs):
        '''
        Compute prediction results when endpoint transformation is valid.

        Parameters
        ----------
        exog : array_like, optional
            The values for which you want to predict.
        transform : bool, optional
            If the model was fit via a formula, do you want to pass
            exog through the formula. Default is True. E.g., if you fit
            a model y ~ log(x1) + log(x2), and transform is True, then
            you can pass a data structure that contains x1 and x2 in
            their original form. Otherwise, you\'d need to log the data
            first.
        which : str
            Which statistic is to be predicted. Default is "mean".
            The available statistics and options depend on the model.
            see the model.predict docstring
        linear : bool
            Linear has been replaced by the `which` keyword and will be
            deprecated.
            If linear is True, then `which` is ignored and the linear
            prediction is returned.
        row_labels : list of str or None
            If row_lables are provided, then they will replace the generated
            labels.
        average : bool
            If average is True, then the mean prediction is computed, that is,
            predictions are computed for individual exog and then the average
            over observation is used.
            If average is False, then the results are the predictions for all
            observations, i.e. same length as ``exog``.
        agg_weights : ndarray, optional
            Aggregation weights, only used if average is True.
            The weights are not normalized.
        y_values : None or nd_array
            Some predictive statistics like which="prob" are computed at
            values of the response variable. If y_values is not None, then
            it will be used instead of the default set of y_values.

            **Warning:** ``which="prob"`` for count models currently computes
            the pmf for all y=k up to max(endog). This can be a large array if
            the observed endog values are large.
            This will likely change so that the set of y_values will be chosen
            to limit the array size.
        **kwargs :
            Some models can take additional keyword arguments, such as offset,
            exposure or additional exog in multi-part models like zero inflated
            models.
            See the predict method of the model for the details.

        Returns
        -------
        prediction_results : PredictionResults
            The prediction results instance contains prediction and prediction
            variance and can on demand calculate confidence intervals and
            summary dataframe for the prediction.

        Notes
        -----
        Status: new in 0.14, experimental
        '''
    def get_distribution(self, exog: Incomplete | None = None, transform: bool = True, **kwargs): ...
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
            - 'all', The marginal effects at each observation. If `at` is all
              only margeff will be available from the returned object.

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
            for discrete variables. For interpretations of these methods
            see notes below.
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
        DiscreteMargins : marginal effects instance
            Returns an object that holds the marginal effects, standard
            errors, confidence intervals, etc. See
            `statsmodels.discrete.discrete_margins.DiscreteMargins` for more
            information.

        Notes
        -----
        Interpretations of methods:

        - 'dydx' - change in `endog` for a change in `exog`.
        - 'eyex' - proportional change in `endog` for a proportional change
          in `exog`.
        - 'dyex' - change in `endog` for a proportional change in `exog`.
        - 'eydx' - proportional change in `endog` for a change in `exog`.

        When using after Poisson, returns the expected number of events per
        period, assuming that the model is loglinear.
        """
    def get_influence(self):
        """
        Get an instance of MLEInfluence with influence and outlier measures

        Returns
        -------
        infl : MLEInfluence instance
            The instance has methods to calculate the main influence and
            outlier measures as attributes.

        See Also
        --------
        statsmodels.stats.outliers_influence.MLEInfluence
        """
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05, yname_list: Incomplete | None = None):
        '''
        Summarize the Regression Results.

        Parameters
        ----------
        yname : str, optional
            The name of the endog variable in the tables. The default is `y`.
        xname : list[str], optional
            The names for the exogenous variables, default is "var_xx".
            Must match the number of parameters in the model.
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title.
        alpha : float
            The significance level for the confidence intervals.

        Returns
        -------
        Summary
            Class that holds the summary tables and text, which can be printed
            or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : Class that hold summary results.
        '''
    def summary2(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05, float_format: str = '%.4f'):
        """
        Experimental function to summarize regression results.

        Parameters
        ----------
        yname : str
            Name of the dependent variable (optional).
        xname : list[str], optional
            List of strings of length equal to the number of parameters
            Names of the independent variables (optional).
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title.
        alpha : float
            The significance level for the confidence intervals.
        float_format : str
            The print format for floats in parameters summary.

        Returns
        -------
        Summary
            Instance that contains the summary tables and text, which can be
            printed or converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary2.Summary : Class that holds summary results.
        """

class CountResults(DiscreteResults):
    __doc__: Incomplete
    def resid(self):
        """
        Residuals

        Notes
        -----
        The residuals for Count models are defined as

        .. math:: y - p

        where :math:`p = \\exp(X\\beta)`. Any exposure and offset variables
        are also handled.
        """
    def get_diagnostic(self, y_max: Incomplete | None = None):
        """
        Get instance of class with specification and diagnostic methods.

        experimental, API of Diagnostic classes will change

        Returns
        -------
        CountDiagnostic instance
            The instance has methods to perform specification and diagnostic
            tesst and plots

        See Also
        --------
        statsmodels.statsmodels.discrete.diagnostic.CountDiagnostic
        """

class NegativeBinomialResults(CountResults):
    __doc__: Incomplete
    def lnalpha(self):
        """Natural log of alpha"""
    def lnalpha_std_err(self):
        """Natural log of standardized error"""
    def aic(self): ...
    def bic(self): ...

class NegativeBinomialPResults(NegativeBinomialResults):
    __doc__: Incomplete

class GeneralizedPoissonResults(NegativeBinomialResults):
    __doc__: Incomplete

class L1CountResults(DiscreteResults):
    __doc__: Incomplete
    trimmed: Incomplete
    nnz_params: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    def __init__(self, model, cntfit) -> None: ...

class PoissonResults(CountResults):
    def predict_prob(self, n: Incomplete | None = None, exog: Incomplete | None = None, exposure: Incomplete | None = None, offset: Incomplete | None = None, transform: bool = True):
        """
        Return predicted probability of each count level for each observation

        Parameters
        ----------
        n : array_like or int
            The counts for which you want the probabilities. If n is None
            then the probabilities for each count from 0 to max(y) are
            given.

        Returns
        -------
        ndarray
            A nobs x n array where len(`n`) columns are indexed by the count
            n. If n is None, then column 0 is the probability that each
            observation is 0, column 1 is the probability that each
            observation is 1, etc.
        """
    @property
    def resid_pearson(self):
        """
        Pearson residuals

        Notes
        -----
        Pearson residuals are defined to be

        .. math:: r_j = \\frac{(y - M_jp_j)}{\\sqrt{M_jp_j(1-p_j)}}

        where :math:`p_j=cdf(X\\beta)` and :math:`M_j` is the total number of
        observations sharing the covariate pattern :math:`j`.

        For now :math:`M_j` is always set to 1.
        """
    def get_influence(self):
        """
        Get an instance of MLEInfluence with influence and outlier measures

        Returns
        -------
        infl : MLEInfluence instance
            The instance has methods to calculate the main influence and
            outlier measures as attributes.

        See Also
        --------
        statsmodels.stats.outliers_influence.MLEInfluence
        """
    def get_diagnostic(self, y_max: Incomplete | None = None):
        """
        Get instance of class with specification and diagnostic methods

        experimental, API of Diagnostic classes will change

        Returns
        -------
        PoissonDiagnostic instance
            The instance has methods to perform specification and diagnostic
            tesst and plots

        See Also
        --------
        statsmodels.statsmodels.discrete.diagnostic.PoissonDiagnostic
        """

class L1PoissonResults(L1CountResults, PoissonResults): ...
class L1NegativeBinomialResults(L1CountResults, NegativeBinomialResults): ...
class L1GeneralizedPoissonResults(L1CountResults, GeneralizedPoissonResults): ...

class OrderedResults(DiscreteResults):
    __doc__: Incomplete

class BinaryResults(DiscreteResults):
    __doc__: Incomplete
    def pred_table(self, threshold: float = 0.5):
        '''
        Prediction table

        Parameters
        ----------
        threshold : scalar
            Number between 0 and 1. Threshold above which a prediction is
            considered 1 and below which a prediction is considered 0.

        Notes
        -----
        pred_table[i,j] refers to the number of times "i" was observed and
        the model predicted "j". Correct predictions are along the diagonal.
        '''
    def summary(self, yname: Incomplete | None = None, xname: Incomplete | None = None, title: Incomplete | None = None, alpha: float = 0.05, yname_list: Incomplete | None = None): ...
    def resid_dev(self):
        """
        Deviance residuals

        Notes
        -----
        Deviance residuals are defined

        .. math:: d_j = \\pm\\left(2\\left[Y_j\\ln\\left(\\frac{Y_j}{M_jp_j}\\right) + (M_j - Y_j\\ln\\left(\\frac{M_j-Y_j}{M_j(1-p_j)} \\right) \\right] \\right)^{1/2}

        where

        :math:`p_j = cdf(X\\beta)` and :math:`M_j` is the total number of
        observations sharing the covariate pattern :math:`j`.

        For now :math:`M_j` is always set to 1.
        """
    def resid_pearson(self):
        """
        Pearson residuals

        Notes
        -----
        Pearson residuals are defined to be

        .. math:: r_j = \\frac{(y - M_jp_j)}{\\sqrt{M_jp_j(1-p_j)}}

        where :math:`p_j=cdf(X\\beta)` and :math:`M_j` is the total number of
        observations sharing the covariate pattern :math:`j`.

        For now :math:`M_j` is always set to 1.
        """
    def resid_response(self):
        """
        The response residuals

        Notes
        -----
        Response residuals are defined to be

        .. math:: y - p

        where :math:`p=cdf(X\\beta)`.
        """

class LogitResults(BinaryResults):
    __doc__: Incomplete
    def resid_generalized(self):
        """
        Generalized residuals

        Notes
        -----
        The generalized residuals for the Logit model are defined

        .. math:: y - p

        where :math:`p=cdf(X\\beta)`. This is the same as the `resid_response`
        for the Logit model.
        """
    def get_influence(self):
        """
        Get an instance of MLEInfluence with influence and outlier measures

        Returns
        -------
        infl : MLEInfluence instance
            The instance has methods to calculate the main influence and
            outlier measures as attributes.

        See Also
        --------
        statsmodels.stats.outliers_influence.MLEInfluence
        """

class ProbitResults(BinaryResults):
    __doc__: Incomplete
    def resid_generalized(self):
        """
        Generalized residuals

        Notes
        -----
        The generalized residuals for the Probit model are defined

        .. math:: y\\frac{\\phi(X\\beta)}{\\Phi(X\\beta)}-(1-y)\\frac{\\phi(X\\beta)}{1-\\Phi(X\\beta)}
        """

class L1BinaryResults(BinaryResults):
    __doc__: Incomplete
    trimmed: Incomplete
    nnz_params: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    def __init__(self, model, bnryfit) -> None: ...

class MultinomialResults(DiscreteResults):
    __doc__: Incomplete
    J: Incomplete
    K: Incomplete
    def __init__(self, model, mlefit) -> None: ...
    def pred_table(self):
        '''
        Returns the J x J prediction table.

        Notes
        -----
        pred_table[i,j] refers to the number of times "i" was observed and
        the model predicted "j". Correct predictions are along the diagonal.
        '''
    def bse(self): ...
    def aic(self): ...
    def bic(self): ...
    def conf_int(self, alpha: float = 0.05, cols: Incomplete | None = None): ...
    def get_prediction(self) -> None:
        """Not implemented for Multinomial
        """
    def margeff(self) -> None: ...
    def resid_misclassified(self):
        """
        Residuals indicating which observations are misclassified.

        Notes
        -----
        The residuals for the multinomial model are defined as

        .. math:: argmax(y_i) \\neq argmax(p_i)

        where :math:`argmax(y_i)` is the index of the category for the
        endogenous variable and :math:`argmax(p_i)` is the index of the
        predicted probabilities for each category. That is, the residual
        is a binary indicator that is 0 if the category with the highest
        predicted probability is the same as that of the observed variable
        and 1 otherwise.
        """
    def summary2(self, alpha: float = 0.05, float_format: str = '%.4f'):
        """Experimental function to summarize regression results

        Parameters
        ----------
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

class L1MultinomialResults(MultinomialResults):
    __doc__: Incomplete
    trimmed: Incomplete
    nnz_params: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    def __init__(self, model, mlefit) -> None: ...

class OrderedResultsWrapper(lm.RegressionResultsWrapper): ...
class CountResultsWrapper(lm.RegressionResultsWrapper): ...
class NegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class NegativeBinomialPResultsWrapper(lm.RegressionResultsWrapper): ...
class GeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class PoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1CountResultsWrapper(lm.RegressionResultsWrapper): ...
class L1PoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class L1NegativeBinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class L1GeneralizedPoissonResultsWrapper(lm.RegressionResultsWrapper): ...
class BinaryResultsWrapper(lm.RegressionResultsWrapper): ...
class L1BinaryResultsWrapper(lm.RegressionResultsWrapper): ...
class MultinomialResultsWrapper(lm.RegressionResultsWrapper): ...
class L1MultinomialResultsWrapper(lm.RegressionResultsWrapper): ...
