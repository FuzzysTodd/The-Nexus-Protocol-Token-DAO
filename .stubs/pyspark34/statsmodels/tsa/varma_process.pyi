from _typeshed import Incomplete
from statsmodels.tsa.tsatools import lagmat as lagmat

def varfilter(x, a):
    """apply an autoregressive filter to a series x

    Warning: I just found out that convolve does not work as I
       thought, this likely does not work correctly for
       nvars>3


    x can be 2d, a can be 1d, 2d, or 3d

    Parameters
    ----------
    x : array_like
        data array, 1d or 2d, if 2d then observations in rows
    a : array_like
        autoregressive filter coefficients, ar lag polynomial
        see Notes

    Returns
    -------
    y : ndarray, 2d
        filtered array, number of columns determined by x and a

    Notes
    -----

    In general form this uses the linear filter ::

        y = a(L)x

    where
    x : nobs, nvars
    a : nlags, nvars, npoly

    Depending on the shape and dimension of a this uses different
    Lag polynomial arrays

    case 1 : a is 1d or (nlags,1)
        one lag polynomial is applied to all variables (columns of x)
    case 2 : a is 2d, (nlags, nvars)
        each series is independently filtered with its own
        lag polynomial, uses loop over nvar
    case 3 : a is 3d, (nlags, nvars, npoly)
        the ith column of the output array is given by the linear filter
        defined by the 2d array a[:,:,i], i.e. ::

            y[:,i] = a(.,.,i)(L) * x
            y[t,i] = sum_p sum_j a(p,j,i)*x(t-p,j)
                     for p = 0,...nlags-1, j = 0,...nvars-1,
                     for all t >= nlags


    Note: maybe convert to axis=1, Not

    TODO: initial conditions

    """
def varinversefilter(ar, nobs, version: int = 1):
    """creates inverse ar filter (MA representation) recursively

    The VAR lag polynomial is defined by ::

        ar(L) y_t = u_t  or
        y_t = -ar_{-1}(L) y_{t-1} + u_t

    the returned lagpolynomial is arinv(L)=ar^{-1}(L) in ::

        y_t = arinv(L) u_t



    Parameters
    ----------
    ar : ndarray, (nlags,nvars,nvars)
        matrix lagpolynomial, currently no exog
        first row should be identity

    Returns
    -------
    arinv : ndarray, (nobs,nvars,nvars)


    Notes
    -----

    """
def vargenerate(ar, u, initvalues: Incomplete | None = None):
    """generate an VAR process with errors u

    similar to gauss
    uses loop

    Parameters
    ----------
    ar : array (nlags,nvars,nvars)
        matrix lagpolynomial
    u : array (nobs,nvars)
        exogenous variable, error term for VAR

    Returns
    -------
    sar : array (1+nobs,nvars)
        sample of var process, inverse filtered u
        does not trim initial condition y_0 = 0

    Examples
    --------
    # generate random sample of VAR
    nobs, nvars = 10, 2
    u = numpy.random.randn(nobs,nvars)
    a21 = np.array([[[ 1. ,  0. ],
                     [ 0. ,  1. ]],

                    [[-0.8,  0. ],
                     [ 0.,  -0.6]]])
    vargenerate(a21,u)

    # Impulse Response to an initial shock to the first variable
    imp = np.zeros((nobs, nvars))
    imp[0,0] = 1
    vargenerate(a21,imp)

    """
def padone(x, front: int = 0, back: int = 0, axis: int = 0, fillvalue: int = 0):
    """pad with zeros along one axis, currently only axis=0


    can be used sequentially to pad several axis

    Examples
    --------
    >>> padone(np.ones((2,3)),1,3,axis=1)
    array([[ 0.,  1.,  1.,  1.,  0.,  0.,  0.],
           [ 0.,  1.,  1.,  1.,  0.,  0.,  0.]])

    >>> padone(np.ones((2,3)),1,1, fillvalue=np.nan)
    array([[ NaN,  NaN,  NaN],
           [  1.,   1.,   1.],
           [  1.,   1.,   1.],
           [ NaN,  NaN,  NaN]])
    """
def trimone(x, front: int = 0, back: int = 0, axis: int = 0):
    """trim number of array elements along one axis


    Examples
    --------
    >>> xp = padone(np.ones((2,3)),1,3,axis=1)
    >>> xp
    array([[ 0.,  1.,  1.,  1.,  0.,  0.,  0.],
           [ 0.,  1.,  1.,  1.,  0.,  0.,  0.]])
    >>> trimone(xp,1,3,1)
    array([[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]])
    """
def ar2full(ar):
    """make reduced lagpolynomial into a right side lagpoly array
    """
def ar2lhs(ar):
    """convert full (rhs) lagpolynomial into a reduced, left side lagpoly array

    this is mainly a reminder about the definition
    """

