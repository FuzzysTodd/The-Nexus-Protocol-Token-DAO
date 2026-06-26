from _typeshed import Incomplete
from scipy import stats

__date__: str

class MaxDist(stats.rv_continuous):
    """ max of n of scipy.stats normal expon ...
        Example:
            maxnormal10 = RVmax( scipy.stats.norm, 10 )
            sample = maxnormal10( size=1000 )
            sample.cdf = cdf ^ n,  ppf ^ (1/n)
    """
    dist: Incomplete
    n: Incomplete
    def __init__(self, dist, n) -> None: ...

maxdistr: Incomplete
