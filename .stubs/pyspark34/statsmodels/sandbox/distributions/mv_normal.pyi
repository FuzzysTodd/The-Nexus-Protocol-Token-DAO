from .extras import mvnormcdf as mvnormcdf
from _typeshed import Incomplete
from statsmodels.sandbox.distributions.multivariate import mvstdtprob as mvstdtprob

def expect_mc(dist, func=..., size: int = 50000):
    """calculate expected value of function by Monte Carlo integration

    Parameters
    ----------
    dist : distribution instance
        needs to have rvs defined as a method for drawing random numbers
    func : callable
        function for which expectation is calculated, this function needs to
        be vectorized, integration is over axis=0
    size : int
        number of random samples to use in the Monte Carlo integration,


    Notes
    -----
    this does not batch

    Returns
    -------
    expected value : ndarray
        return of function func integrated over axis=0 by MonteCarlo, this will
        have the same shape as the return of func without axis=0

    Examples
    --------

    integrate probability that both observations are negative

    >>> mvn = mve.MVNormal([0,0],2.)
    >>> mve.expect_mc(mvn, lambda x: (x<np.array([0,0])).all(-1), size=100000)
    0.25306000000000001

    get tail probabilities of marginal distribution (should be 0.1)

    >>> c = stats.norm.isf(0.05, scale=np.sqrt(2.))
    >>> expect_mc(mvn, lambda x: (np.abs(x)>np.array([c, c])), size=100000)
    array([ 0.09969,  0.0986 ])

    or calling the method

    >>> mvn.expect_mc(lambda x: (np.abs(x)>np.array([c, c])), size=100000)
    array([ 0.09937,  0.10075])


    """
def expect_mc_bounds(dist, func=..., size: int = 50000, lower: Incomplete | None = None, upper: Incomplete | None = None, conditional: bool = False, overfact: float = 1.2):
    """calculate expected value of function by Monte Carlo integration

    Parameters
    ----------
    dist : distribution instance
        needs to have rvs defined as a method for drawing random numbers
    func : callable
        function for which expectation is calculated, this function needs to
        be vectorized, integration is over axis=0
    size : int
        minimum number of random samples to use in the Monte Carlo integration,
        the actual number used can be larger because of oversampling.
    lower : None or array_like
        lower integration bounds, if None, then it is set to -inf
    upper : None or array_like
        upper integration bounds, if None, then it is set to +inf
    conditional : bool
        If true, then the expectation is conditional on being in within
        [lower, upper] bounds, otherwise it is unconditional
    overfact : float
        oversampling factor, the actual number of random variables drawn in
        each attempt are overfact * remaining draws. Extra draws are also
        used in the integration.


    Notes
    -----
    this does not batch

    Returns
    -------
    expected value : ndarray
        return of function func integrated over axis=0 by MonteCarlo, this will
        have the same shape as the return of func without axis=0

    Examples
    --------
    >>> mvn = mve.MVNormal([0,0],2.)
    >>> mve.expect_mc_bounds(mvn, lambda x: np.ones(x.shape[0]),
                                lower=[-10,-10],upper=[0,0])
    0.24990416666666668

    get 3 marginal moments with one integration

    >>> mvn = mve.MVNormal([0,0],1.)
    >>> mve.expect_mc_bounds(mvn, lambda x: np.dstack([x, x**2, x**3, x**4]),
        lower=[-np.inf,-np.inf], upper=[np.inf,np.inf])
    array([[  2.88629497e-03,   9.96706297e-01,  -2.51005344e-03,
              2.95240921e+00],
           [ -5.48020088e-03,   9.96004409e-01,  -2.23803072e-02,
              2.96289203e+00]])
    >>> from scipy import stats
    >>> [stats.norm.moment(i) for i in [1,2,3,4]]
    [0.0, 1.0, 0.0, 3.0]


    """
def bivariate_normal(x, mu, cov):
    """
    Bivariate Gaussian distribution for equal shape *X*, *Y*.

    See `bivariate normal
    <http://mathworld.wolfram.com/BivariateNormalDistribution.html>`_
    at mathworld.
    """

