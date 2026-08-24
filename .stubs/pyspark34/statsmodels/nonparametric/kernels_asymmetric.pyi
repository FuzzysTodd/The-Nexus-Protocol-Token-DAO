from _typeshed import Incomplete

doc_params: str

def pdf_kernel_asym(x, sample, bw, kernel_type, weights: Incomplete | None = None, batch_size: int = 10):
    '''Density estimate based on asymmetric kernel.

    Parameters
    ----------
    x : array_like, float
        Points for which density is evaluated. ``x`` can be scalar or 1-dim.
    sample : ndarray, 1-d
        Sample from which kernel estimate is computed.
    bw : float
        Bandwidth parameter, there is currently no default value for it.
    kernel_type : str or callable
        Kernel name or kernel function.
        Currently supported kernel names are "beta", "beta2", "gamma",
        "gamma2", "bs", "invgamma", "invgauss", "lognorm", "recipinvgauss" and
        "weibull".
    weights : None or ndarray
        If weights is not None, then kernel for sample points are weighted
        by it. No weights corresponds to uniform weighting of each component
        with 1 / nobs, where nobs is the size of `sample`.
    batch_size : float
        If x is an 1-dim array, then points can be evaluated in vectorized
        form. To limit the amount of memory, a loop can work in batches.
        The number of batches is determined so that the intermediate array
        sizes are limited by

        ``np.size(batch) * len(sample) < batch_size * 1000``.

        Default is to have at most 10000 elements in intermediate arrays.

    Returns
    -------
    pdf : float or ndarray
        Estimate of pdf at points x. ``pdf`` has the same size or shape as x.
    '''
def cdf_kernel_asym(x, sample, bw, kernel_type, weights: Incomplete | None = None, batch_size: int = 10):
    '''Estimate of cumulative distribution based on asymmetric kernel.

    Parameters
    ----------
    x : array_like, float
        Points for which density is evaluated. ``x`` can be scalar or 1-dim.
    sample : ndarray, 1-d
        Sample from which kernel estimate is computed.
    bw : float
        Bandwidth parameter, there is currently no default value for it.
    kernel_type : str or callable
        Kernel name or kernel function.
        Currently supported kernel names are "beta", "beta2", "gamma",
        "gamma2", "bs", "invgamma", "invgauss", "lognorm", "recipinvgauss" and
        "weibull".
    weights : None or ndarray
        If weights is not None, then kernel for sample points are weighted
        by it. No weights corresponds to uniform weighting of each component
        with 1 / nobs, where nobs is the size of `sample`.
    batch_size : float
        If x is an 1-dim array, then points can be evaluated in vectorized
        form. To limit the amount of memory, a loop can work in batches.
        The number of batches is determined so that the intermediate array
        sizes are limited by

        ``np.size(batch) * len(sample) < batch_size * 1000``.

        Default is to have at most 10000 elements in intermediate arrays.

    Returns
    -------
    cdf : float or ndarray
        Estimate of cdf at points x. ``cdf`` has the same size or shape as x.
    '''
def kernel_pdf_beta(x, sample, bw): ...
def kernel_cdf_beta(x, sample, bw): ...
def kernel_pdf_beta2(x, sample, bw): ...
def kernel_cdf_beta2(x, sample, bw): ...
def kernel_pdf_gamma(x, sample, bw): ...
def kernel_cdf_gamma(x, sample, bw): ...
def kernel_pdf_gamma2(x, sample, bw): ...
def kernel_cdf_gamma2(x, sample, bw): ...
def kernel_pdf_invgamma(x, sample, bw): ...
def kernel_cdf_invgamma(x, sample, bw): ...
def kernel_pdf_invgauss(x, sample, bw): ...
def kernel_pdf_invgauss_(x, sample, bw):
    """Inverse gaussian kernel density, explicit formula.

    Scaillet 2004
    """
def kernel_cdf_invgauss(x, sample, bw): ...
def kernel_pdf_recipinvgauss(x, sample, bw): ...
def kernel_pdf_recipinvgauss_(x, sample, bw):
    """Reciprocal inverse gaussian kernel density, explicit formula.

    Scaillet 2004
    """
def kernel_cdf_recipinvgauss(x, sample, bw): ...
def kernel_pdf_bs(x, sample, bw): ...
def kernel_cdf_bs(x, sample, bw): ...
def kernel_pdf_lognorm(x, sample, bw): ...
def kernel_cdf_lognorm(x, sample, bw): ...
def kernel_pdf_lognorm_(x, sample, bw):
    """Log-normal kernel for density, pdf, estimation, explicit formula.

    Jin, Kawczak 2003
    """
def kernel_pdf_weibull(x, sample, bw): ...
def kernel_cdf_weibull(x, sample, bw): ...

kernel_dict_cdf: Incomplete
kernel_dict_pdf: Incomplete
