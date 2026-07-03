from _typeshed import Incomplete

def mixture_rvs(prob, size, dist, kwargs: Incomplete | None = None):
    """
    Sample from a mixture of distributions.

    Parameters
    ----------
    prob : array_like
        Probability of sampling from each distribution in dist
    size : int
        The length of the returned sample.
    dist : array_like
        An iterable of distributions objects from scipy.stats.
    kwargs : tuple of dicts, optional
        A tuple of dicts.  Each dict in kwargs can have keys loc, scale, and
        args to be passed to the respective distribution in dist.  If not
        provided, the distribution defaults are used.

    Examples
    --------
    Say we want 5000 random variables from mixture of normals with two
    distributions norm(-1,.5) and norm(1,.5) and we want to sample from the
    first with probability .75 and the second with probability .25.

    >>> from scipy import stats
    >>> prob = [.75,.25]
    >>> Y = mixture_rvs(prob, 5000, dist=[stats.norm, stats.norm],
    ...                 kwargs = (dict(loc=-1,scale=.5),dict(loc=1,scale=.5)))
    """

class MixtureDistribution:
    """univariate mixture distribution

    for simple case for now (unbound support)
    does not yet inherit from scipy.stats.distributions

    adding pdf to mixture_rvs, some restrictions on broadcasting
    Currently it does not hold any state, all arguments included in each method.
    """
    def rvs(self, prob, size, dist, kwargs: Incomplete | None = None): ...
    def pdf(self, x, prob, dist, kwargs: Incomplete | None = None):
        """
        pdf a mixture of distributions.

        Parameters
        ----------
        x : array_like
            Array containing locations where the PDF should be evaluated
        prob : array_like
            Probability of sampling from each distribution in dist
        dist : array_like
            An iterable of distributions objects from scipy.stats.
        kwargs : tuple of dicts, optional
            A tuple of dicts.  Each dict in kwargs can have keys loc, scale, and
            args to be passed to the respective distribution in dist.  If not
            provided, the distribution defaults are used.

        Examples
        --------
        Say we want 5000 random variables from mixture of normals with two
        distributions norm(-1,.5) and norm(1,.5) and we want to sample from the
        first with probability .75 and the second with probability .25.

        >>> import numpy as np
        >>> from scipy import stats
        >>> from statsmodels.distributions.mixture_rvs import MixtureDistribution
        >>> x = np.arange(-4.0, 4.0, 0.01)
        >>> prob = [.75,.25]
        >>> mixture = MixtureDistribution()
        >>> Y = mixture.pdf(x, prob, dist=[stats.norm, stats.norm],
        ...                 kwargs = (dict(loc=-1,scale=.5),dict(loc=1,scale=.5)))
        """
    def cdf(self, x, prob, dist, kwargs: Incomplete | None = None):
        """
        cdf of a mixture of distributions.

        Parameters
        ----------
        x : array_like
            Array containing locations where the CDF should be evaluated
        prob : array_like
            Probability of sampling from each distribution in dist
        size : int
            The length of the returned sample.
        dist : array_like
            An iterable of distributions objects from scipy.stats.
        kwargs : tuple of dicts, optional
            A tuple of dicts.  Each dict in kwargs can have keys loc, scale, and
            args to be passed to the respective distribution in dist.  If not
            provided, the distribution defaults are used.

        Examples
        --------
        Say we want 5000 random variables from mixture of normals with two
        distributions norm(-1,.5) and norm(1,.5) and we want to sample from the
        first with probability .75 and the second with probability .25.

        >>> import numpy as np
        >>> from scipy import stats
        >>> from statsmodels.distributions.mixture_rvs import MixtureDistribution
        >>> x = np.arange(-4.0, 4.0, 0.01)
        >>> prob = [.75,.25]
        >>> mixture = MixtureDistribution()
        >>> Y = mixture.pdf(x, prob, dist=[stats.norm, stats.norm],
        ...                 kwargs = (dict(loc=-1,scale=.5),dict(loc=1,scale=.5)))
        """

def mv_mixture_rvs(prob, size, dist, nvars, **kwargs):
    """
    Sample from a mixture of multivariate distributions.

    Parameters
    ----------
    prob : array_like
        Probability of sampling from each distribution in dist
    size : int
        The length of the returned sample.
    dist : array_like
        An iterable of distributions instances with callable method rvs.
    nvargs : int
        dimension of the multivariate distribution, could be inferred instead
    kwargs : tuple of dicts, optional
        ignored

    Examples
    --------
    Say we want 2000 random variables from mixture of normals with two
    multivariate normal distributions, and we want to sample from the
    first with probability .4 and the second with probability .6.

    import statsmodels.sandbox.distributions.mv_normal as mvd

    cov3 = np.array([[ 1.  ,  0.5 ,  0.75],
                       [ 0.5 ,  1.5 ,  0.6 ],
                       [ 0.75,  0.6 ,  2.  ]])

    mu = np.array([-1, 0.0, 2.0])
    mu2 = np.array([4, 2.0, 2.0])
    mvn3 = mvd.MVNormal(mu, cov3)
    mvn32 = mvd.MVNormal(mu2, cov3/2., 4)
    rvs = mix.mv_mixture_rvs([0.4, 0.6], 2000, [mvn3, mvn32], 3)
    """
