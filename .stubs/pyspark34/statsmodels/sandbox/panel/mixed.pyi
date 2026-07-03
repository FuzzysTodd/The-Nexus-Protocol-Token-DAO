from _typeshed import Incomplete
from statsmodels.base.model import LikelihoodModelResults as LikelihoodModelResults
from statsmodels.tools.decorators import cache_readonly as cache_readonly

class Unit:
    """
    Individual experimental unit for
    EM implementation of (repeated measures)
    mixed effects model.

    'Maximum Likelihood Computations with Repeated Measures:
    Application of the EM Algorithm'

    Nan Laird; Nicholas Lange; Daniel Stram

    Journal of the American Statistical Association,
    Vol. 82, No. 397. (Mar., 1987), pp. 97-105.


    Parameters
    ----------
    endog : ndarray, (nobs,)
        response, endogenous variable
    exog_fe : ndarray, (nobs, k_vars_fe)
        explanatory variables as regressors or fixed effects,
        should include exog_re to correct mean of random
        coefficients, see Notes
    exog_re : ndarray, (nobs, k_vars_re)
        explanatory variables or random effects or coefficients

    Notes
    -----
    If the exog_re variables are not included in exog_fe, then the
    mean of the random constants or coefficients are not centered.
    The covariance matrix of the random parameter estimates are not
    centered in this case. (That's how it looks to me. JP)
    """
    Y: Incomplete
    X: Incomplete
    Z: Incomplete
    n: Incomplete
    def __init__(self, endog, exog_fe, exog_re) -> None: ...
    P: Incomplete
    def compute_P(self, Sinv) -> None:
        """projection matrix (nobs_i, nobs_i) (M in regression ?)  (JP check, guessing)
        Display (3.10) from Laird, Lange, Stram (see help(Unit))

        W - W X Sinv X' W'
        """
    def fit(self, a, D, sigma) -> None:
        """
        Compute unit specific parameters in
        Laird, Lange, Stram (see help(Unit)).

        Displays (3.2)-(3.5).
        """
    def compute_xtwy(self):
        """
        Utility function to compute X^tWY (transposed ?) for Unit instance.
        """
    def compute_xtwx(self):
        """
        Utility function to compute X^tWX for Unit instance.
        """
    def cov_random(self, D, Sinv: Incomplete | None = None):
        """
        Approximate covariance of estimates of random effects. Just after
        Display (3.10) in Laird, Lange, Stram (see help(Unit)).

        D - D' Z' P Z D

        Notes
        -----
        In example where the mean of the random coefficient is not zero, this
        is not a covariance but a non-centered moment. (proof by example)
        """
    def logL(self, a, ML: bool = False):
        """
        Individual contributions to the log-likelihood, tries to return REML
        contribution by default though this requires estimated
        fixed effect a to be passed as an argument.

        no constant with pi included

        a is not used if ML=true  (should be a=None in signature)
        If ML is false, then the residuals are calculated for the given fixed
        effects parameters a.
        """
    def deviance(self, ML: bool = False):
        """deviance defined as 2 times the negative loglikelihood

        """