class BivariateNormal:
    mean: Incomplete
    cov: Incomplete
    nvars: int
    def __init__(self, mean, cov) -> None: ...
    def rvs(self, size: int = 1): ...
    def pdf(self, x): ...
    def logpdf(self, x): ...
    def cdf(self, x): ...
    def expect(self, func=..., lower=(-10, -10), upper=(10, 10)): ...
    def kl(self, other):
        """Kullback-Leibler divergence between this and another distribution

        int f(x) (log f(x) - log g(x)) dx

        where f is the pdf of self, and g is the pdf of other

        uses double integration with scipy.integrate.dblquad

        limits currently hardcoded

        """
    def kl_mc(self, other, size: int = 500000): ...

class MVElliptical:
    """Base Class for multivariate elliptical distributions, normal and t

    contains common initialization, and some common methods
    subclass needs to implement at least rvs and logpdf methods

    """
    extra_args: Incomplete
    mean: Incomplete
    sigma: Incomplete
    nvars: Incomplete
    sigmainv: Incomplete
    cholsigmainv: Incomplete
    logdetsigma: Incomplete
    def __init__(self, mean, sigma, *args, **kwds) -> None:
        """initialize instance

        Parameters
        ----------
        mean : array_like
            parameter mu (might be renamed), for symmetric distributions this
            is the mean
        sigma : array_like, 2d
            dispersion matrix, covariance matrix in normal distribution, but
            only proportional to covariance matrix in t distribution
        args : list
            distribution specific arguments, e.g. df for t distribution
        kwds : dict
            currently not used

        """
    def rvs(self, size: int = 1) -> None:
        """random variable

        Parameters
        ----------
        size : int or tuple
            the number and shape of random variables to draw.

        Returns
        -------
        rvs : ndarray
            the returned random variables with shape given by size and the
            dimension of the multivariate random vector as additional last
            dimension


        """
    def logpdf(self, x) -> None:
        """logarithm of probability density function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector

        Returns
        -------
        logpdf : float or array
            probability density value of each random vector


        this should be made to work with 2d x,
        with multivariate normal vector in each row and iid across rows
        does not work now because of dot in whiten

        """
    def cdf(self, x, **kwds) -> None:
        """cumulative distribution function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector
        kwds : dict
            contains options for the numerical calculation of the cdf

        Returns
        -------
        cdf : float or array
            probability density value of each random vector

        """
    def affine_transformed(self, shift, scale_matrix) -> None:
        """affine transformation define in subclass because of distribution
        specific restrictions"""
    def whiten(self, x):
        """
        whiten the data by linear transformation

        Parameters
        ----------
        x : array_like, 1d or 2d
            Data to be whitened, if 2d then each row contains an independent
            sample of the multivariate random vector

        Returns
        -------
        np.dot(x, self.cholsigmainv.T)

        Notes
        -----
        This only does rescaling, it does not subtract the mean, use standardize
        for this instead

        See Also
        --------
        standardize : subtract mean and rescale to standardized random variable.
        """
    def pdf(self, x):
        """probability density function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector

        Returns
        -------
        pdf : float or array
            probability density value of each random vector

        """
    def standardize(self, x):
        """standardize the random variable, i.e. subtract mean and whiten

        Parameters
        ----------
        x : array_like, 1d or 2d
            Data to be whitened, if 2d then each row contains an independent
            sample of the multivariate random vector

        Returns
        -------
        np.dot(x - self.mean, self.cholsigmainv.T)

        Notes
        -----


        See Also
        --------
        whiten : rescale random variable, standardize without subtracting mean.


        """
    def standardized(self):
        """return new standardized MVNormal instance
        """
    def normalize(self, x):
        """normalize the random variable, i.e. subtract mean and rescale

        The distribution will have zero mean and sigma equal to correlation

        Parameters
        ----------
        x : array_like, 1d or 2d
            Data to be whitened, if 2d then each row contains an independent
            sample of the multivariate random vector

        Returns
        -------
        (x - self.mean)/std_sigma

        Notes
        -----


        See Also
        --------
        whiten : rescale random variable, standardize without subtracting mean.


        """
    def normalized(self, demeaned: bool = True):
        """return a normalized distribution where sigma=corr

        if demeaned is True, then mean will be set to zero

        """
    def normalized2(self, demeaned: bool = True):
        """return a normalized distribution where sigma=corr



        second implementation for testing affine transformation
        """
    @property
    def std(self):
        """standard deviation, square root of diagonal elements of cov
        """
    @property
    def std_sigma(self):
        """standard deviation, square root of diagonal elements of sigma
        """
    @property
    def corr(self):
        """correlation matrix"""
    expect_mc = expect_mc
    def marginal(self, indices):
        """return marginal distribution for variables given by indices

        this should be correct for normal and t distribution

        Parameters
        ----------
        indices : array_like, int
            list of indices of variables in the marginal distribution

        Returns
        -------
        mvdist : instance
            new instance of the same multivariate distribution class that
            contains the marginal distribution of the variables given in
            indices

        """

