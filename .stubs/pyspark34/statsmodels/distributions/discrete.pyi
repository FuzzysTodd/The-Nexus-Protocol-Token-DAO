from _typeshed import Incomplete
from scipy.stats import rv_discrete
from statsmodels.base.model import GenericLikelihoodModel as GenericLikelihoodModel

class genpoisson_p_gen(rv_discrete):
    """Generalized Poisson distribution
    """
    def mean(self, mu, alpha, p): ...
    def var(self, mu, alpha, p): ...

genpoisson_p: Incomplete

class zipoisson_gen(rv_discrete):
    """Zero Inflated Poisson distribution
    """
    def mean(self, mu, w): ...
    def var(self, mu, w): ...

zipoisson: Incomplete

class zigeneralizedpoisson_gen(rv_discrete):
    """Zero Inflated Generalized Poisson distribution
    """
    def mean(self, mu, alpha, p, w): ...
    def var(self, mu, alpha, p, w): ...

zigenpoisson: Incomplete

class zinegativebinomial_gen(rv_discrete):
    """Zero Inflated Generalized Negative Binomial distribution
    """
    def mean(self, mu, alpha, p, w): ...
    def var(self, mu, alpha, p, w): ...
    def convert_params(self, mu, alpha, p): ...

zinegbin: Incomplete

class truncatedpoisson_gen(rv_discrete):
    """Truncated Poisson discrete random variable
    """

truncatedpoisson: Incomplete

class truncatednegbin_gen(rv_discrete):
    """Truncated Generalized Negative Binomial (NB-P) discrete random variable
    """
    def convert_params(self, mu, alpha, p): ...

truncatednegbin: Incomplete

class DiscretizedCount(rv_discrete):
    '''Count distribution based on discretized distribution

    Parameters
    ----------
    distr : distribution instance
    d_offset : float
        Offset for integer interval, default is zero.
        The discrete random variable is ``y = floor(x + offset)`` where x is
        the continuous random variable.
        Warning: not verified for all methods.
    add_scale : bool
        If True (default), then the scale of the base distribution is added
        as parameter for the discrete distribution. The scale parameter is in
        the last position.
    kwds : keyword arguments
        The extra keyword arguments are used delegated to the ``__init__`` of
        the super class.
        Their usage has not been checked, e.g. currently the support of the
        distribution is assumed to be all non-negative integers.

    Notes
    -----
    `loc` argument is currently not supported, scale is not available for
    discrete distributions in scipy. The scale parameter of the underlying
    continuous distribution is the last shape parameter in this
    DiscretizedCount distribution if ``add_scale`` is True.

    The implementation was based mainly on [1]_ and [2]_. However, many new
    discrete distributions have been developed based on the approach that we
    use here. Note, that in many cases authors reparameterize the distribution,
    while this class inherits the parameterization from the underlying
    continuous distribution.

    References
    ----------
    .. [1] Chakraborty, Subrata, and Dhrubajyoti Chakravarty. "Discrete gamma
       distributions: Properties and parameter estimations." Communications in
       Statistics-Theory and Methods 41, no. 18 (2012): 3301-3324.

    .. [2] Alzaatreh, Ayman, Carl Lee, and Felix Famoye. 2012. “On the Discrete
       Analogues of Continuous Distributions.” Statistical Methodology 9 (6):
       589–603.


    '''
    def __new__(cls, *args, **kwds): ...
    distr: Incomplete
    d_offset: Incomplete
    add_scale: Incomplete
    k_shapes: Incomplete
    def __init__(self, distr, d_offset: int = 0, add_scale: bool = True, **kwds) -> None: ...

class DiscretizedModel(GenericLikelihoodModel):
    '''experimental model to fit discretized distribution

    Count models based on discretized distributions can be used to model
    data that is under- or over-dispersed relative to Poisson or that has
    heavier tails.

    Parameters
    ----------
    endog : array_like, 1-D
        Univariate data for fitting the distribution.
    exog : None
        Explanatory variables are not supported. The ``exog`` argument is
        only included for consistency in the signature across models.
    distr : DiscretizedCount instance
        (required) Instance of a DiscretizedCount distribution.

    See Also
    --------
    DiscretizedCount

    Examples
    --------
    >>> from scipy import stats
    >>> from statsmodels.distributions.discrete import (
            DiscretizedCount, DiscretizedModel)

    >>> dd = DiscretizedCount(stats.gamma)
    >>> mod = DiscretizedModel(y, distr=dd)
    >>> res = mod.fit()
    >>> probs = res.predict(which="probs", k_max=5)

    '''
    df_resid: Incomplete
    df_model: int
    k_extra: Incomplete
    k_constant: int
    nparams: Incomplete
    start_params: Incomplete
    def __init__(self, endog, exog: Incomplete | None = None, distr: Incomplete | None = None) -> None: ...
    def loglike(self, params): ...
    def predict(self, params, exog: Incomplete | None = None, which: Incomplete | None = None, k_max: int = 20): ...
    def get_distr(self, params):
        """frozen distribution instance of the discrete distribution.
        """
