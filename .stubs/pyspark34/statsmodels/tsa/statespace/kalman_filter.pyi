from . import tools as tools
from .representation import FrozenRepresentation as FrozenRepresentation, OptionWrapper as OptionWrapper, Representation as Representation
from .tools import reorder_missing_matrix as reorder_missing_matrix, reorder_missing_vector as reorder_missing_vector
from _typeshed import Incomplete
from collections.abc import Generator
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning

FILTER_CONVENTIONAL: int
FILTER_EXACT_INITIAL: int
FILTER_AUGMENTED: int
FILTER_SQUARE_ROOT: int
FILTER_UNIVARIATE: int
FILTER_COLLAPSED: int
FILTER_EXTENDED: int
FILTER_UNSCENTED: int
FILTER_CONCENTRATED: int
FILTER_CHANDRASEKHAR: int
INVERT_UNIVARIATE: int
SOLVE_LU: int
INVERT_LU: int
SOLVE_CHOLESKY: int
INVERT_CHOLESKY: int
STABILITY_FORCE_SYMMETRY: int
MEMORY_STORE_ALL: int
MEMORY_NO_FORECAST_MEAN: int
MEMORY_NO_FORECAST_COV: int
MEMORY_NO_FORECAST: Incomplete
MEMORY_NO_PREDICTED_MEAN: int
MEMORY_NO_PREDICTED_COV: int
MEMORY_NO_PREDICTED: Incomplete
MEMORY_NO_FILTERED_MEAN: int
MEMORY_NO_FILTERED_COV: int
MEMORY_NO_FILTERED: Incomplete
MEMORY_NO_LIKELIHOOD: int
MEMORY_NO_GAIN: int
MEMORY_NO_SMOOTHING: int
MEMORY_NO_STD_FORECAST: int
MEMORY_CONSERVE: Incomplete
TIMING_INIT_PREDICTED: int
TIMING_INIT_FILTERED: int

