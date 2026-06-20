from _typeshed import Incomplete

def kernel(d1, d2, r: Incomplete | None = None, weights: Incomplete | None = None):
    """general product kernel

    hardcoded split for the example:
        cat1 is continuous (time), other categories are discrete

    weights is e.g. Bartlett for cat1
    r is (0,1) indicator vector for boolean weights 1{d1_i == d2_i}

    returns boolean if no continuous weights are used
    """
def aggregate_cov(x, d, r: Incomplete | None = None, weights: Incomplete | None = None):
    """sum of outer procuct over groups and time selected by r

    This is for a generic reference implementation, it uses a nobs-nobs double
    loop.

    Parameters
    ----------
    x : ndarray, (nobs,) or (nobs, k_vars)
        data, for robust standard error calculation, this is array of x_i * u_i
    d : ndarray, (nobs, n_groups)
        integer group labels, each column contains group (or time) indices
    r : ndarray, (n_groups,)
        indicator for which groups to include. If r[i] is zero, then
        this group is ignored. If r[i] is not zero, then the cluster robust
        standard errors include this group.
    weights : ndarray
        weights if the first group dimension uses a HAC kernel

    Returns
    -------
    cov : ndarray (k_vars, k_vars) or scalar
        covariance matrix aggregates over group kernels
    count : int
        number of terms added in sum, mainly returned for cross-checking

    Notes
    -----
    This uses `kernel` to calculate the weighted distance between two
    observations.

    """
def weights_bartlett(nlags): ...
def S_all_hac(x, d, nlags: int = 1):
    """HAC independent of categorical group membership
    """
def S_within_hac(x, d, nlags: int = 1, groupidx: int = 1):
    """HAC for observations within a categorical group
    """
def S_cluster(x, d, groupidx=[1]): ...
def S_white(x, d):
    """simple white heteroscedasticity robust covariance
    note: calculating this way is very inefficient, just for cross-checking
    """
