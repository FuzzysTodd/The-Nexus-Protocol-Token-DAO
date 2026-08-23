from _typeshed import Incomplete
from statsmodels.compat.pandas import Substitution as Substitution
from statsmodels.regression.linear_model import WLS as WLS
from statsmodels.sandbox.regression.gmm import GMM as GMM
from statsmodels.stats.contrast import ContrastResults as ContrastResults
from statsmodels.tools.docstring import indent as indent

def ate_ipw(endog, tind, prob, weighted: bool = True, probt: Incomplete | None = None):
    """average treatment effect based on basic inverse propensity weighting.

    """

class _TEGMMGeneric1(GMM):
    """GMM class to get cov_params for treatment effects

    This combines moment conditions for the selection/treatment model and the
    outcome model to get the standard errors for the treatment effect that
    takes the first step estimation of the treatment model into account.

    this also matches standard errors of ATE and POM in Stata

    """
    results_select: Incomplete
    mom_outcome: Incomplete
    exclude_tmoms: Incomplete
    k_select: int
    prob: Incomplete
    def __init__(self, endog, res_select, mom_outcome, exclude_tmoms: bool = False, **kwargs) -> None: ...
    def momcond(self, params): ...

class _TEGMM(GMM):
    """GMM class to get cov_params for treatment effects

    This combines moment conditions for the selection/treatment model and the
    outcome model to get the standard errors for the treatment effect that
    takes the first step estimation of the treatment model into account.

    this also matches standard errors of ATE and POM in Stata

    """
    results_select: Incomplete
    mom_outcome: Incomplete
    def __init__(self, endog, res_select, mom_outcome) -> None: ...
    def momcond(self, params): ...

class _IPWGMM(_TEGMMGeneric1):
    """ GMM for aipw treatment effect and potential outcome

    uses unweighted outcome regression
    """
    def momcond(self, params): ...

class _AIPWGMM(_TEGMMGeneric1):
    """ GMM for aipw treatment effect and potential outcome

    uses unweighted outcome regression
    """
    def momcond(self, params): ...

class _AIPWWLSGMM(_TEGMMGeneric1):
    """ GMM for aipw-wls treatment effect and potential outcome

    uses weighted outcome regression
    """
    def momcond(self, params): ...

class _RAGMM(_TEGMMGeneric1):
    """GMM for regression adjustment treatment effect and potential outcome

    uses unweighted outcome regression
    """
    def momcond(self, params): ...

class _IPWRAGMM(_TEGMMGeneric1):
    """ GMM for ipwra treatment effect and potential outcome
    """
    def momcond(self, params): ...

class TreatmentEffectResults(ContrastResults):
    """
    Results class for treatment effect estimation

    Parameters
    ----------
    teff : instance of TreatmentEffect class
    results_gmm : instance of GMMResults class
    method : string
        Method and estimator of treatment effect.
    kwds: dict
        Other keywords with additional information.

    Notes
    -----
    This class is a subclass of ContrastResults and inherits methods like
    summary, summary_frame and conf_int. Attributes correspond to a z-test
    given by ``GMMResults.t_test``.
    """
    teff: Incomplete
    results_gmm: Incomplete
    method: Incomplete
    c_names: Incomplete
    def __init__(self, teff, results_gmm, method, **kwds) -> None: ...

doc_params_returns: str
doc_params_returns2: str

class TreatmentEffect:
    '''
    Estimate average treatment effect under conditional independence

    .. versionadded:: 0.14.0

    This class estimates treatment effect and potential outcome using 5
    different methods, ipw, ra, aipw, aipw-wls, ipw-ra.
    Standard errors and inference are based on the joint GMM representation of
    selection or treatment model, outcome model and effect functions.

    Parameters
    ----------
    model : instance of a model class
        The model class should contain endog and exog for the outcome model.
    treatment : ndarray
        indicator array for observations with treatment (1) or without (0)
    results_select : results instance
        The results instance for the treatment or selection model.
    _cov_type : "HC0"
        Internal keyword. The keyword oes not affect GMMResults which always
        corresponds to HC0 standard errors.
    kwds : keyword arguments
        currently not used

    Notes
    -----
    The outcome model is currently limited to a linear model based on OLS.
    Other outcome models, like Logit and Poisson, will become available in
    future.

    See `Treatment Effect notebook
    <../examples/notebooks/generated/treatment_effect.html>`__
    for an overview.

    '''
    treatment: Incomplete
    treat_mask: Incomplete
    results_select: Incomplete
    prob_select: Incomplete
    model_pool: Incomplete
    nobs: Incomplete
    results0: Incomplete
    results1: Incomplete
    exog_grouped: Incomplete
    endog_grouped: Incomplete
    def __init__(self, model, treatment, results_select: Incomplete | None = None, _cov_type: str = 'HC0', **kwds) -> None: ...
    @classmethod
    def from_data(cls, endog, exog, treatment, model: str = 'ols', **kwds) -> None:
        """create models from data

        not yet implemented

        """
    def ipw(self, return_results: bool = True, effect_group: str = 'all', disp: bool = False):
        '''Inverse Probability Weighted treatment effect estimation.

        Parameters
        ----------
        return_results : bool
            If True, then a results instance is returned.
            If False, just ATE, POM0 and POM1 are returned.
        effect_group : {"all", 0, 1}
            ``effectgroup`` determines for which population the effects are
            estimated.
            If effect_group is "all", then sample average treatment effect and
            potential outcomes are returned.
            If effect_group is 1 or "treated", then effects on treated are
            returned.
            If effect_group is 0, "treated" or "control", then effects on
            untreated, i.e. control group, are returned.
        disp : bool
            Indicates whether the scipy optimizer should display the
            optimization results

        Returns
        -------
        TreatmentEffectsResults instance or tuple (ATE, POM0, POM1)

        See Also
        --------
        TreatmentEffectsResults
        '''
    def ra(self, return_results: bool = True, effect_group: str = 'all', disp: bool = False):
        """
        Regression Adjustment treatment effect estimation.
        
%(params_returns)s
        See Also
        --------
        TreatmentEffectsResults
        """
    def aipw(self, return_results: bool = True, disp: bool = False):
        """
        ATE and POM from double robust augmented inverse probability weighting
        
%(params_returns)s
        See Also
        --------
        TreatmentEffectsResults

        """
    results_ipwwls0: Incomplete
    results_ipwwls1: Incomplete
    def aipw_wls(self, return_results: bool = True, disp: bool = False):
        """
        ATE and POM from double robust augmented inverse probability weighting.

        This uses weighted outcome regression, while `aipw` uses unweighted
        outcome regression.
        Option for effect on treated or on untreated is not available.
        
%(params_returns)s
        See Also
        --------
        TreatmentEffectsResults

        """
    def ipw_ra(self, return_results: bool = True, effect_group: str = 'all', disp: bool = False):
        """
        ATE and POM from inverse probability weighted regression adjustment.

        
%(params_returns)s
        See Also
        --------
        TreatmentEffectsResults

        """
