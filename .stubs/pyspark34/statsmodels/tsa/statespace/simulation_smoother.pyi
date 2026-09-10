from . import tools as tools
from .cfa_simulation_smoother import CFASimulationSmoother as CFASimulationSmoother
from .kalman_smoother import KalmanSmoother as KalmanSmoother
from _typeshed import Incomplete

SIMULATION_STATE: int
SIMULATION_DISTURBANCE: int
SIMULATION_ALL: Incomplete

def check_random_state(seed: Incomplete | None = None):
    """Turn `seed` into a `numpy.random.Generator` instance.
    Parameters
    ----------
    seed : {None, int, Generator, RandomState}, optional
        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``numpy.random.RandomState`` instance
        is used, seeded with `seed`.
        If `seed` is already a ``numpy.random.Generator`` or
        ``numpy.random.RandomState`` instance then that instance is used.
    Returns
    -------
    seed : {`numpy.random.Generator`, `numpy.random.RandomState`}
        Random number generator.
    """

class SimulationSmoother(KalmanSmoother):
    """
    State space representation of a time series process, with Kalman filter
    and smoother, and with simulation smoother.

    Parameters
    ----------
    k_endog : {array_like, int}
        The observed time-series process :math:`y` if array like or the
        number of variables in the process if an integer.
    k_states : int
        The dimension of the unobserved state process.
    k_posdef : int, optional
        The dimension of a guaranteed positive definite covariance matrix
        describing the shocks in the measurement equation. Must be less than
        or equal to `k_states`. Default is `k_states`.
    simulation_smooth_results_class : class, optional
        Default results class to use to save output of simulation smoothing.
        Default is `SimulationSmoothResults`. If specified, class must extend
        from `SimulationSmoothResults`.
    simulation_smoother_classes : dict, optional
        Dictionary with BLAS prefixes as keys and classes as values.
    **kwargs
        Keyword arguments may be used to provide default values for state space
        matrices, for Kalman filtering options, for Kalman smoothing
        options, or for Simulation smoothing options.
        See `Representation`, `KalmanFilter`, and `KalmanSmoother` for more
        details.
    """
    simulation_outputs: Incomplete
    simulation_smooth_results_class: Incomplete
    prefix_simulation_smoother_map: Incomplete
    def __init__(self, k_endog, k_states, k_posdef: Incomplete | None = None, simulation_smooth_results_class: Incomplete | None = None, simulation_smoother_classes: Incomplete | None = None, **kwargs) -> None: ...
    def get_simulation_output(self, simulation_output: Incomplete | None = None, simulate_state: Incomplete | None = None, simulate_disturbance: Incomplete | None = None, simulate_all: Incomplete | None = None, **kwargs):
        """
        Get simulation output bitmask

        Helper method to get final simulation output bitmask from a set of
        optional arguments including the bitmask itself and possibly boolean
        flags.

        Parameters
        ----------
        simulation_output : int, optional
            Simulation output bitmask. If this is specified, it is simply
            returned and the other arguments are ignored.
        simulate_state : bool, optional
            Whether or not to include the state in the simulation output.
        simulate_disturbance : bool, optional
            Whether or not to include the state and observation disturbances
            in the simulation output.
        simulate_all : bool, optional
            Whether or not to include all simulation output.
        \\*\\*kwargs
            Additional keyword arguments. Present so that calls to this method
            can use \\*\\*kwargs without clearing out additional arguments.
        """
    def simulator(self, nsimulations, random_state: Incomplete | None = None): ...
    def simulation_smoother(self, simulation_output: Incomplete | None = None, method: str = 'kfs', results_class: Incomplete | None = None, prefix: Incomplete | None = None, nobs: int = -1, random_state: Incomplete | None = None, **kwargs):
        """
        Retrieve a simulation smoother for the statespace model.

        Parameters
        ----------
        simulation_output : int, optional
            Determines which simulation smoother output is calculated.
            Default is all (including state and disturbances).
        method : {'kfs', 'cfa'}, optional
            Method for simulation smoothing. If `method='kfs'`, then the
            simulation smoother is based on Kalman filtering and smoothing
            recursions. If `method='cfa'`, then the simulation smoother is
            based on the Cholesky Factor Algorithm (CFA) approach. The CFA
            approach is not applicable to all state space models, but can be
            faster for the cases in which it is supported.
        results_class : class, optional
            Default results class to use to save output of simulation
            smoothing. Default is `SimulationSmoothResults`. If specified,
            class must extend from `SimulationSmoothResults`.
        prefix : str
            The prefix of the datatype. Usually only used internally.
        nobs : int
            The number of observations to simulate. If set to anything other
            than -1, only simulation will be performed (i.e. simulation
            smoothing will not be performed), so that only the `generated_obs`
            and `generated_state` attributes will be available.
        random_state : {None, int, Generator, RandomState}, optional
            If `seed` is None (or `np.random`), the `numpy.random.RandomState`
            singleton is used.
            If `seed` is an int, a new ``numpy.random.RandomState`` instance
            is used, seeded with `seed`.
            If `seed` is already a ``numpy.random.Generator`` or
            ``numpy.random.RandomState`` instance then that instance is used.
        **kwargs
            Additional keyword arguments, used to set the simulation output.
            See `set_simulation_output` for more details.

        Returns
        -------
        SimulationSmoothResults
        """

