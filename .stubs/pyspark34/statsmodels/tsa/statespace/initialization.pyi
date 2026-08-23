from . import tools as tools
from _typeshed import Incomplete

class Initialization:
    """
    State space initialization

    Parameters
    ----------
    k_states : int
    exact_diffuse_initialization : bool, optional
        Whether or not to use exact diffuse initialization; only has an effect
        if some states are initialized as diffuse. Default is True.
    approximate_diffuse_variance : float, optional
        If using approximate diffuse initialization, the initial variance used.
        Default is 1e6.

    Notes
    -----
    As developed in Durbin and Koopman (2012), the state space recursions
    must be initialized for the first time period. The general form of this
    initialization is:

    .. math::

        \\alpha_1 & = a + A \\delta + R_0 \\eta_0 \\\\\n        \\delta & \\sim N(0, \\kappa I), \\kappa \\to \\infty \\\\\n        \\eta_0 & \\sim N(0, Q_0)

    Thus the state vector can be initialized with a known constant part
    (elements of :math:`a`), with part modeled as a diffuse initial
    distribution (as a part of :math:`\\delta`), and with a part modeled as a
    known (proper) initial distribution (as a part of :math:`\\eta_0`).

    There are two important restrictions:

    1. An element of the state vector initialized as diffuse cannot be also
       modeled with a stationary component. In the `validate` method,
       violations of this cause an exception to be raised.
    2. If an element of the state vector is initialized with both a known
       constant part and with a diffuse initial distribution, the effect of
       the diffuse initialization will essentially ignore the given known
       constant value. In the `validate` method, violations of this cause a
       warning to be given, since it is not technically invalid but may
       indicate user error.

    The :math:`\\eta_0` compoenent is also referred to as the stationary part
    because it is often set to the unconditional distribution of a stationary
    process.

    Initialization is specified for blocks (consecutive only, for now) of the
    state vector, with the entire state vector and individual elements as
    special cases. Denote the block in question as :math:`\\alpha_1^{(i)}`. It
    can be initialized in the following ways:

    - 'known'
    - 'diffuse' or 'exact_diffuse' or 'approximate_diffuse'
    - 'stationary'
    - 'mixed'

    In the first three cases, the block's initialization is specified as an
    instance of the `Initialization` class, with the `initialization_type`
    attribute set to one of those three string values. In the 'mixed' cases,
    the initialization is also an instance of the `Initialization` class, but
    it will itself contain sub-blocks. Details of each type follow.

    Regardless of the type, for each block, the following must be defined:
    the `constant` array, an array `diffuse` with indices corresponding to
    diffuse elements, an array `stationary` with indices corresponding to
    stationary elements, and `stationary_cov`, a matrix with order equal to the
    number of stationary elements in the block.

    **Known**

    If a block is initialized as known, then a known (possibly degenerate)
    distribution is used; in particular, the block of states is understood to
    be distributed
    :math:`\\alpha_1^{(i)} \\sim N(a^{(i)}, Q_0^{(i)})`. Here, is is possible to
    set :math:`a^{(i)} = 0`, and it is also possible that
    :math:`Q_0^{(i)}` is only positive-semidefinite; i.e.
    :math:`\\alpha_1^{(i)}` may be degenerate. One particular example is
    that if the entire block's initial values are known, then
    :math:`R_0^{(i)} = 0`, and so `Var(\\alpha_1^{(i)}) = 0`.

    Here, `constant` must be provided (although it can be zeros), and
    `stationary_cov` is optional (by default it is a matrix of zeros).

    **Diffuse**

    If a block is initialized as diffuse, then set
    :math:`\\alpha_1^{(i)} \\sim N(a^{(i)}, \\kappa^{(i)} I)`. If the block is
    initialized using the exact diffuse initialization procedure, then it is
    understood that :math:`\\kappa^{(i)} \\to \\infty`.

    If the block is initialized using the approximate diffuse initialization
    procedure, then `\\kappa^{(i)}` is set to some large value rather than
    driven to infinity.

    In the approximate diffuse initialization case, it is possible, although
    unlikely, that a known constant value may have some effect on
    initialization if :math:`\\kappa^{(i)}` is not set large enough.

    Here, `constant` may be provided, and `approximate_diffuse_variance` may be
    provided.

    **Stationary**

    If a block is initialized as stationary, then the block of states is
    understood to have the distribution
    :math:`\\alpha_1^{(i)} \\sim N(a^{(i)}, Q_0^{(i)})`. :math:`a^{(i)}` is
    the unconditional mean of the block, computed as
    :math:`(I - T^{(i)})^{-1} c_t`. :math:`Q_0^{(i)}` is the unconditional
    variance of the block, computed as the solution to the discrete Lyapunov
    equation:

    .. math::

        T^{(i)} Q_0^{(i)} T^{(i)} + (R Q R')^{(i)} = Q_0^{(i)}

    :math:`T^{(i)}` and :math:`(R Q R')^{(i)}` are the submatrices of
    the corresponding state space system matrices corresponding to the given
    block of states.

    Here, no values can be provided.

    **Mixed**

    In this case, the block can be further broken down into sub-blocks.
    Usually, only the top-level `Initialization` instance will be of 'mixed'
    type, and in many cases, even the top-level instance will be purely
    'known', 'diffuse', or 'stationary'.

    For a block of type mixed, suppose that it has `J` sub-blocks,
    :math:`\\alpha_1^{(i,j)}`. Then
    :math:`\\alpha_1^{(i)} = a^{(i)} + A^{(i)} \\delta + R_0^{(i)} \\eta_0^{(i)}`.

    Examples
    --------

    Basic examples have one specification for all of the states:

    >>> Initialization(k_states=2, 'known', constant=[0, 1])
    >>> Initialization(k_states=2, 'known', stationary_cov=np.eye(2))
    >>> Initialization(k_states=2, 'known', constant=[0, 1],
                       stationary_cov=np.eye(2))
    >>> Initialization(k_states=2, 'diffuse')
    >>> Initialization(k_states=2, 'approximate_diffuse',
                       approximate_diffuse_variance=1e6)
    >>> Initialization(k_states=2, 'stationary')

    More complex examples initialize different blocks of states separately

    >>> init = Initialization(k_states=3)
    >>> init.set((0, 1), 'known', constant=[0, 1])
    >>> init.set((0, 1), 'known', stationary_cov=np.eye(2))
    >>> init.set((0, 1), 'known', constant=[0, 1],
                 stationary_cov=np.eye(2))
    >>> init.set((0, 1), 'diffuse')
    >>> init.set((0, 1), 'approximate_diffuse',
                 approximate_diffuse_variance=1e6)
    >>> init.set((0, 1), 'stationary')

    A still more complex example initializes a block using a previously
    created `Initialization` object:

    >>> init1 = Initialization(k_states=2, 'known', constant=[0, 1])
    >>> init2 = Initialization(k_states=3)
    >>> init2.set((1, 2), init1)
    """
    k_states: Incomplete
    blocks: Incomplete
    initialization_type: Incomplete
    constant: Incomplete
    stationary_cov: Incomplete
    approximate_diffuse_variance: Incomplete
    prefix_initialization_map: Incomplete
    def __init__(self, k_states, initialization_type: Incomplete | None = None, initialization_classes: Incomplete | None = None, approximate_diffuse_variance: float = 1000000.0, constant: Incomplete | None = None, stationary_cov: Incomplete | None = None) -> None: ...
    @classmethod
    def from_components(cls, k_states, a: Incomplete | None = None, Pstar: Incomplete | None = None, Pinf: Incomplete | None = None, A: Incomplete | None = None, R0: Incomplete | None = None, Q0: Incomplete | None = None):
        """
        Construct initialization object from component matrices

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

        Returns
        -------
        initialization
            Initialization object.

        Notes
        -----
        The matrices `a, Pstar, Pinf, A, R0, Q0` and the process for
        initializing the state space model is as given in Chapter 5 of [1]_.
        For the definitions of these matrices, see equation (5.2) and the
        subsequent discussion there.

        References
        ----------
        .. [*] Durbin, James, and Siem Jan Koopman. 2012.
           Time Series Analysis by State Space Methods: Second Edition.
           Oxford University Press.
        """
    @classmethod
    def from_results(cls, filter_results): ...
    def __setitem__(self, index, initialization_type) -> None: ...
    def set(self, index, initialization_type, constant: Incomplete | None = None, stationary_cov: Incomplete | None = None, approximate_diffuse_variance: Incomplete | None = None) -> None:
        """
        Set initialization for states, either globally or for a block

        Parameters
        ----------
        index : tuple or int or None
            Arguments used to create a `slice` of states. Can be a tuple with
            `(start, stop)` (note that for `slice`, stop is not inclusive), or
            an integer (to select a specific state), or None (to select all the
            states).
        initialization_type : str
            The type of initialization used for the states selected by `index`.
            Must be one of 'known', 'diffuse', 'approximate_diffuse', or
            'stationary'.
        constant : array_like, optional
            A vector of constant values, denoted :math:`a`. Most often used
            with 'known' initialization, but may also be used with
            'approximate_diffuse' (although it will then likely have little
            effect).
        stationary_cov : array_like, optional
            The covariance matrix of the stationary part, denoted :math:`Q_0`.
            Only used with 'known' initialization.
        approximate_diffuse_variance : float, optional
            The approximate diffuse variance, denoted :math:`\\kappa`. Only
            applicable with 'approximate_diffuse' initialization. Default is
            1e6.
        """
    def unset(self, index) -> None:
        """
        Unset initialization for states, either globally or for a block

        Parameters
        ----------
        index : tuple or int or None
            Arguments used to create a `slice` of states. Can be a tuple with
            `(start, stop)` (note that for `slice`, stop is not inclusive), or
            an integer (to select a specific state), or None (to select all the
            states).

        Notes
        -----
        Note that this specifically unsets initializations previously created
        using `set` with this same index. Thus you cannot use `index=None` to
        unset all initializations, but only to unset a previously set global
        initialization. To unset all initializations (including both global and
        block level), use the `clear` method.
        """
    def clear(self) -> None:
        """
        Clear all previously set initializations, either global or block level
        """
    @property
    def initialized(self): ...
    def __call__(self, index: Incomplete | None = None, model: Incomplete | None = None, initial_state_mean: Incomplete | None = None, initial_diffuse_state_cov: Incomplete | None = None, initial_stationary_state_cov: Incomplete | None = None, complex_step: bool = False):
        """
        Construct initialization representation

        Parameters
        ----------
        model : Representation, optional
            A state space model representation object, optional if 'stationary'
            initialization is used and ignored otherwise. See notes for
            details in the stationary initialization case.
        model_index : ndarray, optional
            The base index of the block in the model.
        initial_state_mean : ndarray, optional
            An array (or more usually view) in which to place the initial state
            mean.
        initial_diffuse_state_cov : ndarray, optional
            An array (or more usually view) in which to place the diffuse
            component of initial state covariance matrix.
        initial_stationary_state_cov : ndarray, optional
            An array (or more usually view) in which to place the stationary
            component of initial state covariance matrix.


        Returns
        -------
        initial_state_mean : ndarray
            Initial state mean, :math:`a_1^{(0)} = a`
        initial_diffuse_state_cov : ndarray
            Diffuse component of initial state covariance matrix,
            :math:`P_\\infty = A A'`
        initial_stationary_state_cov : ndarray
            Stationary component of initial state covariance matrix,
            :math:`P_* = R_0 Q_0 R_0'`

        Notes
        -----
        If stationary initialization is used either globally or for any block
        of states, then either `model` or all of `state_intercept`,
        `transition`, `selection`, and `state_cov` must be provided.
        """
