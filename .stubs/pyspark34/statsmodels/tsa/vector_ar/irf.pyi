from _typeshed import Incomplete
from statsmodels.tools.decorators import cache_readonly as cache_readonly

mat: Incomplete

class BaseIRAnalysis:
    """
    Base class for plotting and computing IRF-related statistics, want to be
    able to handle known and estimated processes
    """
    model: Incomplete
    periods: Incomplete
    order: Incomplete
    P: Incomplete
    svar: Incomplete
    irfs: Incomplete
    svar_irfs: Incomplete
    orth_irfs: Incomplete
    cum_effects: Incomplete
    svar_cum_effects: Incomplete
    orth_cum_effects: Incomplete
    lr_effects: Incomplete
    svar_lr_effects: Incomplete
    orth_lr_effects: Incomplete
    def __init__(self, model, P: Incomplete | None = None, periods: int = 10, order: Incomplete | None = None, svar: bool = False, vecm: bool = False) -> None: ...
    def cov(self, *args, **kwargs) -> None: ...
    def cum_effect_cov(self, *args, **kwargs) -> None: ...
    def plot(self, orth: bool = False, *, impulse: Incomplete | None = None, response: Incomplete | None = None, signif: float = 0.05, plot_params: Incomplete | None = None, figsize=(10, 10), subplot_params: Incomplete | None = None, plot_stderr: bool = True, stderr_type: str = 'asym', repl: int = 1000, seed: Incomplete | None = None, component: Incomplete | None = None):
        """
        Plot impulse responses

        Parameters
        ----------
        orth : bool, default False
            Compute orthogonalized impulse responses
        impulse : {str, int}
            variable providing the impulse
        response : {str, int}
            variable affected by the impulse
        signif : float (0 < signif < 1)
            Significance level for error bars, defaults to 95% CI
        subplot_params : dict
            To pass to subplot plotting funcions. Example: if fonts are too big,
            pass {'fontsize' : 8} or some number to your taste.
        plot_params : dict

        figsize : (float, float), default (10, 10)
            Figure size (width, height in inches)
        plot_stderr : bool, default True
            Plot standard impulse response error bands
        stderr_type : str
            'asym': default, computes asymptotic standard errors
            'mc': monte carlo standard errors (use rpl)
        repl : int, default 1000
            Number of replications for Monte Carlo and Sims-Zha standard errors
        seed : int
            np.random.seed for Monte Carlo replications
        component: array or vector of principal component indices
        """
    def plot_cum_effects(self, orth: bool = False, *, impulse: Incomplete | None = None, response: Incomplete | None = None, signif: float = 0.05, plot_params: Incomplete | None = None, figsize=(10, 10), subplot_params: Incomplete | None = None, plot_stderr: bool = True, stderr_type: str = 'asym', repl: int = 1000, seed: Incomplete | None = None):
        """
        Plot cumulative impulse response functions

        Parameters
        ----------
        orth : bool, default False
            Compute orthogonalized impulse responses
        impulse : {str, int}
            variable providing the impulse
        response : {str, int}
            variable affected by the impulse
        signif : float (0 < signif < 1)
            Significance level for error bars, defaults to 95% CI
        subplot_params : dict
            To pass to subplot plotting funcions. Example: if fonts are too big,
            pass {'fontsize' : 8} or some number to your taste.
        plot_params : dict

        figsize: (float, float), default (10, 10)
            Figure size (width, height in inches)
        plot_stderr : bool, default True
            Plot standard impulse response error bands
        stderr_type : str
            'asym': default, computes asymptotic standard errors
            'mc': monte carlo standard errors (use rpl)
        repl : int, default 1000
            Number of replications for monte carlo standard errors
        seed : int
            np.random.seed for Monte Carlo replications
        """

