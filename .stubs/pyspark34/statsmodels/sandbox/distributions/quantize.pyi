from statsmodels.compat.python import lmap as lmap

def prob_bv_rectangle(lower, upper, cdf):
    """helper function for probability of a rectangle in a bivariate distribution

    Parameters
    ----------
    lower : array_like
        tuple of lower integration bounds
    upper : array_like
        tuple of upper integration bounds
    cdf : callable
        cdf(x,y), cumulative distribution function of bivariate distribution


    how does this generalize to more than 2 variates ?
    """
def prob_mv_grid(bins, cdf, axis: int = -1):
    """helper function for probability of a rectangle grid in a multivariate distribution

    how does this generalize to more than 2 variates ?

    bins : tuple
        tuple of bin edges, currently it is assumed that they broadcast
        correctly

    """
def prob_quantize_cdf(binsx, binsy, cdf):
    """quantize a continuous distribution given by a cdf

    Parameters
    ----------
    binsx : array_like, 1d
        binedges

    """
def prob_quantize_cdf_old(binsx, binsy, cdf):
    """quantize a continuous distribution given by a cdf

    old version without precomputing cdf values

    Parameters
    ----------
    binsx : array_like, 1d
        binedges

    """
