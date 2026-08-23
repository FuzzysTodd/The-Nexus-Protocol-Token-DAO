from _typeshed import Incomplete
from statsmodels.tools.sm_exceptions import EstimationWarning as EstimationWarning, ValueWarning as ValueWarning
from statsmodels.tools.validation import array_like as array_like, bool_like as bool_like, float_like as float_like, int_like as int_like, string_like as string_like

class PCA:
    '''
    Principal Component Analysis

    Parameters
    ----------
    data : array_like
        Variables in columns, observations in rows.
    ncomp : int, optional
        Number of components to return.  If None, returns the as many as the
        smaller of the number of rows or columns in data.
    standardize : bool, optional
        Flag indicating to use standardized data with mean 0 and unit
        variance.  standardized being True implies demean.  Using standardized
        data is equivalent to computing principal components from the
        correlation matrix of data.
    demean : bool, optional
        Flag indicating whether to demean data before computing principal
        components.  demean is ignored if standardize is True. Demeaning data
        but not standardizing is equivalent to computing principal components
        from the covariance matrix of data.
    normalize : bool , optional
        Indicates whether to normalize the factors to have unit inner product.
        If False, the loadings will have unit inner product.
    gls : bool, optional
        Flag indicating to implement a two-step GLS estimator where
        in the first step principal components are used to estimate residuals,
        and then the inverse residual variance is used as a set of weights to
        estimate the final principal components.  Setting gls to True requires
        ncomp to be less then the min of the number of rows or columns.
    weights : ndarray, optional
        Series weights to use after transforming data according to standardize
        or demean when computing the principal components.
    method : str, optional
        Sets the linear algebra routine used to compute eigenvectors:

        * \'svd\' uses a singular value decomposition (default).
        * \'eig\' uses an eigenvalue decomposition of a quadratic form
        * \'nipals\' uses the NIPALS algorithm and can be faster than SVD when
          ncomp is small and nvars is large. See notes about additional changes
          when using NIPALS.
    missing : {str, None}
        Method for missing data.  Choices are:

        * \'drop-row\' - drop rows with missing values.
        * \'drop-col\' - drop columns with missing values.
        * \'drop-min\' - drop either rows or columns, choosing by data retention.
        * \'fill-em\' - use EM algorithm to fill missing value.  ncomp should be
          set to the number of factors required.
        * `None` raises if data contains NaN values.
    tol : float, optional
        Tolerance to use when checking for convergence when using NIPALS.
    max_iter : int, optional
        Maximum iterations when using NIPALS.
    tol_em : float
        Tolerance to use when checking for convergence of the EM algorithm.
    max_em_iter : int
        Maximum iterations for the EM algorithm.
    svd_full_matrices : bool, optional
        If the \'svd\' method is selected, this flag is used to set the parameter
        \'full_matrices\' in the singular value decomposition method. Is set to
        False by default.

    Attributes
    ----------
    factors : array or DataFrame
        nobs by ncomp array of principal components (scores)
    scores :  array or DataFrame
        nobs by ncomp array of principal components - identical to factors
    loadings : array or DataFrame
        ncomp by nvar array of principal component loadings for constructing
        the factors
    coeff : array or DataFrame
        nvar by ncomp array of principal component loadings for constructing
        the projections
    projection : array or DataFrame
        nobs by var array containing the projection of the data onto the ncomp
        estimated factors
    rsquare : array or Series
        ncomp array where the element in the ith position is the R-square
        of including the fist i principal components.  Note: values are
        calculated on the transformed data, not the original data
    ic : array or DataFrame
        ncomp by 3 array containing the Bai and Ng (2003) Information
        criteria.  Each column is a different criteria, and each row
        represents the number of included factors.
    eigenvals : array or Series
        nvar array of eigenvalues
    eigenvecs : array or DataFrame
        nvar by nvar array of eigenvectors
    weights : ndarray
        nvar array of weights used to compute the principal components,
        normalized to unit length
    transformed_data : ndarray
        Standardized, demeaned and weighted data used to compute
        principal components and related quantities
    cols : ndarray
        Array of indices indicating columns used in the PCA
    rows : ndarray
        Array of indices indicating rows used in the PCA

    Notes
    -----
    The default options perform principal component analysis on the
    demeaned, unit variance version of data.  Setting standardize to False
    will instead only demean, and setting both standardized and
    demean to False will not alter the data.

    Once the data have been transformed, the following relationships hold when
    the number of components (ncomp) is the same as tne minimum of the number
    of observation or the number of variables.

    .. math:

        X\' X = V \\Lambda V\'

    .. math:

        F = X V

    .. math:

        X = F V\'

    where X is the `data`, F is the array of principal components (`factors`
    or `scores`), and V is the array of eigenvectors (`loadings`) and V\' is
    the array of factor coefficients (`coeff`).

    When weights are provided, the principal components are computed from the
    modified data

    .. math:

        \\Omega^{-\\frac{1}{2}} X

    where :math:`\\Omega` is a diagonal matrix composed of the weights. For
    example, when using the GLS version of PCA, the elements of :math:`\\Omega`
    will be the inverse of the variances of the residuals from

    .. math:

        X - F V\'

    where the number of factors is less than the rank of X

    References
    ----------
    .. [*] J. Bai and S. Ng, "Determining the number of factors in approximate
       factor models," Econometrica, vol. 70, number 1, pp. 191-221, 2002

    Examples
    --------
    Basic PCA using the correlation matrix of the data

    >>> import numpy as np
    >>> from statsmodels.multivariate.pca import PCA
    >>> x = np.random.randn(100)[:, None]
    >>> x = x + np.random.randn(100, 100)
    >>> pc = PCA(x)

    Note that the principal components are computed using a SVD and so the
    correlation matrix is never constructed, unless method=\'eig\'.

    PCA using the covariance matrix of the data

    >>> pc = PCA(x, standardize=False)

    Limiting the number of factors returned to 1 computed using NIPALS

    >>> pc = PCA(x, ncomp=1, method=\'nipals\')
    >>> pc.factors.shape
    (100, 1)
    '''
    data: Incomplete
    weights: Incomplete
    rows: Incomplete
    cols: Incomplete
    transformed_data: Incomplete
    scores: Incomplete
    loadings: Incomplete
    coeff: Incomplete
    eigenvals: Incomplete
    eigenvecs: Incomplete
    projection: Incomplete
    rsquare: Incomplete
    ic: Incomplete
    def __init__(self, data, ncomp: Incomplete | None = None, standardize: bool = True, demean: bool = True, normalize: bool = True, gls: bool = False, weights: Incomplete | None = None, method: str = 'svd', missing: Incomplete | None = None, tol: float = 5e-08, max_iter: int = 1000, tol_em: float = 5e-08, max_em_iter: int = 100, svd_full_matrices: bool = False) -> None: ...
    def project(self, ncomp: Incomplete | None = None, transform: bool = True, unweight: bool = True):
        """
        Project series onto a specific number of factors.

        Parameters
        ----------
        ncomp : int, optional
            Number of components to use.  If omitted, all components
            initially computed are used.
        transform : bool, optional
            Flag indicating whether to return the projection in the original
            space of the data (True, default) or in the space of the
            standardized/demeaned data.
        unweight : bool, optional
            Flag indicating whether to undo the effects of the estimation
            weights.

        Returns
        -------
        array_like
            The nobs by nvar array of the projection onto ncomp factors.

        Notes
        -----
        """
    def plot_scree(self, ncomp: Incomplete | None = None, log_scale: bool = True, cumulative: bool = False, ax: Incomplete | None = None):
        """
        Plot of the ordered eigenvalues

        Parameters
        ----------
        ncomp : int, optional
            Number of components ot include in the plot.  If None, will
            included the same as the number of components computed
        log_scale : boot, optional
            Flag indicating whether ot use a log scale for the y-axis
        cumulative : bool, optional
            Flag indicating whether to plot the eigenvalues or cumulative
            eigenvalues
        ax : AxesSubplot, optional
            An axes on which to draw the graph.  If omitted, new a figure
            is created

        Returns
        -------
        matplotlib.figure.Figure
            The handle to the figure.
        """
    def plot_rsquare(self, ncomp: Incomplete | None = None, ax: Incomplete | None = None):
        """
        Box plots of the individual series R-square against the number of PCs.

        Parameters
        ----------
        ncomp : int, optional
            Number of components ot include in the plot.  If None, will
            plot the minimum of 10 or the number of computed components.
        ax : AxesSubplot, optional
            An axes on which to draw the graph.  If omitted, new a figure
            is created.

        Returns
        -------
        matplotlib.figure.Figure
            The handle to the figure.
        """