class _Var:
    """obsolete VAR class, use tsa.VAR instead, for internal use only


    Examples
    --------

    >>> v = Var(ar2s)
    >>> v.fit(1)
    >>> v.arhat
    array([[[ 1.        ,  0.        ],
            [ 0.        ,  1.        ]],

           [[-0.77784898,  0.01726193],
            [ 0.10733009, -0.78665335]]])

    """
    y: Incomplete
    def __init__(self, y) -> None: ...
    nlags: Incomplete
    yred: Incomplete
    xred: Incomplete
    estresults: Incomplete
    arlhs: Incomplete
    arhat: Incomplete
    rss: Incomplete
    xredrank: Incomplete
    def fit(self, nlags) -> None:
        """estimate parameters using ols

        Parameters
        ----------
        nlags : int
            number of lags to include in regression, same for all variables

        Returns
        -------
        None, but attaches

        arhat : array (nlags, nvar, nvar)
            full lag polynomial array
        arlhs : array (nlags-1, nvar, nvar)
            reduced lag polynomial for left hand side
        other statistics as returned by linalg.lstsq : need to be completed



        This currently assumes all parameters are estimated without restrictions.
        In this case SUR is identical to OLS

        estimation results are attached to the class instance


        """
    yhat: Incomplete
    def predict(self):
        """calculate estimated timeseries (yhat) for sample

        """
    paramcov: Incomplete
    def covmat(self) -> None:
        """ covariance matrix of estimate
        # not sure it's correct, need to check orientation everywhere
        # looks ok, display needs getting used to
        >>> v.rss[None,None,:]*np.linalg.inv(np.dot(v.xred.T,v.xred))[:,:,None]
        array([[[ 0.37247445,  0.32210609],
                [ 0.1002642 ,  0.08670584]],

               [[ 0.1002642 ,  0.08670584],
                [ 0.45903637,  0.39696255]]])
        >>>
        >>> v.rss[0]*np.linalg.inv(np.dot(v.xred.T,v.xred))
        array([[ 0.37247445,  0.1002642 ],
               [ 0.1002642 ,  0.45903637]])
        >>> v.rss[1]*np.linalg.inv(np.dot(v.xred.T,v.xred))
        array([[ 0.32210609,  0.08670584],
               [ 0.08670584,  0.39696255]])
       """
    def forecast(self, horiz: int = 1, u: Incomplete | None = None):
        """calculates forcast for horiz number of periods at end of sample

        Parameters
        ----------
        horiz : int (optional, default=1)
            forecast horizon
        u : array (horiz, nvars)
            error term for forecast periods. If None, then u is zero.

        Returns
        -------
        yforecast : array (nobs+horiz, nvars)
            this includes the sample and the forecasts
        """

class VarmaPoly:
    """class to keep track of Varma polynomial format


    Examples
    --------

    ar23 = np.array([[[ 1. ,  0. ],
                     [ 0. ,  1. ]],

                    [[-0.6,  0. ],
                     [ 0.2, -0.6]],

                    [[-0.1,  0. ],
                     [ 0.1, -0.1]]])

    ma22 = np.array([[[ 1. ,  0. ],
                     [ 0. ,  1. ]],

                    [[ 0.4,  0. ],
                     [ 0.2, 0.3]]])


    """
    ar: Incomplete
    ma: Incomplete
    isstructured: Incomplete
    isindependent: bool
    malags: Incomplete
    hasexog: Incomplete
    arm1: Incomplete
    def __init__(self, ar, ma: Incomplete | None = None) -> None: ...
    def vstack(self, a: Incomplete | None = None, name: str = 'ar'):
        """stack lagpolynomial vertically in 2d array

        """
    def hstack(self, a: Incomplete | None = None, name: str = 'ar'):
        """stack lagpolynomial horizontally in 2d array

        """
    def stacksquare(self, a: Incomplete | None = None, name: str = 'ar', orientation: str = 'vertical'):
        """stack lagpolynomial vertically in 2d square array with eye

        """
    def vstackarma_minus1(self):
        """stack ar and lagpolynomial vertically in 2d array

        """
    def hstackarma_minus1(self):
        """stack ar and lagpolynomial vertically in 2d array

        this is the Kalman Filter representation, I think
        """
    areigenvalues: Incomplete
    def getisstationary(self, a: Incomplete | None = None):
        """check whether the auto-regressive lag-polynomial is stationary

        Returns
        -------
        isstationary : bool

        *attaches*

        areigenvalues : complex array
            eigenvalues sorted by absolute value

        References
        ----------
        formula taken from NAG manual

        """
    maeigenvalues: Incomplete
    def getisinvertible(self, a: Incomplete | None = None):
        """check whether the auto-regressive lag-polynomial is stationary

        Returns
        -------
        isinvertible : bool

        *attaches*

        maeigenvalues : complex array
            eigenvalues sorted by absolute value

        References
        ----------
        formula taken from NAG manual

        """
    def reduceform(self, apoly):
        """

        this assumes no exog, todo

        """