class IRAnalysis(BaseIRAnalysis):
    """
    Impulse response analysis class. Computes impulse responses, asymptotic
    standard errors, and produces relevant plots

    Parameters
    ----------
    model : VAR instance

    Notes
    -----
    Using Lütkepohl (2005) notation
    """
    cov_a: Incomplete
    cov_sig: Incomplete
    def __init__(self, model, P: Incomplete | None = None, periods: int = 10, order: Incomplete | None = None, svar: bool = False, vecm: bool = False) -> None: ...
    def cov(self, orth: bool = False):
        """
        Compute asymptotic standard errors for impulse response coefficients

        Notes
        -----
        Lütkepohl eq 3.7.5

        Returns
        -------
        """
    def errband_mc(self, orth: bool = False, svar: bool = False, repl: int = 1000, signif: float = 0.05, seed: Incomplete | None = None, burn: int = 100):
        """
        IRF Monte Carlo integrated error bands
        """
    def err_band_sz1(self, orth: bool = False, svar: bool = False, repl: int = 1000, signif: float = 0.05, seed: Incomplete | None = None, burn: int = 100, component: Incomplete | None = None):
        '''
        IRF Sims-Zha error band method 1. Assumes symmetric error bands around
        mean.

        Parameters
        ----------
        orth : bool, default False
            Compute orthogonalized impulse responses
        repl : int, default 1000
            Number of MC replications
        signif : float (0 < signif < 1)
            Significance level for error bars, defaults to 95% CI
        seed : int, default None
            np.random seed
        burn : int, default 100
            Number of initial simulated obs to discard
        component : neqs x neqs array, default to largest for each
            Index of column of eigenvector/value to use for each error band
            Note: period of impulse (t=0) is not included when computing
            principle component

        References
        ----------
        Sims, Christopher A., and Tao Zha. 1999. "Error Bands for Impulse
        Response". Econometrica 67: 1113-1155.
        '''
    def err_band_sz2(self, orth: bool = False, svar: bool = False, repl: int = 1000, signif: float = 0.05, seed: Incomplete | None = None, burn: int = 100, component: Incomplete | None = None):
        '''
        IRF Sims-Zha error band method 2.

        This method Does not assume symmetric error bands around mean.

        Parameters
        ----------
        orth : bool, default False
            Compute orthogonalized impulse responses
        repl : int, default 1000
            Number of MC replications
        signif : float (0 < signif < 1)
            Significance level for error bars, defaults to 95% CI
        seed : int, default None
            np.random seed
        burn : int, default 100
            Number of initial simulated obs to discard
        component : neqs x neqs array, default to largest for each
            Index of column of eigenvector/value to use for each error band
            Note: period of impulse (t=0) is not included when computing
            principle component

        References
        ----------
        Sims, Christopher A., and Tao Zha. 1999. "Error Bands for Impulse
        Response". Econometrica 67: 1113-1155.
        '''
    def err_band_sz3(self, orth: bool = False, svar: bool = False, repl: int = 1000, signif: float = 0.05, seed: Incomplete | None = None, burn: int = 100, component: Incomplete | None = None):
        '''
        IRF Sims-Zha error band method 3. Does not assume symmetric error bands around mean.

        Parameters
        ----------
        orth : bool, default False
            Compute orthogonalized impulse responses
        repl : int, default 1000
            Number of MC replications
        signif : float (0 < signif < 1)
            Significance level for error bars, defaults to 95% CI
        seed : int, default None
            np.random seed
        burn : int, default 100
            Number of initial simulated obs to discard
        component : vector length neqs, default to largest for each
            Index of column of eigenvector/value to use for each error band
            Note: period of impulse (t=0) is not included when computing
            principle component

        References
        ----------
        Sims, Christopher A., and Tao Zha. 1999. "Error Bands for Impulse
        Response". Econometrica 67: 1113-1155.
        '''
    def G(self): ...
    def cum_effect_cov(self, orth: bool = False):
        """
        Compute asymptotic standard errors for cumulative impulse response
        coefficients

        Parameters
        ----------
        orth : bool

        Notes
        -----
        eq. 3.7.7 (non-orth), 3.7.10 (orth)

        Returns
        -------
        """
    def cum_errband_mc(self, orth: bool = False, repl: int = 1000, signif: float = 0.05, seed: Incomplete | None = None, burn: int = 100):
        """
        IRF Monte Carlo integrated error bands of cumulative effect
        """
    def lr_effect_cov(self, orth: bool = False):
        """
        Returns
        -------
        """
    def stderr(self, orth: bool = False): ...
    def cum_effect_stderr(self, orth: bool = False): ...
    def lr_effect_stderr(self, orth: bool = False): ...
    def H(self): ...
    def fevd_table(self) -> None: ...
