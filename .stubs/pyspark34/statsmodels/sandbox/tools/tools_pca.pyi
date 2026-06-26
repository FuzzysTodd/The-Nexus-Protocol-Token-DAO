__all__ = ['pca', 'pcasvd']

def pca(data, keepdim: int = 0, normalize: int = 0, demean: bool = True):
    """principal components with eigenvector decomposition
    similar to princomp in matlab

    Parameters
    ----------
    data : ndarray, 2d
        data with observations by rows and variables in columns
    keepdim : int
        number of eigenvectors to keep
        if keepdim is zero, then all eigenvectors are included
    normalize : bool
        if true, then eigenvectors are normalized by sqrt of eigenvalues
    demean : bool
        if true, then the column mean is subtracted from the data

    Returns
    -------
    xreduced : ndarray, 2d, (nobs, nvars)
        projection of the data x on the kept eigenvectors
    factors : ndarray, 2d, (nobs, nfactors)
        factor matrix, given by np.dot(x, evecs)
    evals : ndarray, 2d, (nobs, nfactors)
        eigenvalues
    evecs : ndarray, 2d, (nobs, nfactors)
        eigenvectors, normalized if normalize is true

    Notes
    -----

    See Also
    --------
    pcasvd : principal component analysis using svd

    """
def pcasvd(data, keepdim: int = 0, demean: bool = True):
    """principal components with svd

    Parameters
    ----------
    data : ndarray, 2d
        data with observations by rows and variables in columns
    keepdim : int
        number of eigenvectors to keep
        if keepdim is zero, then all eigenvectors are included
    demean : bool
        if true, then the column mean is subtracted from the data

    Returns
    -------
    xreduced : ndarray, 2d, (nobs, nvars)
        projection of the data x on the kept eigenvectors
    factors : ndarray, 2d, (nobs, nfactors)
        factor matrix, given by np.dot(x, evecs)
    evals : ndarray, 2d, (nobs, nfactors)
        eigenvalues
    evecs : ndarray, 2d, (nobs, nfactors)
        eigenvectors, normalized if normalize is true

    See Also
    --------
    pca : principal component analysis using eigenvector decomposition

    Notes
    -----
    This does not have yet the normalize option of pca.

    """