class OneWayMixed:
    """
    Model for
    EM implementation of (repeated measures)
    mixed effects model.

    'Maximum Likelihood Computations with Repeated Measures:
    Application of the EM Algorithm'

    Nan Laird; Nicholas Lange; Daniel Stram

    Journal of the American Statistical Association,
    Vol. 82, No. 397. (Mar., 1987), pp. 97-105.


    Parameters
    ----------
    units : list of units
       the data for the individual units should be attached to the units
    response, fixed and random : formula expression, called as argument to Formula


    *available results and alias*

    (subject to renaming, and coversion to cached attributes)

    params() -> self.a : coefficient for fixed effects or exog
    cov_params() -> self.Sinv : covariance estimate of fixed effects/exog
    bse() : standard deviation of params

    cov_random -> self.D : estimate of random effects covariance
    params_random_units -> [self.units[...].b] : random coefficient for each unit


    *attributes*

    (others)

    self.m : number of units
    self.p : k_vars_fixed
    self.q : k_vars_random
    self.N : nobs (total)


    Notes
    -----
    Fit returns a result instance, but not all results that use the inherited
    methods have been checked.

    Parameters need to change: drop formula and we require a naming convention for
    the units (currently Y,X,Z). - endog, exog_fe, endog_re ?

    logL does not include constant, e.g. sqrt(pi)
    llf is for MLE not for REML


    convergence criteria for iteration
    Currently convergence in the iterative solver is reached if either the loglikelihood
    *or* the fixed effects parameter do not change above tolerance.

    In some examples, the fixed effects parameters converged to 1e-5 within 150 iterations
    while the log likelihood did not converge within 2000 iterations. This might be
    the case if the fixed effects parameters are well estimated, but there are still
    changes in the random effects. If params_rtol and params_atol are set at a higher
    level, then the random effects might not be estimated to a very high precision.

    The above was with a misspecified model, without a constant. With a
    correctly specified model convergence is fast, within a few iterations
    (6 in example).
    """
    units: Incomplete
    m: Incomplete
    n_units: Incomplete
    N: Incomplete
    nobs: Incomplete
    p: Incomplete
    k_exog_fe: Incomplete
    a: Incomplete
    q: Incomplete
    k_exog_re: Incomplete
    D: Incomplete
    sigma: float
    dev: Incomplete
    def __init__(self, units) -> None: ...
    def cov_fixed(self):
        """
        Approximate covariance of estimates of fixed effects.

        Just after Display (3.10) in Laird, Lange, Stram (see help(Mixed)).
        """
    def cov_random(self):
        """
        Estimate random effects covariance D.

        If ML is True, return the ML estimate of sigma, else return the REML estimate.

        see _compute_D, alias for self.D
        """
    @property
    def params(self):
        """
        estimated coefficients for exogeneous variables or fixed effects

        see _compute_a, alias for self.a
        """
    @property
    def params_random_units(self):
        """random coefficients for each unit

        """
    def cov_params(self):
        """
        estimated covariance for coefficients for exogeneous variables or fixed effects

        see cov_fixed, and Sinv in _compute_a
        """
    @property
    def bse(self):
        """
        standard errors of estimated coefficients for exogeneous variables (fixed)

        """
    def deviance(self, ML: bool = False):
        """deviance defined as 2 times the negative loglikelihood

        """
    def logL(self, ML: bool = False):
        """
        Return log-likelihood, REML by default.
        """
    df_resid: Incomplete
    def initialize(self) -> None: ...
    termination: str
    def cont(self, ML: bool = False, rtol: float = 1e-05, params_rtol: float = 1e-05, params_atol: float = 0.0001):
        """convergence check for iterative estimation

        """
    history: Incomplete
    iterations: Incomplete
    def fit(self, maxiter: int = 100, ML: bool = False, rtol: float = 1e-05, params_rtol: float = 1e-06, params_atol: float = 1e-06): ...

class OneWayMixedResults(LikelihoodModelResults):
    """Results class for OneWayMixed models

    """
    model: Incomplete
    params: Incomplete
    def __init__(self, model) -> None: ...
    def llf(self): ...
    @property
    def params_random_units(self): ...
    def cov_random(self): ...
    def mean_random(self, idx: str = 'lastexog'): ...
    def std_random(self): ...
    def plot_random_univariate(self, bins: Incomplete | None = None, use_loc: bool = True):
        """create plot of marginal distribution of random effects

        Parameters
        ----------
        bins : int or bin edges
            option for bins in matplotlibs hist method. Current default is not
            very sophisticated. All distributions use the same setting for
            bins.
        use_loc : bool
            If True, then the distribution with mean given by the fixed
            effect is used.

        Returns
        -------
        Figure
            figure with subplots

        Notes
        -----
        What can make this fancier?

        Bin edges will not make sense if loc or scale differ across random
        effect distributions.

        """
    def plot_scatter_pairs(self, idx1, idx2, title: Incomplete | None = None, ax: Incomplete | None = None):
        """create scatter plot of two random effects

        Parameters
        ----------
        idx1, idx2 : int
            indices of the two random effects to display, corresponding to
            columns of exog_re
        title : None or string
            If None, then a default title is added
        ax : None or matplotlib axis instance
            If None, then a figure with one axis is created and returned.
            If ax is not None, then the scatter plot is created on it, and
            this axis instance is returned.

        Returns
        -------
        ax_or_fig : axis or figure instance
            see ax parameter

        Notes
        -----
        Still needs ellipse from estimated parameters

        """
    def plot_scatter_all_pairs(self, title: Incomplete | None = None): ...