class SimulationSmoothResults:
    """
    Results from applying the Kalman smoother and/or filter to a state space
    model.

    Parameters
    ----------
    model : Representation
        A Statespace representation
    simulation_smoother : {{prefix}}SimulationSmoother object
        The Cython simulation smoother object with which to simulation smooth.
    random_state : {None, int, Generator, RandomState}, optional
        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``numpy.random.RandomState`` instance
        is used, seeded with `seed`.
        If `seed` is already a ``numpy.random.Generator`` or
        ``numpy.random.RandomState`` instance then that instance is used.

    Attributes
    ----------
    model : Representation
        A Statespace representation
    dtype : dtype
        Datatype of representation matrices
    prefix : str
        BLAS prefix of representation matrices
    simulation_output : int
        Bitmask controlling simulation output.
    simulate_state : bool
        Flag for if the state is included in simulation output.
    simulate_disturbance : bool
        Flag for if the state and observation disturbances are included in
        simulation output.
    simulate_all : bool
        Flag for if simulation output should include everything.
    generated_measurement_disturbance : ndarray
        Measurement disturbance variates used to genereate the observation
        vector.
    generated_state_disturbance : ndarray
        State disturbance variates used to genereate the state and
        observation vectors.
    generated_obs : ndarray
        Generated observation vector produced as a byproduct of simulation
        smoothing.
    generated_state : ndarray
        Generated state vector produced as a byproduct of simulation smoothing.
    simulated_state : ndarray
        Simulated state.
    simulated_measurement_disturbance : ndarray
        Simulated measurement disturbance.
    simulated_state_disturbance : ndarray
        Simulated state disturbance.
    """
    model: Incomplete
    prefix: Incomplete
    dtype: Incomplete
    random_state: Incomplete
    def __init__(self, model, simulation_smoother, random_state: Incomplete | None = None) -> None: ...
    @property
    def simulation_output(self): ...
    @simulation_output.setter
    def simulation_output(self, value) -> None: ...
    @property
    def simulate_state(self): ...
    @simulate_state.setter
    def simulate_state(self, value) -> None: ...
    @property
    def simulate_disturbance(self): ...
    @simulate_disturbance.setter
    def simulate_disturbance(self, value) -> None: ...
    @property
    def simulate_all(self): ...
    @simulate_all.setter
    def simulate_all(self, value) -> None: ...
    @property
    def generated_measurement_disturbance(self):
        """
        Randomly drawn measurement disturbance variates

        Used to construct `generated_obs`.

        Notes
        -----

        .. math::

           \\varepsilon_t^+ ~ N(0, H_t)

        If `disturbance_variates` were provided to the `simulate()` method,
        then this returns those variates (which were N(0,1)) transformed to the
        distribution above.
        """
    @property
    def generated_state_disturbance(self):
        """
        Randomly drawn state disturbance variates, used to construct
        `generated_state` and `generated_obs`.

        Notes
        -----

        .. math::

            \\eta_t^+ ~ N(0, Q_t)

        If `disturbance_variates` were provided to the `simulate()` method,
        then this returns those variates (which were N(0,1)) transformed to the
        distribution above.
        """
    @property
    def generated_obs(self):
        """
        Generated vector of observations by iterating on the observation and
        transition equations, given a random initial state draw and random
        disturbance draws.

        Notes
        -----

        .. math::

            y_t^+ = d_t + Z_t \\alpha_t^+ + \\varepsilon_t^+
        """
    @property
    def generated_state(self):
        """
        Generated vector of states by iterating on the transition equation,
        given a random initial state draw and random disturbance draws.

        Notes
        -----

        .. math::

            \\alpha_{t+1}^+ = c_t + T_t \\alpha_t^+ + \\eta_t^+
        """
    @property
    def simulated_state(self):
        """
        Random draw of the state vector from its conditional distribution.

        Notes
        -----

        .. math::

            \\alpha ~ p(\\alpha \\mid Y_n)
        """
    @property
    def simulated_measurement_disturbance(self):
        """
        Random draw of the measurement disturbance vector from its conditional
        distribution.

        Notes
        -----

        .. math::

            \\varepsilon ~ N(\\hat \\varepsilon, Var(\\hat \\varepsilon \\mid Y_n))
        """
    @property
    def simulated_state_disturbance(self):
        """
        Random draw of the state disturbanc e vector from its conditional
        distribution.

        Notes
        -----

        .. math::

            \\eta ~ N(\\hat \\eta, Var(\\hat \\eta \\mid Y_n))
        """
    def simulate(self, simulation_output: int = -1, disturbance_variates: Incomplete | None = None, measurement_disturbance_variates: Incomplete | None = None, state_disturbance_variates: Incomplete | None = None, initial_state_variates: Incomplete | None = None, pretransformed: Incomplete | None = None, pretransformed_measurement_disturbance_variates: Incomplete | None = None, pretransformed_state_disturbance_variates: Incomplete | None = None, pretransformed_initial_state_variates: bool = False, random_state: Incomplete | None = None) -> None:
        """
        Perform simulation smoothing

        Does not return anything, but populates the object's `simulated_*`
        attributes, as specified by simulation output.

        Parameters
        ----------
        simulation_output : int, optional
            Bitmask controlling simulation output. Default is to use the
            simulation output defined in object initialization.
        measurement_disturbance_variates : array_like, optional
            If specified, these are the shocks to the measurement equation,
            :math:`\\varepsilon_t`. If unspecified, these are automatically
            generated using a pseudo-random number generator. If specified,
            must be shaped `nsimulations` x `k_endog`, where `k_endog` is the
            same as in the state space model.
        state_disturbance_variates : array_like, optional
            If specified, these are the shocks to the state equation,
            :math:`\\eta_t`. If unspecified, these are automatically
            generated using a pseudo-random number generator. If specified,
            must be shaped `nsimulations` x `k_posdef` where `k_posdef` is the
            same as in the state space model.
        initial_state_variates : array_like, optional
            If specified, this is the state vector at time zero, which should
            be shaped (`k_states` x 1), where `k_states` is the same as in the
            state space model. If unspecified, but the model has been
            initialized, then that initialization is used.
        initial_state_variates : array_likes, optional
            Random values to use as initial state variates. Usually only
            specified if results are to be replicated (e.g. to enforce a seed)
            or for testing. If not specified, random variates are drawn.
        pretransformed_measurement_disturbance_variates : bool, optional
            If `measurement_disturbance_variates` is provided, this flag
            indicates whether it should be directly used as the shocks. If
            False, then it is assumed to contain draws from the standard Normal
            distribution that must be transformed using the `obs_cov`
            covariance matrix. Default is False.
        pretransformed_state_disturbance_variates : bool, optional
            If `state_disturbance_variates` is provided, this flag indicates
            whether it should be directly used as the shocks. If False, then it
            is assumed to contain draws from the standard Normal distribution
            that must be transformed using the `state_cov` covariance matrix.
            Default is False.
        pretransformed_initial_state_variates : bool, optional
            If `initial_state_variates` is provided, this flag indicates
            whether it should be directly used as the initial_state. If False,
            then it is assumed to contain draws from the standard Normal
            distribution that must be transformed using the `initial_state_cov`
            covariance matrix. Default is False.
        random_state : {None, int, Generator, RandomState}, optional
            If `seed` is None (or `np.random`), the `numpy.random.RandomState`
            singleton is used.
            If `seed` is an int, a new ``numpy.random.RandomState`` instance
            is used, seeded with `seed`.
            If `seed` is already a ``numpy.random.Generator`` or
            ``numpy.random.RandomState`` instance then that instance is used.
        disturbance_variates : bool, optional
            Deprecated, please use pretransformed_measurement_shocks and
            pretransformed_state_shocks instead.

            .. deprecated:: 0.14.0

               Use ``measurement_disturbance_variates`` and
               ``state_disturbance_variates`` as replacements.

        pretransformed : bool, optional
            Deprecated, please use pretransformed_measurement_shocks and
            pretransformed_state_shocks instead.

            .. deprecated:: 0.14.0

               Use ``pretransformed_measurement_disturbance_variates`` and
               ``pretransformed_state_disturbance_variates`` as replacements.
        """