class MVNormal0:
    """Class for Multivariate Normal Distribution

    original full version, kept for testing, new version inherits from
    MVElliptical

    uses Cholesky decomposition of covariance matrix for the transformation
    of the data

    """
    mean: Incomplete
    cov: Incomplete
    nvars: Incomplete
    covinv: Incomplete
    cholcovinv: Incomplete
    logdetcov: Incomplete
    def __init__(self, mean, cov) -> None: ...
    def whiten(self, x):
        """
        whiten the data by linear transformation

        Parameters
        ----------
        X : array_like, 1d or 2d
            Data to be whitened, if 2d then each row contains an independent
            sample of the multivariate random vector

        Returns
        -------
        np.dot(x, self.cholcovinv.T)

        Notes
        -----
        This only does rescaling, it does not subtract the mean, use standardize
        for this instead

        See Also
        --------
        standardize : subtract mean and rescale to standardized random variable.
        """
    def rvs(self, size: int = 1):
        """random variable

        Parameters
        ----------
        size : int or tuple
            the number and shape of random variables to draw.

        Returns
        -------
        rvs : ndarray
            the returned random variables with shape given by size and the
            dimension of the multivariate random vector as additional last
            dimension

        Notes
        -----
        uses numpy.random.multivariate_normal directly

        """
    def pdf(self, x):
        """probability density function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector

        Returns
        -------
        pdf : float or array
            probability density value of each random vector

        """
    def logpdf(self, x):
        """logarithm of probability density function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector

        Returns
        -------
        logpdf : float or array
            probability density value of each random vector


        this should be made to work with 2d x,
        with multivariate normal vector in each row and iid across rows
        does not work now because of dot in whiten

        """
    expect_mc = expect_mc

