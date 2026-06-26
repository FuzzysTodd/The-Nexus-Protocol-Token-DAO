from _typeshed import Incomplete
from statsmodels.compat.scipy import SP_LT_17 as SP_LT_17
from statsmodels.tools.sm_exceptions import ValueWarning as ValueWarning

FLOAT_EPS: Incomplete

class Family:
    """
    The parent class for one-parameter exponential families.

    Parameters
    ----------
    link : a link function instance
        Link is the linear transformation function.
        See the individual families for available links.
    variance : a variance function
        Measures the variance as a function of the mean probabilities.
        See the individual families for the default variance function.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    See Also
    --------
    :ref:`links` : Further details on links.
    """
    valid: Incomplete
    links: Incomplete
    link: Incomplete
    variance: Incomplete
    def __init__(self, link, variance, check_link: bool = True) -> None: ...
    def starting_mu(self, y):
        """
        Starting value for mu in the IRLS algorithm.

        Parameters
        ----------
        y : ndarray
            The untransformed response variable.

        Returns
        -------
        mu_0 : ndarray
            The first guess on the transformed response variable.

        Notes
        -----
        .. math::

           \\mu_0 = (Y + \\overline{Y})/2

        Only the Binomial family takes a different initial value.
        """
    def weights(self, mu):
        """
        Weights for IRLS steps

        Parameters
        ----------
        mu : array_like
            The transformed mean response variable in the exponential family

        Returns
        -------
        w : ndarray
            The weights for the IRLS steps

        Notes
        -----
        .. math::

           w = 1 / (g'(\\mu)^2  * Var(\\mu))
        """
    def deviance(self, endog, mu, var_weights: float = 1.0, freq_weights: float = 1.0, scale: float = 1.0):
        """
        The deviance function evaluated at (endog, mu, var_weights,
        freq_weights, scale) for the distribution.

        Deviance is usually defined as twice the loglikelihood ratio.

        Parameters
        ----------
        endog : array_like
            The endogenous response variable
        mu : array_like
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        freq_weights : array_like
            1d array of frequency weights. The default is 1.
        scale : float, optional
            An optional scale argument. The default is 1.

        Returns
        -------
        Deviance : ndarray
            The value of deviance function defined below.

        Notes
        -----
        Deviance is defined

        .. math::

           D = 2\\sum_i (freq\\_weights_i * var\\_weights *
           (llf(endog_i, endog_i) - llf(endog_i, \\mu_i)))

        where y is the endogenous variable. The deviance functions are
        analytically defined for each family.

        Internally, we calculate deviance as:

        .. math::
           D = \\sum_i freq\\_weights_i * var\\_weights * resid\\_dev_i  / scale
        """
    def resid_dev(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The deviance residuals

        Parameters
        ----------
        endog : array_like
            The endogenous response variable
        mu : array_like
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional scale argument. The default is 1.

        Returns
        -------
        resid_dev : float
            Deviance residuals as defined below.

        Notes
        -----
        The deviance residuals are defined by the contribution D_i of
        observation i to the deviance as

        .. math::
           resid\\_dev_i = sign(y_i-\\mu_i) \\sqrt{D_i}

        D_i is calculated from the _resid_dev method in each family.
        Distribution-specific documentation of the calculation is available
        there.
        """
    def fitted(self, lin_pred):
        """
        Fitted values based on linear predictors lin_pred.

        Parameters
        ----------
        lin_pred : ndarray
            Values of the linear predictor of the model.
            :math:`X \\cdot \\beta` in a classical linear model.

        Returns
        -------
        mu : ndarray
            The mean response variables given by the inverse of the link
            function.
        """
    def predict(self, mu):
        """
        Linear predictors based on given mu values.

        Parameters
        ----------
        mu : ndarray
            The mean response variables

        Returns
        -------
        lin_pred : ndarray
            Linear predictors based on the mean response variables.  The value
            of the link function at the given mu.
        """
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0) -> None:
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        This is defined for each family. endog and mu are not restricted to
        ``endog`` and ``mu`` respectively.  For instance, you could call
        both ``loglike(endog, endog)`` and ``loglike(endog, mu)`` to get the
        log-likelihood ratio.
        """
    def loglike(self, endog, mu, var_weights: float = 1.0, freq_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function in terms of the fitted mean response.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        freq_weights : array_like
            1d array of frequency weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, freq_weights, scale) as defined below.

        Notes
        -----
        Where :math:`ll_i` is the by-observation log-likelihood:

        .. math::
           ll = \\sum(ll_i * freq\\_weights_i)

        ``ll_i`` is defined for each family. endog and mu are not restricted
        to ``endog`` and ``mu`` respectively.  For instance, you could call
        both ``loglike(endog, endog)`` and ``loglike(endog, mu)`` to get the
        log-likelihood ratio.
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0) -> None:
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        See Also
        --------
        statsmodels.genmod.families.family.Family : `resid_anscombe` for the
          individual families for more information

        Notes
        -----
        Anscombe residuals are defined by

        .. math::
           resid\\_anscombe_i = \\frac{A(y)-A(\\mu)}{A'(\\mu)\\sqrt{Var[\\mu]}} *
           \\sqrt(var\\_weights)

        where :math:`A'(y)=v(y)^{-\\frac{1}{3}}` and :math:`v(\\mu)` is the
        variance function :math:`Var[y]=\\frac{\\phi}{w}v(mu)`.
        The transformation :math:`A(y)` makes the residuals more normal
        distributed.
        """

class Poisson(Family):
    """
    Poisson exponential family.

    Parameters
    ----------
    link : a link instance, optional
        The default link for the Poisson family is the log link. Available
        links are log, identity, and sqrt. See statsmodels.families.links for
        more information.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    Poisson.link : a link instance
        The link function of the Poisson instance.
    Poisson.variance : varfuncs instance
        ``variance`` is an instance of
        statsmodels.genmod.families.varfuncs.mu

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.
    """
    links: Incomplete
    variance: Incomplete
    valid: Incomplete
    safe_links: Incomplete
    def __init__(self, link: Incomplete | None = None, check_link: bool = True) -> None: ...
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Poisson distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        .. math::
            ll_i = var\\_weights_i / scale * (endog_i * \\ln(\\mu_i) - \\mu_i -
            \\ln \\Gamma(endog_i + 1))
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals for the Poisson family defined below

        Notes
        -----
        .. math::

           resid\\_anscombe_i = (3/2) * (endog_i^{2/3} - \\mu_i^{2/3}) /
           \\mu_i^{1/6} * \\sqrt(var\\_weights)
        """
    def get_distribution(self, mu, scale: float = 1.0, var_weights: float = 1.0):
        """
        Frozen Poisson distribution instance for given parameters

        Parameters
        ----------
        mu : ndarray
            Usually but not always the fitted mean response variable.
        scale : float
            The scale parameter is ignored.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
            var_weights are ignored for Poisson.

        Returns
        -------
        distribution instance

        """

class Gaussian(Family):
    """
    Gaussian exponential family distribution.

    Parameters
    ----------
    link : a link instance, optional
        The default link for the Gaussian family is the identity link.
        Available links are log, identity, and inverse.
        See statsmodels.genmod.families.links for more information.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    Gaussian.link : a link instance
        The link function of the Gaussian instance
    Gaussian.variance : varfunc instance
        ``variance`` is an instance of
        statsmodels.genmod.families.varfuncs.constant

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.
    """
    links: Incomplete
    variance: Incomplete
    safe_links = links
    def __init__(self, link: Incomplete | None = None, check_link: bool = True) -> None: ...
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Gaussian distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        If the link is the identity link function then the
        loglikelihood function is the same as the classical OLS model.

        .. math::

           llf = -nobs / 2 * (\\log(SSR) + (1 + \\log(2 \\pi / nobs)))

        where

        .. math::

           SSR = \\sum_i (Y_i - g^{-1}(\\mu_i))^2

        If the links is not the identity link then the loglikelihood
        function is defined as

        .. math::

           ll_i = -1 / 2 \\sum_i  * var\\_weights * ((Y_i - mu_i)^2 / scale +
                                                \\log(2 * \\pi * scale))
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals for the Gaussian family defined below

        Notes
        -----
        For the Gaussian distribution, Anscombe residuals are the same as
        deviance residuals.

        .. math::

           resid\\_anscombe_i = (Y_i - \\mu_i) / \\sqrt{scale} *
           \\sqrt(var\\_weights)
        """
    def get_distribution(self, mu, scale, var_weights: float = 1.0):
        """
        Frozen Gaussian distribution instance for given parameters

        Parameters
        ----------
        mu : ndarray
            Usually but not always the fitted mean response variable.
        scale : float
            The scale parameter is required argument for get_distribution.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.

        Returns
        -------
        distribution instance

        """

class Gamma(Family):
    """
    Gamma exponential family distribution.

    Parameters
    ----------
    link : a link instance, optional
        The default link for the Gamma family is the inverse link.
        Available links are log, identity, and inverse.
        See statsmodels.genmod.families.links for more information.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    Gamma.link : a link instance
        The link function of the Gamma instance
    Gamma.variance : varfunc instance
        ``variance`` is an instance of
        statsmodels.genmod.family.varfuncs.mu_squared

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.
    """
    links: Incomplete
    variance: Incomplete
    safe_links: Incomplete
    def __init__(self, link: Incomplete | None = None, check_link: bool = True) -> None: ...
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Gamma distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        .. math::

           ll_i = var\\_weights_i / scale * (\\ln(var\\_weights_i * endog_i /
           (scale * \\mu_i)) - (var\\_weights_i * endog_i) /
           (scale * \\mu_i)) - \\ln \\Gamma(var\\_weights_i / scale) - \\ln(\\mu_i)
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals for the Gamma family defined below

        Notes
        -----
        .. math::

           resid\\_anscombe_i = 3 * (endog_i^{1/3} - \\mu_i^{1/3}) / \\mu_i^{1/3}
           / \\sqrt{scale} * \\sqrt(var\\_weights)
        """
    def get_distribution(self, mu, scale, var_weights: float = 1.0):
        """
        Frozen Gamma distribution instance for given parameters

        Parameters
        ----------
        mu : ndarray
            Usually but not always the fitted mean response variable.
        scale : float
            The scale parameter is required argument for get_distribution.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.

        Returns
        -------
        distribution instance

        """

class Binomial(Family):
    """
    Binomial exponential family distribution.

    Parameters
    ----------
    link : a link instance, optional
        The default link for the Binomial family is the logit link.
        Available links are logit, probit, cauchy, log, loglog, and cloglog.
        See statsmodels.genmod.families.links for more information.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    Binomial.link : a link instance
        The link function of the Binomial instance
    Binomial.variance : varfunc instance
        ``variance`` is an instance of
        statsmodels.genmod.families.varfuncs.binary

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.

    Notes
    -----
    endog for Binomial can be specified in one of three ways:
    A 1d array of 0 or 1 values, indicating failure or success
    respectively.
    A 2d array, with two columns. The first column represents the
    success count and the second column represents the failure
    count.
    A 1d array of proportions, indicating the proportion of
    successes, with parameter `var_weights` containing the
    number of trials for each row.
    """
    links: Incomplete
    variance: Incomplete
    safe_links: Incomplete
    n: int
    def __init__(self, link: Incomplete | None = None, check_link: bool = True) -> None: ...
    def starting_mu(self, y):
        """
        The starting values for the IRLS algorithm for the Binomial family.
        A good choice for the binomial family is :math:`\\mu_0 = (Y_i + 0.5)/2`
        """
    def initialize(self, endog, freq_weights):
        """
        Initialize the response variable.

        Parameters
        ----------
        endog : ndarray
            Endogenous response variable
        freq_weights : ndarray
            1d array of frequency weights

        Returns
        -------
        If `endog` is binary, returns `endog`

        If `endog` is a 2d array, then the input is assumed to be in the format
        (successes, failures) and
        successes/(success + failures) is returned.  And n is set to
        successes + failures.
        """
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Binomial distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        If the endogenous variable is binary:

        .. math::

         ll_i = \\sum_i (y_i * \\log(\\mu_i/(1-\\mu_i)) + \\log(1-\\mu_i)) *
               var\\_weights_i

        If the endogenous variable is binomial:

        .. math::

           ll_i = \\sum_i var\\_weights_i * (\\ln \\Gamma(n+1) -
                  \\ln \\Gamma(y_i + 1) - \\ln \\Gamma(n_i - y_i +1) + y_i *
                  \\log(\\mu_i / (n_i - \\mu_i)) + n * \\log(1 - \\mu_i/n_i))

        where :math:`y_i = Y_i * n_i` with :math:`Y_i` and :math:`n_i` as
        defined in Binomial initialize.  This simply makes :math:`y_i` the
        original number of successes.
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        '''
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals as defined below.

        Notes
        -----
        .. math::

            n^{2/3}*(cox\\_snell(endog)-cox\\_snell(mu)) /
            (mu*(1-mu/n)*scale^3)^{1/6} * \\sqrt(var\\_weights)

        where cox_snell is defined as
        cox_snell(x) = betainc(2/3., 2/3., x)*betainc(2/3.,2/3.)
        where betainc is the incomplete beta function as defined in scipy,
        which uses a regularized version (with the unregularized version, one
        would just have :math:`cox_snell(x) = Betainc(2/3., 2/3., x)`).

        The name \'cox_snell\' is idiosyncratic and is simply used for
        convenience following the approach suggested in Cox and Snell (1968).
        Further note that
        :math:`cox\\_snell(x) = \\frac{3}{2}*x^{2/3} *
        hyp2f1(2/3.,1/3.,5/3.,x)`
        where hyp2f1 is the hypergeometric 2f1 function.  The Anscombe
        residuals are sometimes defined in the literature using the
        hyp2f1 formulation.  Both betainc and hyp2f1 can be found in scipy.

        References
        ----------
        Anscombe, FJ. (1953) "Contribution to the discussion of H. Hotelling\'s
            paper." Journal of the Royal Statistical Society B. 15, 229-30.

        Cox, DR and Snell, EJ. (1968) "A General Definition of Residuals."
            Journal of the Royal Statistical Society B. 30, 248-75.
        '''
    def get_distribution(self, mu, scale: float = 1.0, var_weights: float = 1.0, n_trials: int = 1):
        """
        Frozen Binomial distribution instance for given parameters

        Parameters
        ----------
        mu : ndarray
            Usually but not always the fitted mean response variable.
        scale : float
            The scale parameter is ignored.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
            var_weights are ignored for Poisson.
        n_trials : int
            Number of trials for the binomial distribution. The default is 1
            which corresponds to a Bernoulli random variable.

        Returns
        -------
        distribution instance

        """

class InverseGaussian(Family):
    """
    InverseGaussian exponential family.

    Parameters
    ----------
    link : a link instance, optional
        The default link for the inverse Gaussian family is the
        inverse squared link.
        Available links are InverseSquared, Inverse, Log, and Identity.
        See statsmodels.genmod.families.links for more information.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    InverseGaussian.link : a link instance
        The link function of the inverse Gaussian instance
    InverseGaussian.variance : varfunc instance
        ``variance`` is an instance of
        statsmodels.genmod.families.varfuncs.mu_cubed

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.

    Notes
    -----
    The inverse Gaussian distribution is sometimes referred to in the
    literature as the Wald distribution.
    """
    links: Incomplete
    variance: Incomplete
    safe_links: Incomplete
    def __init__(self, link: Incomplete | None = None, check_link: bool = True) -> None: ...
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Inverse Gaussian distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        .. math::

           ll_i = -1/2 * (var\\_weights_i * (endog_i - \\mu_i)^2 /
           (scale * endog_i * \\mu_i^2) + \\ln(scale * \\endog_i^3 /
           var\\_weights_i) - \\ln(2 * \\pi))
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals for the inverse Gaussian distribution  as
            defined below

        Notes
        -----
        .. math::

           resid\\_anscombe_i = \\log(Y_i / \\mu_i) / \\sqrt{\\mu_i * scale} *
           \\sqrt(var\\_weights)
        """
    def get_distribution(self, mu, scale, var_weights: float = 1.0):
        """
        Frozen Inverse Gaussian distribution instance for given parameters

        Parameters
        ----------
        mu : ndarray
            Usually but not always the fitted mean response variable.
        scale : float
            The scale parameter is required argument for get_distribution.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.

        Returns
        -------
        distribution instance

        """

class NegativeBinomial(Family):
    """
    Negative Binomial exponential family (corresponds to NB2).

    Parameters
    ----------
    link : a link instance, optional
        The default link for the negative binomial family is the log link.
        Available links are log, cloglog, identity, nbinom and power.
        See statsmodels.genmod.families.links for more information.
    alpha : float, optional
        The ancillary parameter for the negative binomial distribution.
        For now ``alpha`` is assumed to be nonstochastic.  The default value
        is 1.  Permissible values are usually assumed to be between .01 and 2.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    NegativeBinomial.link : a link instance
        The link function of the negative binomial instance
    NegativeBinomial.variance : varfunc instance
        ``variance`` is an instance of
        statsmodels.genmod.families.varfuncs.nbinom

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.

    Notes
    -----
    Power link functions are not yet supported.

    Parameterization for :math:`y=0, 1, 2, \\ldots` is

    .. math::

       f(y) = \\frac{\\Gamma(y+\\frac{1}{\\alpha})}{y!\\Gamma(\\frac{1}{\\alpha})}
              \\left(\\frac{1}{1+\\alpha\\mu}\\right)^{\\frac{1}{\\alpha}}
              \\left(\\frac{\\alpha\\mu}{1+\\alpha\\mu}\\right)^y

    with :math:`E[Y]=\\mu\\,` and :math:`Var[Y]=\\mu+\\alpha\\mu^2`.
    """
    links: Incomplete
    variance: Incomplete
    safe_links: Incomplete
    alpha: Incomplete
    def __init__(self, link: Incomplete | None = None, alpha: float = 1.0, check_link: bool = True) -> None: ...
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Negative Binomial distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        Defined as:

        .. math::

           llf = \\sum_i var\\_weights_i / scale * (Y_i * \\log{(\\alpha * \\mu_i /
                 (1 + \\alpha * \\mu_i))} - \\log{(1 + \\alpha * \\mu_i)}/
                 \\alpha + Constant)

        where :math:`Constant` is defined as:

        .. math::

           Constant = \\ln \\Gamma{(Y_i + 1/ \\alpha )} - \\ln \\Gamma(Y_i + 1) -
                      \\ln \\Gamma{(1/ \\alpha )}

        constant = (special.gammaln(endog + 1 / self.alpha) -
                    special.gammaln(endog+1)-special.gammaln(1/self.alpha))
        return (endog * np.log(self.alpha * mu / (1 + self.alpha * mu)) -
                np.log(1 + self.alpha * mu) / self.alpha +
                constant) * var_weights / scale
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals as defined below.

        Notes
        -----
        Anscombe residuals for Negative Binomial are the same as for Binomial
        upon setting :math:`n=-\\frac{1}{\\alpha}`. Due to the negative value of
        :math:`-\\alpha*Y` the representation with the hypergeometric function
        :math:`H2F1(x) =  hyp2f1(2/3.,1/3.,5/3.,x)` is advantageous

        .. math::

            resid\\_anscombe_i = \\frac{3}{2} *
            (Y_i^(2/3)*H2F1(-\\alpha*Y_i) - \\mu_i^(2/3)*H2F1(-\\alpha*\\mu_i))
            / (\\mu_i * (1+\\alpha*\\mu_i) * scale^3)^(1/6) * \\sqrt(var\\_weights)

        Note that for the (unregularized) Beta function, one has
        :math:`Beta(z,a,b) = z^a/a * H2F1(a,1-b,a+1,z)`
        """
    def get_distribution(self, mu, scale: float = 1.0, var_weights: float = 1.0):
        """
        Frozen NegativeBinomial distribution instance for given parameters

        Parameters
        ----------
        mu : ndarray
            Usually but not always the fitted mean response variable.
        scale : float
            The scale parameter is ignored.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
            var_weights are ignored for NegativeBinomial.

        Returns
        -------
        distribution instance

        """

class Tweedie(Family):
    """
    Tweedie family.

    Parameters
    ----------
    link : a link instance, optional
        The default link for the Tweedie family is the log link.
        Available links are log, Power and any aliases of power.
        See statsmodels.genmod.families.links for more information.
    var_power : float, optional
        The variance power. The default is 1.
    eql : bool
        If True, the Extended Quasi-Likelihood is used, else the
        likelihood is used.
        In both cases, for likelihood computations the var_power
        must be between 1 and 2.
    check_link : bool
        If True (default), then and exception is raised if the link is invalid
        for the family.
        If False, then the link is not checked.

    Attributes
    ----------
    Tweedie.link : a link instance
        The link function of the Tweedie instance
    Tweedie.variance : varfunc instance
        ``variance`` is an instance of
        statsmodels.genmod.families.varfuncs.Power
    Tweedie.var_power : float
        The power parameter of the variance function.

    See Also
    --------
    statsmodels.genmod.families.family.Family : Parent class for all links.
    :ref:`links` : Further details on links.

    Notes
    -----
    Loglikelihood function not implemented because of the complexity of
    calculating an infinite series of summations. The variance power can be
    estimated using the ``estimate_tweedie_power`` function that is part of the
    statsmodels.genmod.generalized_linear_model.GLM class.
    """
    links: Incomplete
    variance: Incomplete
    safe_links: Incomplete
    var_power: Incomplete
    eql: Incomplete
    def __init__(self, link: Incomplete | None = None, var_power: float = 1.0, eql: bool = False, check_link: bool = True) -> None: ...
    def loglike_obs(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The log-likelihood function for each observation in terms of the fitted
        mean response for the Tweedie distribution.

        Parameters
        ----------
        endog : ndarray
            Usually the endogenous response variable.
        mu : ndarray
            Usually but not always the fitted mean response variable.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float
            The scale parameter. The default is 1.

        Returns
        -------
        ll_i : float
            The value of the loglikelihood evaluated at
            (endog, mu, var_weights, scale) as defined below.

        Notes
        -----
        If eql is True, the Extended Quasi-Likelihood is used.  At present,
        this method returns NaN if eql is False.  When the actual likelihood
        is implemented, it will be accessible by setting eql to False.

        References
        ----------
        R Kaas (2005).  Compound Poisson Distributions and GLM's -- Tweedie's
        Distribution.
        https://core.ac.uk/download/pdf/6347266.pdf#page=11

        JA Nelder, D Pregibon (1987).  An extended quasi-likelihood function.
        Biometrika 74:2, pp 221-232.  https://www.jstor.org/stable/2336136
        """
    def resid_anscombe(self, endog, mu, var_weights: float = 1.0, scale: float = 1.0):
        """
        The Anscombe residuals

        Parameters
        ----------
        endog : ndarray
            The endogenous response variable
        mu : ndarray
            The inverse of the link function at the linear predicted values.
        var_weights : array_like
            1d array of variance (analytic) weights. The default is 1.
        scale : float, optional
            An optional argument to divide the residuals by sqrt(scale).
            The default is 1.

        Returns
        -------
        resid_anscombe : ndarray
            The Anscombe residuals as defined below.

        Notes
        -----
        When :math:`p = 3`, then

        .. math::

            resid\\_anscombe_i = \\log(endog_i / \\mu_i) / \\sqrt{\\mu_i * scale} *
            \\sqrt(var\\_weights)

        Otherwise,

        .. math::

            c = (3 - p) / 3

        .. math::

            resid\\_anscombe_i = (1 / c) * (endog_i^c - \\mu_i^c) / \\mu_i^{p / 6}
            / \\sqrt{scale} * \\sqrt(var\\_weights)
        """
