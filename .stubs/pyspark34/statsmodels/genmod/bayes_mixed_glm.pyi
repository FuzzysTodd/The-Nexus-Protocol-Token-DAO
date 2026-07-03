import statsmodels.base.model as base
from _typeshed import Incomplete
from statsmodels.genmod import families as families
from statsmodels.iolib import summary2 as summary2

glw: Incomplete

class _BayesMixedGLM(base.Model):
    exog_vc: Incomplete
    exog_vc2: Incomplete
    ident: Incomplete
    family: Incomplete
    k_fep: Incomplete
    k_vc: Incomplete
    k_vcp: Incomplete
    fep_names: Incomplete
    vcp_names: Incomplete
    vc_names: Incomplete
    fe_p: Incomplete
    vcp_p: Incomplete
    names: Incomplete
    def __init__(self, endog, exog, exog_vc: Incomplete | None = None, ident: Incomplete | None = None, family: Incomplete | None = None, vcp_p: int = 1, fe_p: int = 2, fep_names: Incomplete | None = None, vcp_names: Incomplete | None = None, vc_names: Incomplete | None = None, **kwargs) -> None: ...
    def logposterior(self, params):
        """
        The overall log-density: log p(y, fe, vc, vcp).

        This differs by an additive constant from the log posterior
        log p(fe, vc, vcp | y).
        """
    def logposterior_grad(self, params):
        """
        The gradient of the log posterior.
        """
    @classmethod
    def from_formula(cls, formula, vc_formulas, data, family: Incomplete | None = None, vcp_p: int = 1, fe_p: int = 2):
        """
        Fit a BayesMixedGLM using a formula.

        Parameters
        ----------
        formula : str
            Formula for the endog and fixed effects terms (use ~ to
            separate dependent and independent expressions).
        vc_formulas : dictionary
            vc_formulas[name] is a one-sided formula that creates one
            collection of random effects with a common variance
            parameter.  If using categorical (factor) variables to
            produce variance components, note that generally `0 + ...`
            should be used so that an intercept is not included.
        data : data frame
            The data to which the formulas are applied.
        family : genmod.families instance
            A GLM family.
        vcp_p : float
            The prior standard deviation for the logarithms of the standard
            deviations of the random effects.
        fe_p : float
            The prior standard deviation for the fixed effects parameters.
        """
    def fit(self, method: str = 'BFGS', minim_opts: Incomplete | None = None) -> None:
        """
        fit is equivalent to fit_map.

        See fit_map for parameter information.

        Use `fit_vb` to fit the model using variational Bayes.
        """
    exog: Incomplete
    def fit_map(self, method: str = 'BFGS', minim_opts: Incomplete | None = None, scale_fe: bool = False):
        """
        Construct the Laplace approximation to the posterior distribution.

        Parameters
        ----------
        method : str
            Optimization method for finding the posterior mode.
        minim_opts : dict
            Options passed to scipy.minimize.
        scale_fe : bool
            If True, the columns of the fixed effects design matrix
            are centered and scaled to unit variance before fitting
            the model.  The results are back-transformed so that the
            results are presented on the original scale.

        Returns
        -------
        BayesMixedGLMResults instance.
        """
    def predict(self, params, exog: Incomplete | None = None, linear: bool = False):
        """
        Return the fitted mean structure.

        Parameters
        ----------
        params : array_like
            The parameter vector, may be the full parameter vector, or may
            be truncated to include only the mean parameters.
        exog : array_like
            The design matrix for the mean structure.  If omitted, use the
            model's design matrix.
        linear : bool
            If True, return the linear predictor without passing through the
            link function.

        Returns
        -------
        A 1-dimensional array of predicted values
        """

