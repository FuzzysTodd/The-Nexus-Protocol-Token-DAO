from _typeshed import Incomplete

all_models: Incomplete
model_para: Incomplete
model_para_num: Incomplete
curve_combination_models: Incomplete

def vap(x, a, b, c):
    """Vapor pressure model

    Parameters
    ----------
    x : int
    a : float
    b : float
    c : float

    Returns
    -------
    float
        np.exp(a+b/x+c*np.log(x))
    """
def pow3(x, c, a, alpha):
    """pow3

    Parameters
    ----------
    x : int
    c : float
    a : float
    alpha : float

    Returns
    -------
    float
        c - a * x**(-alpha)
    """
def linear(x, a, b):
    """linear

    Parameters
    ----------
    x : int
    a : float
    b : float

    Returns
    -------
    float
        a*x + b
    """
def logx_linear(x, a, b):
    """logx linear

    Parameters
    ----------
    x : int
    a : float
    b : float

    Returns
    -------
    float
        a * np.log(x) + b
    """
def dr_hill_zero_background(x, theta, eta, kappa):
    """dr hill zero background

    Parameters
    ----------
    x : int
    theta : float
    eta : float
    kappa : float

    Returns
    -------
    float
        (theta* x**eta) / (kappa**eta + x**eta)
    """
def log_power(x, a, b, c):
    '''"logistic power

    Parameters
    ----------
    x : int
    a : float
    b : float
    c : float

    Returns
    -------
    float
        a/(1.+(x/np.exp(b))**c)
    '''
def pow4(x, alpha, a, b, c):
    """pow4

    Parameters
    ----------
    x : int
    alpha : float
    a : float
    b : float
    c : float

    Returns
    -------
    float
        c - (a*x+b)**-alpha
    """
def mmf(x, alpha, beta, kappa, delta):
    """Morgan-Mercer-Flodin
    http://www.pisces-conservation.com/growthhelp/index.html?morgan_mercer_floden.htm

    Parameters
    ----------
    x : int
    alpha : float
    beta : float
    kappa : float
    delta : float

    Returns
    -------
    float
        alpha - (alpha - beta) / (1. + (kappa * x)**delta)
    """
def exp4(x, c, a, b, alpha):
    """exp4

    Parameters
    ----------
    x : int
    c : float
    a : float
    b : float
    alpha : float

    Returns
    -------
    float
        c - np.exp(-a*(x**alpha)+b)
    """
def ilog2(x, c, a):
    """ilog2

    Parameters
    ----------
    x : int
    c : float
    a : float

    Returns
    -------
    float
        c - a / np.log(x)
    """
def weibull(x, alpha, beta, kappa, delta):
    """Weibull model
    http://www.pisces-conservation.com/growthhelp/index.html?morgan_mercer_floden.htm

    Parameters
    ----------
    x : int
    alpha : float
    beta : float
    kappa : float
    delta : float

    Returns
    -------
    float
        alpha - (alpha - beta) * np.exp(-(kappa * x)**delta)
    """
def janoschek(x, a, beta, k, delta):
    """http://www.pisces-conservation.com/growthhelp/janoschek.htm

    Parameters
    ----------
    x : int
    a : float
    beta : float
    k : float
    delta : float

    Returns
    -------
    float
        a - (a - beta) * np.exp(-k*x**delta)
    """
