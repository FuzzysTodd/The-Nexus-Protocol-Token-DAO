from _typeshed import Incomplete

def quantiles(a, prob=..., alphap: float = 0.4, betap: float = 0.4, axis: Incomplete | None = None, limit=(), masknan: bool = False):
    """
    Computes empirical quantiles for a data array.

    Samples quantile are defined by :math:`Q(p) = (1-g).x[i] +g.x[i+1]`,
    where :math:`x[j]` is the *j*th order statistic, and
    `i = (floor(n*p+m))`, `m=alpha+p*(1-alpha-beta)` and `g = n*p + m - i`.

    Typical values of (alpha,beta) are:
        - (0,1)    : *p(k) = k/n* : linear interpolation of cdf (R, type 4)
        - (.5,.5)  : *p(k) = (k+1/2.)/n* : piecewise linear
          function (R, type 5)
        - (0,0)    : *p(k) = k/(n+1)* : (R type 6)
        - (1,1)    : *p(k) = (k-1)/(n-1)*. In this case, p(k) = mode[F(x[k])].
          That's R default (R type 7)
        - (1/3,1/3): *p(k) = (k-1/3)/(n+1/3)*. Then p(k) ~ median[F(x[k])].
          The resulting quantile estimates are approximately median-unbiased
          regardless of the distribution of x. (R type 8)
        - (3/8,3/8): *p(k) = (k-3/8)/(n+1/4)*. Blom.
          The resulting quantile estimates are approximately unbiased
          if x is normally distributed (R type 9)
        - (.4,.4)  : approximately quantile unbiased (Cunnane)
        - (.35,.35): APL, used with PWM ?? JP
        - (0.35, 0.65): PWM   ?? JP  p(k) = (k-0.35)/n

    Parameters
    ----------
    a : array_like
        Input data, as a sequence or array of dimension at most 2.
    prob : array_like, optional
        List of quantiles to compute.
    alpha : float, optional
        Plotting positions parameter, default is 0.4.
    beta : float, optional
        Plotting positions parameter, default is 0.4.
    axis : int, optional
        Axis along which to perform the trimming.
        If None (default), the input array is first flattened.
    limit : tuple
        Tuple of (lower, upper) values.
        Values of `a` outside this closed interval are ignored.

    Returns
    -------
    quants : MaskedArray
        An array containing the calculated quantiles.

    Examples
    --------
    >>> from scipy.stats.mstats import mquantiles
    >>> a = np.array([6., 47., 49., 15., 42., 41., 7., 39., 43., 40., 36.])
    >>> mquantiles(a)
    array([ 19.2,  40. ,  42.8])

    Using a 2D array, specifying axis and limit.

    >>> data = np.array([[   6.,    7.,    1.],
                         [  47.,   15.,    2.],
                         [  49.,   36.,    3.],
                         [  15.,   39.,    4.],
                         [  42.,   40., -999.],
                         [  41.,   41., -999.],
                         [   7., -999., -999.],
                         [  39., -999., -999.],
                         [  43., -999., -999.],
                         [  40., -999., -999.],
                         [  36., -999., -999.]])
    >>> mquantiles(data, axis=0, limit=(0, 50))
    array([[ 19.2 ,  14.6 ,   1.45],
           [ 40.  ,  37.5 ,   2.5 ],
           [ 42.8 ,  40.05,   3.55]])

    >>> data[:, 2] = -999.
    >>> mquantiles(data, axis=0, limit=(0, 50))
    masked_array(data =
     [[19.2 14.6 --]
     [40.0 37.5 --]
     [42.8 40.05 --]],
                 mask =
     [[False False  True]
      [False False  True]
      [False False  True]],
           fill_value = 1e+20)
    """
def scoreatpercentile(data, per, limit=(), alphap: float = 0.4, betap: float = 0.4, axis: int = 0, masknan: Incomplete | None = None):
    """Calculate the score at the given 'per' percentile of the
    sequence a.  For example, the score at per=50 is the median.

    This function is a shortcut to mquantile
    """
def plotting_positions(data, alpha: float = 0.4, beta: float = 0.4, axis: int = 0, masknan: bool = False):
    '''Returns the plotting positions (or empirical percentile points) for the
    data.
    Plotting positions are defined as (i-alpha)/(n+1-alpha-beta), where:
        - i is the rank order statistics (starting at 1)
        - n is the number of unmasked values along the given axis
        - alpha and beta are two parameters.

    Typical values for alpha and beta are:
        - (0,1)    : *p(k) = k/n* : linear interpolation of cdf (R, type 4)
        - (.5,.5)  : *p(k) = (k-1/2.)/n* : piecewise linear function (R, type 5)
          (Bliss 1967: "Rankit")
        - (0,0)    : *p(k) = k/(n+1)* : Weibull (R type 6), (Van der Waerden 1952)
        - (1,1)    : *p(k) = (k-1)/(n-1)*. In this case, p(k) = mode[F(x[k])].
          That\'s R default (R type 7)
        - (1/3,1/3): *p(k) = (k-1/3)/(n+1/3)*. Then p(k) ~ median[F(x[k])].
          The resulting quantile estimates are approximately median-unbiased
          regardless of the distribution of x. (R type 8), (Tukey 1962)
        - (3/8,3/8): *p(k) = (k-3/8)/(n+1/4)*.
          The resulting quantile estimates are approximately unbiased
          if x is normally distributed (R type 9) (Blom 1958)
        - (.4,.4)  : approximately quantile unbiased (Cunnane)
        - (.35,.35): APL, used with PWM

    Parameters
    ----------
    x : sequence
        Input data, as a sequence or array of dimension at most 2.
    prob : sequence
        List of quantiles to compute.
    alpha : {0.4, float} optional
        Plotting positions parameter.
    beta : {0.4, float} optional
        Plotting positions parameter.

    Notes
    -----
    I think the adjustments assume that there are no ties in order to be a reasonable
    approximation to a continuous density function. TODO: check this

    References
    ----------
    unknown,
    dates to original papers from Beasley, Erickson, Allison 2009 Behav Genet
    '''
meppf = plotting_positions

def plotting_positions_w1d(data, weights: Incomplete | None = None, alpha: float = 0.4, beta: float = 0.4, method: str = 'notnormed'):
    '''Weighted plotting positions (or empirical percentile points) for the data.

    observations are weighted and the plotting positions are defined as
    (ws-alpha)/(n-alpha-beta), where:
        - ws is the weighted rank order statistics or cumulative weighted sum,
          normalized to n if method is "normed"
        - n is the number of values along the given axis if method is "normed"
          and total weight otherwise
        - alpha and beta are two parameters.

    wtd.quantile in R package Hmisc seems to use the "notnormed" version.
    notnormed coincides with unweighted segment in example, drop "normed" version ?


    See Also
    --------
    plotting_positions : unweighted version that works also with more than one
        dimension and has other options
    '''
def edf_normal_inverse_transformed(x, alpha=..., beta=..., axis: int = 0):
    """rank based normal inverse transformed cdf
    """