def pca(data, ncomp: Incomplete | None = None, standardize: bool = True, demean: bool = True, normalize: bool = True, gls: bool = False, weights: Incomplete | None = None, method: str = 'svd'):
    """
    Perform Principal Component Analysis (PCA).

    Parameters
    ----------
    data : ndarray
        Variables in columns, observations in rows.
    ncomp : int, optional
        Number of components to return.  If None, returns the as many as the
        smaller to the number of rows or columns of data.
    standardize : bool, optional
        Flag indicating to use standardized data with mean 0 and unit
        variance.  standardized being True implies demean.
    demean : bool, optional
        Flag indicating whether to demean data before computing principal
        components.  demean is ignored if standardize is True.
    normalize : bool , optional
        Indicates whether th normalize the factors to have unit inner
        product.  If False, the loadings will have unit inner product.
    gls : bool, optional
        Flag indicating to implement a two-step GLS estimator where
        in the first step principal components are used to estimate residuals,
        and then the inverse residual variance is used as a set of weights to
        estimate the final principal components
    weights : ndarray, optional
        Series weights to use after transforming data according to standardize
        or demean when computing the principal components.
    method : str, optional
        Determines the linear algebra routine uses.  'eig', the default,
        uses an eigenvalue decomposition. 'svd' uses a singular value
        decomposition.

    Returns
    -------
    factors : {ndarray, DataFrame}
        Array (nobs, ncomp) of principal components (also known as scores).
    loadings : {ndarray, DataFrame}
        Array (ncomp, nvar) of principal component loadings for constructing
        the factors.
    projection : {ndarray, DataFrame}
        Array (nobs, nvar) containing the projection of the data onto the ncomp
        estimated factors.
    rsquare : {ndarray, Series}
        Array (ncomp,) where the element in the ith position is the R-square
        of including the fist i principal components.  The values are
        calculated on the transformed data, not the original data.
    ic : {ndarray, DataFrame}
        Array (ncomp, 3) containing the Bai and Ng (2003) Information
        criteria.  Each column is a different criteria, and each row
        represents the number of included factors.
    eigenvals : {ndarray, Series}
        Array of eigenvalues (nvar,).
    eigenvecs : {ndarray, DataFrame}
        Array of eigenvectors. (nvar, nvar).

    Notes
    -----
    This is a simple function wrapper around the PCA class. See PCA for
    more information and additional methods.
    """