class MVNormal(MVElliptical):
    """Class for Multivariate Normal Distribution

    uses Cholesky decomposition of covariance matrix for the transformation
    of the data

    """
    def rvs(self, size: int = 1):
        """random variable

        Parameters
        ----------
        size : int or tuple
            the number and shape of random variables to draw.

        Returns
        -------
        rvs : ndarray
            the returned random variables with shape given by size and the
            dimension of the multivariate random vector as additional last
            dimension

        Notes
        -----
        uses numpy.random.multivariate_normal directly

        """
    def logpdf(self, x):
        """logarithm of probability density function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector

        Returns
        -------
        logpdf : float or array
            probability density value of each random vector


        this should be made to work with 2d x,
        with multivariate normal vector in each row and iid across rows
        does not work now because of dot in whiten

        """
    def cdf(self, x, **kwds):
        """cumulative distribution function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector
        kwds : dict
            contains options for the numerical calculation of the cdf

        Returns
        -------
        cdf : float or array
            probability density value of each random vector

        """
    @property
    def cov(self):
        """covariance matrix"""
    def affine_transformed(self, shift, scale_matrix):
        """return distribution of an affine transform

        for full rank scale_matrix only

        Parameters
        ----------
        shift : array_like
            shift of mean
        scale_matrix : array_like
            linear transformation matrix

        Returns
        -------
        mvt : instance of MVNormal
            instance of multivariate normal distribution given by affine
            transformation

        Notes
        -----
        the affine transformation is defined by
        y = a + B x

        where a is shift,
        B is a scale matrix for the linear transformation

        Notes
        -----
        This should also work to select marginal distributions, but not
        tested for this case yet.

        currently only tested because it's called by standardized

        """
    def conditional(self, indices, values):
        """return conditional distribution

        indices are the variables to keep, the complement is the conditioning
        set
        values are the values of the conditioning variables

        \\bar{\\mu} = \\mu_1 + \\Sigma_{12} \\Sigma_{22}^{-1} \\left( a - \\mu_2 \\right)

        and covariance matrix

        \\overline{\\Sigma} = \\Sigma_{11} - \\Sigma_{12} \\Sigma_{22}^{-1} \\Sigma_{21}.T

        Parameters
        ----------
        indices : array_like, int
            list of indices of variables in the marginal distribution
        given : array_like
            values of the conditioning variables

        Returns
        -------
        mvn : instance of MVNormal
            new instance of the MVNormal class that contains the conditional
            distribution of the variables given in indices for given
             values of the excluded variables.


        """

np_log: Incomplete
np_pi: Incomplete
sps_gamln: Incomplete

class MVT(MVElliptical):
    extra_args: Incomplete
    df: Incomplete
    def __init__(self, mean, sigma, df) -> None:
        """initialize instance

        Parameters
        ----------
        mean : array_like
            parameter mu (might be renamed), for symmetric distributions this
            is the mean
        sigma : array_like, 2d
            dispersion matrix, covariance matrix in normal distribution, but
            only proportional to covariance matrix in t distribution
        args : list
            distribution specific arguments, e.g. df for t distribution
        kwds : dict
            currently not used

        """
    def rvs(self, size: int = 1):
        """random variables with Student T distribution

        Parameters
        ----------
        size : int or tuple
            the number and shape of random variables to draw.

        Returns
        -------
        rvs : ndarray
            the returned random variables with shape given by size and the
            dimension of the multivariate random vector as additional last
            dimension
            - TODO: Not sure if this works for size tuples with len>1.

        Notes
        -----
        generated as a chi-square mixture of multivariate normal random
        variables.
        does this require df>2 ?


        """
    def logpdf(self, x):
        """logarithm of probability density function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector

        Returns
        -------
        logpdf : float or array
            probability density value of each random vector

        """
    def cdf(self, x, **kwds):
        """cumulative distribution function

        Parameters
        ----------
        x : array_like
            can be 1d or 2d, if 2d, then each row is taken as independent
            multivariate random vector
        kwds : dict
            contains options for the numerical calculation of the cdf

        Returns
        -------
        cdf : float or array
            probability density value of each random vector

        """
    @property
    def cov(self):
        """covariance matrix

        The covariance matrix for the t distribution does not exist for df<=2,
        and is equal to sigma * df/(df-2) for df>2

        """
    def affine_transformed(self, shift, scale_matrix):
        """return distribution of a full rank affine transform

        for full rank scale_matrix only

        Parameters
        ----------
        shift : array_like
            shift of mean
        scale_matrix : array_like
            linear transformation matrix

        Returns
        -------
        mvt : instance of MVT
            instance of multivariate t distribution given by affine
            transformation


        Notes
        -----

        This checks for eigvals<=0, so there are possible problems for cases
        with positive eigenvalues close to zero.

        see: http://www.statlect.com/mcdstu1.htm

        I'm not sure about general case, non-full rank transformation are not
        multivariate t distributed.

        y = a + B x

        where a is shift,
        B is full rank scale matrix with same dimension as sigma

        """

def quad2d(func=..., lower=(-10, -10), upper=(10, 10)): ...
