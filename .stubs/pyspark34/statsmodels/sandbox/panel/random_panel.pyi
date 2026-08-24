from _typeshed import Incomplete

class PanelSample:
    """data generating process for panel with within correlation

    allows various within correlation structures, but no random intercept yet

    Parameters
    ----------
    nobs : int
        total number of observations
    k_vars : int
        number of explanatory variables to create in exog, including constant
    n_groups int
        number of groups in balanced sample
    exog : None or ndarray
        default is None, in which case a exog is created
    within : bool
        If True (default), then the exog vary within a group. If False, then
        only variation across groups is used.
        TODO: this option needs more work
    corr_structure : ndarray or ??
        Default is np.eye.
    corr_args : tuple
        arguments for the corr_structure
    scale : float
        scale of noise, standard deviation of normal distribution
    seed : None or int
        If seed is given, then this is used to create the random numbers for
        the sample.

    Notes
    -----
    The behavior for panel robust covariance estimators seems to differ by
    a large amount by whether exog have mostly within group or across group
    variation. I do not understand why this should be the case from the theory,
    and this would warrant more investigation.

    This is just used in one example so far and needs more usage to see what
    will be useful to add.

    """
    nobs: Incomplete
    nobs_i: Incomplete
    n_groups: Incomplete
    k_vars: Incomplete
    corr_structure: Incomplete
    groups: Incomplete
    group_indices: Incomplete
    exog: Incomplete
    y_true: Incomplete
    beta: Incomplete
    seed: Incomplete
    random_state: Incomplete
    std: Incomplete
    cov: Incomplete
    group_means: Incomplete
    def __init__(self, nobs, k_vars, n_groups, exog: Incomplete | None = None, within: bool = True, corr_structure=..., corr_args=(), scale: int = 1, seed: Incomplete | None = None) -> None: ...
    def get_y_true(self) -> None: ...
    def generate_panel(self):
        """
        generate endog for a random panel dataset with within correlation

        """