class KalmanFilter(Representation):
    """
    State space representation of a time series process, with Kalman filter

    Parameters
    ----------
    k_endog : {array_like, int}
        The observed time-series process :math:`y` if array like or the
        number of variables in the process if an integer.
    k_states : int
        The dimension of the unobserved state process.
    k_posdef : int, optional
        The dimension of a guaranteed positive definite covariance matrix
        describing the shocks in the transition equation. Must be less than
        or equal to `k_states`. Default is `k_states`.
    loglikelihood_burn : int, optional
        The number of initial periods during which the loglikelihood is not
        recorded. Default is 0.
    tolerance : float, optional
        The tolerance at which the Kalman filter determines convergence to
        steady-state. Default is 1e-19.
    results_class : class, optional
        Default results class to use to save filtering output. Default is
        `FilterResults`. If specified, class must extend from `FilterResults`.
    **kwargs
        Keyword arguments may be used to provide values for the filter,
        inversion, and stability methods. See `set_filter_method`,
        `set_inversion_method`, and `set_stability_method`.
        Keyword arguments may be used to provide default values for state space
        matrices. See `Representation` for more details.

    See Also
    --------
    FilterResults
    statsmodels.tsa.statespace.representation.Representation

    Notes
    -----
    There are several types of options available for controlling the Kalman
    filter operation. All options are internally held as bitmasks, but can be
    manipulated by setting class attributes, which act like boolean flags. For
    more information, see the `set_*` class method documentation. The options
    are:

    filter_method
        The filtering method controls aspects of which
        Kalman filtering approach will be used.
    inversion_method
        The Kalman filter may contain one matrix inversion: that of the
        forecast error covariance matrix. The inversion method controls how and
        if that inverse is performed.
    stability_method
        The Kalman filter is a recursive algorithm that may in some cases
        suffer issues with numerical stability. The stability method controls
        what, if any, measures are taken to promote stability.
    conserve_memory
        By default, the Kalman filter computes a number of intermediate
        matrices at each iteration. The memory conservation options control
        which of those matrices are stored.
    filter_timing
        By default, the Kalman filter follows Durbin and Koopman, 2012, in
        initializing the filter with predicted values. Kim and Nelson, 1999,
        instead initialize the filter with filtered values, which is
        essentially just a different timing convention.

    The `filter_method` and `inversion_method` options intentionally allow
    the possibility that multiple methods will be indicated. In the case that
    multiple methods are selected, the underlying Kalman filter will attempt to
    select the optional method given the input data.

    For example, it may be that INVERT_UNIVARIATE and SOLVE_CHOLESKY are
    indicated (this is in fact the default case). In this case, if the
    endogenous vector is 1-dimensional (`k_endog` = 1), then INVERT_UNIVARIATE
    is used and inversion reduces to simple division, and if it has a larger
    dimension, the Cholesky decomposition along with linear solving (rather
    than explicit matrix inversion) is used. If only SOLVE_CHOLESKY had been
    set, then the Cholesky decomposition method would *always* be used, even in
    the case of 1-dimensional data.
    """
    filter_methods: Incomplete
    filter_conventional: Incomplete
    filter_exact_initial: Incomplete
    filter_augmented: Incomplete
    filter_square_root: Incomplete
    filter_univariate: Incomplete
    filter_collapsed: Incomplete
    filter_extended: Incomplete
    filter_unscented: Incomplete
    filter_concentrated: Incomplete
    filter_chandrasekhar: Incomplete
    inversion_methods: Incomplete
    invert_univariate: Incomplete
    solve_lu: Incomplete
    invert_lu: Incomplete
    solve_cholesky: Incomplete
    invert_cholesky: Incomplete
    stability_methods: Incomplete
    stability_force_symmetry: Incomplete
    memory_options: Incomplete
    memory_store_all: Incomplete
    memory_no_forecast_mean: Incomplete
    memory_no_forecast_cov: Incomplete
    @property
    def memory_no_forecast(self):
        """
        (bool) Flag to prevent storing all forecast-related output.
        """
    @memory_no_forecast.setter
    def memory_no_forecast(self, value) -> None: ...
    memory_no_predicted_mean: Incomplete
    memory_no_predicted_cov: Incomplete
    @property
    def memory_no_predicted(self):
        """
        (bool) Flag to prevent storing predicted state and covariance matrices.
        """
    @memory_no_predicted.setter
    def memory_no_predicted(self, value) -> None: ...
    memory_no_filtered_mean: Incomplete
    memory_no_filtered_cov: Incomplete
    @property
    def memory_no_filtered(self):
        """
        (bool) Flag to prevent storing filtered state and covariance matrices.
        """
    @memory_no_filtered.setter
    def memory_no_filtered(self, value) -> None: ...
    memory_no_likelihood: Incomplete
    memory_no_gain: Incomplete
    memory_no_smoothing: Incomplete
    memory_no_std_forecast: Incomplete
    memory_conserve: Incomplete
    timing_options: Incomplete
    timing_init_predicted: Incomplete
    timing_init_filtered: Incomplete
    filter_method = FILTER_CONVENTIONAL
    inversion_method: Incomplete
    stability_method = STABILITY_FORCE_SYMMETRY
    conserve_memory = MEMORY_STORE_ALL
    filter_timing = TIMING_INIT_PREDICTED
    loglikelihood_burn: Incomplete
    results_class: Incomplete
    prefix_kalman_filter_map: Incomplete
    tolerance: Incomplete
    def __init__(self, k_endog, k_states, k_posdef: Incomplete | None = None, loglikelihood_burn: int = 0, tolerance: float = 1e-19, results_class: Incomplete | None = None, kalman_filter_classes: Incomplete | None = None, **kwargs) -> None: ...
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
        The filtering method is defined by a collection of boolean flags, and
        is internally stored as a bitmask. The methods available are:

        FILTER_CONVENTIONAL
            Conventional Kalman filter.
        FILTER_UNIVARIATE
            Univariate approach to Kalman filtering. Overrides conventional
            method if both are specified.
        FILTER_COLLAPSED
            Collapsed approach to Kalman filtering. Will be used *in addition*
            to conventional or univariate filtering.
        FILTER_CONCENTRATED
            Use the concentrated log-likelihood function. Will be used
            *in addition* to the other options.

        Note that only the first method is available if using a Scipy version
        older than 0.16.

        If the bitmask is set directly via the `filter_method` argument, then
        the full method must be provided.

        If keyword arguments are used to set individual boolean flags, then
        the lowercase of the method must be used as an argument name, and the
        value is the desired value of the boolean flag (True or False).

        Note that the filter method may also be specified by directly modifying
        the class attributes which are defined similarly to the keyword
        arguments.

        The default filtering method is FILTER_CONVENTIONAL.

        Examples
        --------
        >>> mod = sm.tsa.statespace.SARIMAX(range(10))
        >>> mod.ssm.filter_method
        1
        >>> mod.ssm.filter_conventional
        True
        >>> mod.ssm.filter_univariate = True
        >>> mod.ssm.filter_method
        17
        >>> mod.ssm.set_filter_method(filter_univariate=False,
        ...                           filter_collapsed=True)
        >>> mod.ssm.filter_method
        33
        >>> mod.ssm.set_filter_method(filter_method=1)
        >>> mod.ssm.filter_conventional
        True
        >>> mod.ssm.filter_univariate
        False
        >>> mod.ssm.filter_collapsed
        False
        >>> mod.ssm.filter_univariate = True
        >>> mod.ssm.filter_method
        17
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
        The inversion method is defined by a collection of boolean flags, and
        is internally stored as a bitmask. The methods available are:

        INVERT_UNIVARIATE
            If the endogenous time series is univariate, then inversion can be
            performed by simple division. If this flag is set and the time
            series is univariate, then division will always be used even if
            other flags are also set.
        SOLVE_LU
            Use an LU decomposition along with a linear solver (rather than
            ever actually inverting the matrix).
        INVERT_LU
            Use an LU decomposition along with typical matrix inversion.
        SOLVE_CHOLESKY
            Use a Cholesky decomposition along with a linear solver.
        INVERT_CHOLESKY
            Use an Cholesky decomposition along with typical matrix inversion.

        If the bitmask is set directly via the `inversion_method` argument,
        then the full method must be provided.

        If keyword arguments are used to set individual boolean flags, then
        the lowercase of the method must be used as an argument name, and the
        value is the desired value of the boolean flag (True or False).

        Note that the inversion method may also be specified by directly
        modifying the class attributes which are defined similarly to the
        keyword arguments.

        The default inversion method is `INVERT_UNIVARIATE | SOLVE_CHOLESKY`

        Several things to keep in mind are:

        - If the filtering method is specified to be univariate, then simple
          division is always used regardless of the dimension of the endogenous
          time series.
        - Cholesky decomposition is about twice as fast as LU decomposition,
          but it requires that the matrix be positive definite. While this
          should generally be true, it may not be in every case.
        - Using a linear solver rather than true matrix inversion is generally
          faster and is numerically more stable.

        Examples
        --------
        >>> mod = sm.tsa.statespace.SARIMAX(range(10))
        >>> mod.ssm.inversion_method
        1
        >>> mod.ssm.solve_cholesky
        True
        >>> mod.ssm.invert_univariate
        True
        >>> mod.ssm.invert_lu
        False
        >>> mod.ssm.invert_univariate = False
        >>> mod.ssm.inversion_method
        8
        >>> mod.ssm.set_inversion_method(solve_cholesky=False,
        ...                              invert_cholesky=True)
        >>> mod.ssm.inversion_method
        16
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
        The stability method is defined by a collection of boolean flags, and
        is internally stored as a bitmask. The methods available are:

        STABILITY_FORCE_SYMMETRY = 0x01
            If this flag is set, symmetry of the predicted state covariance
            matrix is enforced at each iteration of the filter, where each
            element is set to the average of the corresponding elements in the
            upper and lower triangle.

        If the bitmask is set directly via the `stability_method` argument,
        then the full method must be provided.

        If keyword arguments are used to set individual boolean flags, then
        the lowercase of the method must be used as an argument name, and the
        value is the desired value of the boolean flag (True or False).

        Note that the stability method may also be specified by directly
        modifying the class attributes which are defined similarly to the
        keyword arguments.

        The default stability method is `STABILITY_FORCE_SYMMETRY`

        Examples
        --------
        >>> mod = sm.tsa.statespace.SARIMAX(range(10))
        >>> mod.ssm.stability_method
        1
        >>> mod.ssm.stability_force_symmetry
        True
        >>> mod.ssm.stability_force_symmetry = False
        >>> mod.ssm.stability_method
        0
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
            method by setting individual boolean flags. See notes for details.

        Notes
        -----
        The memory conservation method is defined by a collection of boolean
        flags, and is internally stored as a bitmask. The methods available
        are:

        MEMORY_STORE_ALL
            Store all intermediate matrices. This is the default value.
        MEMORY_NO_FORECAST_MEAN
            Do not store the forecast or forecast errors. If this option is
            used, the `predict` method from the results class is unavailable.
        MEMORY_NO_FORECAST_COV
            Do not store the forecast error covariance matrices.
        MEMORY_NO_FORECAST
            Do not store the forecast, forecast error, or forecast error
            covariance matrices. If this option is used, the `predict` method
            from the results class is unavailable.
        MEMORY_NO_PREDICTED_MEAN
            Do not store the predicted state.
        MEMORY_NO_PREDICTED_COV
            Do not store the predicted state covariance
            matrices.
        MEMORY_NO_PREDICTED
            Do not store the predicted state or predicted state covariance
            matrices.
        MEMORY_NO_FILTERED_MEAN
            Do not store the filtered state.
        MEMORY_NO_FILTERED_COV
            Do not store the filtered state covariance
            matrices.
        MEMORY_NO_FILTERED
            Do not store the filtered state or filtered state covariance
            matrices.
        MEMORY_NO_LIKELIHOOD
            Do not store the vector of loglikelihood values for each
            observation. Only the sum of the loglikelihood values is stored.
        MEMORY_NO_GAIN
            Do not store the Kalman gain matrices.
        MEMORY_NO_SMOOTHING
            Do not store temporary variables related to Kalman smoothing. If
            this option is used, smoothing is unavailable.
        MEMORY_NO_STD_FORECAST
            Do not store standardized forecast errors.
        MEMORY_CONSERVE
            Do not store any intermediate matrices.

        If the bitmask is set directly via the `conserve_memory` argument,
        then the full method must be provided.

        If keyword arguments are used to set individual boolean flags, then
        the lowercase of the method must be used as an argument name, and the
        value is the desired value of the boolean flag (True or False).

        Note that the memory conservation method may also be specified by
        directly modifying the class attributes which are defined similarly to
        the keyword arguments.

        The default memory conservation method is `MEMORY_STORE_ALL`, so that
        all intermediate matrices are stored.

        Examples
        --------
        >>> mod = sm.tsa.statespace.SARIMAX(range(10))
        >>> mod.ssm..conserve_memory
        0
        >>> mod.ssm.memory_no_predicted
        False
        >>> mod.ssm.memory_no_predicted = True
        >>> mod.ssm.conserve_memory
        2
        >>> mod.ssm.set_conserve_memory(memory_no_filtered=True,
        ...                             memory_no_forecast=True)
        >>> mod.ssm.conserve_memory
        7
        """
    def set_filter_timing(self, alternate_timing: Incomplete | None = None, **kwargs) -> None:
        """
        Set the filter timing convention

        By default, the Kalman filter follows Durbin and Koopman, 2012, in
        initializing the filter with predicted values. Kim and Nelson, 1999,
        instead initialize the filter with filtered values, which is
        essentially just a different timing convention.

        Parameters
        ----------
        alternate_timing : int, optional
            Whether or not to use the alternate timing convention. Default is
            unspecified.
        **kwargs
            Keyword arguments may be used to influence the memory conservation
            method by setting individual boolean flags. See notes for details.
        """
    def fixed_scale(self, scale) -> Generator[None, None, None]:
        """
        fixed_scale(scale)

        Context manager for fixing the scale when FILTER_CONCENTRATED is set

        Parameters
        ----------
        scale : numeric
            Scale of the model.

        Notes
        -----
        This a no-op if scale is None.

        This context manager is most useful in models which are explicitly
        concentrating out the scale, so that the set of parameters they are
        estimating does not include the scale.
        """
    def filter(self, filter_method: Incomplete | None = None, inversion_method: Incomplete | None = None, stability_method: Incomplete | None = None, conserve_memory: Incomplete | None = None, filter_timing: Incomplete | None = None, tolerance: Incomplete | None = None, loglikelihood_burn: Incomplete | None = None, complex_step: bool = False):
        """
        Apply the Kalman filter to the statespace model.

        Parameters
        ----------
        filter_method : int, optional
            Determines which Kalman filter to use. Default is conventional.
        inversion_method : int, optional
            Determines which inversion technique to use. Default is by Cholesky
            decomposition.
        stability_method : int, optional
            Determines which numerical stability techniques to use. Default is
            to enforce symmetry of the predicted state covariance matrix.
        conserve_memory : int, optional
            Determines what output from the filter to store. Default is to
            store everything.
        filter_timing : int, optional
            Determines the timing convention of the filter. Default is that
            from Durbin and Koopman (2012), in which the filter is initialized
            with predicted values.
        tolerance : float, optional
            The tolerance at which the Kalman filter determines convergence to
            steady-state. Default is 1e-19.
        loglikelihood_burn : int, optional
            The number of initial periods during which the loglikelihood is not
            recorded. Default is 0.

        Notes
        -----
        This function by default does not compute variables required for
        smoothing.
        """
    def loglike(self, **kwargs):
        """
        Calculate the loglikelihood associated with the statespace model.

        Parameters
        ----------
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.

        Returns
        -------
        loglike : float
            The joint loglikelihood.
        """
    def loglikeobs(self, **kwargs):
        """
        Calculate the loglikelihood for each observation associated with the
        statespace model.

        Parameters
        ----------
        **kwargs
            Additional keyword arguments to pass to the Kalman filter. See
            `KalmanFilter.filter` for more details.

        Notes
        -----
        If `loglikelihood_burn` is positive, then the entries in the returned
        loglikelihood vector are set to be zero for those initial time periods.

        Returns
        -------
        loglike : array of float
            Array of loglikelihood values for each observation.
        """
    def simulate(self, nsimulations, measurement_shocks: Incomplete | None = None, state_shocks: Incomplete | None = None, initial_state: Incomplete | None = None, pretransformed_measurement_shocks: bool = True, pretransformed_state_shocks: bool = True, pretransformed_initial_state: bool = True, simulator: Incomplete | None = None, return_simulator: bool = False, random_state: Incomplete | None = None):
        """
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
            If specified, this is the state vector at time zero, which should
            be shaped (`k_states` x 1), where `k_states` is the same as in the
            state space model. If unspecified, but the model has been
            initialized, then that initialization is used. If unspecified and
            the model has not been initialized, then a vector of zeros is used.
            Note that this is not included in the returned `simulated_states`
            array.
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
        return_simulator : bool, optional
            Whether or not to return the simulator object. Typically used to
            improve performance when performing repeated sampling. Default is
            False.
        random_state : {None, int, Generator, RandomState}, optionall
            If `seed` is None (or `np.random`), the `numpy.random.RandomState`
            singleton is used.
            If `seed` is an int, a new ``RandomState`` instance is used,
            seeded with `seed`.
            If `seed` is already a ``Generator`` or ``RandomState`` instance
            then that instance is used.

        Returns
        -------
        simulated_obs : ndarray
            An (nsimulations x k_endog) array of simulated observations.
        simulated_states : ndarray
            An (nsimulations x k_states) array of simulated states.
        simulator : SimulationSmoothResults
            If `return_simulator=True`, then an instance of a simulator is
            returned, which can be reused for additional simulations of the
            same size.
        """
    def impulse_responses(self, steps: int = 10, impulse: int = 0, orthogonalized: bool = False, cumulative: bool = False, direct: bool = False):
        """
        Impulse response function

        Parameters
        ----------
        steps : int, optional
            The number of steps for which impulse responses are calculated.
            Default is 10. Note that the initial impulse is not counted as a
            step, so if `steps=1`, the output will have 2 entries.
        impulse : int or array_like
            If an integer, the state innovation to pulse; must be between 0
            and `k_posdef-1` where `k_posdef` is the same as in the state
            space model. Alternatively, a custom impulse vector may be
            provided; must be a column vector with shape `(k_posdef, 1)`.
        orthogonalized : bool, optional
            Whether or not to perform impulse using orthogonalized innovations.
            Note that this will also affect custum `impulse` vectors. Default
            is False.
        cumulative : bool, optional
            Whether or not to return cumulative impulse responses. Default is
            False.

        Returns
        -------
        impulse_responses : ndarray
            Responses for each endogenous variable due to the impulse
            given by the `impulse` argument. A (steps + 1 x k_endog) array.

        Notes
        -----
        Intercepts in the measurement and state equation are ignored when
        calculating impulse responses.

        TODO: add note about how for time-varying systems this is - perhaps
        counter-intuitively - returning the impulse response within the given
        model (i.e. starting at period 0 defined by the model) and it is *not*
        doing impulse responses after the end of the model. To compute impulse
        responses from arbitrary time points, it is necessary to clone a new
        model with the appropriate system matrices.
        """

class FilterResults(FrozenRepresentation):
    """
    Results from applying the Kalman filter to a state space model.

    Parameters
    ----------
    model : Representation
        A Statespace representation

    Attributes
    ----------
    nobs : int
        Number of observations.
    nobs_diffuse : int
        Number of observations under the diffuse Kalman filter.
    k_endog : int
        The dimension of the observation series.
    k_states : int
        The dimension of the unobserved state process.
    k_posdef : int
        The dimension of a guaranteed positive definite
        covariance matrix describing the shocks in the
        measurement equation.
    dtype : dtype
        Datatype of representation matrices
    prefix : str
        BLAS prefix of representation matrices
    shapes : dictionary of name,tuple
        A dictionary recording the shapes of each of the
        representation matrices as tuples.
    endog : ndarray
        The observation vector.
    design : ndarray
        The design matrix, :math:`Z`.
    obs_intercept : ndarray
        The intercept for the observation equation, :math:`d`.
    obs_cov : ndarray
        The covariance matrix for the observation equation :math:`H`.
    transition : ndarray
        The transition matrix, :math:`T`.
    state_intercept : ndarray
        The intercept for the transition equation, :math:`c`.
    selection : ndarray
        The selection matrix, :math:`R`.
    state_cov : ndarray
        The covariance matrix for the state equation :math:`Q`.
    missing : array of bool
        An array of the same size as `endog`, filled
        with boolean values that are True if the
        corresponding entry in `endog` is NaN and False
        otherwise.
    nmissing : array of int
        An array of size `nobs`, where the ith entry
        is the number (between 0 and `k_endog`) of NaNs in
        the ith row of the `endog` array.
    time_invariant : bool
        Whether or not the representation matrices are time-invariant
    initialization : str
        Kalman filter initialization method.
    initial_state : array_like
        The state vector used to initialize the Kalamn filter.
    initial_state_cov : array_like
        The state covariance matrix used to initialize the Kalamn filter.
    initial_diffuse_state_cov : array_like
        Diffuse state covariance matrix used to initialize the Kalamn filter.
    filter_method : int
        Bitmask representing the Kalman filtering method
    inversion_method : int
        Bitmask representing the method used to
        invert the forecast error covariance matrix.
    stability_method : int
        Bitmask representing the methods used to promote
        numerical stability in the Kalman filter
        recursions.
    conserve_memory : int
        Bitmask representing the selected memory conservation method.
    filter_timing : int
        Whether or not to use the alternate timing convention.
    tolerance : float
        The tolerance at which the Kalman filter
        determines convergence to steady-state.
    loglikelihood_burn : int
        The number of initial periods during which
        the loglikelihood is not recorded.
    converged : bool
        Whether or not the Kalman filter converged.
    period_converged : int
        The time period in which the Kalman filter converged.
    filtered_state : ndarray
        The filtered state vector at each time period.
    filtered_state_cov : ndarray
        The filtered state covariance matrix at each time period.
    predicted_state : ndarray
        The predicted state vector at each time period.
    predicted_state_cov : ndarray
        The predicted state covariance matrix at each time period.
    forecast_error_diffuse_cov : ndarray
        Diffuse forecast error covariance matrix at each time period.
    predicted_diffuse_state_cov : ndarray
        The predicted diffuse state covariance matrix at each time period.
    kalman_gain : ndarray
        The Kalman gain at each time period.
    forecasts : ndarray
        The one-step-ahead forecasts of observations at each time period.
    forecasts_error : ndarray
        The forecast errors at each time period.
    forecasts_error_cov : ndarray
        The forecast error covariance matrices at each time period.
    llf_obs : ndarray
        The loglikelihood values at each time period.
    """
    def __init__(self, model) -> None: ...
    def update_representation(self, model, only_options: bool = False) -> None:
        """
        Update the results to match a given model

        Parameters
        ----------
        model : Representation
            The model object from which to take the updated values.
        only_options : bool, optional
            If set to true, only the filter options are updated, and the state
            space representation is not updated. Default is False.

        Notes
        -----
        This method is rarely required except for internal usage.
        """
    initial_state: Incomplete
    initial_state_cov: Incomplete
    filter_method: Incomplete
    inversion_method: Incomplete
    stability_method: Incomplete
    conserve_memory: Incomplete
    filter_timing: Incomplete
    tolerance: Incomplete
    loglikelihood_burn: Incomplete
    converged: Incomplete
    period_converged: Incomplete
    univariate_filter: Incomplete
    filtered_state: Incomplete
    filtered_state_cov: Incomplete
    predicted_state: Incomplete
    predicted_state_cov: Incomplete
    tmp1: Incomplete
    tmp2: Incomplete
    tmp3: Incomplete
    tmp4: Incomplete
    M: Incomplete
    M_diffuse: Incomplete
    forecasts: Incomplete
    forecasts_error: Incomplete
    forecasts_error_cov: Incomplete
    llf_obs: Incomplete
    nobs_diffuse: Incomplete
    initial_diffuse_state_cov: Incomplete
    forecasts_error_diffuse_cov: Incomplete
    predicted_diffuse_state_cov: Incomplete
    missing_forecasts: Incomplete
    missing_forecasts_error: Incomplete
    missing_forecasts_error_cov: Incomplete
    collapsed_forecasts: Incomplete
    collapsed_forecasts_error: Incomplete
    collapsed_forecasts_error_cov: Incomplete
    scale: float
    obs_cov: Incomplete
    state_cov: Incomplete
    filter_concentrated: bool
    llf: Incomplete
    def update_filter(self, kalman_filter) -> None:
        """
        Update the filter results

        Parameters
        ----------
        kalman_filter : statespace.kalman_filter.KalmanFilter
            The model object from which to take the updated values.

        Notes
        -----
        This method is rarely required except for internal usage.
        """
    @property
    def kalman_gain(self):
        """
        Kalman gain matrices
        """
    @property
    def standardized_forecasts_error(self):
        """
        Standardized forecast errors

        Notes
        -----
        The forecast errors produced by the Kalman filter are

        .. math::

            v_t \\sim N(0, F_t)

        Hypothesis tests are usually applied to the standardized residuals

        .. math::

            v_t^s = B_t v_t \\sim N(0, I)

        where :math:`B_t = L_t^{-1}` and :math:`F_t = L_t L_t'`; then
        :math:`F_t^{-1} = (L_t')^{-1} L_t^{-1} = B_t' B_t`; :math:`B_t`
        and :math:`L_t` are lower triangular. Finally,
        :math:`B_t v_t \\sim N(0, B_t F_t B_t')` and
        :math:`B_t F_t B_t' = L_t^{-1} L_t L_t' (L_t')^{-1} = I`.

        Thus we can rewrite :math:`v_t^s = L_t^{-1} v_t` or
        :math:`L_t v_t^s = v_t`; the latter equation is the form required to
        use a linear solver to recover :math:`v_t^s`. Since :math:`L_t` is
        lower triangular, we can use a triangular solver (?TRTRS).
        """
    def predict(self, start: Incomplete | None = None, end: Incomplete | None = None, dynamic: Incomplete | None = None, **kwargs):
        """
        In-sample and out-of-sample prediction for state space models generally

        Parameters
        ----------
        start : int, optional
            Zero-indexed observation number at which to start prediction, i.e.,
            the first prediction will be at start.
        end : int, optional
            Zero-indexed observation number at which to end prediction, i.e.,
            the last prediction will be at end.
        dynamic : int, optional
            Offset relative to `start` at which to begin dynamic prediction.
            Prior to this observation, true endogenous values will be used for
            prediction; starting with this observation and continuing through
            the end of prediction, predicted endogenous values will be used
            instead.
        **kwargs
            If the prediction range is outside of the sample range, any
            of the state space representation matrices that are time-varying
            must have updated values provided for the out-of-sample range.
            For example, of `obs_intercept` is a time-varying component and
            the prediction range extends 10 periods beyond the end of the
            sample, a (`k_endog` x 10) matrix must be provided with the new
            intercept values.

        Returns
        -------
        results : kalman_filter.PredictionResults
            A PredictionResults object.

        Notes
        -----
        All prediction is performed by applying the deterministic part of the
        measurement equation using the predicted state variables.

        Out-of-sample prediction first applies the Kalman filter to missing
        data for the number of periods desired to obtain the predicted states.
        """

class PredictionResults(FilterResults):
    """
    Results of in-sample and out-of-sample prediction for state space models
    generally

    Parameters
    ----------
    results : FilterResults
        Output from filtering, corresponding to the prediction desired
    start : int
        Zero-indexed observation number at which to start forecasting,
        i.e., the first forecast will be at start.
    end : int
        Zero-indexed observation number at which to end forecasting, i.e.,
        the last forecast will be at end.
    nstatic : int
        Number of in-sample static predictions (these are always the first
        elements of the prediction output).
    ndynamic : int
        Number of in-sample dynamic predictions (these always follow the static
        predictions directly, and are directly followed by the forecasts).
    nforecast : int
        Number of in-sample forecasts (these always follow the dynamic
        predictions directly).

    Attributes
    ----------
    npredictions : int
        Number of observations in the predicted series; this is not necessarily
        the same as the number of observations in the original model from which
        prediction was performed.
    start : int
        Zero-indexed observation number at which to start prediction,
        i.e., the first predict will be at `start`; this is relative to the
        original model from which prediction was performed.
    end : int
        Zero-indexed observation number at which to end prediction,
        i.e., the last predict will be at `end`; this is relative to the
        original model from which prediction was performed.
    nstatic : int
        Number of in-sample static predictions.
    ndynamic : int
        Number of in-sample dynamic predictions.
    nforecast : int
        Number of in-sample forecasts.
    endog : ndarray
        The observation vector.
    design : ndarray
        The design matrix, :math:`Z`.
    obs_intercept : ndarray
        The intercept for the observation equation, :math:`d`.
    obs_cov : ndarray
        The covariance matrix for the observation equation :math:`H`.
    transition : ndarray
        The transition matrix, :math:`T`.
    state_intercept : ndarray
        The intercept for the transition equation, :math:`c`.
    selection : ndarray
        The selection matrix, :math:`R`.
    state_cov : ndarray
        The covariance matrix for the state equation :math:`Q`.
    filtered_state : ndarray
        The filtered state vector at each time period.
    filtered_state_cov : ndarray
        The filtered state covariance matrix at each time period.
    predicted_state : ndarray
        The predicted state vector at each time period.
    predicted_state_cov : ndarray
        The predicted state covariance matrix at each time period.
    forecasts : ndarray
        The one-step-ahead forecasts of observations at each time period.
    forecasts_error : ndarray
        The forecast errors at each time period.
    forecasts_error_cov : ndarray
        The forecast error covariance matrices at each time period.

    Notes
    -----
    The provided ranges must be conformable, meaning that it must be that
    `end - start == nstatic + ndynamic + nforecast`.

    This class is essentially a view to the FilterResults object, but
    returning the appropriate ranges for everything.
    """
    representation_attributes: Incomplete
    filter_attributes: Incomplete
    smoother_attributes: Incomplete
    results: Incomplete
    oos_results: Incomplete
    npredictions: Incomplete
    start: Incomplete
    end: Incomplete
    nstatic: Incomplete
    ndynamic: Incomplete
    nforecast: Incomplete
    def __init__(self, results, start, end, nstatic, ndynamic, nforecast, oos_results: Incomplete | None = None) -> None: ...
    def clear(self) -> None: ...
    def __getattr__(self, attr):
        """
        Provide access to the representation and filtered output in the
        appropriate range (`start` - `end`).
        """
    @property
    def predicted_signal(self): ...
    @property
    def predicted_signal_cov(self): ...
    @property
    def filtered_signal(self): ...
    @property
    def filtered_signal_cov(self): ...
    @property
    def smoothed_signal(self): ...
    @property
    def smoothed_signal_cov(self): ...
    @property
    def filtered_forecasts(self): ...
    @property
    def filtered_forecasts_error_cov(self): ...
    @property
    def smoothed_forecasts(self): ...
    @property
    def smoothed_forecasts_error_cov(self): ...