class _VariationalBayesMixedGLM:
    """
    A mixin providing generic (not family-specific) methods for
    variational Bayes mean field fitting.
    """
    rng: int
    verbose: bool
    def vb_elbo_base(self, h, tm, fep_mean, vcp_mean, vc_mean, fep_sd, vcp_sd, vc_sd):
        """
        Returns the evidence lower bound (ELBO) for the model.

        This function calculates the family-specific ELBO function
        based on information provided from a subclass.

        Parameters
        ----------
        h : function mapping 1d vector to 1d vector
            The contribution of the model to the ELBO function can be
            expressed as y_i*lp_i + Eh_i(z), where y_i and lp_i are
            the response and linear predictor for observation i, and z
            is a standard normal random variable.  This formulation
            can be achieved for any GLM with a canonical link
            function.
        """
    def vb_elbo_grad_base(self, h, tm, tv, fep_mean, vcp_mean, vc_mean, fep_sd, vcp_sd, vc_sd):
        """
        Return the gradient of the ELBO function.

        See vb_elbo_base for parameters.
        """
    exog: Incomplete
    def fit_vb(self, mean: Incomplete | None = None, sd: Incomplete | None = None, fit_method: str = 'BFGS', minim_opts: Incomplete | None = None, scale_fe: bool = False, verbose: bool = False):
        """
        Fit a model using the variational Bayes mean field approximation.

        Parameters
        ----------
        mean : array_like
            Starting value for VB mean vector
        sd : array_like
            Starting value for VB standard deviation vector
        fit_method : str
            Algorithm for scipy.minimize
        minim_opts : dict
            Options passed to scipy.minimize
        scale_fe : bool
            If true, the columns of the fixed effects design matrix
            are centered and scaled to unit variance before fitting
            the model.  The results are back-transformed so that the
            results are presented on the original scale.
        verbose : bool
            If True, print the gradient norm to the screen each time
            it is calculated.

        Notes
        -----
        The goal is to find a factored Gaussian approximation
        q1*q2*...  to the posterior distribution, approximately
        minimizing the KL divergence from the factored approximation
        to the actual posterior.  The KL divergence, or ELBO function
        has the form

            E* log p(y, fe, vcp, vc) - E* log q

        where E* is expectation with respect to the product of qj.

        References
        ----------
        Blei, Kucukelbir, McAuliffe (2017).  Variational Inference: A
        review for Statisticians
        https://arxiv.org/pdf/1601.00670.pdf
        """

class BayesMixedGLMResults:
    """
    Class to hold results from a Bayesian estimation of a Mixed GLM model.

    Attributes
    ----------
    fe_mean : array_like
        Posterior mean of the fixed effects coefficients.
    fe_sd : array_like
        Posterior standard deviation of the fixed effects coefficients
    vcp_mean : array_like
        Posterior mean of the logged variance component standard
        deviations.
    vcp_sd : array_like
        Posterior standard deviation of the logged variance component
        standard deviations.
    vc_mean : array_like
        Posterior mean of the random coefficients
    vc_sd : array_like
        Posterior standard deviation of the random coefficients
    """
    model: Incomplete
    params: Incomplete
    optim_retvals: Incomplete
    fe_sd: Incomplete
    vcp_sd: Incomplete
    vc_sd: Incomplete
    def __init__(self, model, params, cov_params, optim_retvals: Incomplete | None = None) -> None: ...
    def cov_params(self): ...
    def summary(self): ...
    def random_effects(self, term: Incomplete | None = None):
        """
        Posterior mean and standard deviation of random effects.

        Parameters
        ----------
        term : int or None
            If None, results for all random effects are returned.  If
            an integer, returns results for a given set of random
            effects.  The value of `term` refers to an element of the
            `ident` vector, or to a position in the `vc_formulas`
            list.

        Returns
        -------
        Data frame of posterior means and posterior standard
        deviations of random effects.
        """
    def predict(self, exog: Incomplete | None = None, linear: bool = False):
        """
        Return predicted values for the mean structure.

        Parameters
        ----------
        exog : array_like
            The design matrix for the mean structure.  If None,
            use the model's design matrix.
        linear : bool
            If True, returns the linear predictor, otherwise
            transform the linear predictor using the link function.

        Returns
        -------
        A one-dimensional array of fitted values.
        """

class BinomialBayesMixedGLM(_VariationalBayesMixedGLM, _BayesMixedGLM):
    __doc__: Incomplete
    def __init__(self, endog, exog, exog_vc, ident, vcp_p: int = 1, fe_p: int = 2, fep_names: Incomplete | None = None, vcp_names: Incomplete | None = None, vc_names: Incomplete | None = None) -> None: ...
    @classmethod
    def from_formula(cls, formula, vc_formulas, data, vcp_p: int = 1, fe_p: int = 2): ...
    def vb_elbo(self, vb_mean, vb_sd):
        """
        Returns the evidence lower bound (ELBO) for the model.
        """
    def vb_elbo_grad(self, vb_mean, vb_sd):
        """
        Returns the gradient of the model's evidence lower bound (ELBO).
        """

class PoissonBayesMixedGLM(_VariationalBayesMixedGLM, _BayesMixedGLM):
    __doc__: Incomplete
    def __init__(self, endog, exog, exog_vc, ident, vcp_p: int = 1, fe_p: int = 2, fep_names: Incomplete | None = None, vcp_names: Incomplete | None = None, vc_names: Incomplete | None = None) -> None: ...
    @classmethod
    def from_formula(cls, formula, vc_formulas, data, vcp_p: int = 1, fe_p: int = 2, vcp_names: Incomplete | None = None, vc_names: Incomplete | None = None): ...
    def vb_elbo(self, vb_mean, vb_sd):
        """
        Returns the evidence lower bound (ELBO) for the model.
        """
    def vb_elbo_grad(self, vb_mean, vb_sd):
        """
        Returns the gradient of the model's evidence lower bound (ELBO).
        """
