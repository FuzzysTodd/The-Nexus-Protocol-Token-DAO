from . import tools as tools
from .initialization import Initialization as Initialization
from .tools import find_best_blas_type as find_best_blas_type, validate_matrix_shape as validate_matrix_shape, validate_vector_shape as validate_vector_shape
from _typeshed import Incomplete

class OptionWrapper:
    mask_attribute: Incomplete
    mask_value: Incomplete
    def __init__(self, mask_attribute, mask_value) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, value) -> None: ...

class MatrixWrapper:
    name: Incomplete
    attribute: Incomplete
    def __init__(self, name, attribute) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, value) -> None: ...

class Representation:
    """
    State space representation of a time series process

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
    initial_variance : float, optional
        Initial variance used when approximate diffuse initialization is
        specified. Default is 1e6.
    initialization : Initialization object or str, optional
        Initialization method for the initial state. If a string, must be one
        of {'diffuse', 'approximate_diffuse', 'stationary', 'known'}.
    initial_state : array_like, optional
        If `initialization='known'` is used, the mean of the initial state's
        distribution.
    initial_state_cov : array_like, optional
        If `initialization='known'` is used, the covariance matrix of the
        initial state's distribution.
    nobs : int, optional
        If an endogenous vector is not given (i.e. `k_endog` is an integer),
        the number of observations can optionally be specified. If not
        specified, they will be set to zero until data is bound to the model.
    dtype : np.dtype, optional
        If an endogenous vector is not given (i.e. `k_endog` is an integer),
        the default datatype of the state space matrices can optionally be
        specified. Default is `np.float64`.
    design : array_like, optional
        The design matrix, :math:`Z`. Default is set to zeros.
    obs_intercept : array_like, optional
        The intercept for the observation equation, :math:`d`. Default is set
        to zeros.
    obs_cov : array_like, optional
        The covariance matrix for the observation equation :math:`H`. Default
        is set to zeros.
    transition : array_like, optional
        The transition matrix, :math:`T`. Default is set to zeros.
    state_intercept : array_like, optional
        The intercept for the transition equation, :math:`c`. Default is set to
        zeros.
    selection : array_like, optional
        The selection matrix, :math:`R`. Default is set to zeros.
    state_cov : array_like, optional
        The covariance matrix for the state equation :math:`Q`. Default is set
        to zeros.
    **kwargs
        Additional keyword arguments. Not used directly. It is present to
        improve compatibility with subclasses, so that they can use `**kwargs`
        to specify any default state space matrices (e.g. `design`) without
        having to clean out any other keyword arguments they might have been
        passed.

    Attributes
    ----------
    nobs : int
        The number of observations.
    k_endog : int
        The dimension of the observation series.
    k_states : int
        The dimension of the unobserved state process.
    k_posdef : int
        The dimension of a guaranteed positive
        definite covariance matrix describing
        the shocks in the measurement equation.
    shapes : dictionary of name:tuple
        A dictionary recording the initial shapes
        of each of the representation matrices as
        tuples.
    initialization : str
        Kalman filter initialization method. Default is unset.
    initial_variance : float
        Initial variance for approximate diffuse
        initialization. Default is 1e6.

    Notes
    -----
    A general state space model is of the form

    .. math::

        y_t & = Z_t \\alpha_t + d_t + \\varepsilon_t \\\\\n        \\alpha_t & = T_t \\alpha_{t-1} + c_t + R_t \\eta_t \\\\\n
    where :math:`y_t` refers to the observation vector at time :math:`t`,
    :math:`\\alpha_t` refers to the (unobserved) state vector at time
    :math:`t`, and where the irregular components are defined as

    .. math::

        \\varepsilon_t \\sim N(0, H_t) \\\\\n        \\eta_t \\sim N(0, Q_t) \\\\\n
    The remaining variables (:math:`Z_t, d_t, H_t, T_t, c_t, R_t, Q_t`) in the
    equations are matrices describing the process. Their variable names and
    dimensions are as follows

    Z : `design`          :math:`(k\\_endog \\times k\\_states \\times nobs)`

    d : `obs_intercept`   :math:`(k\\_endog \\times nobs)`

    H : `obs_cov`         :math:`(k\\_endog \\times k\\_endog \\times nobs)`

    T : `transition`      :math:`(k\\_states \\times k\\_states \\times nobs)`

    c : `state_intercept` :math:`(k\\_states \\times nobs)`

    R : `selection`       :math:`(k\\_states \\times k\\_posdef \\times nobs)`

    Q : `state_cov`       :math:`(k\\_posdef \\times k\\_posdef \\times nobs)`

    In the case that one of the matrices is time-invariant (so that, for
    example, :math:`Z_t = Z_{t+1} ~ \\forall ~ t`), its last dimension may
    be of size :math:`1` rather than size `nobs`.

    References
    ----------
    .. [*] Durbin, James, and Siem Jan Koopman. 2012.
       Time Series Analysis by State Space Methods: Second Edition.
       Oxford University Press.
    """
    endog: Incomplete
    design: Incomplete
    obs_intercept: Incomplete
    obs_cov: Incomplete
    transition: Incomplete
    state_intercept: Incomplete
    selection: Incomplete
    state_cov: Incomplete
    shapes: Incomplete
    k_endog: Incomplete
    nobs: Incomplete
    k_states: Incomplete
    k_posdef: Incomplete
    initial_variance: Incomplete
    prefix_statespace_map: Incomplete
    initialization: Incomplete
    def __init__(self, k_endog, k_states, k_posdef: Incomplete | None = None, initial_variance: float = 1000000.0, nobs: int = 0, dtype=..., design: Incomplete | None = None, obs_intercept: Incomplete | None = None, obs_cov: Incomplete | None = None, transition: Incomplete | None = None, state_intercept: Incomplete | None = None, selection: Incomplete | None = None, state_cov: Incomplete | None = None, statespace_classes: Incomplete | None = None, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def clone(self, endog, **kwargs):
        """
        Clone a state space representation while overriding some elements

        Parameters
        ----------
        endog : array_like
            An observed time-series process :math:`y`.
        **kwargs
            Keyword arguments to pass to the new state space representation
            model constructor. Those that are not specified are copied from
            the specification of the current state space model.

        Returns
        -------
        Representation

        Notes
        -----
        If some system matrices are time-varying, then new time-varying
        matrices *must* be provided.
        """
    def extend(self, endog, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs):
        """
        Extend the current state space model, or a specific (time) subset

        Parameters
        ----------
        endog : array_like
            An observed time-series process :math:`y`.
        start : int, optional
            The first period of a time-varying state space model to include in
            the new model. Has no effect if the state space model is
            time-invariant. Default is the initial period.
        end : int, optional
            The last period of a time-varying state space model to include in
            the new model. Has no effect if the state space model is
            time-invariant. Default is the final period.
        **kwargs
            Keyword arguments to pass to the new state space representation
            model constructor. Those that are not specified are copied from
            the specification of the current state space model.

        Returns
        -------
        Representation

        Notes
        -----
        This method does not allow replacing a time-varying system matrix with
        a time-invariant one (or vice-versa). If that is required, use `clone`.
        """
    def diff_endog(self, new_endog, tolerance: float = 1e-10): ...
    @property
    def prefix(self):
        """
        (str) BLAS prefix of currently active representation matrices
        """
    @property
    def dtype(self):
        """
        (dtype) Datatype of currently active representation matrices
        """
    @property
    def time_invariant(self):
        """
        (bool) Whether or not currently active representation matrices are
        time-invariant
        """
    @property
    def obs(self):
        """
        (array) Observation vector: :math:`y~(k\\_endog \\times nobs)`
        """
    def bind(self, endog) -> None:
        """
        Bind data to the statespace representation

        Parameters
        ----------
        endog : ndarray
            Endogenous data to bind to the model. Must be column-ordered
            ndarray with shape (`k_endog`, `nobs`) or row-ordered ndarray with
            shape (`nobs`, `k_endog`).

        Notes
        -----
        The strict requirements arise because the underlying statespace and
        Kalman filtering classes require Fortran-ordered arrays in the wide
        format (shaped (`k_endog`, `nobs`)), and this structure is setup to
        prevent copying arrays in memory.

        By default, numpy arrays are row (C)-ordered and most time series are
        represented in the long format (with time on the 0-th axis). In this
        case, no copying or re-ordering needs to be performed, instead the
        array can simply be transposed to get it in the right order and shape.

        Although this class (Representation) has stringent `bind` requirements,
        it is assumed that it will rarely be used directly.
        """
    def initialize(self, initialization, approximate_diffuse_variance: Incomplete | None = None, constant: Incomplete | None = None, stationary_cov: Incomplete | None = None, a: Incomplete | None = None, Pstar: Incomplete | None = None, Pinf: Incomplete | None = None, A: Incomplete | None = None, R0: Incomplete | None = None, Q0: Incomplete | None = None) -> None:
        """Create an Initialization object if necessary"""
    def initialize_known(self, constant, stationary_cov) -> None:
        """
        Initialize the statespace model with known distribution for initial
        state.

        These values are assumed to be known with certainty or else
        filled with parameters during, for example, maximum likelihood
        estimation.

        Parameters
        ----------
        constant : array_like
            Known mean of the initial state vector.
        stationary_cov : array_like
            Known covariance matrix of the initial state vector.
        """
    def initialize_approximate_diffuse(self, variance: Incomplete | None = None) -> None:
        """
        Initialize the statespace model with approximate diffuse values.

        Rather than following the exact diffuse treatment (which is developed
        for the case that the variance becomes infinitely large), this assigns
        an arbitrary large number for the variance.

        Parameters
        ----------
        variance : float, optional
            The variance for approximating diffuse initial conditions. Default
            is 1e6.
        """
    def initialize_components(self, a: Incomplete | None = None, Pstar: Incomplete | None = None, Pinf: Incomplete | None = None, A: Incomplete | None = None, R0: Incomplete | None = None, Q0: Incomplete | None = None) -> None:
        """
        Initialize the statespace model with component matrices

        Parameters
        ----------
        a : array_like, optional
            Vector of constant values describing the mean of the stationary
            component of the initial state.
        Pstar : array_like, optional
            Stationary component of the initial state covariance matrix. If
            given, should be a matrix shaped `k_states x k_states`. The
            submatrix associated with the diffuse states should contain zeros.
            Note that by definition, `Pstar = R0 @ Q0 @ R0.T`, so either
            `R0,Q0` or `Pstar` may be given, but not both.
        Pinf : array_like, optional
            Diffuse component of the initial state covariance matrix. If given,
            should be a matrix shaped `k_states x k_states` with ones in the
            diagonal positions corresponding to states with diffuse
            initialization and zeros otherwise. Note that by definition,
            `Pinf = A @ A.T`, so either `A` or `Pinf` may be given, but not
            both.
        A : array_like, optional
            Diffuse selection matrix, used in the definition of the diffuse
            initial state covariance matrix. If given, should be a
            `k_states x k_diffuse_states` matrix that contains the subset of
            the columns of the identity matrix that correspond to states with
            diffuse initialization. Note that by definition, `Pinf = A @ A.T`,
            so either `A` or `Pinf` may be given, but not both.
        R0 : array_like, optional
            Stationary selection matrix, used in the definition of the
            stationary initial state covariance matrix. If given, should be a
            `k_states x k_nondiffuse_states` matrix that contains the subset of
            the columns of the identity matrix that correspond to states with a
            non-diffuse initialization. Note that by definition,
            `Pstar = R0 @ Q0 @ R0.T`, so either `R0,Q0` or `Pstar` may be
            given, but not both.
        Q0 : array_like, optional
            Covariance matrix associated with stationary initial states. If
            given, should be a matrix shaped
            `k_nondiffuse_states x k_nondiffuse_states`.
            Note that by definition, `Pstar = R0 @ Q0 @ R0.T`, so either
            `R0,Q0` or `Pstar` may be given, but not both.

        Notes
        -----
        The matrices `a, Pstar, Pinf, A, R0, Q0` and the process for
        initializing the state space model is as given in Chapter 5 of [1]_.
        For the definitions of these matrices, see equation (5.2) and the
        subsequent discussion there.

        References
        ----------
        .. [1] Durbin, James, and Siem Jan Koopman. 2012.
           Time Series Analysis by State Space Methods: Second Edition.
           Oxford University Press.
        """
    def initialize_stationary(self) -> None:
        """
        Initialize the statespace model as stationary.
        """
    def initialize_diffuse(self) -> None:
        """
        Initialize the statespace model as diffuse.
        """

class FrozenRepresentation:
    """
    Frozen Statespace Model

    Takes a snapshot of a Statespace model.

    Parameters
    ----------
    model : Representation
        A Statespace representation

    Attributes
    ----------
    nobs : int
        Number of observations.
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
    shapes : dictionary of name:tuple
        A dictionary recording the shapes of each of
        the representation matrices as tuples.
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
    initialization : Initialization object
        Kalman filter initialization method.
    initial_state : array_like
        The state vector used to initialize the Kalamn filter.
    initial_state_cov : array_like
        The state covariance matrix used to initialize the Kalamn filter.
    """
    def __init__(self, model) -> None: ...
    model: Incomplete
    prefix: Incomplete
    dtype: Incomplete
    nobs: Incomplete
    k_endog: Incomplete
    k_states: Incomplete
    k_posdef: Incomplete
    time_invariant: Incomplete
    endog: Incomplete
    design: Incomplete
    obs_intercept: Incomplete
    obs_cov: Incomplete
    transition: Incomplete
    state_intercept: Incomplete
    selection: Incomplete
    state_cov: Incomplete
    missing: Incomplete
    nmissing: Incomplete
    shapes: Incomplete
    initialization: Incomplete
    initial_state: Incomplete
    initial_state_cov: Incomplete
    initial_diffuse_state_cov: Incomplete
    def update_representation(self, model) -> None:
        """Update model Representation"""
