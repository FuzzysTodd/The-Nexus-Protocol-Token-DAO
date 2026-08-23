import statsmodels.base.wrapper as wrap
import statsmodels.tsa.base.prediction as pred
import statsmodels.tsa.base.tsa_model as tsbase
from .initialization import Initialization as Initialization
from .kalman_filter import INVERT_UNIVARIATE as INVERT_UNIVARIATE, MEMORY_CONSERVE as MEMORY_CONSERVE, SOLVE_LU as SOLVE_LU
from .kalman_smoother import SmootherResults as SmootherResults
from .news import NewsResults as NewsResults
from .simulation_smoother import SimulationSmoother as SimulationSmoother
from .tools import concat as concat, get_impact_dates as get_impact_dates, prepare_exog as prepare_exog
from _typeshed import Incomplete
from collections.abc import Generator
from statsmodels.base.data import PandasData as PandasData
from statsmodels.compat.pandas import is_int_index as is_int_index
from statsmodels.tools.decorators import cache_readonly as cache_readonly
from statsmodels.tools.eval_measures import aic as aic, aicc as aicc, bic as bic, hqic as hqic
from statsmodels.tools.numdiff import approx_fprime as approx_fprime, approx_fprime_cs as approx_fprime_cs, approx_hess_cs as approx_hess_cs
from statsmodels.tools.sm_exceptions import PrecisionWarning as PrecisionWarning, ValueWarning as ValueWarning
from statsmodels.tools.tools import Bunch as Bunch, pinv_extended as pinv_extended

