from _typeshed import Incomplete

class ParametricMixtureD:
    """mixtures with a discrete distribution

    The mixing distribution is a discrete distribution like scipy.stats.poisson.
    All distribution in the mixture of the same type and parametrized
    by the outcome of the mixing distribution and have to be a continuous
    distribution (or have a pdf method).
    As an example, a mixture of normal distributed random variables with
    Poisson as the mixing distribution.


    assumes vectorized shape, loc and scale as in scipy.stats.distributions

    assume mixing_dist is frozen

    initialization looks fragile for all possible cases of lower and upper
    bounds of the distributions.

    """
    mixing_dist: Incomplete
    base_dist: Incomplete
    ma: Incomplete
    mb: Incomplete
    mixing_probs: Incomplete
    bd_args: Incomplete
    bd_kwds: Incomplete
    def __init__(self, mixing_dist, base_dist, bd_args_func, bd_kwds_func, cutoff: float = 0.001) -> None:
        """create a mixture distribution

        Parameters
        ----------
        mixing_dist : discrete frozen distribution
            mixing distribution
        base_dist : continuous distribution
            parametrized distributions in the mixture
        bd_args_func : callable
            function that builds the tuple of args for the base_dist.
            The function obtains as argument the values in the support of
            the mixing distribution and should return an empty tuple or
            a tuple of arrays.
        bd_kwds_func : callable
            function that builds the dictionary of kwds for the base_dist.
            The function obtains as argument the values in the support of
            the mixing distribution and should return an empty dictionary or
            a dictionary with arrays as values.
        cutoff : float
            If the mixing distribution has infinite support, then the
            distribution is truncated with approximately (subject to integer
            conversion) the cutoff probability in the missing tail. Random
            draws that are outside the truncated range are clipped, that is
            assigned to the highest or lowest value in the truncated support.

        """
    def rvs(self, size: int = 1): ...
    def pdf(self, x): ...
    def cdf(self, x): ...

class ClippedContinuous:
    """clipped continuous distribution with a masspoint at clip_lower


    Notes
    -----
    first version, to try out possible designs
    insufficient checks for valid arguments and not clear
    whether it works for distributions that have compact support

    clip_lower is fixed and independent of the distribution parameters.
    The clip_lower point in the pdf has to be interpreted as a mass point,
    i.e. different treatment in integration and expect function, which means
    none of the generic methods for this can be used.

    maybe this will be better designed as a mixture between a degenerate or
    discrete and a continuous distribution

    Warning: uses equality to check for clip_lower values in function
    arguments, since these are floating points, the comparison might fail
    if clip_lower values are not exactly equal.
    We could add a check whether the values are in a small neighborhood, but
    it would be expensive (need to search and check all values).

    """
    base_dist: Incomplete
    clip_lower: Incomplete
    def __init__(self, base_dist, clip_lower) -> None: ...
    def rvs(self, *args, **kwds): ...
    def pdf(self, x, *args, **kwds): ...
    def cdf(self, x, *args, **kwds): ...
    def sf(self, x, *args, **kwds): ...
    def ppf(self, x, *args, **kwds) -> None: ...
    def plot(self, x, *args, **kwds) -> None: ...
