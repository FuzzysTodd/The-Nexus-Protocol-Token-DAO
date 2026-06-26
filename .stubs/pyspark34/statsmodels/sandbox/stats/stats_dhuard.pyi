from _typeshed import Incomplete

def scoreatpercentile(data, percentile):
    """Return the score at the given percentile of the data.

    Example:
        >>> data = randn(100)
            >>> scoreatpercentile(data, 50)

        will return the median of sample `data`.
    """
def percentileofscore(data, score):
    """Return the percentile-position of score relative to data.

    score: Array of scores at which the percentile is computed.

    Return percentiles (0-100).

    Example
            r = randn(50)
        x = linspace(-2,2,100)
        percentileofscore(r,x)

    Raise an error if the score is outside the range of data.
    """
def empiricalcdf(data, method: str = 'Hazen'):
    """Return the empirical cdf.

    Methods available:
        Hazen:       (i-0.5)/N
            Weibull:     i/(N+1)
        Chegodayev:  (i-.3)/(N+.4)
        Cunnane:     (i-.4)/(N+.2)
        Gringorten:  (i-.44)/(N+.12)
        California:  (i-1)/N

    Where i goes from 1 to N.
    """

class HistDist:
    """Distribution with piecewise linear cdf, pdf is step function

    can be created from empiricial distribution or from a histogram (not done yet)

    work in progress, not finished


    """
    data: Incomplete
    binlimit: Incomplete
    ranking: Incomplete
    cdfintp: Incomplete
    ppfintp: Incomplete
    def __init__(self, data) -> None: ...
    def empiricalcdf(self, data: Incomplete | None = None, method: str = 'Hazen'):
        """Return the empirical cdf.

        Methods available:
            Hazen:       (i-0.5)/N
                Weibull:     i/(N+1)
            Chegodayev:  (i-.3)/(N+.4)
            Cunnane:     (i-.4)/(N+.2)
            Gringorten:  (i-.44)/(N+.12)
            California:  (i-1)/N

        Where i goes from 1 to N.
        """
    def cdf_emp(self, score):
        """
        this is score in dh

        """
    def ppf_emp(self, quantile):
        """
        this is score in dh

        """
    nbin: Incomplete
    def optimize_binning(self, method: str = 'Freedman'):
        """Find the optimal number of bins and update the bin countaccordingly.
        Available methods : Freedman
                            Scott
        """
