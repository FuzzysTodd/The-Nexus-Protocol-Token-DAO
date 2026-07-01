from _typeshed import Incomplete
from statsmodels.compat.python import lmap as lmap, lzip as lzip

def logsumexp(a, axis: Incomplete | None = None):
    """
    Compute the log of the sum of exponentials log(e^{a_1}+...e^{a_n}) of a

    Avoids numerical overflow.

    Parameters
    ----------
    a : array_like
        The vector to exponentiate and sum
    axis : int, optional
        The axis along which to apply the operation.  Defaults is None.

    Returns
    -------
    sum(log(exp(a)))

    Notes
    -----
    This function was taken from the mailing list
    http://mail.scipy.org/pipermail/scipy-user/2009-October/022931.html

    This should be superceded by the ufunc when it is finished.
    """
def discretize(X, method: str = 'ef', nbins: Incomplete | None = None):
    '''
    Discretize `X`

    Parameters
    ----------
    bins : int, optional
        Number of bins.  Default is floor(sqrt(N))
    method : str
        "ef" is equal-frequency binning
        "ew" is equal-width binning

    Examples
    --------
    '''
def logbasechange(a, b):
    """
    There is a one-to-one transformation of the entropy value from
    a log base b to a log base a :

    H_{b}(X)=log_{b}(a)[H_{a}(X)]

    Returns
    -------
    log_{b}(a)
    """
def natstobits(X):
    """
    Converts from nats to bits
    """
def bitstonats(X):
    """
    Converts from bits to nats
    """
def shannonentropy(px, logbase: int = 2):
    """
    This is Shannon's entropy

    Parameters
    ----------
    logbase, int or np.e
        The base of the log
    px : 1d or 2d array_like
        Can be a discrete probability distribution, a 2d joint distribution,
        or a sequence of probabilities.

    Returns
    -----
    For log base 2 (bits) given a discrete distribution
        H(p) = sum(px * log2(1/px) = -sum(pk*log2(px)) = E[log2(1/p(X))]

    For log base 2 (bits) given a joint distribution
        H(px,py) = -sum_{k,j}*w_{kj}log2(w_{kj})

    Notes
    -----
    shannonentropy(0) is defined as 0
    """
def shannoninfo(px, logbase: int = 2):
    """
    Shannon's information

    Parameters
    ----------
    px : float or array_like
        `px` is a discrete probability distribution

    Returns
    -------
    For logbase = 2
    np.log2(px)
    """
def condentropy(px, py, pxpy: Incomplete | None = None, logbase: int = 2):
    """
    Return the conditional entropy of X given Y.

    Parameters
    ----------
    px : array_like
    py : array_like
    pxpy : array_like, optional
        If pxpy is None, the distributions are assumed to be independent
        and conendtropy(px,py) = shannonentropy(px)
    logbase : int or np.e

    Returns
    -------
    sum_{kj}log(q_{j}/w_{kj}

    where q_{j} = Y[j]
    and w_kj = X[k,j]
    """
def mutualinfo(px, py, pxpy, logbase: int = 2):
    """
    Returns the mutual information between X and Y.

    Parameters
    ----------
    px : array_like
        Discrete probability distribution of random variable X
    py : array_like
        Discrete probability distribution of random variable Y
    pxpy : 2d array_like
        The joint probability distribution of random variables X and Y.
        Note that if X and Y are independent then the mutual information
        is zero.
    logbase : int or np.e, optional
        Default is 2 (bits)

    Returns
    -------
    shannonentropy(px) - condentropy(px,py,pxpy)
    """
def corrent(px, py, pxpy, logbase: int = 2):
    """
    An information theoretic correlation measure.

    Reflects linear and nonlinear correlation between two random variables
    X and Y, characterized by the discrete probability distributions px and py
    respectively.

    Parameters
    ----------
    px : array_like
        Discrete probability distribution of random variable X
    py : array_like
        Discrete probability distribution of random variable Y
    pxpy : 2d array_like, optional
        Joint probability distribution of X and Y.  If pxpy is None, X and Y
        are assumed to be independent.
    logbase : int or np.e, optional
        Default is 2 (bits)

    Returns
    -------
    mutualinfo(px,py,pxpy,logbase=logbase)/shannonentropy(py,logbase=logbase)

    Notes
    -----
    This is also equivalent to

    corrent(px,py,pxpy) = 1 - condent(px,py,pxpy)/shannonentropy(py)
    """
def covent(px, py, pxpy, logbase: int = 2):
    """
    An information theoretic covariance measure.

    Reflects linear and nonlinear correlation between two random variables
    X and Y, characterized by the discrete probability distributions px and py
    respectively.

    Parameters
    ----------
    px : array_like
        Discrete probability distribution of random variable X
    py : array_like
        Discrete probability distribution of random variable Y
    pxpy : 2d array_like, optional
        Joint probability distribution of X and Y.  If pxpy is None, X and Y
        are assumed to be independent.
    logbase : int or np.e, optional
        Default is 2 (bits)

    Returns
    -------
    condent(px,py,pxpy,logbase=logbase) + condent(py,px,pxpy,
            logbase=logbase)

    Notes
    -----
    This is also equivalent to

    covent(px,py,pxpy) = condent(px,py,pxpy) + condent(py,px,pxpy)
    """
def renyientropy(px, alpha: int = 1, logbase: int = 2, measure: str = 'R'):
    '''
    Renyi\'s generalized entropy

    Parameters
    ----------
    px : array_like
        Discrete probability distribution of random variable X.  Note that
        px is assumed to be a proper probability distribution.
    logbase : int or np.e, optional
        Default is 2 (bits)
    alpha : float or inf
        The order of the entropy.  The default is 1, which in the limit
        is just Shannon\'s entropy.  2 is Renyi (Collision) entropy.  If
        the string "inf" or numpy.inf is specified the min-entropy is returned.
    measure : str, optional
        The type of entropy measure desired.  \'R\' returns Renyi entropy
        measure.  \'T\' returns the Tsallis entropy measure.

    Returns
    -------
    1/(1-alpha)*log(sum(px**alpha))

    In the limit as alpha -> 1, Shannon\'s entropy is returned.

    In the limit as alpha -> inf, min-entropy is returned.
    '''
def gencrossentropy(px, py, pxpy, alpha: int = 1, logbase: int = 2, measure: str = 'T') -> None:
    """
    Generalized cross-entropy measures.

    Parameters
    ----------
    px : array_like
        Discrete probability distribution of random variable X
    py : array_like
        Discrete probability distribution of random variable Y
    pxpy : 2d array_like, optional
        Joint probability distribution of X and Y.  If pxpy is None, X and Y
        are assumed to be independent.
    logbase : int or np.e, optional
        Default is 2 (bits)
    measure : str, optional
        The measure is the type of generalized cross-entropy desired. 'T' is
        the cross-entropy version of the Tsallis measure.  'CR' is Cressie-Read
        measure.
    """
