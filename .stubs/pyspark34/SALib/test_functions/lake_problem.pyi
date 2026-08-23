import numpy as np
from _typeshed import Incomplete

FLOAT_OR_ARRAY: Incomplete

def lake_problem(X: FLOAT_OR_ARRAY, a: FLOAT_OR_ARRAY = 0.1, q: FLOAT_OR_ARRAY = 2.0, b: FLOAT_OR_ARRAY = 0.42, eps: FLOAT_OR_ARRAY = 0.02) -> float:
    '''Lake Problem as given in Hadka et al., (2015) and Kwakkel (2017)
    modified for use as a test function.

    The `mean` and `stdev` parameters control the log normal distribution of
    natural inflows (`epsilon` in [1] and [2]).

    References
    ----------
    .. [1] Hadka, D., Herman, J., Reed, P., Keller, K., (2015).
           "An open source framework for many-objective robust decision making."
           Environmental Modelling & Software 74, 114-129.
           doi:10.1016/j.envsoft.2015.07.014

    .. [2] Kwakkel, J.H, (2017). "The Exploratory Modeling Workbench: An open
           source toolkit for exploratory modeling, scenario discovery, and
           (multi-objective) robust decision making."
           Environmental Modelling & Software 96, 239-250.
           doi:10.1016/j.envsoft.2017.06.054

    .. [3] Singh, R., Reed, P., Keller, K., (2015). "Many-objective robust
           decision making for managing an ecosystem with a deeply uncertain
           threshold response."
           Ecology and Society 20.
           doi:10.5751/ES-07687-200312


    Parameters
    ----------
    X : float or np.ndarray
        normalized concentration of Phosphorus at point in time
    a : float or np.ndarray
        rate of anthropogenic pollution (0.0 to 0.1)
    q : float or np.ndarray
        exponent controlling recycling rate (2.0 to 4.5).
    b : float or np.ndarray
        decay rate for phosphorus
        (0.1 to 0.45, where default 0.42 is irreversible, as described in [1])
    eps : float or np.ndarray
        natural inflows of phosphorus (pollution), see [3]



    Returns
    -------
    float, phosphorus pollution for a point in time
    '''
def evaluate_lake(values: np.ndarray, seed: int = 101) -> np.ndarray:
    '''Evaluate the Lake Problem with an array of parameter values.

    References
    ----------
    .. [1] Hadka, D., Herman, J., Reed, P., Keller, K., (2015).
           "An open source framework for many-objective robust decision
           making."
           Environmental Modelling & Software 74, 114–129.
           doi:10.1016/j.envsoft.2015.07.014

    .. [2] Singh, R., Reed, P., Keller, K., (2015). "Many-objective robust
           decision making for managing an ecosystem with a deeply uncertain
           threshold response."
           Ecology and Society 20.
           doi:10.5751/ES-07687-200312

    Parameters
    ----------
    values : np.ndarray,
        model inputs in the (column) order of
        a, q, b, mean, stdev

        where
        * `a` is rate of anthropogenic pollution
        * `q` is exponent controlling recycling rate
        * `b` is decay rate for phosphorus
        * `mean` and
        * `stdev` set the log normal distribution of `eps`, see [2]

    Returns
    -------
    np.ndarray, of Phosphorus pollution over time `t`
    '''
def evaluate(values: np.ndarray, nvars: int = 100, seed: int = 101):
    """Evaluate the Lake Problem with an array of parameter values.

    Parameters
    ----------
    values : np.ndarray,
             model inputs in the (column) order of
             a, q, b, mean, stdev, delta, alpha

    nvars : int,
            number of decision variables to simulate (default: 100)


    Returns
    -------
    np.ndarray : max_P, utility, inertia, reliability
    """
