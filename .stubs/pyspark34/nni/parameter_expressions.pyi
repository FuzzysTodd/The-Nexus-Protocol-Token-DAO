def choice(options, random_state):
    """
    options: 1-D array-like or int
    random_state: an object of numpy.random.RandomState
    """
def randint(lower, upper, random_state):
    """
    Generate a random integer from `lower` (inclusive) to `upper` (exclusive).
    lower: an int that represent an lower bound
    upper: an int that represent an upper bound
    random_state: an object of numpy.random.RandomState
    """
def uniform(low, high, random_state):
    """
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    random_state: an object of numpy.random.RandomState
    """
def quniform(low, high, q, random_state):
    """
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    q: sample step
    random_state: an object of numpy.random.RandomState
    """
def loguniform(low, high, random_state):
    """
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    random_state: an object of numpy.random.RandomState
    """
def qloguniform(low, high, q, random_state):
    """
    low: an float that represent an lower bound
    high: an float that represent an upper bound
    q: sample step
    random_state: an object of numpy.random.RandomState
    """
def normal(mu, sigma, random_state):
    """
    The probability density function of the normal distribution,
    first derived by De Moivre and 200 years later by both Gauss and Laplace independently.
    mu: float or array_like of floats
        Mean (“centre”) of the distribution.
    sigma: float or array_like of floats
           Standard deviation (spread or “width”) of the distribution.
    random_state: an object of numpy.random.RandomState
    """
def qnormal(mu, sigma, q, random_state):
    """
    mu: float or array_like of floats
    sigma: float or array_like of floats
    q: sample step
    random_state: an object of numpy.random.RandomState
    """
def lognormal(mu, sigma, random_state):
    """
    mu: float or array_like of floats
    sigma: float or array_like of floats
    random_state: an object of numpy.random.RandomState
    """
def qlognormal(mu, sigma, q, random_state):
    """
    mu: float or array_like of floats
    sigma: float or array_like of floats
    q: sample step
    random_state: an object of numpy.random.RandomState
    """
