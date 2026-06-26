from _typeshed import Incomplete

def evaluate(values, a: Incomplete | None = None, delta: Incomplete | None = None, alpha: Incomplete | None = None):
    """Modified Sobol G-function.

    Reverts to original Sobol G-function if delta and alpha are not given.

    .. [1] Saltelli, A., Annoni, P., Azzini, I., Campolongo, F., Ratto, M.,
           Tarantola, S., 2010. Variance based sensitivity analysis of model
           output. Design and estimator for the total sensitivity index.
           Computer Physics Communications 181, 259–270.
           https://doi.org/10.1016/j.cpc.2009.09.018

    Parameters
    ----------
    values : numpy.ndarray
        input variables
    a : numpy.ndarray
        parameter values
    delta : numpy.ndarray
        shift parameters
    alpha : numpy.ndarray
        curvature parameters

    Returns
    -------
    Y : Result of G-function
    """
def sensitivity_index(a, alpha: Incomplete | None = None): ...
def total_sensitivity_index(a, alpha: Incomplete | None = None): ...