class MLEModel(tsbase.TimeSeriesModel):
    """
    State space model for maximum likelihood estimation

    Parameters
    ----------
    endog : array_like
        The observed time-series process :math:`y`
    k_states : int
        The dimension of the unobserved state process.
    exog : array_like, optional
        Array of exogenous regressors, shaped nobs x k. Default is no
        exogenous regressors.
    dates : array_like of datetime, optional
        An array-like object of datetime objects. If a Pandas object is given
        for endog, it is assumed to have a DateIndex.
    freq : str, optional
        The frequency of the time-series. A Pandas offset or 'B', 'D', 'W',
        'M', 'A', or 'Q'. This is optional if dates are given.
    **kwargs
        Keyword arguments may be used to provide default values for state space
        matrices or for Kalman filtering options. See `Representation`, and
        `KalmanFilter` for more details.

    Attributes
    ----------
    ssm : statsmodels.tsa.statespace.kalman_filter.KalmanFilter
        Underlying state space representation.

    See Also
    --------
    statsmodels.tsa.statespace.mlemodel.MLEResults
    statsmodels.tsa.statespace.kalman_filter.KalmanFilter
    statsmodels.tsa.statespace.representation.Representation

    Notes
    -----
    This class wraps the state space model with Kalman filtering to add in
    functionality for maximum likelihood estimation. In particular, it adds
    the concept of updating the state space representation based on a defined
    set of parameters, through the `update` method or `updater` attribute (see
    below for more details on which to use when), and it adds a `fit` method
    which uses a numerical optimizer to select the parameters that maximize
    the likelihood of the model.

    The `start_params` `update` method must be overridden in the
    child class (and the `transform` and `untransform` methods, if needed).
    """
    nobs: Incomplete
    k_states: Incomplete
    def __init__(self, endog, k_states, exog: Incomplete | None = None, dates: Incomplete | None = None, freq: Incomplete | None = None, **kwargs) -> None: ...
    def prepare_data(self):
        """
        Prepare data for use in the state space representation
        """
    ssm: Incomplete
    k_endog: Incomplete
    def initialize_statespace(self, **kwargs) -> None:
        """
        Initialize the state space representation

        Parameters
        ----------
        **kwargs
            Additional keyword arguments to pass to the state space class
            constructor.
        """
    def __setitem__(self, key, value) -> None: ...
    def __getitem__(self, key): ...
    def clone(self, endog, exog: Incomplete | None = None, **kwargs) -> None:
        """
        Clone state space model with new data and optionally new specification

        Parameters
        ----------
        endog : array_like
            The observed time-series process :math:`y`
        k_states : int
            The dimension of the unobserved state process.
        exog : array_like, optional
            Array of exogenous regressors, shaped nobs x k. Default is no
            exogenous regressors.
        kwargs
            Keyword arguments to pass to the new model class to change the
            model specification.

        Returns
        -------
        model : MLEModel subclass

        Notes
        -----
        This method must be implemented
        """
    def set_filter_method(self, filter_method: Incomplete | None = None, **kwargs) -> None:
        """
        Set the filtering method

        The filtering method controls aspects of which Kalman filtering
        approach will be used.

        Parameters
        ----------
        filter_method : int, optional
            Bitmask value to set the filter method to. See notes for details.
        **kwargs
            Keyword arguments may be used to influence the filter method by
            setting individual boolean flags. See notes for details.

        Notes
        -----
        This method is rarely used. See the corresponding function in the
        `KalmanFilter` class for details.
        """
    def set_inversion_method(self, inversion_method: Incomplete | None = None, **kwargs) -> None:
        """
        Set the inversion method

        The Kalman filter may contain one matrix inversion: that of the
        forecast error covariance matrix. The inversion method controls how and
        if that inverse is performed.

        Parameters
        ----------
        inversion_method : int, optional
            Bitmask value to set the inversion method to. See notes for
            details.
        **kwargs
            Keyword arguments may be used to influence the inversion method by
            setting individual boolean flags. See notes for details.

        Notes
        -----
        This method is rarely used. See the corresponding function in the
        `KalmanFilter` class for details.
        """
    def set_stability_method(self, stability_method: Incomplete | None = None, **kwargs) -> None:
        """
        Set the numerical stability method

        The Kalman filter is a recursive algorithm that may in some cases
        suffer issues with numerical stability. The stability method controls
        what, if any, measures are taken to promote stability.

        Parameters
        ----------
        stability_method : int, optional
            Bitmask value to set the stability method to. See notes for
            details.
        **kwargs
            Keyword arguments may be used to influence the stability method by
            setting individual boolean flags. See notes for details.

        Notes
        -----
        This method is rarely used. See the corresponding function in the
        `KalmanFilter` class for details.
        """
    def set_conserve_memory(self, conserve_memory: Incomplete | None = None, **kwargs) -> None:
        """
        Set the memory conservation method

        By default, the Kalman filter computes a number of intermediate
        matrices at each iteration. The memory conservation options control
        which of those matrices are stored.

        Parameters
        ----------
        conserve_memory : int, optional
            Bitmask value to set the memory conservation method to. See notes
            for details.
        **kwargs
            Keyword arguments may be used to influence the memory conservation
            method by setting individual boolean flags.

        Notes
        -----
        This method is rarely used. See the corresponding function in the
        `KalmanFilter` class for details.
        """
    def set_smoother_output(self, smoother_output: Incomplete | None = None, **kwargs) -> None:
        """
        Set the smoother output

        The smoother can produce several types of results. The smoother output
        variable controls which are calculated and returned.

        Parameters
        ----------
        smoother_output : int, optional
            Bitmask value to set the smoother output to. See notes for details.
        **kwargs
            Keyword arguments may be used to influence the smoother output by
            setting individual boolean flags.

        Notes
        -----
        This method is rarely used. See the corresponding function in the
        `KalmanSmoother` class for details.
        """
    def initialize_known(self, initial_state, initial_state_cov) -> None:
        """Initialize known"""
    def initialize_approximate_diffuse(self, variance: Incomplete | None = None) -> None:
        """Initialize approximate diffuse"""
    def initialize_stationary(self) -> None:
        """Initialize stationary"""
    @property
    def initialization(self): ...
    @initialization.setter
    def initialization(self, value) -> None: ...
    @property
    def initial_variance(self): ...
    @initial_variance.setter
    def initial_variance(self, value) -> None: ...
    @property
    def loglikelihood_burn(self): ...
    @loglikelihood_burn.setter
    def loglikelihood_burn(self, value) -> None: ...
    @property
    def tolerance(self): ...
    @tolerance.setter
    def tolerance(self, value) -> None: ...
    def fix_params(self, params) -> Generator[None, None, None]:
        """
        Fix parameters to specific values (context manager)

        Parameters
        ----------
        params : dict
            Dictionary describing the fixed parameter values, of the form
            `param_name: fixed_value`. See the `param_names` property for valid
            parameter names.

        Examples
        --------
        >>> mod = sm.tsa.SARIMAX(endog, order=(1, 0, 1))
        >>> with mod.fix_params({'ar.L1': 0.5}):
                res = mod.fit()
        """
    def fit(self, start_params: Incomplete | None = None, transformed: bool = True, includes_fixed: bool = False, cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, method: str = 'lbfgs', maxiter: int = 50, full_output: int = 1, disp: int = 5, callback: Incomplete | None = None, return_params: bool = False, optim_score: Incomplete | None = None, optim_complex_step: Incomplete | None = None, optim_hessian: Incomplete | None = None, flags: Incomplete | None = None, low_memory: bool = False, **kwargs):
        """
        Fits the model by maximum likelihood via Kalman filter.

        Parameters
        ----------
        start_params : array_like, optional
            Initial guess of the solution for the loglikelihood maximization.
            If None, the default is given by Model.start_params.
        transformed : bool, optional
            Whether or not `start_params` is already transformed. Default is
            True.
        includes_fixed : bool, optional
            If parameters were previously fixed with the `fix_params` method,
            this argument describes whether or not `start_params` also includes
            the fixed parameters, in addition to the free parameters. Default
            is False.
        cov_type : str, optional
            The `cov_type` keyword governs the method for calculating the
            covariance matrix of parameter estimates. Can be one of:

            - 'opg' for the outer product of gradient estimator
            - 'oim' for the observed information matrix estimator, calculated
              using the method of Harvey (1989)
            - 'approx' for the observed information matrix estimator,
              calculated using a numerical approximation of the Hessian matrix.
            - 'robust' for an approximate (quasi-maximum likelihood) covariance
              matrix that may be valid even in the presence of some
              misspecifications. Intermediate calculations use the 'oim'
              method.
            - 'robust_approx' is the same as 'robust' except that the
              intermediate calculations use the 'approx' method.
            - 'none' for no covariance matrix calculation.

            Default is 'opg' unless memory conservation is used to avoid
            computing the loglikelihood values for each observation, in which
            case the default is 'approx'.
        cov_kwds : dict or None, optional
            A dictionary of arguments affecting covariance matrix computation.

            **opg, oim, approx, robust, robust_approx**

            - 'approx_complex_step' : bool, optional - If True, numerical
              approximations are computed using complex-step methods. If False,
              numerical approximations are computed using finite difference
              methods. Default is True.
            - 'approx_centered' : bool, optional - If True, numerical
              approximations computed using finite difference methods use a
              centered approximation. Default is False.
        method : str, optional
            The `method` determines which solver from `scipy.optimize`
            is used, and it can be chosen from among the following strings:

            - 'newton' for Newton-Raphson
            - 'nm' for Nelder-Mead
            - 'bfgs' for Broyden-Fletcher-Goldfarb-Shanno (BFGS)
            - 'lbfgs' for limited-memory BFGS with optional box constraints
            - 'powell' for modified Powell's method
            - 'cg' for conjugate gradient
            - 'ncg' for Newton-conjugate gradient
            - 'basinhopping' for global basin-hopping solver

            The explicit arguments in `fit` are passed to the solver,
            with the exception of the basin-hopping solver. Each
            solver has several optional arguments that are not the same across
            solvers. See the notes section below (or scipy.optimize) for the
            available arguments and for the list of explicit arguments that the
            basin-hopping solver supports.
        maxiter : int, optional
            The maximum number of iterations to perform.
        full_output : bool, optional
            Set to True to have all available output in the Results object's
            mle_retvals attribute. The output is dependent on the solver.
            See LikelihoodModelResults notes section for more information.
        disp : bool, optional
            Set to True to print convergence messages.
        callback : callable callback(xk), optional
            Called after each iteration, as callback(xk), where xk is the
            current parameter vector.
        return_params : bool, optional
            Whether or not to return only the array of maximizing parameters.
            Default is False.
        optim_score : {'harvey', 'approx'} or None, optional
            The method by which the score vector is calculated. 'harvey' uses
            the method from Harvey (1989), 'approx' uses either finite
            difference or complex step differentiation depending upon the
            value of `optim_complex_step`, and None uses the built-in gradient
            approximation of the optimizer. Default is None. This keyword is
            only relevant if the optimization method uses the score.
        optim_complex_step : bool, optional
            Whether or not to use complex step differentiation when
            approximating the score; if False, finite difference approximation
            is used. Default is True. This keyword is only relevant if
            `optim_score` is set to 'harvey' or 'approx'.
        optim_hessian : {'opg','oim','approx'}, optional
            The method by which the Hessian is numerically approximated. 'opg'
            uses outer product of gradients, 'oim' uses the information
            matrix formula from Harvey (1989), and 'approx' uses numerical
            approximation. This keyword is only relevant if the
            optimization method uses the Hessian matrix.
        low_memory : bool, optional
            If set to True, techniques are applied to substantially reduce
            memory usage. If used, some features of the results object will
            not be available (including smoothed results and in-sample
            prediction), although out-of-sample forecasting is possible.
            Default is False.
        **kwargs
            Additional keyword arguments to pass to the optimizer.

        Returns
        -------
        results
            Results object holding results from fitting a state space model.

        See Also
        --------
        statsmodels.base.model.LikelihoodModel.fit
        statsmodels.tsa.statespace.mlemodel.MLEResults
        statsmodels.tsa.statespace.structural.UnobservedComponentsResults
        """
    def fit_constrained(self, constraints, start_params: Incomplete | None = None, **fit_kwds):
        """
        Fit the model with some parameters subject to equality constraints.

        Parameters
        ----------
        constraints : dict
            Dictionary of constraints, of the form `param_name: fixed_value`.
            See the `param_names` property for valid parameter names.
        start_params : array_like, optional
            Initial guess of the solution for the loglikelihood maximization.
            If None, the default is given by Model.start_params.
        **fit_kwds : keyword arguments
            fit_kwds are used in the optimization of the remaining parameters.

        Returns
        -------
        results : Results instance

        Examples
        --------
        >>> mod = sm.tsa.SARIMAX(endog, order=(1, 0, 1))
        >>> res = mod.fit_constrained({'ar.L1': 0.5})
        """
    def filter(self, params, transformed: bool = True, includes_fixed: bool = False, complex_step: bool = False, cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, return_ssm: bool = False, results_class: Incomplete | None = None, results_wrapper_class: Incomplete | None = None, low_memory: bool = False, **kwargs):
        """
        Kalman filtering

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the loglikelihood
            function.
        transformed : bool, optional
            Whether or not `params` is already transformed. Default is True.
        return_ssm : bool,optional
            Whether or not to return only the state space output or a full
            results object. Default is to return a full results object.
        cov_type : str, optional
            See `MLEResults.fit` for a description of covariance matrix types
            for results object.
        cov_kwds : dict or None, optional
            See `MLEResults.get_robustcov_results` for a description required
            keywords for alternative covariance estimators
        low_memory : bool, optional
            If set to True, techniques are applied to substantially reduce
            memory usage. If used, some features of the results object will
            not be available (including in-sample prediction), although
            out-of-sample forecasting is possible. Default is False.
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.
        """
    def smooth(self, params, transformed: bool = True, includes_fixed: bool = False, complex_step: bool = False, cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, return_ssm: bool = False, results_class: Incomplete | None = None, results_wrapper_class: Incomplete | None = None, **kwargs):
        """
        Kalman smoothing

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the loglikelihood
            function.
        transformed : bool, optional
            Whether or not `params` is already transformed. Default is True.
        return_ssm : bool,optional
            Whether or not to return only the state space output or a full
            results object. Default is to return a full results object.
        cov_type : str, optional
            See `MLEResults.fit` for a description of covariance matrix types
            for results object.
        cov_kwds : dict or None, optional
            See `MLEResults.get_robustcov_results` for a description required
            keywords for alternative covariance estimators
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.
        """
    def loglike(self, params, *args, **kwargs):
        """
        Loglikelihood evaluation

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the loglikelihood
            function.
        transformed : bool, optional
            Whether or not `params` is already transformed. Default is True.
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.

        See Also
        --------
        update : modifies the internal state of the state space model to
                 reflect new params

        Notes
        -----
        [1]_ recommend maximizing the average likelihood to avoid scale issues;
        this is done automatically by the base Model fit method.

        References
        ----------
        .. [1] Koopman, Siem Jan, Neil Shephard, and Jurgen A. Doornik. 1999.
           Statistical Algorithms for Models in State Space Using SsfPack 2.2.
           Econometrics Journal 2 (1): 107-60. doi:10.1111/1368-423X.00023.
        """
    def loglikeobs(self, params, transformed: bool = True, includes_fixed: bool = False, complex_step: bool = False, **kwargs):
        """
        Loglikelihood evaluation

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the loglikelihood
            function.
        transformed : bool, optional
            Whether or not `params` is already transformed. Default is True.
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.

        See Also
        --------
        update : modifies the internal state of the Model to reflect new params

        Notes
        -----
        [1]_ recommend maximizing the average likelihood to avoid scale issues;
        this is done automatically by the base Model fit method.

        References
        ----------
        .. [1] Koopman, Siem Jan, Neil Shephard, and Jurgen A. Doornik. 1999.
           Statistical Algorithms for Models in State Space Using SsfPack 2.2.
           Econometrics Journal 2 (1): 107-60. doi:10.1111/1368-423X.00023.
        """
    def simulation_smoother(self, simulation_output: Incomplete | None = None, **kwargs):
        """
        Retrieve a simulation smoother for the state space model.

        Parameters
        ----------
        simulation_output : int, optional
            Determines which simulation smoother output is calculated.
            Default is all (including state and disturbances).
        **kwargs
            Additional keyword arguments, used to set the simulation output.
            See `set_simulation_output` for more details.

        Returns
        -------
        SimulationSmoothResults
        """
    def observed_information_matrix(self, params, transformed: bool = True, includes_fixed: bool = False, approx_complex_step: Incomplete | None = None, approx_centered: bool = False, **kwargs):
        """
        Observed information matrix

        Parameters
        ----------
        params : array_like, optional
            Array of parameters at which to evaluate the loglikelihood
            function.
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.

        Notes
        -----
        This method is from Harvey (1989), which shows that the information
        matrix only depends on terms from the gradient. This implementation is
        partially analytic and partially numeric approximation, therefore,
        because it uses the analytic formula for the information matrix, with
        numerically computed elements of the gradient.

        References
        ----------
        Harvey, Andrew C. 1990.
        Forecasting, Structural Time Series Models and the Kalman Filter.
        Cambridge University Press.
        """
    def opg_information_matrix(self, params, transformed: bool = True, includes_fixed: bool = False, approx_complex_step: Incomplete | None = None, **kwargs):
        """
        Outer product of gradients information matrix

        Parameters
        ----------
        params : array_like, optional
            Array of parameters at which to evaluate the loglikelihood
            function.
        **kwargs
            Additional arguments to the `loglikeobs` method.

        References
        ----------
        Berndt, Ernst R., Bronwyn Hall, Robert Hall, and Jerry Hausman. 1974.
        Estimation and Inference in Nonlinear Structural Models.
        NBER Chapters. National Bureau of Economic Research, Inc.
        """
    def score(self, params, *args, **kwargs):
        """
        Compute the score function at params.

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the score.
        *args
            Additional positional arguments to the `loglike` method.
        **kwargs
            Additional keyword arguments to the `loglike` method.

        Returns
        -------
        score : ndarray
            Score, evaluated at `params`.

        Notes
        -----
        This is a numerical approximation, calculated using first-order complex
        step differentiation on the `loglike` method.

        Both args and kwargs are necessary because the optimizer from
        `fit` must call this function and only supports passing arguments via
        args (for example `scipy.optimize.fmin_l_bfgs`).
        """
    def score_obs(self, params, method: str = 'approx', transformed: bool = True, includes_fixed: bool = False, approx_complex_step: Incomplete | None = None, approx_centered: bool = False, **kwargs):
        """
        Compute the score per observation, evaluated at params

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the score.
        **kwargs
            Additional arguments to the `loglike` method.

        Returns
        -------
        score : ndarray
            Score per observation, evaluated at `params`.

        Notes
        -----
        This is a numerical approximation, calculated using first-order complex
        step differentiation on the `loglikeobs` method.
        """
    def hessian(self, params, *args, **kwargs):
        """
        Hessian matrix of the likelihood function, evaluated at the given
        parameters

        Parameters
        ----------
        params : array_like
            Array of parameters at which to evaluate the hessian.
        *args
            Additional positional arguments to the `loglike` method.
        **kwargs
            Additional keyword arguments to the `loglike` method.

        Returns
        -------
        hessian : ndarray
            Hessian matrix evaluated at `params`

        Notes
        -----
        This is a numerical approximation.

        Both args and kwargs are necessary because the optimizer from
        `fit` must call this function and only supports passing arguments via
        args (for example `scipy.optimize.fmin_l_bfgs`).
        """
    @property
    def start_params(self):
        """
        (array) Starting parameters for maximum likelihood estimation.
        """
    @property
    def param_names(self):
        """
        (list of str) List of human readable parameter names (for parameters
        actually included in the model).
        """
    @property
    def state_names(self):
        """
        (list of str) List of human readable names for unobserved states.
        """
    def transform_jacobian(self, unconstrained, approx_centered: bool = False):
        """
        Jacobian matrix for the parameter transformation function

        Parameters
        ----------
        unconstrained : array_like
            Array of unconstrained parameters used by the optimizer.

        Returns
        -------
        jacobian : ndarray
            Jacobian matrix of the transformation, evaluated at `unconstrained`

        See Also
        --------
        transform_params

        Notes
        -----
        This is a numerical approximation using finite differences. Note that
        in general complex step methods cannot be used because it is not
        guaranteed that the `transform_params` method is a real function (e.g.
        if Cholesky decomposition is used).
        """
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
        This is a noop in the base class, subclasses should override where
        appropriate.
        """
    def untransform_params(self, constrained):
        """
        Transform constrained parameters used in likelihood evaluation
        to unconstrained parameters used by the optimizer

        Parameters
        ----------
        constrained : array_like
            Array of constrained parameters used in likelihood evaluation, to
            be transformed.

        Returns
        -------
        unconstrained : array_like
            Array of unconstrained parameters used by the optimizer.

        Notes
        -----
        This is a noop in the base class, subclasses should override where
        appropriate.
        """
    def handle_params(self, params, transformed: bool = True, includes_fixed: bool = False, return_jacobian: bool = False):
        """
        Ensure model parameters satisfy shape and other requirements
        """
    def update(self, params, transformed: bool = True, includes_fixed: bool = False, complex_step: bool = False):
        """
        Update the parameters of the model

        Parameters
        ----------
        params : array_like
            Array of new parameters.
        transformed : bool, optional
            Whether or not `params` is already transformed. If set to False,
            `transform_params` is called. Default is True.

        Returns
        -------
        params : array_like
            Array of parameters.

        Notes
        -----
        Since Model is a base class, this method should be overridden by
        subclasses to perform actual updating steps.
        """
    def simulate(self, params, nsimulations, measurement_shocks: Incomplete | None = None, state_shocks: Incomplete | None = None, initial_state: Incomplete | None = None, anchor: Incomplete | None = None, repetitions: Incomplete | None = None, exog: Incomplete | None = None, extend_model: Incomplete | None = None, extend_kwargs: Incomplete | None = None, transformed: bool = True, includes_fixed: bool = False, pretransformed_measurement_shocks: bool = True, pretransformed_state_shocks: bool = True, pretransformed_initial_state: bool = True, random_state: Incomplete | None = None, **kwargs):
        '''
        Simulate a new time series following the state space model

        Parameters
        ----------
        params : array_like
            Array of parameters to use in constructing the state space
            representation to use when simulating.
        nsimulations : int
            The number of observations to simulate. If the model is
            time-invariant this can be any number. If the model is
            time-varying, then this number must be less than or equal to the
            number of observations.
        measurement_shocks : array_like, optional
            If specified, these are the shocks to the measurement equation,
            :math:`\\varepsilon_t`. If unspecified, these are automatically
            generated using a pseudo-random number generator. If specified,
            must be shaped `nsimulations` x `k_endog`, where `k_endog` is the
            same as in the state space model.
        state_shocks : array_like, optional
            If specified, these are the shocks to the state equation,
            :math:`\\eta_t`. If unspecified, these are automatically
            generated using a pseudo-random number generator. If specified,
            must be shaped `nsimulations` x `k_posdef` where `k_posdef` is the
            same as in the state space model.
        initial_state : array_like, optional
            If specified, this is the initial state vector to use in
            simulation, which should be shaped (`k_states` x 1), where
            `k_states` is the same as in the state space model. If unspecified,
            but the model has been initialized, then that initialization is
            used. This must be specified if `anchor` is anything other than
            "start" or 0 (or else you can use the `simulate` method on a
            results object rather than on the model object).
        anchor : int, str, or datetime, optional
            First period for simulation. The simulation will be conditional on
            all existing datapoints prior to the `anchor`.  Type depends on the
            index of the given `endog` in the model. Two special cases are the
            strings \'start\' and \'end\'. `start` refers to beginning the
            simulation at the first period of the sample, and `end` refers to
            beginning the simulation at the first period after the sample.
            Integer values can run from 0 to `nobs`, or can be negative to
            apply negative indexing. Finally, if a date/time index was provided
            to the model, then this argument can be a date string to parse or a
            datetime type. Default is \'start\'.
        repetitions : int, optional
            Number of simulated paths to generate. Default is 1 simulated path.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        transformed : bool, optional
            Whether or not `params` is already transformed. Default is
            True.
        includes_fixed : bool, optional
            If parameters were previously fixed with the `fix_params` method,
            this argument describes whether or not `params` also includes
            the fixed parameters, in addition to the free parameters. Default
            is False.
        pretransformed_measurement_shocks : bool, optional
            If `measurement_shocks` is provided, this flag indicates whether it
            should be directly used as the shocks. If False, then it is assumed
            to contain draws from the standard Normal distribution that must be
            transformed using the `obs_cov` covariance matrix. Default is True.
        pretransformed_state_shocks : bool, optional
            If `state_shocks` is provided, this flag indicates whether it
            should be directly used as the shocks. If False, then it is assumed
            to contain draws from the standard Normal distribution that must be
            transformed using the `state_cov` covariance matrix. Default is
            True.
        pretransformed_initial_state : bool, optional
            If `initial_state` is provided, this flag indicates whether it
            should be directly used as the initial_state. If False, then it is
            assumed to contain draws from the standard Normal distribution that
            must be transformed using the `initial_state_cov` covariance
            matrix. Default is True.
        random_state : {None, int, Generator, RandomState}, optional
            If `seed` is None (or `np.random`), the
            class:``~numpy.random.RandomState`` singleton is used.
            If `seed` is an int, a new class:``~numpy.random.RandomState``
            instance is used, seeded with `seed`.
            If `seed` is already a class:``~numpy.random.Generator`` or
            class:``~numpy.random.RandomState`` instance then that instance is
            used.

        Returns
        -------
        simulated_obs : ndarray
            An array of simulated observations. If `repetitions=None`, then it
            will be shaped (nsimulations x k_endog) or (nsimulations,) if
            `k_endog=1`. Otherwise it will be shaped
            (nsimulations x k_endog x repetitions). If the model was given
            Pandas input then the output will be a Pandas object. If
            `k_endog > 1` and `repetitions` is not None, then the output will
            be a Pandas DataFrame that has a MultiIndex for the columns, with
            the first level containing the names of the `endog` variables and
            the second level containing the repetition number.

        See Also
        --------
        impulse_responses
            Impulse response functions
        '''
    def impulse_responses(self, params, steps: int = 1, impulse: int = 0, orthogonalized: bool = False, cumulative: bool = False, anchor: Incomplete | None = None, exog: Incomplete | None = None, extend_model: Incomplete | None = None, extend_kwargs: Incomplete | None = None, transformed: bool = True, includes_fixed: bool = False, **kwargs):
        '''
        Impulse response function

        Parameters
        ----------
        params : array_like
            Array of model parameters.
        steps : int, optional
            The number of steps for which impulse responses are calculated.
            Default is 1. Note that for time-invariant models, the initial
            impulse is not counted as a step, so if `steps=1`, the output will
            have 2 entries.
        impulse : int, str or array_like
            If an integer, the state innovation to pulse; must be between 0
            and `k_posdef-1`. If a str, it indicates which column of df
            the unit (1) impulse is given.
            Alternatively, a custom impulse vector may be provided; must be
            shaped `k_posdef x 1`.
        orthogonalized : bool, optional
            Whether or not to perform impulse using orthogonalized innovations.
            Note that this will also affect custum `impulse` vectors. Default
            is False.
        cumulative : bool, optional
            Whether or not to return cumulative impulse responses. Default is
            False.
        anchor : int, str, or datetime, optional
            Time point within the sample for the state innovation impulse. Type
            depends on the index of the given `endog` in the model. Two special
            cases are the strings \'start\' and \'end\', which refer to setting the
            impulse at the first and last points of the sample, respectively.
            Integer values can run from 0 to `nobs - 1`, or can be negative to
            apply negative indexing. Finally, if a date/time index was provided
            to the model, then this argument can be a date string to parse or a
            datetime type. Default is \'start\'.
        exog : array_like, optional
            New observations of exogenous regressors for our-of-sample periods,
            if applicable.
        transformed : bool, optional
            Whether or not `params` is already transformed. Default is
            True.
        includes_fixed : bool, optional
            If parameters were previously fixed with the `fix_params` method,
            this argument describes whether or not `params` also includes
            the fixed parameters, in addition to the free parameters. Default
            is False.
        **kwargs
            If the model has time-varying design or transition matrices and the
            combination of `anchor` and `steps` implies creating impulse
            responses for the out-of-sample period, then these matrices must
            have updated values provided for the out-of-sample steps. For
            example, if `design` is a time-varying component, `nobs` is 10,
            `anchor=1`, and `steps` is 15, a (`k_endog` x `k_states` x 7)
            matrix must be provided with the new design matrix values.

        Returns
        -------
        impulse_responses : ndarray
            Responses for each endogenous variable due to the impulse
            given by the `impulse` argument. For a time-invariant model, the
            impulse responses are given for `steps + 1` elements (this gives
            the "initial impulse" followed by `steps` responses for the
            important cases of VAR and SARIMAX models), while for time-varying
            models the impulse responses are only given for `steps` elements
            (to avoid having to unexpectedly provide updated time-varying
            matrices).

        See Also
        --------
        simulate
            Simulate a time series according to the given state space model,
            optionally with specified series for the innovations.

        Notes
        -----
        Intercepts in the measurement and state equation are ignored when
        calculating impulse responses.

        TODO: add an option to allow changing the ordering for the
              orthogonalized option. Will require permuting matrices when
              constructing the extended model.
        '''
    @classmethod
    def from_formula(cls, formula, data, subset: Incomplete | None = None) -> None:
        """
        Not implemented for state space models
        """

class MLEResults(tsbase.TimeSeriesModelResults):
    """
    Class to hold results from fitting a state space model.

    Parameters
    ----------
    model : MLEModel instance
        The fitted model instance
    params : ndarray
        Fitted parameters
    filter_results : KalmanFilter instance
        The underlying state space model and Kalman filter output

    Attributes
    ----------
    model : Model instance
        A reference to the model that was fit.
    filter_results : KalmanFilter instance
        The underlying state space model and Kalman filter output
    nobs : float
        The number of observations used to fit the model.
    params : ndarray
        The parameters of the model.
    scale : float
        This is currently set to 1.0 unless the model uses concentrated
        filtering.

    See Also
    --------
    MLEModel
    statsmodels.tsa.statespace.kalman_filter.FilterResults
    statsmodels.tsa.statespace.representation.FrozenRepresentation
    """
    data: Incomplete
    fixed_params: Incomplete
    param_names: Incomplete
    filter_results: Incomplete
    smoother_results: Incomplete
    nobs: Incomplete
    nobs_diffuse: Incomplete
    nobs_effective: Incomplete
    k_diffuse_states: Incomplete
    df_model: Incomplete
    df_resid: Incomplete
    cov_kwds: Incomplete
    cov_type: Incomplete
    cov_params_default: Incomplete
    forecasts: Incomplete
    forecasts_error: Incomplete
    forecasts_error_cov: Incomplete
    predicted_state: Incomplete
    predicted_state_cov: Incomplete
    filtered_state: Incomplete
    filtered_state_cov: Incomplete
    standardized_forecasts_error: Incomplete
    def __init__(self, model, params, results, cov_type: Incomplete | None = None, cov_kwds: Incomplete | None = None, **kwargs) -> None: ...
    def aic(self):
        """
        (float) Akaike Information Criterion
        """
    def aicc(self):
        """
        (float) Akaike Information Criterion with small sample correction
        """
    def bic(self):
        """
        (float) Bayes Information Criterion
        """
    def cov_params_approx(self):
        """
        (array) The variance / covariance matrix. Computed using the numerical
        Hessian approximated by complex step or finite differences methods.
        """
    def cov_params_oim(self):
        """
        (array) The variance / covariance matrix. Computed using the method
        from Harvey (1989).
        """
    def cov_params_opg(self):
        """
        (array) The variance / covariance matrix. Computed using the outer
        product of gradients method.
        """
    def cov_params_robust(self):
        """
        (array) The QMLE variance / covariance matrix. Alias for
        `cov_params_robust_oim`
        """
    def cov_params_robust_oim(self):
        """
        (array) The QMLE variance / covariance matrix. Computed using the
        method from Harvey (1989) as the evaluated hessian.
        """
    def cov_params_robust_approx(self):
        """
        (array) The QMLE variance / covariance matrix. Computed using the
        numerical Hessian as the evaluated hessian.
        """
    def info_criteria(self, criteria, method: str = 'standard'):
        """
        Information criteria

        Parameters
        ----------
        criteria : {'aic', 'bic', 'hqic'}
            The information criteria to compute.
        method : {'standard', 'lutkepohl'}
            The method for information criteria computation. Default is
            'standard' method; 'lutkepohl' computes the information criteria
            as in Lütkepohl (2007). See Notes for formulas.

        Notes
        -----
        The `'standard'` formulas are:

        .. math::

            AIC & = -2 \\log L(Y_n | \\hat \\psi) + 2 k \\\\\n            BIC & = -2 \\log L(Y_n | \\hat \\psi) + k \\log n \\\\\n            HQIC & = -2 \\log L(Y_n | \\hat \\psi) + 2 k \\log \\log n \\\\\n
        where :math:`\\hat \\psi` are the maximum likelihood estimates of the
        parameters, :math:`n` is the number of observations, and `k` is the
        number of estimated parameters.

        Note that the `'standard'` formulas are returned from the `aic`, `bic`,
        and `hqic` results attributes.

        The `'lutkepohl'` formulas are (Lütkepohl, 2010):

        .. math::

            AIC_L & = \\log | Q | + \\frac{2 k}{n} \\\\\n            BIC_L & = \\log | Q | + \\frac{k \\log n}{n} \\\\\n            HQIC_L & = \\log | Q | + \\frac{2 k \\log \\log n}{n} \\\\\n
        where :math:`Q` is the state covariance matrix. Note that the Lütkepohl
        definitions do not apply to all state space models, and should be used
        with care outside of SARIMAX and VARMAX models.

        References
        ----------
        .. [*] Lütkepohl, Helmut. 2007. *New Introduction to Multiple Time*
           *Series Analysis.* Berlin: Springer.
        """
    def fittedvalues(self):
        """
        (array) The predicted values of the model. An (nobs x k_endog) array.
        """
    def hqic(self):
        """
        (float) Hannan-Quinn Information Criterion
        """
    def llf_obs(self):
        """
        (float) The value of the log-likelihood function evaluated at `params`.
        """
    def llf(self):
        """
        (float) The value of the log-likelihood function evaluated at `params`.
        """
    def loglikelihood_burn(self):
        """
        (float) The number of observations during which the likelihood is not
        evaluated.
        """
    def mae(self):
        """
        (float) Mean absolute error
        """
    def mse(self):
        """
        (float) Mean squared error
        """
    def pvalues(self):
        """
        (array) The p-values associated with the z-statistics of the
        coefficients. Note that the coefficients are assumed to have a Normal
        distribution.
        """
    def resid(self):
        """
        (array) The model residuals. An (nobs x k_endog) array.
        """
    @property
    def states(self): ...
    def sse(self):
        """
        (float) Sum of squared errors
        """
    def zvalues(self):
        """
        (array) The z-statistics for the coefficients.
        """
    def test_normality(self, method):
        """
        Test for normality of standardized residuals.

        Null hypothesis is normality.

        Parameters
        ----------
        method : {'jarquebera', None}
            The statistical test for normality. Must be 'jarquebera' for
            Jarque-Bera normality test. If None, an attempt is made to select
            an appropriate test.

        See Also
        --------
        statsmodels.stats.stattools.jarque_bera
            The Jarque-Bera test of normality.

        Notes
        -----
        Let `d` = max(loglikelihood_burn, nobs_diffuse); this test is
        calculated ignoring the first `d` residuals.

        In the case of missing data, the maintained hypothesis is that the
        data are missing completely at random. This test is then run on the
        standardized residuals excluding those corresponding to missing
        observations.
        """
    def test_heteroskedasticity(self, method, alternative: str = 'two-sided', use_f: bool = True):
        """
        Test for heteroskedasticity of standardized residuals

        Tests whether the sum-of-squares in the first third of the sample is
        significantly different than the sum-of-squares in the last third
        of the sample. Analogous to a Goldfeld-Quandt test. The null hypothesis
        is of no heteroskedasticity.

        Parameters
        ----------
        method : {'breakvar', None}
            The statistical test for heteroskedasticity. Must be 'breakvar'
            for test of a break in the variance. If None, an attempt is
            made to select an appropriate test.
        alternative : str, 'increasing', 'decreasing' or 'two-sided'
            This specifies the alternative for the p-value calculation. Default
            is two-sided.
        use_f : bool, optional
            Whether or not to compare against the asymptotic distribution
            (chi-squared) or the approximate small-sample distribution (F).
            Default is True (i.e. default is to compare against an F
            distribution).

        Returns
        -------
        output : ndarray
            An array with `(test_statistic, pvalue)` for each endogenous
            variable. The array is then sized `(k_endog, 2)`. If the method is
            called as `het = res.test_heteroskedasticity()`, then `het[0]` is
            an array of size 2 corresponding to the first endogenous variable,
            where `het[0][0]` is the test statistic, and `het[0][1]` is the
            p-value.

        See Also
        --------
        statsmodels.tsa.stattools.breakvar_heteroskedasticity_test

        Notes
        -----
        The null hypothesis is of no heteroskedasticity.

        For :math:`h = [T/3]`, the test statistic is:

        .. math::

            H(h) = \\sum_{t=T-h+1}^T  \\tilde v_t^2
            \\Bigg / \\sum_{t=d+1}^{d+1+h} \\tilde v_t^2

        where :math:`d` = max(loglikelihood_burn, nobs_diffuse)` (usually
        corresponding to diffuse initialization under either the approximate
        or exact approach).

        This statistic can be tested against an :math:`F(h,h)` distribution.
        Alternatively, :math:`h H(h)` is asymptotically distributed according
        to :math:`\\chi_h^2`; this second test can be applied by passing
        `use_f=True` as an argument.

        See section 5.4 of [1]_ for the above formula and discussion, as well
        as additional details.

        TODO

        - Allow specification of :math:`h`

        References
        ----------
        .. [1] Harvey, Andrew C. 1990. *Forecasting, Structural Time Series*
               *Models and the Kalman Filter.* Cambridge University Press.
        """
    def test_serial_correlation(self, method, df_adjust: bool = False, lags: Incomplete | None = None):
        """
        Ljung-Box test for no serial correlation of standardized residuals

        Null hypothesis is no serial correlation.

        Parameters
        ----------
        method : {'ljungbox','boxpierece', None}
            The statistical test for serial correlation. If None, an attempt is
            made to select an appropriate test.
        lags : None, int or array_like
            If lags is an integer then this is taken to be the largest lag
            that is included, the test result is reported for all smaller lag
            length.
            If lags is a list or array, then all lags are included up to the
            largest lag in the list, however only the tests for the lags in the
            list are reported.
            If lags is None, then the default maxlag is min(10, nobs // 5) for
            non-seasonal models and min(2*m, nobs // 5) for seasonal time
            series where m is the seasonal period.
        df_adjust : bool, optional
            If True, the degrees of freedom consumed by the model is subtracted
            from the degrees-of-freedom used in the test so that the adjusted
            dof for the statistics are lags - model_df. In an ARMA model, this
            value is usually p+q where p is the AR order and q is the MA order.
            When using df_adjust, it is not possible to use tests based on
            fewer than model_df lags.
        Returns
        -------
        output : ndarray
            An array with `(test_statistic, pvalue)` for each endogenous
            variable and each lag. The array is then sized
            `(k_endog, 2, lags)`. If the method is called as
            `ljungbox = res.test_serial_correlation()`, then `ljungbox[i]`
            holds the results of the Ljung-Box test (as would be returned by
            `statsmodels.stats.diagnostic.acorr_ljungbox`) for the `i` th
            endogenous variable.

        See Also
        --------
        statsmodels.stats.diagnostic.acorr_ljungbox
            Ljung-Box test for serial correlation.

        Notes
        -----
        Let `d` = max(loglikelihood_burn, nobs_diffuse); this test is
        calculated ignoring the first `d` residuals.

        Output is nan for any endogenous variable which has missing values.
        """
    def get_prediction(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, information_set: str = 'predicted', signal_only: bool = False, index: Incomplete | None = None, exog: Incomplete | None = None, extend_model: Incomplete | None = None, extend_kwargs: Incomplete | None = None, **kwargs):
        '''
        In-sample prediction and out-of-sample forecasting

        Parameters
        ----------
        start : int, str, or datetime, optional
            Zero-indexed observation number at which to start forecasting,
            i.e., the first forecast is start. Can also be a date string to
            parse or a datetime type. Default is the the zeroth observation.
        end : int, str, or datetime, optional
            Zero-indexed observation number at which to end forecasting, i.e.,
            the last forecast is end. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out of sample prediction. Default is the last observation in
            the sample.
        dynamic : bool, int, str, or datetime, optional
            Integer offset relative to `start` at which to begin dynamic
            prediction. Can also be an absolute date string to parse or a
            datetime type (these are not interpreted as offsets).
            Prior to this observation, true endogenous values will be used for
            prediction; starting with this observation and continuing through
            the end of prediction, forecasted endogenous values will be used
            instead.
        information_set : str, optional
            The information set to condition each prediction on. Default is
            "predicted", which computes predictions of period t values
            conditional on observed data through period t-1; these are
            one-step-ahead predictions, and correspond with the typical
            `fittedvalues` results attribute. Alternatives are "filtered",
            which computes predictions of period t values conditional on
            observed data through period t, and "smoothed", which computes
            predictions of period t values conditional on the entire dataset
            (including also future observations t+1, t+2, ...).
        signal_only : bool, optional
            Whether to compute predictions of only the "signal" component of
            the observation equation. Default is False. For example, the
            observation equation of a time-invariant model is
            :math:`y_t = d + Z \\alpha_t + \\varepsilon_t`, and the "signal"
            component is then :math:`Z \\alpha_t`. If this argument is set to
            True, then predictions of the "signal" :math:`Z \\alpha_t` will be
            returned. Otherwise, the default is for predictions of :math:`y_t`
            to be returned.
        **kwargs
            Additional arguments may required for forecasting beyond the end
            of the sample. See `FilterResults.predict` for more details.

        Returns
        -------
        predictions : PredictionResults
            PredictionResults instance containing in-sample predictions /
            out-of-sample forecasts and results including confidence intervals.

        See Also
        --------
        forecast
            Out-of-sample forecasts.
        predict
            In-sample predictions and out-of-sample forecasts.
        get_forecast
            Out-of-sample forecasts and results including confidence intervals.
        '''
    def get_forecast(self, steps: int = 1, signal_only: bool = False, **kwargs):
        '''
        Out-of-sample forecasts and prediction intervals

        Parameters
        ----------
        steps : int, str, or datetime, optional
            If an integer, the number of steps to forecast from the end of the
            sample. Can also be a date string to parse or a datetime type.
            However, if the dates index does not have a fixed frequency, steps
            must be an integer. Default is 1.
        signal_only : bool, optional
            Whether to compute forecasts of only the "signal" component of
            the observation equation. Default is False. For example, the
            observation equation of a time-invariant model is
            :math:`y_t = d + Z \\alpha_t + \\varepsilon_t`, and the "signal"
            component is then :math:`Z \\alpha_t`. If this argument is set to
            True, then forecasts of the "signal" :math:`Z \\alpha_t` will be
            returned. Otherwise, the default is for forecasts of :math:`y_t`
            to be returned.
        **kwargs
            Additional arguments may required for forecasting beyond the end
            of the sample. See `FilterResults.predict` for more details.

        Returns
        -------
        forecasts : PredictionResults
            PredictionResults instance containing out-of-sample forecasts and
            results including confidence intervals.

        See also
        --------
        forecast
            Out-of-sample forecasts.
        predict
            In-sample predictions and out-of-sample forecasts.
        get_prediction
            In-sample predictions / out-of-sample forecasts and results
            including confidence intervals.
        '''
    def predict(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: bool = False, information_set: str = 'predicted', signal_only: bool = False, **kwargs):
        '''
        In-sample prediction and out-of-sample forecasting

        Parameters
        ----------
        start : {int, str,datetime}, optional
            Zero-indexed observation number at which to start forecasting,
            i.e., the first forecast is start. Can also be a date string to
            parse or a datetime type. Default is the zeroth observation.
        end : {int, str,datetime}, optional
            Zero-indexed observation number at which to end forecasting, i.e.,
            the last forecast is end. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out of sample prediction. Default is the last observation in
            the sample.
        dynamic : {bool, int, str,datetime}, optional
            Integer offset relative to `start` at which to begin dynamic
            prediction. Can also be an absolute date string to parse or a
            datetime type (these are not interpreted as offsets).
            Prior to this observation, true endogenous values will be used for
            prediction; starting with this observation and continuing through
            the end of prediction, forecasted endogenous values will be used
            instead.
        information_set : str, optional
            The information set to condition each prediction on. Default is
            "predicted", which computes predictions of period t values
            conditional on observed data through period t-1; these are
            one-step-ahead predictions, and correspond with the typical
            `fittedvalues` results attribute. Alternatives are "filtered",
            which computes predictions of period t values conditional on
            observed data through period t, and "smoothed", which computes
            predictions of period t values conditional on the entire dataset
            (including also future observations t+1, t+2, ...).
        signal_only : bool, optional
            Whether to compute predictions of only the "signal" component of
            the observation equation. Default is False. For example, the
            observation equation of a time-invariant model is
            :math:`y_t = d + Z \\alpha_t + \\varepsilon_t`, and the "signal"
            component is then :math:`Z \\alpha_t`. If this argument is set to
            True, then predictions of the "signal" :math:`Z \\alpha_t` will be
            returned. Otherwise, the default is for predictions of :math:`y_t`
            to be returned.
        **kwargs
            Additional arguments may be required for forecasting beyond the end
            of the sample. See ``FilterResults.predict`` for more details.

        Returns
        -------
        predictions : array_like
            In-sample predictions / Out-of-sample forecasts. (Numpy array or
            Pandas Series or DataFrame, depending on input and dimensions).
            Dimensions are `(npredict x k_endog)`.

        See Also
        --------
        forecast
            Out-of-sample forecasts.
        get_forecast
            Out-of-sample forecasts and results including confidence intervals.
        get_prediction
            In-sample predictions / out-of-sample forecasts and results
            including confidence intervals.
        '''
    def forecast(self, steps: int = 1, signal_only: bool = False, **kwargs):
        '''
        Out-of-sample forecasts

        Parameters
        ----------
        steps : int, str, or datetime, optional
            If an integer, the number of steps to forecast from the end of the
            sample. Can also be a date string to parse or a datetime type.
            However, if the dates index does not have a fixed frequency, steps
            must be an integer. Default is 1.
        signal_only : bool, optional
            Whether to compute forecasts of only the "signal" component of
            the observation equation. Default is False. For example, the
            observation equation of a time-invariant model is
            :math:`y_t = d + Z \\alpha_t + \\varepsilon_t`, and the "signal"
            component is then :math:`Z \\alpha_t`. If this argument is set to
            True, then forecasts of the "signal" :math:`Z \\alpha_t` will be
            returned. Otherwise, the default is for forecasts of :math:`y_t`
            to be returned.
        **kwargs
            Additional arguments may required for forecasting beyond the end
            of the sample. See `FilterResults.predict` for more details.

        Returns
        -------
        forecast : array_like
            Out-of-sample forecasts (Numpy array or Pandas Series or DataFrame,
            depending on input and dimensions).
            Dimensions are `(steps x k_endog)`.

        See Also
        --------
        predict
            In-sample predictions and out-of-sample forecasts.
        get_forecast
            Out-of-sample forecasts and results including confidence intervals.
        get_prediction
            In-sample predictions / out-of-sample forecasts and results
            including confidence intervals.
        '''
    def simulate(self, nsimulations, measurement_shocks: Incomplete | None = None, state_shocks: Incomplete | None = None, initial_state: Incomplete | None = None, anchor: Incomplete | None = None, repetitions: Incomplete | None = None, exog: Incomplete | None = None, extend_model: Incomplete | None = None, extend_kwargs: Incomplete | None = None, pretransformed_measurement_shocks: bool = True, pretransformed_state_shocks: bool = True, pretransformed_initial_state: bool = True, random_state: Incomplete | None = None, **kwargs):
        '''
        Simulate a new time series following the state space model

        Parameters
        ----------
        nsimulations : int
            The number of observations to simulate. If the model is
            time-invariant this can be any number. If the model is
            time-varying, then this number must be less than or equal to the
            number
        measurement_shocks : array_like, optional
            If specified, these are the shocks to the measurement equation,
            :math:`\\varepsilon_t`. If unspecified, these are automatically
            generated using a pseudo-random number generator. If specified,
            must be shaped `nsimulations` x `k_endog`, where `k_endog` is the
            same as in the state space model.
        state_shocks : array_like, optional
            If specified, these are the shocks to the state equation,
            :math:`\\eta_t`. If unspecified, these are automatically
            generated using a pseudo-random number generator. If specified,
            must be shaped `nsimulations` x `k_posdef` where `k_posdef` is the
            same as in the state space model.
        initial_state : array_like, optional
            If specified, this is the initial state vector to use in
            simulation, which should be shaped (`k_states` x 1), where
            `k_states` is the same as in the state space model. If unspecified,
            but the model has been initialized, then that initialization is
            used. This must be specified if `anchor` is anything other than
            "start" or 0.
        anchor : int, str, or datetime, optional
            Starting point from which to begin the simulations; type depends on
            the index of the given `endog` model. Two special cases are the
            strings \'start\' and \'end\', which refer to starting at the beginning
            and end of the sample, respectively. If a date/time index was
            provided to the model, then this argument can be a date string to
            parse or a datetime type. Otherwise, an integer index should be
            given. Default is \'start\'.
        repetitions : int, optional
            Number of simulated paths to generate. Default is 1 simulated path.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        pretransformed_measurement_shocks : bool, optional
            If `measurement_shocks` is provided, this flag indicates whether it
            should be directly used as the shocks. If False, then it is assumed
            to contain draws from the standard Normal distribution that must be
            transformed using the `obs_cov` covariance matrix. Default is True.
        pretransformed_state_shocks : bool, optional
            If `state_shocks` is provided, this flag indicates whether it
            should be directly used as the shocks. If False, then it is assumed
            to contain draws from the standard Normal distribution that must be
            transformed using the `state_cov` covariance matrix. Default is
            True.
        pretransformed_initial_state : bool, optional
            If `initial_state` is provided, this flag indicates whether it
            should be directly used as the initial_state. If False, then it is
            assumed to contain draws from the standard Normal distribution that
            must be transformed using the `initial_state_cov` covariance
            matrix. Default is True.
        random_state : {None, int, Generator, RandomState}, optional
            If `seed` is None (or `np.random`), the
            class:``~numpy.random.RandomState`` singleton is used.
            If `seed` is an int, a new class:``~numpy.random.RandomState``
            instance is used, seeded with `seed`.
            If `seed` is already a class:``~numpy.random.Generator`` or
            class:``~numpy.random.RandomState`` instance then that instance is
            used.

        Returns
        -------
        simulated_obs : ndarray
            An array of simulated observations. If `repetitions=None`, then it
            will be shaped (nsimulations x k_endog) or (nsimulations,) if
            `k_endog=1`. Otherwise it will be shaped
            (nsimulations x k_endog x repetitions). If the model was given
            Pandas input then the output will be a Pandas object. If
            `k_endog > 1` and `repetitions` is not None, then the output will
            be a Pandas DataFrame that has a MultiIndex for the columns, with
            the first level containing the names of the `endog` variables and
            the second level containing the repetition number.

        See Also
        --------
        impulse_responses
            Impulse response functions
        '''
    def impulse_responses(self, steps: int = 1, impulse: int = 0, orthogonalized: bool = False, cumulative: bool = False, **kwargs):
        '''
        Impulse response function

        Parameters
        ----------
        steps : int, optional
            The number of steps for which impulse responses are calculated.
            Default is 1. Note that for time-invariant models, the initial
            impulse is not counted as a step, so if `steps=1`, the output will
            have 2 entries.
        impulse : int, str or array_like
            If an integer, the state innovation to pulse; must be between 0
            and `k_posdef-1`. If a str, it indicates which column of df
            the unit (1) impulse is given.
            Alternatively, a custom impulse vector may be provided; must be
            shaped `k_posdef x 1`.
        orthogonalized : bool, optional
            Whether or not to perform impulse using orthogonalized innovations.
            Note that this will also affect custum `impulse` vectors. Default
            is False.
        cumulative : bool, optional
            Whether or not to return cumulative impulse responses. Default is
            False.
        anchor : int, str, or datetime, optional
            Time point within the sample for the state innovation impulse. Type
            depends on the index of the given `endog` in the model. Two special
            cases are the strings \'start\' and \'end\', which refer to setting the
            impulse at the first and last points of the sample, respectively.
            Integer values can run from 0 to `nobs - 1`, or can be negative to
            apply negative indexing. Finally, if a date/time index was provided
            to the model, then this argument can be a date string to parse or a
            datetime type. Default is \'start\'.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        **kwargs
            If the model has time-varying design or transition matrices and the
            combination of `anchor` and `steps` implies creating impulse
            responses for the out-of-sample period, then these matrices must
            have updated values provided for the out-of-sample steps. For
            example, if `design` is a time-varying component, `nobs` is 10,
            `anchor=1`, and `steps` is 15, a (`k_endog` x `k_states` x 7)
            matrix must be provided with the new design matrix values.

        Returns
        -------
        impulse_responses : ndarray
            Responses for each endogenous variable due to the impulse
            given by the `impulse` argument. For a time-invariant model, the
            impulse responses are given for `steps + 1` elements (this gives
            the "initial impulse" followed by `steps` responses for the
            important cases of VAR and SARIMAX models), while for time-varying
            models the impulse responses are only given for `steps` elements
            (to avoid having to unexpectedly provide updated time-varying
            matrices).

        See Also
        --------
        simulate
            Simulate a time series according to the given state space model,
            optionally with specified series for the innovations.

        Notes
        -----
        Intercepts in the measurement and state equation are ignored when
        calculating impulse responses.
        '''
    def news(self, comparison, impact_date: Incomplete | None = None, impacted_variable: Incomplete | None = None, start: Incomplete | None = None, end: Incomplete | None = None, periods: Incomplete | None = None, exog: Incomplete | None = None, comparison_type: Incomplete | None = None, state_index: Incomplete | None = None, return_raw: bool = False, tolerance: float = 1e-10, **kwargs):
        '''
        Compute impacts from updated data (news and revisions)

        Parameters
        ----------
        comparison : array_like or MLEResults
            An updated dataset with updated and/or revised data from which the
            news can be computed, or an updated or previous results object
            to use in computing the news.
        impact_date : int, str, or datetime, optional
            A single specific period of impacts from news and revisions to
            compute. Can also be a date string to parse or a datetime type.
            This argument cannot be used in combination with `start`, `end`, or
            `periods`. Default is the first out-of-sample observation.
        impacted_variable : str, list, array, or slice, optional
            Observation variable label or slice of labels specifying that only
            specific impacted variables should be shown in the News output. The
            impacted variable(s) describe the variables that were *affected* by
            the news. If you do not know the labels for the variables, check
            the `endog_names` attribute of the model instance.
        start : int, str, or datetime, optional
            The first period of impacts from news and revisions to compute.
            Can also be a date string to parse or a datetime type. Default is
            the first out-of-sample observation.
        end : int, str, or datetime, optional
            The last period of impacts from news and revisions to compute.
            Can also be a date string to parse or a datetime type. Default is
            the first out-of-sample observation.
        periods : int, optional
            The number of periods of impacts from news and revisions to
            compute.
        exog : array_like, optional
            Array of exogenous regressors for the out-of-sample period, if
            applicable.
        comparison_type : {None, \'previous\', \'updated\'}
            This denotes whether the `comparison` argument represents a
            *previous* results object or dataset or an *updated* results object
            or dataset. If not specified, then an attempt is made to determine
            the comparison type.
        state_index : array_like, optional
            An optional index specifying a subset of states to use when
            constructing the impacts of revisions and news. For example, if
            `state_index=[0, 1]` is passed, then only the impacts to the
            observed variables arising from the impacts to the first two
            states will be returned. Default is to use all states.
        return_raw : bool, optional
            Whether or not to return only the specific output or a full
            results object. Default is to return a full results object.
        tolerance : float, optional
            The numerical threshold for determining zero impact. Default is
            that any impact less than 1e-10 is assumed to be zero.

        Returns
        -------
        NewsResults
            Impacts of data revisions and news on estimates

        References
        ----------
        .. [1] Bańbura, Marta, and Michele Modugno.
               "Maximum likelihood estimation of factor models on datasets with
               arbitrary pattern of missing data."
               Journal of Applied Econometrics 29, no. 1 (2014): 133-160.
        .. [2] Bańbura, Marta, Domenico Giannone, and Lucrezia Reichlin.
               "Nowcasting."
               The Oxford Handbook of Economic Forecasting. July 8, 2011.
        .. [3] Bańbura, Marta, Domenico Giannone, Michele Modugno, and Lucrezia
               Reichlin.
               "Now-casting and the real-time data flow."
               In Handbook of economic forecasting, vol. 2, pp. 195-237.
               Elsevier, 2013.
        '''
    def get_smoothed_decomposition(self, decomposition_of: str = 'smoothed_state', state_index: Incomplete | None = None):
        '''
        Decompose smoothed output into contributions from observations

        Parameters
        ----------
        decomposition_of : {"smoothed_state", "smoothed_signal"}
            The object to perform a decomposition of. If it is set to
            "smoothed_state", then the elements of the smoothed state vector
            are decomposed into the contributions of each observation. If it
            is set to "smoothed_signal", then the predictions of the
            observation vector based on the smoothed state vector are
            decomposed. Default is "smoothed_state".
        state_index : array_like, optional
            An optional index specifying a subset of states to use when
            constructing the decomposition of the "smoothed_signal". For
            example, if `state_index=[0, 1]` is passed, then only the
            contributions of observed variables to the smoothed signal arising
            from the first two states will be returned. Note that if not all
            states are used, the contributions will not sum to the smoothed
            signal. Default is to use all states.

        Returns
        -------
        data_contributions : pd.DataFrame
            Contributions of observations to the decomposed object. If the
            smoothed state is being decomposed, then `data_contributions` is
            shaped `(k_states x nobs, k_endog x nobs)` with a `pd.MultiIndex`
            index corresponding to `state_to x date_to` and `pd.MultiIndex`
            columns corresponding to `variable_from x date_from`. If the
            smoothed signal is being decomposed, then `data_contributions` is
            shaped `(k_endog x nobs, k_endog x nobs)` with `pd.MultiIndex`-es
            corresponding to `variable_to x date_to` and
            `variable_from x date_from`.
        obs_intercept_contributions : pd.DataFrame
            Contributions of the observation intercept to the decomposed
            object. If the smoothed state is being decomposed, then
            `obs_intercept_contributions` is
            shaped `(k_states x nobs, k_endog x nobs)` with a `pd.MultiIndex`
            index corresponding to `state_to x date_to` and `pd.MultiIndex`
            columns corresponding to `obs_intercept_from x date_from`. If the
            smoothed signal is being decomposed, then
            `obs_intercept_contributions` is shaped
            `(k_endog x nobs, k_endog x nobs)` with `pd.MultiIndex`-es
            corresponding to `variable_to x date_to` and
            `obs_intercept_from x date_from`.
        state_intercept_contributions : pd.DataFrame
            Contributions of the state intercept to the decomposed
            object. If the smoothed state is being decomposed, then
            `state_intercept_contributions` is
            shaped `(k_states x nobs, k_states x nobs)` with a `pd.MultiIndex`
            index corresponding to `state_to x date_to` and `pd.MultiIndex`
            columns corresponding to `state_intercept_from x date_from`. If the
            smoothed signal is being decomposed, then
            `state_intercept_contributions` is shaped
            `(k_endog x nobs, k_states x nobs)` with `pd.MultiIndex`-es
            corresponding to `variable_to x date_to` and
            `state_intercept_from x date_from`.
        prior_contributions : pd.DataFrame
            Contributions of the prior to the decomposed object. If the
            smoothed state is being decomposed, then `prior_contributions` is
            shaped `(nobs x k_states, k_states)`, with a `pd.MultiIndex`
            index corresponding to `state_to x date_to` and columns
            corresponding to elements of the prior mean (aka "initial state").
            If the smoothed signal is being decomposed, then
            `prior_contributions` is shaped `(nobs x k_endog, k_states)`,
            with a `pd.MultiIndex` index corresponding to
            `variable_to x date_to` and columns corresponding to elements of
            the prior mean.

        Notes
        -----
        Denote the smoothed state at time :math:`t` by :math:`\\alpha_t`. Then
        the smoothed signal is :math:`Z_t \\alpha_t`, where :math:`Z_t` is the
        design matrix operative at time :math:`t`.
        '''
    def append(self, endog, exog: Incomplete | None = None, refit: bool = False, fit_kwargs: Incomplete | None = None, copy_initialization: bool = False, **kwargs):
        """
        Recreate the results object with new data appended to the original data

        Creates a new result object applied to a dataset that is created by
        appending new data to the end of the model's original data. The new
        results can then be used for analysis or forecasting.

        Parameters
        ----------
        endog : array_like
            New observations from the modeled time-series process.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        refit : bool, optional
            Whether to re-fit the parameters, based on the combined dataset.
            Default is False (so parameters from the current results object
            are used to create the new results object).
        copy_initialization : bool, optional
            Whether or not to copy the initialization from the current results
            set to the new model. Default is False
        fit_kwargs : dict, optional
            Keyword arguments to pass to `fit` (if `refit=True`) or `filter` /
            `smooth`.
        copy_initialization : bool, optional
        **kwargs
            Keyword arguments may be used to modify model specification
            arguments when created the new model object.

        Returns
        -------
        results
            Updated Results object, that includes results from both the
            original dataset and the new dataset.

        Notes
        -----
        The `endog` and `exog` arguments to this method must be formatted in
        the same way (e.g. Pandas Series versus Numpy array) as were the
        `endog` and `exog` arrays passed to the original model.

        The `endog` argument to this method should consist of new observations
        that occurred directly after the last element of `endog`. For any other
        kind of dataset, see the `apply` method.

        This method will apply filtering to all of the original data as well
        as to the new data. To apply filtering only to the new data (which
        can be much faster if the original dataset is large), see the `extend`
        method.

        See Also
        --------
        statsmodels.tsa.statespace.mlemodel.MLEResults.extend
        statsmodels.tsa.statespace.mlemodel.MLEResults.apply

        Examples
        --------
        >>> index = pd.period_range(start='2000', periods=2, freq='A')
        >>> original_observations = pd.Series([1.2, 1.5], index=index)
        >>> mod = sm.tsa.SARIMAX(original_observations)
        >>> res = mod.fit()
        >>> print(res.params)
        ar.L1     0.9756
        sigma2    0.0889
        dtype: float64
        >>> print(res.fittedvalues)
        2000    0.0000
        2001    1.1707
        Freq: A-DEC, dtype: float64
        >>> print(res.forecast(1))
        2002    1.4634
        Freq: A-DEC, dtype: float64

        >>> new_index = pd.period_range(start='2002', periods=1, freq='A')
        >>> new_observations = pd.Series([0.9], index=new_index)
        >>> updated_res = res.append(new_observations)
        >>> print(updated_res.params)
        ar.L1     0.9756
        sigma2    0.0889
        dtype: float64
        >>> print(updated_res.fittedvalues)
        2000    0.0000
        2001    1.1707
        2002    1.4634
        Freq: A-DEC, dtype: float64
        >>> print(updated_res.forecast(1))
        2003    0.878
        Freq: A-DEC, dtype: float64
        """
    def extend(self, endog, exog: Incomplete | None = None, fit_kwargs: Incomplete | None = None, **kwargs):
        """
        Recreate the results object for new data that extends the original data

        Creates a new result object applied to a new dataset that is assumed to
        follow directly from the end of the model's original data. The new
        results can then be used for analysis or forecasting.

        Parameters
        ----------
        endog : array_like
            New observations from the modeled time-series process.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        fit_kwargs : dict, optional
            Keyword arguments to pass to `filter` or `smooth`.
        **kwargs
            Keyword arguments may be used to modify model specification
            arguments when created the new model object.

        Returns
        -------
        results
            Updated Results object, that includes results only for the new
            dataset.

        See Also
        --------
        statsmodels.tsa.statespace.mlemodel.MLEResults.append
        statsmodels.tsa.statespace.mlemodel.MLEResults.apply

        Notes
        -----
        The `endog` argument to this method should consist of new observations
        that occurred directly after the last element of the model's original
        `endog` array. For any other kind of dataset, see the `apply` method.

        This method will apply filtering only to the new data provided by the
        `endog` argument, which can be much faster than re-filtering the entire
        dataset. However, the returned results object will only have results
        for the new data. To retrieve results for both the new data and the
        original data, see the `append` method.

        Examples
        --------
        >>> index = pd.period_range(start='2000', periods=2, freq='A')
        >>> original_observations = pd.Series([1.2, 1.5], index=index)
        >>> mod = sm.tsa.SARIMAX(original_observations)
        >>> res = mod.fit()
        >>> print(res.params)
        ar.L1     0.9756
        sigma2    0.0889
        dtype: float64
        >>> print(res.fittedvalues)
        2000    0.0000
        2001    1.1707
        Freq: A-DEC, dtype: float64
        >>> print(res.forecast(1))
        2002    1.4634
        Freq: A-DEC, dtype: float64

        >>> new_index = pd.period_range(start='2002', periods=1, freq='A')
        >>> new_observations = pd.Series([0.9], index=new_index)
        >>> updated_res = res.extend(new_observations)
        >>> print(updated_res.params)
        ar.L1     0.9756
        sigma2    0.0889
        dtype: float64
        >>> print(updated_res.fittedvalues)
        2002    1.4634
        Freq: A-DEC, dtype: float64
        >>> print(updated_res.forecast(1))
        2003    0.878
        Freq: A-DEC, dtype: float64
        """
    def apply(self, endog, exog: Incomplete | None = None, refit: bool = False, fit_kwargs: Incomplete | None = None, copy_initialization: bool = False, **kwargs):
        """
        Apply the fitted parameters to new data unrelated to the original data

        Creates a new result object using the current fitted parameters,
        applied to a completely new dataset that is assumed to be unrelated to
        the model's original data. The new results can then be used for
        analysis or forecasting.

        Parameters
        ----------
        endog : array_like
            New observations from the modeled time-series process.
        exog : array_like, optional
            New observations of exogenous regressors, if applicable.
        refit : bool, optional
            Whether to re-fit the parameters, using the new dataset.
            Default is False (so parameters from the current results object
            are used to create the new results object).
        copy_initialization : bool, optional
            Whether or not to copy the initialization from the current results
            set to the new model. Default is False
        fit_kwargs : dict, optional
            Keyword arguments to pass to `fit` (if `refit=True`) or `filter` /
            `smooth`.
        **kwargs
            Keyword arguments may be used to modify model specification
            arguments when created the new model object.

        Returns
        -------
        results
            Updated Results object, that includes results only for the new
            dataset.

        See Also
        --------
        statsmodels.tsa.statespace.mlemodel.MLEResults.append
        statsmodels.tsa.statespace.mlemodel.MLEResults.apply

        Notes
        -----
        The `endog` argument to this method should consist of new observations
        that are not necessarily related to the original model's `endog`
        dataset. For observations that continue that original dataset by follow
        directly after its last element, see the `append` and `extend` methods.

        Examples
        --------
        >>> index = pd.period_range(start='2000', periods=2, freq='A')
        >>> original_observations = pd.Series([1.2, 1.5], index=index)
        >>> mod = sm.tsa.SARIMAX(original_observations)
        >>> res = mod.fit()
        >>> print(res.params)
        ar.L1     0.9756
        sigma2    0.0889
        dtype: float64
        >>> print(res.fittedvalues)
        2000    0.0000
        2001    1.1707
        Freq: A-DEC, dtype: float64
        >>> print(res.forecast(1))
        2002    1.4634
        Freq: A-DEC, dtype: float64

        >>> new_index = pd.period_range(start='1980', periods=3, freq='A')
        >>> new_observations = pd.Series([1.4, 0.3, 1.2], index=new_index)
        >>> new_res = res.apply(new_observations)
        >>> print(new_res.params)
        ar.L1     0.9756
        sigma2    0.0889
        dtype: float64
        >>> print(new_res.fittedvalues)
        1980    1.1707
        1981    1.3659
        1982    0.2927
        Freq: A-DEC, dtype: float64
        Freq: A-DEC, dtype: float64
        >>> print(new_res.forecast(1))
        1983    1.1707
        Freq: A-DEC, dtype: float64
        """
    def plot_diagnostics(self, variable: int = 0, lags: int = 10, fig: Incomplete | None = None, figsize: Incomplete | None = None, truncate_endog_names: int = 24, auto_ylims: bool = False, bartlett_confint: bool = False, acf_kwargs: Incomplete | None = None):
        """
        Diagnostic plots for standardized residuals of one endogenous variable

        Parameters
        ----------
        variable : int, optional
            Index of the endogenous variable for which the diagnostic plots
            should be created. Default is 0.
        lags : int, optional
            Number of lags to include in the correlogram. Default is 10.
        fig : Figure, optional
            If given, subplots are created in this figure instead of in a new
            figure. Note that the 2x2 grid will be created in the provided
            figure using `fig.add_subplot()`.
        figsize : tuple, optional
            If a figure is created, this argument allows specifying a size.
            The tuple is (width, height).
        auto_ylims : bool, optional
            If True, adjusts automatically the y-axis limits to ACF values.
        bartlett_confint : bool, default True
            Confidence intervals for ACF values are generally placed at 2
            standard errors around r_k. The formula used for standard error
            depends upon the situation. If the autocorrelations are being used
            to test for randomness of residuals as part of the ARIMA routine,
            the standard errors are determined assuming the residuals are white
            noise. The approximate formula for any lag is that standard error
            of each r_k = 1/sqrt(N). See section 9.4 of [1] for more details on
            the 1/sqrt(N) result. For more elementary discussion, see section
            5.3.2 in [2].
            For the ACF of raw data, the standard error at a lag k is
            found as if the right model was an MA(k-1). This allows the
            possible interpretation that if all autocorrelations past a
            certain lag are within the limits, the model might be an MA of
            order defined by the last significant autocorrelation. In this
            case, a moving average model is assumed for the data and the
            standard errors for the confidence intervals should be
            generated using Bartlett's formula. For more details on
            Bartlett formula result, see section 7.2 in [1].+
        acf_kwargs : dict, optional
            Optional dictionary of keyword arguments that are directly passed
            on to the correlogram Matplotlib plot produced by plot_acf().

        Returns
        -------
        Figure
            Figure instance with diagnostic plots

        See Also
        --------
        statsmodels.graphics.gofplots.qqplot
        statsmodels.graphics.tsaplots.plot_acf

        Notes
        -----
        Produces a 2x2 plot grid with the following plots (ordered clockwise
        from top left):

        1. Standardized residuals over time
        2. Histogram plus estimated density of standardized residuals, along
           with a Normal(0,1) density plotted for reference.
        3. Normal Q-Q plot, with Normal reference line.
        4. Correlogram

        References
        ----------
        [1] Brockwell and Davis, 1987. Time Series Theory and Methods
        [2] Brockwell and Davis, 2010. Introduction to Time Series and
        Forecasting, 2nd edition.
        """
    def summary(self, alpha: float = 0.05, start: Incomplete | None = None, title: Incomplete | None = None, model_name: Incomplete | None = None, display_params: bool = True, display_diagnostics: bool = True, truncate_endog_names: Incomplete | None = None, display_max_endog: Incomplete | None = None, extra_top_left: Incomplete | None = None, extra_top_right: Incomplete | None = None):
        """
        Summarize the Model

        Parameters
        ----------
        alpha : float, optional
            Significance level for the confidence intervals. Default is 0.05.
        start : int, optional
            Integer of the start observation. Default is 0.
        model_name : str
            The name of the model used. Default is to use model class name.

        Returns
        -------
        summary : Summary instance
            This holds the summary table and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary
        """

class MLEResultsWrapper(wrap.ResultsWrapper): ...

class PredictionResults(pred.PredictionResults):
    """
    Prediction result from MLE models

    Parameters
    ----------
    model : MLEModel
        The models used to make the prediction
    prediction_results : kalman_filter.PredictionResults instance
        Results object from prediction after fitting or filtering a state space
        model.
    row_labels : iterable
        Row labels for the predicted data.
    information_set : str
        Name of information set
    signal_only : bool
        Whether the prediction is for the signal only

    Attributes
    ----------
    model : MLEModel
        The models used to make the prediction
    prediction_results : kalman_filter.PredictionResults instance
        Results object from prediction after fitting or filtering a state space
        model.
    information_set : str
        Name of information set
    signal_only : bool
        Whether the prediction is for the signal only
    """
    model: Incomplete
    prediction_results: Incomplete
    information_set: Incomplete
    signal_only: Incomplete
    def __init__(self, model, prediction_results, row_labels: Incomplete | None = None, information_set: str = 'predicted', signal_only: bool = False) -> None: ...
    @property
    def se_mean(self): ...
    def conf_int(self, method: str = 'endpoint', alpha: float = 0.05, **kwds): ...
    def summary_frame(self, endog: int = 0, alpha: float = 0.05): ...

class PredictionResultsWrapper(wrap.ResultsWrapper): ...
