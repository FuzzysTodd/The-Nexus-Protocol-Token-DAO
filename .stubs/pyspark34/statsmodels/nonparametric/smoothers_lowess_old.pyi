def lowess(endog, exog, frac=..., it: int = 3):
    '''
    LOWESS (Locally Weighted Scatterplot Smoothing)

    A lowess function that outs smoothed estimates of endog
    at the given exog values from points (exog, endog)

    Parameters
    ----------
    endog : 1-D numpy array
        The y-values of the observed points
    exog : 1-D numpy array
        The x-values of the observed points
    frac : float
        Between 0 and 1. The fraction of the data used
        when estimating each y-value.
    it : int
        The number of residual-based reweightings
        to perform.

    Returns
    -------
    out: numpy array
        A numpy array with two columns. The first column
        is the sorted x values and the second column the
        associated estimated y-values.

    Notes
    -----
    This lowess function implements the algorithm given in the
    reference below using local linear estimates.

    Suppose the input data has N points. The algorithm works by
    estimating the true ``y_i`` by taking the frac*N closest points
    to ``(x_i,y_i)`` based on their x values and estimating ``y_i``
    using a weighted linear regression. The weight for ``(x_j,y_j)``
    is `_lowess_tricube` function applied to ``|x_i-x_j|``.

    If ``iter > 0``, then further weighted local linear regressions
    are performed, where the weights are the same as above
    times the `_lowess_bisquare` function of the residuals. Each iteration
    takes approximately the same amount of time as the original fit,
    so these iterations are expensive. They are most useful when
    the noise has extremely heavy tails, such as Cauchy noise.
    Noise with less heavy-tails, such as t-distributions with ``df > 2``,
    are less problematic. The weights downgrade the influence of
    points with large residuals. In the extreme case, points whose
    residuals are larger than 6 times the median absolute residual
    are given weight 0.

    Some experimentation is likely required to find a good
    choice of frac and iter for a particular dataset.

    References
    ----------
    Cleveland, W.S. (1979) "Robust Locally Weighted Regression
    and Smoothing Scatterplots". Journal of the American Statistical
    Association 74 (368): 829-836.

    Examples
    --------
    The below allows a comparison between how different the fits from
    `lowess` for different values of frac can be.

    >>> import numpy as np
    >>> import statsmodels.api as sm
    >>> lowess = sm.nonparametric.lowess
    >>> x = np.random.uniform(low=-2*np.pi, high=2*np.pi, size=500)
    >>> y = np.sin(x) + np.random.normal(size=len(x))
    >>> z = lowess(y, x)
    >>> w = lowess(y, x, frac=1./3)

    This gives a similar comparison for when it is 0 vs not.

    >>> import scipy.stats as stats
    >>> x = np.random.uniform(low=-2*np.pi, high=2*np.pi, size=500)
    >>> y = np.sin(x) + stats.cauchy.rvs(size=len(x))
    >>> z = lowess(y, x, frac= 1./3, it=0)
    >>> w = lowess(y, x, frac=1./3)
    '''
