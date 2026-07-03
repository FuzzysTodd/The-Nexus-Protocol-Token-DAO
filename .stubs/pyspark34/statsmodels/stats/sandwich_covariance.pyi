from _typeshed import Incomplete
from statsmodels.stats.moment_helpers import se_cov as se_cov

__all__ = ['cov_cluster', 'cov_cluster_2groups', 'cov_hac', 'cov_nw_panel', 'cov_white_simple', 'cov_hc0', 'cov_hc1', 'cov_hc2', 'cov_hc3', 'se_cov', 'weights_bartlett', 'weights_uniform']

def cov_hc0(results):
    """
    See statsmodels.RegressionResults
    """
def cov_hc1(results):
    """
    See statsmodels.RegressionResults
    """
def cov_hc2(results):
    """
    See statsmodels.RegressionResults
    """
def cov_hc3(results):
    """
    See statsmodels.RegressionResults
    """
def weights_bartlett(nlags):
    """Bartlett weights for HAC

    this will be moved to another module

    Parameters
    ----------
    nlags : int
       highest lag in the kernel window, this does not include the zero lag

    Returns
    -------
    kernel : ndarray, (nlags+1,)
        weights for Bartlett kernel

    """
def weights_uniform(nlags):
    """uniform weights for HAC

    this will be moved to another module

    Parameters
    ----------
    nlags : int
       highest lag in the kernel window, this does not include the zero lag

    Returns
    -------
    kernel : ndarray, (nlags+1,)
        weights for uniform kernel

    """
def cov_cluster(results, group, use_correction: bool = True):
    """cluster robust covariance matrix

    Calculates sandwich covariance matrix for a single cluster, i.e. grouped
    variables.

    Parameters
    ----------
    results : result instance
       result of a regression, uses results.model.exog and results.resid
       TODO: this should use wexog instead
    use_correction : bool
       If true (default), then the small sample correction factor is used.

    Returns
    -------
    cov : ndarray, (k_vars, k_vars)
        cluster robust covariance matrix for parameter estimates

    Notes
    -----
    same result as Stata in UCLA example and same as Peterson

    """
def cov_cluster_2groups(results, group, group2: Incomplete | None = None, use_correction: bool = True):
    """cluster robust covariance matrix for two groups/clusters

    Parameters
    ----------
    results : result instance
       result of a regression, uses results.model.exog and results.resid
       TODO: this should use wexog instead
    use_correction : bool
       If true (default), then the small sample correction factor is used.

    Returns
    -------
    cov_both : ndarray, (k_vars, k_vars)
        cluster robust covariance matrix for parameter estimates, for both
        clusters
    cov_0 : ndarray, (k_vars, k_vars)
        cluster robust covariance matrix for parameter estimates for first
        cluster
    cov_1 : ndarray, (k_vars, k_vars)
        cluster robust covariance matrix for parameter estimates for second
        cluster

    Notes
    -----

    verified against Peterson's table, (4 decimal print precision)
    """
def cov_white_simple(results, use_correction: bool = True):
    """
    heteroscedasticity robust covariance matrix (White)

    Parameters
    ----------
    results : result instance
       result of a regression, uses results.model.exog and results.resid
       TODO: this should use wexog instead

    Returns
    -------
    cov : ndarray, (k_vars, k_vars)
        heteroscedasticity robust covariance matrix for parameter estimates

    Notes
    -----
    This produces the same result as cov_hc0, and does not include any small
    sample correction.

    verified (against LinearRegressionResults and Peterson)

    See Also
    --------
    cov_hc1, cov_hc2, cov_hc3 : heteroscedasticity robust covariance matrices
        with small sample corrections

    """
cov_hac = cov_hac_simple

def cov_nw_panel(results, nlags, groupidx, weights_func=..., use_correction: str = 'hac'):
    """Panel HAC robust covariance matrix

    Assumes we have a panel of time series with consecutive, equal spaced time
    periods. Data is assumed to be in long format with time series of each
    individual stacked into one array. Panel can be unbalanced.

    Parameters
    ----------
    results : result instance
       result of a regression, uses results.model.exog and results.resid
       TODO: this should use wexog instead
    nlags : int or None
        Highest lag to include in kernel window. Currently, no default
        because the optimal length will depend on the number of observations
        per cross-sectional unit.
    groupidx : list of tuple
        each tuple should contain the start and end index for an individual.
        (groupidx might change in future).
    weights_func : callable
        weights_func is called with nlags as argument to get the kernel
        weights. default are Bartlett weights
    use_correction : 'cluster' or 'hac' or False
        If False, then no small sample correction is used.
        If 'cluster' (default), then the same correction as in cov_cluster is
        used.
        If 'hac', then the same correction as in single time series, cov_hac
        is used.


    Returns
    -------
    cov : ndarray, (k_vars, k_vars)
        HAC robust covariance matrix for parameter estimates

    Notes
    -----
    For nlags=0, this is just White covariance, cov_white.
    If kernel is uniform, `weights_uniform`, with nlags equal to the number
    of observations per unit in a balance panel, then cov_cluster and
    cov_hac_panel are identical.

    Tested against STATA `newey` command with same defaults.

    Options might change when other kernels besides Bartlett and uniform are
    available.

    """
